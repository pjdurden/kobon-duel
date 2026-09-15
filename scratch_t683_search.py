
import random
from kobon import verify

def orbit(seed):
    a,b,c = seed
    lines=[(a,b,c)]
    for _ in range(2):
        a,b,c = lines[-1]
        lines.append((b-a,-a,c))
    return lines

def build(seeds):
    lines=[]
    for s in seeds:
        lines.extend(orbit(s))
    return lines

def simple(lines):
    L = verify.normalize(lines)
    n=len(L)
    for i in range(n):
        for j in range(i+1,n):
            if verify.intersect(L[i],L[j]) is None:
                return False
    seen={}
    for i in range(n):
        for j in range(i+1,n):
            p = verify.intersect(L[i],L[j])
            seen.setdefault(p, set()).update([i,j])
    for p, idxs in seen.items():
        if len(idxs) > 2:
            return False
    return True

def s_value(lines):
    tris = verify.triangles(lines)
    s = 0
    for (i,j,k,verts) in tris:
        oi, oj, ok = i//3, j//3, k//3
        if oi==oj==ok:
            s += 1
    return s, len(tris)

def score(seeds):
    lines = build(seeds)
    if not simple(lines):
        return None
    s, T = s_value(lines)
    return T, s

def rand_seed(scale=40):
    return (random.randint(-scale,scale), random.randint(-scale,scale), random.randint(-scale,scale))

def anneal(seeds0, steps, scales, T0=3.0, require_s1=False):
    seeds = list(seeds0)
    cur = score(seeds)
    while cur is None:
        seeds=[rand_seed() for _ in range(6)]
        cur = score(seeds)
    best = (cur, list(seeds))
    for step in range(steps):
        temp = T0 * (1 - step/steps)
        i = random.randrange(len(seeds))
        scale = random.choice(scales)
        a,b,c = seeds[i]
        coord = random.randrange(3)
        delta = random.choice([-scale, scale])
        newv = [a,b,c]
        newv[coord]+=delta
        newseeds = list(seeds)
        newseeds[i] = tuple(newv)
        sc = score(newseeds)
        if sc is None:
            continue
        T_new, s_new = sc
        T_cur, s_cur = cur
        if require_s1:
            obj_new = T_new if s_new==1 else T_new - 100
            obj_cur = T_cur if s_cur==1 else T_cur - 100
        else:
            obj_new, obj_cur = T_new, T_cur
        accept = obj_new >= obj_cur or (temp>0 and random.random() < pow(2.71828, (obj_new-obj_cur)/max(temp,0.01)))
        if accept:
            seeds = newseeds
            cur = sc
            if s_new==1 and T_new > best[0][0] and best[0][1]==1:
                best = (sc, list(seeds))
            elif best[0][1] != 1 and s_new == 1:
                best = (sc, list(seeds))
    return best

if __name__ == "__main__":
    import sys
    random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 0)
    n_restarts = int(sys.argv[2]) if len(sys.argv)>2 else 10
    n_steps = int(sys.argv[3]) if len(sys.argv)>3 else 300
    require_s1 = len(sys.argv)>4 and sys.argv[4]=="s1"
    results=[]
    for r in range(n_restarts):
        seeds0=[rand_seed() for _ in range(6)]
        best = anneal(seeds0, n_steps, scales=[1,2,4,8,16,32], require_s1=require_s1)
        results.append(best)
    results.sort(key=lambda x: (x[0][1]==1, x[0][0]), reverse=True)
    for (T,s), seeds in results[:10]:
        print(T, s, seeds)
