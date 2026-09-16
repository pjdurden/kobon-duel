"""Referee T691: the mirror family nobody built.

Axis-absent reflection y -> -y with f_perp = 0 (no vertical line, no line on the
axis): k/2 seed lines plus their mirrors. No line is fixed, so no triangle is
fixed (T675's parity law) and T is even -- which is what the targets at k=14
(54) and k=18 (94) are. No forced concurrency and no forced parallel, so the
budget is the full k(k-2).
"""
import numpy as np, random, sys, json
from itertools import combinations
from fractions import Fraction
from kobon import verify

_cache = {}


def triples(K):
    if K not in _cache:
        t = np.array(list(combinations(range(K), 3)))
        _cache[K] = (t, t[:, 0], t[:, 1], t[:, 2])
    return _cache[K]


def build(seeds):
    out = []
    for (a, b, c) in seeds:
        out.append((a, b, c))
        out.append((a, -b, c))
    return out


def ranks(lines):
    n = len(lines)
    pts = {}
    for i, j in combinations(range(n), 2):
        (a1, b1, c1), (a2, b2, c2) = lines[i], lines[j]
        det = a1 * b2 - a2 * b1
        if det == 0:
            return False, None
        pts[(i, j)] = (Fraction(c1 * b2 - c2 * b1, det), Fraction(a1 * c2 - a2 * c1, det))
    if len(set(pts.values())) != len(pts):
        return False, None
    P = np.full((n, n), -1, dtype=np.int32)
    for i in range(n):
        a, b, _ = lines[i]
        key = sorted(((pts[(min(i, j), max(i, j))][0 if b != 0 else 1], j)
                      for j in range(n) if j != i))
        for r, (_, j) in enumerate(key):
            P[i][j] = r
    return True, P


def faces(P, K):
    TR, TI, TJ, TK = triples(K)
    r = np.arange(len(TR))
    tot = np.zeros(len(TR), dtype=np.int32)
    for M, u, v in ((P[TI], TJ, TK), (P[TJ], TI, TK), (P[TK], TI, TJ)):
        e1, e2 = M[r, u], M[r, v]
        lo = np.minimum(e1, e2)[:, None]
        hi = np.maximum(e1, e2)[:, None]
        tot += ((M > lo) & (M < hi)).sum(1).astype(np.int32)
    return TR[tot == 0]


def analyse(seeds):
    lines = build(seeds)
    K = len(lines)
    if any(b == 0 for (a, b, c) in seeds):
        return None
    ok, P = ranks(lines)
    if not ok:
        return None
    tris = faces(P, K)
    # mirror partner of line index x is x^1
    fixed = sum(1 for t in tris if tuple(sorted(int(x) ^ 1 for x in t)) == tuple(t))
    part = np.zeros(K, dtype=int)
    for t in tris:
        part[t] += 1
    return dict(T=len(tris), fixed=int(fixed), part=list(map(int, part)))


def exact(seeds):
    L = build(seeds)
    tris = verify.triangles(L)
    fx = sum(1 for (i, j, k, _) in tris if tuple(sorted((i ^ 1, j ^ 1, k ^ 1))) == (i, j, k))
    return len(tris), fx


SCALES = [1, 1, 2, 2, 4, 8, 16, 32]


def rand_seeds(h, scale=45):
    out = []
    while len(out) < h:
        a, b, c = (random.randint(-scale, scale) for _ in range(3))
        if b != 0:
            out.append((a, b, c))
    return out


def anneal(seeds, steps, T0=4.0):
    cur = analyse(seeds)
    h = len(seeds)
    while cur is None:
        seeds = rand_seeds(h)
        cur = analyse(seeds)
    best = (cur["T"], cur, list(seeds))
    for st in range(steps):
        temp = max(0.05, T0 * (1 - st / steps))
        ns = list(seeds)
        for _ in range(1 if random.random() < 0.85 else 2):
            i = random.randrange(h)
            v = list(ns[i])
            v[random.randrange(3)] += random.choice([-1, 1]) * random.choice(SCALES)
            if v[1] == 0:
                continue
            ns[i] = tuple(v)
        r = analyse(ns)
        if r is None:
            continue
        if r["T"] >= cur["T"] or random.random() < pow(2.718281828, (r["T"] - cur["T"]) / temp):
            seeds, cur = ns, r
            if r["T"] > best[0]:
                best = (r["T"], r, list(seeds))
    return best


if __name__ == "__main__":
    K = int(sys.argv[1]); restarts = int(sys.argv[2]); steps = int(sys.argv[3])
    random.seed(int(sys.argv[4]))
    hist = {}; top = []
    for r in range(restarts):
        T, res, seeds = anneal(rand_seeds(K // 2), steps)
        hist[T] = hist.get(T, 0) + 1
        top.append((T, res["fixed"], seeds))
        top.sort(key=lambda x: -x[0]); top = top[:5]
        print(f"restart {r}: T={T} fixed={res['fixed']} seeds={seeds}", flush=True)
    print("HIST", json.dumps({str(k): v for k, v in sorted(hist.items())}), flush=True)
    for T, f, seeds in top:
        print("TOP", T, f, seeds, "exact=", exact(seeds), flush=True)
