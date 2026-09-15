"""REFEREE turn 667, part 2: the k=19 flip ball (T661/T662/T663) and the
orbit-triangle congruence at k=18.

Run: python3 referee_t667_checks2.py
"""
import random
from fractions import Fraction as F
from kobon import corpus, table, verify

C = corpus.by_key()
random.seed(6672)


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
            try:
                ia, ib = row.index(a), row.index(b)
            except ValueError:
                ok = False
                break
            if abs(ia - ib) != 1:
                ok = False
                break
            row[ia], row[ib] = row[ib], row[ia]
        if ok:
            out.append((tuple(sorted(tri)), tb))
    return out


def key(t):
    return tuple(tuple(r) for r in t)


def free_gaps(t):
    """(row, j) for every bounded gap j of row i not used as a triangle side."""
    tris = set(frozenset(x) for x in table.triangles(t))
    out = []
    for i, row in enumerate(t, start=1):
        for j in range(len(row) - 1):
            if frozenset((i, row[j], row[j + 1])) not in tris:
                out.append((i, j))
    return out


def gap_stats(t):
    tris = set(frozenset(x) for x in table.triangles(t))
    ext_u = ext_f = int_u = int_f = 0
    for i, row in enumerate(t, start=1):
        last = len(row) - 2
        for j in range(len(row) - 1):
            used = frozenset((i, row[j], row[j + 1])) in tris
            if j == 0 or j == last:
                if used:
                    ext_u += 1
                else:
                    ext_f += 1
            else:
                if used:
                    int_u += 1
                else:
                    int_f += 1
    return ext_u, ext_f, int_u, int_f


def mutual_extremal_free_pairs(t):
    tris = set(frozenset(x) for x in table.triangles(t))
    pos = table.positions(t)
    out = []
    for i, row_i in enumerate(t, start=1):
        for j, row_j in enumerate(t, start=1):
            if j <= i:
                continue
            ri, rj = list(row_i), list(row_j)
            for (gi, gj) in ((0, 0), (0, len(rj) - 2),
                             (len(ri) - 2, 0), (len(ri) - 2, len(rj) - 2)):
                if gi < 0 or gj < 0:
                    continue
                if j not in (ri[gi], ri[gi + 1]):
                    continue
                if i not in (rj[gj], rj[gj + 1]):
                    continue
                if frozenset((i, ri[gi], ri[gi + 1])) in tris:
                    continue
                if frozenset((j, rj[gj], rj[gj + 1])) in tris:
                    continue
                out.append((i, gi, j, gj))
    return out


def parallels(t):
    k = len(t)
    pos = table.positions(t)
    return [(i, j) for i in range(1, k + 1) for j in range(i + 1, k + 1)
            if j not in pos[i]]


def concurrences(t):
    return sum(1 for row in t for e in row if isinstance(e, (list, tuple)))


# ------------------------------------------------------------- calibration
sec("667(d)  flips() calibrated against reference data 48a")
for name in ("kobon_17_85tri", "kobon_13_m_sym_47tri"):
    t = [list(r) for r in C[name]["table"]]
    h = {}
    for _, tb in flips(t):
        c = table.count(tb)
        h[c] = h.get(c, 0) + 1
    print("   %-22s %3d flips  %s" % (name, len(flips(t)), dict(sorted(h.items()))))

# ------------------------------------------------------------- k=19 ball
sec("667(e)  k=19 flip ball from kobon_19_107tri  (T661, T662)")
base = [list(r) for r in C["kobon_19_107tri"]["table"]]
print("   base T = %d  p = %d  c = %d" % (table.count(base), len(parallels(base)),
                                          concurrences(base)))
seen = {key(base)}
d1 = {}
for _, tb in flips(base):
    k1 = key(tb)
    if k1 in seen:
        continue
    seen.add(k1)
    d1[k1] = tb
h1 = {}
for tb in d1.values():
    c = table.count(tb)
    h1[c] = h1.get(c, 0) + 1
print("   distance 1: %d distinct new   %s" % (len(d1), dict(sorted(h1.items()))))

d2 = {}
for tb in d1.values():
    for _, tc in flips(tb):
        k2 = key(tc)
        if k2 in seen or k2 in d2:
            continue
        d2[k2] = tc
for k2 in d2:
    seen.add(k2)
h2 = {}
for tb in d2.values():
    c = table.count(tb)
    h2[c] = h2.get(c, 0) + 1
print("   distance 2: %d distinct new   %s" % (len(d2), dict(sorted(h2.items()))))
print("   T=107 anywhere else: %s"
      % any(table.count(tb) == 107 for tb in list(d1.values()) + list(d2.values())))

t106 = [tb for tb in list(d1.values()) + list(d2.values()) if table.count(tb) == 106]
t105 = [tb for tb in list(d1.values()) + list(d2.values()) if table.count(tb) == 105]
print()
print("   T'=106 tables: %d      T'=105 tables: %d" % (len(t106), len(t105)))
for n, tb in enumerate(t106):
    eu, ef, iu, ifr = gap_stats(tb)
    print("   T106-%d  p=%d c=%d  F'=%d  ext %d/%d free  int %d/%d free  mutual-ext-free pairs %d"
          % (n, len(parallels(tb)), concurrences(tb), ef + ifr,
             ef, eu + ef, ifr, iu + ifr, len(mutual_extremal_free_pairs(tb))))
    print("          free gaps: %s" % (free_gaps(tb),))

sig = {}
for tb in t105:
    eu, ef, iu, ifr = gap_stats(tb)
    m = len(mutual_extremal_free_pairs(tb))
    sig[(eu, ef, m > 0)] = sig.get((eu, ef, m > 0), 0) + 1
print("   T'=105 signatures (ext_used, ext_free, has_mutual_ext_free_pair): %s"
      % dict(sorted(sig.items())))

# ------------------------------------------------------------- T662 / T663
sec("667(f)  T662 and T663: flipping the T'=105 tables once more")
good = [tb for tb in t105 if mutual_extremal_free_pairs(tb)]
print("   T'=105 with a mutual extremal free pair: %d" % len(good))
tot = 0
h = {}
for tb in good:
    for _, tc in flips(tb):
        tot += 1
        c = table.count(tc)
        h[c] = h.get(c, 0) + 1
print("   T662: %d flips of those -> %s" % (tot, dict(sorted(h.items()))))

tot = 0
hits = set()
for tb in t105:
    for _, tc in flips(tb):
        tot += 1
        if table.count(tc) == 106:
            hits.add(key(tc))
print("   T663: %d flips of all 18 -> %d distinct T'=106 tables, all already known: %s"
      % (tot, len(hits), hits <= set(key(x) for x in t106)))

# T663's cross-tab: does the swap touching an extremal slot predict ext_f>0 ?
tab = {}
for tri, tb in flips(base):
    touched = False
    for i in tri:
        row = base[i - 1]
        a, b = [x for x in tri if x != i]
        ia = row.index(a)
        ib = row.index(b)
        if min(ia, ib) == 0 or max(ia, ib) == len(row) - 1:
            touched = True
    ef = gap_stats(tb)[1]
    tab[(touched, ef > 0)] = tab.get((touched, ef > 0), 0) + 1
print("   T663 cross-tab (swap at extremal, ext_f>0): %s  total %d"
      % (dict(sorted(tab.items())), sum(tab.values())))

# ------------------------------------------------------------- b at k=18
sec("667(g)  order-3 at k=18: the orbit-triangle congruence T = b (mod 3)")
M = [[0, 1], [-1, -1]]


def map_line(Mm, line):
    a, b, c = line
    d = Mm[0][0] * Mm[1][1] - Mm[0][1] * Mm[1][0]
    Mi = [[F(Mm[1][1], d), F(-Mm[0][1], d)], [F(-Mm[1][0], d), F(Mm[0][0], d)]]
    MiT = [[Mi[0][0], Mi[1][0]], [Mi[0][1], Mi[1][1]]]
    return (MiT[0][0] * F(a) + MiT[0][1] * F(b),
            MiT[1][0] * F(a) + MiT[1][1] * F(b), F(c))


seeds = [(-16, 10, -8), (2, -7, -11), (18, -8, -10), (9, 7, 6), (-6, -2, 6),
         (-1, -21, 2)]
lines, orbit_of = [], {}
for oi, s in enumerate(seeds):
    L = (F(s[0]), F(s[1]), F(s[2]))
    for _ in range(3):
        orbit_of[len(lines)] = oi
        lines.append(L)
        L = map_line(M, L)
T = verify.triangles(lines)
b = sum(1 for (i, j, k, _) in T if len({orbit_of[i], orbit_of[j], orbit_of[k]}) == 1)
print("   my best k=18 order-3 arrangement: T = %d, orbit-triangles b = %d"
      % (len(T), b))
print("   T mod 3 = %d, b mod 3 = %d  ->  congruence holds: %s"
      % (len(T) % 3, b % 3, len(T) % 3 == b % 3))
print("   target 94 mod 3 = %d, so 94 needs b in {1,4}; not excluded at k=18."
      % (94 % 3))
