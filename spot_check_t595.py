
import itertools
from kobon import corpus, table
import referee_t593_checks as R

C = corpus.by_key()
base = C["kobon_17_85tri"]["table"]
k = len(base)

variants = []
idx = 0
for row_i in range(k):
    row = base[row_i]
    for j in range(len(row)-1):
        idx += 1
        t2 = [list(r) for r in base]
        r = t2[row_i]
        r[j], r[j+1] = r[j+1], r[j]
        t2[row_i] = r
        try:
            table.validate(t2)
        except ValueError:
            continue
        if table.count(t2) != 84:
            continue
        variants.append((idx, t2))

print("total swap positions tried:", idx, "passing T=84:", len(variants))
floors = {}
for vi, t2 in variants:
    g = R.free_gaps(t2)
    if len(g) != 3:
        floors[vi] = ("unexpected free gaps", g)
        continue
    interior = {i: j for i, j in g}
    floors[vi] = R.base_floor(t2, interior)

print("sample floors:", {vi: floors[vi] for vi in list(floors)[:8]})
print("min floor:", min(floors.values()) if floors else None)
print("all positive:", all(v > 0 for v in floors.values() if isinstance(v,int)))
