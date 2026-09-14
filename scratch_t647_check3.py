
from fractions import Fraction as F
from kobon import verify

lines = []
labels = []
lines.append((F(1000), F(-1), F(1000))); labels.append(1)
lines.append((F(-1000), F(-1), F(1000))); labels.append(2)
for i in range(1,12):
    lines.append((F(i), F(-1), F(-i) - F(i*i,1000))); labels.append(2+i)

tris = verify.triangles(lines)
from collections import Counter
cnt = Counter()
for i,j,k,_ in tris:
    cnt[labels[i]] += 1
    cnt[labels[j]] += 1
    cnt[labels[k]] += 1
for lab in labels:
    print(lab, cnt.get(lab,0))
print("total triangle-line incidences:", sum(cnt.values()), "= 3*", len(tris))
