"""REFEREE turn 643, part 2: the free-gap extremality census, priced.

Run:  python3 referee_t643_checks2.py
"""
import itertools, math
from kobon import corpus, table
import referee_t593_checks as R

C = corpus.by_key()


def bracketfree(t):
    return not any(isinstance(e, (list, tuple)) for row in t for e in row)


def gap_census(t):
    """Every bounded segment of every line, classified extremal/interior and
    used/free.  A row of R entries has R-1 gaps; extremal = j in {0, R-2}."""
    tr = set(frozenset(x) for x in table.triangles(t))
    ext_u = ext_f = int_u = int_f = 0
    free = []
    for i, row in enumerate(t, start=1):
        Rl = len(row)
        for j in range(Rl - 1):
            if any(isinstance(e, (list, tuple)) for e in (row[j], row[j + 1])):
                continue
            ex = (j == 0 or j == Rl - 2)
            used = frozenset((i, row[j], row[j + 1])) in tr
            if ex and used: ext_u += 1
            elif ex: ext_f += 1; free.append((i, j, "extremal"))
            elif used: int_u += 1
            else: int_f += 1; free.append((i, j, "interior"))
    return ext_u, ext_f, int_u, int_f, free


def tamura(k):
    return k * (k - 2) // 3


print("=" * 74)
print("49(c)  T641's slot census on kobon_14_53tri, reproduced")
t = C["kobon_14_53tri"]["table"]
eu, ef, iu, if_, free = gap_census(t)
k = len(t)
p = sum(1 for i in range(1, k + 1) for j in range(i + 1, k + 1)
        if j not in table.positions(t)[i])
print("   T = %d   k = %d   parallel pairs p = %d" % (table.count(t), k, p))
print("   k(k-2) = %d   B(k,p,c) = k(k-2) - 2p = %d   segments counted = %d"
      % (k * (k - 2), k * (k - 2) - 2 * p, eu + ef + iu + if_))
print("   extremal: %d used, %d free (of %d)   interior: %d used, %d free (of %d)"
      % (eu, ef, eu + ef, iu, if_, iu + if_))
print("   free list:", free)
N, E, F = eu + ef + iu + if_, eu + ef, ef + if_
# P(>= ef of the F free slots are extremal) under the uniform null
tot = math.comb(N, F)
pv = sum(math.comb(E, a) * math.comb(N - E, F - a)
         for a in range(ef, min(E, F) + 1)) / tot
print("   uniform null: %d free slots among %d, %d extremal."
      " E[extremal free] = %.2f;  P(>= %d) = %.3f" % (F, N, E, F * E / N, ef, pv))

print()
print("=" * 74)
print("49(d)  T642's Tamura-tight census, reproduced and priced")
rows = []
for name, rec in sorted(C.items()):
    t = rec["table"]
    if not bracketfree(t):
        continue
    k = len(t)
    if k < 3 or table.count(t) != tamura(k):
        continue
    eu, ef, iu, if_, free = gap_census(t)
    rows.append((name, k, eu + ef, ef, iu + if_, if_))
    print("   %-24s k=%2d  extremal free %d/%-4d  interior free %d/%-4d"
          % (name, k, ef, eu + ef, if_, iu + if_))
info = [r for r in rows if r[3] + r[5] > 0]
print("   records: %d,  of which with any free gap at all: %d"
      % (len(rows), len(info)))
print("   free gaps across those: %d, extremal among them: %d"
      % (sum(r[3] + r[5] for r in info), sum(r[3] for r in info)))
P = 1.0
for name, k, E, ef, I, if_ in info:
    N, F = E + I, ef + if_
    pz = math.comb(I, F) / math.comb(N, F)
    P *= pz
    print("      %-24s P(all %d free gaps interior) = %.4f" % (name, F, pz))
print("   uniform-null probability of the whole 0-extremal pattern: %.4f" % P)

print()
print("=" * 74)
print("49(e)  the same census over reference data 48h's p'=0 set (T602's 11 gaps)")
tot_g = tot_e = 0; Pb = 1.0
for name, rec in sorted(C.items()):
    t = rec["table"]
    if not bracketfree(t):
        continue
    k = len(t)
    if any(len(r) != k - 1 for r in t):
        continue
    eu, ef, iu, if_, free = gap_census(t)
    if ef + if_ == 0:
        continue
    N, E, F = eu + ef + iu + if_, eu + ef, ef + if_
    Pb *= math.comb(N - E, F) / math.comb(N, F)
    tot_g += F; tot_e += ef
    print("   %-24s k=%2d  T=%3d (Tamura %3d)  free %d, extremal %d,  P(all interior) %.4f"
          % (name, k, table.count(t), tamura(k), F, ef,
             math.comb(N - E, F) / math.comb(N, F)))
print("   total free gaps %d, extremal %d, uniform-null P(0 extremal) = %.4f"
      % (tot_g, tot_e, Pb))
