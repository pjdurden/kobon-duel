"""Render THREAD.md into docs/index.html for GitHub Pages."""
from __future__ import annotations

import html
import json
import pathlib
import re
import sys

import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>kobon-duel</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<style>
:root {
  --bg: #fbfaf8; --fg: #1a1a18; --muted: #6b6b66; --line: #e2e0da;
  --con-bg: #eef4fb; --con-ac: #2f6fb5;
  --obs-bg: #fdf3e8; --obs-ac: #b5722f;
  --ref-bg: #f2f1ee; --ref-ac: #56564f;
  --warn: #b03a2e;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #16161a; --fg: #e8e6e1; --muted: #94938c; --line: #2c2c32;
    --con-bg: #16222f; --con-ac: #6aa8e8;
    --obs-bg: #2c2115; --obs-ac: #e0a05a;
    --ref-bg: #212127; --ref-ac: #a3a29a;
    --warn: #e5705f;
  }
}
:root[data-theme="dark"] {
  --bg: #16161a; --fg: #e8e6e1; --muted: #94938c; --line: #2c2c32;
  --con-bg: #16222f; --con-ac: #6aa8e8;
  --obs-bg: #2c2115; --obs-ac: #e0a05a;
  --ref-bg: #212127; --ref-ac: #a3a29a;
  --warn: #e5705f;
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--fg);
  font: 16px/1.65 ui-serif, Georgia, "Times New Roman", serif;
}
.wrap { max-width: 52rem; margin: 0 auto; padding: 3rem 1.25rem 6rem; }
header { border-bottom: 1px solid var(--line); padding-bottom: 1.75rem; margin-bottom: 2.5rem; }
h1 { font-size: 1.9rem; margin: 0 0 .4rem; letter-spacing: -.01em; }
.sub { color: var(--muted); margin: 0 0 1.5rem; font-size: .95rem; }
table { border-collapse: collapse; font-size: .88rem; width: 100%; max-width: 30rem; }
th, td { text-align: left; padding: .3rem .8rem .3rem 0; border-bottom: 1px solid var(--line); }
th { color: var(--muted); font-weight: 600; }
.turn { border-radius: 10px; padding: 1.1rem 1.3rem; margin: 0 0 1.5rem; border: 1px solid var(--line); }
.turn.constructor { background: var(--con-bg); border-left: 3px solid var(--con-ac); margin-right: 3rem; }
.turn.obstructor  { background: var(--obs-bg); border-left: 3px solid var(--obs-ac); margin-left: 3rem; }
.turn.referee     { background: var(--ref-bg); border-left: 3px solid var(--ref-ac); }
.meta-line { font: .74rem/1 ui-monospace, SFMono-Regular, Menlo, monospace;
  color: var(--muted); text-transform: uppercase; letter-spacing: .07em; margin-bottom: .8rem; }
.turn.constructor .meta-line { color: var(--con-ac); }
.turn.obstructor  .meta-line { color: var(--obs-ac); }
.badge { display: inline-block; padding: .1rem .45rem; border-radius: 4px;
  border: 1px solid currentColor; margin-left: .5rem; }
.tier-gold { color: #b8860b; } .tier-silver { color: #7d7d85; }
.viol { color: var(--warn); font-size: .84rem; border-top: 1px dashed var(--warn);
  margin-top: .9rem; padding-top: .6rem; }
.body :first-child { margin-top: 0; } .body :last-child { margin-bottom: 0; }
pre, code { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: .85em; }
pre { overflow-x: auto; background: rgba(127,127,127,.1); padding: .8rem; border-radius: 6px; }
blockquote { margin: .8rem 0; padding-left: .9rem; border-left: 2px solid var(--muted); color: var(--muted); }
footer { margin-top: 4rem; padding-top: 1.5rem; border-top: 1px solid var(--line);
  color: var(--muted); font-size: .85rem; }
a { color: inherit; }
</style>
</head>
<body>
<div class="wrap">
<header>
<h1>kobon-duel</h1>
<p class="sub">Two Claude sessions with opposed priors, arguing about the Kobon
triangle problem. They alternate hourly through an append-only file. A daily
referee rewrites the ledger and may reopen anything they agreed on. Neither can
declare a result; only the verifier can.</p>
<!--TABLE-->
</header>
<main id="thread">
"""

FOOT = """</main>
<footer>
<p>Source and full transcript:
<a href="https://github.com/pjdurden/kobon-duel">github.com/pjdurden/kobon-duel</a>.
Upper bounds from Clement and Bader (2007) and the improved even-k bound.
Prior art: Savchuk (2025), <a href="https://arxiv.org/abs/2507.07951">arXiv:2507.07951</a>.</p>
</footer>
</div>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script>
document.querySelectorAll("[data-md]").forEach(function (el) {
  el.innerHTML = marked.parse(JSON.parse(el.getAttribute("data-md")));
});
if (window.renderMathInElement) {
  renderMathInElement(document.body, {
    delimiters: [
      {left: "$$", right: "$$", display: true},
      {left: "\\\\[", right: "\\\\]", display: true},
      {left: "$", right: "$", display: false}
    ],
    throwOnError: false
  });
}
</script>
</body>
</html>
"""

OPEN_ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*\d+\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*OPEN\s*\|",
    re.MULTILINE,
)


def _target_table(known_text: str) -> str:
    """Build the header table from KNOWN.md so the site cannot drift from it."""
    rows = OPEN_ROW_RE.findall(known_text)
    if not rows:
        return ""
    body = "".join(
        f"<tr><td>{k}</td><td>{ub}</td><td>{best}</td>"
        f"<td>{int(ub) - int(best)}</td></tr>"
        for k, ub, best in rows
    )
    return (
        "<table><tr><th>k</th><th>best upper bound</th>"
        "<th>best known</th><th>gap</th></tr>" + body + "</table>"
    )


def _turn_html(t: thread.Turn) -> str:
    cls = t.speaker.lower()
    tier = (t.meta or {}).get("tier", "none")
    badge = ""
    if tier in ("silver", "gold"):
        badge = f'<span class="badge tier-{tier}">{tier}</span>'

    body, viol = t.body, []
    marker = "**Gate violations**"
    if marker in body:
        body, _, rest = body.partition(marker)
        viol = [
            ln.lstrip("- ").strip()
            for ln in rest.splitlines()
            if ln.strip().startswith("-")
        ]

    payload = html.escape(json.dumps(body.strip()), quote=True)
    viol_html = ""
    if viol:
        items = "".join(f"<div>{html.escape(v)}</div>" for v in viol)
        viol_html = f'<div class="viol">{items}</div>'

    return (
        f'<article class="turn {cls}">'
        f'<div class="meta-line">Turn {t.number} &middot; {html.escape(t.speaker)} '
        f'&middot; {html.escape(t.timestamp)}{badge}</div>'
        f'<div class="body" data-md="{payload}"></div>'
        f"{viol_html}</article>"
    )


def render(thread_text: str, known_text: str) -> str:
    turns = thread.parse(thread_text)
    head = HEAD.replace("<!--TABLE-->", _target_table(known_text))
    return head + "\n".join(_turn_html(t) for t in turns) + "\n" + FOOT


def main() -> int:
    out = render(
        (ROOT / "THREAD.md").read_text(),
        (ROOT / "KNOWN.md").read_text(),
    )
    (ROOT / "docs" / "index.html").write_text(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
