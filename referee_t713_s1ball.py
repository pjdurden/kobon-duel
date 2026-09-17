"""Referee T713: the move T712 named and nobody ran -- the sigma-equivariant
flip ball centred on an s=1 object, not on the s=0 record.

Includes a coordinates -> table converter (exact Fraction ordering along each
line), calibrated against kobon.verify.triangles and kobon.table.triangles
before use.
"""
from __future__ import annotations

import copy
import json
import sys
from fractions import Fraction
from itertools import combinations

from kobon import table as T, verify
from referee_t713_flip import (SIGMA, sig_tri, equivariant_moves, canon,
                               s_count, shortrows)
import referee_t713_flip as RF
from referee_t691_par import build, analyse, exact

# The record's table labels its orbits {1,8,13}...; a build()-ordered table
# labels them {1,2,3},{4,5,6},...  Switch sigma to match the object in hand.
BUILD_ORBITS = [(3 * j + 1, 3 * j + 2, 3 * j + 3) for j in range(6)]


def set_sigma(orbits):
    RF.SIGMA.clear()
    for o in orbits:
        for idx, x in enumerate(o):
            RF.SIGMA[x] = o[(idx + 1) % 3]


def to_table(lines):
    """Exact table of an arrangement of (a,b,c) lines.  c = 0 assumed."""
    n = len(lines)
    pts = {}
    for i, j in combinations(range(n), 2):
        (a1, b1, c1), (a2, b2, c2) = lines[i], lines[j]
        det = a1 * b2 - a2 * b1
        if det == 0:
            continue
        pts[(i, j)] = (Fraction(c1 * b2 - c2 * b1, det),
                       Fraction(a1 * c2 - a2 * c1, det))
    if len(set(pts.values())) != len(pts):
        raise ValueError("concurrence or repeated point -- converter assumes c=0")
    rows = []
    for i in range(n):
        a, b, _ = lines[i]
        key = 0 if b != 0 else 1   # parametrise along x unless the line is vertical
        items = []
        for j in range(n):
            if j == i:
                continue
            p = pts.get((min(i, j), max(i, j)))
            if p is None:
                continue
            items.append((p[key], j + 1))
        items.sort()
        rows.append([j for _, j in items])
    T.validate(rows)
    return rows


def bfs(t0, max_radius, label):
    seen = {canon(t0): 0}
    frontier = [t0]
    print(f"--- BFS from {label}: T={T.count(t0)} s={s_count(t0)} "
          f"shortrows={shortrows(t0)}", flush=True)
    for rad in range(1, max_radius + 1):
        nxt, hist, s1 = [], {}, {}
        for t in frontier:
            ok, _ = equivariant_moves(t)
            for _, t2 in ok:
                c = canon(t2)
                if c in seen:
                    continue
                seen[c] = rad
                nxt.append(t2)
                n = T.count(t2)
                hist[n] = hist.get(n, 0) + 1
                if s_count(t2):
                    s1[n] = s1.get(n, 0) + 1
        print(f"radius {rad}: {len(nxt)} new  max={max(hist) if hist else '-'}  "
              f"hist={dict(sorted(hist.items()))}", flush=True)
        print(f"   s>0 subset: {dict(sorted(s1.items()))}  "
              f"max s>0 = {max(s1) if s1 else '-'}", flush=True)
        frontier = nxt
        if not frontier:
            break


REF91 = [(9, 9, 21), (65, -13, -17), (-47, -60, 29), (8, 13, 27),
         (-42, -31, -24), (-42, -31, 47)]
T695_91 = [(19, -22, 65), (-48, -1, 71), (159, -14, 86), (-243, 35, 52),
           (-14, -82, -101), (-14, -82, 73)]
T701_93 = [(12, -99, 125), (55, 15, 47), (-65, 80, 26), (254, 7, 65),
           (-6, 11, 96), (-6, 11, -10)]

if __name__ == "__main__":
    rad = int(sys.argv[1]) if len(sys.argv) > 1 else 3

    # ---- calibrate the converter on an object whose numbers are on record ----
    set_sigma(BUILD_ORBITS)
    for name, seeds, want in (("T701_93", T701_93, 3), ("ref_91", REF91, 3),
                              ("T695_91", T695_91, 3)):
        lines = build(seeds)
        a = analyse(seeds, want)
        tab = to_table(lines)
        # sigma must be a table automorphism of the converted table
        auto = all(sorted(sig_tri(x) for x in T.triangles(tab))
                   == sorted(tuple(x) for x in T.triangles(tab)) for _ in (0,))
        print(f"{name}: analyse {a}  exact {exact(seeds)}  "
              f"table T={T.count(tab)} s={s_count(tab)} "
              f"shortrows={shortrows(tab)} sigma-preserves-triangle-set={auto}",
              flush=True)

    # ---- the 91-witnesses, converted from coordinates ----
    for name, seeds in (("ref_91", REF91), ("T695_91", T695_91)):
        set_sigma(BUILD_ORBITS)
        tab = to_table(build(seeds))
        bfs(tab, rad, f"{name} (T=91, s=1)")

    # ---- the two s=1 T=88 children of the record ----
    from kobon import corpus
    set_sigma([(1, 8, 13), (2, 7, 14), (3, 9, 15), (4, 10, 16), (5, 11, 17),
               (6, 12, 18)])
    t0 = corpus.by_key()["kobon_18_93tri"]["table"]
    ok, _ = equivariant_moves(t0)
    kids = [(k, t) for k, t in ok if T.count(t) % 3 == 1]
    for k, t in kids:
        bfs(t, rad, f"record child via orbit {k} (T=88, s=1)")
