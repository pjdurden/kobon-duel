"""Fast exact-rank triangle counter for C3 k=18 search (referee T691).

Ranks along each line are computed from exact integer cross-products, so the
combinatorics are exact; only the ordering is used, never a float threshold.
Any winner is re-confirmed with kobon.verify.triangles.
"""
import numpy as np
from itertools import combinations
from fractions import Fraction
from kobon import verify

K = 18
TRIPLES = np.array(list(combinations(range(K), 3)))
TI, TJ, TK = TRIPLES[:, 0], TRIPLES[:, 1], TRIPLES[:, 2]


def orbit(seed):
    a, b, c = seed
    L = [(a, b, c)]
    for _ in range(2):
        a, b, c = L[-1]
        L.append((b - a, -a, c))
    return L


def build(seeds):
    out = []
    for s in seeds:
        out.extend(orbit(s))
    return out


def ranks(lines):
    """Return (ok, P) with P[i][j] the rank of j's crossing along line i.

    ok is False if any pair is parallel or any three lines are concurrent.
    """
    n = len(lines)
    pts = {}
    for i, j in combinations(range(n), 2):
        (a1, b1, c1), (a2, b2, c2) = lines[i], lines[j]
        det = a1 * b2 - a2 * b1
        if det == 0:
            return False, None
        x = Fraction(c1 * b2 - c2 * b1, det)
        y = Fraction(a1 * c2 - a2 * c1, det)
        pts[(i, j)] = (x, y)
    # concurrency check
    if len(set(pts.values())) != len(pts):
        return False, None
    P = np.full((n, n), -1, dtype=np.int32)
    for i in range(n):
        a, b, _ = lines[i]
        key = []
        for j in range(n):
            if j == i:
                continue
            x, y = pts[(min(i, j), max(i, j))]
            key.append(((x if b != 0 else y), j))
        key.sort()
        for r, (_, j) in enumerate(key):
            P[i][j] = r
    return True, P


def count_from_ranks(P):
    A = P[TI]
    B = P[TJ]
    C = P[TK]
    r = np.arange(len(TRIPLES))
    tot = np.zeros(len(TRIPLES), dtype=np.int32)
    for M, u, v in ((A, TJ, TK), (B, TI, TK), (C, TI, TJ)):
        e1 = M[r, u]
        e2 = M[r, v]
        lo = np.minimum(e1, e2)[:, None]
        hi = np.maximum(e1, e2)[:, None]
        tot += ((M > lo) & (M < hi)).sum(1).astype(np.int32)
    return tot == 0


def analyse(seeds):
    lines = build(seeds)
    # distinct?
    keys = set()
    for (a, b, c) in lines:
        g = np.gcd.reduce([abs(a), abs(b), abs(c)]) or 1
        s = -1 if (a < 0 or (a == 0 and b < 0)) else 1
        keys.add((s * a // g, s * b // g, s * c // g))
    if len(keys) != len(lines):
        return None
    ok, P = ranks(lines)
    if not ok:
        return None
    mask = count_from_ranks(P)
    tris = TRIPLES[mask]
    T = len(tris)
    part = np.zeros(K, dtype=int)
    for t in tris:
        part[t] += 1
    s = int(sum(1 for t in tris if t[0] // 3 == t[1] // 3 == t[2] // 3))
    d = [16 - int(part[3 * o]) for o in range(6)]
    return dict(T=T, s=s, d=d, sumd=sum(d), part=list(map(int, part)))


def exact_check(seeds):
    L = build(seeds)
    tris = verify.triangles(L)
    s = sum(1 for (i, j, k, _) in tris if i // 3 == j // 3 == k // 3)
    return len(tris), s
