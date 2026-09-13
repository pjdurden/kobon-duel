"""REFEREE turn 618, part 4: does 47c's criterion survive on a base with
parallels, once the floor is restricted to triples that can be triangles?

Run:  python3 referee_t618_checks4.py
"""
import itertools
from kobon import corpus, table
import referee_t593_checks as R
from referee_t618_checks import floor_restricted

C = corpus.by_key()
t = C["kobon_14_53tri"]["table"]
n = len(t)

rows = range(1, n + 1)
mismatch_all = mismatch_res = tested = zero_all = zero_res = crit = 0
examples = []
for i1, i2 in itertools.combinations(rows, 2):
    for j1 in range(len(t[i1 - 1]) - 1):
        for j2 in range(len(t[i2 - 1]) - 1):
            tested += 1
            fa = R.base_floor(t, {i1: j1, i2: j2})
            fr = floor_restricted(t, {i1: j1, i2: j2})
            cr = R.criterion(t[i1 - 1], j1, i2, t[i2 - 1], j2, i1)
            zero_all += fa == 0
            zero_res += fr == 0
            crit += cr
            if (fa == 0) != cr:
                mismatch_all += 1
            if (fr == 0) != cr:
                mismatch_res += 1
                if len(examples) < 6:
                    examples.append((i1, j1, i2, j2, fa, fr, cr))

print("kobon_14_53tri (p = 3 parallel pairs), every two-interior-row cut:")
print("   %d cuts tested" % tested)
print("   base_floor == 0 : %d      restricted floor == 0 : %d      criterion true : %d"
      % (zero_all, zero_res, crit))
print("   criterion vs base_floor==0   mismatches: %d" % mismatch_all)
print("   criterion vs restricted==0   mismatches: %d" % mismatch_res)
for e in examples:
    print("      i1=%d j1=%d i2=%d j2=%d  base_floor=%d restricted=%d criterion=%s" % e)
