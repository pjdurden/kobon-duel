
from fractions import Fraction as F
from kobon import verify, table
from itertools import combinations
import sys
sys.path.insert(0, ".")
from referee_t593_checks import criterion, free_gaps

lines = []
labels = []
lines.append((F(1000), F(-1), F(1000))); labels.append(1)   # a
lines.append((F(-1000), F(-1), F(1000))); labels.append(2)  # b
for i in range(1,12):
    lines.append((F(i), F(-1), F(-i) - F(i*i,1000))); labels.append(2+i)  # c_i -> label i+2

n = len(lines)
idx_of_label = {lab: i for i, lab in enumerate(labels)}

# build rows: for each line, sort OTHER lines by x-coord of intersection point
rows = []
for row_idx in range(n):
    pts = []
    for j in range(n):
        if j == row_idx:
            continue
        p = verify.intersect(lines[row_idx], lines[j])
        pts.append((p[0], labels[j]))
    pts.sort()
    rows.append([lab for _, lab in pts])

t = [rows[i] for i in range(n)]
print("row 1 (a):", t[0])
print("row 13 (c11):", t[12])

print("validate:", table.validate(t))
tc = table.triangles(t)
print("table.count:", len(tc))
vtris = verify.triangles(lines)
print("verify.count:", len(vtris))

fg = free_gaps(t)
print("free_gaps:", fg)

# criterion: row 1 (a), j=len-2=10, other label=13(c11); row13(c11), j=10, other label=1(a)
r1 = t[0]
r13 = t[12]
print("r1 len", len(r1), "r13 len", len(r13))
j1 = len(r1) - 2
j13 = len(r13) - 2
print("j1", j1, "j13", j13)
print("r1[j1:]", r1[j1:])
print("r13[j13:]", r13[j13:])
res = criterion(r1, j1, 13, r13, j13, 1)
print("criterion fires:", res)
print("(1,%d) in free_gaps:" % j1, (1, j1) in fg)
print("(13,%d) in free_gaps:" % j13, (13, j13) in fg)
