"""REFEREE turn 643, part 3: the global slot census, and the labelling hole in
T637's flip-distance floor.

Run:  python3 referee_t643_checks3.py
"""
import math, random
from kobon import corpus, table
from referee_t643_checks2 import gap_census, bracketfree, tamura

C = corpus.by_key()

print("=" * 74)
print("49(f)  extremal vs interior free rates over EVERY bracket-free record")
tE = tEf = tI = tIf = 0
per = []
for name, rec in sorted(C.items()):
    t = rec["table"]
    if not bracketfree(t) or len(t) < 4:
        continue
    eu, ef, iu, if_, _ = gap_census(t)
    if ef + if_ == 0:
        continue
    per.append((name, len(t), table.count(t), tamura(len(t)), eu + ef, ef, iu + if_, if_))
    tE += eu + ef; tEf += ef; tI += iu + if_; tIf += if_
for row in per:
    print("   %-24s k=%2d T=%3d/%3d  extremal free %d/%-3d (%.1f%%)"
          "  interior free %d/%-4d (%.2f%%)"
          % (row[0], row[1], row[2], row[3], row[5], row[4],
             100 * row[5] / row[4], row[7], row[6], 100 * row[7] / row[6]))
print("   ------")
print("   TOTAL  extremal free %d/%d = %.2f%%   interior free %d/%d = %.2f%%"
      % (tEf, tE, 100 * tEf / tE, tIf, tI, 100 * tIf / tI))
N, E, F = tE + tI, tE, tEf + tIf
p_ge = sum(math.comb(E, a) * math.comb(N - E, F - a)
           for a in range(tEf, min(E, F) + 1)) / math.comb(N, F)
p_le = sum(math.comb(E, a) * math.comb(N - E, F - a)
           for a in range(0, tEf + 1)) / math.comb(N, F)
print("   pooled: %d free slots of %d, %d extremal slots. E[extremal free] = %.2f,"
      " observed %d" % (F, N, E, F * E / N, tEf))
print("   one-sided P(>= observed) = %.4f ;  P(<= observed) = %.4f" % (p_ge, p_le))

print()
print("=" * 74)
print("49(g)  T637's numerator: is 66 a property of the order types or of the")
print("       corpus's arbitrary line labelling?")


def tset(t):
    return set(frozenset(x) for x in table.triangles(t))


A = [list(r) for r in C["kobon_21_133tri_1"]["table"]]
B = [list(r) for r in C["kobon_21_133tri_2"]["table"]]
D = [list(r) for r in C["kobon_21_133tri_3"]["table"]]
for n1, t1, n2, t2 in (("_1", A, "_2", B), ("_1", A, "_3", D), ("_2", B, "_3", D)):
    print("   |tris(%s) D tris(%s)| = %d" % (n1, n2, len(tset(t1) ^ tset(t2))))


def relabel(t, perm):
    """perm: dict old->new label."""
    k = len(t)
    out = [None] * k
    for i, row in enumerate(t, start=1):
        out[perm[i] - 1] = [perm[x] for x in row]
    return out


def anneal(t1, t2, seed, iters=200000):
    """Minimise |tris(t1) D tris(relabel(t2,perm))| over relabellings of t2."""
    rnd = random.Random(seed)
    k = len(t2)
    s1 = tset(t1)
    perm = {i: i for i in range(1, k + 1)}
    cur = len(s1 ^ tset(relabel(t2, perm)))
    best = cur
    Temp = 6.0
    for step in range(iters):
        Temp = 4.0 * (1 - step / iters) + 0.01
        a, b = rnd.sample(range(1, k + 1), 2)
        perm[a], perm[b] = perm[b], perm[a]
        new = len(s1 ^ tset(relabel(t2, perm)))
        if new <= cur or rnd.random() < math.exp((cur - new) / Temp):
            cur = new
            best = min(best, cur)
        else:
            perm[a], perm[b] = perm[b], perm[a]
    return best


for n1, t1, n2, t2 in (("_1", A, "_2", B), ("_1", A, "_3", D), ("_2", B, "_3", D)):
    b = min(anneal(t1, t2, s, 4000) for s in (1, 2))
    print("   min over relabellings (annealed, 2x4k) |tris(%s) D tris(%s')| <= %d"
          % (n1, n2, b))
