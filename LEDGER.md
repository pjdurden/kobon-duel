# Ledger

Claim registry, rewritten daily by the referee. `SETTLED` requires a complete
argument or a verifier run. Two agents agreeing is not evidence.

Rewritten by REFEREE after turn 179. Turns 156-179 audited.

Three things happened in this stretch and only one of them was worth 24 turns.

**Turns 156-162 finished the face census and did it correctly.** Eleven of the
nineteen non-triangular bounded faces of Kabanovitch's k=13 optimum are now named
and I checked every one of them edge by edge against the printed rows: F2, F3,
F4, F5, G1, H1, plus the two hexagons, the pentagon P, and the two sigma-images.
All fifty-eight cited row adjacencies hold. All five sigma-fixed faces are named
and they sit on the axis in exactly the order reference data 10 predicted. This
is the most solid block of work in the project's history and both agents did it.

**Turns 163-168 built a wrong bound.** The owner refuted it after turn 170. I have
now audited that stretch myself and the owner is right, but the diagnosis in the
owner correction was one step off and I have replaced it with reference data 11.
The leak is not `l`'s two rays. Rays provably gain nothing. The leak is that a
**bounded chord of `l` can lie in an unbounded face of B**, and clipping the
corner of an unbounded wedge creates a bounded triangle that the T/N labelling
never counts. The k=4 to k=5 case saturates this exactly: three chords, one
non-triangular bounded face, gain of three, so at least two of the three chords
must be sitting in unbounded faces and every one of the three gains.

**Turns 169-179 spent eleven turns on a construction family that a two-line
count kills.** PythagorAss proposed a 7-line optimum plus its mirror image pushed
to infinity. Turns 171 through 179 then argued about angles, critical directions,
quotient-rule derivatives, monotonicity regimes and hinge lines, and every one of
those arguments is angle-dependent and regime-dependent. None of them asked the
prior question: how many mixed triangles can this family have at all? The answer
is at most fourteen, for any directions, any axis, any D past threshold, and it
follows from counting segment types on a single line. **The family caps at 36
triangles.** It never had a route to 53, let alone 54. Reference data 13.

## The referee's findings this cycle

1. **The verifier really is unavailable, and the agenda was wrong to blame the
   agents.** I tried `python3 -c`, `/usr/bin/python3 -c`, and a chained form.
   All three were refused before execution in this session, exactly as turns 172
   through 179 reported. The agents told the truth for eight consecutive turns
   while the agenda threatened them with a NO_VERIFIER_RUN stamp for it. The fix
   is an owner action on the permission allowlist, not an agent behaviour. The
   threat is withdrawn until the tool exists.
2. **Agenda item 2, "the whole of k=14 now reduces to bounding Y", is dead, and
   KNOWN.md kills it without any geometry.** Reference data 12. Deleting a line
   from a k=13 optimum leaves at most N(12) = 38, so re-inserting gains at least
   9 out of 11 bounded chords. At k=15 the same computation forces a gain of at
   least 11 out of 13. The gain-to-chord ratio runs at 0.78 to 0.86 in the
   neighbouring closed cases. Reaching 54 at k=14 needs 7 out of 12, a ratio of
   0.58, which is **below** what k=9, k=11 and k=13 already achieve. Any program
   whose goal is to prove `Y <= 6` is trying to prove something the neighbouring
   values say is not true of insertion in general. Nine turns of it, then an
   owner override promoting it to the highest-value target in the project. It was
   never a target.
3. **The mirror-translate family caps at 36.** Reference data 13. Two lines of
   counting, no angles. It also reproduces turn 178's bound of three mixed
   triangles per side as the special case where every line clusters its new
   crossings at one end, which is a check on both results.
4. **Turn 179 re-imported a conclusion turn 176 had already shown does not
   follow.** Details in the call-outs below.

## Call-outs, by turn number

- **T163 through T168.** Six turns of correct algebra on a case split nobody
  checked for exhaustiveness. Both agents verified the sums. Neither asked what
  face a chord lands in when it is not a triangle and not one of the nineteen.
  T164 came within one sentence of catching it, then spent the turn on
  concurrences instead.
- **T168.** "This closes one construction method, not k=14." The disclaimer was
  right for the wrong reason. The generalization to every simple 13-line base was
  the tell: it would have proved `N(14) <= 53` outright, which should have
  triggered a check against KNOWN.md's own increments. Nobody ran that check for
  eleven turns. It takes one subtraction.
- **T169.** Euclidn't accepted T168's generalization with "I have nothing to
  concede since the insertion-from-13 program was retired in my favor." A result
  that hands you your own conclusion is the one you should audit hardest. This is
  the single clearest instance in the thread of the failure mode the project
  exists to detect.
- **T171 through T179.** Eleven turns inside a family that a segment-type count
  caps at 36. Every turn in this stretch is locally correct and globally wasted.
  The specific missed move: T170 established that all 49 cross-family crossings
  land outside both lines' old spans. That single fact makes the old crossings on
  each line contiguous, which caps old-new adjacencies at two per line, which
  caps the mixed triangle count at fourteen. It is available at T171 and neither
  agent took it in nine subsequent turns.
- **T177.** "By the one-triangle-per-segment rule, a claimed segment cannot also
  serve as V(i,i') for a new mixed triangle." This is the owner-refuted mechanism
  from T163 reappearing under a new name seven turns after it was struck from the
  ledger, in a turn that opens by citing reference data 4. T178 caught it and
  T179 withdrew it properly. Credit to both, but the ledger said this in writing
  and it was cited anyway.
- **T179.** "cos(theta_i) changes sign exactly once as theta_i ranges over
  (0,180), at 90. That means there are at most two monotonicity regimes for the
  ranking function." The ranking function
  `g_i(theta_j) = cos(theta_j)/sin(theta_i+theta_j)` has a **pole** at
  `theta_j = 180 - theta_i`, and that pole moves with i. On each side of the pole
  g is monotone; across it g jumps from minus infinity to plus infinity. So the
  induced ranking of the seven mirror lines depends on where the pole sits
  relative to them, which is i-dependent. T176 stated this correctly ("it only
  forces monotonicity within each line's own arc, and the arc boundary itself
  moves") and T179 dropped the clause without argument. The "at most two distinct
  hinge values" conclusion is not established. It is also moot, per reference
  data 13.
- **T160, gate stamp.** The mechanical gate stamped UNGROUNDED_CONCESSION on a
  turn that does re-derive the conceded lemma in its own words. The gate is
  wrong there. Noting it so the public record is not misread.
- **Good behaviour, named.** T176 conceded a bound against its own prior and then
  strengthened it with an exact derivative rather than accepting the opponent's
  weaker limit argument. T178 refuted a mechanism and then explicitly declined to
  claim the refutation rescued its own position. T179 withdrew a mechanism with a
  re-derivation of why it was the wrong mechanism, not a restatement. That is
  three consecutive turns of the standard the project asks for, spent on a dead
  family.

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

Derived by three local arguments from the table alone, no coordinates.

## Referee reference data 4: the parallel-pair budget

For k lines, p parallel pairs, no concurrences: `V = C(k,2) - p`, `E = 2V + k`,
bounded segments `B = k(k-2) - 2p`. Tamura's argument runs segment by segment: a
bounded segment on line a with endpoints V(a,b), V(a,c) is a side of at most one
triangular face, namely {a,b,c}, on the side of a containing V(b,c). Hence

    T <= floor(B/3) = floor((k(k-2) - 2p)/3)      and      sum_l deg_T(l) = 3T

At k = 14: p=0 gives 56, p=1 gives 55, p=2 and p=3 give 54, p=4 gives 53. Any
14-line arrangement with 54 triangles has **p <= 3**, and at p = 3 it has zero
slack. Bader sits at p = 3 with 53, so **exactly three** of its 162 bounded
segments are free.

**Standing caution, added after T177.** This rule says a segment is a side of at
most one triangle *in the arrangement it belongs to*. It says nothing about the
far side of that segment, and nothing at all about what happens after new lines
are inserted. It has now been misused for that purpose twice, at T163 and T177.

## Referee reference data 5: Bader's three free segments and the deficiency path

    S1  line 11, row-11 positions 1-2    V(11,12) - V(11,13)   cand {11,12,13}
    S2  line 12, row-12 positions 1-2    V(12,11) - V(12,8)    cand {8,11,12}
    S3  line  8, row-8  positions 2-3    V(8,10)  - V(8,12)    cand {8,10,12}

They form a connected path:

    V(11,13) --11-- V(11,12) --12-- V(8,12) --8-- V(8,10)

S1 and S2 are two adjacent sides of pentagon F; S3 hangs off F's corner V(8,12).
The path is not a near-miss triangle: the only triangle lines 8, 11, 12 can bound
is {8,11,12}, which fails two of its three legs.

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

## Referee reference data 7: the k=13 optimum, completely solved

**Both free segments.** Segment A is line 9, row-9 positions 4-5,
V(9,5) - V(9,4), candidate `{4,5,9}`. Segment B is line 6, row-6 positions 4-5,
V(6,10) - V(6,11), candidate `{6,10,11}`. Rows 4, 5, 7, 12, 13 are fully
saturated.

**The mirror automorphism.** `sigma: 1 -> 1, i -> 15 - i` for i in 2..13.
Applying sigma entrywise to row i yields row sigma(i) exactly for i = 2..13, and
yields the reverse of row 1 for i = 1. Verified on all thirteen rows.

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

`{1,7,8}` is the unique sigma-fixed triangle; the other 46 fall into 23 orbits.

## Referee reference data 8: the side rule, and why a free segment has an unbounded face

**The side rule (two lookups).** For lines y and z,

    "after x in row y" and "after x in row z" name the same side of x
    iff  V(y,z) is after x in row y  and  V(y,z) is after x in row z

Chaining from one reference line orients all k-1 lines with respect to x in k-2
lookups; a single turn in a face walk needs one such comparison, two row lookups.

**Why one face on a free segment is unbounded.** Let the free segment be
V(9,4) - V(9,5). Row 4 has 9 at position 1 and row 5 has 9 at position 1, so both
rays point away from the triangle lines 4, 5, 9 bound, hence into the same open
half-plane of line 9. The region bounded by the segment and the two rays admits
no crossing line, so it is a single unbounded face with three sides. **Each free
segment contributes one of the nineteen, not two.**

## Referee reference data 9: the two free-segment faces of k=13, both hexagons

    Segment A face:  V(9,4) - V(4,2) - V(2,10) - V(10,7) - V(7,5) - V(5,9)
    Segment B face:  V(6,11) - V(11,13) - V(13,5) - V(5,8) - V(8,10) - V(10,6)

Both hexagons, one sigma-orbit. All twelve edges verified adjacent in their rows.

## Referee reference data 10: the mirror axis and the fixed-face census

**Fixed vertices.** Exactly six: V(2,13), V(3,12), V(4,11), V(5,10), V(6,9),
V(7,8). **Fixed edges.** Exactly one: V(1,7) - V(1,8), row 1 positions 6-7.

The axis meets the arrangement in seven points, eight arcs, two unbounded, so it
passes through six bounded faces, one of which is the triangle `{1,7,8}`. Hence

    exactly 5 of the 19 non-triangular bounded faces are sigma-fixed,
    and the other 14 form exactly 7 sigma-orbits.

**The five fixed faces, all now named and all referee-verified.**

    P  = V(1,7) - V(7,12) - V(12,3) - V(3,8) - V(8,1)                 pentagon
    F2 = V(3,12) - V(3,7) - V(7,11) - V(4,11) - V(4,8) - V(8,12)      hexagon
    F3 = V(4,11) - V(4,7) - V(7,13) - V(2,13) - V(2,8) - V(8,11)      hexagon
    F4 = V(2,13) - V(8,13) - V(5,8) - V(5,10) - V(7,10) - V(2,7)      hexagon
    F5 = V(5,10) - V(8,10) - V(6,8) - V(6,9) - V(7,9) - V(5,7)        hexagon

**Axis order, complete.**

    infinity - V(7,8) - {1,7,8} - mid(V(1,7),V(1,8)) - P - V(3,12) - F2
             - V(4,11) - F3 - V(2,13) - F4 - V(5,10) - F5 - V(6,9) - infinity

Every fixed vertex appears exactly once and in the right place. The census of
sigma-fixed faces is closed.

## Referee reference data 11: the corrected insertion accounting (replaces the owner's diagnosis)

Insert a straight line `l` into a simple 13-line arrangement B, generic: `l`
misses every vertex and is parallel to no line of B. `l` is cut by its 13
crossings into 2 rays and 12 bounded chords, which lie in 14 **distinct** faces
of B (convexity, T159). Write `T(A) = T(B) + Y`.

**(a) Every piece gains at most 1.** A convex n-gon cut by a chord entering
through one edge and leaving through another splits into parts with `a+3` and
`b+3` sides where `a + b = n - 2`. Both parts are triangles only if `a = b = 0`,
i.e. `n = 2`, impossible. So no piece of `l` ever creates two triangles.

**(b) A chord lying in a triangle of B gains exactly 0.** `n = 3` forces
`{a,b} = {0,1}`, parts of 3 and 4 sides: one triangle destroyed, one created.

**(c) The two rays of `l` gain exactly 0.** Let a ray of `l` lie in an unbounded
face U of B. With no parallels, U's recession cone is a wedge spanned by its two
boundary rays' directions, with nonempty interior, and `l`'s direction lies
strictly inside it (equality would mean `l` is parallel to a line of B). The ray
splits U into two parts whose recession cones are the two sub-wedges, both
nonempty, so both parts are unbounded. No triangle is created. **The owner
correction's "corner-clip an unbounded wedge" mechanism is real but it is a
chord phenomenon, not a ray phenomenon.**

**(d) Where the leak actually is.** A **bounded chord** of `l` can lie in an
unbounded face of B. T163's labelling of the twelve chords as T (in a triangle)
or N (in one of the nineteen) is therefore not exhaustive: there is a third
class, U-chords, and a U-chord clipping the corner of an unbounded wedge produces
a bounded triangle worth +1 that the alternation argument never sees. Writing
`n_T + n_N + n_U = 12`, the true statement is

    Y <= n_N + n_U,     with no two consecutive chords both N.

The N-N alternation lemma survives intact. It just does not bound Y.

**(e) The k=4 to k=5 case saturates this exactly, and is the cleanest test.**
A simple 4-line arrangement has 3 bounded faces; `N(4) = 2` so two are triangles
and one is not. Insert the fifth line: 3 bounded chords, 2 rays, `N(5) = 5`, so
`Y = 3`. Rays give 0 by (c) and chords in triangles give 0 by (b), so all three
chords gain, and since only one non-triangular bounded face exists, **at least
two of the three chords sit in unbounded faces.** Every chord gains, and the
alternation cap of `ceil(3/2) = 2` is beaten by the U-chords alone.

## Referee reference data 12: the gain-to-chord ratio, computed from KNOWN.md

Delete one line from an optimal k-line arrangement: what remains has at most
`N(k-1)` triangles, so re-inserting that line gains at least `N(k) - N(k-1)`,
using at most `k-2` bounded chords. No geometry, no order type, three subtractions.

    k    N(k-1) -> N(k)    min gain    chords (k-2)    ratio
    5      2 ->  5            3            3           1.00
    7      7 -> 11            4            5           0.80
    9     15 -> 21            6            7           0.86
    11    25 -> 32            7            9           0.78
    13    38 -> 47            9           11           0.82
    ---
    14    47 -> 54            7           12           0.58   (what 54 needs)

**Consequence.** Any program aiming to prove `Y <= 6` for insertion into a
13-line arrangement is aiming below a ratio that k=9, k=11 and k=13 all exceed on
closed, published values. In particular `Y = 9` is realized at k=12 -> 13 and
`Y >= 11` is forced at k=14 -> 15. The insertion gain is not a quantity that
alternation-style arguments cap near half the chord count; empirically it runs at
four fifths of it. The reduction "k=14 reduces to bounding Y" is sound as a
reduction and useless as a route, because the bound it needs is milder than what
neighbouring cases already achieve, not stronger.

## Referee reference data 13: the mirror-translate family caps at 36

The family (T170, conceded T171): take 7 lines, reflect across an axis, translate
the mirror copy by `D * n_hat` with `D` past the threshold `D0`, so that all 49
cross-family crossings land outside both lines' old spans.

**Step 1. Both halves survive whole.** If a mirror line met the interior of a
bounded face of the original half, it would cross some original line at a point
inside that line's old span, contradiction. So every bounded face of each half is
a face of the union, and same-side triangles number `2 * T(half) <= 22`.

**Step 2. Old crossings are contiguous on every line.** On original line `l_i`
the 6 old crossings occupy a consecutive block of the 13 and the 7 new ones lie
outside it. So `l_i`'s 12 bounded segments split as 5 old-old, at most 2 old-new
(one per end of the old block), and the rest new-new. **At most two old-new
segments per line**, and exactly one when the new crossings all cluster at a
single end.

**Step 3. Every mixed triangle burns two old-new segments.** A triangle on the
14 lines uses either 3 originals, 3 mirrors, or 2 of one and 1 of the other. Take
`{i, i', j}` with `i, i'` original and `j` mirror. Its side on line `i` joins
`V(i,i')` (old) to `V(i,j)` (new), so it is an old-new segment of `l_i`; its side
on `l_i'` is likewise an old-new segment of `l_i'`. By reference data 4 each
segment serves at most one triangle. The 7 original lines carry at most 14
old-new segments in total, so there are **at most 7 triangles of type
{2 original, 1 mirror}**, and by mirror symmetry at most 7 of type
{1 original, 2 mirror}.

**Conclusion.**

    T(mirror-translate family) <= 22 + 7 + 7 = 36

for every choice of the seven directions, every axis, every `D > D0`, split or
clustered. That is 17 below the best known k=14 construction and 18 below the
target. **The family was never a candidate.**

**Cross-check against the agents' own numbers.** In the fully clustered regime
each line has one old-new segment, not two, so the original half carries 7 of
them and the type-{2,1} count drops to `floor(7/2) = 3`, giving `T <= 22+3+3 =
28`. That is exactly T178's mutual-extremality bound of three per side, obtained
here by counting segment types instead of ranking angles. T178's number is
correct; T175's 4 and T177's 4 were reached by a refuted mechanism and are
superseded. T170's demand that 96 of 98 new segments triangulate is refuted
outright: at most 42 of them can be triangle sides in the split case.

## Referee reference data 14: census status, k=13 non-triangular bounded faces

Eleven of nineteen named, all verified by the referee against reference data 6
row by row. Five sigma-fixed (P, F2, F3, F4, F5, reference data 10) and three
sigma-orbits:

    orbit 1   the two free-segment hexagons A and B          (reference data 9)
    orbit 2   G1 = V(2,4)-V(2,9)-V(3,9)-V(3,13)-V(13,10)-V(10,4)
              sigma(G1) on lines {2,5,6,11,12,13}
    orbit 3   H1 = V(2,5)-V(5,12)-V(12,4)-V(4,8)-V(8,11)-V(2,11)
              sigma(H1) on lines {3,4,7,10,11,13}

Ten hexagons and one pentagon so far. **Four orbits, eight faces, remain.**
Note for the corrected insertion question: face size is now known to be
irrelevant to the gain (reference data 11a caps every piece at +1), so what the
census still owes is not more polygons but **adjacency data**: for each of the
nineteen, how many of its edges border an unbounded face of B.

---

## Table

| slug | k | status | evidence | opened | last touched |
|---|---|---|---|---|---|
| `mirror-translate-family-capped-at-36` | 14 | **SETTLED (referee)** | Reference data 13. Segment-type count on a single line, no angles, no D, no order type. `T <= 22 + 7 + 7 = 36` for the entire distant-mirror family; `T <= 28` in the clustered regime, reproducing T178. Kills T170's 96-of-98 saturation demand, T171's "compute the stable order type", and the whole of T173-T179 as a line of inquiry. | T180 | T180 |
| `insertion-gain-ratio-refutes-y-bound-program` | all | **SETTLED (referee)** | Reference data 12. `N(13) - N(12) = 9` from 11 chords; `N(15) - N(14) >= 11` from 13 chords; ratios of 0.78 to 0.86 across k=9, 11, 13. The 7-from-12 that k=14 needs is a ratio of 0.58, milder than three closed cases already realize. **Agenda item 2 of the owner override is dead.** Bounding Y below 7 is not a plausible target and was never checked against KNOWN.md before being promoted. | T180 | T180 |
| `insertion-leak-is-u-chords-not-rays` | all | **SETTLED (referee)** | Reference data 11. Rays gain exactly 0 (recession-cone argument, needs only no-parallels). Every piece gains at most 1 (the `a+3`/`b+3` split). The leak in T163's partition is bounded chords lying in **unbounded** faces. The k=4 to k=5 case pins it: 3 chords, 1 non-triangular bounded face, gain 3, so at least 2 chords sit in unbounded wedges and all 3 gain. The owner correction reached the right verdict by the wrong route; this replaces it. | T180 | T180 |
| `insertion-y-capped-at-6-independent-of-concurrence-count` | 13/14 | **REFUTED (owner T170, referee-confirmed T180)** | T167's `Y <= (n+m+1)/2 = 6.5`. Algebra right, partition wrong. See reference data 11d. Do not cite. | T167 | T180 |
| `generic-insertion-into-any-simple-13-line-caps-53` | 13/14 | **REFUTED (owner T170, referee-confirmed T180)** | T168's generalization inherits the same omission. Reference data 12 now also shows it is false in spirit: the insertion gain at k=12 -> 13 is already 9. | T168 | T180 |
| `no-two-nontriangular-faces-share-an-edge` | 13 | **SETTLED as stated, MISUSED twice downstream** | The literal claim is true and is Tamura's per-segment argument. What does not follow is any cap on Y, because the chord classes are not exhaustive. Misused at T163 and again at T177 under the name "segment supply". Keep the fact, never the corollary. | T163 | T180 |
| `unbounded-wedge-clip-creates-bounded-triangle` | all | **SETTLED (referee)** | Reference data 11d and 11e. It happens, it is a chord phenomenon, and at k=4 -> 5 it accounts for at least two of the three gained triangles. What remains open is the **count**: how many of `l`'s twelve chords can lie in unbounded faces of a simple 13-line arrangement. That number, `n_U`, is now the only unknown in `Y <= n_N + n_U`. | T170 | T180 |
| `n-u-chord-count-unknown` | 13/14 | **OPEN, and this is the live question** | `l` has 12 bounded chords; each lies in one of B's 26 unbounded faces or 66 bounded ones, all distinct by convexity. Nobody has bounded `n_U` in either direction. A bound `n_U + n_N <= 6` would close k=14; reference data 12 says do not expect one. A construction with `n_N + n_U >= 7` all clipping is the other side. | T180 | T180 |
| `same-quadrant-mirror-forces-single-hinge` | 14 | **SETTLED (SILVER)** | T175 proposed it in the eps -> 0 narrow-band limit; T176 conceded against its own prior and **strengthened** it with the exact derivative `g'(theta_j) = -cos(theta_i)/sin^2(theta_i+theta_j)`, valid for any seven directions in a common quadrant, no limit needed. I re-derived the quotient rule and it is right: on a common quadrant `theta_i + theta_j` never reaches a pole, so `g` is strictly decreasing throughout and the nearest new crossing on every original line is the same mirror line. Genuine forced convergence, evidence-gated, on a falsifiable statement. **Second silver in the ledger.** Its value is bounded by reference data 13: it is a sharp result about a family that dies to a cruder count. | T175 | T180 |
| `mirror-hinge-ranking-has-a-moving-pole` | 14 | **CONTESTED (referee correction of T179)** | `g_i(theta_j) = cos(theta_j)/sin(theta_i+theta_j)` has a pole at `theta_j = 180 - theta_i` that moves with i; across it `g` jumps from `-inf` to `+inf`. T176 said so explicitly; T179's "at most two monotonicity regimes, hence at most two distinct hinge values" drops that clause without argument and does not follow. Moot under reference data 13, recorded so the reasoning error is not inherited. | T179 | T180 |
| `mixed-triangle-segment-supply-cap` | 14 | **DEAD (refuted T178, withdrawn T179)** | T177's "a claimed Tamura segment cannot serve as `V(i,i')` for a new mixed triangle". T178's refutation is correct: Tamura's rule constrains one side of a segment in one arrangement and says nothing about a different triangle in a larger arrangement. T179 withdrew with a correct re-derivation. Superseded in any case by reference data 13, which reaches a stronger bound without it. | T177 | T180 |
| `distant-axis-preserves-same-side-triangles` | 14 | **SETTLED** | T170's limit argument, re-derived independently at T171 with the explicit affine `t(D) = a + bD`. Referee-checked: the crossing parameter along `l_i` has leading term `D cos(theta_j)/sin(theta_i+theta_j)`, which diverges whenever `sin(theta_i+theta_j) != 0`. Finite intersection of 49 eventually-true conditions gives one `D0`. This is the one durable result of the mirror stretch, and reference data 13 is built on it. | T170 | T180 |
| `mirror-translate-involution-phi` | 14 | **SETTLED** | T172, re-derived T173. `phi = T_v after R` with `v` along the axis normal satisfies `phi^2 = id`, swaps the two sevens, fixes no line, so no triangle is phi-fixed and every triangle sits in an orbit of 2. Correct and now decorative. | T172 | T180 |
| `mirror-line-new-point-split-forced-by-critical-direction` | 14 | **SETTLED, then answered** | T173 showed the divergence sign can differ across mirror lines, splitting a line's new crossings across both ends. T174 answered it with an explicit shear-into-a-narrow-band recipe, conceded T175. Both are right; reference data 13 shows the split case caps at 36 and the clustered case at 28, so the distinction never mattered. | T173 | T180 |
| `straight-insertion-visits-distinct-faces-by-convexity` | all | **SETTLED** | T159, conceded with re-derivation T160. A line meets a convex region's boundary at most twice, so `l`'s 14 pieces lie in 14 distinct faces of B. Load-bearing in reference data 11. The T160 gate stamp of UNGROUNDED_CONCESSION on that turn is a gate error; the turn does re-derive. | T159 | T180 |
| `k13-axis-face-census-complete` | 13 | **SETTLED (referee-verified edge by edge)** | Reference data 10 and 14. T156 gave F2 and F3, T157 gave F4 and F5, and all five sigma-fixed faces sit on the axis in the predicted order. I checked all 30 cited row adjacencies against reference data 6 and every one holds. Agenda item 1 of the T155 agenda is closed and was closed correctly. | T156 | T180 |
| `k13-orbit-faces-g1-h1-and-images` | 13 | **SETTLED (referee-verified)** | T158's G1, T159's `sigma(G1)`, T160's H1, T161's `sigma(H1)`. All twelve of G1's and H1's cited row adjacencies check out. Eleven of nineteen named; four orbits remain. | T158 | T180 |
| `triangle-list-resolves-sector-ambiguity-without-side-rule` | 13 | **SETTLED** | T156's tool: at a walk vertex, test the candidate triple against reference data 7's list of 47; a genuine triangle occupies a known sector, so the exit edge is pinned. Equivalent in strength to reference data 8 and cheaper. It is what made T156-T162 fast. | T156 | T180 |
| `folding-back-is-discovery-redundancy-not-target-shrinkage` | 13 | **SETTLED** | T162, conceded with re-derivation at T163. A hexagon has six sides so six of the 141 triangle-side seeds point at it; two walks landing on the same face is what redundancy predicts. Correctly kills T161's inference. | T162 | T180 |
| `extreme-concurrence-yields-no-chord-not-a-gain` | 13/14 | **SETTLED** | T165, sharpened T166 into zero credit rather than reduced credit, via the argument that a bounded face cannot contain an unbounded ray with no earlier crossing. Independent of the refuted cap and survives it. | T165 | T170 |
| `face-walk-side-test-is-two-lookups` | all | **SETTLED (referee)** | Reference data 8. Two agents declared the method blocked at T153-T154 on the turn before it would have worked. | T153 | T155 |
| `k13-free-segment-outer-face-is-unbounded` | 13 | **SETTLED** | Reference data 8. Each free segment contributes one of the nineteen, not two. | T153 | T155 |
| `k13-free-segment-faces-are-a-hexagon-sigma-pair` | 13 | **SETTLED (referee)** | Reference data 9. | T155 | T155 |
| `k13-mirror-axis-fixed-cell-census` | 13 | **SETTLED (referee)** | Reference data 10, and now fully instantiated: all five fixed faces named and axis-ordered. The prediction held. | T155 | T180 |
| `k13-fixed-pentagon-on-line-1` | 13 | **SETTLED (referee)** | Reference data 10. | T155 | T155 |
| `perfect-extremal-score-equivalent-to-zero-slack` | 14 | **SETTLED (self-reversal resolved at T154)** | Not silver: no opponent forced it. | T137 | T155 |
| `zero-slack-forbids-mutual-extremal-failure` | 14 | **DEAD (true but not a shortcut)** | Usable as a filter on a candidate table, nothing more. | T108 | T155 |
| `suzuki-deletion-route-fully-exhausted` | 15/14 | **SETTLED (computed twice, second run defective)** | `R_l = 0` for all fifteen l. T145 and T151 each mislabelled a candidate; referee ran both missing checks. Result stands, second run does not establish it. | T119 | T152 |
| `two-leg-near-miss-is-a-counting-artifact` | 15 | **DEAD (refuted by referee)** | The leg that held in each case is the one the deletion creates by definition. | T135 | T152 |
| `k13-second-free-segment-is-line6-row-positions-4-5` | 13 | **SETTLED (referee)** | Reference data 7. | T152 | T152 |
| `k13-complete-47-triangle-enumeration` | 13 | **SETTLED (referee)** | Reference data 7, cross-checked three ways. | T152 | T152 |
| `k13-mirror-automorphism` | 13 | **SETTLED (referee)** | Verified on all thirteen rows. It has now paid five times: free segments, triangle orbits, the fixed-face census, `sigma(G1)` and `sigma(H1)`. The single most productive structural fact in the project. | T152 | T180 |
| `k13-free-segments-forced-by-b-mod-3` | 13 | **SETTLED (SILVER)** | T140, conceded by re-derivation T141, referee-verified. `143 mod 3 = 2`. At k=14, p=3, `162 mod 3 = 0`, so a 54-triangle arrangement has zero free segments. | T140 | T152 |
| `parallel-pair-adjacency-forced-free-mechanism-cleared-in-bader` | 14 | **SETTLED** | T143, all 36 combinations checked. | T143 | T152 |
| `p3-forces-per-line-tiered-saturation-12-or-11` | 14 | **SETTLED** | T131, re-derived T132. `8(12) + 6(11) = 162`. | T131 | T152 |
| `v11-12-is-the-single-unresolved-mutual-extremal-vertex` | 14 | SETTLED (not new) | Already in reference data 5 since T127. | T147 | T152 |
| `deletion-from-a-known-optimum-needs-R` | all | **DEAD (parked with reason)** | `T' = T - deg_T(l) + R_l` stays; the construction route on it does not. Note reference data 12 uses the same identity in the other direction and gets a live result out of it. | T119 | T180 |
| `deletion-identity-is-T-minus-deg-plus-R` | 14/15 | **SETTLED (referee)** | R is not always zero; T121's proof miscounted a merged face's sides by one. | T119 | T127 |
| `insertion-into-k13-needs-seven-corner-clips` | 13/14 | **CONTESTED (reopened, correctly stated at last)** | `T' = T(B) + Y` with `Y` the number of `l`'s pieces that clip a corner. Reaching 54 from 47 needs `Y = 7` out of 12 bounded chords. Reference data 11 gives the correct decomposition `Y <= n_N + n_U`; reference data 12 says a ratio of 7/12 is unremarkable next to the 9/11 realized at k=12 -> 13. This is the live route and it is a **construction** route, not an obstruction route. | T125 | T180 |
| `tamura-tight-implies-every-line-saturated` | all | **SETTLED (referee)** | Suzuki's k=15 is degree-regular at 13 as a theorem. | T127 | T127 |
| `bader-three-free-segments-form-a-path` | 14 | **SETTLED** | Reference data 5. | T102 | T127 |
| `three-free-segments-prove-T-leq-53-for-this-table` | 14 | **SETTLED** | `3T <= 162 - 3`. | T127 | T127 |
| `bader-triangle-adjacency-test-is-iff` | 14 | **SETTLED** | T94 proposed, T95 proved sufficiency, referee supplied necessity. Still the most productive claim in the ledger. | T94 | T152 |
| `mutual-extremal-vertex-tv-leq-1-general` | all | **SETTLED** | T106. Extremality at a vertex is a statement about which sectors escape. | T106 | T155 |
| `extremal-announcement-parity-O-even` | all | SETTLED | T108. `2M + O = 2k`. | T108 | T127 |
| `all-28-extremal-segments-accounted-third-free-is-interior` | 14 | **SETTLED** | T107, vindicated T118, reproduced at k=13. | T107 | T127 |
| `row1-fully-saturated-zero-free-segments`, `line8-saturation-one-free-segment`, `row11-swap-8-13-nets-50-not-54` | 14 | SETTLED | T117, T118, T116, all referee-verified. | - | T127 |
| `signotope-vs-chirotope-5-element-gate` | all | SETTLED, **still never invoked** | T114. Any table surgery owes the rank-3 exchange axiom, then stretchability. 179 turns, zero invocations, because nobody has produced a candidate table to test. | T114 | T180 |
| `parallel-pair-budget-for-54` | 14 | **SETTLED** | Reference data 4. | T102 | T127 |
| `bader-face-F-is-a-pentagon` | 14 | **SETTLED** | Reference data 3. | T102 | T155 |
| `suzuki-concurrency-freeness-verified`, `global-facecount-check-is-consistency-not-verification` | 15 | SETTLED | T122-T124. | - | T127 |
| `k13-optimum-is-p0-two-free-segments-both-interior` | 13 | **SETTLED** | Reference data 6 and 7. | T127 | T152 |
| `line15-fusion-cannot-create-triangle` | 15 | **DEAD (refuted)** | Side count wrong by one. Do not cite. | T121 | T127 |
| `suzuki-rotation-orbit-decomposition-unfounded` | 15 | SETTLED | T124 caught T123. **The permutation is still not on the record**, fifty-five turns later, while the k=13 analogue has now paid five times. | T124 | T180 |
| `bader-witness-75-bounded-22-nontriangular` | 14 | SETTLED (SILVER) | T89-T91, referee-corrected. | T89 | T102 |
| `bader-53-witness-is-nonsimple-parallel-built`, `deparallelize-yields-nontriangle-all-three-pairs`, `bader-extremal-vertex-inventory` | 14 | SETTLED | T82-T85, T97. | - | T102 |
| `simple-line-load-bearing-verification-burden` | 14 | **CONTESTED (answered for k=13)** | Reference data 7 answers it in full at k=13. Still open for eleven of Bader's fourteen lines. | T91 | T152 |
| `repair-bill-is-36-checks-not-6`, `row11-edit-5-subset-risk-bound-365-of-715`, `v11-12-corner-fix-requires-third-line-swap`, `orphan-V8-10-resolves-to-triangle-8-9-10` | 14 | SETTLED (moot or minor) | Unchanged. | - | T127 |
| `endpoint-label-match-false-positive-at-k4`, `deparallelize-shared-transversal-criterion`, `line5-partner-positions`, `extremal-ray-trick-is-local-only`, `line5-slot-accounting-4-not-2`, `line5-bounded-segment-slot-recount`, `line5-extremal-segments-may-border-unbounded-face`, `corpus-has-no-triangle-enumeration`, `bader-row9-citation-off-by-one`, `corner-slicing-program-capped-at-14`, `exterior-wedge-slicing-nets-plus-one-free`, `parallel-offset-slicing-has-constant-total-yield`, `exterior-wedge-fails-across-two-apexes`, `pentagon-corner-slice-nets-plus-one`, `sat-not-run-at-k14`, `k14-bounded-face-budget-24` | 14 | SETTLED (archive) | Unchanged. `sat-not-run-at-k14` obeyed for a ninth day. `exterior-wedge-slicing-nets-plus-one-free` is the same phenomenon reference data 11d has now made central; it sat in the archive for a hundred turns while T163-T168 built a bound that contradicts it. | - | T180 |
| `k14-54-reachable` | 14 | **CONTESTED** | The actual question. 179 turns, zero verifier runs (tool unavailable, verified by the referee), zero 14-line arrangements built by either agent. Nothing this cycle moved it in either direction: the census firmed up, one construction family died at 36, and the only claimed obstruction was refuted. | T1 | T180 |
| `mirror-program-weakly-dominated`, `pentagram-vertices-all-spoken-for`, `cluster-siting-abandoned-the-554-premise`, `outside-line-role-pigeonhole`, `similarity-rotation-budget-is-per-cluster`, `parking-confinement-blocks-secondary-reuse`, `companion-lines-are-not-free-they-are-clusters`, `companion-slopes-are-open-not-pinned`, `similarity-freedom-resolves-dual-role-tension`, `hull-avoidance-forces-external-crossings`, `direction-freedom-global`, `endpoint-match-convention-calibrated-against-k4-kills-all-three`, `local-lookup-program-exhausted` | 14 | DEAD (archive) | Unchanged. Do not cite. | - | T102 |
| `external-ray-triangle-verified`, `4cluster-negative-export-is-free`, `l1-carves-existing-ade-face`, `homothety-margin-not-scale-invariant`, `recentered-homothety-clears-E`, `wedge-cut-criterion-exact`, `pentagram-directions-equally-spaced`, `export-costs-intracluster-triangles`, `pentagram-walls-are-four-distinct`, `wall-tip-correspondence`, `cevian-wall-formula-invalid`, `euler-point-resolution-deltaF`, `degenerate-arrangement-63-faces`, `clustering-forces-three-nontriangles`, `cross-cluster-ratio-not-harder`, `homothety-realizes-S12`, `intracluster-tamura-cap-12`, `c7-mod7-kill-k14`, `central-symmetry-parallel-tax`, `mirror-fixed-lines-parallel`, `f0-no-self-symmetric-triangles`, `f0-axis-sector-forced-nontriangular`, `clustering-is-not-concurrence`, `pairwise-subarrangement-cap-67`, `mod2-weak-filter`, `cb-stacking-tautology`, `three-of-four-crossings-unhandled`, `construction-rate-far-below-target` | 14 | SETTLED (archive) | Unchanged. | - | T81 |
| `global-counting-cannot-obstruct-k14`, `symmetry-tax-pattern`, `f0-forced-nontri-at-least-10`, `m2-exhaustively-capped-28`, `single-line-translation-export`, `export-mechanism-needs-second-line`, `bc-to-m1m2-construction-dead`, `first-m2-triangle-exhibited`, `theta10-construction-unsited`, `sliver-exposure-question`, `corridor-danger-is-local-not-global`, `corridor-clipping-debate-t47-t51`, `translation-crossings-diverge-generically`, `pairwise-cap-gives-no-pressure`, `subarrangement-averaging-upper-bound`, `cevian-r80-and-descendants`, `edge-incidence-bound-121`, `vertex-corner-identity`, `nearpencil-starves-triangles`, `m3-nearpencil-hits-ceiling`, `residue-stacking-cb-vs-improved-even` | 14/all | DEAD or CONTESTED (archive) | Unchanged. | - | T77 |
