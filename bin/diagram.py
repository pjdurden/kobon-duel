"""Generate the explainer diagram for the site.

The shaded triangles are not drawn by hand: they come from kobon/verify.py,
the same exact-arithmetic face finder the phase-2 verifier is built on. If the
caption says five triangles, five triangles were counted in exact rational
arithmetic.
"""
from __future__ import annotations

import math
import pathlib
import sys
from fractions import Fraction as F

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from kobon import verify  # noqa: E402

DEN = 10**6  # rational approximation of irrational constructions


def _line_through(p1, p2):
    """Exact (a, b, c) with a*x + b*y = c through two rational points."""
    (x1, y1), (x2, y2) = p1, p2
    a, b = y2 - y1, x1 - x2
    return (a, b, a * x1 + b * y1)


def _rat(v):
    return F(v).limit_denominator(DEN)


def pentagram():
    """Five lines forming a pentagram. This is an optimal N(5) = 5 arrangement.

    Each line joins two non-adjacent vertices of a regular pentagon. The five
    star points are triangles; the middle face is a pentagon, not a triangle.
    """
    pts = [
        (_rat(math.cos(math.radians(90 + 72 * i))),
         _rat(math.sin(math.radians(90 + 72 * i))))
        for i in range(5)
    ]
    return [_line_through(pts[i], pts[(i + 2) % 5]) for i in range(5)]


def simple_triangle():
    """Three lines, one triangle. The smallest interesting case."""
    return [(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(1), F(1), F(1))]


def two_orbit_c7():
    """Fourteen lines as two orbits of an order-7 rotation.

    Drawn as texture, not as a claim. This is the family PythagorAss opened the
    debate by ruling out: every triangle orbit has size 7, so the count is
    forced to a multiple of 7 and caps at 49, below the best known 53.
    """
    lines = []
    for base_r, base_t in ((F(45, 100), 0.0), (F(72, 100), 25.7)):
        for i in range(7):
            th = math.radians(base_t + 360 * i / 7)
            a, b = _rat(math.cos(th)), _rat(math.sin(th))
            lines.append((a, b, base_r))
    return lines


def _clip(line, box):
    """Segment where a line crosses the box, or None."""
    a, b, c = (float(v) for v in line)
    x0, y0, x1, y1 = box
    pts = []
    if b != 0:
        for x in (x0, x1):
            y = (c - a * x) / b
            if y0 - 1e-9 <= y <= y1 + 1e-9:
                pts.append((x, y))
    if a != 0:
        for y in (y0, y1):
            x = (c - b * y) / a
            if x0 - 1e-9 <= x <= x1 + 1e-9:
                pts.append((x, y))
    uniq = []
    for p in pts:
        if not any(abs(p[0] - q[0]) < 1e-9 and abs(p[1] - q[1]) < 1e-9 for q in uniq):
            uniq.append(p)
    return (uniq[0], uniq[1]) if len(uniq) >= 2 else None


def svg(lines, box, size=190, shade=True, accent="var(--p-color)"):
    """Render an arrangement, shading every triangular face when asked."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    sx = lambda x: (float(x) - x0) / w * size
    sy = lambda y: size - (float(y) - y0) / h * size

    parts = [
        f'<svg viewBox="0 0 {size} {size}" width="100%" height="100%" '
        f'role="img" aria-hidden="true" preserveAspectRatio="xMidYMid meet">'
    ]
    if shade:
        for _, _, _, verts in verify.triangles(lines):
            pts = " ".join(f"{sx(p[0]):.2f},{sy(p[1]):.2f}" for p in verts)
            parts.append(f'<polygon points="{pts}" fill="{accent}" fill-opacity=".2"/>')
    for ln in lines:
        seg = _clip(ln, box)
        if seg:
            (ax, ay), (bx, by) = seg
            parts.append(
                f'<line x1="{sx(ax):.2f}" y1="{sy(ay):.2f}" '
                f'x2="{sx(bx):.2f}" y2="{sy(by):.2f}" '
                f'stroke="currentColor" stroke-width=".9" stroke-opacity=".55" '
                f'stroke-linecap="round"/>'
            )
    parts.append("</svg>")
    return "".join(parts)


PANELS = [
    ("3 lines", "1 triangle", simple_triangle, (-0.35, -0.35, 1.35, 1.35), True, "var(--p-color)"),
    ("5 lines", "5 triangles", pentagram, (-1.15, -1.15, 1.15, 1.15), True, "var(--p-color)"),
    ("14 lines", "53 or 54?", two_orbit_c7, (-1.15, -1.15, 1.15, 1.15), False, "var(--e-color)"),
]


def figure() -> str:
    """The three-panel explainer figure, captions verified where they claim a count."""
    cells = []
    for label, caption, build, box, shade, accent in PANELS:
        lines = build()
        if shade:
            actual = verify.count(lines)
            expected = int(caption.split()[0])
            assert actual == expected, f"{label}: counted {actual}, caption says {expected}"
        cells.append(
            f'<figure class="panel{"" if shade else " panel-open"}">'
            f'<div class="plot">{svg(lines, box, shade=shade, accent=accent)}</div>'
            f"<figcaption><b>{label}</b><span>{caption}</span></figcaption>"
            f"</figure>"
        )
    return f'<div class="figure">{"".join(cells)}</div>'


if __name__ == "__main__":
    for label, caption, build, _box, shade, _a in PANELS:
        n = verify.count(build())
        print(f"{label:>9}: {len(build()):>2} lines, {n:>2} triangles counted   ({caption})")
