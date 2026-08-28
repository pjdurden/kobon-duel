# Ledger

Claim registry, rewritten daily by the referee. `SETTLED` requires a complete
argument or a verifier run. Two agents agreeing is not evidence.

Rewritten by REFEREE after turn 229. Turns 180-229 audited.

**Read this first: thirty-eight of the last fifty turns are empty.** Turns 188
through 225 inclusive, and the referee pass scheduled at turn 205, all failed
with "OAuth session expired and could not be refreshed." Nothing was argued in
any of them. The ledger was therefore last rewritten after turn 180, and by the
time the agents came back at turn 226 the seven substantive turns before the
outage had fallen out of their context window entirely. Turn 226 believed the
outage was five turns long and that turn 180 was the last real content. It was
not. **Turns 181 through 187 are the strongest constructive work in the project
and turns 226 through 229 rebuilt a weaker version of it from scratch, unaware
it existed.** I have restored it as reference data 15. The lesson is structural,
not an agent failure: the ledger is the only memory this project has, and one
missed referee pass costs a week of work.

**Turns 181-187 built a real candidate and got twelve row-insertions right.**
PythagorAss gave a crossing order for a fourteenth line against Kabanovitch's B
and, under correct pressure from turns 182 and 186, pinned all twelve two-row
insertion positions for six corner-clips. I checked every one of the twelve
against reference data 6 and against the face vertex lists in reference data 3,
9 and 10. Every one is correct. Six clips into six distinct non-triangular faces
is `n_N = 6`, the alternation maximum, and would land the arrangement on 53 with
one spacer chord needed for 54.

**The chain does not exist, and the reason is two lookups.** Reference data 17.
Clipping the pentagon P at corner V(1,7) forces the very next face along line 14
to be the triangle `{1,7,12}`; clipping F3 at corner V(2,13) forces the face
immediately before it to be the triangle `{2,8,13}`. Those are the same piece of
line 14 and they are two different faces. Three turns of checking passed over
this because all three checked triples against the iff test, and the iff test
cannot validate a table, only a triple inside one.

**And the whole `n_N = 6` branch is now closed, for this base arrangement.**
Reference data 19. Not by the ordering accident that kills T181, but by a forced
chain: at `n_N = 6` the six N-chords must occupy one of seven position patterns,
every spacer sandwiched between two N-chords is a triangle, and the only chord
that can be a clipping U-chord is a terminal one. Following the forced successors
back from wedge A through triangle `{2,4,9}` or `{5,7,9}` into G1 or F5, the
N-clip two steps upstream needs a line the tail has already consumed. Both
branches die, and the mirror branches die by sigma. **`n_N = 6` implies `Y <= 6`,
so 54 out of Kabanovitch's optimum needs `n_N <= 5` and at least two clipping
U-chords.** This is the first obstruction result in the project that has survived
my own audit, and it is mine, so see the caution in finding 6.

**Turns 226-229 restarted from behind and still produced one good exchange.**
T226's sigma-lemma is right and its corridor inference is not; T227 demolished
the inference cleanly; T228 conceded it by re-deriving the double-count. That is
this cycle's silver. T228 then proposed the free-segment wedge clip, which is
correct and turns out to be the forced last step of the branch reference data 19
closes, and T229 tried to cap it at two with an argument that does not hold.

## The referee's findings this cycle

1. **Every edge of a non-triangular bounded face of B has a triangle on its far
   side, except the two free segments.** Reference data 16b. Three lines from
   reference data 4, and it does more work than anything else now in the ledger:
   it forces the successor face at every step of an inserted line's trajectory,
   it re-proves the N-N alternation cap from scratch, and it is what makes
   reference data 19 possible.
2. **The insertion problem is a walk, not a chord-typing exercise.** Reference
   data 16. Line `l`'s fourteen pieces are a walk in the face-adjacency graph of
   B consuming thirteen distinct line labels, first and last face unbounded, and
   `Y` counts the pieces whose entry and exit edges share a vertex and whose face
   is not a triangle. **The successor of a face is determined by the exit edge.
   It is not a free choice.** T181 picked six corners and hoped they chained; the
   walk formulation kills that chain in one step and would have saved six turns.
3. **`n_N = 6` implies `Y <= 6` for Kabanovitch's B.** Reference data 19. So 54
   from this base needs `n_N <= 5` and two or more clipping U-chords, which is a
   materially harder object than anything either agent has proposed.
4. **T229's cap of two is refuted.** Reference data 18. A corner clip of an
   unbounded face does not need a free segment. The k=3 to k=4 case clips a
   corner one of whose edges already carries a triangle, gains one, and the
   books close exactly. This is the fourth misuse of reference data 4's standing
   caution, after T163, T177, and the mechanism the owner struck at T170.
5. **The verifier is still gated, on the eleventh consecutive day.** I ran
   `python3 -c "print(1)"` in this session; refused before execution. Both agents
   have reported this honestly every turn they have been able to speak at all.
   Owner action, twice over now: the allowlist, and the OAuth refresh that ate
   thirty-eight turns.
6. **Caution on reference data 19, entered by me against my own result.** It is
   my argument, checked only by me, and no agent has had a turn to attack it. It
   closes one branch (`n_N = 6`) for one base arrangement (Kabanovitch's). It is
   **not** a proof that `N(14) = 53` and must not be cited as one. I am not
   calling it gold, and agenda item 1 is an instruction to try to break it.

## Call-outs, by turn number

- **T181.** Six corners chosen for having disjoint line-pairs, then sequenced by
  writing the pairs down in order. Disjointness of line-pairs is not a chaining
  condition and nothing in the turn checks that the six clips can follow one
  another. The turn calls its own gap "which face a spacer lands in", which is
  the right question asked one level too weakly: the spacer is not a thing to be
  discovered later, it is **forced** by the previous clip's exit edge. Reference
  data 17 kills the chain with two lookups in reference data 7's own list.
- **T182.** Correct and important. "A single permutation of thirteen crossings
  does not pin down a table" is exactly right and it produced the best six turns
  of the project. Credit where it is due.
- **T184.** "Both pinned clips actually do pass the iff test... I'm not going to
  manufacture a problem with something that's actually correct." The triples are
  correct and the table is impossible. The iff test (reference data 2) tells you
  which triples are triangular **given a valid table**; it cannot tell you a
  table is valid. Declining to manufacture an objection is good discipline; it is
  not a substitute for asking what lies on the far side of the edge each clip
  exits through, which is one lookup per clip.
- **T185, T186.** Same omission, twice more. Twelve pins were checked, six iff
  tests were run and re-run, and across three turns nobody looked at the far side
  of a single exit edge. All six far sides are named triangles sitting in
  reference data 7.
- **T186.** Named the gap correctly, then reached for the most expensive
  available tool. "A signotope question across a quadruple `{14,7,9,x}`" is the
  costly framing of a cheap fact: the face after the P-clip is forced and it is a
  triangle already in the ledger. `signotope-vs-chirotope-5-element-gate` has now
  been nominated as "the concrete next step" in five separate turns over 229
  turns and run zero times. **It is a ritual. Stop citing it until someone runs
  one**, and if it is unrunnable by hand, say so instead.
- **T187.** The best turn of the stretch and the one the outage buried. It went
  looking for a bonus triangle `{14,8,12}`, found that it would reuse the
  crossing V(14,12) that the F2 clip already spends, and reported the error
  itself. That is reference data 4 applied at a vertex instead of a segment, it
  is correct, and it is the first time in the thread anybody used that rule
  without misusing it.
- **T188 through T225.** Thirty-eight consecutive turns lost to OAuth expiry,
  including the turn-205 referee pass. Not an agent fault. Recorded because the
  public transcript should show why the argument appears to restart at T226.
- **T226.** "The last five turns on the record, 220 through 225, are empty." It
  was thirty-eight, 188 through 225. The count is wrong and the consequence is
  worse: the turn rebuilt from a stale baseline without asking whether anything
  had been lost between the ledger's last rewrite and its own context window.
- **T226, the corridor.** Counted five sigma-fixed faces twice, once for line 7
  and once for line 8, and called the total a density. The sigma-lemma the same
  turn proves is precisely what makes that double-count mandatory, so the
  evidence offered for the corridor is the lemma restating itself.
- **T228.** "That's two concrete, mechanism-backed triangles." One clip is
  genuine and correct. Two is not available: reference data 19 shows each wedge
  clip has to be a terminal bounded chord of `l` with hexagon A or B immediately
  upstream, and the position patterns admit at most one such chord when
  `n_N = 6`. T228 flagged joint realizability as its own honest gap and was right
  to; the answer is no.
- **T229.** Fourth misuse of reference data 4's standing caution. "Their bounded
  edges are already triangle sides, meaning a clip there nets zero by 11b" reads
  11b, which is about a chord lying **inside** a triangle, as if it governed a
  chord lying in an unbounded face that happens to border one. Those are two
  different chords of the same line and only the second one nets zero. Reference
  data 18 gives the complete k=3 to k=4 counterexample.
- **T229, the abandoned promise.** T227 ended "I'll bring that computation next
  turn rather than a promissory note", naming the adjacency data of agenda item
  3. T229 brought a cap argument instead and the computation is still not on the
  record. Both agents did this: T226 and T228 each closed by committing to
  deliver a full chord typing "next turn" and neither did.
- **Good behaviour, named.** T183 conceded T182's critique by re-deriving why a
  corner clip is a two-row fact rather than restating that it is. T187 reported
  its own error while it was still winning. T227's refutation of the corridor is
  clean, quantitative and does not overreach into claiming it closes anything.
  T228 conceded it in the same terms and kept the part of its own lemma that
  survived. That is the standard the project asks for.

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

**The adjacency question the T180 agenda assigned here is now answered, and the
answer needed no census at all.** It asked, for each of the nineteen, how many of
its edges border an unbounded face of B. By reference data 16b the answer is
**zero for seventeen of them, and exactly one each for hexagons A and B**, whose
free segments are the only bounded segments in the arrangement with a
non-triangle on both sides. Agenda item 3 of the T180 agenda is closed. Face size
is likewise irrelevant to the gain (reference data 11a caps every piece at +1).
What the census still owes is the eight unnamed faces themselves, and one of them
in particular: see the agenda.

---

## Referee reference data 15: the T181-T185 candidate, restored and verified

Recovered from turns 181, 183 and 185, which fell out of both agents' context
during the thirty-eight-turn outage. Insert a fourteenth line `l` into
Kabanovitch's B (reference data 6). Row 14, `l`'s own crossing order, is

    14:  1  7  2 13  9  4  6 11  5 10  3 12  8

and the six claimed corner-clips, with both row insertions each:

    clip  face  corner    row/gap                   row/gap
    1     P     V(1,7)    row 1 between 7 and 8     row 7 between 12 and 1
    2     F3    V(2,13)   row 2 between 13 and 8    row 13 between 2 and 7
    3     A     V(9,4)    row 9 between 5 and 4 *   row 4 between 9 and 2
    4     B     V(6,11)   row 6 between 10 and 11 * row 11 between 6 and 13
    5     F5    V(5,10)   row 5 between 7 and 10    row 10 between 8 and 5
    6     F2    V(3,12)   row 3 between 7 and 12    row 12 between 8 and 3

`*` = the free segment itself. Row 8 was never pinned.

**All twelve insertions are correct.** I checked each gap against the printed row
in reference data 6 and against the face's vertex list in reference data 3, 9 and
10: in every case the two named entries are consecutive in the row and the
segment between them is the face's edge on that line. Each clip individually is a
genuine corner clip of a genuine non-triangular face, worth +1 by 11a. What is
wrong with the candidate is the **sequencing**, not the clips. See reference
data 17.

## Referee reference data 16: an inserted line's trajectory is a forced walk

**(a) The segment census.** B has 143 bounded segments and 47 triangles. By
reference data 4 a bounded segment is a side of at most one triangle, so the 141
triangle-sides are 141 distinct segments and exactly 2 carry no triangle at all:
the free segments (`k13-free-segments-forced-by-b-mod-3`, reference data 7).

**(b) The successor lemma.** Let F be one of the nineteen non-triangular bounded
faces of B and `e` an edge of F. Then the face on the far side of `e` is

    a triangle of B                      if e is one of the 141, and
    a 3-sided unbounded wedge            if e is one of the 2 free segments.

It is never another non-triangular bounded face. Proof: `e` is bounded, so it has
two faces; F is not a triangle, so the one triangle `e` may serve is on the far
side; if `e` is free, reference data 8 identifies the far face as the unbounded
wedge spanned by `e` and two rays. Note the corollary the T180 agenda was
reaching for: **exactly two edges in the entire arrangement separate a
non-triangular bounded face from an unbounded one.**

**(c) The walk.** `l`'s fourteen pieces (reference data 11, T159) form a walk

    U_0 , F_1 , F_2 , ... , F_12 , U_13

in the face-adjacency graph of B, where consecutive faces share an edge lying on
the line crossed at that step, the thirteen crossed lines are all distinct, and
`U_0`, `U_13` are unbounded. Then

    Y = # { i : F_i is not a triangle, and F_i's entry and exit edges
                share a vertex }

by 11a (a chord cutting a convex n-gon yields a triangle iff it separates a
single vertex) and 11b (in a triangle the gain is zero). **The successor of a
face is determined by the exit edge. It is not chosen.** This is the fact T181
through T186 did not have.

**(d) The alternation cap, re-proved.** Two consecutive pieces share an edge, so
by (b) no two consecutive pieces are both in non-triangular bounded faces. Hence
`n_N <= 6`, and at `n_N = 6` the six N-chords are a 6-subset of `{1,...,12}` with
no two consecutive: there are `C(7,6) = 7` such subsets.

**(e) Interior spacers are triangles.** If a spacer at position `m` has N-chords
at `m-1` and `m+1`, its face is the far side of both flanking clips' edges, so by
(b) it is a triangle or a free-segment wedge; a wedge has exactly one bounded
edge (reference data 8) so it cannot border two distinct N-faces. Triangle. It
gains 0.

## Referee reference data 17: the T181 chain is impossible

Two lookups in reference data 7.

- P's edge on line 7 is `V(1,7)-V(7,12)` = row 7 positions 10-11 (`12 1`). The
  only triangle that segment can serve is `{1,7,12}`, and `{1,7,12}` **is** in
  reference data 7, with row-1 positions 5-6 (`12 7`) and row-12 positions 8-9
  (`7 1`) confirming all three legs. So the face across P's line-7 edge is the
  triangle `{1,7,12}`.
- F3's edge on line 2 is `V(2,13)-V(2,8)` = row 2 positions 6-7 (`13 8`). The
  only triangle that segment can serve is `{2,8,13}`, which **is** in reference
  data 7, with row-13 positions 5-6 (`8 2`) and row-8 positions 5-6 (`13 2`)
  confirming the other two legs. So the face across F3's line-2 edge is the
  triangle `{2,8,13}`.

Row 14 crosses `1, 7, 2, 13, ...`, so the piece between the line-7 crossing and
the line-2 crossing is simultaneously the face across P's line-7 edge and the
face across F3's line-2 edge. `{1,7,12} != {2,8,13}`. **The chain is dead as
ordered.** The twelve pins survive, the six clips survive individually, the
sequence does not.

## Referee reference data 18: a corner clip does not need a free segment

T229 claimed only a free segment can be corner-clipped, hence a cap of 2. The
failing step is the appeal to 11b. **11b is about a chord lying inside a
triangle.** A clip chord lies inside an *unbounded* face; the triangle sharing
the clipped edge is a different face, entered by a *different* chord of `l`, and
it is that other chord which nets zero.

**Complete worked instance, k=3 to k=4.** B = three lines in general position,
triangle `ABC` with `A = V(1,2)`, `B = V(1,3)`, `C = V(2,3)`, `T(B) = 1`. All
three bounded segments are triangle sides, so B has **no** free segment at all.
Let U be the unbounded face across `AB` from `C`: sides are the segment `AB` on
line 1 and the rays of lines 2 and 3 from `A` and `B`. Insert line 4 crossing
line 2 on its ray at `q`, then line 1 inside `AB` at `p`, then line 3 inside `BC`
at `r`.

    piece            face      result                              gain
    ray                 -      unbounded                            0
    chord q->p          U      clips corner A: triangle {1,2,4}     +1
    chord p->r        ABC      destroys {1,2,3}, creates {1,3,4}     0
    ray                 -      unbounded                            0

`T = 2 = N(4)`, and `N(4) - N(3) = 1 = 1 + 0`. The books close exactly, and the
clipped edge `Ap` is part of `AB`, which already carries triangle `ABC`.
**Freeness is not required and the cap of 2 is false.** What T229 was reaching
for, and what is true, is reference data 19.

## Referee reference data 19: `n_N = 6` forces `Y <= 6` in Kabanovitch's B

Suppose `l` is inserted into B with `n_N = 6` and `Y = 7`. By 16d the six
N-chords are one of seven non-consecutive 6-subsets of `{1,...,12}`; by 16e every
spacer sandwiched between two N-chords is a triangle and gains 0. So the +7 needs
all six N-chords to clip **and** a seventh gain from a spacer that is not
sandwiched. Two shapes of pattern:

**Shape 1, patterns `{1,3,5,7,9,11}` and `{2,4,6,8,10,12}`.** Exactly one spacer
is unsandwiched: position 12 (resp. 1). Reversing `l` if needed, take it to be
12. It must gain, so it is not a triangle, so by 16b the exit edge of the N-clip
at chord 11 is a **free segment**, so chord 11's face is hexagon A or hexagon B
and chord 12's face is wedge A or wedge B. By sigma take A. Then crossing 12 is
line 9 (inside the free segment). Wedge A's edges are the free segment and the
rays of lines 4 and 5, so crossing 13 is line 4 or line 5; hexagon A's line-9
edge is adjacent only to its line-4 edge (at `V(9,4)`) and its line-5 edge (at
`V(5,9)`), so for chord 11 to clip, crossing 11 is line 4 or line 5. Two cases,
and both are the same argument:

    crossing 11 = 4, crossing 13 = 5:
      spacer 10 = far side of A's line-4 edge V(9,4)-V(4,2) = triangle {2,4,9}
        (in reference data 7; row 4 pos 1-2 `9 2`, row 2 pos 2-3 `9 4`,
         row 9 pos 5-6 `4 2`)
      chord 10 exits {2,4,9} on line 4, so it entered on line 2 or 9;
        line 9 is crossing 12, so crossing 10 = line 2
      chord 9 = far side of {2,4,9}'s line-2 edge V(2,9)-V(2,4) = G1
        (reference data 14: G1 = V(2,4)-V(2,9)-V(3,9)-V(3,13)-V(13,10)-V(10,4))
      chord 9 exits G1 on line 2; G1's line-2 edge is adjacent only to its
        line-9 edge and its line-4 edge, so crossing 9 must be line 9 or line 4
      both are already spent, at crossings 12 and 11.        CONTRADICTION

    crossing 11 = 5, crossing 13 = 4:
      spacer 10 = far side of A's line-5 edge V(7,5)-V(5,9) = triangle {5,7,9}
        (row 5 pos 1-2 `9 7`, row 7 pos 2-3 `9 5`, row 9 pos 3-4 `7 5`)
      chord 10 entered on line 7 (line 9 is crossing 12), so crossing 10 = 7
      chord 9 = far side of {5,7,9}'s line-7 edge V(7,9)-V(7,5) = F5
        (reference data 10: F5 = V(5,10)-V(8,10)-V(6,8)-V(6,9)-V(7,9)-V(5,7))
      F5's line-7 edge is adjacent only to its line-9 and line-5 edges, so
        crossing 9 must be line 9 or line 5; both spent.     CONTRADICTION

Wedge B gives the sigma-images of both cases (`sigma: A -> B`,
`{2,4,9} -> {6,11,13}`, `{5,7,9} -> {6,8,10}`, `G1 -> sigma(G1)`, `F5 -> F5`),
which die identically.

**Shape 2, the five middle patterns.** Each has exactly two unsandwiched
spacers and they are **adjacent**, at positions `j, j+1`. Suppose one of them is
unbounded. A wedge's neighbours are its hexagon (across the free segment) and
two unbounded faces (across its rays), so:
 - if spacer `j` is wedge A, spacer `j+1` is unbounded and is reached across a
   ray, so it is not wedge A or B (wedge B shares no line with wedge A's rays);
   but spacer `j+1` must be the far side of the N-clip at `j+2`, hence a triangle
   or a wedge, by 16b. Contradiction.
 - if spacer `j+1` is a wedge, spacer `j` is its neighbour and must be the far
   side of the N-clip at `j-1`, hence a triangle or a wedge; a triangle cannot
   border a wedge (a wedge's only bounded-face neighbour is its hexagon, which is
   not a triangle), and wedges A and B share no edge. Contradiction.

So both spacers are triangles, both gain 0, and `Y <= 6`.

**Conclusion.** `n_N = 6` implies `Y <= 6`. Reaching 54 by inserting a line into
Kabanovitch's optimum therefore requires `n_N <= 5` and **at least two clipping
U-chords**, since `Y <= n_N + n_U` and every clipping U-chord is now known not to
be cheap. Note what this does *not* say: it says nothing about the other k=13
optima, and it is not a proof that `N(14) = 53`. It is one branch, one base.

---

## Table

| slug | k | status | evidence | opened | last touched |
|---|---|---|---|---|---|
| `n-face-edges-carry-triangles-except-free-segments` | 13 | **SETTLED (referee)** | Reference data 16b. 143 bounded segments, 141 triangle-sides, 2 free; a non-triangular bounded face is never on the triangle side, so every edge of the nineteen has a triangle across it except the two free segments, which have unbounded wedges. Answers the T180 agenda's adjacency question outright: 17 of the 19 faces border no unbounded face at all, hexagons A and B border exactly one each. | T230 | T230 |
| `insertion-trajectory-is-a-forced-walk` | all | **SETTLED (referee)** | Reference data 16. `l`'s 14 pieces are a walk in B's face-adjacency graph with 13 distinct line labels; `Y` counts pieces whose entry and exit edges share a vertex and whose face is not a triangle; **the successor face is determined by the exit edge**. Replaces the chord-typing frame of reference data 11 with something that constrains. | T230 | T230 |
| `n-N-6-forces-Y-at-most-6-in-kabanovitch` | 13/14 | **SETTLED (referee), UNATTACKED** | Reference data 19. Seven position patterns, interior spacers forced to triangles, the only clipping U-chord terminal, then the forced chain wedge A -> `{2,4,9}` or `{5,7,9}` -> G1 or F5 needs a line already spent. Mirror cases by sigma. **Consequence: 54 from Kabanovitch's B needs `n_N <= 5` and two clipping U-chords.** Flagged UNATTACKED because it is the referee's own argument and no agent has had a turn on it. Not a proof that `N(14) = 53`. | T230 | T230 |
| `t181-six-clip-chain-as-ordered` | 14 | **DEAD (refuted by referee)** | Reference data 17. The spacer between the P-clip and the F3-clip must be triangle `{1,7,12}` and triangle `{2,8,13}` at once. Checked in T184, T185 and T186 and missed in all three. | T181 | T230 |
| `t181-t185-twelve-row-insertions-correct` | 14 | **SETTLED (referee-verified)** | Reference data 15. All twelve two-row pins for the six corner-clips check out against reference data 6 and the face vertex lists. The clips are individually genuine; only the sequencing fails. Recovered from turns 181-185 after the outage dropped them from both agents' context. | T183 | T230 |
| `corner-clip-requires-a-free-segment` | all | **REFUTED (referee)** | Reference data 18. T229's cap of 2. Misreads 11b, which governs a chord **inside** a triangle, as governing a chord in an unbounded face bordering one. The k=3 to k=4 instance has zero free segments, clips an edge that already carries a triangle, gains +1, and the arithmetic closes exactly. Fourth misuse of reference data 4's standing caution. Do not cite. | T229 | T230 |
| `free-segment-wedge-clip-gains-one` | 13/14 | **SETTLED** | T228's mechanism is correct: enter wedge A across the free segment, leave across a ray meeting its far endpoint, +1. Reference data 19 shows it is not one option among many but the forced final step of the `n_N = 6` branch, and that the branch then dies two steps upstream. Right move, wrong reason, dead end. | T228 | T230 |
| `sigma-fixed-face-line-set-is-sigma-invariant` | 13 | **SETTLED (referee-verified)** | T226. A sigma-fixed face's supporting-line set is sigma-invariant, and `sigma(7) = 8`, so it contains both 7 and 8 or neither. Verified on P, F2, F3, F4, F5. Referee addition: the set is a union of sigma-orbits, so `|S|` is even unless line 1 bounds the face, which is exactly why P is the only odd fixed face. Retrodictive, not predictive; the census was already closed. | T226 | T230 |
| `line-7-8-corridor-is-a-density-artifact` | 13 | **SETTLED (SILVER)** | T226 claimed lines 7 and 8 border 7 of 11 named faces so the corridor is the dense target. T227 subtracted the five sigma-fixed faces, which the same turn's own lemma forces to contain both lines, and the count collapses to 2 of 6 each, an even split. T228 conceded by re-deriving the double-count and dropped the inference while keeping the lemma. Recorded disagreement, evidence-gated concession, falsifiable claim. **Third silver in the ledger.** | T226 | T230 |
| `iff-test-cannot-validate-a-table` | all | **SETTLED (referee)** | The reference data 2 test says which triples are triangular **given** a valid arrangement table. Six locally-true triples were checked across T184, T185 and T186 and the table they sat in does not exist. State it once here so it is never used as a table certificate again. | T230 | T230 |
| `corner-clip-cannot-reuse-a-crossing` | 14 | **SETTLED** | T187. `{14,8,12}` would need line 14 adjacent to 8 on the far side of the crossing V(14,12) that the F2 clip already spends. One crossing, one position, two sides, one of them already taken. Reference data 4 applied at a vertex, and the first correct use of that rule in the thread. | T187 | T230 |
| `mirror-translate-family-capped-at-36` | 14 | **SETTLED (referee)** | Reference data 13. Segment-type count on a single line, no angles, no D, no order type. `T <= 22 + 7 + 7 = 36` for the entire distant-mirror family; `T <= 28` in the clustered regime, reproducing T178. Kills T170's 96-of-98 saturation demand, T171's "compute the stable order type", and the whole of T173-T179 as a line of inquiry. | T180 | T180 |
| `insertion-gain-ratio-refutes-y-bound-program` | all | **SETTLED (referee)** | Reference data 12. `N(13) - N(12) = 9` from 11 chords; `N(15) - N(14) >= 11` from 13 chords; ratios of 0.78 to 0.86 across k=9, 11, 13. The 7-from-12 that k=14 needs is a ratio of 0.58, milder than three closed cases already realize. **Agenda item 2 of the owner override is dead.** Bounding Y below 7 is not a plausible target and was never checked against KNOWN.md before being promoted. | T180 | T180 |
| `insertion-leak-is-u-chords-not-rays` | all | **SETTLED (referee)** | Reference data 11. Rays gain exactly 0 (recession-cone argument, needs only no-parallels). Every piece gains at most 1 (the `a+3`/`b+3` split). The leak in T163's partition is bounded chords lying in **unbounded** faces. The k=4 to k=5 case pins it: 3 chords, 1 non-triangular bounded face, gain 3, so at least 2 chords sit in unbounded wedges and all 3 gain. The owner correction reached the right verdict by the wrong route; this replaces it. | T180 | T180 |
| `insertion-y-capped-at-6-independent-of-concurrence-count` | 13/14 | **REFUTED (owner T170, referee-confirmed T180)** | T167's `Y <= (n+m+1)/2 = 6.5`. Algebra right, partition wrong. See reference data 11d. Do not cite. | T167 | T180 |
| `generic-insertion-into-any-simple-13-line-caps-53` | 13/14 | **REFUTED (owner T170, referee-confirmed T180)** | T168's generalization inherits the same omission. Reference data 12 now also shows it is false in spirit: the insertion gain at k=12 -> 13 is already 9. | T168 | T180 |
| `no-two-nontriangular-faces-share-an-edge` | 13 | **SETTLED as stated, MISUSED twice downstream** | The literal claim is true and is Tamura's per-segment argument. What does not follow is any cap on Y, because the chord classes are not exhaustive. Misused at T163 and again at T177 under the name "segment supply". Keep the fact, never the corollary. | T163 | T180 |
| `unbounded-wedge-clip-creates-bounded-triangle` | all | **SETTLED (referee)** | Reference data 11d, 11e and now 18, which supplies a complete worked k=3 -> k=4 instance with the gains tallied piece by piece. It is a chord phenomenon, it does not need a free segment, and it is the only source of a seventh triangle once reference data 19 caps the N-clips. | T170 | T230 |
| `two-clipping-u-chords-needed` | 13/14 | **OPEN, and this is now the live question** | Reference data 19 replaces the old `n-u-chord-count-unknown` framing. `n_U` in the abstract is not the quantity; a bare U-chord is worthless and `n_U = 12` is achievable by a line that misses B's bounded region entirely and gains almost nothing. The question is whether one straight line can make **two clipping U-chords** while still making five N-clips, on thirteen crossings. Nobody has exhibited or excluded it. | T180 | T230 |
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
| `insertion-into-k13-needs-seven-corner-clips` | 13/14 | **CONTESTED, and now half-closed** | `T' = T(B) + Y`; reaching 54 from 47 needs `Y = 7` from 12 bounded chords. Reference data 12 still says 7/12 is unremarkable next to the 9/11 realized at k=12 -> 13, so the route stays live. But reference data 19 closes the `n_N = 6` half of it for Kabanovitch's base, which is the half both agents have spent every constructive turn on. What is left is `n_N <= 5` with two clipping U-chords. | T125 | T230 |
| `tamura-tight-implies-every-line-saturated` | all | **SETTLED (referee)** | Suzuki's k=15 is degree-regular at 13 as a theorem. | T127 | T127 |
| `bader-three-free-segments-form-a-path` | 14 | **SETTLED** | Reference data 5. | T102 | T127 |
| `three-free-segments-prove-T-leq-53-for-this-table` | 14 | **SETTLED** | `3T <= 162 - 3`. | T127 | T127 |
| `bader-triangle-adjacency-test-is-iff` | 14 | **SETTLED** | T94 proposed, T95 proved sufficiency, referee supplied necessity. Still the most productive claim in the ledger. | T94 | T152 |
| `mutual-extremal-vertex-tv-leq-1-general` | all | **SETTLED** | T106. Extremality at a vertex is a statement about which sectors escape. | T106 | T155 |
| `extremal-announcement-parity-O-even` | all | SETTLED | T108. `2M + O = 2k`. | T108 | T127 |
| `all-28-extremal-segments-accounted-third-free-is-interior` | 14 | **SETTLED** | T107, vindicated T118, reproduced at k=13. | T107 | T127 |
| `row1-fully-saturated-zero-free-segments`, `line8-saturation-one-free-segment`, `row11-swap-8-13-nets-50-not-54` | 14 | SETTLED | T117, T118, T116, all referee-verified. | - | T127 |
| `signotope-vs-chirotope-5-element-gate` | all | SETTLED, **and now a banned incantation** | T114. Any table surgery owes the rank-3 exchange axiom, then stretchability. 229 turns, zero invocations. It was nominated as "the concrete next step" at T182, T184, T186 and twice more, including at moments when a two-lookup argument (reference data 17) settled the same question. **Do not name it as a next step again unless you run one in the same turn or explain why it cannot be run by hand.** | T114 | T230 |
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
| `k14-54-reachable` | 14 | **CONTESTED** | The actual question. 229 turns, zero verifier runs (tool unavailable, referee-confirmed again this cycle), zero 14-line arrangements built. This cycle moved it, for the first time, toward 53: reference data 19 closes the `n_N = 6` insertion branch for Kabanovitch's optimum. That is one branch of one base of one route and it is my own unattacked argument, so the row stays CONTESTED and the prior does not move. | T1 | T230 |
| `mirror-program-weakly-dominated`, `pentagram-vertices-all-spoken-for`, `cluster-siting-abandoned-the-554-premise`, `outside-line-role-pigeonhole`, `similarity-rotation-budget-is-per-cluster`, `parking-confinement-blocks-secondary-reuse`, `companion-lines-are-not-free-they-are-clusters`, `companion-slopes-are-open-not-pinned`, `similarity-freedom-resolves-dual-role-tension`, `hull-avoidance-forces-external-crossings`, `direction-freedom-global`, `endpoint-match-convention-calibrated-against-k4-kills-all-three`, `local-lookup-program-exhausted` | 14 | DEAD (archive) | Unchanged. Do not cite. | - | T102 |
| `external-ray-triangle-verified`, `4cluster-negative-export-is-free`, `l1-carves-existing-ade-face`, `homothety-margin-not-scale-invariant`, `recentered-homothety-clears-E`, `wedge-cut-criterion-exact`, `pentagram-directions-equally-spaced`, `export-costs-intracluster-triangles`, `pentagram-walls-are-four-distinct`, `wall-tip-correspondence`, `cevian-wall-formula-invalid`, `euler-point-resolution-deltaF`, `degenerate-arrangement-63-faces`, `clustering-forces-three-nontriangles`, `cross-cluster-ratio-not-harder`, `homothety-realizes-S12`, `intracluster-tamura-cap-12`, `c7-mod7-kill-k14`, `central-symmetry-parallel-tax`, `mirror-fixed-lines-parallel`, `f0-no-self-symmetric-triangles`, `f0-axis-sector-forced-nontriangular`, `clustering-is-not-concurrence`, `pairwise-subarrangement-cap-67`, `mod2-weak-filter`, `cb-stacking-tautology`, `three-of-four-crossings-unhandled`, `construction-rate-far-below-target` | 14 | SETTLED (archive) | Unchanged. | - | T81 |
| `global-counting-cannot-obstruct-k14`, `symmetry-tax-pattern`, `f0-forced-nontri-at-least-10`, `m2-exhaustively-capped-28`, `single-line-translation-export`, `export-mechanism-needs-second-line`, `bc-to-m1m2-construction-dead`, `first-m2-triangle-exhibited`, `theta10-construction-unsited`, `sliver-exposure-question`, `corridor-danger-is-local-not-global`, `corridor-clipping-debate-t47-t51`, `translation-crossings-diverge-generically`, `pairwise-cap-gives-no-pressure`, `subarrangement-averaging-upper-bound`, `cevian-r80-and-descendants`, `edge-incidence-bound-121`, `vertex-corner-identity`, `nearpencil-starves-triangles`, `m3-nearpencil-hits-ceiling`, `residue-stacking-cb-vs-improved-even` | 14/all | DEAD or CONTESTED (archive) | Unchanged. | - | T77 |
