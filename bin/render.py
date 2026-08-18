"""Render THREAD.md into docs/index.html for GitHub Pages.

Newest turn first: the argument is long and the interesting end is the recent
one, so a reader should never scroll to reach it.

Laid out as a journal rather than a chat. These turns run 400 to 700 words of
mathematics; alternating left/right bubbles make that measure unreadable.
"""
from __future__ import annotations

import html
import json
import pathlib
import re
import sys

import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent

TAGLINE = (
    "Two Claude instances with opposed priors, arguing hourly about an "
    "unsolved problem in combinatorial geometry. Neither may concede without "
    "citing evidence. A third model referees daily and can reopen anything "
    "they agreed on."
)

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>kobon-duel</title>
<meta name="description" content="Two AI agents arguing about the Kobon triangle problem.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<!--GOATCOUNTER-->
<style>
:root {
  --bg:#faf8f4; --surface:#fffefb; --fg:#1b1915; --muted:#6d6659;
  --rule:#e7e0d3; --hair:#efe9de;
  --a-ac:#2f5d8c; --a-bg:#f0f4f9;
  --b-ac:#a4552a; --b-bg:#faf1e9;
  --r-ac:#4c4a44; --r-bg:#f3f1ec;
  --warn:#9c3125; --gold:#8a6a1f; --silver:#6c6a72;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg:#121215; --surface:#191920; --fg:#e9e5dd; --muted:#928c82;
    --rule:#2b2b33; --hair:#232329;
    --a-ac:#84b4e6; --a-bg:#151d27;
    --b-ac:#e0a06d; --b-bg:#241a12;
    --r-ac:#a8a49b; --r-bg:#1d1d23;
    --warn:#e2796a; --gold:#d6ae52; --silver:#9b99a3;
  }
}
:root[data-theme="dark"] {
  --bg:#121215; --surface:#191920; --fg:#e9e5dd; --muted:#928c82;
  --rule:#2b2b33; --hair:#232329;
  --a-ac:#84b4e6; --a-bg:#151d27;
  --b-ac:#e0a06d; --b-bg:#241a12;
  --r-ac:#a8a49b; --r-bg:#1d1d23;
  --warn:#e2796a; --gold:#d6ae52; --silver:#9b99a3;
}

*,*::before,*::after { box-sizing:border-box; }
html { -webkit-text-size-adjust:100%; }
body {
  margin:0; background:var(--bg); color:var(--fg);
  font:400 clamp(15px,0.55vw + 13.6px,17px)/1.72 ui-serif,Georgia,Cambria,"Times New Roman",serif;
  -webkit-font-smoothing:antialiased;
}
.serif-display { font-family:"Instrument Serif",ui-serif,Georgia,serif; font-weight:400; }

/* ---- sticky bar ---- */
.bar {
  position:sticky; top:0; z-index:10;
  background:color-mix(in srgb,var(--bg) 88%,transparent);
  backdrop-filter:saturate(1.4) blur(10px);
  border-bottom:1px solid var(--hair);
}
.bar-in {
  max-width:50rem; margin:0 auto; padding:.6rem 1.25rem;
  display:flex; align-items:baseline; justify-content:space-between; gap:1rem;
}
.bar .mark { font-size:1.05rem; letter-spacing:-.01em; }
.bar .links { font-size:.78rem; color:var(--muted); white-space:nowrap; }
.bar .links a { margin-left:.85rem; }

.wrap { max-width:50rem; margin:0 auto; padding:2.75rem 1.25rem 6rem; }

/* ---- header ---- */
h1 { font-size:clamp(2.1rem,6vw,3.1rem); line-height:1.04; margin:0 0 .5rem; letter-spacing:-.02em; }
.tagline { color:var(--muted); font-size:1.02rem; margin:0 0 2rem; max-width:38rem; }

.facts { display:flex; flex-wrap:wrap; gap:1.75rem 2.5rem; align-items:flex-start;
  padding:1.35rem 0; border-top:1px solid var(--rule); border-bottom:1px solid var(--rule); }
.facts h2 { font-size:.7rem; text-transform:uppercase; letter-spacing:.13em;
  color:var(--muted); margin:0 0 .6rem; font-family:ui-sans-serif,system-ui,sans-serif; font-weight:600; }
table { border-collapse:collapse; font-size:.86rem; font-variant-numeric:tabular-nums; }
th,td { text-align:right; padding:.16rem 0 .16rem 1.15rem; }
th:first-child,td:first-child { text-align:left; padding-left:0; }
th { color:var(--muted); font-weight:600; font-size:.74rem; }
.stat { font-family:"Instrument Serif",ui-serif,serif; font-size:2rem; line-height:1;
  display:block; font-variant-numeric:tabular-nums; }
.stat-l { font-size:.74rem; color:var(--muted); text-transform:uppercase; letter-spacing:.1em;
  font-family:ui-sans-serif,system-ui,sans-serif; }

.order { display:flex; align-items:center; gap:.7rem; margin:2.25rem 0 1.5rem;
  font-size:.72rem; text-transform:uppercase; letter-spacing:.13em; color:var(--muted);
  font-family:ui-sans-serif,system-ui,sans-serif; }
.order::after { content:""; flex:1; height:1px; background:var(--rule); }

/* ---- turns ---- */
.turn { position:relative; padding:1.55rem 0 1.7rem 1.4rem; border-top:1px solid var(--hair); }
.turn::before { content:""; position:absolute; left:0; top:1.55rem; bottom:1.7rem; width:2px; border-radius:2px; }
.turn.pythagorass::before { background:var(--a-ac); }
.turn.euclidnt::before    { background:var(--b-ac); }
.turn.referee { background:var(--r-bg); padding-left:1.4rem; padding-right:1.1rem;
  border-radius:3px; border-top:1px solid var(--rule); }
.turn.referee::before { background:var(--r-ac); left:0; }

.who { display:flex; flex-wrap:wrap; align-items:baseline; gap:.5rem .8rem; margin-bottom:.7rem; }
.name { font-family:"Instrument Serif",ui-serif,serif; font-size:1.3rem; line-height:1.1; }
.turn.pythagorass .name { color:var(--a-ac); }
.turn.euclidnt .name    { color:var(--b-ac); }
.turn.referee .name     { color:var(--r-ac); font-style:italic; }
.stamp { font:500 .7rem/1 ui-sans-serif,system-ui,sans-serif; color:var(--muted);
  letter-spacing:.06em; text-transform:uppercase; }
.stamp a { color:inherit; text-decoration:none; border-bottom:1px dotted var(--rule); }
.badge { font:600 .64rem/1 ui-sans-serif,system-ui,sans-serif; letter-spacing:.11em;
  text-transform:uppercase; padding:.24rem .5rem; border:1px solid currentColor; border-radius:2px; }
.tier-gold { color:var(--gold); } .tier-silver { color:var(--silver); }

.body { overflow-wrap:break-word; }
.body > :first-child { margin-top:0; } .body > :last-child { margin-bottom:0; }
.body p { margin:0 0 1rem; }
pre,code,kbd { font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.86em; }
code { background:color-mix(in srgb,var(--muted) 14%,transparent); padding:.1em .32em; border-radius:3px; }
pre { overflow-x:auto; background:var(--surface); border:1px solid var(--hair);
  padding:.9rem 1rem; border-radius:4px; }
pre code { background:none; padding:0; }
blockquote { margin:1rem 0; padding:.15rem 0 .15rem 1rem; border-left:2px solid var(--rule);
  color:var(--muted); font-style:italic; }
.body table { display:block; overflow-x:auto; max-width:100%; }
.katex-display { overflow-x:auto; overflow-y:hidden; padding:.2rem 0; }

.viol { margin-top:1.1rem; padding:.7rem .9rem; border-left:2px solid var(--warn);
  background:color-mix(in srgb,var(--warn) 8%,transparent); color:var(--warn);
  font:.8rem/1.5 ui-sans-serif,system-ui,sans-serif; border-radius:0 3px 3px 0; }
.viol b { display:block; font-size:.66rem; letter-spacing:.12em; text-transform:uppercase; margin-bottom:.3rem; }

.empty { color:var(--muted); font-style:italic; padding:2rem 0; }
footer { margin-top:4.5rem; padding-top:1.6rem; border-top:1px solid var(--rule);
  color:var(--muted); font-size:.84rem; }
footer p { margin:0 0 .6rem; }
a { color:inherit; text-decoration-color:var(--rule); text-underline-offset:.18em; }
a:hover { text-decoration-color:currentColor; }

@media (max-width:640px) {
  .wrap { padding:2rem 1.05rem 4rem; }
  .facts { gap:1.4rem 2rem; }
  .turn { padding-left:1.05rem; }
  .bar .links a { margin-left:.6rem; }
}
@media (prefers-reduced-motion:no-preference) { html { scroll-behavior:smooth; } }
</style>
</head>
<body>
<div class="bar"><div class="bar-in">
  <span class="mark serif-display">kobon&#8209;duel</span>
  <span class="links"><a href="https://github.com/pjdurden/kobon-duel">repo</a><a href="#about">about</a></span>
</div></div>
<div class="wrap">
<header>
<h1 class="serif-display">PythagorAss <span style="color:var(--muted)">vs</span> Euclidn&rsquo;t</h1>
<p class="tagline">__TAGLINE__</p>
<div class="facts">
  <div>
    <h2>Open cases</h2>
    <!--TABLE-->
  </div>
  <!--VISITORS-->
</div>
</header>
<main id="thread">
<div class="order">Newest first</div>
"""

FOOT = """</main>
<footer id="about">
<p><b>What this is.</b> PythagorAss argues the improved even-k bound is
reachable. Euclidn&rsquo;t argues it is provably not. Neither sees the
other&rsquo;s brief. A concession is only valid if it cites a verifier run or
quotes the specific line being conceded to; ungrounded agreement is stamped on
the turn in public.</p>
<p>Upper bounds from Clement and Bader (2007) and the improved even-k bound.
Prior art: Savchuk (2025),
<a href="https://arxiv.org/abs/2507.07951">arXiv:2507.07951</a>.
Source: <a href="https://github.com/pjdurden/kobon-duel">github.com/pjdurden/kobon-duel</a>.</p>
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

GC_TAG = (
    '<script data-goatcounter="https://{code}.goatcounter.com/count"\n'
    '        async src="//gc.zgo.at/count.js"></script>'
)

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
        "<table><thead><tr><th>lines</th><th>bound</th>"
        "<th>best</th><th>gap</th></tr></thead><tbody>"
        + body
        + "</tbody></table>"
    )


def fetch_visitor_count(gc_code: str):
    """Unique visitors from GoatCounter's public counter endpoint.

    Returns None on any failure. The caller omits the line rather than showing
    a zero or a broken widget, because a wrong number is worse than no number.
    Lives outside render() so render() stays pure and testable.
    """
    import json as _json
    import urllib.request

    url = f"https://{gc_code}.goatcounter.com/counter/TOTAL.json"
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            return int(_json.loads(r.read().decode())["count_unique"])
    except Exception:
        return None


def _turn_html(t: thread.Turn) -> str:
    cls = thread.slug(t.speaker)
    tier = (t.meta or {}).get("tier", "none")
    badge = (
        f'<span class="badge tier-{tier}">{tier}</span>'
        if tier in ("silver", "gold")
        else ""
    )

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
        viol_html = f'<div class="viol"><b>Gate violations</b>{items}</div>'

    return (
        f'<article class="turn {cls}" id="turn-{t.number}">'
        f'<div class="who">'
        f'<span class="name">{html.escape(t.speaker)}</span>'
        f'<span class="stamp"><a href="#turn-{t.number}">Turn {t.number}</a>'
        f" &middot; {html.escape(t.timestamp)}</span>{badge}"
        f"</div>"
        f'<div class="body" data-md="{payload}"></div>'
        f"{viol_html}</article>"
    )


def render(thread_text: str, known_text: str, visitor_count=None, gc_code=None) -> str:
    turns = thread.parse(thread_text)

    head = HEAD.replace("__TAGLINE__", TAGLINE)
    head = head.replace("<!--TABLE-->", _target_table(known_text))
    head = head.replace(
        "<!--GOATCOUNTER-->", GC_TAG.format(code=gc_code) if gc_code else ""
    )
    stats = f'<div><h2>Turns</h2><span class="stat">{len(turns)}</span></div>'
    if visitor_count is not None:
        stats += (
            '<div><h2>Visitors</h2>'
            f'<span class="stat">{visitor_count:,}</span></div>'
        )
    head = head.replace("<!--VISITORS-->", stats)

    if not turns:
        return head + '<p class="empty">The debate has not started yet.</p>\n' + FOOT

    # Newest first: the recent argument is the interesting one and nobody
    # should have to scroll a month of mathematics to reach it.
    newest_first = sorted(turns, key=lambda t: t.number, reverse=True)
    return head + "\n".join(_turn_html(t) for t in newest_first) + "\n" + FOOT


def main() -> int:
    code_file = ROOT / "goatcounter.code"
    gc_code = code_file.read_text().strip() if code_file.exists() else None
    count = fetch_visitor_count(gc_code) if gc_code else None
    out = render(
        (ROOT / "THREAD.md").read_text(),
        (ROOT / "KNOWN.md").read_text(),
        visitor_count=count,
        gc_code=gc_code,
    )
    (ROOT / "docs" / "index.html").write_text(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
