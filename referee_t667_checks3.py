"""REFEREE turn 667, part 3: the coverage-fraction denominator, and the x=8 chain.

T657 -> T658 -> T662 -> T663 all price search coverage against ((k-1)!)^k, the
space of arbitrary row-tuples.  Almost none of that space is an arrangement.
Here is the real denominator at small k, by exhaustive flip-graph enumeration.

Run: python3 referee_t667_checks3.py
"""
import itertools
import math
import random
from fractions import Fraction as F
from kobon import corpus, table, verify

C = corpus.by_key()
random.seed(6673)


def sec(s):
    print()
    print("=" * 74)
    print(s)


def flips(t):
    out = []
    for tri in table.triangles(t):
        tb = [list(r) for r in t]
        ok = True
        for i in tri:
            a, b = [x for x in tri if x != i]
            row = tb[i - 1]
            ia, ib = row.index(a), row.index(b)
            if abs(ia - ib) != 1:
                ok = False
                break
            row[ia], row[ib] = row[ib], row[ia]
        if ok:
            out.append(tb)
    return out


def key(t):
    return tuple(tuple(r) for r in t)


def table_from_lines(lines):
    k = len(lines)
    rows = []
    for i in range(k):
        a, b, c = lines[i]
        # direction vector along line i
        dx, dy = -b, a
        others = []
        for j in range(k):
            if j == i:
                continue
            p = verify.intersect(lines[i], lines[j])
            if p is None:
                return None
            others.append((p[0] * dx + p[1] * dy, j + 1))
        others.sort()
        if len(set(x for x, _ in others)) != len(others):
            return None          # concurrence
        rows.append([j for _, j in others])
    return rows


def random_simple(k):
    while True:
        lines = [(F(random.randint(-40, 40)), F(random.randint(-40, 40)),
                  F(random.randint(-40, 40))) for _ in range(k)]
        t = table_from_lines(lines)
        if t is not None:
            return t


# ------------------------------------------------------- the real denominator
sec("667(h)  what the coverage denominator actually is")
print("   T657/T658 price k=13 coverage against (12!)^9 = 1.33e78.")
print("   T662 prices k=19 coverage against (18!)^19 = 1.0e301.")
print("   Both denominators count arbitrary row-tuples.  A row-tuple is an")
print("   arrangement only if it is reciprocal AND realizable as a wiring")
print("   diagram.  Exhaustive flip-graph enumeration at small k:")
print()
print("   %3s %14s %20s %12s" % ("k", "flip component", "((k-1)!)^k", "ratio"))
for k in (4, 5, 6):
    seed = random_simple(k)
    seen = {key(seed)}
    frontier = [seed]
    while frontier:
        nxt = []
        for t in frontier:
            for tb in flips(t):
                kk = key(tb)
                if kk not in seen:
                    seen.add(kk)
                    nxt.append(tb)
        frontier = nxt
    naive = math.factorial(k - 1) ** k
    print("   %3d %14d %20.3e %12.3e" % (k, len(seen), naive, len(seen) / naive))
print()
print("   The gap is already 5 orders of magnitude at k=6 and grows")
print("   super-exponentially.  ((k-1)!)^k is not the space either agent")
print("   searched; the flip component is, and its size is unknown at k=13")
print("   and k=19 but is smaller than the naive count by a factor that")
print("   dwarfs every coverage fraction quoted this window.")

# ------------------------------------------------------- x=8 chain
sec("667(i)  the x=8 deletion chain (T652-T656), spot-reproduced")


def delete_line(t, x):
    k = len(t)
    new = []
    for i in range(1, k + 1):
        if i == x:
            continue
        row = [j for j in t[i - 1] if j != x]
        new.append([j - 1 if j > x else j for j in row])
    return new


base14 = [list(r) for r in C["kobon_14_53tri"]["table"]]
cen = {x: table.count(delete_line(base14, x)) for x in range(1, 15)}
print("   14-way deletion census: %s   max %d" % (list(cen.values()), max(cen.values())))

d8 = delete_line(base14, 8)
pos = table.positions(d8)
par = [(i, j) for i in range(1, 14) for j in range(i + 1, 14) if j not in pos[i]]
print("   x=8: T'=%d  p=%d  pairs %s" % (table.count(d8), len(par), par))


def free(t, i, j):
    tris = set(frozenset(x) for x in table.triangles(t))
    row = t[i - 1]
    return frozenset((i, row[j], row[j + 1])) not in tris


print("   criterion pair rows 10/11 at gap 0: row10[0]=%d row11[0]=%d free=%s,%s"
      % (d8[9][0], d8[10][0], free(d8, 10, 0), free(d8, 11, 0)))


def insert(row, lab, p):
    r = list(row)
    r.insert(p, lab)
    return r


best = -1
dist = {}
n1, n2 = len(d8[0]), len(d8[1])
n3, n4 = len(d8[2]), len(d8[3])
for p1 in range(n1 + 1):
    for p2 in range(n2 + 1):
        for p3 in range(n3 + 1):
            for p4 in range(n4 + 1):
                t = [list(r) for r in d8]
                t[0] = insert(t[0], 2, p1)
                t[1] = insert(t[1], 1, p2)
                t[2] = insert(t[2], 4, p3)
                t[3] = insert(t[3], 3, p4)
                c = table.count(t)
                dist[c] = dist.get(c, 0) + 1
                best = max(best, c)
print("   combined {1,2}x{3,4} insertion sweep: %d combos, best %d, dist %s"
      % (sum(dist.values()), best, dict(sorted(dist.items()))))

# ------------------------------------------------------- T650 / T651
sec("667(j)  kobon_11_32tri incidence and mutual row-extreme pairs (T650, T651)")
t11 = [list(r) for r in C["kobon_11_32tri"]["table"]]
deg = table.incidence_degrees(t11)
print("   T=%d  per-line incidence %s" % (table.count(t11), [deg[i] for i in range(1, 12)]))
pos11 = table.positions(t11)
pairs = []
for i in range(1, 12):
    for j in range(i + 1, 12):
        ri, rj = t11[i - 1], t11[j - 1]
        if (ri[0] == j or ri[-1] == j) and (rj[0] == i or rj[-1] == i):
            pairs.append((i, j))
print("   mutual row-extreme pairs: %s" % (pairs,))
print("   incidences there: %s" % ([(deg[i], deg[j]) for i, j in pairs],))
tris11 = set(frozenset(x) for x in table.triangles(t11))
fg = [(i, j) for i in range(1, 12) for j in range(len(t11[i - 1]) - 1)
      if frozenset((i, t11[i - 1][j], t11[i - 1][j + 1])) not in tris11]
print("   free_gaps: %s   extremal free: %d"
      % (fg, sum(1 for (i, j) in fg if j == 0 or j == len(t11[i - 1]) - 2)))

# ------------------------------------------------------- T646 construction
sec("667(k)  T646's corrected 13-line coordinate construction")
lines = [(F(1000), F(-1), F(1000)), (F(-1000), F(-1), F(1000))]
for i in range(1, 12):
    lines.append((F(i), F(-1), -F(i) - F(i * i, 1000)))
conc = 0
for a, b, c in itertools.combinations(range(13), 3):
    p1 = verify.intersect(lines[a], lines[b])
    p2 = verify.intersect(lines[a], lines[c])
    if p1 is not None and p1 == p2:
        conc += 1
par = sum(1 for a, b in itertools.combinations(range(13), 2)
          if verify.intersect(lines[a], lines[b]) is None)
T = verify.triangles(lines)
inc = [0] * 13
for (a, b, c, _) in T:
    inc[a] += 1
    inc[b] += 1
    inc[c] += 1
print("   concurrent triples %d of 286, parallel pairs %d, verify.count = %d"
      % (conc, par, len(T)))
print("   per-line incidence %s   (T647 reported [1,2,3,3,3,3,3,3,3,3,3,2,1])" % inc)
