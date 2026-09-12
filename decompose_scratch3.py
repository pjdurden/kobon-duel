
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


import random as _r
rnd5 = _r.Random(2024)
results = []
for trial in range(3000):
    fb2 = dict((i, rnd5.choice(["front","back"])) for i in rows_fb)
    t_b = build_no_row15(fb2)
    pos2 = {}
    for i in range(1, n+1):
        row = t_b[i-1]
        along = {}
        for idx, e in enumerate(row):
            along[e] = idx
        pos2[i] = along
    def cb(i,a,b,x,pos2=pos2):
        along = pos2[i]
        if x not in along or a not in along or b not in along:
            return False
        lo, hi = sorted((along[a], along[b]))
        return lo < along[x] < hi
    S2 = 0
    for a,b in pairs:
        s = 0
        for x in range(1,15):
            if x in (a,b):
                continue
            tt2 = cb(a, L, b, x)
            tt3 = cb(b, L, a, x)
            s += (tt2 ^ tt3)
        S2 += s
    lb2 = abs(C_fixed - S2)
    results.append((lb2, S2, fb2))

results.sort(key=lambda r: r[0])
print("min lower_bound over 3000 fb draws:", results[0][0], "S_total:", results[0][1])
print("max lower_bound:", results[-1][0])
print("median-ish:", results[len(results)//2][0])
print("count of fb with lower_bound == 0:", sum(1 for r in results if r[0]==0))


good_fb = [r[2] for r in results if r[0] == 0]
print("num good fb (lower_bound 0):", len(good_fb))

def total_parity_violations(t):
    from itertools import combinations
    nn = len(t)
    posx = table.positions(t)
    bad = 0
    inst = 0
    for i,j,m in combinations(range(1,nn+1), 3):
        if j not in posx[i] or m not in posx[i] or m not in posx[j]:
            continue
        if posx[i][j]==posx[i][m] or posx[j][i]==posx[j][m] or posx[m][i]==posx[m][j]:
            continue
        for x in range(1, nn+1):
            if x in (i,j,m):
                continue
            inst += 1
            s = (table._crosses_between(posx, i, j, m, x)
                 + table._crosses_between(posx, j, i, m, x)
                 + table._crosses_between(posx, m, i, j, x)) % 2
            bad += s
    return bad, inst

def hillclimb(fb, start_order, iters=150):
    order = list(start_order)
    t = build(fb, order)
    cur, inst = total_parity_violations(t)
    improved = True
    rounds = 0
    while improved and rounds < iters:
        improved = False
        rounds += 1
        for a in range(14):
            for b in range(a+1, 14):
                order[a], order[b] = order[b], order[a]
                t2 = build(fb, order)
                try:
                    table.validate(t2)
                except ValueError:
                    order[a], order[b] = order[b], order[a]
                    continue
                v, _ = total_parity_violations(t2)
                if v < cur:
                    cur = v
                    improved = True
                else:
                    order[a], order[b] = order[b], order[a]
    return cur, order

rnd6 = _r.Random(555)
overall = None
for gi, gfb in enumerate(good_fb[:5]):
    for _ in range(3):
        order0 = list(range(1,15))
        rnd6.shuffle(order0)
        v, o = hillclimb(gfb, order0, iters=100)
        print("good_fb", gi, "hillclimb ->", v)
        if overall is None or v < overall[0]:
            overall = (v, gfb, o)

print("BEST over good_fb hillclimbs:", overall[0])
