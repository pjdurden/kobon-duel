"""Referee T691: the C3 k=18 branch with one orbit of parallel pairs.

kobon_18_93tri -- the published best-known -- is a C3 object with six line
orbits and exactly one orbit of parallel pairs, B = 282 = 3*94.  So in this
branch T = 94 is a perfect packing (F = 0), the same shape kobon_21_133tri_1
achieves at k = 21.  Seeds 4 and 5 share a direction, which makes exactly three
parallel pairs; everything else is free.
"""
import numpy as np, random, sys, json
from itertools import combinations
from fractions import Fraction
from kobon import verify

TR = np.array(list(combinations(range(18), 3)))
TI, TJ, TK = TR[:, 0], TR[:, 1], TR[:, 2]


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


def analyse(seeds, want_par):
    lines = build(seeds)
    n = len(lines)
    pts = {}
    par = 0
    for i, j in combinations(range(n), 2):
        (a1, b1, c1), (a2, b2, c2) = lines[i], lines[j]
        det = a1 * b2 - a2 * b1
        if det == 0:
            if c1 * a2 == c2 * a1 and c1 * b2 == c2 * b1:
                return None  # identical lines
            par += 1
            continue
        pts[(i, j)] = (Fraction(c1 * b2 - c2 * b1, det), Fraction(a1 * c2 - a2 * c1, det))
    if par != want_par or len(set(pts.values())) != len(pts):
        return None
    P = np.full((n, n), -1, dtype=np.int32)
    for i in range(n):
        b = lines[i][1]
        key = sorted((pts[(min(i, j), max(i, j))][0 if b != 0 else 1], j)
                     for j in range(n) if (min(i, j), max(i, j)) in pts)
        for r, (_, j) in enumerate(key):
            P[i][j] = r
    r = np.arange(len(TR))
    tot = np.zeros(len(TR), dtype=np.int32)
    ok = np.ones(len(TR), dtype=bool)
    for M, u, v in ((P[TI], TJ, TK), (P[TJ], TI, TK), (P[TK], TI, TJ)):
        e1, e2 = M[r, u], M[r, v]
        ok &= (e1 >= 0) & (e2 >= 0)
        lo = np.minimum(e1, e2)[:, None]
        hi = np.maximum(e1, e2)[:, None]
        tot += ((M > lo) & (M < hi)).sum(1).astype(np.int32)
    tris = TR[ok & (tot == 0)]
    s = sum(1 for t in tris if t[0] // 3 == t[1] // 3 == t[2] // 3)
    B = int((P >= 0).sum(1).sum()) - n  # sum over lines of (crossings - 1)
    return dict(T=len(tris), s=int(s), B=B, F=B - 3 * len(tris), p=par)


def exact(seeds):
    tris = verify.triangles(build(seeds))
    return len(tris), sum(1 for (i, j, k, _) in tris if i // 3 == j // 3 == k // 3)


SCALES = [1, 1, 2, 2, 4, 8, 16, 32]


def rand_seeds(scale=45):
    s = [tuple(random.randint(-scale, scale) for _ in range(3)) for _ in range(6)]
    s[5] = (s[4][0], s[4][1], random.randint(-scale, scale))
    return s


def fix_par(s):
    s = list(s)
    s[5] = (s[4][0], s[4][1], s[5][2])
    return s


def anneal(seeds, steps, want_par, T0=4.0):
    cur = analyse(seeds, want_par)
    while cur is None:
        seeds = rand_seeds()
        cur = analyse(seeds, want_par)
    best = (cur["T"], cur, list(seeds))
    for st in range(steps):
        temp = max(0.05, T0 * (1 - st / steps))
        ns = list(seeds)
        i = random.randrange(6)
        v = list(ns[i])
        v[random.randrange(3)] += random.choice([-1, 1]) * random.choice(SCALES)
        ns[i] = tuple(v)
        ns = fix_par(ns) if i != 5 else ns
        if i == 4:
            ns[5] = (ns[4][0], ns[4][1], ns[5][2])
        r = analyse(ns, want_par)
        if r is None:
            continue
        if r["T"] >= cur["T"] or random.random() < pow(2.718281828, (r["T"] - cur["T"]) / temp):
            seeds, cur = ns, r
            if r["T"] > best[0]:
                best = (r["T"], r, list(seeds))
    return best


if __name__ == "__main__":
    restarts, steps, want_par = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    random.seed(int(sys.argv[4]))
    hist = {}
    top = []
    for r in range(restarts):
        T, res, seeds = anneal(rand_seeds(), steps, want_par)
        hist[T] = hist.get(T, 0) + 1
        top.append((T, res, seeds))
        top.sort(key=lambda x: -x[0])
        top = top[:5]
        print(f"restart {r}: T={T} s={res['s']} B={res['B']} F={res['F']} p={res['p']} seeds={seeds}", flush=True)
    print("HIST", json.dumps({str(k): v for k, v in sorted(hist.items())}), flush=True)
    for T, res, seeds in top:
        print("TOP", T, res, seeds, "exact=", exact(seeds), flush=True)
