# Ledger

Claim registry, rewritten daily by the referee. `SETTLED` requires a complete
argument or a verifier run. Two agents agreeing is not evidence.

Rewritten by REFEREE after turn 154. Turns 152-154 audited.

Two turns, and they are the first two turns in this project's history to
attempt a boundary walk. That is worth saying plainly before the criticism:
turn 153 opened the walk, found something real that contradicted the referee's
own agenda, and refused to guess past the first obstacle. Turn 154 reproduced
the mirror half independently and landed on sigma-image vertices, and then
retired agenda item 4 with a re-derivation rather than a restatement. Both are
correct behaviour.

The failure is that both turns stopped at the same place, for the same stated
reason, and the reason is wrong. Turn 153: "Choosing between them needs a
turning-direction rule, not adjacent-row lookup alone." Turn 154: "it's a global
reconstruction from all thirteen rows at once, not a lookup in the row you're
standing on. Neither agent has built it. The face-tracing method has a sourced
gap." It is two lookups. See `face-walk-side-test-is-two-lookups`. The referee
resolved the exact vertex each agent stopped at, finished both walks, and then
traced a third face for good measure. Two agents declared a method broken on
the turn before it would have worked.

The referee's findings this cycle:

1. **The agenda was wrong and turn 153 caught it.** "A free segment is a side
   of no triangle, so both faces adjacent to it are non-triangular. That is four
   of the nineteen handed to you" — false. One of the two is unbounded, so each
   free segment contributes exactly **one** of the nineteen. It is two, not
   four. Turn 153 found this. Turn 153 also asserted the conclusion with "the
   natural reading is," which is not an argument; the argument is in reference
   data 8 and it takes three lines.
2. **Both walks close.** Segment A's bounded face is the hexagon
   V(9,4) - V(4,2) - V(2,10) - V(10,7) - V(7,5) - V(5,9). Segment B's is its
   sigma-image hexagon V(6,11) - V(11,13) - V(13,5) - V(5,8) - V(8,10) -
   V(10,6). Every one of the twelve edges is adjacent in its row; both closures
   were forced by the side rule, not assumed. Reference data 9.
3. **The mirror axis gives the face census for free.** Sigma has exactly six
   fixed vertices and exactly one fixed edge, both counts proved from the rows.
   The axis therefore meets the arrangement in seven points and passes through
   six bounded faces, one of which is the triangle `{1,7,8}`. So **exactly five
   of the nineteen are sigma-fixed and the other fourteen form seven orbits.**
   Reference data 10. This is a falsifier on every face list produced from here.
4. **A third face, sigma-fixed, traced by the referee.** The pentagon
   V(1,7) - V(7,12) - V(12,3) - V(3,8) - V(8,1), on lines 1, 7, 12, 3, 8, whose
   line set is sigma-closed. Sixteen of the nineteen remain. Reference data 10.
5. **Item 4 is off the board and Euclidn't took it off.** Turn 154 re-derived
   turn 137's argument instead of citing it, and stated the self-reversal at
   turn 147 in its own words. That is the standing concession rule applied to
   oneself, which nobody has done before in this project. It is not silver,
   because no opponent forced it and the referee had to ask, but it is the right
   shape.

---

## OWNER CORRECTION, entered after turn 170, standing until re-argued

**Turns 163 to 168 built a bound that is not sound, and it must not be carried
forward.** The referee has not audited that stretch yet. This entry pre-empts it.

The claims `no-two-nontriangular-faces-share-an-edge`,
`generic-insertion-into-b-caps-53`,
`y-leq-6-independent-of-concurrence-count`,
`insertion-y-capped-at-6-independent-of-concurrence-count` and
`generic-insertion-into-any-simple-13-line-caps-53` are **REFUTED**. Do not cite
any of them as settled.

**The defect.** Turn 168's own re-derivation says every bounded edge borders
"exactly one triangle-or-unbounded face and exactly one of the nineteen," and
then treats that first category as contributing zero. That is true for a
triangle, because a chord through a triangle destroys one and creates one. It is
false for an unbounded face. A chord that clips the corner of an unbounded wedge
produces a **bounded** triangle, worth +1, and the T/N labelling never counts it.
The partition is not exhaustive, so the no-two-adjacent-N argument does not bound
Y.

**Decisive check, no geometry needed.** N(4) = 2 and N(5) = 5, both in KNOWN.md.
Delete a line from any 5-line optimum: the remaining simple 4-line arrangement has
at most 2 triangles, so re-inserting must create at least 3. It has exactly 3
bounded chords against an alternation cap of ceil(3/2) = 2. Cap violated. Further,
a simple 4-line arrangement has C(3,2) = 3 bounded faces, two of them its
triangles, leaving exactly **one** bounded non-triangle, so at least two of the
three new triangles come from clipping unbounded faces. The same failure recurs at
k = 7, where N(7) - N(6) = 4 against a cap of 3.

**Where it lands.** Reference data 8, which is correct, says each of the two free
segments of B has an unbounded three-sided wedge on one side and a hexagon on the
other. That wedge is a clippable unbounded face, so a line can gain twice in a row
there: clip the hexagon on the way in, clip the wedge on the way out. Two free
segments give two exemptions, and turn 167's own formula with n = 12 and three
segments then yields Y <= (12 + 3)/2 = 7.5, so **7**. That is exactly the value
reaching 54 requires. The cap does not merely have a gap, it collapses onto the
target.

**What survives.** The face census (reference data 9 and 10, and the faces named
in turns 156 to 162) is independent of this and stands. Turn 165 and 166's result
that extreme concurrences contribute zero credit is correct and unaffected. What
does not survive is the headline, and turn 168's generalization propagated the
error rather than exposing it.

**How it got through.** Both agents and the gate verified the algebra, which was
fine, and nobody verified that the case analysis was exhaustive, which it was not.
Neither agent ran a single line of the repository's own enumerator. Across 170
turns `verifier_runs` has been empty 170 times.

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
97's inventory that fails to resolve.

**The path is not a near-miss triangle.** The three free segments lie on lines
8, 11, 12 and the only triangle those three can bound is {8,11,12}, which fails
two of its three legs: row 11 has 12 at position 1 and 8 at position 9; row 8
has 12 at position 3 and 11 at position 11. Closing this path is a reordering of
seven crossings on each of two rows.

## Referee reference data 6: Kabanovitch's k=13, 47-triangle table

`corpus/arrangements.json` lines 944-1131, key `kobon_13_m_sym_47tri`.

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
referee. Rows 4, 5, 7, 12, 13 are fully saturated, nine of nine interior
segments each.

**The mirror automorphism.** `sigma: 1 -> 1, i -> 15 - i` for i in 2..13.
Applying sigma entrywise to row i yields row sigma(i) exactly for i = 2..13, and
yields the reverse of row 1 for i = 1. Verified on all thirteen rows. Segment A
and segment B are a single sigma-orbit.

**All forty-seven triangles.**

    {1,2,6}  {1,3,5}  {1,3,8}  {1,4,5}  {1,4,6}  {1,7,8}  {1,7,12} {1,9,11}
    {1,9,13} {1,10,11} {1,10,12}
    {2,3,9}  {2,4,9}  {2,4,10} {2,5,11} {2,5,12} {2,6,12} {2,7,10} {2,7,13}
    {2,8,11} {2,8,13}
    {3,4,6}  {3,5,6}  {3,7,11} {3,7,12} {3,8,12} {3,9,13} {3,10,11} {3,10,13}
    {4,5,12} {4,7,11} {4,7,13} {4,8,11} {4,8,12} {4,10,13}
    {5,7,9}  {5,7,10} {5,8,10} {5,8,13} {5,11,13}
    {6,7,9}  {6,8,9}  {6,8,10} {6,11,13} {6,12,13}
    {9,10,12} {9,11,12}

Sigma permutes this set. `{1,7,8}` is the unique fixed point and the remaining
46 fall into exactly 23 orbits. Per-line degrees are 11 for every line except
lines 6 and 9, which carry 10.

## Referee reference data 8: the side rule, and why a free segment has an unbounded face

**The side rule (two lookups).** Fix a line x. For any other line y, row y tells
you which points of y are before x and which are after; what a walk needs is
which of those two halves is which *physical* side of x, consistently across
different y. That comparison is one vertex lookup per pair. For lines y and z,
the vertex V(y,z) lies on both, so

    "after x in row y" and "after x in row z" name the same side of x
    iff  V(y,z) is after x in row y  and  V(y,z) is after x in row z
         (or before in both).

Chaining this from one reference line orients all k-1 lines with respect to x in
k-2 lookups, and a single turn in a face walk needs exactly one such comparison,
i.e. two row lookups. Nothing global, nothing unbuilt, no appeal to the circle
convention's entry order.

**Concretely, at the two vertices where turns 153 and 154 stopped.** Turn 153
stopped at V(2,4) with candidates V(2,9) at row-2 position 2 and V(2,10) at
row-2 position 4. The face contains V(4,9). Bridge on line 4: row 4 has 2 at
position 2, 9 at position 1 and 10 at position 3, so V(4,9) and V(4,10) are on
opposite sides of line 2. Row 2 has 4 at position 3 and 10 at position 4, so the
positions above 2 are V(2,10)'s side and the positions below are V(2,9)'s. The
face is on the V(2,10) side. **Next vertex V(2,10).** By sigma the answer at
turn 154's V(11,13) is **V(13,5)**, row-13 position 4, not V(13,6).

**Why one face on a free segment is unbounded.** Let the free segment be
V(9,4) - V(9,5), adjacent in row 9, so it is a full side of the triangle that
lines 4, 5, 9 bound in the plane, whose other vertices are V(4,5) on both lines
4 and 5. Row 4 has 9 at position 1 and 5 at position 9, so along line 4 the
direction from V(4,9) toward V(4,5) is the increasing one and the decreasing one
is a ray. Row 5 has 9 at position 1 and 4 at position 9, identically. So **both
rays point away from that triangle, hence into the same open half-plane of line
9.** The region bounded by the segment and the two rays admits no crossing line:
any line entering it must cross the segment (which is an edge, so crossing-free)
or a ray (rays carry no crossings). It is therefore a single unbounded face with
three sides. The other side of the free segment lies inside a bounded triangle
and is a bounded non-triangular face. **One of the nineteen per free segment,
not two.**

## Referee reference data 9: the two free-segment faces of k=13, both hexagons

Walked with reference data 8, each turn forced, each edge checked adjacent in
its row.

    Segment A face:  V(9,4) - V(4,2) - V(2,10) - V(10,7) - V(7,5) - V(5,9)
    sides on lines   9, 4, 2, 10, 7, 5

    edge on 9 : row 9  positions 5,4   (values 4,5)     = segment A
    edge on 4 : row 4  positions 1,2   (values 9,2)
    edge on 2 : row 2  positions 3,4   (values 4,10)
    edge on 10: row 10 positions 5,4   (values 2,7)
    edge on 7 : row 7  positions 4,3   (values 10,5)
    edge on 5 : row 5  positions 2,1   (values 7,9)

    Segment B face = sigma(A face):
                     V(6,11) - V(11,13) - V(13,5) - V(5,8) - V(8,10) - V(10,6)
    sides on lines   6, 11, 13, 5, 8, 10

    edge on 6 : row 6  positions 5,4   (values 11,10)   = segment B
    edge on 11: row 11 positions 1,2   (values 6,13)
    edge on 13: row 13 positions 3,4   (values 11,5)
    edge on 5 : row 5  positions 5,4   (values 13,8)
    edge on 8 : row 8  positions 4,3   (values 5,10)
    edge on 10: row 10 positions 2,1   (values 8,6)

Both are hexagons. They are one sigma-orbit. Seventeen of the nineteen remain.

## Referee reference data 10: the mirror axis and the fixed-face census

**Fixed vertices.** V(a,b) is sigma-fixed iff {sigma(a),sigma(b)} = {a,b}. Line
1 is the only fixed line, so the only possibility is b = 15 - a. Exactly six:

    V(2,13)  V(3,12)  V(4,11)  V(5,10)  V(6,9)  V(7,8)

**Fixed edges.** An edge on line i with i != 1 maps to an edge on line 15 - i,
so it is not fixed. On line 1, sigma reverses the row, sending the edge at
positions (j, j+1) to the edge at positions (12-j, 13-j); fixed iff j = 6. Row 1
is `13 9 11 10 12 7 8 3 5 4 6 2`, so positions 6 and 7 carry 7 and 8. Exactly
one fixed edge: **V(1,7) - V(1,8)**.

**The axis.** Realized as a plane reflection — which is what the corpus key
`m_sym` asserts and what the row-1 reversal forces, line 1 being perpendicular
to the axis — the fixed point set is a line meeting the arrangement in those six
vertices plus the midpoint of the one fixed edge. **Seven points, eight arcs,
two unbounded, six bounded faces met.** One of the six is the triangle
`{1,7,8}`, the unique sigma-fixed triangle: row 7 has 8 last and row 8 has 7
last, so beyond V(7,8) both continuations are rays and the arc past V(7,8) is
unbounded. Hence

    exactly 5 of the 19 non-triangular bounded faces are sigma-fixed,
    and the other 14 form exactly 7 sigma-orbits.

Combinatorial cross-check with no geometry: sigma is an involution on 19 faces,
so the fixed count is odd; 5 is odd; and 47 triangles with 1 fixed is odd, and
1 + 5 = 6 is even as it must be for 66 bounded faces.

**Axis order so far.**

    infinity -- V(7,8) -- [triangle {1,7,8}] -- midpoint of V(1,7)-V(1,8)
             -- [pentagon P] -- V(3,12) -- [F2] -- ... -- infinity

**The pentagon P, traced by the referee.** It is the face on the far side of the
one fixed edge from `{1,7,8}`:

    P = V(1,7) - V(7,12) - V(12,3) - V(3,8) - V(8,1)
    sides on lines 1, 7, 12, 3, 8

    edge on 1 : row 1  positions 6,7    (values 7,8)
    edge on 7 : row 7  positions 11,10  (values 1,12)
    edge on 12: row 12 positions 8,7    (values 7,3)
    edge on 3 : row 3  positions 7,8    (values 12,8)
    edge on 8 : row 8  positions 10,11  (values 3,1)

Its line set {1,3,7,8,12} is sigma-closed and its two edges at V(3,12) are
sigma-images of each other, as a fixed face's must be. The turn at V(7,12) was
forced by the side rule, not by the convexity shortcut: the face contains
V(1,8); row 1 has 7 at 6, 8 at 7 and 12 at 5, so V(1,8) and V(1,12) are on
opposite sides of line 7; row 12 has 7 at 8 and 1 at 9, so positions above 8 are
V(1,12)'s side; the face takes positions below 8, giving V(12,3).

**The next fixed face, seeded.** The axis leaves P at V(3,12) into the
vertically opposite sector, whose two edges are V(3,12) - V(3,7) (row 3 position
6) and V(12,3) - V(12,8) (row 12 position 6). Those two are sigma-images. Start
F2 there.

---

## Table

| slug | k | status | evidence | opened | last touched |
|---|---|---|---|---|---|
| `insertion-y-capped-at-6-independent-of-concurrence-count` | 13/14 | **REFUTED (owner, after T170)** | T167's closed form `Y <= (n+m+1)/2 = 6.5`. The algebra is right and the premise is not: the T/N partition of chords omits chords lying in unbounded faces, which can be corner-clipped to create bounded triangles. See the owner correction at the top of this file. Counterexample to the mechanism, from classical values only: N(5)-N(4) = 3 from 3 chords against a cap of 2, and N(7)-N(6) = 4 from 5 chords against a cap of 3. | T167 | T170 |
| `generic-insertion-into-any-simple-13-line-caps-53` | 13/14 | **REFUTED (owner, after T170)** | T168 generalized T163's cap to every simple 13-line base. It inherits the same omission. Note what it would have implied had it held, which neither agent noticed: every 14-line arrangement is a single-line insertion into a 13-line one, and N(13)=47 is closed, so the cap would have given N(14) <= 53 outright. That is the reason to be suspicious of it, not to bank it. | T168 | T170 |
| `no-two-nontriangular-faces-share-an-edge` | 13 | **SETTLED as stated, MISUSED downstream** | The literal claim is true and is Tamura's per-segment argument: each bounded edge borders at most one triangle, and B - 3T = 2 free segments each carry an unbounded wedge on one side. What does not follow is that consecutive chords cannot both gain, because the wedge is clippable. Keep the fact, drop the corollary. | T163 | T170 |
| `unbounded-wedge-clip-creates-bounded-triangle` | all | **OPEN, and this is the live question** | A chord entering an unbounded three-sided wedge through its bounded edge and leaving through one of its two rays cuts off a bounded triangle. Free segments are exactly where such a wedge sits adjacent to one of the nineteen. How many of l's twelve chords can occupy clippable unbounded faces at k=13, and can two consecutive gains actually be realized by a straight line at a free segment? Settle this and the insertion program is either dead or alive on evidence rather than on an incomplete case split. | T170 | T170 |
| `face-walk-side-test-is-two-lookups` | all | **SETTLED (referee), and it kills a claimed obstacle** | Reference data 8. T153: "Choosing between them needs a turning-direction rule, not adjacent-row lookup alone... that trick doesn't transfer directly." T154 escalated it to a sourced impossibility: the phase-2 design doc fixes entry order but not exit order, therefore "a global reconstruction from all thirteen rows at once, not a lookup in the row you're standing on. Neither agent has built it. The face-tracing method has a sourced gap." The quotation from `docs/superpowers/specs/2026-08-20-kobon-duel-phase2-design.md` is accurate and the inference from it is wrong. Two lines y, z meet at V(y,z); that single vertex ties row y's before/after split at x to row z's. One comparison, two row lookups, resolves any single turn; k-2 comparisons orient every line against x. The referee applied it to the exact vertices both agents stopped at and finished both walks in the same pass. **No gap.** | T153 | T155 |
| `k13-free-segment-outer-face-is-unbounded` | 13 | **SETTLED (T153, argument supplied by referee)** | Reference data 8. If a free segment V(a,b) - V(a,c) has b and c each meeting a at its own row-position 1, both rays point away from the triangle that a, b, c bound, so they lie in the same half-plane of a and close a three-sided unbounded face with the segment. Both k=13 free segments have exactly this shape. **Consequence: each free segment contributes one of the nineteen, not two.** The referee's own agenda at turn 152 said four; the correct number is two, and T153 caught it. T153 reached the right answer by "the natural reading is a single unbounded wedge," which is a guess that happened to be true; the ray-alignment step is the content and it was not supplied until now. | T153 | T155 |
| `k13-free-segment-faces-are-a-hexagon-sigma-pair` | 13 | **SETTLED (referee)** | Reference data 9. Segment A's bounded face is the hexagon V(9,4) - V(4,2) - V(2,10) - V(10,7) - V(7,5) - V(5,9); segment B's is its sigma-image. All twelve edges verified adjacent in their rows, both closures forced rather than assumed. Two of nineteen named. Note what the shape says: the free segment does not sit on a large ragged face, it sits on a hexagon, which is the second-hardest size to corner-clip after the ones above it. That is the first real datum for agenda item 2. | T155 | T155 |
| `k13-mirror-axis-fixed-cell-census` | 13 | **SETTLED (referee)** | Reference data 10. Six fixed vertices V(i,15-i) for i = 2..7 and exactly one fixed edge V(1,7) - V(1,8), both proved from the rows with no geometry. Under the reflection realization the axis meets the arrangement in seven points and passes through six bounded faces, one being triangle `{1,7,8}`, so **exactly five of the nineteen are sigma-fixed and fourteen form seven orbits**. Parity cross-check with no geometry: an involution on 19 has an odd fixed count. This is a falsifier on every face list produced from here, and it converts the agenda from "trace nineteen things" into "trace five along a known line and six orbit representatives." | T155 | T155 |
| `k13-fixed-pentagon-on-line-1` | 13 | **SETTLED (referee)** | Reference data 10. P = V(1,7) - V(7,12) - V(12,3) - V(3,8) - V(8,1), sides on lines 1, 7, 12, 3, 8, line set sigma-closed, all five edges verified adjacent. It is the first of the five fixed faces and it borders triangle `{1,7,8}` across the unique fixed edge. Three of nineteen named. | T155 | T155 |
| `perfect-extremal-score-equivalent-to-zero-slack` | 14 | **SETTLED (self-reversal resolved at T154)** | T137: at zero slack every bounded segment is a triangle side, so the mutual/orphan bookkeeping adds nothing beyond full saturation except localization, and proving a perfect extremal score impossible means solving the resolvability system for all 28 slots at once — the original problem, not a reduction. T147 reopened it as "the load-bearing question" without citing T137 and T148 agreed. T154 re-derived T137 rather than restating it — "zero-slack full saturation already implies every mutual vertex resolves and every orphan closes, so the bookkeeping can't fail without the arrangement failing to exist" — and withdrew T147. Correct, and correctly done. **Not silver:** no opponent forced it, the referee asked for it, and the disagreement was one agent with itself. | T137 | T155 |
| `zero-slack-forbids-mutual-extremal-failure` | 14 | **DEAD (true but not a shortcut; off the board T154)** | T108's statement is true — at p=3 with zero free segments every mutual-extremal vertex must resolve and every orphan must close — and is now known to carry no independent content beyond full saturation, per the entry above. Bader scores 12 of 13, Kabanovitch 11 of 11 and 4 of 4. Do not reopen as a route to impossibility. It stays usable as a filter on a candidate table, nothing more. | T108 | T155 |
| `suzuki-deletion-route-fully-exhausted` | 15/14 | **SETTLED (and computed twice)** | Deleting any single line l from Suzuki's k=15, 65-triangle optimum gives `T' = 65 - 13 + R_l` with `R_l = 0` for all fifteen l. First run T127-T136; second, identical run T144-T151. The second run introduced two defects the first did not have: T145's line-8 row-3 candidate should be `{3,14,15}`, not `{3,12,15}`, and T151's line-14 row-4 candidate should be `{2,4,15}`, not a second copy of `{2,4,10}`. Referee ran both missing checks; both fail. **The result stands; the second run does not establish it.** | T119 | T152 |
| `two-leg-near-miss-is-a-counting-artifact` | 15 | **DEAD (refuted by referee)** | T135's `{2,4,15}` and T151's `{3,7,15}` were both reported as clearing two of three legs. The leg that held in each is the adjacency in the row that *generated* the candidate, which the deletion creates by definition and which holds for all 180 candidates. Neither clears a non-trivial leg. Do not open a third. | T135 | T152 |
| `k13-second-free-segment-is-line6-row-positions-4-5` | 13 | **SETTLED (referee)** | Reference data 7. Line 6, V(6,10) - V(6,11), candidate `{6,10,11}`, killed by row 10 and independently by row 11. With T139's `{4,5,9}` this exhausts the budget of two. | T152 | T152 |
| `k13-complete-47-triangle-enumeration` | 13 | **SETTLED (referee)** | Reference data 7. Cross-checked three ways: each triple appears exactly three times across the thirteen row sweeps; the total is 141 = 143 - 2; the set is sigma-closed with exactly one fixed point as parity demands. | T152 | T152 |
| `k13-mirror-automorphism` | 13 | **SETTLED (referee)** | `sigma: 1 -> 1, i -> 15-i`, verified on all thirteen rows. It has now paid three times: the free segments are one orbit, the triangles fall into 23 orbits plus `{1,7,8}`, and reference data 10 turns it into a face census. | T152 | T155 |
| `k13-free-segments-forced-by-b-mod-3` | 13 | **SETTLED (SILVER)** | T140, conceded by re-derivation at T141, referee-verified. `B = 143` at k=13, p=0, and 143 mod 3 = 2, so any p=0 13-line arrangement reaching T=47 has exactly two free segments regardless of order type. Kills T139's reading of those segments as "a structural floor under perfect saturation." The contrast that makes it load-bearing: at k=14, p=3, B = 162 and 162 mod 3 = 0, so a 54-triangle arrangement must have zero free segments. Still the only silver in the ledger. | T140 | T152 |
| `parallel-pair-adjacency-forced-free-mechanism-cleared-in-bader` | 14 | **SETTLED** | T143. If p, q are a parallel pair and some third line a has p, q adjacent in row a, the segment V(a,p)-V(a,q) can never carry a triangle, because V(p,q) does not exist. At p=3 with zero slack this would kill 54 outright. All 36 (pair, third-line) combinations checked against Bader, zero adjacencies; referee spot-checked six. | T143 | T152 |
| `p3-forces-per-line-tiered-saturation-12-or-11` | 14 | **SETTLED** | T131, re-derived T132, referee-checked. At k=14, p=3 the eight lines outside a parallel pair saturate at 12 and the six inside one at 11; 8(12) + 6(11) = 162. A necessary condition on a hypothetical object, not evidence about existence. | T131 | T152 |
| `v11-12-is-the-single-unresolved-mutual-extremal-vertex` | 14 | SETTLED (not new) | T147, correct, and already written out in reference data 5 since turn 127. T148's "genuine consolidation, not new content" is the right reading. | T147 | T152 |
| `deletion-from-a-known-optimum-needs-R` | all | **DEAD (parked with reason)** | `T' = T - deg_T(l) + R_l` is correct and stays. The construction route built on it does not: R = 0 in fifteen of fifteen cases at k=15, against a requirement of 2 at k=15 -> 14, 3 at k=21 -> 20 and 4 at k=19 -> 18. Reopen only with a mechanism that predicts where R > 0 comes from. | T119 | T152 |
| `deletion-identity-is-T-minus-deg-plus-R` | 14/15 | **SETTLED (referee correction of T121-T124)** | R counts faces of the reduced arrangement that are triangles and were crossed by l, and is not always zero. T121's proof that it is miscounted a merged face's sides by one. | T119 | T127 |
| `insertion-into-k13-needs-seven-corner-clips` | 13/14 | **CONTESTED (now three faces in and no longer blocked)** | Inserting a generic line l into B gives `T' = T(B) + Y`, where Y counts l's bounded chords that clip a corner off a non-triangular face; a chord through a triangle destroys one and creates one, net zero. l has 12 bounded chords at k=13. Reaching 54 from Kabanovitch's 47 requires **Y = 7 and X <= 5**: seven of the nineteen non-triangular bounded faces corner-clipped, at most five of the forty-seven triangles crossed. Three of the nineteen are now named (reference data 9 and 10): two hexagons and a pentagon. Sixteen to go, structured as four fixed faces along the axis plus six orbit representatives. | T125 | T155 |
| `tamura-tight-implies-every-line-saturated` | all | **SETTLED (referee)** | If `T = k(k-2)/3` then p = 0 and `deg_T(l) = k-2` for every line. Suzuki's k=15 is degree-regular at 13 as a theorem. | T127 | T127 |
| `bader-three-free-segments-form-a-path` | 14 | **SETTLED** | Reference data 5. | T102 | T127 |
| `three-free-segments-prove-T-leq-53-for-this-table` | 14 | **SETTLED** | `3T <= 162 - 3`, so `T <= 53` for `kobon_14_53tri` independently of the corpus count field. | T127 | T127 |
| `bader-triangle-adjacency-test-is-iff` | 14 | **SETTLED** | T94 proposed, T95 proved sufficiency, referee supplied necessity. The most productive claim in the ledger. | T94 | T152 |
| `mutual-extremal-vertex-tv-leq-1-general` | all | **SETTLED** | T106. At a vertex where both lines are at an extremal row position the two outward rays are cyclically adjacent, never opposite, so at most one of the four sectors is a bounded triangle corner. Reference data 8's unbounded-face argument is the same geometry applied to one line at a time and it is worth noticing that the pair generalizes: extremality at a vertex is always a statement about which sectors escape. | T106 | T155 |
| `extremal-announcement-parity-O-even` | all | SETTLED | T108. `2M + O = 2k`; on k=13, 2(11) + 4 = 26. | T108 | T127 |
| `all-28-extremal-segments-accounted-third-free-is-interior` | 14 | **SETTLED** | T107, vindicated by T118. Reproduced at k=13: all 26 extremal segments are triangle sides and both free segments are interior. | T107 | T127 |
| `row1-fully-saturated-zero-free-segments` | 14 | SETTLED | T117, re-derived T118 and by the referee. | T117 | T127 |
| `line8-saturation-one-free-segment` | 14 | SETTLED | T118, referee-verified. | T118 | T127 |
| `row11-swap-8-13-nets-50-not-54` | 14 | SETTLED | T116, referee-verified. Net 50. | T116 | T127 |
| `signotope-vs-chirotope-5-element-gate` | all | SETTLED | T114. 4-element consistency does not imply realizability; the rank-3 exchange axiom is a 5-element condition. Any table surgery owes this gate, then stretchability. | T114 | T115 |
| `parallel-pair-budget-for-54` | 14 | **SETTLED** | Reference data 4. | T102 | T127 |
| `bader-face-F-is-a-pentagon` | 14 | **SETTLED** | Reference data 3. And it is now clear that the method that produced it generalizes: reference data 8 does with two lookups what reference data 3 did with a special case. | T102 | T155 |
| `suzuki-concurrency-freeness-verified` | 15 | SETTLED | T122 demanded, T123 ran, T124 re-read, referee confirmed. p = 0. | T122 | T127 |
| `global-facecount-check-is-consistency-not-verification` | 15 | SETTLED | T122. Aggregate Euler arithmetic cannot see individual side counts. | T122 | T127 |
| `k13-optimum-is-p0-two-free-segments-both-interior` | 13 | **SETTLED** | Reference data 6 and 7. | T127 | T152 |
| `line15-fusion-cannot-create-triangle` | 15 | **DEAD (refuted)** | T121, endorsed T122, banked T123, generalized T124. Side count wrong by one. Do not cite. | T121 | T127 |
| `suzuki-rotation-orbit-decomposition-unfounded` | 15 | SETTLED | T124 caught T123's claim that 5-fold rotation fixes line 15 and splits the rest into orbits of 5, which 5 does not divide. T125 withdrew. **The permutation is still not on the record**, thirty turns later, and the k=13 analogue has now paid for itself three separate times. | T124 | T155 |
| `bader-witness-75-bounded-22-nontriangular` | 14 | SETTLED (SILVER) | T89-T91, referee-corrected. | T89 | T102 |
| `bader-53-witness-is-nonsimple-parallel-built` | 14 | SETTLED | T82-T84, referee-verified. | T82 | T102 |
| `deparallelize-yields-nontriangle-all-three-pairs` | 14 | SETTLED (referee proof) | Criterion is a common extremal transversal t with V(t,a), V(t,b) adjacent in row t; all three pairs fail. | T85 | T102 |
| `bader-extremal-vertex-inventory` | 14 | SETTLED | T97, fully re-verified. 28 endpoints, 13 mutual pairs, 2 orphans, twelve of thirteen resolving. | T97 | T102 |
| `simple-line-load-bearing-verification-burden` | 14 | **CONTESTED (partially answered)** | T91's demand: before any face counts as a target, show which triangles rest on the line being moved. Answered for k=13 in full by reference data 7. Still open for eleven of Bader's fourteen lines. | T91 | T152 |
| `repair-bill-is-36-checks-not-6`, `row11-edit-5-subset-risk-bound-365-of-715`, `v11-12-corner-fix-requires-third-line-swap`, `orphan-V8-10-resolves-to-triangle-8-9-10` | 14 | SETTLED (moot or minor) | Unchanged. | - | T127 |
| `endpoint-label-match-false-positive-at-k4`, `deparallelize-shared-transversal-criterion`, `line5-partner-positions`, `extremal-ray-trick-is-local-only`, `line5-slot-accounting-4-not-2`, `line5-bounded-segment-slot-recount`, `line5-extremal-segments-may-border-unbounded-face`, `corpus-has-no-triangle-enumeration`, `bader-row9-citation-off-by-one`, `corner-slicing-program-capped-at-14`, `exterior-wedge-slicing-nets-plus-one-free`, `parallel-offset-slicing-has-constant-total-yield`, `exterior-wedge-fails-across-two-apexes`, `pentagon-corner-slice-nets-plus-one`, `sat-not-run-at-k14`, `k14-bounded-face-budget-24` | 14 | SETTLED (archive) | Statuses unchanged. `sat-not-run-at-k14` obeyed for an eighth day. Note that `line5-extremal-segments-may-border-unbounded-face` is the same observation reference data 8 has now turned into a proof; it sat in the archive as a maybe for fifty turns. | - | T155 |
| `k14-54-reachable` | 14 | **CONTESTED** | The actual question. 154 turns, zero verifier runs, zero 14-line arrangements built by either agent. New since turn 152: three of the nineteen non-triangular bounded faces of Kabanovitch's k=13 are named, the face-walk method is unblocked and cheap, and the fixed-face census predicts the shape of the remaining sixteen. Agenda item 2 — can one line corner-clip seven of nineteen — is now a finite, answerable question for the first time. | T1 | T155 |
| `mirror-program-weakly-dominated`, `pentagram-vertices-all-spoken-for`, `cluster-siting-abandoned-the-554-premise`, `outside-line-role-pigeonhole`, `similarity-rotation-budget-is-per-cluster`, `parking-confinement-blocks-secondary-reuse`, `companion-lines-are-not-free-they-are-clusters`, `companion-slopes-are-open-not-pinned`, `similarity-freedom-resolves-dual-role-tension`, `hull-avoidance-forces-external-crossings`, `direction-freedom-global`, `endpoint-match-convention-calibrated-against-k4-kills-all-three`, `local-lookup-program-exhausted` | 14 | DEAD (archive) | Unchanged. Do not cite. | - | T102 |
| `external-ray-triangle-verified`, `4cluster-negative-export-is-free`, `l1-carves-existing-ade-face`, `homothety-margin-not-scale-invariant`, `recentered-homothety-clears-E`, `wedge-cut-criterion-exact`, `pentagram-directions-equally-spaced`, `export-costs-intracluster-triangles`, `pentagram-walls-are-four-distinct`, `wall-tip-correspondence`, `cevian-wall-formula-invalid`, `euler-point-resolution-deltaF`, `degenerate-arrangement-63-faces`, `clustering-forces-three-nontriangles`, `cross-cluster-ratio-not-harder`, `homothety-realizes-S12`, `intracluster-tamura-cap-12`, `c7-mod7-kill-k14`, `central-symmetry-parallel-tax`, `mirror-fixed-lines-parallel`, `f0-no-self-symmetric-triangles`, `f0-axis-sector-forced-nontriangular`, `clustering-is-not-concurrence`, `pairwise-subarrangement-cap-67`, `mod2-weak-filter`, `cb-stacking-tautology`, `three-of-four-crossings-unhandled`, `construction-rate-far-below-target` | 14 | SETTLED (archive) | Unchanged, none cited since turn 81. | - | T81 |
| `global-counting-cannot-obstruct-k14`, `symmetry-tax-pattern`, `f0-forced-nontri-at-least-10`, `m2-exhaustively-capped-28`, `single-line-translation-export`, `export-mechanism-needs-second-line`, `bc-to-m1m2-construction-dead`, `first-m2-triangle-exhibited`, `theta10-construction-unsited`, `sliver-exposure-question`, `corridor-danger-is-local-not-global`, `corridor-clipping-debate-t47-t51`, `translation-crossings-diverge-generically`, `pairwise-cap-gives-no-pressure`, `subarrangement-averaging-upper-bound`, `cevian-r80-and-descendants`, `edge-incidence-bound-121`, `vertex-corner-identity`, `nearpencil-starves-triangles`, `m3-nearpencil-hits-ceiling`, `residue-stacking-cb-vs-improved-even` | 14/all | DEAD or CONTESTED (archive) | Unchanged. | - | T77 |
