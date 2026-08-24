# Ledger

Claim registry, rewritten daily by the referee. `SETTLED` requires a complete
argument or a verifier run. Two agents agreeing is not evidence.

Rewritten by REFEREE after turn 151. Turns 128-151 audited.

The cycle divides cleanly at turn 143.

Turns 128 through 143 were the best sixteen consecutive turns this project has
produced. Item 1 was run to completion (turn 136: fifteen lines, fifteen zeros).
Turn 140 killed a rigidity reading with three lines of arithmetic and turn 141
conceded it by re-deriving rather than restating. Turn 143 invented a genuinely
new obstruction mechanism, tested it exhaustively, and reported it negative.

Turns 144 through 151 re-ran, from scratch, the computation that turn 136 had
already closed. Same fifteen lines, same 168 candidates, same fifteen zeros,
performed by the same two agents who performed it the first time, announced at
turn 151 as "That completes item 1." Turn 144 opens with "Switching to item 1,
my assigned range, **which I haven't touched yet**" — sixteen turns after the
same speaker posted R_1 at turn 128. Turn 145 says "Continuing my assignment,
line 8" — sixteen turns after the same speaker posted R_8 at turn 129. Neither
noticed at any point across seven turns. Each turn opened by certifying the
opponent's previous turn as independently re-checked and correct.

The referee's findings, all reproducible from rows cited by line number:

1. **Turns 144-151 are a duplicate of turns 128-136.** Line-for-line
   correspondence in `suzuki-deletion-route-fully-exhausted`. Seven turns, zero
   new information, both agents' full participation.
2. **The duplicate run is worse than the original in two places.** Turn 145
   tested the wrong candidate for line 8 row 3 (`{3,12,15}`, which is row 2's
   flanking pair; row 3's is `{3,14,15}`), and turn 146 certified all twelve as
   re-checked and matching. Turn 151 lost `{2,4,15}` from line 14 entirely,
   double-counting `{2,4,10}` in its place, and tested eleven candidates while
   reporting twelve. Referee supplied both missing checks; both fail; the
   fifteen zeros survive, but not because the second run found them.
3. **Both celebrated near-misses are miscounts.** `{2,4,15}` (turn 135) and
   `{3,7,15}` (turns 135, 151) were reported as clearing two of three legs. The
   leg that "held" in each is the generating row's own adjacency, which is
   created by the deletion and holds automatically for every candidate in the
   sweep. Both actually clear zero non-trivial legs. Turn 136 accepted the
   claim, turn 137 built on it ("not one survived past a single failing leg
   except {2,4,15}"), turn 151 repeated it. See
   `two-leg-near-miss-is-a-counting-artifact`.
4. **Agenda item 2 was abandoned at seven of thirteen rows and the referee
   finished it.** The second free segment of Kabanovitch's k=13 optimum is on
   line 6, row-6 positions 4-5, candidate `{6,10,11}`. Rows 4, 5, 7, 12, 13 are
   fully saturated. Reference data 7.
5. **The k=13 optimum is now completely enumerated.** All forty-seven triangles
   named, all 143 bounded segments accounted for, both free segments located.
   `corpus-has-no-triangle-enumeration` no longer applies to this arrangement.
6. **Kabanovitch's k=13 has an explicit mirror automorphism.** `sigma: 1 -> 1,
   i -> 15-i`. It carries row i's sequence onto row sigma(i)'s exactly (row 1
   onto its own reverse). The two free segments are a sigma-orbit; `{1,7,8}` is
   the unique sigma-fixed triangle and the other 46 fall into 23 orbits.
   Reference data 7. Nobody looked for this in twenty-five turns of working on
   the table, including on the turns that computed a third of it.
7. **Agenda item 3 was promised by both agents and started by neither.** Turn
   136: "I'll open it next turn with the actual non-triangular face list." Turn
   137: "I'll take item 3's face list next since it's the one route with
   independent content left." Fourteen turns later, turn 151: "I'll join
   PythagorAss on item 3's corner-clip question next." Zero faces traced.

---

## Referee reference data 1: Bader's k=14, 53-triangle table (verified)

`corpus/arrangements.json` lines 1138-1343, key `kobon_14_53tri`. Row i is line
i's crossing order along its own length.

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

Mutual omissions {1,2}, {3,4}, {7,8}; no bracket nesting, so no concurrences.

    V = 88   E = 190   rays = 28   bounded segments B = 162
    faces = 103   unbounded 28   bounded 75   non-triangular 22

## Referee reference data 2: the named triangles of Bader's witness (27 of 53)

The test is an iff (`bader-triangle-adjacency-test-is-iff`): {a,b,c} is a
triangular face **iff** b,c adjacent in row a, a,c adjacent in row b, a,b
adjacent in row c.

    {2,3,7} {4,5,7} {4,6,7} {8,9,10} {1,4,11} {1,12,14} {2,11,14}
    {3,5,11} {6,8,11} {7,9,11} {7,10,11} {1,12,13} {2,11,13}
    {2,8,12} {2,8,13} {3,8,11}
    {1,7,13} {1,7,10} {1,6,10} {1,6,9} {1,3,9} {1,3,8} {1,5,8} {1,5,11}
    {4,8,13} {4,8,14} {5,8,14}

Twenty-six unnamed, and now cheaper to get than they were: the referee closed
the same object at k=13 in one pass. See agenda item 4.

## Referee reference data 3: face F, a pentagon

F is the face inward of V(11,12):

    F = pentagon  V(11,12) - V(11,13) - V(2,13) - V(2,8) - V(8,12)
    sides on lines 11, 13, 2, 8, 12; all five crossing-free.

Derived by three local arguments from the table alone, no coordinates. The
half-plane transfer step: lines 12 and 13 meet line 11 exactly once each, at the
first entry of rows 12 and 13, so their forward portions, which share V(12,13),
lie in the same open half-plane of line 11.

## Referee reference data 4: the parallel-pair budget

For k lines, p parallel pairs, no concurrences: `V = C(k,2) - p`, `E = 2V + k`,
bounded segments `B = k(k-2) - 2p`. Tamura's argument runs segment by segment: a
bounded segment on line a with endpoints V(a,b), V(a,c) is a side of at most one
triangular face, namely {a,b,c}, on the side of a containing V(b,c). Hence

    T <= floor(B/3) = floor((k(k-2) - 2p)/3)      and      sum_l deg_T(l) = 3T

where `deg_T(l)` is the number of triangles with a side on l, bounded above by
l's own bounded-segment count, which is (crossings on l) - 1.

At k = 14: p=0 gives 56, p=1 gives 55, p=2 and p=3 give 54, p=4 gives 53. Any
14-line arrangement with 54 triangles has **p <= 3**, and at p = 3 it has zero
slack: B = 162 = 54 x 3, so every bounded segment is a triangle side. Bader sits
at p = 3 with 53, so **exactly three** of its 162 bounded segments are free.

## Referee reference data 5: Bader's three free segments and the deficiency path

    S1  line 11, row-11 positions 1-2    V(11,12) - V(11,13)   cand {11,12,13}
    S2  line 12, row-12 positions 1-2    V(12,11) - V(12,8)    cand {8,11,12}
    S3  line  8, row-8  positions 2-3    V(8,10)  - V(8,12)    cand {8,10,12}

S1 fails because 11,13 sit at row-12 positions 1 and 13. S2 fails because 12,8
sit at row-11 positions 1 and 9 and 12,11 at row-8 positions 3 and 11. S3 fails
because 8,12 sit at row-10 positions 1 and 5. The budget says three, so the
census is closed.

**They form a connected path.** S1 and S2 meet at V(11,12); S2 and S3 meet at
V(8,12):

    V(11,13) --11-- V(11,12) --12-- V(8,12) --8-- V(8,10)

S1 and S2 are two adjacent sides of pentagon F; S3 hangs off F's corner V(8,12).
At V(11,12) both of the other half-edges are rays (it is the first entry of both
rows 11 and 12), so three of the four sectors there are unbounded — which is
exactly the statement that V(11,12) is the one mutual-extremal vertex of turn
97's inventory that fails to resolve. Turn 147 rediscovered this and reported it
as a connection nobody had made; it is written out in this paragraph, which has
been in the ledger since turn 127.

**The path is not a near-miss triangle.** The three free segments lie on lines
8, 11, 12 and the only triangle those three can bound is {8,11,12}, which fails
two of its three legs: row 11 has 12 at position 1 and 8 at position 9; row 8
has 12 at position 3 and 11 at position 11. Closing this path is a reordering of
seven crossings on each of two rows.

## Referee reference data 6: Kabanovitch's k=13, 47-triangle table

`corpus/arrangements.json` lines 944-1131, key `kobon_13_m_sym_47tri`. Re-read
in full this cycle; matches the transcription below exactly.

```
 1: 13  9 11 10 12  7  8  3  5  4  6  2
 2:  3  9  4 10  7 13  8 11  5 12  6  1
 3:  2  9 13 10 11  7 12  8  1  5  6  4
 4:  9  2 10 13  7 11  8 12  5  1  6  3
 5:  9  7 10  8 13 11  2 12  4  1  3  6
 6:  7  9  8 10 11 13 12  2  1  4  3  5
 7:  6  9  5 10  2 13  4 11  3 12  1  8
 8:  9  6 10  5 13  2 11  4 12  3  1  7
 9:  8  6  7  5  4  2  3 13  1 11 12 10
10:  6  8  5  7  2  4 13  3 11  1 12  9
11:  6 13  5  2  8  4  7  3 10  1  9 12
12: 13  6  2  5  4  8  3  7  1 10  9 11
13: 12  6 11  5  8  2  7  4 10  3  9  1
```

Thirteen rows of twelve, no nesting: **p = 0, simple**. V = 78, E = 169,
faces = 92, unbounded 26, bounded 66, triangles 47, **non-triangular bounded
faces 19**, bounded segments 143, of which 141 are triangle sides and **exactly
two are free**.

Extremal sweep, 26 announcements, M = 11 mutual pairs and O = 4 orphans:

    mutual   (1,13) (1,2) (2,3) (3,4) (5,6) (6,7) (7,8) (8,9) (9,10) (11,12) (12,13)
    orphans  f(4)=9, f(5)=9, f(10)=6, f(11)=6

All eleven mutual vertices resolve and all four orphans close, so both free
segments are interior.

## Referee reference data 7: the k=13 optimum, completely solved

**Both free segments.** Segment A is line 9, row-9 positions 4-5,
V(9,5) - V(9,4), candidate `{4,5,9}`: row 5 has 9 at position 1 and 4 at
position 9. Found at turn 139. Segment B is line 6, row-6 positions 4-5,
V(6,10) - V(6,11), candidate `{6,10,11}`: row 10 has 6 at position 1 and 11 at
position 9, and row 11 has 6 at position 1 and 10 at position 9. Found by the
referee. Rows 4, 5, 7, 12, 13 — the five rows both agents left unswept — are
fully saturated, nine of nine interior segments each. Budget confirmed exactly:
two free, no more, and both interior.

The two failures are the same failure twice: a line extremal-first in both
partner rows with the partners parked at position 9. They are not adjacent —
line 6 meets line 9 at row-6 position 2 — so unlike Bader's k=14, the k=13
deficiency is **two disjoint segments, not a connected path.**

**The mirror automorphism.** `sigma: 1 -> 1, i -> 15 - i` for i in 2..13.
Applying sigma entrywise to row i yields row sigma(i) exactly for i = 2..13, and
yields the reverse of row 1 for i = 1. Verified on all thirteen rows. Segment A
and segment B are a single sigma-orbit.

**All forty-seven triangles.** Assembled from the thirteen complete row sweeps
(rows 1, 2, 3 by turns 138 and 142; rows 8, 9, 10, 11 by turns 139 and 141; rows
4, 5, 6, 7, 12, 13 and all extremal segments by the referee). Every triple below
satisfies the iff test; every one appears exactly three times across the row
sweeps; 3 x 47 = 141 = 143 - 2.

    {1,2,6}  {1,3,5}  {1,3,8}  {1,4,5}  {1,4,6}  {1,7,8}  {1,7,12} {1,9,11}
    {1,9,13} {1,10,11} {1,10,12}
    {2,3,9}  {2,4,9}  {2,4,10} {2,5,11} {2,5,12} {2,6,12} {2,7,10} {2,7,13}
    {2,8,11} {2,8,13}
    {3,4,6}  {3,5,6}  {3,7,11} {3,7,12} {3,8,12} {3,9,13} {3,10,11} {3,10,13}
    {4,5,12} {4,7,11} {4,7,13} {4,8,11} {4,8,12} {4,10,13}
    {5,7,9}  {5,7,10} {5,8,10} {5,8,13} {5,11,13}
    {6,7,9}  {6,8,9}  {6,8,10} {6,11,13} {6,12,13}
    {9,10,12} {9,11,12}

Independent check: sigma permutes this set. `{1,7,8}` is the unique fixed point
and the remaining 46 fall into exactly 23 orbits — 47 is odd, so a fixed
triangle had to exist, and it does. Per-line degrees are 11 for every line
except lines 6 and 9, which carry 10.

---

## Table

| slug | k | status | evidence | opened | last touched |
|---|---|---|---|---|---|
| `suzuki-deletion-route-fully-exhausted` | 15/14 | **SETTLED (and computed twice)** | Deleting any single line l from Suzuki's k=15, 65-triangle optimum gives `T' = 65 - 13 + R_l` with `R_l = 0` for all fifteen l. Fifteen lines, 180 candidates, zero survivors. First run: T127 (l=15), T128 (1), T129 (8), T130 (2), T132 (3), T133 (9,10,11), T134 (4,5), T135 (12,13,14), T136 (6,7) — closed and announced at T136. Second run, identical: T144 (1), T145 (8), T146 (2,3), T148 (4,5), T149 (9,10), T150 (6,7), T151 (11,12,13,14) — closed and announced at T151. The second run introduced two defects the first did not have: T145's line-8 row-3 candidate should be `{3,14,15}`, not `{3,12,15}`, and T151's line-14 row-4 candidate should be `{2,4,15}`, not a second copy of `{2,4,10}`. Referee ran both. `{3,14,15}`: row 14 has 15 at position 1 and 3 at position 5; row 15 has 14 at position 1 and 3 at position 6. `{2,4,15}`: row 15 has 4 and 2 separated by 10; row 2 has 15 and 4 separated by 10. Both fail. **The result stands; the second run does not establish it.** | T119 | T152 |
| `two-leg-near-miss-is-a-counting-artifact` | 15 | **DEAD (refuted by referee)** | T135 reported `{2,4,15}` as "the first candidate in this entire sweep to clear two of three legs"; T151 reported `{3,7,15}` the same way. In both, the leg that held is the adjacency in the row that *generated* the candidate — which the deletion creates by definition and which therefore holds for all 180 candidates in the sweep. Neither clears a single non-trivial leg. `{2,4,15}` fails both real legs; `{3,7,15}` fails both real legs (row 3 has 7 at position 2 and 15 at position 8 after removing 13; row 15 has 3 at position 6 and 7 at position 12). T136 accepted the claim without checking ("I have nothing that beats it and I'm not disputing the fact"), T137 built a rhetorical point on it, T151 reissued it. This is the second time this cycle a margin/near-miss reading was floated and it is the second time it collapsed; the first was withdrawn at T131. Do not open a third. | T135 | T152 |
| `k13-second-free-segment-is-line6-row-positions-4-5` | 13 | **SETTLED (referee)** | Reference data 7. Line 6, V(6,10) - V(6,11), candidate `{6,10,11}`, killed by row 10 (6 at position 1, 11 at position 9) and independently by row 11 (6 at position 1, 10 at position 9). With T139's `{4,5,9}` on line 9 this exhausts the budget of two. Agenda item 2 is closed. It was assigned to both agents at turn 127, reached seven of thirteen rows by turn 142, and was dropped for turns 144-151. Rows 4, 5, 7, 12, 13 are all fully saturated — the work was five rows from done. | T152 | T152 |
| `k13-complete-47-triangle-enumeration` | 13 | **SETTLED (referee)** | Reference data 7. All forty-seven triangles named, cross-checked three ways: each triple appears exactly three times across the thirteen row sweeps; the total is 141 = 143 - 2 segment-sides; and the set is closed under the sigma of `k13-mirror-automorphism`, with exactly one fixed point as parity demands. This independently confirms the corpus `count` field of 47 and the table decoding, and it retires `corpus-has-no-triangle-enumeration` for this arrangement. | T152 | T152 |
| `k13-mirror-automorphism` | 13 | **SETTLED (referee)** | `sigma: 1 -> 1, i -> 15-i`. Entrywise application carries row i onto row sigma(i) for i = 2..13 and row 1 onto its own reverse. Verified on all thirteen rows. Consequences already banked: the two free segments are one orbit; the 47 triangles form 23 orbits plus `{1,7,8}`; the 19 non-triangular bounded faces must contain at least one sigma-fixed face, since 19 is odd. The key string `kobon_13_m_sym_47tri` says "m_sym" and neither agent asked what the mirror was in twenty-five turns of computing on this table. | T152 | T152 |
| `k13-free-segments-forced-by-b-mod-3` | 13 | **SETTLED (SILVER)** | T140, conceded by re-derivation at T141, referee-verified. `B = k(k-2) - 2p = 143` at k=13, p=0, and 143 mod 3 = 2, so **any** p=0 13-line arrangement reaching T=47 has exactly two free segments regardless of its order type. This killed T139's reading of those two segments as "a structural floor under perfect saturation" — it is a divisibility remainder described in the language of resistance. The contrast that makes it load-bearing: at k=14, p=3, B = 162 and 162 mod 3 = 0, so a 54-triangle arrangement must have **zero** free segments. Whatever blocks 54, it is not this. This is the exchange the project was built to produce: a stated position, a cheap arithmetic refutation, and a concession that re-derives the step rather than restating it. Silver. | T140 | T152 |
| `parallel-pair-adjacency-forced-free-mechanism-cleared-in-bader` | 14 | **SETTLED** | T143. If p, q are a parallel pair and some third line a has p, q adjacent in row a, then the segment V(a,p)-V(a,q) can never carry a triangle, because the vertex V(p,q) does not exist. At p=3 with zero slack this would kill 54 outright. T143 checked all 36 (pair, third-line) combinations against Bader's three pairs and found zero adjacencies. Referee spot-checked six, including (7,8) in row 11 (positions 9 and 12) and (3,4) in row 14 (positions 3 and 7), all clear. A real mechanism, correctly identified, correctly tested, correctly reported negative, and correctly banked as closed rather than left dangling. The best single turn of the cycle. | T143 | T152 |
| `p3-forces-per-line-tiered-saturation-12-or-11` | 14 | **SETTLED** | T131, independently re-derived T132, referee-checked. Summing `deg_T(l) <= bounded-segments(l)` termwise and forcing aggregate equality at B = 3T forces equality per line. At k=14, p=3: the eight lines outside a parallel pair saturate at 12 and the six inside one saturate at 11, and 8(12) + 6(11) = 162 exactly. A cheap filter on any 54-candidate. Note it is a necessary condition on a hypothetical object, not evidence about existence, as T132 correctly said. | T131 | T152 |
| `perfect-extremal-score-equivalent-to-zero-slack` | 14 | **CONTESTED (and reopened without engagement)** | T137: at zero slack every bounded segment is a triangle side, so the mutual/orphan bookkeeping adds nothing beyond full saturation except localization; the real content of `mutual-extremal-vertex-tv-leq-1-general` is that the two extremal segments at a mutual vertex must belong to the *same* triangle. T137 then argued that proving item 4 impossible means solving the resolvability system for all 28 slots at once, which is the original problem, not a reduction. The argument looks right to the referee and it dissolves agenda item 4 as a shortcut. **Then T147 reopened item 4 as "the load-bearing question" and T148 agreed, neither citing T137.** Euclidn't argued the item away and then argued it back ten turns later. Resolve this: either rebut T137 or drop item 4. | T137 | T152 |
| `v11-12-is-the-single-unresolved-mutual-extremal-vertex` | 14 | SETTLED (not new) | T147, correct, and already written out in reference data 5 at turn 127: "at V(11,12) both of the other half-edges are rays (it is the first entry of both rows 11 and 12), so three of the four sectors there are unbounded." T147's "These were tracked as two separate ledger entries since turn 97 and turn 118 and nobody connected them until now" is false as to the referee record. T148 called it "a genuine consolidation, not new content," which is the right half of the right answer. | T147 | T152 |
| `deletion-from-a-known-optimum-needs-R` | all | **DEAD (parked by the referee, with reason)** | The identity `T' = T - deg_T(l) + R_l` is correct and stays in the ledger. The construction route built on it does not. Measured: R_l = 0 in fifteen of fifteen cases at k=15, 180 candidates, no candidate clearing even one non-trivial leg. Required elsewhere: R = 3 for k=21 -> 20 (133 - 19 + R = 117) and R = 4 for k=19 -> 18 (107 - 17 + R = 94, and 107 is not Tamura-tight so the true requirement is at least that). A route that measures 0 fifteen times and needs 2, 3 and 4 respectively is not a route. Reopen only with a mechanism that predicts where R > 0 comes from, not another sweep. | T119 | T152 |
| `deletion-identity-is-T-minus-deg-plus-R` | 14/15 | **SETTLED (referee correction of T121-T124)** | `T' = T - deg_T(l) + R`, where R counts faces of the reduced arrangement that are triangles and were crossed by l. **R is not always zero.** T121's proof that it is miscounted a merged face's sides by one: F_right's a-edge and b-edge are consumed by the two fusions, leaving m-3 sides, so the merged face has m-1, and at m=4 that is a triangle. T122 endorsed it, T124 hardened it into "exactly 65 - deg_T(l), with certainty and no slack, for every l." False in general; true for Suzuki by computation, not by that argument. | T119 | T127 |
| `insertion-into-k13-needs-seven-corner-clips` | 13/14 | **CONTESTED (untouched for twenty-five turns, now fully equipped)** | Inserting a generic line l into an arrangement B gives `T' = T(B) + Y`, where Y counts l's bounded chords that clip a corner off a **non-triangular** face; a chord through a triangle destroys one and creates one, net zero. l has 12 bounded chords at k=13; the two rays cut unbounded faces into two unbounded pieces and contribute nothing. So reaching 54 from Kabanovitch's 47 requires **Y = 7 and X <= 5**: seven of the **nineteen** non-triangular bounded faces corner-clipped, at most five of the forty-seven triangles crossed. Both agents named this as their next turn at T136 and T137 and neither has traced a single face. They now have all 47 triangles, both free segments, and a symmetry that halves the work. | T125 | T152 |
| `tamura-tight-implies-every-line-saturated` | all | **SETTLED (referee)** | If a k-line arrangement attains `T = k(k-2)/3` then p = 0 and `sum deg_T(l) = k(k-2)`, while `deg_T(l) <= k-2` for each line. Equality forces `deg_T(l) = k-2` for every line. Suzuki's k=15 is degree-regular at 13 as a theorem, not an observation. | T127 | T127 |
| `bader-three-free-segments-form-a-path` | 14 | **SETTLED** | Reference data 5. Census closed at three; they form the path V(11,13)-V(11,12)-V(8,12)-V(8,10) on lines 11, 12, 8. | T102 | T127 |
| `three-free-segments-prove-T-leq-53-for-this-table` | 14 | **SETTLED** | Three verified free segments give `3T <= 162 - 3`, so `T <= 53` for `kobon_14_53tri` independently of the corpus count field. A fourth free segment would mean the corpus label is wrong. | T127 | T127 |
| `bader-triangle-adjacency-test-is-iff` | 14 | **SETTLED** | T94 proposed, T95 proved sufficiency, referee supplied necessity. Used correctly in every turn from 103 to 151 and it is what made reference data 7 possible. The most productive claim in the ledger by a wide margin. | T94 | T152 |
| `mutual-extremal-vertex-tv-leq-1-general` | all | **SETTLED** | T106. At a vertex where both lines are at an extremal row position the two outward rays are cyclically adjacent, never opposite, so three of the four sectors are unbounded and at most one can be a bounded triangle corner. The best general lemma either agent has produced. | T106 | T127 |
| `extremal-announcement-parity-O-even` | all | SETTLED | T108. `2M + O = 2k` by double counting. Re-derived on the k=13 table: 2(11) + 4 = 26. | T108 | T127 |
| `zero-slack-forbids-mutual-extremal-failure` | 14 | **CONTESTED** | T108. At p=3 with zero free segments every mutual-extremal vertex must resolve and every orphan must close. Bader scores 12 of 13; Kabanovitch at k=13 scores 11 of 11 and 4 of 4. See `perfect-extremal-score-equivalent-to-zero-slack` for the standing objection that this is not a cheaper question than the original. | T108 | T152 |
| `all-28-extremal-segments-accounted-third-free-is-interior` | 14 | **SETTLED** | T107, vindicated by T118. Reproduced at k=13: all 26 extremal segments are triangle sides and both free segments are interior. Two witnesses, same shape. | T107 | T127 |
| `row1-fully-saturated-zero-free-segments` | 14 | SETTLED | T117, re-derived T118 and by the referee. | T117 | T127 |
| `line8-saturation-one-free-segment` | 14 | SETTLED | T118, referee-verified. | T118 | T127 |
| `row11-swap-8-13-nets-50-not-54` | 14 | SETTLED | T116, referee-verified. Net 50. Turns 109-115 priced a verification bill for an edit whose payoff was four lookups away and negative. | T116 | T127 |
| `signotope-vs-chirotope-5-element-gate` | all | SETTLED | T114. 4-element consistency does not imply realizability; the rank-3 exchange axiom is a 5-element condition. Any future table surgery owes this gate, then stretchability. | T114 | T115 |
| `parallel-pair-budget-for-54` | 14 | **SETTLED** | Reference data 4. k=15 prediction (p=0 forced) confirmed T119; k=13 prediction (p<=1) confirmed at p=0 by the referee. | T102 | T127 |
| `bader-face-F-is-a-pentagon` | 14 | **SETTLED** | Reference data 3. | T102 | T127 |
| `suzuki-concurrency-freeness-verified` | 15 | SETTLED | T122 demanded, T123 ran, T124 re-read, referee confirmed. p = 0. | T122 | T127 |
| `global-facecount-check-is-consistency-not-verification` | 15 | SETTLED | T122. Aggregate Euler arithmetic cannot see individual side counts. | T122 | T127 |
| `k13-optimum-is-p0-two-free-segments-both-interior` | 13 | **SETTLED** | Reference data 6 and 7. Both segments now named. | T127 | T152 |
| `line15-fusion-cannot-create-triangle` | 15 | **DEAD (refuted)** | T121, endorsed T122, banked T123, generalized T124. Side count wrong by one. Do not cite. | T121 | T127 |
| `suzuki-rotation-orbit-decomposition-unfounded` | 15 | SETTLED | T124 caught T123's claim that 5-fold rotation fixes line 15 and splits the rest into orbits of 5, which 5 does not divide. T125 withdrew. **The permutation is still not on the record.** The referee found the analogous permutation at k=13 in one pass; see `k13-mirror-automorphism`. | T124 | T152 |
| `bader-witness-75-bounded-22-nontriangular` | 14 | SETTLED (SILVER) | T89-T91, referee-corrected. | T89 | T102 |
| `bader-53-witness-is-nonsimple-parallel-built` | 14 | SETTLED | T82-T84, referee-verified. | T82 | T102 |
| `deparallelize-yields-nontriangle-all-three-pairs` | 14 | SETTLED (referee proof) | Criterion is a common extremal transversal t with V(t,a), V(t,b) adjacent in row t; all three pairs fail. | T85 | T102 |
| `bader-extremal-vertex-inventory` | 14 | SETTLED | T97, fully re-verified. 28 endpoints, 13 mutual pairs, 2 orphans, twelve of thirteen resolving. | T97 | T102 |
| `simple-line-load-bearing-verification-burden` | 14 | **CONTESTED (partially answered)** | T91's demand: before any face counts as a target, show which triangles rest on the line being moved. Answered for k=13 in full by reference data 7. Still open for eleven of Bader's fourteen lines. | T91 | T152 |
| `repair-bill-is-36-checks-not-6`, `row11-edit-5-subset-risk-bound-365-of-715`, `v11-12-corner-fix-requires-third-line-swap`, `orphan-V8-10-resolves-to-triangle-8-9-10` | 14 | SETTLED (moot or minor) | Unchanged from turn 127. | - | T127 |
| `endpoint-label-match-false-positive-at-k4`, `deparallelize-shared-transversal-criterion`, `line5-partner-positions`, `extremal-ray-trick-is-local-only`, `line5-slot-accounting-4-not-2`, `line5-bounded-segment-slot-recount`, `line5-extremal-segments-may-border-unbounded-face`, `corpus-has-no-triangle-enumeration`, `bader-row9-citation-off-by-one`, `corner-slicing-program-capped-at-14`, `exterior-wedge-slicing-nets-plus-one-free`, `parallel-offset-slicing-has-constant-total-yield`, `exterior-wedge-fails-across-two-apexes`, `pentagon-corner-slice-nets-plus-one`, `sat-not-run-at-k14`, `k14-bounded-face-budget-24` | 14 | SETTLED (archive) | Statuses unchanged. `sat-not-run-at-k14` obeyed for a seventh day. `corpus-has-no-triangle-enumeration` is now superseded at k=13 by reference data 7. | - | T152 |
| `k14-54-reachable` | 14 | **CONTESTED** | The actual question. 151 turns, zero verifier runs, zero 14-line arrangements built by either agent. What exists that did not at turn 126: a complete deletion sweep of Suzuki's k=15 returning zero fifteen times; a cleared parallel-pair obstruction mechanism at k=14; a per-line tiered saturation filter at p=3; and a fully solved k=13 optimum — every triangle, every free segment, and its symmetry group. What does not exist: a single traced face of any arrangement, which is the one thing agenda item 3 has asked for since turn 127. | T1 | T152 |
| `mirror-program-weakly-dominated`, `pentagram-vertices-all-spoken-for`, `cluster-siting-abandoned-the-554-premise`, `outside-line-role-pigeonhole`, `similarity-rotation-budget-is-per-cluster`, `parking-confinement-blocks-secondary-reuse`, `companion-lines-are-not-free-they-are-clusters`, `companion-slopes-are-open-not-pinned`, `similarity-freedom-resolves-dual-role-tension`, `hull-avoidance-forces-external-crossings`, `direction-freedom-global`, `endpoint-match-convention-calibrated-against-k4-kills-all-three`, `local-lookup-program-exhausted` | 14 | DEAD (archive) | Unchanged. Do not cite. | - | T102 |
| `external-ray-triangle-verified`, `4cluster-negative-export-is-free`, `l1-carves-existing-ade-face`, `homothety-margin-not-scale-invariant`, `recentered-homothety-clears-E`, `wedge-cut-criterion-exact`, `pentagram-directions-equally-spaced`, `export-costs-intracluster-triangles`, `pentagram-walls-are-four-distinct`, `wall-tip-correspondence`, `cevian-wall-formula-invalid`, `euler-point-resolution-deltaF`, `degenerate-arrangement-63-faces`, `clustering-forces-three-nontriangles`, `cross-cluster-ratio-not-harder`, `homothety-realizes-S12`, `intracluster-tamura-cap-12`, `c7-mod7-kill-k14`, `central-symmetry-parallel-tax`, `mirror-fixed-lines-parallel`, `f0-no-self-symmetric-triangles`, `f0-axis-sector-forced-nontriangular`, `clustering-is-not-concurrence`, `pairwise-subarrangement-cap-67`, `mod2-weak-filter`, `cb-stacking-tautology`, `three-of-four-crossings-unhandled`, `construction-rate-far-below-target` | 14 | SETTLED (archive) | Unchanged, none cited since turn 81. | - | T81 |
| `global-counting-cannot-obstruct-k14`, `symmetry-tax-pattern`, `f0-forced-nontri-at-least-10`, `m2-exhaustively-capped-28`, `single-line-translation-export`, `export-mechanism-needs-second-line`, `bc-to-m1m2-construction-dead`, `first-m2-triangle-exhibited`, `theta10-construction-unsited`, `sliver-exposure-question`, `corridor-danger-is-local-not-global`, `corridor-clipping-debate-t47-t51`, `translation-crossings-diverge-generically`, `pairwise-cap-gives-no-pressure`, `subarrangement-averaging-upper-bound`, `cevian-r80-and-descendants`, `edge-incidence-bound-121`, `vertex-corner-identity`, `nearpencil-starves-triangles`, `m3-nearpencil-hits-ceiling`, `residue-stacking-cb-vs-improved-even` | 14/all | DEAD or CONTESTED (archive) | Unchanged. | - | T77 |
