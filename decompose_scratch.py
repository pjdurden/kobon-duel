
import random
from kobon import corpus, table

C = corpus.by_key()
base = C["kobon_14_53tri"]["table"]
n = 14
L = 15

def build_no_row15(front_back):
    t = [list(r) for r in base]
    t[10] = t[10][:1] + [L] + t[10][1:]
    t[11] = t[11][:1] + [L] + t[11][1:]
    for i in range(1, n+1):
        if i in (11,12):
            continue
        row = t[i-1]
        if front_back[i] == "front":
            t[i-1] = [L] + row
        else:
            t[i-1] = row + [L]
    return t

def build(front_back, order15):
    t = build_no_row15(front_back)
    t.append(list(order15))
    return t

rows_fb = [i for i in range(1,15) if i not in (11,12)]
rnd = random.Random(42)
best = (-1, None, None)
for trial in range(4000):
    fb = dict((i, rnd.choice(["front","back"])) for i in rows_fb)
    order15 = list(range(1,15))
    rnd.shuffle(order15)
    t = build(fb, order15)
    try:
        table.validate(t)
    except ValueError:
        continue
    c = table.count(t)
    if c > best[0]:
        best = (c, dict(fb), list(order15))

fb_best = best[1]
print("fb_best recovered, count-at-that-order15:", best[0])

t_base_only = build_no_row15(fb_best)
pos = {}
for i in range(1, n+1):
    row = t_base_only[i-1]
    along = {}
    for idx, e in enumerate(row):
        along[e] = idx
    pos[i] = along

def crosses_between(i, a, b, x):
    along = pos[i]
    if x not in along or a not in along or b not in along:
        return False
    lo, hi = sorted((along[a], along[b]))
    return lo < along[x] < hi

pairs = [(a,b) for a in range(1,15) for b in range(a+1,15)]
S_total = 0
per_pair_S = {}
for a,b in pairs:
    s = 0
    for x in range(1,15):
        if x in (a,b):
            continue
        t2 = crosses_between(a, L, b, x)
        t3 = crosses_between(b, L, a, x)
        target = t2 ^ t3
        s += target
    per_pair_S[(a,b)] = s
    S_total += s

m = 14
C_fixed = sum((q-p-1) for p in range(m) for q in range(p+1,m))
print("S_total", S_total)
print("C_fixed", C_fixed)
print("lower_bound", abs(C_fixed - S_total))

vals = sorted(per_pair_S.values())
print("per_pair_S min/max/mean", vals[0], vals[-1], sum(vals)/len(vals))
