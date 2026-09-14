
from fractions import Fraction as F
from kobon import verify
from itertools import combinations

lines = []
labels = []
lines.append((F(1000), F(-1), F(1000))); labels.append("a")
lines.append((F(-1000), F(-1), F(1000))); labels.append("b")
for i in range(1,12):
    lines.append((F(i), F(-1), F(-i) - F(i*i,1000))); labels.append("c%d" % i)

n = len(lines)
print("n lines", n)

concurrent_triples = []
for i,j,k in combinations(range(n),3):
    pij = verify.intersect(lines[i], lines[j])
    pjk = verify.intersect(lines[j], lines[k])
    pik = verify.intersect(lines[i], lines[k])
    if pij is None or pjk is None or pik is None:
        continue
    if pij == pjk == pik:
        concurrent_triples.append((labels[i],labels[j],labels[k]))
print("concurrent triples count", len(concurrent_triples))
print(concurrent_triples[:20])

parallel_pairs = []
for i,j in combinations(range(n),2):
    if verify.intersect(lines[i], lines[j]) is None:
        parallel_pairs.append((labels[i],labels[j]))
print("parallel pairs", parallel_pairs)

tris = verify.triangles(lines)
print("triangle count", len(tris))
tri_labels = [frozenset((labels[i],labels[j],labels[k])) for i,j,k,_ in tris]
for t in sorted(tuple(sorted(x)) for x in tri_labels):
    print(t)
print("uses a:", sum(1 for t in tri_labels if "a" in t))
print("uses b:", sum(1 for t in tri_labels if "b" in t))
