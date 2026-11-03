"""The four judges. Model IDs and effort are fixed by the pre-registration.

No fallback models on purpose: a fallback would silently swap the judge mid-study.
No temperature: current Claude models reject it, so every judge runs at its default sampling.
"""
import json
import threading

import anthropic
import openai

from study.prompt import SCHEMA

EFFORT = "medium"
MAX_TOKENS = 16000

JUDGES = {
    "haiku-5-5": ("anthropic", "claude-haiku-5-5"),
    "sonnet-5-5": ("anthropic", "claude-sonnet-5-5"),
    "opus-5-5": ("anthropic", "claude-opus-5-5"),
    "gpt-5-5": ("openai", "gpt-5.5"),
}

# USD per million tokens (input, output). Fill in gpt-5.5 from OpenAI's price page before estimating.
PRICES = {
    "haiku-5-5": (0.10, 0.50),
    "sonnet-5-5": (2.00, 10.00),
    "opus-5-5": (4.00, 20.00),
    "gpt-5-5": None,
}

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


def judge(name, prompt):
    provider, model = JUDGES[name]
    if provider == "anthropic":
        return _call_anthropic(model, prompt)
    return _call_openai(model, prompt)


def _call_anthropic(model, prompt):
    r = _client("anthropic").messages.create(
        model=model,
        max_tokens=MAX_TOKENS,
        output_config={"effort": EFFORT, "format": {"type": "json_schema", "schema": SCHEMA}},
        messages=[{"role": "user", "content": prompt}],
    )
    out = {
        "model_returned": r.model,
        "stop_reason": r.stop_reason,
        "input_tokens": r.usage.input_tokens,
        "output_tokens": r.usage.output_tokens,
    }
    if r.stop_reason == "refusal":
        return {**out, "verdict": None, "reason": None, "refusal": True}
    text = "".join(b.text for b in r.content if b.type == "text")
    data = json.loads(text)
    return {**out, "verdict": data["verdict"], "reason": data["reason"], "refusal": False}


def _call_openai(model, prompt):
    r = _client("openai").chat.completions.create(
        model=model,
        reasoning_effort=EFFORT,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_schema", "json_schema": {"name": "verdict", "strict": True, "schema": SCHEMA}},
    )
    msg = r.choices[0].message
    out = {
        "model_returned": r.model,
        "stop_reason": r.choices[0].finish_reason,
        "input_tokens": r.usage.prompt_tokens,
        "output_tokens": r.usage.completion_tokens,
    }
    if getattr(msg, "refusal", None):
        return {**out, "verdict": None, "reason": None, "refusal": True}
    data = json.loads(msg.content)
    return {**out, "verdict": data["verdict"], "reason": data["reason"], "refusal": False}
