"""Referee T713: the sigma-equivariant flip ball on kobon_18_93tri, done once,
correctly, and pushed past the radius T691 reached.

T691 reported radius-1 = 31 states, hist {84:23, 87:5, 88:2, 90:1}.
T696 reproduced it as 93 orbit-moves, hist {84:69, 87:15, 88:6, 90:3}.
T711 reported radius-1 = 19 states, hist {84:16, 87:2, 90:1}.
T712 reported radius-1 = 31 orbits, hist {84:23, 87:5, 88:2, 90:1}.

This file settles which is right, diagnoses the 12 missing moves, and runs the
BFS on the correct move set far enough to bound the s=1 stratum inside the ball.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import deque

from kobon import corpus, table as T

ORBITS = [(1, 8, 13), (2, 7, 14), (3, 9, 15), (4, 10, 16), (5, 11, 17), (6, 12, 18)]
SIGMA = {}
for o in ORBITS:
    for idx, x in enumerate(o):
        SIGMA[x] = o[(idx + 1) % 3]


def sig_tri(tri):
    return tuple(sorted(SIGMA[x] for x in tri))


def swap_adjacent(row, x, y):
    ix = iy = None
    for idx, e in enumerate(row):
        if isinstance(e, (list, tuple)):
            if x in e or y in e:
                raise ValueError("bracket at flip site")
            continue
        if e == x:
            ix = idx
        if e == y:
            iy = idx
    if ix is None or iy is None or abs(ix - iy) != 1:
        raise ValueError(f"not adjacent: {x},{y} at {ix},{iy}")
    row[ix], row[iy] = row[iy], row[ix]


def flip_in_place(t, tri):
    a, b, c = tri
    swap_adjacent(t[a - 1], b, c)
    swap_adjacent(t[b - 1], a, c)
    swap_adjacent(t[c - 1], a, b)


def equivariant_moves(t):
    """Every sigma-orbit of triangles, applied as one atomic triple-flip.

    Returns (list of (orbit_key, new_table), list of (orbit_key, reason))."""
    tris = T.triangles(t)
    triset = set(tuple(x) for x in tris)
    seen = set()
    ok, bad = [], []
    for tri in tris:
        tri = tuple(tri)
        orb = [tri]
        x = sig_tri(tri)
        while x != tri:
            orb.append(x)
            x = sig_tri(x)
        key = min(orb)
        if key in seen:
            continue
        seen.add(key)
        if not all(o in triset for o in orb):
            bad.append((key, "orbit not all triangles"))
            continue
        t2 = copy.deepcopy(t)
        try:
            for o in orb:
                flip_in_place(t2, o)
            T.validate(t2)
        except ValueError as exc:
            bad.append((key, str(exc)))
            continue
        ok.append((key, t2))
    return ok, bad


def canon(t):
    return json.dumps(t)


def s_count(t):
    """sigma-fixed triangles of a table."""
    return sum(1 for tri in T.triangles(t) if sig_tri(tri) == tuple(tri))


def shortrows(t):
    k = len(t)
    return sum(1 for r in t if sum(len(e) if isinstance(e, (list, tuple)) else 1
                                   for e in r) < k - 1)


def bfs(t0, max_radius):
    start = canon(t0)
    seen = {start: 0}
    frontier = [t0]
    out = []
    for rad in range(1, max_radius + 1):
        nxt = []
        hist = {}
        s1hist = {}
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
                s = s_count(t2)
                if s:
                    s1hist[n] = s1hist.get(n, 0) + 1
        out.append((rad, len(nxt), dict(sorted(hist.items())), dict(sorted(s1hist.items()))))
        print(f"radius {rad}: {len(nxt)} new  max={max(hist) if hist else '-'}  "
              f"hist={dict(sorted(hist.items()))}", flush=True)
        print(f"   of which sigma-fixed-triangle-bearing (s>0): {dict(sorted(s1hist.items()))}",
              flush=True)
        frontier = nxt
        if not frontier:
            break
    return out


if __name__ == "__main__":
    ks = corpus.by_key()
    t0 = ks["kobon_18_93tri"]["table"]
    print("base T =", T.count(t0), " s =", s_count(t0), " short rows =", shortrows(t0))

    tris = T.triangles(t0)
    # orbit census
    orbs = {}
    for tri in tris:
        tri = tuple(tri)
        orb = [tri]
        x = sig_tri(tri)
        while x != tri:
            orb.append(x)
            x = sig_tri(x)
        orbs[min(orb)] = orb
    print("triangle orbits:", len(orbs),
          "sizes:", sorted(set(len(v) for v in orbs.values())))

    shared = [k for k, v in orbs.items()
              if len(set(k) | set(v[1])) < 6]
    print("orbits whose triangle shares a line with its own sigma-image:",
          len(shared), shared)

    ok, bad = equivariant_moves(t0)
    hist = {}
    for key, t2 in ok:
        n = T.count(t2)
        hist[n] = hist.get(n, 0) + 1
    print("radius-1 moves that succeed:", len(ok), " fail:", len(bad))
    print("radius-1 hist:", dict(sorted(hist.items())))
    print("distinct canonical children:", len(set(canon(t2) for _, t2 in ok)))
    for key, t2 in ok:
        n = T.count(t2)
        if n % 3 == 1:
            print(f"   s=1 child from orbit rep {key}: T={n} s={s_count(t2)} "
                  f"shortrows={shortrows(t2)} valid=OK")
    print("failures:", bad)

    rad = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    bfs(t0, rad)
