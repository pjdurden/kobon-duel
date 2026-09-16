"""Referee T691: the axis-absent f_perp=2 mirror family at k=20, annealed.

kobon_20_116tri -- the best known k=20 arrangement -- is exactly this: an
order-2 automorphism with two fixed lines (its only parallel pair), nine swapped
pairs, s_mirror = 2, B = 358.  T678 sampled the family with 120 random draws and
read a ceiling off the mean.  This anneals it.
"""
import numpy as np, random, sys, json
from itertools import combinations
from fractions import Fraction
from kobon import verify

K = 20
TR = np.array(list(combinations(range(K), 3)))
TI, TJ, TK = TR[:, 0], TR[:, 1], TR[:, 2]


def build(seeds):
    """seeds = [(v1,), (v2,)] as two ints then 9 (a,b,c) triples."""
    v1, v2, pairs = seeds[0], seeds[1], seeds[2]
    lines = [(1, 0, v1), (1, 0, v2)]
    for (a, b, c) in pairs:
        lines.append((a, b, c))
        lines.append((a, -b, c))
    return lines


def analyse(seeds):
    lines = build(seeds)
    n = len(lines)
    pts = {}
    par = 0
    for i, j in combinations(range(n), 2):
        (a1, b1, c1), (a2, b2, c2) = lines[i], lines[j]
        det = a1 * b2 - a2 * b1
        if det == 0:
            par += 1
            continue
        pts[(i, j)] = (Fraction(c1 * b2 - c2 * b1, det), Fraction(a1 * c2 - a2 * c1, det))
    if par != 1 or len(set(pts.values())) != len(pts):
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

    def mir(x):
        return x if x < 2 else (x ^ 1) + 2 - 2 * ((x - 2) % 2 == 0) + 2 * ((x - 2) % 2 == 0)
    def m2(x):
        return x if x < 2 else (2 + ((x - 2) ^ 1))
    s = sum(1 for t in tris if tuple(sorted(m2(int(x)) for x in t)) == tuple(t))
    B = int((P >= 0).sum()) - n
    return dict(T=len(tris), s=int(s), B=B, F=B - 3 * len(tris))


def exact(seeds):
    lines = build(seeds)
    tris = verify.triangles(lines)
    def m2(x):
        return x if x < 2 else (2 + ((x - 2) ^ 1))
    s = sum(1 for (i, j, k, _) in tris if tuple(sorted((m2(i), m2(j), m2(k)))) == (i, j, k))
    return len(tris), s


SCALES = [1, 1, 2, 2, 4, 8, 16, 32]


def rand_seeds(scale=45):
    v1, v2 = random.randint(-scale, scale), random.randint(-scale, scale)
    while v2 == v1:
        v2 = random.randint(-scale, scale)
    pairs = []
    while len(pairs) < 9:
        a, b, c = (random.randint(-scale, scale) for _ in range(3))
        if b != 0:
            pairs.append((a, b, c))
    return [v1, v2, pairs]


def perturb(seeds):
    v1, v2, pairs = seeds[0], seeds[1], [list(p) for p in seeds[2]]
    d = random.choice([-1, 1]) * random.choice(SCALES)
    r = random.random()
    if r < 0.1:
        v1 += d
    elif r < 0.2:
        v2 += d
    else:
        i = random.randrange(9)
        j = random.randrange(3)
        pairs[i][j] += d
        if pairs[i][1] == 0:
            return None
    return [v1, v2, [tuple(p) for p in pairs]]


def anneal(seeds, steps, T0=4.0):
    cur = analyse(seeds)
    while cur is None:
        seeds = rand_seeds()
        cur = analyse(seeds)
    best = (cur["T"], cur, seeds)
    for st in range(steps):
        temp = max(0.05, T0 * (1 - st / steps))
        ns = perturb(seeds)
        if ns is None:
            continue
        r = analyse(ns)
        if r is None:
            continue
        if r["T"] >= cur["T"] or random.random() < pow(2.718281828, (r["T"] - cur["T"]) / temp):
            seeds, cur = ns, r
            if r["T"] > best[0]:
                best = (r["T"], r, ns)
    return best


if __name__ == "__main__":
    restarts, steps = int(sys.argv[1]), int(sys.argv[2])
    random.seed(int(sys.argv[3]))
    hist = {}
    top = []
    for r in range(restarts):
        T, res, seeds = anneal(rand_seeds(), steps)
        hist[T] = hist.get(T, 0) + 1
        top.append((T, res, seeds))
        top.sort(key=lambda x: -x[0])
        top = top[:3]
        print(f"restart {r}: T={T} s_mirror={res['s']} B={res['B']} F={res['F']}", flush=True)
    print("HIST", json.dumps({str(k): v for k, v in sorted(hist.items())}), flush=True)
    for T, res, seeds in top:
        print("TOP", T, res, seeds, "exact=", exact(seeds), flush=True)
