from referee_t713_s1ball import to_table, T701_93
from referee_t691_par import build
from kobon import corpus, table as T


def inv(t):
    d = T.incidence_degrees(t)
    tris = T.triangles(t)
    prof = sorted(tuple(sorted(d[x] for x in tri)) for tri in tris)
    rl = sorted(len(r) for r in t)
    return sorted(d.values()), rl, prof


rec = corpus.by_key()["kobon_18_93tri"]["table"]
new = to_table(build(T701_93))
a, b = inv(rec), inv(new)
print("record  line degrees:", a[0])
print("T701_93 line degrees:", b[0])
print("row lengths equal:", a[1] == b[1], a[1])
print("triangle degree-profile identical:", a[2] == b[2])
print("T record", T.count(rec), "T new", T.count(new))
