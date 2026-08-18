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
<meta name="color-scheme" content="light">
<title>kobon-duel</title>
<meta name="description" content="Two AI agents arguing about an unsolved problem in combinatorial geometry.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,300;6..72,400;6..72,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<!--GOATCOUNTER-->
<style>
/* Light only, on purpose. The palette is Anthropic's: ivory ground, white
   cards, slate text, book-cloth clay accent. No prefers-color-scheme block:
   a dark override is what made this render dark on a dark-mode machine. */
:root{
  color-scheme:light;
  --bg:#f0eee6; --card:#ffffff; --card-2:#faf9f5; --sunk:#e8e5da;
  --text:#191919; --dim:#6a6a68; --faint:#93938d;
  --border:#e0ddd0; --line:#e8e5da;
  --clay:#cc785c; --kraft:#d4a27f; --manilla:#ebdbbc;
  --p-color:#4f6b7d; --p-bg:#eef1f4; --p-edge:#dbe2e8;
  --e-color:#bf6446; --e-bg:#faece5; --e-edge:#f0d9cd;
  --r-color:#6a6a68; --r-bg:#f3f2ed; --r-edge:#e2e0d6;
  --warn:#a2493a; --warn-bg:#fbeeeb; --gold:#8f6d29; --silver:#77747c;
  --shadow:0 1px 2px rgba(25,25,25,.04),0 4px 16px rgba(25,25,25,.045);
  --serif:"Newsreader",ui-serif,Georgia,Cambria,serif;
  --sans:"Inter",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}

*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);
  font:400 clamp(15px,.3vw + 14.2px,16.5px)/1.68 var(--sans);
  -webkit-font-smoothing:antialiased;letter-spacing:-.003em}

.bar{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 88%,transparent);
  backdrop-filter:saturate(1.4) blur(12px);border-bottom:1px solid var(--border)}
.bar-in{max-width:53rem;margin:0 auto;padding:.62rem 1.4rem;display:flex;
  align-items:center;justify-content:space-between;gap:1rem}
.brand{font-family:var(--serif);font-size:1.16rem;font-weight:400;white-space:nowrap}
.brand .dot{display:inline-block;width:.42rem;height:.42rem;border-radius:50%;
  background:var(--clay);margin-right:.42rem;vertical-align:.1em}
.repo{display:inline-flex;align-items:center;gap:.42rem;font:500 .78rem/1 var(--sans);
  color:var(--dim);text-decoration:none;padding:.4rem .7rem;border:1px solid var(--border);
  border-radius:8px;background:var(--card);white-space:nowrap;transition:.15s}
.repo:hover{color:var(--text);border-color:var(--faint)}
.repo svg{width:.9rem;height:.9rem;flex:none}
.repo .full{display:inline}.repo .short{display:none}
@media (max-width:620px){.repo .full{display:none}.repo .short{display:inline}}

.wrap{max-width:53rem;margin:0 auto;padding:3.2rem 1.4rem 5rem}

.kicker{font:500 .78rem/1 var(--sans);letter-spacing:.01em;color:var(--clay);margin:0 0 1.1rem}
h1{font-family:var(--serif);font-weight:400;font-size:clamp(2.5rem,7.5vw,4.2rem);
  line-height:1.02;letter-spacing:-.022em;margin:0}
h1 .vs{display:block;font-style:italic;font-weight:300;font-size:.4em;
  color:var(--faint);letter-spacing:-.01em;margin:.14em 0 .06em}
h1 .a{color:var(--p-color)} h1 .b{color:var(--e-color)}
.lede{margin:1.5rem 0 0;max-width:36em;font-size:1.08rem;line-height:1.6;color:var(--dim)}

.sec{font:500 .8rem/1 var(--sans);letter-spacing:.01em;color:var(--clay);
  margin:3.2rem 0 1.3rem;padding-bottom:.7rem;border-bottom:1px solid var(--border)}

.problem p{margin:0 0 1.05rem;max-width:37em}
.problem p:last-child{margin-bottom:0}
.problem b{font-weight:600}
.figure{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem;margin:1.9rem 0 0}
.panel{margin:0}
.plot{aspect-ratio:1/1;border:1px solid var(--border);border-radius:12px;background:var(--card);
  padding:.7rem;color:var(--dim);display:flex;box-shadow:var(--shadow)}
.panel-open .plot{background:var(--e-bg);border-color:var(--e-edge);border-style:dashed}
figcaption{margin-top:.6rem;font:.79rem/1.35 var(--sans);display:flex;flex-direction:column;gap:.05rem}
figcaption b{font-weight:600}figcaption span{color:var(--faint)}
.panel-open figcaption b{color:var(--e-color)}
@media (max-width:560px){.figure{grid-template-columns:repeat(2,minmax(0,1fr))}
  .panel:last-child{grid-column:1/-1}.panel:last-child .plot{aspect-ratio:2/1}}

.facts{display:flex;flex-wrap:wrap;gap:1.9rem 3.2rem;align-items:flex-start;margin-top:2rem;
  padding:1.5rem 1.7rem;background:var(--card);border:1px solid var(--border);
  border-radius:14px;box-shadow:var(--shadow)}
.facts h2{font:500 .76rem/1 var(--sans);color:var(--faint);margin:0 0 .8rem}
table{border-collapse:collapse;font-size:.87rem;font-variant-numeric:tabular-nums lining-nums}
th,td{text-align:right;padding:.2rem 0 .2rem 1.25rem}
th:first-child,td:first-child{text-align:left;padding-left:0}
th{color:var(--faint);font-weight:500;font-size:.76rem}
tbody td:last-child{color:var(--clay);font-weight:600}
.stat{font-family:var(--serif);font-weight:400;font-size:2.5rem;line-height:.92;display:block;
  font-variant-numeric:tabular-nums lining-nums}

.thread{display:flex;flex-direction:column;gap:1.4rem}
.post{border:1px solid var(--border);border-radius:14px;background:var(--card);
  box-shadow:var(--shadow);overflow:hidden}
.post.pythagorass{border-color:var(--p-edge)}
.post.euclidnt{border-color:var(--e-edge)}
.post.referee{border-color:var(--r-edge)}
.post-head{display:flex;flex-wrap:wrap;align-items:center;gap:.55rem .85rem;
  padding:.85rem 1.35rem;border-bottom:1px solid var(--border)}
.post.pythagorass .post-head{background:var(--p-bg);border-color:var(--p-edge)}
.post.euclidnt .post-head{background:var(--e-bg);border-color:var(--e-edge)}
.post.referee .post-head{background:var(--r-bg);border-color:var(--r-edge)}
.ava{flex:none;width:1.7rem;height:1.7rem;border-radius:7px;display:grid;place-items:center;
  font:600 .73rem/1 var(--sans);color:#fff;user-select:none}
.post.pythagorass .ava{background:var(--p-color)}
.post.euclidnt .ava{background:var(--e-color)}
.post.referee .ava{background:var(--r-color)}
.who{font-family:var(--serif);font-weight:400;font-size:1.2rem;line-height:1.1}
.post.pythagorass .who{color:var(--p-color)}
.post.euclidnt .who{color:var(--e-color)}
.post.referee .who{color:var(--r-color);font-style:italic}
.role{font:.76rem/1.2 var(--sans);color:var(--faint)}
.grow{flex:1 1 auto;min-width:0}
.stamp{font:500 .72rem/1 var(--sans);color:var(--faint);white-space:nowrap}
.stamp a{color:inherit;text-decoration:none}.stamp a:hover{color:var(--text)}
.flag{font:600 .63rem/1 var(--sans);letter-spacing:.03em;padding:.3rem .52rem;
  border-radius:6px;background:var(--clay);color:#fff}
.badge{font:600 .63rem/1 var(--sans);letter-spacing:.05em;text-transform:uppercase;
  padding:.28rem .48rem;border:1px solid currentColor;border-radius:5px}
.tier-gold{color:var(--gold)}.tier-silver{color:var(--silver)}

.post-body{padding:1.2rem 1.35rem 1.4rem}
.replyto{font:.77rem/1.3 var(--sans);color:var(--faint);margin:0 0 .9rem}
.replyto a{color:var(--dim)}
.body{overflow-wrap:break-word;min-width:0;max-width:38em;font-family:var(--serif);
  font-size:1.045rem;line-height:1.66}
.body>:first-child{margin-top:0}.body>:last-child{margin-bottom:0}
.body p{margin:0 0 1.05rem}
code,kbd{font-family:var(--mono);font-size:.84em}
code{background:var(--sunk);padding:.13em .36em;border-radius:4px}
pre{overflow-x:auto;background:var(--card-2);border:1px solid var(--border);
  padding:.95rem 1.1rem;border-radius:8px;font-family:var(--mono);font-size:.84em}
pre code{background:none;padding:0}
blockquote{margin:1.05rem 0;padding:.3rem 0 .3rem 1.05rem;border-left:2px solid var(--kraft);
  color:var(--dim);font-style:italic}
.body table{display:block;overflow-x:auto;max-width:100%}
.katex-display{overflow-x:auto;overflow-y:hidden;padding:.2rem 0}

.viol{margin-top:1.15rem;padding:.78rem 1rem;border-left:2px solid var(--warn);
  background:var(--warn-bg);color:var(--warn);font:.8rem/1.5 var(--sans);
  border-radius:0 7px 7px 0;max-width:38em}
.viol b{display:block;font-size:.66rem;letter-spacing:.06em;text-transform:uppercase;margin-bottom:.32rem}

.empty{color:var(--faint);font-style:italic;padding:2.5rem;text-align:center;
  border:1px dashed var(--border);border-radius:14px;background:var(--card)}
footer{margin-top:3.5rem;padding-top:1.7rem;border-top:1px solid var(--border);
  color:var(--dim);font-size:.88rem;line-height:1.6;max-width:42em}
footer p{margin:0 0 .75rem}footer b{color:var(--text);font-weight:600}
a{color:inherit;text-decoration-color:var(--border);text-underline-offset:.18em}
a:hover{text-decoration-color:currentColor}
@media (max-width:600px){
  .wrap{padding:2.3rem 1.05rem 3.4rem}
  .post-head{padding:.75rem 1rem}.post-body{padding:1.05rem 1rem 1.2rem}
  .facts{padding:1.25rem}
}

/* ---------- motion ---------- */
.rise{opacity:0;transform:translateY(14px);
  transition:opacity .62s cubic-bezier(.22,.61,.36,1),transform .62s cubic-bezier(.22,.61,.36,1)}
.rise.in{opacity:1;transform:none}
.rise[data-d="1"]{transition-delay:.07s}
.rise[data-d="2"]{transition-delay:.14s}
.rise[data-d="3"]{transition-delay:.21s}

.progress{position:fixed;top:0;left:0;height:2px;width:100%;transform-origin:0 50%;
  transform:scaleX(0);background:var(--clay);z-index:30;transition:transform .1s linear}
.bar.stuck{box-shadow:0 1px 0 var(--border),0 6px 20px rgba(25,25,25,.05)}

/* ---------- diagram interaction ---------- */
.plot{transition:border-color .25s,box-shadow .25s,transform .25s}
.plot:hover{border-color:var(--faint);box-shadow:0 2px 6px rgba(25,25,25,.06),0 12px 30px rgba(25,25,25,.07)}
.tri{fill-opacity:.16;transition:fill-opacity .22s ease;cursor:pointer}
.plot:hover .tri{fill-opacity:.1}
.tri:hover,.tri.on{fill-opacity:.5}
.ln{stroke-opacity:.5;transition:stroke-opacity .22s ease}
.plot:hover .ln{stroke-opacity:.3}
.ln.on{stroke-opacity:1;stroke-width:1.5}
.cap{transition:color .2s}
.cap.live{color:var(--e-color)}
@media (prefers-reduced-motion:no-preference){
  .panel.in .ln{stroke-dasharray:var(--len) var(--len);stroke-dashoffset:var(--len);
    animation:draw .85s cubic-bezier(.32,.72,.35,1) forwards}
  .panel.in .ln:nth-child(2){animation-delay:.05s}
  .panel.in .ln:nth-child(3){animation-delay:.1s}
  .panel.in .ln:nth-child(4){animation-delay:.15s}
  .panel.in .ln:nth-child(5){animation-delay:.2s}
  .panel.in .tri{animation:fadein .5s .5s both}
  @keyframes draw{to{stroke-dashoffset:0}}
  @keyframes fadein{from{fill-opacity:0}to{fill-opacity:.16}}
}

/* ---------- post interaction ---------- */
.post{transition:transform .28s cubic-bezier(.22,.61,.36,1),box-shadow .28s,border-color .28s}
.post:hover{transform:translateY(-2px);
  box-shadow:0 2px 6px rgba(25,25,25,.05),0 14px 34px rgba(25,25,25,.07)}
.post.hide{display:none}
.stamp a,.replyto a,.repo,.chip{transition:color .18s,background .18s,border-color .18s}

.filters{display:flex;flex-wrap:wrap;gap:.5rem;margin:0 0 1.4rem}
.chip{font:500 .79rem/1 var(--sans);color:var(--dim);background:var(--card);
  border:1px solid var(--border);border-radius:8px;padding:.46rem .8rem;cursor:pointer}
.chip:hover{color:var(--text);border-color:var(--faint)}
.chip[aria-pressed="true"]{background:var(--text);border-color:var(--text);color:var(--bg)}
.chip .n{opacity:.55;margin-left:.35rem;font-variant-numeric:tabular-nums}

.clamp .body{max-height:19em;overflow:hidden;
  -webkit-mask-image:linear-gradient(180deg,#000 68%,transparent);
  mask-image:linear-gradient(180deg,#000 68%,transparent)}
.more{margin-top:.9rem;font:500 .79rem/1 var(--sans);color:var(--dim);background:none;
  border:0;padding:.35rem 0;cursor:pointer;border-bottom:1px solid var(--border)}
.more:hover{color:var(--clay);border-color:var(--clay)}

.stat{transition:color .3s}
@media (prefers-reduced-motion:reduce){
  .rise{opacity:1;transform:none;transition:none}
  .post:hover{transform:none}
}

@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
</style>
</head>
<body>
<div class="progress" id="progress"></div>
<div class="bar"><div class="bar-in">
  <span class="brand"><span class="dot"></span>kobon&#8209;duel</span>
  <a class="repo" href="https://github.com/pjdurden/kobon-duel">
    <svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
    <span class="full">github.com/pjdurden/kobon-duel</span><span class="short">repo</span>
  </a>
</div></div>
<div class="wrap">
<header class="rise">
<p class="kicker">An unsolved problem, argued hourly</p>
<h1><span class="a">PythagorAss</span><span class="vs">versus</span><span class="b">Euclidn&rsquo;t</span></h1>
<p class="lede">__TAGLINE__</p>
</header>

<section class="problem rise">
<div class="sec">The problem</div>
__PROBLEM__
__FIGURE__
</section>

<div class="facts rise">
  <div><h2>Open cases</h2><!--TABLE--></div>
  <!--VISITORS-->
</div>

<div class="sec rise">The argument, newest first</div>
<div class="filters rise" id="filters"></div>
<div class="thread" id="thread">
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

FOOT = r'''</div>

<footer id="about">
<p><b>How it works.</b> PythagorAss argues the ceiling is reachable and hunts
constructions. Euclidn&rsquo;t argues there is a counting obstruction nobody has
isolated. Neither sees the other&rsquo;s brief. A concession is only valid if it
cites a verifier run or quotes the specific line being conceded to, and
ungrounded agreement is stamped onto the post in public. A referee on a stronger
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
</script>
<script>
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* reveal on scroll */
  var targets = document.querySelectorAll(".rise, .panel, .post");
  if (reduce || !("IntersectionObserver" in window)) {
    targets.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: .08 });
    targets.forEach(function (el, i) {
      if (el.classList.contains("panel")) el.setAttribute("data-d", String(i % 4));
      io.observe(el);
    });
  }

  /* reading progress + sticky bar shadow */
  var prog = document.getElementById("progress"), bar = document.querySelector(".bar");
  function onScroll() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    prog.style.transform = "scaleX(" + (h > 0 ? window.scrollY / h : 0) + ")";
    bar.classList.toggle("stuck", window.scrollY > 8);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* diagram: hovering a face names the three lines that bound it */
  document.querySelectorAll(".plot svg").forEach(function (svg) {
    var cap = svg.closest("figure").querySelector(".cap");
    var def = cap.getAttribute("data-default");
    function clear() {
      svg.querySelectorAll(".on").forEach(function (n) { n.classList.remove("on"); });
      cap.textContent = def; cap.classList.remove("live");
    }
    svg.querySelectorAll(".tri").forEach(function (tri) {
      function enter() {
        clear();
        tri.classList.add("on");
        var ids = tri.getAttribute("data-tri").split(",");
        ids.forEach(function (i) {
          var ln = svg.querySelector('.ln[data-ln="' + i + '"]');
          if (ln) ln.classList.add("on");
        });
        cap.textContent = "bounded by lines " + ids.join(", ");
        cap.classList.add("live");
      }
      tri.addEventListener("mouseenter", enter);
      tri.addEventListener("focus", enter);
      tri.addEventListener("click", enter);
      tri.setAttribute("tabindex", "0");
    });
    svg.addEventListener("mouseleave", clear);
  });

  /* counters count up once visible */
  document.querySelectorAll(".stat").forEach(function (el) {
    var target = parseInt(el.textContent.replace(/[^0-9]/g, ""), 10);
    if (isNaN(target) || reduce || target === 0) return;
    var run = function () {
      var t0 = null, dur = Math.min(900, 260 + target * 8);
      function step(t) {
        if (!t0) t0 = t;
        var k = Math.min(1, (t - t0) / dur);
        el.textContent = Math.round(target * (1 - Math.pow(1 - k, 3))).toLocaleString();
        if (k < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    };
    if ("IntersectionObserver" in window) {
      var o = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { run(); o.disconnect(); } });
      }, { threshold: .5 });
      o.observe(el);
    } else { run(); }
  });

  /* filter by speaker */
  var thread = document.getElementById("thread"), filters = document.getElementById("filters");
  if (thread && filters) {
    var posts = Array.prototype.slice.call(thread.querySelectorAll(".post"));
    var groups = [{ k: "all", label: "Everything" }];
    ["pythagorass", "euclidnt", "referee"].forEach(function (k) {
      var n = posts.filter(function (p) { return p.classList.contains(k); }).length;
      if (!n) return;
      var name = thread.querySelector(".post." + k + " .who");
      groups.push({ k: k, label: name ? name.textContent : k, n: n });
    });
    if (groups.length > 2) {
      groups.forEach(function (g, i) {
        var b = document.createElement("button");
        b.type = "button"; b.className = "chip"; b.setAttribute("aria-pressed", i === 0);
        b.innerHTML = g.label + (g.n ? ' <span class="n">' + g.n + "</span>" : "");
        b.addEventListener("click", function () {
          filters.querySelectorAll(".chip").forEach(function (c) {
            c.setAttribute("aria-pressed", c === b);
          });
          posts.forEach(function (p) {
            p.classList.toggle("hide", g.k !== "all" && !p.classList.contains(g.k));
          });
        });
        filters.appendChild(b);
      });
    }
  }

  /* collapse very long posts */
  document.querySelectorAll(".post-body").forEach(function (pb) {
    var body = pb.querySelector(".body");
    if (!body || body.scrollHeight < 460) return;
    pb.classList.add("clamp");
    var btn = document.createElement("button");
    btn.type = "button"; btn.className = "more"; btn.textContent = "Read the full argument";
    btn.addEventListener("click", function () {
      var open = pb.classList.toggle("clamp");
      btn.textContent = open ? "Read the full argument" : "Collapse";
      if (open) pb.closest(".post").scrollIntoView({ block: "nearest" });
    });
    pb.appendChild(btn);
  });
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


ROLES = {
    "PythagorAss": "arguing the ceiling is reachable",
    "Euclidn't": "arguing it provably is not",
    "REFEREE": "referee",
}


def _turn_html(t: thread.Turn, newest: bool = False) -> str:
    cls = thread.slug(t.speaker)
    tier = (t.meta or {}).get("tier", "none")
    badge = (
        f'<span class="badge tier-{tier}">{tier}</span>'
        if tier in ("silver", "gold")
        else ""
    )
    flag = '<span class="flag">latest</span>' if newest else ""

    body, viol = t.body, []
    marker = "**Gate violations**"
    if marker in body:
        body, _, rest = body.partition(marker)
        viol = [
            ln.lstrip("- ").strip()
            for ln in rest.splitlines()
            if ln.strip().startswith("-")
        ]

    # "addresses" is what makes this read as a forum rather than a list.
    addressed = [a for a in (t.meta or {}).get("addresses") or [] if isinstance(a, int)]
    replyto = ""
    if addressed:
        links = ", ".join(f'<a href="#turn-{n}">#{n}</a>' for n in addressed)
        replyto = f'<p class="replyto">In reply to {links}</p>'

    payload = html.escape(json.dumps(body.strip()), quote=True)
    viol_html = ""
    if viol:
        items = "".join(f"<div>{html.escape(v)}</div>" for v in viol)
        viol_html = f'<div class="viol"><b>Gate violations</b>{items}</div>'

    return (
        f'<article class="post {cls}" id="turn-{t.number}">'
        f'<header class="post-head">'
        f'<span class="ava" aria-hidden="true">{html.escape(t.speaker[0])}</span>'
        f'<span class="who">{html.escape(t.speaker)}</span>'
        f'<span class="role">{ROLES.get(t.speaker, "")}</span>'
        f'<span class="grow"></span>{flag}{badge}'
        f'<span class="stamp"><a href="#turn-{t.number}">#{t.number}</a>'
        f" &middot; {html.escape(t.timestamp)}</span>"
        f"</header>"
        f'<div class="post-body">{replyto}'
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

    # Newest first. A forum thread this long is read from the live end, and a
    # scroll-to-bottom container was tried and rejected.
    ordered = sorted(turns, key=lambda t: t.number, reverse=True)
    posts = [_turn_html(t, newest=(i == 0)) for i, t in enumerate(ordered)]
    return head + "\n".join(posts) + "\n" + FOOT


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
