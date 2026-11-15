"""The four models. Model IDs and effort are fixed by the pre-registration (version 2).

No fallback models on purpose: a fallback would silently swap the model mid-study.
No temperature: every model runs at its default sampling.
"""
import json
import threading

import anthropic
import openai
from openai.types.chat import ChatCompletion

EFFORT = "medium"
MAX_TOKENS = 16000

MODELS = {
    "haiku": ("anthropic", "claude-haiku-5-5"),
    "sonnet": ("anthropic", "claude-sonnet-5-5"),
    "gpt": ("openai", "gpt-6.1-sol"),
    "opus": ("anthropic", "claude-opus-5-5"),
}
CHECKERS = ("haiku", "sonnet", "gpt")
CRITIC = "opus"

# USD per million tokens (input, output). Fill in from the providers' price pages before costing.
PRICES = {"haiku": None, "sonnet": None, "gpt": None, "opus": None}

API_ERRORS = (anthropic.APIError, openai.APIError)

_clients = {}
_lock = threading.Lock()


def _client(provider):
    with _lock:
        if provider not in _clients:
            if provider == "anthropic":
                _clients[provider] = anthropic.Anthropic(max_retries=8)
            else:
                _clients[provider] = openai.OpenAI(max_retries=8)
        return _clients[provider]


def call(name, prompt, schema):
    """One call with structured output.

    Returns the usage and either `data` (the parsed object) or a no-verdict:
    `refusal` if the model refused, `parse_failed` if the response was still
    unparseable after one retry. API errors raise, and the runner retries them later.
    """
    provider, model = MODELS[name]
    fn = _call_anthropic if provider == "anthropic" else _call_openai
    out = {"input_tokens": 0, "output_tokens": 0}
    for attempt in (1, 2):
        try:
            r = fn(model, prompt, schema)
        except API_ERRORS:
            if attempt == 1:
                raise
            r = fn(model, prompt, schema)  # the retry itself hit an API error: one more go, keeping the count and tokens
        out["input_tokens"] += r["input_tokens"]
        out["output_tokens"] += r["output_tokens"]
        out.update(model_returned=r["model_returned"], stop_reason=r["stop_reason"], attempts=attempt)
        status, data = interpret(r, schema)
        if status == "refusal":
            return {**out, "data": None, "refusal": True, "parse_failed": False}
        if status == "ok":
            return {**out, "data": data, "refusal": False, "parse_failed": False}
    return {**out, "data": None, "refusal": False, "parse_failed": True}


def interpret(r, schema):
    """One reply -> ("ok", the parsed object), ("refusal", None) or ("unparseable", None)."""
    if r["refusal"]:
        return "refusal", None
    try:
        data = json.loads(r["text"])
        if not isinstance(data, dict) or any(k not in data for k in schema["required"]):
            raise ValueError("missing fields")
        if "verdict" in schema["required"] and data["verdict"] not in ("safe", "unsafe"):
            raise ValueError("verdict outside safe/unsafe")
        return "ok", data
    except (ValueError, TypeError):
        return "unparseable", None


# The request for one call. The live call and the batch send exactly the same request.
def _anthropic_params(model, prompt, schema):
    return {
        "model": model,
        "max_tokens": MAX_TOKENS,
        "output_config": {"effort": EFFORT, "format": {"type": "json_schema", "schema": schema}},
        "messages": [{"role": "user", "content": prompt}],
    }


def _openai_body(model, prompt, schema):
    return {
        "model": model,
        "reasoning_effort": EFFORT,
        "max_completion_tokens": MAX_TOKENS,
        "messages": [{"role": "user", "content": prompt}],
        "response_format": {"type": "json_schema", "json_schema": {"name": "output", "strict": True, "schema": schema}},
    }


def _call_anthropic(model, prompt, schema):
    return _read_anthropic(_client("anthropic").messages.create(**_anthropic_params(model, prompt, schema)))


def _read_anthropic(r):
    return {
        "model_returned": r.model,
        "stop_reason": r.stop_reason,
        "input_tokens": r.usage.input_tokens,
        "output_tokens": r.usage.output_tokens,
        "refusal": r.stop_reason == "refusal",
        "text": "".join(b.text for b in r.content if b.type == "text"),
    }


def _call_openai(model, prompt, schema):
    return _read_openai(_client("openai").chat.completions.create(**_openai_body(model, prompt, schema)))


def _read_openai(r):
    msg = r.choices[0].message
    return {
        "model_returned": r.model,
        "stop_reason": r.choices[0].finish_reason,
        "input_tokens": r.usage.prompt_tokens,
        "output_tokens": r.usage.completion_tokens,
        "refusal": bool(getattr(msg, "refusal", None)),
        "text": msg.content or "",
    }


# Batches: the same requests, sent through each provider's batch service (half price, results within 24 hours).

class BatchFailed(Exception):
    """The provider rejected the whole batch (for example the model is not offered for batches)."""


def submit_batch(provider, requests):
    """Send one batch. `requests` is a list of (custom_id, model name, prompt, schema). Returns the batch id."""
    if provider == "anthropic":
        return _client("anthropic").messages.batches.create(requests=[
            {"custom_id": cid, "params": _anthropic_params(MODELS[name][1], text, schema)}
            for cid, name, text, schema in requests
        ]).id
    lines = "\n".join(
        json.dumps({"custom_id": cid, "method": "POST", "url": "/v1/chat/completions",
                    "body": _openai_body(MODELS[name][1], text, schema)})
        for cid, name, text, schema in requests
    )
    client = _client("openai")
    upload = client.files.create(file=("batch.jsonl", lines.encode()), purpose="batch")
    return client.batches.create(input_file_id=upload.id, endpoint="/v1/chat/completions", completion_window="24h").id


def poll_batch(provider, batch_id):
    """None while the batch is still running. Once it has ended, a list of (custom_id, reply, error):
    `reply` is what a live call returns before parsing, and `error` is set instead when that request failed.
    A request the provider did not answer (expired, cancelled) may be missing from the list.
    """
    if provider == "anthropic":
        client = _client("anthropic")
        if client.messages.batches.retrieve(batch_id).processing_status != "ended":
            return None
        rows = []
        for row in client.messages.batches.results(batch_id):
            if row.result.type == "succeeded":
                rows.append((row.custom_id, _read_anthropic(row.result.message), None))
            else:
                rows.append((row.custom_id, None, f"{row.result.type}: {getattr(row.result, 'error', '')}"[:300]))
        return rows
    client = _client("openai")
    batch = client.batches.retrieve(batch_id)
    if batch.status not in ("completed", "failed", "expired", "cancelled"):
        return None
    if batch.status == "failed":
        raise BatchFailed(str(batch.errors)[:500])
    rows = []
    for file_id in (batch.output_file_id, batch.error_file_id):
        if not file_id:
            continue
        for line in client.files.content(file_id).text.splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            response = row.get("response") or {}
            if row.get("error") or response.get("status_code") != 200:
                rows.append((row["custom_id"], None, json.dumps(row.get("error") or response.get("body"))[:300]))
                continue
            try:
                rows.append((row["custom_id"], _read_openai(ChatCompletion.model_validate(response["body"])), None))
            except Exception as e:  # one malformed row must not block the rest of the batch: it is retried
                rows.append((row["custom_id"], None, f"unreadable row: {type(e).__name__}: {str(e)[:200]}"))
    return rows
