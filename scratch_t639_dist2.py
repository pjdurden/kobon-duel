
import copy, itertools
from kobon import corpus, table as T
import referee_t593_checks as R

def flip(t, tri):
    a, b, c = tri
    t2 = [list(row) for row in t]
    def swap_adjacent(row, x, y):
        ix = iy = None
        for idx, e in enumerate(row):
            if e == x: ix = idx
            if e == y: iy = idx
        if ix is None or iy is None or abs(ix - iy) != 1:
            raise ValueError("not adjacent")
        row[ix], row[iy] = row[iy], row[ix]
    swap_adjacent(t2[a-1], b, c)
    swap_adjacent(t2[b-1], a, c)
    swap_adjacent(t2[c-1], a, b)
    return t2

def key_of(t):
    return tuple(tuple(row) for row in t)

def all_flips(t):
    out = []
    for tri in T.triangles(t):
        t2 = flip(t, tri)
        T.validate(t2)
        out.append((tri, t2))
    return out

def parity_violations(tb):
    pos = T.positions(tb)
    k = len(tb)
    bad = inst = 0
    for i, j, m in itertools.combinations(range(1, k+1), 3):
        if j not in pos[i] or m not in pos[i] or m not in pos[j]:
            continue
        if pos[i][j] == pos[i][m] or pos[j][i] == pos[j][m] or pos[m][i] == pos[m][j]:
            continue
        for x in range(1, k+1):
            if x in (i,j,m): continue
            inst += 1
            bad += (T._crosses_between(pos, i, j, m, x)
                    + T._crosses_between(pos, j, i, m, x)
                    + T._crosses_between(pos, m, i, j, x)) % 2
    return bad, inst

B = corpus.by_key()["kobon_13_m_sym_47tri"]["table"]
base_key = key_of(B)
n0 = T.count(B)
print("base count", n0)

# distance 1
d1 = all_flips(B)
hist1 = {}
d1_tables = {}
for tri, t2 in d1:
    c = T.count(t2)
    hist1[c] = hist1.get(c, 0) + 1
    d1_tables.setdefault(key_of(t2), t2)
print("distance-1: flips", len(d1), "hist", hist1, "distinct tables", len(d1_tables))

# distance 2: flip every distance-1 table again
d2_tables = {}
total_d2_flips = 0
for k1, t1 in d1_tables.items():
    for tri, t2 in all_flips(t1):
        total_d2_flips += 1
        kk = key_of(t2)
        if kk == base_key:
            continue
        d2_tables.setdefault(kk, t2)

hist2 = {}
for kk, t2 in d2_tables.items():
    c = T.count(t2)
    hist2[c] = hist2.get(c, 0) + 1
print("distance-2: total flip-applications", total_d2_flips, "distinct new tables", len(d2_tables), "hist", hist2)

t47_d1 = [t for t in d1_tables.values() if T.count(t) == 47]
t47_d2 = [t for t in d2_tables.values() if T.count(t) == 47]
print("distinct T=47 tables at distance 1 (excluding base):", len(t47_d1))
print("distinct T=47 tables at distance 2 (excluding base):", len(t47_d2))

for label, lst in [("d1", t47_d1), ("d2", t47_d2)]:
    for t in lst:
        gaps = R.free_gaps(t)
        R_ = len(t[0]) + 1  # not used directly
        info = []
        extremal_flags = []
        for (i, j) in gaps:
            row = t[i-1]
            is_ext = (j == 0) or (j == len(row) - 2)
            extremal_flags.append(is_ext)
        crit_hit = False
        if len(gaps) == 2:
            (r1i, j1), (r2i, j2) = gaps
            row1 = t[r1i-1]; row2 = t[r2i-1]
            crit_hit = R.criterion(row1, j1, r2i, row2, j2, r1i)
        b, ins = parity_violations(t)
        same_as_base = (key_of(t) == base_key)
        print(label, "key!=B" if not same_as_base else "SAME AS B",
              "free_gaps", gaps, "extremal", extremal_flags,
              "criterion", crit_hit, "parity", b, "/", ins)
