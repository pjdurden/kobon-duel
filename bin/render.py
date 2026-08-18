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

import diagram
import thread

ROOT = pathlib.Path(__file__).resolve().parent.parent

TAGLINE = (
    "Two Claude instances with opposed priors, arguing hourly about an "
    "unsolved problem in combinatorial geometry. Neither may concede without "
    "citing evidence. A third model referees daily and can reopen anything "
    "they agreed on."
)

HEAD = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>kobon-duel</title>
<meta name="description" content="Two AI agents arguing about an unsolved problem in combinatorial geometry.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<!--GOATCOUNTER-->
<style>
:root{
  --bg:#f0eee9; --panel:#e9e6e0; --surface:#ffffff; --sent:#eef2f7;
  --text:#1f1e1c; --dim:#6b665e; --faint:#8d887f;
  --border:#e0dcd3; --line:#d6d1c6;
  --p-color:#2f6098; --e-color:#b0552a; --r-color:#5c5a54;
  --warn:#9c3125; --gold:#8a6a1f; --silver:#6c6a72;
  --shadow:0 1px 2px rgba(30,25,15,.05),0 4px 14px rgba(30,25,15,.05);
  --serif:"Source Serif 4",ui-serif,Georgia,Cambria,serif;
  --display:"Instrument Serif",ui-serif,Georgia,serif;
  --sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#1a1a19; --panel:#141413; --surface:#262625; --sent:#2b3037;
  --text:#efece6; --dim:#a39e95; --faint:#847f77;
  --border:#383734; --line:#302f2c;
  --p-color:#8ab9ea; --e-color:#e5a26a; --r-color:#a8a49c;
  --warn:#e58474; --gold:#d5ad51; --silver:#9b99a3;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 14px rgba(0,0,0,.22);
}}
:root[data-theme="dark"]{
  --bg:#1a1a19; --panel:#141413; --surface:#262625; --sent:#2b3037;
  --text:#efece6; --dim:#a39e95; --faint:#847f77;
  --border:#383734; --line:#302f2c;
  --p-color:#8ab9ea; --e-color:#e5a26a; --r-color:#a8a49c;
  --warn:#e58474; --gold:#d5ad51; --silver:#9b99a3;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 14px rgba(0,0,0,.22);
}

*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);
  font:400 clamp(15px,.35vw + 14px,16.5px)/1.66 var(--serif);
  -webkit-font-smoothing:antialiased}

/* ---------- bar ---------- */
.bar{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 88%,transparent);
  backdrop-filter:saturate(1.5) blur(12px);border-bottom:1px solid var(--border)}
.bar-in{max-width:60rem;margin:0 auto;padding:.6rem 1.4rem;display:flex;
  align-items:center;justify-content:space-between;gap:1rem}
.brand{font-family:var(--display);font-size:1.1rem;white-space:nowrap}
.brand .dot{display:inline-block;width:.4rem;height:.4rem;border-radius:50%;
  background:var(--e-color);margin-right:.4rem;vertical-align:.08em}
.repo{display:inline-flex;align-items:center;gap:.42rem;font:500 .76rem/1 var(--sans);
  color:var(--dim);text-decoration:none;padding:.38rem .66rem;border:1px solid var(--border);
  border-radius:99px;background:var(--surface);white-space:nowrap;transition:.15s}
.repo:hover{color:var(--text);border-color:var(--faint)}
.repo svg{width:.9rem;height:.9rem;flex:none}
.repo .full{display:inline}.repo .short{display:none}
@media (max-width:620px){.repo .full{display:none}.repo .short{display:inline}}

.wrap{max-width:60rem;margin:0 auto;padding:2.8rem 1.4rem 4rem}

/* ---------- masthead ---------- */
.kicker{font:600 .68rem/1 var(--sans);letter-spacing:.17em;text-transform:uppercase;
  color:var(--faint);margin:0 0 1rem}
h1{font-family:var(--display);font-weight:400;font-size:clamp(2.3rem,7vw,3.9rem);
  line-height:1;letter-spacing:-.015em;margin:0}
h1 .vs{display:block;font-style:italic;font-size:.42em;color:var(--faint);margin:.2em 0 .08em}
h1 .a{color:var(--p-color)} h1 .b{color:var(--e-color)}
.lede{margin:1.4rem 0 0;max-width:34em;font-size:1.02rem;color:var(--dim)}

.sec{display:flex;align-items:center;gap:.9rem;margin:2.9rem 0 1.2rem;
  font:600 .68rem/1 var(--sans);letter-spacing:.17em;text-transform:uppercase;color:var(--faint)}
.sec::after{content:"";flex:1;height:1px;background:var(--line)}

/* ---------- problem ---------- */
.problem p{margin:0 0 1rem;max-width:36em}
.problem p:last-child{margin-bottom:0}
.problem b{font-weight:600}
.figure{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem;margin:1.7rem 0 0}
.panel{margin:0}
.plot{aspect-ratio:1/1;border:1px solid var(--border);border-radius:10px;background:var(--surface);
  padding:.6rem;color:var(--dim);display:flex;box-shadow:var(--shadow)}
.panel-open .plot{border-style:dashed}
figcaption{margin-top:.55rem;font:.77rem/1.35 var(--sans);display:flex;flex-direction:column}
figcaption b{font-weight:600}figcaption span{color:var(--faint)}
.panel-open figcaption b{color:var(--e-color)}
@media (max-width:560px){.figure{grid-template-columns:repeat(2,minmax(0,1fr))}
  .panel:last-child{grid-column:1/-1}.panel:last-child .plot{aspect-ratio:2/1}}

/* ---------- facts ---------- */
.facts{display:flex;flex-wrap:wrap;gap:1.8rem 3rem;align-items:flex-start;margin-top:1.9rem;
  padding:1.4rem 1.5rem;background:var(--surface);border:1px solid var(--border);
  border-radius:12px;box-shadow:var(--shadow)}
.facts h2{font:600 .68rem/1 var(--sans);letter-spacing:.13em;text-transform:uppercase;
  color:var(--faint);margin:0 0 .7rem}
table{border-collapse:collapse;font-size:.86rem;font-variant-numeric:tabular-nums lining-nums}
th,td{text-align:right;padding:.18rem 0 .18rem 1.2rem}
th:first-child,td:first-child{text-align:left;padding-left:0}
th{color:var(--faint);font-weight:600;font-size:.73rem;font-family:var(--sans)}
tbody td:last-child{color:var(--e-color);font-weight:600}
.stat{font-family:var(--display);font-size:2.3rem;line-height:.9;display:block;
  font-variant-numeric:tabular-nums lining-nums}

/* ---------- chat ---------- */
.chat-wrap{position:relative;margin-top:.2rem}
.chat{height:clamp(430px,74vh,900px);overflow-y:auto;overscroll-behavior:contain;
  background:var(--panel);border:1px solid var(--border);border-radius:14px;
  padding:1.4rem 1.2rem 1.6rem;scroll-behavior:auto}
.stream{display:flex;flex-direction:column;gap:1.4rem}

.msg{display:flex;gap:.7rem;align-items:flex-start;max-width:100%}
.msg.right{flex-direction:row-reverse}
.msg.center{justify-content:center}

.avatar{flex:none;width:1.85rem;height:1.85rem;border-radius:50%;display:grid;place-items:center;
  font:600 .74rem/1 var(--sans);color:#fff;margin-top:.15rem;user-select:none}
.msg.pythagorass .avatar{background:var(--p-color)}
.msg.euclidnt .avatar{background:var(--e-color)}
.msg.referee .avatar{background:var(--r-color)}

.bubble{background:var(--surface);border:1px solid var(--border);border-radius:14px;
  padding:.95rem 1.15rem 1.05rem;box-shadow:var(--shadow);max-width:min(88%,42rem);min-width:0}
.msg.left  .bubble{border-top-left-radius:5px}
.msg.right .bubble{border-top-right-radius:5px;background:var(--sent)}
.msg.center .bubble{max-width:min(96%,48rem);background:transparent;border-style:dashed;
  box-shadow:none}

.meta{display:flex;flex-wrap:wrap;align-items:baseline;gap:.3rem .6rem;margin-bottom:.6rem;
  padding-bottom:.5rem;border-bottom:1px solid var(--line)}
.msg.right .meta{flex-direction:row-reverse}
.msg.center .meta{justify-content:center}
.name{font-family:var(--display);font-size:1.14rem;line-height:1.1}
.msg.pythagorass .name{color:var(--p-color)}
.msg.euclidnt .name{color:var(--e-color)}
.msg.referee .name{color:var(--r-color);font-style:italic}
.stamp{font:500 .69rem/1 var(--sans);color:var(--faint);letter-spacing:.04em}
.stamp a{color:inherit;text-decoration:none}.stamp a:hover{color:var(--text)}
.badge{font:600 .61rem/1 var(--sans);letter-spacing:.11em;text-transform:uppercase;
  padding:.26rem .46rem;border:1px solid currentColor;border-radius:3px}
.tier-gold{color:var(--gold)}.tier-silver{color:var(--silver)}

.body{overflow-wrap:break-word;min-width:0}
.body>:first-child{margin-top:0}.body>:last-child{margin-bottom:0}
.body p{margin:0 0 .95rem}
code,kbd{font-family:var(--mono);font-size:.86em}
code{background:color-mix(in srgb,var(--dim) 16%,transparent);padding:.12em .34em;border-radius:3px}
pre{overflow-x:auto;background:var(--bg);border:1px solid var(--border);padding:.9rem 1rem;
  border-radius:6px;font-family:var(--mono);font-size:.86em}
pre code{background:none;padding:0}
blockquote{margin:1rem 0;padding:.2rem 0 .2rem 1rem;border-left:2px solid var(--line);
  color:var(--dim);font-style:italic}
.body table{display:block;overflow-x:auto;max-width:100%}
.katex-display{overflow-x:auto;overflow-y:hidden;padding:.2rem 0}

.viol{margin-top:1rem;padding:.7rem .9rem;border-left:2px solid var(--warn);
  background:color-mix(in srgb,var(--warn) 9%,transparent);color:var(--warn);
  font:.78rem/1.5 var(--sans);border-radius:0 5px 5px 0}
.viol b{display:block;font-size:.64rem;letter-spacing:.13em;text-transform:uppercase;margin-bottom:.3rem}

.jump{position:absolute;left:50%;bottom:1.1rem;transform:translateX(-50%) translateY(.4rem);
  background:var(--surface);color:var(--text);border:1px solid var(--border);border-radius:99px;
  padding:.44rem .95rem;font:600 .73rem/1 var(--sans);box-shadow:var(--shadow);cursor:pointer;
  opacity:0;pointer-events:none;transition:opacity .18s,transform .18s}
.jump.show{opacity:1;pointer-events:auto;transform:translateX(-50%) translateY(0)}

.empty{color:var(--faint);font-style:italic;padding:2rem;text-align:center}
footer{margin-top:2.6rem;padding-top:1.6rem;border-top:1px solid var(--line);
  color:var(--dim);font-size:.85rem;max-width:42em}
footer p{margin:0 0 .7rem}footer b{color:var(--text);font-weight:600}
a{color:inherit;text-decoration-color:var(--line);text-underline-offset:.18em}
a:hover{text-decoration-color:currentColor}
@media (max-width:600px){
  .wrap{padding:2.1rem 1.05rem 3rem}
  .chat{padding:1.1rem .85rem 1.3rem;border-radius:12px}
  .bubble{max-width:calc(100% - 2.5rem)}
  .facts{padding:1.2rem}
}
</style>
</head>
<body>
<div class="bar"><div class="bar-in">
  <span class="brand"><span class="dot"></span>kobon&#8209;duel</span>
  <a class="repo" href="https://github.com/pjdurden/kobon-duel">
    <svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
    <span class="full">github.com/pjdurden/kobon-duel</span><span class="short">repo</span>
  </a>
</div></div>
<div class="wrap">
<header>
<p class="kicker">An unsolved problem, argued hourly</p>
<h1><span class="a">PythagorAss</span><span class="vs">versus</span><span class="b">Euclidn&rsquo;t</span></h1>
<p class="lede">__TAGLINE__</p>
</header>

<section class="problem">
<div class="sec">The problem</div>
__PROBLEM__
__FIGURE__
</section>

<div class="facts">
  <div><h2>Open cases</h2><!--TABLE--></div>
  <!--VISITORS-->
</div>

<div class="sec">The argument</div>
<div class="chat-wrap">
<div class="chat" id="chat"><div class="stream" id="stream">
'''

PROBLEM = '''<p>Draw <b>k</b> straight lines across a plane. Wherever three of them
enclose a region that no other line cuts through, you get a triangle. Because
no line passes through them, these triangles never overlap. The question is
simply: <b>how many can you force?</b></p>

<p>Three lines give you one. Five lines arranged as a pentagram give you five,
and five is provably the most five lines can do. The counts climb from there,
and for most k the exact answer is settled. For three values it is not.</p>

<p>At <b>14, 18 and 20 lines</b>, the best arrangement anyone has ever built
falls exactly <b>one triangle short</b> of the ceiling that has been proven.
Nobody knows whether the missing triangle is out there or whether the ceiling
is simply wrong. Closing any one of the three means either drawing the
arrangement or proving it cannot exist.</p>

<p>That single triangle is what these two are arguing about.</p>'''

FOOT = r'''</div></div>
<button class="jump" id="jump" type="button">Jump to latest &darr;</button>
</div>

<footer id="about">
<p><b>How it works.</b> PythagorAss argues the ceiling is reachable and hunts
constructions. Euclidn&rsquo;t argues there is a counting obstruction nobody has
isolated. Neither sees the other&rsquo;s brief. A concession is only valid if it
cites a verifier run or quotes the specific line being conceded to, and
ungrounded agreement is stamped onto the turn in public. A referee on a stronger
model rewrites the ledger daily and can reopen anything they agreed on. Neither
debater can declare a result.</p>
<p><b>Sources.</b> Upper bounds from Clement and Bader (2007) and the improved
even-k bound. Prior art: Savchuk (2025),
<a href="https://arxiv.org/abs/2507.07951">arXiv:2507.07951</a>, which closed
k=23 and k=27 by SAT and proved k=11 unreachable. The diagrams above are
generated from exact rational arithmetic, not drawn by hand.</p>
<p><a href="https://github.com/pjdurden/kobon-duel">github.com/pjdurden/kobon-duel</a></p>
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
      {left: "\\[", right: "\\]", display: true},
      {left: "$", right: "$", display: false}
    ],
    throwOnError: false
  });
}
(function () {
  var chat = document.getElementById("chat"), jump = document.getElementById("jump");
  if (!chat) return;
  function toBottom(smooth) {
    chat.scrollTo({ top: chat.scrollHeight, behavior: smooth ? "smooth" : "auto" });
  }
  function atBottom() {
    return chat.scrollHeight - chat.scrollTop - chat.clientHeight < 90;
  }
  // Land on the newest turn. Fonts and KaTeX change height after paint, so
  // settle again once they have.
  toBottom(false);
  window.addEventListener("load", function () { toBottom(false); });
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { toBottom(false); });
  }
  chat.addEventListener("scroll", function () {
    jump.classList.toggle("show", !atBottom());
  }, { passive: true });
  jump.addEventListener("click", function () { toBottom(true); });
  // A deep link to a turn should win over the auto-scroll.
  if (location.hash && document.querySelector(location.hash)) {
    document.querySelector(location.hash).scrollIntoView({ block: "center" });
  }
})();
</script>
</body>
</html>
'''

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
    side = {"PythagorAss": "left", "Euclidn't": "right"}.get(t.speaker, "center")
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
        f'<article class="msg {side} {cls}" id="turn-{t.number}">'
        f'<div class="avatar" aria-hidden="true">{html.escape(t.speaker[0])}</div>'
        f'<div class="bubble">'
        f'<div class="meta"><span class="name">{html.escape(t.speaker)}</span>'
        f'<span class="stamp"><a href="#turn-{t.number}">Turn {t.number}</a>'
        f" &middot; {html.escape(t.timestamp)}</span>{badge}</div>"
        f'<div class="body" data-md="{payload}"></div>'
        f"{viol_html}</div></article>"
    )


def render(thread_text: str, known_text: str, visitor_count=None, gc_code=None) -> str:
    turns = thread.parse(thread_text)

    head = HEAD.replace("__TAGLINE__", TAGLINE)
    head = head.replace("__PROBLEM__", PROBLEM)
    head = head.replace("__FIGURE__", diagram.figure())
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

    # Chat order: oldest at the top, newest at the bottom. The panel scrolls
    # itself to the newest turn on load, so nobody has to hunt for the live
    # argument even though it lives at the end.
    ordered = sorted(turns, key=lambda t: t.number)
    return head + "\n".join(_turn_html(t) for t in ordered) + "\n" + FOOT


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
