"""Builds paper/report.pdf from REPORT.md: Markdown to HTML with the `markdown` package, then
Chrome's print-to-PDF. Set CHROME to the browser's path if it is not in the usual place.

    poetry run python paper/build_pdf.py
"""

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

CSS = """
@page { size: A4; margin: 24mm 25mm 24mm; }
body { font-family: Charter, "Bitstream Charter", "Times New Roman", Times, serif; font-size: 11pt;
       line-height: 1.42; color: #111; }
h1 { font-size: 19pt; line-height: 1.2; text-align: center; margin: 6pt 0 10pt; }
h1 + p, h1 + p + p { text-align: center; margin-bottom: 5pt; }
h1 + p + p { margin-bottom: 16pt; }
/* A heading claims room below itself (padding cancelled by a negative margin), so a section
   only starts on a page that has about a third of a page left; otherwise it moves to the next page. */
h2 { font-size: 13pt; margin: 18pt 0 calc(6pt - 65mm); padding-bottom: 65mm; break-inside: avoid; break-after: avoid; }
h3 { font-size: 11pt; margin: 13pt 0 calc(4pt - 35mm); padding-bottom: 35mm; break-inside: avoid; break-after: avoid; }
p { margin: 0 0 7pt; text-align: justify; hyphens: auto; orphans: 3; widows: 3; }
p.short { break-inside: avoid; }
li { margin-bottom: 3pt; text-align: justify; hyphens: auto; break-inside: avoid; }
ul, ol { padding-left: 18pt; margin: 0 0 7pt; }
img { max-width: 100%; display: block; margin: 8pt auto 4pt; break-inside: avoid; }
p:has(> img) { break-inside: avoid; break-after: avoid; }
p:has(> img) + p { font-size: 9.3pt; text-align: left; margin: 0 0 11pt; }
table { border-collapse: collapse; margin: 8pt 0 11pt; font-size: 9.3pt; line-height: 1.35; width: 100%;
        break-inside: avoid; border-top: 1px solid #111; border-bottom: 1px solid #111; }
th, td { padding: 3pt 7pt; text-align: left; vertical-align: top; }
th { border-bottom: 0.6px solid #111; }
blockquote { margin: 5pt 0 8pt; padding: 0 14pt; font-size: 9.5pt; break-inside: avoid; }
blockquote:has(table) { padding: 0; font-size: inherit; break-inside: auto; }
blockquote:has(table) p, h3 + p:has(+ p > img), h2 + p:has(+ h3), h2 + p:has(+ p > img), p:not(p:has(> img) + p):has(+ blockquote) { break-after: avoid; }  /* keep a lead line with what follows */
blockquote:has(table) table { break-inside: auto; }  /* the terms box may run over a page, row by row */
tr { break-inside: avoid; }
code { font-family: Menlo, monospace; font-size: 8.6pt; }
td code { white-space: nowrap; }
pre { margin: 6pt 0 10pt; padding: 0 14pt; white-space: pre-wrap; break-inside: avoid; }
pre code { font-size: 7.8pt; }
a { color: #1a4f9c; text-decoration: none; }
"""


def main():
    text = (ROOT / "REPORT.md").read_text().replace("\\\n", "  \n")  # backslash line breaks
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    # A paragraph too short to split with three lines on each side of the break stays in one piece.
    body = re.sub(r"<p>((?:(?!</p>).)*)</p>", lambda m: m.group(0) if len(re.sub(r"<[^>]+>", "", m.group(1))) > 520
                  else f'<p class="short">{m.group(1)}</p>', body, flags=re.S)
    title = text.splitlines()[0].lstrip("# ").strip()
    html = (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><base href='{ROOT.as_uri()}/'>"
            f"<title>{title}</title><style>{CSS}</style></head><body>{body}</body></html>")
    out = ROOT / "paper" / "report.pdf"
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "report.html"
        page.write_text(html)
        done = subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files",
                               f"--print-to-pdf={out}", page.as_uri()], capture_output=True, text=True)
    if done.returncode or not out.exists():
        sys.exit(f"Chrome failed: {done.stderr[-500:]}")
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
