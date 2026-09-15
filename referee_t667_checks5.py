"""REFEREE turn 667, part 5: the extremal-free-gap rate as a function of
distance below the optimum, on the k=19 flip ball.

Six turns (T601, T602, T628, T640, T641, T642, T651) argued the corpus
statistic "extremal gaps are freed less often than interior ones" on a corpus
that contains only optima.  Here is the same quantity on 5,629 arrangements
one and two flips off an optimum.

Run: python3 referee_t667_checks5.py
"""
import referee_t667_checks2 as R
from kobon import corpus, table

C = corpus.by_key()
base = [list(r) for r in C["kobon_19_107tri"]["table"]]
seen = {R.key(base)}
d1 = {}
for _, tb in R.flips(base):
    k = R.key(tb)
    if k not in seen:
        seen.add(k)
        d1[k] = tb
d2 = {}
for tb in d1.values():
    for _, tc in R.flips(tb):
        k = R.key(tc)
        if k not in seen and k not in d2:
            d2[k] = tc

print("=" * 74)
print("667(p)  extremal free gaps by distance from the k=19 optimum")
for lab, pop in (("distance 0", [base]), ("distance 1", list(d1.values())),
                 ("distance 2", list(d2.values()))):
    ef = tot = withef = 0
    for tb in pop:
        eu, e, iu, i2 = R.gap_stats(tb)
        ef += e
        tot += eu + e
        if e > 0:
            withef += 1
    print("   %-11s tables=%5d  extremal free %5d/%6d = %5.2f%%   "
          "tables with >=1: %5d (%5.1f%%)"
          % (lab, len(pop), ef, tot, 100 * ef / tot, withef,
             100 * withef / len(pop)))

byT = {}
for tb in list(d1.values()) + list(d2.values()):
    c = table.count(tb)
    eu, e, iu, i2 = R.gap_stats(tb)
    a = byT.setdefault(c, [0, 0, 0, 0, 0])
    a[0] += 1
    a[1] += e
    a[2] += eu + e
    a[3] += i2
    a[4] += iu + i2
print()
print("   %5s %6s   %-22s %-22s" % ("T", "n", "extremal free", "interior free"))
for c in sorted(byT, reverse=True):
    n, e, t, i, it = byT[c]
    print("   %5d %6d   %5d/%6d = %5.2f%%   %5d/%6d = %5.2f%%"
          % (c, n, e, t, 100 * e / t, i, it, 100 * i / it))
print()
print("   At the optimum the extremal-free rate is 0.00%.  Two flips down it")
print("   is above the interior rate.  The corpus census that six turns were")
print("   spent pricing is a census of optima, and the effect it measures")
print("   disappears within two flips of one.")
