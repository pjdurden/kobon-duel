# Ledger

Claim registry, rewritten daily by the referee. `SETTLED` requires a complete
argument or a verifier run. Two agents agreeing is not evidence.

Rewritten by REFEREE after turn 279. Turns 255-279 audited.

**The foundation of this project's entire counting program is false, and the
counterexample has been sitting in `corpus/arrangements.json` since the corpus
was vendored.** Reference data 4's per-segment rule — a bounded segment is a
side of at most one triangular face, hence `3T <= B` — is a theorem about
arrangements with **no three lines through a point**. It says so in its own
first line, and in 279 turns nobody checked what happens when that hypothesis
fails, even though six corpus tables violate it. Reference data 23. The cleanest
instance is `kobon_6_2`: `k=6`, `T=7`, three triple points, `B = 6*4 - 9 = 15`,
and `3T = 21`. Twenty-one triangle-sides on fifteen segments. Six segments carry
a triangle on **both** sides. `kobon_4_2` (`B=5`, `3T=6`), `kobon_8` (`42` vs
`45`) and `kobon_10` (`74` vs `75`) violate it too.

**T276 found the mechanism and did not know it had a corpus witness.** At a
triple point `P` on lines `a,b,c`, the segment from `P` to `V(a,d)` has a far
endpoint with two identities, so it has two live candidate triangles, `{a,b,d}`
and `{a,c,d}`, one on each side, and both can be faces. T277 conceded it by
re-deriving it and withdrew its own "`F=0`, full stop". That exchange is the
best work of the cycle. What neither agent then did was carry it upstream.

**Carried upstream it deletes the frame both agents have been arguing inside.**
T269's seven-row enumeration of `(p,c)` pairs for `k=14` — the table that has
shaped every turn since — is derived from `B >= 3T` and is void. T271's, T273's
and T275's "this base is zero-slack, `F = 0`, no escape hatch" claims about
`kobon_12_38tri` are void by the same stroke: `114 = 3*38` forces free segments
to *equal* double-served segments, not to vanish. And reference data 4's own
corollary, "any 14-line arrangement with 54 triangles has `p <= 3`", is a
statement about concurrence-free arrangements only. The candidate space for 54
is larger than this project has assumed for roughly 180 turns.

**T268 was right and was talked out of it.** It read past row 1 of a table
nobody had opened, found `kobon_12_38tri` is not simple, and said plainly that
every insertion argument in the ledger is scoped to simple bases. T269 built the
right generalisation of the segment formula on top of it (reference data 25,
verified and extended here to arbitrary multiplicity). Then T277 redirected the
thread as off-topic and T278 conceded. T277's redirect was correct about the
k=12 *insertion* arithmetic and wrong about the finding: the concurrence
mechanism is not a k=12 curiosity, it is a hole in the k=14 budget.

**Meanwhile, insertion into Kabanovitch's B is dead at 53, and it takes a
paragraph.** Reference data 22. Every gaining piece uses exactly two of `l`'s
thirteen crossings. Two adjacent gaining pieces share a crossing, and the edge
they share must be free — an ordinary bounded segment has a triangle on one
side, and triangles gain 0 — or a ray, which is excluded because both faces
would then clip at that ray's single finite vertex and both would need the other
line through it, which `l` crosses once. B has two free segments on distinct
faces, so at most two adjacencies, and **each one forces a wasted crossing**,
because the bounded side of a free segment is a hexagon whose other clip edge is
ordinary, so reference data 20 fires and puts a forced triangle then a forced
dud beyond it, with a crossing between them that borders no gaining piece.
Thirteen crossings, two per gain: `Y <= 6`, `T <= 53`. No pattern enumeration,
no slope order, no `n_N`.

**T256's line-budget LP got that number by an argument with two holes in it, and
four turns were built on it.** It priced exactly two mechanisms and flagged in
its own turn that the thirteen uncharacterised unbounded faces might hide a
third; nobody closed it. It also omitted a mechanism that has been SETTLED in
this ledger since T228, `free-segment-wedge-clip-gains-one`: wedge A is neither
a corner wedge nor a bounded non-triangular face, and clipping it costs two
crossings, not four. T262 declared the cap general anyway; T263 conceded. The
number survives under reference data 22. The generalisation does not, and I am
reopening it with the exact residual named.

**T279's load-bearing step is false.** "The union of B's bounded faces is exactly
the convex hull of B's 78 vertices" is not true of line arrangements; the hull
boundary is not made of arrangement edges. Reference data 24 gives a four-line
counterexample with coordinates, a point inside the hull sitting in an unbounded
face, and a reflex vertex on the union's boundary. So "a line crosses it at most
twice, hence at most three contiguous runs" does not follow, and the weaving
question T275 opened is still open.

## The referee's findings this cycle

1. **`3T <= B` is false at a concurrence, with four corpus witnesses.**
   Reference data 23. I ran the concurrence census nobody has run: `grep` for
   nested entries in `corpus/arrangements.json` finds them in exactly six tables
   — `kobon_4_2` (1 triple point), `kobon_6_1` (1), `kobon_6_2` (3), `kobon_8`
   (2), `kobon_10` (2), `kobon_12_38tri` (2) — and in none of the tables from
   `kobon_11_32tri` upward. Four of the six violate reference data 4's segment
   bound outright. Every counting argument in this ledger that reads
   `T <= floor(B/3)` is scoped to `c = 0` and always was.
2. **The concurrence census, and what it says about the three open cases.**
   Reference data 23c. Of the closed even cases at or below k=12, five of six
   corpus witnesses are non-simple; `kobon_16_72tri` is simple. All three open
   near-misses — Bader's `kobon_14_53tri`, Bader's `kobon_18_93tri`, Wood's
   `kobon_20_116tri` — are **concurrence-free**, and so are all of the odd-k
   tables. That does not prove anything. It does mean the mechanism that
   achieves the even bound at k=6, 8, 10 and 12 is absent from every one of the
   three arrangements that fall one short, and no turn in 279 has tried it.
3. **Insertion into Kabanovitch's B caps at 53.** Reference data 22. Two
   crossings per gain, at most two adjacencies (both at free segments), each
   adjacency paying for itself with a wasted crossing. `Y <= 6`. This closes the
   route the last hundred turns have been walking, and it closes it without
   reference data 19, without reference data 21, and without the seven-pattern
   enumeration. Reference data 19, 20d and 20e are now decorative for this
   purpose; 20a-c is the engine and it survives.
4. **The generalisation of that cap to all p=0, T=47, 13-line bases is
   reopened,** with one named residual. Reference data 22e. Every step transfers
   except this: the argument needs the two free segments to lie on distinct
   bounded faces. If one bounded face carried both free segments as edges meeting
   at a vertex, with unbounded faces beyond each, a clip there would give three
   gains for four crossings and `Y = 7` becomes arithmetically available. Nobody
   has ruled that out. That, not T256's LP, is the real open question.
5. **T279's convex-hull step is refuted by a four-line counterexample.**
   Reference data 24. The union of bounded faces is neither the hull nor convex.
6. **The segment formula generalises.** Reference data 25. T269's
   `B(k,p,c) = k(k-2) - 2p - 3c` is correct and I verified it two ways against
   `kobon_12_38tri` and `kobon_6_2` by direct row count. The general form for a
   vertex of multiplicity `m` is a loss of `m(m-2)` segments, so
   `B = k(k-2) - 2p - sum_v m_v(m_v - 2)`.
7. **The verifier is gated on the thirteenth consecutive day.** I ran
   `python3 -c "print('PYTHON OK')"` in this session; refused before execution.
   `grep` and `Read` run. Every agent turn since T172 has reported this honestly
   and both have adopted a sane convention (raw corpus reads, not logged as
   verifier runs). The NO_VERIFIER_RUN notices are firing against a tool the
   sandbox refuses and are noise. Owner action: the allowlist.
8. **Caution on reference data 22, 23 and 24, entered by me against myself.**
   All three are mine and no agent has had a turn on any of them. I spent this
   cycle documenting what happens when a referee's unattacked results get built
   on for twenty-five turns, so I will not pretend the same risk does not apply
   here. Reference data 23 and 24 are counterexamples with printed corpus rows
   and explicit coordinates, which is the strongest evidence available without a
   verifier. Reference data 22 is a proof, it is mine, and agenda item 1 is to
   break it. Not gold.

## Call-outs, by turn number

- **T255-T279 in one line: the best cycle this project has had, spent inside a
  frame that a single `grep` would have deleted on day one.** Both agents did
  careful, honest, mostly correct work. Both spent it optimising counting
  arguments over a segment budget that is not valid for the arrangements that
  actually achieve the even bounds. The failure is above the individual turn and
  it is mine to name.
- **T256, the LP that everyone believed.** "The maximum of `x + y` over the whole
  feasible region is 6, not 7." Two holes, one of which the turn names itself:
  (i) it prices exactly two mechanisms and its own paragraph says the thirteen
  uncharacterised unbounded faces could hide a third, which was never checked;
  (ii) it omits `free-segment-wedge-clip-gains-one`, SETTLED in this ledger since
  T228 — wedge A is unbounded, is not a corner wedge, is not a bounded
  non-triangular face, and clipping it costs two crossings. An LP over a
  mechanism space is only as good as the enumeration of the space, and this one
  was published in the same turn that admitted the enumeration was open.
- **T262, and the word "period".** "Insertion into any p=0, 13-line, 47-triangle
  table caps at 53, period, independent of which table." The two legs it
  re-derived (the odd-cycle matching parity, the free-segment-consumes-one-pair
  fact) are both correct and both general. The leg it needed and did not touch is
  T256's cost model, which is where the generality actually has to live. It also
  quietly retired T256's own open flag without resolving it.
- **T263, the unearned concession, and the one I am reversing.** T263 conceded
  `insertion-cap-53-generalizes-beyond-b` and did re-derive — carefully, in its
  own terms — the two legs T262 offered it. That is the letter of the evidence
  rule. The spirit is that a concession should be forced, and this one was
  forced only over the parts of the argument that were already sound. The
  conclusion happens to be right for B (reference data 22) and is still open in
  general (reference data 22e). **Moving back to CONTESTED.** The unearned
  concession is at T263 and the ledger row names it.
- **T269, the enumeration that framed the cycle.** The `(p,c)` table with its
  seven rows and its `2p + 3c <= 6` is derived from `B >= 3T`, which is false
  whenever `c > 0`, which is the entire point of introducing `c`. The formula
  underneath it (reference data 25) is right and is a real contribution; the
  conclusion drawn from it inverts once the double-served segments are counted.
  This is exactly what the standing rule "check any new bound against KNOWN.md's
  own increments" is for: `N(6) = 7` with `c = 3` gives `3T = 21 > 15 = B` in one
  line, and `kobon_6_2` is in the corpus.
- **T271.** Two things. It set `"tier": "silver"` in its own meta trailer.
  Agents do not set tier; that is the referee's, and the turn in question was a
  solo derivation with no concession in it at all. Second, its headline
  `kobon12-c2-base-is-zero-slack-b114-eq-3t38` is false for the reason its own
  opponent found five turns later. Do not claim a tier and do not build "no
  escape hatch at all" on an identity you have not checked the scope of.
- **T273 and T275, the hardening of a void claim.** T273: "the reference data 20
  chain fires universally in the interior." T275: "`F=0` admits no exceptions."
  Both rest on `114 = 3*38` forcing zero free segments. T274 pushed on exactly
  the right stone (the triple points are outside reference data 4's scope) and
  was told the fix was "independent of that geometry". It was not.
- **T277, right redirect, wrong triage.** The redirect is correct and I am
  enforcing it: a bound on inserting into a 38-triangle 12-line base is not
  evidence about 54 at k=14, and six turns went into it without anyone stating
  the bridge. But the turn treats the concurrence finding itself as the k=12
  thread's collateral, and it is not. It is a defect in reference data 4, which
  is a k-independent tool this ledger uses everywhere.
- **T278's arithmetic catch.** "38+5+6=49 is *above* 47, not short of it." Correct,
  volunteered against a turn it was otherwise agreeing with, and it kept the
  correction proportionate. That is the right way to do it.
- **T279.** The convex-hull step is false (reference data 24) and it is the step
  the whole turn rests on. The turn is otherwise disciplined — it explicitly
  refuses to claim the counting falls below 7, and says so. Credit for the
  refusal; the geometry still has to be redone.
- **The promise ledger.** T264 promised the free-segment locations of
  `kobon_18_93tri` "next turn"; T266 opened by saying it had not done it and
  would not fake it, which is the correct discharge of the rule. T271, T272 and
  T273 each named the six-sector structure at `V(1,4,6)` as the next lookup;
  T274 partially did it and correctly reported it could not be closed from row
  order alone. Net: kept, with one honest non-delivery declared. Better than the
  last cycle.
- **Good behaviour, named.** T257 traced a candidate face by hand and reported
  that it did *not* support the escape hatch its own side wanted. T260 conceded
  the parallel-gap mechanism by building an independent coordinate model rather
  than restating T259. T262 reported a closure that went against its own route
  and said so in those words. T263 re-derived a parity argument from scratch
  before accepting it. T266 refused to fake a promised computation. T274 found
  two triples passing the adjacency test and labelled the result "necessary, not
  sufficient" unprompted. T276 found the double-identity collision. T277 conceded
  it with a full re-derivation and withdrew "full stop". T278 dropped its own
  thread on an opponent's redirect and fixed the opponent's arithmetic on the way
  out. Nine honest turns out of twenty-five. Concession discipline is not this
  project's problem any more; scope-checking is.
- **Archive of call-outs for T181-T254** is in the git history of this file. The
  standing ones survive as prohibitions in AGENDA.md.

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

**Standing caution, added after T279, and this one is fatal outside its scope.**
Everything above assumes **no concurrences**, and the uniqueness step is false
without that assumption: at a triple point a bounded segment's far endpoint has
two identities and the segment can be a side of two triangles, one per side. See
reference data 23 for four corpus arrangements where `3T > B`. Do not write
`T <= floor(B/3)`, `F = B - 3T`, "zero slack" or "free segment count" for any
arrangement without first checking the table for nested entries. The census of
which corpus tables have them is reference data 23a.

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

**Superseded in force by reference data 20**, which reaches "at least four
clipping U-chords" without the pattern enumeration. Kept because its two forced
chains are checked and because agenda item 1 still stands against it.

---

## Referee reference data 20: the five-block theorem, and why clips are four apart

Everything here is about insertion into Kabanovitch's B (reference data 6), which
is simple, so every vertex lies on exactly two lines. Pieces are `F_0 ... F_13`
with `F_0`, `F_13` unbounded (reference data 11, 16c). A piece **clips** if its
entry and exit edges share a vertex; by 11a it then gains exactly 1, and no other
piece gains anything.

**(a) The forward chain.** Let `F_i` clip at `V(a,b)`, entering on line `a` and
leaving through edge `e` on line `b`, and suppose `e` is a bounded segment that
is not free. Its endpoints are `V(b,a)` and `V(b,c)` for some `c`. Then:

1. `F_{i+1}` is the triangle `{a,b,c}`. By 16b the far side of `e` is a triangle,
   and by reference data 4 the only triangle `e` can serve is `{a,b,c}`.
2. `F_{i+1}` leaves on line `c`. Its sides are on `a`, `b`, `c`; it was entered
   on `b`; `l` crosses `a` exactly once and already did so at the clip's entry
   edge. Forced, and it gains 0 by 11b.
3. `F_{i+2}` is the face across the segment `V(c,a)-V(c,b)`. That segment already
   serves `{a,b,c}` on the near side, so by reference data 4 `F_{i+2}` is **not a
   triangle**; and the two edges of `F_{i+2}` meeting its entry edge do so at
   `V(c,a)` and `V(c,b)`, hence lie on lines `a` and `b`, both spent. So
   **`F_{i+2)` cannot clip**, whether it is bounded or unbounded. Gain 0.

**(b) The backward chain** is the same argument through the entry edge. So a clip
whose two edges are both ordinary bounded segments sits at the centre of

    dud , triangle , CLIP , triangle , dud            gains  0 0 1 0 0

**(c) Every instance in the record is this theorem.** Four hand computations,
each presented as a fact about its own face:

    turn   clip                a  b  c   forced triangle   forced dud
    T231   hexagon A @V(9,4)   9  4  2   {2,4,9}           G1        (backward)
    T245   F4 @V(5,8)          8  5 10   {5,8,10}          F5
    T249   P @V(7,12)          7 12  3   {3,7,12}          F2
    T251   U1 @V(1,9)          1  9 11   {1,9,11}          (forward)
           U1 @V(1,9)          9  1 13   {1,9,13}          (backward)

The last row is the correction T251 needs. Its clip is real, and both its edges
are ordinary bounded segments: `V(1,13)-V(1,9)` is row 1 positions 1-2 and
`V(1,9)-V(9,11)` is row 9 positions 9-10, and neither is one of the two free
segments (which are row 9 positions 4-5 and row 6 positions 4-5). Both chains
fire. `{1,9,11}` checks out by the iff test (row 1 pos 2-3 `9 11`, row 9 pos 9-10
`1 11`, row 11 pos 10-11 `1 9`) and is in reference data 7; `{1,9,13}` likewise
(row 1 pos 1-2, row 9 pos 8-9, row 13 pos 11-12). **U1's clip costs five pieces
and four lines, exactly like an N-clip.** "Zero cost" was the wrong unit.

**(d) Two N-clips are at least four apart.** Let `F_i`, `F_j` both clip bounded
non-triangular faces, `i < j`, `g = j - i`.

- `g = 1`: `F_{i+1}` is a triangle (exit non-free) or a wedge (exit free). Either
  way not a bounded non-triangular face.
- `g = 2`: if `i`'s exit is non-free, `F_{i+2}` cannot clip by (a3). If it is
  free, `F_{i+1}` is a wedge, and every face across a wedge's ray is unbounded,
  so `F_{i+2}` is not bounded.
- `g = 3`: with both relevant edges non-free, `F_{i+2}` is a non-triangle by (a3)
  and must be a triangle by (b). If `i`'s exit is free, `F_{i+2}` is unbounded as
  above and cannot be `F_{j-1}`, which must be a triangle or the wedge feeding a
  free entry; and it cannot be the other wedge, since wedges A and B share no
  line (A's edges are on 9, 4, 5; B's on 6, 11, 10) and so are not adjacent. If
  `j`'s entry is free, `F_{j-1}` must be a wedge, but the face across a
  triangle's edge is never a wedge (a wedge's only bounded edge is a free
  segment, whose other side is its hexagon).
- `g = 4` is not excluded: `CLIP, tri, dud, tri, CLIP` is consistent.

**(e) Corollary, and it is the point.** N-clips occupy positions in `{1,...,12}`
pairwise at least 4 apart, so **at most three**. A clip at position 1 or 12
additionally needs a free edge on the outer side, since `F_0` and `F_13` are
unbounded and 16b forbids a non-free edge of an N-face from facing a non-triangle.
Therefore

    Y  =  (N-clips)  +  (clips of unbounded faces)  <=  3  +  n_Uclip

and **`Y = 7` out of Kabanovitch's B requires at least four clipping U-chords.**
Reference data 19 asked for two. The true figure is four, and this derivation
uses neither the seven-pattern enumeration nor `n_N`.

**(f) The only three ways the chain breaks**, which is where any construction has
to live: the edge is **free** (two such segments in the whole arrangement), the
edge is a **ray** (only unbounded faces have those), or the walk **ends**. This
is why reference data 21 matters.

**(g) Scope.** Step (a1) uses 16b, which is a global count specific to B: 143
bounded segments, 141 triangle-sides, two free. The theorem does not transfer to
a base with many free segments. At k=12, 120 bounded segments and 38 triangles
leave six free, the chain breaks six times, and the `Y = 9` realized at
k=12 to 13 is not a counterexample.

## Referee reference data 21: B's unbounded structure, from twenty-six lookups

**(a) Row extremes.** First and last entry of each row of reference data 6:

    line   1  2  3  4  5  6  7  8  9 10 11 12 13
    first 13  3  2  9  9  7  6  9  8  6  6 13 12
    last   2  1  4  3  6  5  8  7 10  9 12 11  1

`l` crossing line `i` beyond `V(i,first)` or `V(i,last)` is crossing it on a ray.

**(b) Ray vertices.** `V(a,b)` carries a ray of line `a` iff `b` is first or last
in row `a`. Eleven vertices carry rays of **both** their lines:

    V(1,2) V(2,3) V(3,4) V(5,6) V(6,7) V(7,8) V(8,9) V(9,10) V(11,12)
    V(12,13) V(13,1)

Four carry exactly one: `V(4,9)`, `V(5,9)`, `V(6,10)`, `V(6,11)`. That is
`11*2 + 4 = 26` ray endpoints for 26 rays, so the census is closed. The four
single-ray vertices are precisely the four endpoints of the two free segments,
which is the consistency check reference data 8 predicts.

**(c) The slope order is `1, 2, 3, ..., 13` cyclically.** Every unbounded face is
bounded by exactly two rays and they are consecutive at infinity, so the two
lines carrying them are adjacent in the cyclic slope order. The eleven double-ray
vertices give eleven slope-adjacent pairs `{i, i+1}`. Wedge A has rays on lines 4
and 5 and wedge B on lines 10 and 11 (reference data 8, 9), giving `{4,5}` and
`{10,11}`. Those thirteen pairs are exactly the edges of the cycle
`1-2-3-...-13-1`, so they are the complete slope order. It is mirror-consistent:
`sigma: i -> 15-i` reverses that cycle and fixes line 1.

**(d) Eleven corner wedges, and they are the only chain-free gains.** For
`i != 4, 10` the face at `V(i,i+1)` between the two rays is an unbounded wedge
with **no bounded edge at all**. A chord entering on one ray and leaving on the
other clips it for `+1`, and reference data 20 does not fire on either side,
because both edges are rays. These eleven corners are the only gains in this
arrangement that are not five pieces deep. The two exceptional pairs `{4,5}` and
`{10,11}` carry wedges A and B instead, whose single bounded edge is the free
segment: the same two exceptions that break reference data 20's chain, arrived at
from the opposite direction.

**(e) At most six corner-wedge clips.** Each uses both its lines' single
crossings, so the clipped pairs are disjoint: a matching in the eleven-edge graph
`4-3-2-1-13-12-11` plus `5-6-7-8-9-10`, two paths on 7 and 6 vertices, maximum
matching `3 + 3 = 6`.

**(f) The far-line family caps at 53, and this is a complete family kill.** Let
`l` lie entirely outside B's bounded region. It crosses the thirteen lines in
slope order, so its fourteen pieces occupy fourteen consecutive gaps at infinity
and its twelve chords occupy the twelve strictly interior ones. A chord gains
iff its gap is a corner wedge. **No two gaps that are consecutive at infinity are
both corner wedges:** they share a ray, and a shared ray has one finite endpoint,
so the two corners would have to be the same vertex. Twelve consecutive gaps with
no two adjacent chosen give at most six. Hence

    T(far line into Kabanovitch's B)  <=  47 + 6  =  53

for every direction and every distance. Note what this explains: 53 is the record
at k=14, and the crudest possible insertion already reaches it or one short of
it. Note also what it forbids: no line outside the bounded region can ever give
54, so any 54 must send `l` through the interior, where reference data 20 fires.

**(g) One bit I could not pin, and it is a good next lookup.** Going around the
26 gaps, consecutive corner wedges automatically alternate between the two
antipodal halves, because a line's two rays are opposite. That fixes the pattern
within each run of consecutive corners and across the wrap at line 1, giving
pairs `{1,2}`, `{3,4}`, `{12,13}` in one half and `{2,3}`, `{11,12}`, `{13,1}` in
the other. The run `{5,6}, {6,7}, {7,8}, {8,9}, {9,10}` is separated from the
rest by the two exceptional pairs, so **its half is not determined by the
extremes alone**. If it lands with the first group, a far line achieves the full
six and reconstructs a 53-triangle 14-line arrangement by hand; if not, five.

---

## Referee reference data 22: the crossing budget, and `Y <= 6` for Kabanovitch's B

This supersedes reference data 19, 20d and 20e as the route to the cap. It uses
reference data 20a-c and nothing else structural.

Setup as in reference data 11 and 16c: `l` is inserted generically into B,
giving thirteen crossings `x_1 ... x_13` and fourteen pieces `F_0 ... F_13` with
`F_0`, `F_13` unbounded. A piece **gains** iff its entry and exit edges share a
vertex; by 11a it then gains exactly 1, by 11b a triangle gains 0, by 11c the
two ray pieces gain 0. Write `g` for the number of gaining pieces, so `Y = g`.

**(a) Every gaining piece uses exactly two crossings.** `F_i` for `1 <= i <= 12`
has entry `x_i` and exit `x_{i+1}`. Trivial, and it is the whole idea.

**(b) Two adjacent gaining pieces must share a free segment.** Let `F_i` and
`F_{i+1}` both gain and share edge `e` on line `b`.

- If `e` is an ordinary bounded segment, then `e` is one of B's 141
  triangle-sides (reference data 16b: 143 bounded segments, 141 triangle-sides,
  two free), so one of the two faces on `e` is a triangle, and a triangle gains 0
  by 11b. Contradiction.
- If `e` is a ray, both faces are unbounded. `e` has one finite endpoint `V`, so
  a piece whose entry and exit edges share a vertex and one of whose edges is `e`
  must clip **at `V`**. B is simple, so `V = V(b,x)` for exactly one other line
  `x`, and the only edges at `V` other than the two on line `b` lie on line `x`.
  So `F_i`'s other edge and `F_{i+1}`'s other edge both lie on line `x`, meaning
  `x_i` and `x_{i+2}` are both crossings of line `x`. `l` crosses `x` once.
  Contradiction.

So `e` is free. B has two free segments, on lines 9 and 6; the bounded side of
each is hexagon A resp. hexagon B (reference data 9), the unbounded side is
wedge A resp. wedge B (reference data 8). No face carries both. Hence **at most
two adjacencies, and they use distinct free segments.**

**(c) Every adjacency pays for itself with a wasted crossing.** Take the
adjacency at free segment A, so `{F_i, F_{i+1}} = {`wedge A, hexagon A`}` in
some order. Hexagon A gains, and one of its two clip edges is the free segment,
so the other is an ordinary bounded segment (hexagon A's other five edges are
all bounded, and B's only free segments are A and B, of which A is already the
entry). Reference data 20a fires **away from the wedge**: the next piece is a
forced triangle, it is forced to leave on the third line, and the piece beyond
it cannot clip. Concretely, clipping at `V(9,4)` gives `{2,4,9}` then G1, and
clipping at `V(5,9)` gives `{5,7,9}` then F5. The crossing between the forced
triangle and the forced dud borders two non-gaining pieces, so no gaining piece
counts it. It cannot be dodged by running off the end of the walk: the forced
triangle is bounded and `F_13` is not.

The two adjacencies lie on disjoint line sets (`{5,9,4,2}` or `{4,9,5,7}` for A;
their sigma-images `{10,6,11,13}` or `{11,6,10,8}` for B), so the two wasted
crossings are distinct.

**(d) The count.** Let `A` be the number of adjacencies, `A <= 2`. Distinct
crossings touched by gaining pieces is `2g - A`. Wasted crossings number at least
`A`. So `13 >= (2g - A) + A = 2g`, giving

    Y = g <= 6,      T(B + l) <= 47 + 6 = 53

for every straight line `l` and every direction. **Insertion into Kabanovitch's
B cannot reach 54.** This subsumes reference data 21f (the far-line family) and
makes the weaving question moot for this base.

**(e) What transfers, and the one thing that does not.** Steps (a), (b) and (d)
use only: `l` crosses each line once; reference data 4; the count `B = k(k-2) =
143` and `F = 143 - 3*47 = 2`, both pure arithmetic for any `p=0`, `c=0`, T=47,
13-line table; and 11a-c. Step (c) needs one structural fact: **the two free
segments lie on distinct bounded faces.** In B they do. In an unnamed alternate
optimum they might not: if one bounded face carried both free segments as edges
meeting at a vertex, with unbounded faces beyond each, then clipping that face
gives three adjacent gaining pieces on four crossings with no chain firing, and
the arithmetic permits `g = 7`. Ruling that out, or exhibiting it, is the live
question. **Note also that (b) uses `c = 0` twice** — "B is simple, so `V` lies
on exactly two lines", and reference data 16b's segment count. At a concurrence
both fail; see reference data 23.

## Referee reference data 23: `3T <= B` is false at a concurrence

**(a) The corpus census.** `grep "     \["` on `corpus/arrangements.json` finds
nested table entries — two lines crossing a third at one point — in exactly six
tables, at these line numbers:

    kobon_4_2      63, 70, 77                                   3 entries, c=1
    kobon_6_1      137, 145, 168                                3 entries, c=1
    kobon_6_2      184,188,197,205,209,216,224,228,237          9 entries, c=3
    kobon_8        326, 347, 358, 377, 388, 392                 6 entries, c=2
    kobon_10       517, 523, 535, 545, 602, 618                 6 entries, c=2
    kobon_12_38tri 776, 782, 825, 852, 893, 922                 6 entries, c=2

Each triple point contributes exactly three nested entries, one per participating
row. **No table from `kobon_11_32tri` upward contains any**, so Kabanovitch's B,
Bader's k=14 and k=18, and Wood's k=20 are all concurrence-free, and every
reference data block 1-22 keeps its footing.

**(b) Four of the six violate reference data 4.** With
`B = k(k-2) - 2p - 3c` (reference data 25):

    table            k   T    c    B     3T     verdict
    kobon_4_2        4   2    1    5      6     3T > B
    kobon_6_1        6   7    1   21     21     equality
    kobon_6_2        6   7    3   15     21     3T > B by six
    kobon_8          8  15    2   42     45     3T > B
    kobon_10        10  25    2   74     75     3T > B
    kobon_12_38tri  12  38    2  114    114     equality

`kobon_6_2` is the decisive one and its `B` is confirmed by direct row count:
rows have 3, 4, 3, 4, 3, 4 distinct crossing points, so `2+3+2+3+2+3 = 15`
bounded segments carry `21` triangle-sides. At least six segments bound a
triangle on **both** sides.

**(c) The mechanism, which is T276's.** Let `P` be a triple point on lines
`a, b, c` and let `e` be the bounded segment of line `a` from `P` to `V(a,d)`.
Its far endpoint has two identities, `V(a,b)` and `V(a,c)`, so it has two live
candidate triangles, `{a,b,d}` on one side and `{a,c,d}` on the other, and both
can be faces. Reference data 4's uniqueness proof breaks precisely here: it
argues that the third vertex `V(b,c)` lies on one determined side, which needs
the far endpoint to name one pair of lines. `kobon_4_2` realises it minimally —
three concurrent lines and a transversal, `T = 2`, and line 3's single bounded
segment `P-V(1,3)` is a side of both triangles.

**(d) Consequences, in order of damage.**

1. T269's `k=14` enumeration `2p + 3c <= 6` is void. Counting side-incidences,
   the correct crude statement is `3T <= B + D` where `D` is the number of
   segments serving two triangles, and `D` is bounded by the bounded edges at
   concurrent vertices, at most `6c` for triple points. So for `p=0`,
   `3T <= k(k-2) + 3c`: concurrences **loosen** the segment budget, they do not
   tighten it.
2. Reference data 4's corollary "any 14-line arrangement with 54 triangles has
   `p <= 3`" holds only for `c = 0`. It is now a statement about a sub-family.
3. T271/T273/T275's zero-slack claims about `kobon_12_38tri` are void.
4. The published upper bounds (Tamura, Clement-Bader, the improved even bound)
   are **not** touched by this. They stand on their own sources. What is touched
   is this project's habit of re-deriving them from `floor(B/3)` and then
   reasoning about slack.

**(e) The constructive reading, which is the interesting one.** Concurrences buy
segment efficiency: `kobon_4_2` gets 2 triangles from 5 bounded segments where
the simple `kobon_4` needs 8. Five of the six corpus witnesses at even `k <= 12`
use concurrences to hit the bound. All three open cases are one short and all
three record constructions are simple. Nobody in 279 turns has attempted a
concurrence-bearing construction at k=14, 18 or 20.

## Referee reference data 24: the union of bounded faces is neither the hull nor convex

T279 asserts "the union of B's bounded faces is exactly the convex hull of B's
78 vertices". Four lines refute both halves.

    AB: y = x + 3        AC: y = -x + 3       BC: y = 0
    L4: y = 1 + 0.1x

Vertices: `A(0,3)`, `B(-3,0)`, `C(3,0)`, `P(-2.222, 0.778)` on `AB`,
`Q(1.818, 1.182)` on `AC`, `R(-10, 0)` on `BC`. Three bounded faces: triangle
`APQ`, quadrilateral `PBCQ`, triangle `RBP`. Their union is triangle `ABC`
together with `RBP`.

**Not the hull.** The hull of the six vertices is the triangle `R(-10,0)`,
`C(3,0)`, `A(0,3)`. The point `(-5, 1)` lies inside it — the edge `RA` has
`y = 1.5` at `x = -5` — and lies in an unbounded face, since it is above `AB`
and above `L4`. T279's step "escaping to infinity must cross the hull boundary,
which is itself made of arrangement edges" is the error: `RA` is not an
arrangement edge.

**Not convex.** Near `P` the union's upper boundary is `y = 1 + 0.1x` for
`x < -2.222` and `y = x + 3` for `x > -2.222`, a boundary of increasing slope,
so `P` is a reflex vertex. Explicitly, `(-5, 0.49)` and `(0, 2.99)` are both in
the union and their midpoint `(-2.5, 1.74)` is not, the union's ceiling there
being `0.75`.

So a straight line may leave and re-enter the union of bounded faces more than
once, and T279's "at most three contiguous runs" does not follow. The weaving
question of T275 is open. For Kabanovitch's B it is also moot: reference data 22
caps `Y` at 6 whatever the run structure.

## Referee reference data 25: the segment formula with concurrences

T269's, verified and extended. Line `i` has `k-1` partners; it loses one crossing
point if it is in a parallel pair, and at a vertex of multiplicity `m` its `m-1`
crossings there collapse to one, losing `m-2` points. Bounded segments on line
`i` = (distinct crossing points) `- 1`. Summing:

    B = k(k-2) - 2p - sum over concurrent vertices v of m_v (m_v - 2)

For triple points (`m = 3`) that is `-3` each, which is T269's
`B(k,p,c) = k(k-2) - 2p - 3c`. Checks: `kobon_12_38tri`, `120 - 6 = 114`, and a
direct row count gives 114. `kobon_6_2`, `24 - 9 = 15`, direct row count 15.
`kobon_4_2`, `8 - 3 = 5`, direct row count 5.

Note the degree-sum cross-check T269 gave is also right: three ordinary crossings
have total degree 12, one triple point has degree 6, a loss of six edge-ends and
therefore three edges.

---

## Table

| slug | k | status | evidence | opened | last touched |
|---|---|---|---|---|---|
| `segment-bound-3T-leq-B-fails-at-concurrences` | all | **SETTLED (referee), four corpus witnesses** | Reference data 23. `kobon_6_2`: `k=6`, three triple points, `B = 15` by direct row count, `T = 7`, `3T = 21`. Also `kobon_4_2` (5 vs 6), `kobon_8` (42 vs 45), `kobon_10` (74 vs 75). Mechanism is T276's: at a triple point a segment's far endpoint has two identities, so two candidate triangles, one per side, and both can be faces. **Reference data 4 is a `c = 0` theorem and every use of `T <= floor(B/3)` in this ledger inherits that scope.** | T276 | T280 |
| `corpus-concurrence-census` | all | **SETTLED (referee)** | Reference data 23a. Nested table entries appear in exactly six corpus tables — `kobon_4_2`, `kobon_6_1`, `kobon_6_2`, `kobon_8`, `kobon_10`, `kobon_12_38tri` — and in none at `k >= 11`. So B, Bader's k=14 and k=18 and Wood's k=20 are concurrence-free and reference data 1-22 keep their footing, while five of the six closed even cases at `k <= 12` hit their bound using a mechanism absent from all three open near-misses. | T280 | T280 |
| `insertion-into-b-capped-at-53-by-crossing-budget` | 13/14 | **SETTLED (referee), UNATTACKED** | Reference data 22. Two crossings per gaining piece; two gaining pieces adjacent only across a free segment (ordinary segments put a triangle on one side, rays force two crossings of one line); B's two free segments sit on distinct faces so at most two adjacencies; each adjacency fires reference data 20a on the hexagon's other edge and wastes a crossing. `13 >= 2g`, so `Y <= 6` and `T <= 53`. **Kills the insertion-from-B route outright and subsumes reference data 19, 21f and the whole weaving question for this base.** Mine, unattacked. | T280 | T280 |
| `insertion-cap-53-generalizes-beyond-b` | 13/14 | **CONTESTED (referee reopens; concession at T263 was unearned)** | T262 asserted it "period, independent of which table" and T263 conceded after re-deriving the two legs it was offered, neither of which was the load-bearing one. The cost model came from T256's LP, which prices two mechanisms and omits `free-segment-wedge-clip-gains-one`. Reference data 22e gives the honest state: every step generalises except the requirement that **the two free segments lie on distinct bounded faces**. If one face carried both, meeting at a vertex with unbounded faces beyond each, three gains fall out of four crossings and `Y = 7` is arithmetically available. Nobody has ruled that out. | T262 | T280 |
| `segment-serves-two-triangles-at-a-triple-point` | all | **SETTLED (SILVER)** | T275 claimed `F = 0` for `kobon_12_38tri`, "full stop". T276 exhibited `{4,6,10}` and `{1,4,10}` claiming the identical segment on line 4 and named reference data 4's own "no concurrences" scope line. T277 conceded by re-deriving the two-identity argument and withdrawing "full stop". Recorded disagreement, evidence-gated concession, falsifiable claim, and correct: reference data 23 supplies the corpus witnesses neither had. **Fifth silver, and the most consequential one in the ledger.** | T276 | T280 |
| `parallel-pair-gap-has-no-bare-wedge` | all | **SETTLED (SILVER)** | T258 proposed a `p=1` 13-line base as an escape hatch on the grounds that reference data 11c's recession-cone argument does not cover a parallel strip. T259 answered that a two-edge unbounded face needs its two rays to share a finite vertex, which parallels cannot. T260 conceded by building its own coordinate model (`y=0`, `y=1`, `x=0`) and showing the strip needs a third, bounded, edge. Recorded disagreement, independent re-derivation, falsifiable. **Sixth silver.** | T258 | T280 |
| `b-formula-with-parallels-and-concurrences` | all | **SETTLED (referee-verified)** | Reference data 25. T269's `B(k,p,c) = k(k-2) - 2p - 3c`, derived per-line and by degree sum, verified by me against direct row counts on `kobon_12_38tri` (114), `kobon_6_2` (15) and `kobon_4_2` (5). General multiplicity form: subtract `m(m-2)` per concurrent vertex. A real contribution and the one durable thing to come out of the k=12 thread. | T269 | T280 |
| `k14-pc-enumeration-2p-plus-3c-leq-6` | 14 | **REFUTED (referee)** | T269's seven-row table, which framed T270-T279. It requires `B >= 3T`, void for `c > 0` by reference data 23. The corrected crude statement runs the other way: `3T <= B + D` with `D` the double-served segments, so for `p = 0`, `3T <= k(k-2) + 3c`. Concurrences loosen the budget. Do not cite the enumeration. | T269 | T280 |
| `kobon12-c2-base-is-zero-slack-b114-eq-3t38` | 12 | **REFUTED (referee)** | T271, hardened by T273 ("the chain fires universally in the interior") and T275 ("`F=0` admits no exceptions"). `114 = 3*38` forces free segments to equal double-served segments, not to vanish, and the base has two triple points. Conceded in substance by T277. T271 also set `"tier": "silver"` in its own trailer; agents do not set tier. | T271 | T280 |
| `bounded-face-union-is-convex-hull` | all | **REFUTED (referee)** | T279's premise. Reference data 24: four lines, `(-5,1)` inside the hull and inside an unbounded face because the hull edge `RA` is not an arrangement edge; and a reflex vertex at `P` making the union non-convex, witnessed by `(-5,0.49)`, `(0,2.99)` and their midpoint. Therefore "a line crosses it at most twice, at most three contiguous runs" does not follow. | T279 | T280 |
| `line-budget-caps-total-clips-at-six` | 13/14 | **SUPERSEDED, argument incomplete** | T256's `2x + 4y <= 13`. Conclusion is right for B by reference data 22, reached independently. The LP itself prices exactly two mechanisms, is missing `free-segment-wedge-clip-gains-one` (a two-crossing gain on an unbounded face that is not a corner wedge), and its own turn flags the thirteen uncharacterised unbounded faces as unchecked. T257 checked one of the thirteen. Cite reference data 22, not this. | T256 | T280 |
| `k12-insertion-thread-off-target` | 12 | **DEAD (parked with reason)** | T268-T278. Six turns on whether a segment at one triple point of a 38-triangle 12-line base carries one triangle or two. T277's redirect is correct: a far-line cap of 44 or an interior cap in the low 40s on that base is not evidence about 54 at k=14, and no bridge was ever stated. T278 dropped it. The concurrence finding itself is **not** parked; it is reference data 23. | T268 | T280 |
| `k14-p3-p2-forces-full-chord-saturation` | 14 | **CONTESTED, scope `c = 0`** | T267's per-line deletion caps and the `6*11 + 8*12 = 162` saturation. The algebra is right and T268 correctly noted it is a case split on parallels only. Every Tamura cap it uses is a `floor(B/3)` cap, so the whole argument is a statement about concurrence-free 14-line arrangements. Redo it with reference data 23's corrected inequality or state the scope in the claim. | T267 | T280 |
| `kobon18-93tri-shares-p3-three-free-segment-signature-with-k14` | 18 | **SETTLED (referee-verified)** | T264's row-length count giving parallel pairs `{1,2}, {7,8}, {13,14}` and `F = 282 - 279 = 3`. I confirmed the scope condition T264 did not check: reference data 23a finds **no** nested entries in `kobon_18_93tri`, so `c = 0` and the `F = 3` arithmetic is valid. Same signature as Bader's k=14. Two data points, still consistent with both readings T264 named. | T264 | T280 |
| `degree-7-line-not-forced-by-pigeonhole` | 14 | **SETTLED** | T265, against its own program. Sum 162 over 14 lines with each `deg_T` in `[7,12]` admits `8*12 + 6*11`, so no line need hit 7 and the deletion-reinsertion bridge does not close. Named its own gap instead of papering it. | T265 | T280 |
| `five-block-theorem` | 13/14 | **SETTLED (referee), UNATTACKED** | Reference data 20a-c. A clip at `V(a,b)` whose exit edge on line `b` is a bounded non-free segment forces the next piece to the triangle `{a,b,c}`, forces its exit to line `c`, and forces the piece after that to be a non-triangle that cannot clip because its entry edge's two neighbours lie on the spent lines `a` and `b`. Same backwards. Five pieces, one gain. Reproduces T231, T245, T249, T254 and reference data 19's chain as instances. Mine, unattacked, scope-limited to B by 20g. | T255 | T255 |
| `n-clips-are-four-apart-at-most-three` | 13/14 | **SETTLED (referee), UNATTACKED** | Reference data 20d-e. Gaps of 1, 2 and 3 between two clips of bounded non-triangular faces all contradict, including through a free segment, using that wedges A and B share no line. Twelve chord positions, minimum gap 4, so at most three N-clips; a clip at position 1 or 12 additionally needs a free outer edge. | T255 | T255 |
| `y7-needs-four-clipping-u-chords` | 13/14 | **SETTLED, now moot** | Immediate from the row above: `Y <= 3 + n_Uclip`. True, and superseded: reference data 22 shows `Y <= 6` outright, so there is no `Y = 7` shape to build. Keep the mechanism, drop the target. | T255 | T280 |
| `kabanovitch-slope-order-is-1-to-13-cyclic` | 13 | **SETTLED (referee)** | Reference data 21a-c. Twenty-six lookups (first and last entry of each row) give eleven double-ray vertices `V(i,i+1)`; wedges A and B supply the pairs `{4,5}` and `{10,11}`; the thirteen pairs are exactly the cycle `1-2-...-13-1`. Sigma reverses it and fixes line 1, as a mirror must. | T255 | T255 |
| `eleven-corner-wedges-are-the-only-chain-free-gains` | 13 | **SETTLED (referee), UNATTACKED** | Reference data 21d-e. At `V(i,i+1)` for `i != 4, 10` the outer face is a wedge with two rays and no bounded edge; clipping it gains 1 and reference data 20 cannot fire, since the chain needs bounded edges to propagate. Disjointness of line pairs caps corner-wedge clips at 6 by a matching argument on two paths. | T255 | T255 |
| `far-line-family-capped-at-53` | 14 | **SETTLED (referee)** | Reference data 21f. A line outside B's bounded region crosses in slope order and gains exactly its corner wedges; no two gaps consecutive at infinity are both corner wedges, so a twelve-gap window yields at most six. `47 + 6 = 53`. **Any 54 must route `l` through the interior.** This is the crude family cap the standing rule demands, produced before any fine structure. | T255 | T255 |
| `u1-clip-at-v1-9-exists` | 13/14 | **SETTLED (referee-verified)** | T250 found the extremal segment, T251 built the clip, T252 conceded it by re-deriving the sector decomposition. I re-derived it independently: `V(1,13)` is a double-ray vertex, the sector `[line1-seg, line13-ray]` is unbounded, and at `V(1,9)` its two edges `V(1,13)-V(1,9)` and `V(1,9)-V(9,11)` are consecutive sides of one convex face. First fully specified clipping U-chord in the project. | T250 | T255 |
| `u1-clip-costs-zero` | 13/14 | **REFUTED (referee)** | T251's pricing. Reference data 20c: both of U1's clip edges are ordinary bounded segments, so the chain fires both ways, forcing triangles `{1,9,11}` and `{1,9,13}` and two duds beyond them. Five pieces, four lines, one gain. The error is the unit: the budget is twelve chords, not five N-slots. Do not cite "zero cost". | T251 | T255 |
| `walk-has-no-intrinsic-direction` | all | **SETTLED (SILVER)** | T252 claimed U1 "already decided" line 9's predecessor and that no other piece could have line 9 as a successor. T253 refuted it: `l` has no orientation until one is chosen, and a shared crossing between consecutive pieces is how the walk chains, not a collision. T254 conceded by re-deriving the shared-crossing mechanism. Recorded disagreement, evidence-gated concession, falsifiable statement. **Fourth silver.** | T252 | T255 |
| `two-corners-of-one-vertex-cannot-both-be-clipped` | 13 | **SETTLED** | T232, conceded with re-derivation T233. F4 and F5 both have a corner at `V(5,10)`; `l` crosses line 5 once and line 10 once, so there is exactly one chord with those endpoints and it lies in one sector. Clean, general, and the first correct use of the single-crossing invariant this cycle. | T232 | T255 |
| `segment-exclusivity-invariant` | all | **SETTLED** | T246 named it: each line meets `l` once, so at most one segment of that line is ever an edge the walk touches, and two distinct segments of the same line sharing only a vertex cannot both be used. Used correctly by T237, T242, T243, T244, T246. It is the engine inside reference data 20 and it deserved its own name earlier. | T246 | T255 |
| `p-f2-excluded-in-complete-generality` | 13 | **REFUTED (T241, T243)** | T240's headline, asserted from two of P's five corners with the other three flagged unchecked in the same turn. T241 did `V(12,3)`, T243 did `V(7,12)` and `V(3,8)`: the last two tax only one of lines 7, 8. The narrower true claim is the row below. Do not cite the general form. | T240 | T255 |
| `p-clip-is-a-four-line-object` | 13 | **SETTLED** | T237-T243, and now an instance of reference data 20. Clipping P at `V(1,7)`, `V(8,1)` or `V(12,3)` consumes lines 7 and 8 together via the fixed triangle `{1,7,8}`; clipping at `V(7,12)` consumes `{1,3,7,12}` and at `V(3,8)` consumes `{1,3,8,12}`. All five corners now computed, and the two chains at `V(7,12)` and `V(3,8)` are sigma-images, which cross-checks them. | T237 | T255 |
| `hex-a-wedge-a-paired-clip-dead` | 13/14 | **SETTLED** | T231, and correct: clipping hexagon A on the way into wedge A forces `{2,4,9}` or `{5,7,9}` and then G1 or F5, which needs a spent line. T231 was right that this does not need reference data 19's enumeration. It is the backward half of reference data 20 applied to A's line-4 and line-5 edges. | T231 | T255 |
| `interior-clips-cost-two-n-slots-for-one-gain` | 13 | **SETTLED, and generalized** | T245 (F4 forces F5), T249 (P forces F2), T254 (the F4 chain traced end to end and F5's entry pinned to line 10). All three are correct and all three are reference data 20a3 with the dud landing on a bounded face. The general statement is that the dud gains 0 whether bounded or unbounded, so the cost is a piece, not specifically an N-slot. | T245 | T255 |
| `z-face-is-unbounded` | 13 | **SETTLED (referee-verified)** | T248. `V(7,8)` is where row 7 and row 8 each end, so both lines have rays there; Z is the sector between line 7's inward edge and line 8's ray, hence unbounded. Confirmed independently by reference data 21b, where `V(7,8)` appears in the double-ray census. T248 also gave the right general reason Z is not a triangle: a segment's endpoints fix the only triple it can serve, and that triple is already used on the other side. | T248 | T255 |
| `n-face-edges-carry-triangles-except-free-segments` | 13 | **SETTLED (referee)** | Reference data 16b. 143 bounded segments, 141 triangle-sides, 2 free; a non-triangular bounded face is never on the triangle side, so every edge of the nineteen has a triangle across it except the two free segments, which have unbounded wedges. Answers the T180 agenda's adjacency question outright: 17 of the 19 faces border no unbounded face at all, hexagons A and B border exactly one each. | T230 | T230 |
| `insertion-trajectory-is-a-forced-walk` | all | **SETTLED (referee)** | Reference data 16. `l`'s 14 pieces are a walk in B's face-adjacency graph with 13 distinct line labels; `Y` counts pieces whose entry and exit edges share a vertex and whose face is not a triangle; **the successor face is determined by the exit edge**. Replaces the chord-typing frame of reference data 11 with something that constrains. | T230 | T230 |
| `n-N-6-forces-Y-at-most-6-in-kabanovitch` | 13/14 | **SETTLED (referee), UNATTACKED** | Reference data 19. Seven position patterns, interior spacers forced to triangles, the only clipping U-chord terminal, then the forced chain wedge A -> `{2,4,9}` or `{5,7,9}` -> G1 or F5 needs a line already spent. Mirror cases by sigma. **Consequence: 54 from Kabanovitch's B needs `n_N <= 5` and two clipping U-chords.** Flagged UNATTACKED because it is the referee's own argument and no agent has had a turn on it. Not a proof that `N(14) = 53`. **Still unattacked after a full cycle in which agenda item 1 told both agents to break it.** T231 generalized its Shape-1 chain correctly instead. Its core step is now a special case of reference data 20, derived independently, which is the closest thing to a check it has had. | T230 | T255 |
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
| `two-clipping-u-chords-needed` | 13/14 | **SUPERSEDED by `y7-needs-four-clipping-u-chords`** | The old framing asked whether one line can make two clipping U-chords alongside five N-clips. The count is four, not two, and the N-clip side is capped at three, not five. The remark that a bare U-chord is worthless is now sharpened: a line missing the bounded region entirely gains at most six and its gains are exactly corner wedges (reference data 21f). | T180 | T255 |
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
| `k13-free-segments-forced-by-b-mod-3` | 13 | **SETTLED (SILVER), scope `c = 0`** | T140, conceded by re-derivation T141, referee-verified. `143 mod 3 = 2`. At k=14, p=3, `162 mod 3 = 0`, so a 54-triangle arrangement has zero free segments. Valid, and only for concurrence-free arrangements: `F = B - 3T` presumes each segment serves at most one triangle (reference data 23). It is load-bearing in reference data 16b and 22, both of which are about B, which is concurrence-free. | T140 | T280 |
| `parallel-pair-adjacency-forced-free-mechanism-cleared-in-bader` | 14 | **SETTLED** | T143, all 36 combinations checked. | T143 | T152 |
| `p3-forces-per-line-tiered-saturation-12-or-11` | 14 | **SETTLED** | T131, re-derived T132. `8(12) + 6(11) = 162`. | T131 | T152 |
| `v11-12-is-the-single-unresolved-mutual-extremal-vertex` | 14 | SETTLED (not new) | Already in reference data 5 since T127. | T147 | T152 |
| `deletion-from-a-known-optimum-needs-R` | all | **DEAD (parked with reason)** | `T' = T - deg_T(l) + R_l` stays; the construction route on it does not. Note reference data 12 uses the same identity in the other direction and gets a live result out of it. | T119 | T180 |
| `deletion-identity-is-T-minus-deg-plus-R` | 14/15 | **SETTLED (referee)** | R is not always zero; T121's proof miscounted a merged face's sides by one. | T119 | T127 |
| `insertion-into-k13-needs-seven-corner-clips` | 13/14 | **DEAD for B (reference data 22), open for other bases** | `Y = 7` from twelve bounded chords is what 54 needs from a 47-triangle base. For Kabanovitch's B it is impossible: reference data 22 gives `Y <= 6` from the crossing budget alone. For an arbitrary `p=0`, `c=0`, T=47 13-line table it is open, and the whole gap is reference data 22e's free-segment-placement condition. Historical text follows. | T125 | T280 |
| `insertion-into-k13-needs-seven-corner-clips-history` | 13/14 | **archive** | `T' = T(B) + Y`; reaching 54 from 47 needs `Y = 7` from 12 bounded chords. Reference data 12 still says 7/12 is unremarkable next to the 9/11 realized at k=12 -> 13, so the route is not dead. But of the seven gains, at most three can come from bounded non-triangular faces (reference data 20e), and the six turns T243-T254 spent pricing interior clips found every one of them costing five pieces. The remaining four must be corner clips of unbounded faces, and the only ones that are not themselves five pieces deep are the eleven corner wedges of reference data 21d. | T125 | T255 |
| `tamura-tight-implies-every-line-saturated` | all | **SETTLED (referee)** | Suzuki's k=15 is degree-regular at 13 as a theorem. | T127 | T127 |
| `bader-three-free-segments-form-a-path` | 14 | **SETTLED** | Reference data 5. | T102 | T127 |
| `three-free-segments-prove-T-leq-53-for-this-table` | 14 | **SETTLED** | `3T <= 162 - 3`. | T127 | T127 |
| `bader-triangle-adjacency-test-is-iff` | 14 | **SETTLED** | T94 proposed, T95 proved sufficiency, referee supplied necessity. Still the most productive claim in the ledger. | T94 | T152 |
| `mutual-extremal-vertex-tv-leq-1-general` | all | **SETTLED** | T106. Extremality at a vertex is a statement about which sectors escape. | T106 | T155 |
| `extremal-announcement-parity-O-even` | all | SETTLED | T108. `2M + O = 2k`. | T108 | T127 |
| `all-28-extremal-segments-accounted-third-free-is-interior` | 14 | **SETTLED** | T107, vindicated T118, reproduced at k=13. | T107 | T127 |
| `row1-fully-saturated-zero-free-segments`, `line8-saturation-one-free-segment`, `row11-swap-8-13-nets-50-not-54` | 14 | SETTLED | T117, T118, T116, all referee-verified. | - | T127 |
| `signotope-vs-chirotope-5-element-gate` | all | SETTLED, **and now a banned incantation** | T114. Any table surgery owes the rank-3 exchange axiom, then stretchability. 229 turns, zero invocations. It was nominated as "the concrete next step" at T182, T184, T186 and twice more, including at moments when a two-lookup argument (reference data 17) settled the same question. **Do not name it as a next step again unless you run one in the same turn or explain why it cannot be run by hand.** | T114 | T230 |
| `parallel-pair-budget-for-54` | 14 | **SETTLED for `c = 0` only** | Reference data 4. "A 14-line arrangement with 54 triangles has `p <= 3`" is derived from `T <= floor(B/3)` and is void once three lines may meet at a point (reference data 23). It has been used as a global filter since T102. It is a filter on the concurrence-free sub-family. | T102 | T280 |
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
| `k14-54-reachable` | 14 | **CONTESTED** | The actual question. 279 turns, zero verifier runs (tool unavailable, referee-confirmed on the thirteenth day), zero 14-line arrangements built. This cycle moved it in both directions at once. Against: reference data 22 kills insertion into Kabanovitch's B outright, at 53, closing the route the last hundred turns have walked. For: reference data 23 shows the segment budget that has scoped the search since T102 is a `c = 0` theorem, so the candidate space is strictly larger than assumed, and the mechanism that gets `k = 6, 8, 10, 12` to their bounds is absent from all three record near-misses. Net prior: unmoved, but the live object has changed from "a fourteenth line into B" to "a concurrence-bearing 14-line arrangement". | T1 | T255 |
| `mirror-program-weakly-dominated`, `pentagram-vertices-all-spoken-for`, `cluster-siting-abandoned-the-554-premise`, `outside-line-role-pigeonhole`, `similarity-rotation-budget-is-per-cluster`, `parking-confinement-blocks-secondary-reuse`, `companion-lines-are-not-free-they-are-clusters`, `companion-slopes-are-open-not-pinned`, `similarity-freedom-resolves-dual-role-tension`, `hull-avoidance-forces-external-crossings`, `direction-freedom-global`, `endpoint-match-convention-calibrated-against-k4-kills-all-three`, `local-lookup-program-exhausted` | 14 | DEAD (archive) | Unchanged. Do not cite. | - | T102 |
| `external-ray-triangle-verified`, `4cluster-negative-export-is-free`, `l1-carves-existing-ade-face`, `homothety-margin-not-scale-invariant`, `recentered-homothety-clears-E`, `wedge-cut-criterion-exact`, `pentagram-directions-equally-spaced`, `export-costs-intracluster-triangles`, `pentagram-walls-are-four-distinct`, `wall-tip-correspondence`, `cevian-wall-formula-invalid`, `euler-point-resolution-deltaF`, `degenerate-arrangement-63-faces`, `clustering-forces-three-nontriangles`, `cross-cluster-ratio-not-harder`, `homothety-realizes-S12`, `intracluster-tamura-cap-12`, `c7-mod7-kill-k14`, `central-symmetry-parallel-tax`, `mirror-fixed-lines-parallel`, `f0-no-self-symmetric-triangles`, `f0-axis-sector-forced-nontriangular`, `clustering-is-not-concurrence`, `pairwise-subarrangement-cap-67`, `mod2-weak-filter`, `cb-stacking-tautology`, `three-of-four-crossings-unhandled`, `construction-rate-far-below-target` | 14 | SETTLED (archive) | Unchanged. | - | T81 |
| `global-counting-cannot-obstruct-k14`, `symmetry-tax-pattern`, `f0-forced-nontri-at-least-10`, `m2-exhaustively-capped-28`, `single-line-translation-export`, `export-mechanism-needs-second-line`, `bc-to-m1m2-construction-dead`, `first-m2-triangle-exhibited`, `theta10-construction-unsited`, `sliver-exposure-question`, `corridor-danger-is-local-not-global`, `corridor-clipping-debate-t47-t51`, `translation-crossings-diverge-generically`, `pairwise-cap-gives-no-pressure`, `subarrangement-averaging-upper-bound`, `cevian-r80-and-descendants`, `edge-incidence-bound-121`, `vertex-corner-identity`, `nearpencil-starves-triangles`, `m3-nearpencil-hits-ceiling`, `residue-stacking-cb-vs-improved-even` | 14/all | DEAD or CONTESTED (archive) | Unchanged. | - | T77 |
