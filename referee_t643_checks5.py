"""REFEREE turn 643, part 5: T626's 456/4536 partition of T598's zero table."""
import itertools
from kobon import corpus, table
from referee_t618_checks2 import build, FB, ROW15, total_parity

C = corpus.by_key()
t = build(FB, ROW15)
table.validate(t)
n = len(t)
pos = table.positions(t)
base = C["kobon_14_53tri"]["table"]
bpos = table.positions(base)
par = [(i, j) for i in range(1, 15) for j in range(i + 1, 15) if j not in bpos[i]]
print("   base parallel pairs:", par)
forced = free = fbad = frbad = 0
for i, j, m in itertools.combinations(range(1, n + 1), 3):
    if j not in pos[i] or m not in pos[i] or m not in pos[j]:
        continue
    if pos[i][j] == pos[i][m] or pos[j][i] == pos[j][m] or pos[m][i] == pos[m][j]:
        continue
    for x in range(1, n + 1):
        if x in (i, j, m):
            continue
        b = (table._crosses_between(pos, i, j, m, x)
             + table._crosses_between(pos, j, i, m, x)
             + table._crosses_between(pos, m, i, j, x)) % 2
        isf = any(tuple(sorted((x, p))) in [tuple(sorted(q)) for q in par]
                  for p in (i, j, m))
        if isf:
            forced += 1; fbad += b
        else:
            free += 1; frbad += b
print("   table.count = %d, total parity %s" % (table.count(t), total_parity(t)))
print("   parallel-forced instances: %d bad of %d" % (fbad, forced))
print("   free instances:            %d bad of %d" % (frbad, free))
