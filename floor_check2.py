
from kobon import corpus, table
from itertools import combinations

rec = corpus.by_key()["kobon_19_107tri"]["table"]
n = len(rec)
pos = table.positions(rec)

def gap_index(row_list, a, b):
    ia, ib = row_list.index(a), row_list.index(b)
    lo, hi = min(ia, ib), max(ia, ib)
    assert hi == lo + 1
    return lo

row3 = rec[2]
row18 = rec[17]
g3 = gap_index(row3, 19, 1)
g18 = gap_index(row18, 2, 1)

def flag(i, g, j, m):
    if g == "front" or g == "back":
        return 0
    along = pos[i]
    if j not in along or m not in along:
        return 0
    lo, hi = sorted((along[j], along[m]))
    return 1 if lo <= g < hi else 0

def base_floor(slots):
    interior_rows = dict((r, g) for r, g in slots.items() if g != "front" and g != "back")
    odd = 0
    for i, j, m in combinations(range(1, n + 1), 3):
        if j not in pos[i] or m not in pos[i] or m not in pos[j]:
            continue
        if pos[i][j] == pos[i][m]:
            continue
        s = 0
        triples = [(i, j, m), (j, i, m), (m, i, j)]
        for a, b, c in triples:
            if a in interior_rows:
                s += flag(a, interior_rows[a], b, c)
        if s % 2 == 1:
            odd += 1
    return odd

overall_min = None
overall_min_loc = None
for r in range(1, n + 1):
    if r in (3, 18):
        continue
    row_r = rec[r - 1]
    for gi in range(len(row_r) - 1):
        f = base_floor({3: g3, 18: g18, r: gi})
        if overall_min is None or f < overall_min:
            overall_min = f
            overall_min_loc = (r, gi)
print("D=1 full census: rows 1..19 except 3,18, all gaps -> min floor", overall_min, "at", overall_min_loc)
print("baseline (rows 3,18 only) floor = 62")
