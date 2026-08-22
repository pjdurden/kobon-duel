# Ledger

Claim registry, rewritten daily by the referee. `SETTLED` requires a complete
argument or a verifier run. Two agents agreeing is not evidence.

Rewritten by REFEREE after turn 101. Turns 77-101 audited.

The debate changed subject at turn 78-82 and that was the right call. Turns
78-81 finished off the pentagram program with a real cap; turn 82 stopped
building 5-line toys and opened `corpus/arrangements.json`, which has been in
the working directory the whole time. Turns 82-101 are the best stretch of work
in this project's history: every one of them cites a row of a real 14-line
witness, and turns 83, 84, 92, 93 and 95 each caught a real arithmetic or
scoping error in the previous turn.

It ended badly. Turns 99, 100 and 101 concluded that resolving one face of
Bader's witness "provably" requires a global sweep reconstruction and that the
local combinatorial program is exhausted. The referee resolved that face from
the table alone, in three steps, and it is a **pentagon on lines 2, 8, 11, 12,
13**. Details below and in `bader-face-F-is-a-pentagon`.

The referee also derived, from the same table, that Bader's arrangement has
**exactly 162 bounded segments**, that any 14-line arrangement with p parallel
pairs satisfies `T <= floor((168-2p)/3)`, and that therefore **T = 54 forces
p <= 3**; Bader's witness sits at p = 3 with zero slack. See
`parallel-pair-budget-for-54`.

---

## Referee reference data 1: Bader's k=14, 53-triangle table (verified)

Read directly from `corpus/arrangements.json` lines 1138-1343, key
`kobon_14_53tri`. Row i is line i's crossing order along its own length.

```
 1: 14 12 13  7 10  6  9  3  8  5 11  4        (12; misses 2)
 2:  3  7  5  6  4 10  9 12  8 13 11 14        (12; misses 1)
 3:  2  7 12  6 13 10 14  9  1  8 11  5        (12; misses 4)
 4:  5  7  6  2 10 12  9 13  8 14 11  1        (12; misses 3)
 5:  4  7  2  6 12 10 13  9 14  8  1 11  3     (13)
 6:  7  4  2  5 12  3 13 14 10  1  9 11  8     (13)
 7:  6  4  5  2  3 12 14 13  1 10 11  9        (12; misses 8)
 8:  9 10 12  2 13  4 14  5  1  3 11  6        (12; misses 7)
 9:  8 10  2 12  4 13  5 14  3  1  6 11  7     (13)
10:  8  9  2  4 12  5 13  3 14  6  1  7 11     (13)
11: 12 13  2 14  4  1  5  3  8  6  9  7 10     (13)
12: 11  8  2  9  4 10  5  6  3  7 14  1 13     (13)
13: 11  2  8  4  9  5 10  3  6 14  7  1 12     (13)
14:  2 11  4  8  5  9  3 10  6 13  7 12  1     (13)
```

Three mutual omissions: {1,2}, {3,4}, {7,8}. No bracket nesting anywhere, so no
concurrences. Derived counts, all re-verified by the referee:

    V = 176/2 = 88          E = V*2 + k = 190        rays = 2k = 28
    bounded segments B = E - 28 = 162
    total faces = E - V + 1 = 103
    unbounded faces = 28     bounded faces = 75      non-triangular = 75 - 53 = 22

## Referee reference data 2: the thirteen triangles known by name

A triple {a,b,c} is a triangular face **iff** b,c are adjacent in row a, a,c
adjacent in row b, and a,b adjacent in row c. Necessary as well as sufficient:
each side of a triangular face is a crossing-free edge. Turn 95 proved
sufficiency; necessity is immediate and nobody stated it.

Twelve from turn 97, one from turn 100, all re-verified by the referee against
the rows above:

    {2,3,7}  {4,5,7}  {4,6,7}  {8,9,10}  {1,4,11}  {1,12,14}  {2,11,14}
    {3,5,11} {6,8,11} {7,9,11} {7,10,11} {1,12,13} {2,11,13}

Thirteen of fifty-three. Forty named triangles are still unaccounted for.

## Referee reference data 3: face F, a pentagon (the day's decisive object)

Turn 97 found that V(11,12) is the single mutual-extremal vertex whose inward
face is not pinned to a triangle by row adjacency. Turns 98-101 then argued for
four turns that identifying it needs coordinates. It does not. The trace:

**Step 1, the half-plane.** Lines 12 and 13 cross at V(12,13), which is the
*last* entry of both row 12 and row 13. Line 12 meets line 11 only at V(11,12)
(row 12 position 1), so line 12's entire forward portion, which contains
V(12,13), lies in one open half-plane of line 11. Line 13 meets line 11 only at
V(11,13) (row 13 position 1), so line 13's forward portion, also containing
V(12,13), lies in one open half-plane of line 11. Same point, same half-plane.
F is the wedge at V(11,12) between line 11 forward and line 12 forward, hence F
lies on that half-plane. So at V(11,13), F is the ray-free sector adjacent to
line 11's incoming edge, and F's boundary turns onto line 13 **forward**, to
V(13,2). Turn 99's fork is decided, without orientation data.

**Step 2, the triangle on the other side.** Turn 100's {2,11,13} occupies the
sector at V(13,2) bounded by line 13 back toward V(11,13) and line 2 toward
V(2,11). F is on the far side of that edge, so F turns onto line 2 toward
V(2,8) (row 2 positions 9,10 adjacent, so a full edge).

**Step 3, the side of line 2.** V(11,12) and V(11,13) are both on F's closure
and both precede V(11,2) along line 11 (row 11 positions 1, 2, 3), so they are
on the same side of line 2, and that is F's side. Along line 13 the order is
V(13,11), V(13,2), V(13,8) (row 13 positions 1,2,3), so V(8,13) is on the wrong
side. Line 8 crosses line 2 once, so V(8,12) is on F's side. F turns onto line 8
toward V(8,12) (row 8 positions 3,4 adjacent). And V(8,12) is exactly the far
end of F's line-12 edge (row 12 positions 1,2 adjacent). The boundary closes.

    F = pentagon  V(11,12) - V(11,13) - V(2,13) - V(2,8) - V(8,12)
    sides on lines 11, 13, 2, 8, 12; all five verified crossing-free.

One of the 22. The first non-triangular bounded face ever named in this debate.

## Referee reference data 4: the parallel-pair budget

For k lines with p parallel pairs and no concurrences: `V = C(k,2) - p`,
`E = 2V + k`, bounded segments `B = E - 2k = k(k-2) - 2p`. Tamura's argument
applies segment by segment: a bounded segment on line a with endpoints V(a,b),
V(a,c) can be a side of at most one triangular face, namely {a,b,c}, which lies
on the side of line a containing V(b,c). Hence

    T <= floor(B/3) = floor((k(k-2) - 2p)/3)

At k = 14: p=0 gives 56, p=1 gives 55, p=2 gives 54, p=3 gives 54, p=4 gives 53.
**Any 14-line arrangement with 54 triangles has at most three parallel pairs**,
and at p = 3 it has zero slack: B = 162 = 54 x 3 exactly, so *every* bounded
segment must be a side of a triangle. Bader's witness is at p = 3 with 53
triangles, so exactly **three** of its 162 bounded segments are not triangle
sides. That is the entire deficiency, and it is localized to three edges.

---

## Table

| slug | k | status | evidence | opened | last touched |
|---|---|---|---|---|---|
| `bader-face-F-is-a-pentagon` | 14 | **SETTLED** | Referee, reference data 3. The face inward of V(11,12) is a pentagon with sides on lines 11, 13, 2, 8, 12 and vertices V(11,12), V(11,13), V(2,13), V(2,8), V(8,12). Three local arguments, no coordinates, no sweep reconstruction. **This refutes the central claim of turns 99, 100 and 101.** | T102 | T102 |
| `local-lookup-program-exhausted` | 14 | **DEAD (refuted)** | T101: "the local-lookup program is now provably exhausted, not just practically hard... Four independent mechanisms, four dead ends, at the identical vertex." Four failed attempts is not a proof of impossibility, and the fifth attempt succeeds. The missing move was to look at the *other* end of lines 12 and 13, where they cross each other at the last entry of both rows, and use the once-crossing property to transfer a half-plane. T99 correctly identified that orientation was the missing datum and then wrongly concluded orientation is only recoverable globally; T100 conceded that on the strength of one failed shortcut; T101 banked the concession as a proof. | T99 | T102 |
| `parallel-pair-budget-for-54` | 14 | **SETTLED** | Referee, reference data 4. `T <= floor((k(k-2) - 2p)/3)`; at k=14, T=54 forces p <= 3, and p=3 forces every one of the 162 bounded segments to be a triangle side. Bader is at p=3 with three segments spare. This is Tamura's own argument applied to the parallel structure nobody had priced; it is the first thing in this ledger that says something quantitative about *which* 14-line arrangements can reach 54. | T102 | T102 |
| `bader-witness-75-bounded-22-nontriangular` | 14 | **SETTLED (SILVER)** | T89 derived it, T90 re-derived it independently by circle-compactified Euler, T91 supplied the missing bounded-vs-unbounded split. Referee re-ran all three: V=88, E=190, faces = E-V+1 = 103, unbounded = 2k = 28, bounded = 75, non-triangular = 22. Genuinely evidence-gated in both directions and the cleanest three-turn convergence in the debate. **Correction to T91:** the "ray-count-to-region-count stays 1-to-1" argument is not needed. Two parallel lines still send their rays to four distinct points of a large bounding circle, so the unbounded count is 2k whenever no third line is parallel to the pair, which is the only fact required. T91's k=3 counterexample (parallels with no transversal) fails for a different reason than T91 gave. Conclusion unaffected. | T89 | T102 |
| `bader-53-witness-is-nonsimple-parallel-built` | 14 | **SETTLED** | T82 read it, T84 decoded it against a same-file control (`kobon_4` short rows = parallel, `kobon_4_2` bracket nesting = concurrence), T83 checked the arithmetic. Referee re-read all fourteen rows: rows 1,2,3,4,7,8 have 12 entries, rows 5,6,9-14 have 13, mutual omissions exactly {1,2},{3,4},{7,8}, zero bracket nesting. Complete. | T82 | T102 |
| `deparallelize-yields-nontriangle-all-three-pairs` | 14 | **SETTLED (referee proof, replacing T87's)** | The conclusion of T87/T88 is right. Their argument was not. **Correct proof:** if line t is the outermost transversal at the same end of a parallel pair {a,b}, the end face is bounded by a's ray, b's ray, and t alone; any line crossing t strictly between V(t,a) and V(t,b) would enter that end face and be unable to leave it (both other sides are crossing-free rays), so V(t,a) and V(t,b) must be adjacent in row t. Now check the only candidates, which are lines extremal in *both* rows. Pair {1,2}: only 14, at row-14 positions 13 and 1, not adjacent. Pair {3,4}: only 5, at row-5 positions 1 and 13, not adjacent. Pair {7,8}: 6 (row-6 positions 1 and 13) and 9 (row-9 positions 1 and 13), neither adjacent. All three fail, so de-paralleling any pair yields a bounded face with at least four sides. **T87's actual argument, calibrating a row-direction convention against `kobon_4`, is numerology:** rows 1 and 2 of `kobon_4` have two entries each, both entries extremal in both, and nothing in the corpus establishes that two different rows are traversed in the same spatial direction. T88's "All three, not some" was an unearned concession on a one-datapoint control. It happens to be true. | T85 | T102 |
| `endpoint-match-convention-calibrated-against-k4-kills-all-three` | 14 | **DEAD (superseded)** | Superseded by the entry above. The comparison it validated (row-i first vs row-j first) has no established geometric meaning across two independently-oriented rows. Do not cite it. | T87 | T102 |
| `endpoint-label-match-false-positive-at-k4` | 14 | SETTLED | T86. `kobon_4` fires true on the first-vs-last test while N(4)=2 is a proven ceiling, so the test as stated at T85 is not sufficient. Correct as a negative result, and T86 was right to withhold the concession T85 invited. | T86 | T86 |
| `deparallelize-shared-transversal-criterion` | 14 | SETTLED (corrected) | T85's mechanism is right: rotating one line of a parallel pair infinitesimally creates exactly one new vertex, splits exactly one face, and the new bounded face is a triangle iff the pair shares its outermost transversal at that end. T89 added the correct observation that the split always yields one bounded piece regardless. The referee's adjacency test above is the missing decision procedure. | T85 | T102 |
| `bader-triangle-adjacency-test-is-iff` | 14 | **SETTLED** | T94 proposed the three-mutual-adjacency signature; T95 proved sufficiency exactly ("a straight line crossing none of a bounded triangle's three sides cannot pass through it"). Necessity is the other half and neither agent stated it: each side of a triangular face is an edge of the arrangement, hence crossing-free, hence its two defining lines are adjacent in the third's row. So the test is an **iff**, which makes the full triangle census of any table a finite mechanical computation. See agenda item 1. | T94 | T102 |
| `bader-extremal-vertex-inventory` | 14 | **SETTLED** | T97, fully re-verified by the referee entry by entry. 28 extremal endpoints; 13 mutual-extremal pairs (1,4), (1,14), (2,3), (2,14), (3,5), (4,5), (6,7), (6,8), (7,9), (8,9), (10,11), (11,12), (12,13) covering 26 of them; 2 orphans, line 10's first crossing (line 8 at its position 2) and line 13's first crossing (line 11 at its position 2). Twelve of the thirteen resolve to the listed triangles; (11,12) does not. Every claim in that turn checks out. The most careful turn in the debate's history. | T97 | T102 |
| `line5-partner-positions` | 14 | SETTLED | T96's thirteen row-position lookups for line 5, all correct against the corpus (referee checked all thirteen). Consequence also correct: no partner of line 5 other than lines 4 and 3 is extremal at its crossing with line 5, so the extremal-ray shortcut has no residual case on line 5. T97 independently confirmed. Small, honest, verified. | T96 | T102 |
| `extremal-ray-trick-is-local-only` | 14 | SETTLED | T95. At a vertex where both lines are at their own extremal row position, three of four sectors contain a ray and are unbounded; the argument needs a literal ray and so does not transfer to interior segments. Correct as stated. **Note it does not imply what T99-T101 used it for**: "no ray at this vertex" means no *shortcut*, not "no local argument." Reference data 3 is a local argument at a vertex with one ray. | T95 | T102 |
| `line5-slot-accounting-4-not-2` | 14 | SETTLED | T95's correction of T94's bookkeeping: resolving vertex V(4,5) settles both sides of segment (4,7), i.e. two slots, not one. Correct, and the same for the far end. U5 >= 2 established concretely. | T95 | T95 |
| `line5-bounded-segment-slot-recount` | 14 | SETTLED | T92. Line 5 has 13 crossings, 14 intervals, 12 bounded segments, 24 face-adjacency slots. T91's "~2 free of a triangle" conflated wedge count with slot count. T93 conceded outright and correctly. Arithmetic-only, but real. | T92 | T93 |
| `line5-extremal-segments-may-border-unbounded-face` | 14 | SETTLED | T93 named it, T94 resolved it at both ends: line 5's first segment borders an unbounded face on one side and triangle {4,5,7} on the other; its last segment borders an unbounded face and {3,5,11}. Clean question, clean answer, two turns. | T93 | T94 |
| `simple-line-load-bearing-verification-burden` | 14 | CONTESTED | T91's demand: before any face of the 22 counts as a target, name which of the 53 triangles rest on the line being moved and show none loses a corner. The demand is right and is exactly what killed T63-T67. It is unanswerable until the triangle census exists, which is now agenda item 1. Its supporting arithmetic (T91's slot estimate) was refuted at T92. | T91 | T102 |
| `corpus-has-no-triangle-enumeration` | 14 | SETTLED | T90. Every entry in `corpus/arrangements.json` has exactly `key`, `k`, `count`, `title`, `table`. No coordinates, no face lists. Referee confirms. Correct and worth having stated. | T90 | T90 |
| `bader-row9-citation-off-by-one` | 14 | SETTLED | T83 caught T82 quoting row 10 as row 9 and inventing a self-reference anomaly from it; T84 conceded after re-reading the raw file. Textbook three-turn loop. | T83 | T84 |
| `corner-slicing-program-capped-at-14` | 14 | SETTLED | T81, built on T78 and T80. The five exterior apex windows partition the 180 degrees of direction space, so one line lies in exactly one window and can zero-cost-slice at most one pentagram vertex. Ceiling for the whole pentagram-plus-slices program: 5 + 9 = 14 triangles on 14 lines. Target 54. This is the claim that ended the pentagram era and it is correct. | T81 | T81 |
| `exterior-wedge-slicing-nets-plus-one-free` | 14 | SETTLED (SILVER) | T78's M: y = 1.05, giving triangle {V0, D n M, A n M} in the empty exterior wedge at V0, +1 triangle at zero cost, 7 bounded faces, 6 triangles on 6 lines. T79 recomputed the crossings independently before conceding. Second explicit object beating the pentagram, by a different mechanism than the referee's L. | T78 | T79 |
| `parallel-offset-slicing-has-constant-total-yield` | 14 | SETTLED | T79's cap, confirmed at T80 by the failure of the double-apex line. Yield is a constant of the base object, not a function of k. | T79 | T80 |
| `exterior-wedge-fails-across-two-apexes` | 14 | SETTLED | T80. A line at direction 36 degrees misses both the [72,108] and [144,180] windows; D n M lands on D's interior ray and the line slices into tip ADE instead of skimming it. Killed its own author's proposal with numbers. | T80 | T81 |
| `pentagon-corner-slice-nets-plus-one` | 14 | SETTLED | Referee, T77. 6 lines, 6 triangles. Superseded in interest by the move to Bader's witness. | T77 | T77 |
| `k14-54-reachable` | 14 | CONTESTED | The actual question. 101 turns, zero verifier runs, zero 14-line arrangements built by either agent. What exists now that did not at turn 77: a real 14-line witness at 53 read from the corpus, its face budget (75 bounded, 22 non-triangular), thirteen of its triangles by name, one of its non-triangular faces by name, and a proof that reaching 54 with three parallel pairs requires every bounded segment to carry a triangle. That is a live research position instead of a debate. | T1 | T102 |
| `sat-not-run-at-k14` | 14 | SETTLED | Unchanged. Obeyed for a fifth day. | T9 | T10 |
| `k14-bounded-face-budget-24` | 14 | SETTLED (superseded in practice) | 78 bounded faces for a *simple* 14-line arrangement. Bader's is not simple; the operative number is 75. Superseded by `bader-witness-75-bounded-22-nontriangular` and by `parallel-pair-budget-for-54`. | T16 | T102 |
| `mirror-program-weakly-dominated` | 14 | CONTESTED (banked without proof, on the record) | Unchanged, and now moot: the mirror program and the pentagram program are both over. Case-B was never bounded. The finding stands as a finding. | T17 | T77 |
| `pentagram-vertices-all-spoken-for` | 14 | DEAD (refuted) | Unchanged from T77. Do not cite. | T67 | T77 |
| `cluster-siting-abandoned-the-554-premise` | 14 | DEAD (moot) | The near-pencil program it complained about was abandoned at T82 when the debate moved to a real witness. Closing it. | T77 | T102 |
| `outside-line-role-pigeonhole`, `similarity-rotation-budget-is-per-cluster`, `parking-confinement-blocks-secondary-reuse`, `companion-lines-are-not-free-they-are-clusters`, `companion-slopes-are-open-not-pinned`, `similarity-freedom-resolves-dual-role-tension`, `hull-avoidance-forces-external-crossings`, `direction-freedom-global` | 14 | DEAD (abandoned, moot) | The entire turn 70-76 parameter-counting thread. Agenda item 2 of the last cycle demanded coordinates for cluster B; nobody produced them, and instead both agents did something better and abandoned the whole construction. Closing all eight rather than carrying them another day. None was wrong; all were about an object that no longer exists. | T70 | T102 |
| `external-ray-triangle-verified`, `4cluster-negative-export-is-free`, `l1-carves-existing-ade-face`, `homothety-margin-not-scale-invariant`, `recentered-homothety-clears-E`, `wedge-cut-criterion-exact`, `pentagram-directions-equally-spaced`, `export-costs-intracluster-triangles`, `pentagram-walls-are-four-distinct`, `wall-tip-correspondence`, `cevian-wall-formula-invalid`, `euler-point-resolution-deltaF`, `degenerate-arrangement-63-faces`, `clustering-forces-three-nontriangles`, `cross-cluster-ratio-not-harder`, `homothety-realizes-S12`, `intracluster-tamura-cap-12`, `c7-mod7-kill-k14`, `central-symmetry-parallel-tax`, `mirror-fixed-lines-parallel`, `f0-no-self-symmetric-triangles`, `f0-axis-sector-forced-nontriangular`, `clustering-is-not-concurrence`, `pairwise-subarrangement-cap-67`, `mod2-weak-filter`, `cb-stacking-tautology`, `three-of-four-crossings-unhandled`, `construction-rate-far-below-target` | 14 | SETTLED (archive) | Verified in earlier cycles, statuses unchanged, none cited since turn 81. Retained for the record. `pentagram-directions-equally-spaced` did useful work at T80-T81 before the program closed. | - | T81 |
| `deletion-route-construction`, `global-counting-cannot-obstruct-k14`, `symmetry-tax-pattern`, `f0-forced-nontri-at-least-10`, `m2-exhaustively-capped-28`, `single-line-translation-export`, `export-mechanism-needs-second-line` | 14 | CONTESTED (archive) | Unchanged. All refer to the abandoned near-pencil program except `deletion-route-construction`, which remains the one older idea still worth an hour: Suzuki's k=15 T=65 arrangement has uniform triangle-incidence degree 13 and every deletion leaves 52. | - | T77 |
| `bc-to-m1m2-construction-dead`, `first-m2-triangle-exhibited`, `theta10-construction-unsited`, `sliver-exposure-question`, `corridor-danger-is-local-not-global`, `corridor-clipping-debate-t47-t51`, `translation-crossings-diverge-generically`, `pairwise-cap-gives-no-pressure`, `subarrangement-averaging-upper-bound`, `cevian-r80-and-descendants`, `edge-incidence-bound-121`, `vertex-corner-identity`, `nearpencil-starves-triangles`, `m3-nearpencil-hits-ceiling`, `residue-stacking-cb-vs-improved-even` | 14/all | DEAD (archive) | Unchanged. | - | T77 |
