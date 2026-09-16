"""Referee T691: a real search of the C3 k=18 orbit family.

Two modes: free (maximise T) and s1 (maximise T subject to s == 1, the residue
condition 94 requires). Seeds printed for every reported object.
"""
import random, sys, json
from referee_t691_fast import analyse, exact_check

SCALES = [1, 1, 2, 2, 4, 8, 16, 32]


def rand_seeds(scale=45):
    return [tuple(random.randint(-scale, scale) for _ in range(3)) for _ in range(6)]


def obj(r, mode):
    if r is None:
        return None
    if mode == "s1":
        return r["T"] if r["s"] == 1 else r["T"] - 60
    return r["T"]


def anneal(seeds, steps, mode, T0=4.0):
    cur = analyse(seeds)
    while cur is None:
        seeds = rand_seeds()
        cur = analyse(seeds)
    best = (obj(cur, mode), cur, list(seeds))
    for st in range(steps):
        temp = max(0.05, T0 * (1 - st / steps))
        ns = list(seeds)
        nmoves = 1 if random.random() < 0.85 else 2
        for _ in range(nmoves):
            i = random.randrange(6)
            v = list(ns[i])
            v[random.randrange(3)] += random.choice([-1, 1]) * random.choice(SCALES)
            ns[i] = tuple(v)
        r = analyse(ns)
        if r is None:
            continue
        o_new, o_cur = obj(r, mode), obj(cur, mode)
        if o_new >= o_cur or random.random() < pow(2.718281828, (o_new - o_cur) / temp):
            seeds, cur = ns, r
            if o_new > best[0]:
                best = (o_new, r, list(seeds))
    return best


if __name__ == "__main__":
    mode = sys.argv[1]
    restarts = int(sys.argv[2])
    steps = int(sys.argv[3])
    random.seed(int(sys.argv[4]))
    hall = []
    hist = {}
    for r in range(restarts):
        o, res, seeds = anneal(rand_seeds(), steps, mode)
        hist[res["T"]] = hist.get(res["T"], 0) + 1
        hall.append((res["T"], res["s"], res["d"], seeds))
        hall.sort(key=lambda x: -x[0])
        hall = hall[:8]
        print(f"restart {r}: T={res['T']} s={res['s']} d={res['d']} seeds={seeds}", flush=True)
    print("HIST", json.dumps({str(k): v for k, v in sorted(hist.items())}), flush=True)
    print("TOP:", flush=True)
    for T, s, d, seeds in hall:
        eT, eS = exact_check(seeds)
        print(f"  T={T} s={s} d={d} seeds={seeds}  exact=({eT},{eS})", flush=True)
