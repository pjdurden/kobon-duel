"""Referee T691: deep re-anneal of the axis-absent f_perp=0 mirror family from
the best witnesses of the first sweep."""
import random, sys, json
from referee_t691_mirror import analyse, anneal, exact, rand_seeds

STARTS_14 = [
    [(162,252,-149),(225,-102,32),(-19,-153,-79),(-54,55,-84),(58,-82,43),(-135,-32,24),(-1,109,-10)],
    [(-154,108,-5),(-136,44,-140),(17,-233,-24),(54,19,-8),(-35,34,42),(-176,111,62),(-43,-38,-74)],
    [(4,130,-11),(-57,52,-108),(115,-31,-18),(-37,-146,29),(83,143,5),(-78,75,-75),(-29,-133,-137)],
    [(-3,33,12),(-54,107,-133),(-104,91,-53),(-207,-24,-22),(-55,132,150),(12,4,-16),(168,233,-93)],
    [(-6,46,-119),(96,48,8),(-140,-53,47),(-11,146,43),(-82,20,-31),(-52,62,-69),(91,25,-126)],
]

if __name__ == "__main__":
    reps, steps = int(sys.argv[1]), int(sys.argv[2])
    random.seed(int(sys.argv[3]))
    best = (0, None)
    hist = {}
    for r in range(reps):
        st = [tuple(s) for s in STARTS_14[r % len(STARTS_14)]]
        T, res, seeds = anneal(st, steps)
        hist[T] = hist.get(T, 0) + 1
        if T > best[0]:
            best = (T, seeds)
        print(f"rep {r}: T={T} fixed={res['fixed']} seeds={seeds}", flush=True)
    print("HIST", json.dumps({str(k): v for k, v in sorted(hist.items())}), flush=True)
    print("BEST", best[0], best[1], "exact=", exact(best[1]), flush=True)
