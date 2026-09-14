"""REFEREE turn 643, part 4: reproduce the two flip censuses (T638, T639).

Run:  python3 referee_t643_checks4.py
"""
from kobon import corpus, table


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
                ok = False; break
            if abs(ia - ib) != 1:
                ok = False; break
            row[ia], row[ib] = row[ib], row[ia]
        if ok:
            out.append((tuple(sorted(tri)), tb))
    return out


def key(t):
    return tuple(tuple(r) for r in t)


C = corpus.by_key()

print("=" * 74)
print("49(h)  T638: flip distance 2 from kobon_17_85tri")
t17 = [list(r) for r in C["kobon_17_85tri"]["table"]]
d1 = {}
for _, tb in flips(t17):
    d1[key(tb)] = tb
print("   distance 1: %d distinct, counts %s"
      % (len(d1), {c: sum(1 for tb in d1.values() if table.count(tb) == c)
                   for c in sorted({table.count(tb) for tb in d1.values()})}))
mult = {}
d2 = {}
for tb in d1.values():
    for _, tc in flips(tb):
        c = table.count(tc)
        mult[c] = mult.get(c, 0) + 1
        k = key(tc)
        if k != key(t17) and k not in d1:
            d2[k] = tc
print("   distance-2 flips with multiplicity: %d, count histogram %s"
      % (sum(mult.values()), dict(sorted(mult.items()))))
h2 = {}
for tb in d2.values():
    c = table.count(tb); h2[c] = h2.get(c, 0) + 1
print("   distance 2: %d distinct NEW tables, counts %s"
      % (len(d2), dict(sorted(h2.items()))))
print("   any table.count == 84 at distance <= 2:",
      any(table.count(tb) == 84 for tb in list(d1.values()) + list(d2.values())))

print()
print("=" * 74)
print("49(i)  T639: flip distances 1-3 from kobon_13_m_sym_47tri")
B = [list(r) for r in C["kobon_13_m_sym_47tri"]["table"]]
seen = {key(B)}
frontier = {key(B): B}
for dist in (1, 2, 3):
    nxt = {}
    for tb in frontier.values():
        for _, tc in flips(tb):
            k = key(tc)
            if k not in seen and k not in nxt:
                nxt[k] = tc
    seen |= set(nxt)
    h = {}
    for tb in nxt.values():
        c = table.count(tb); h[c] = h.get(c, 0) + 1
    print("   distance %d: %5d distinct new tables, counts %s"
          % (dist, len(nxt), dict(sorted(h.items()))))
    frontier = nxt
print("   any T = 47 at distance 1-3 other than the base:",
      any(table.count(tb) == 47 for tb in frontier.values()))
