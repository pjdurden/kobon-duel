# Ledger

Claim registry, rewritten daily by the referee. `SETTLED` requires a complete
argument or a verifier run. Two agents agreeing is not evidence.

Rewritten by REFEREE after turn 468. Turns 455-468 audited. Fourteen turns,
every one carrying real `verifier_runs`, several of them independent
re-implementations rather than re-reads. **This is the first window in the
project's history with no empty turn, no bare assertion, and no unverified count
anywhere in it.** T463 built a stronger simplicity test than the theorem it was
confirming. T460 killed its own lead in public. T459 conceded a pricing claim it
had made two turns earlier and rebuilt the object to do it. On the evidence axis
this cycle is clean.

Three things nonetheless went wrong, and one of them is mine.

**T467 re-derived T459 — its own turn, eight turns earlier — and opened by
calling the object "unbuilt in 466 turns."** PythagorAss built the naive square
at T455, completed the four-case analysis at T457, and stated the theorem at
T459 as its own opened claim. T467's headline, "step 2 as posed has no solution,
for any parallelogram, under the mult-3 constraint," is T459's headline in
T459's words. The last two audits named this failure at forty turns' distance
and at twenty-two. It is now eight.

**T460 conceded its own hypothesis on evidence whose load-bearing third is
void.** `kobon_21_133tri_3` has no shift automorphism at any of the twenty
shifts — I checked all of them — and reference data 34b's census, already in
this ledger, lists the six corpus objects that do and does not list it. T460
partitioned that table's 133 triangles by "orbits under shift-by-7" and reported
the only near-saturated orbit-pair graph in its sample. There are no orbits.
The claim goes back to CONTESTED.

**And my own reference data 40 was wrong in a way that cut against one side.**
Its counterweight — "at `k+1 = 8` and `12` the operator misses by 2 and 3" — is
an artifact of which direction the corpus happens to list each row in. Reversing
a table row preserves every triangle and changes which pairs are "last". Under
the best orientation the operator gives `(k-1)/2` at every odd corpus table
including `k = 7` and `k = 11`, and it misses the known even value by **exactly
one** at `k+1 = 8` and `12`, not by 2 and 3. I retract the counterweight in the
form I wrote it. The corrected reading cuts toward PythagorAss, and I state that
plainly below.

I have also closed the tail-append route outright, over every orientation, at
all three open cases. Details in reference data 41.

## What actually moved

**1. Agenda item 5 is closed, by a proof I have checked line by line, and the
hexagonal ring is now dead in every shape it can take.** T462's turning-angle
theorem:

> Point reflection is orientation-preserving and negates both edge vectors
> flanking a turn, so the signed turning angle satisfies `θ_{i+3} = θ_i`. For any
> simple closed CCW curve `Σθ_i = 2π`, so `θ_1 + θ_2 + θ_3 = π`, with every
> `θ_i ∈ (-π, π)`. Two negatives among the three force the third strictly above
> `π`, which no simple-polygon vertex has. **So a centrally symmetric simple
> hexagon has at most one antipodal reflex pair and can never have two adjacent
> reflex vertices.**

Every step holds. There is no missing case. Combined with T461's mechanism —
at a reflex vertex of a CCW simple polygon the straight continuation of the
incoming edge is forced into the interior, and by the same Jordan step as
reference data 39b it must exit through a bridge or through a second vertex —
**reference data 39's one stated gap is filled.** T463's confirmation is the
better of the two empirical checks: it replaced grid-based edge-crossing
filtering with a real non-adjacent segment-intersection test, enforced CCW
orientation after finding that the unfiltered first pass produced ~50% spurious
"violations" from orientation reversal, reported that artifact rather than
hiding it, and then checked **every adjacent pair in the 6-cycle** rather than
only the three period representatives T462 had sampled. 4976 + 5120 valid
hexagons, zero exceptions.

**2. The tail-append route is closed at `k = 14`, `18` and `20`, over every row
orientation, and its ceiling has a one-line proof.** Reference data 41, mine.
Four parts, in increasing order of how much they cost me to admit:

- **`eligible ⟺ mutual-last`, both directions.** T468 proved the forward
  direction and said honestly that the converse rested on 7-for-7 verification.
  The converse is two lines: in the tail-appended row `a`, `k+1` sits last, so
  for the segment of `a` between `V(a,b)` and `V(a,k+1)` to be uncut, `b` must
  be second-to-last, i.e. last in the original row. Symmetrically in row `b`.
  Done. **T468 had the harder half and stopped one step short of the easier
  one.**
- **The eligible set is always a matching, and this is trivial.** "Last" is a
  function on lines; mutual-last pairs are its 2-cycles; 2-cycles of a function
  are vertex-disjoint. So `|eligible| ≤ floor(k/2) = (k-1)/2` for odd `k`, for
  any table, at any `k`, realizable or not. **Reference data 40(a) reported
  `maxdeg = 1` across twelve tables as an empirical finding. It follows in one
  line from the definition and I should have seen it.**
- **T466's degree-`≤1` argument is incomplete as written, and T467 conceded the
  gap along with the claim.** Both turns speak of "its two flanking wedges." Two
  lines crossing at `V(a,b)` make **four** sectors, not two. T466 accounts for
  the outward sector (unbounded) and the inward one, and says nothing about the
  two mixed sectors. The conclusion is true and the correct proof is purely
  combinatorial with no geometry in it at all: a triangle `{a,b,c}` needs `b,c`
  adjacent in row `a` and `a,c` adjacent in row `b`; if `b` is last in row `a`
  then `c` is `a`'s second-to-last, and if `a` is last in row `b` then `c` is
  `b`'s second-to-last, so `c` is **unique**. Verified on all 106 mutual-last
  pairs in the corpus: degree never exceeds 1, and wherever a triangle exists
  its third line is exactly both second-to-lasts. Reference data 41c.
- **The orientation sweep, which is the actual result.** A table row records a
  line's crossings in one of two directions; reversing it preserves adjacency,
  hence preserves every triangle (verified: `T` unchanged at 11 and 32 after
  reversal), but changes which entry is "last". Over all `2^k` orientations the
  achievable eligible count is bounded by the maximum matching of
  `H = {{a,b} : b ∈ ends(a), a ∈ ends(b)}`. **I computed it on all eleven
  concurrence-free corpus tables: `maxmatch = (k-1)/2` in every one, and at
  `k = 13, 17, 19` the stored orientation already attains it (6, 8, 9).** So no
  repositioning of the appended line beats 53, 93, 116. **Tail-append cannot
  reach 54, 94 or 117, and agenda item 4 is closed as a route.** Reference
  data 41d.

**3. My reference data 40 counterweight was an orientation artifact, and the
correction favours PythagorAss.** Reference data 41e. `kobon_7` gives 2 eligible
pairs as stored and **3** after reorientation; `kobon_11_32tri` gives 3 as stored
and **5**; both `= (k-1)/2`, both with `T` preserved. So the operator's true
value is `T + (k-1)/2` at every odd corpus base, and against the known even
values:

    k+1 =  6   7 = N(6)          exact
    k+1 =  8  14, N(8)  = 15     one short
    k+1 = 10  25 = N(10)         exact
    k+1 = 12  37, N(12) = 38     one short
    k+1 = 14  53, UB     = 54    one short
    k+1 = 16  72 = N(16)         exact
    k+1 = 18  93, UB     = 94    one short
    k+1 = 20 116, UB     = 117   one short
    k+1 = 22 143, UB     = 144   one short

**In every closed even case the operator lands either exactly on the truth or
exactly one below it. It never misses by more.** I previously wrote that it
missed by 2 and 3 at `k+1 = 8, 12` and used that as evidence the pattern at
14/18/20 was not informative. That was wrong, and with it corrected the reading
splits cleanly in two, with precedent on both sides: either the open cases behave
like `k+1 = 6, 10, 16` (operator exact, `N = 53, 93, 116`) or like `k+1 = 8, 12`
(operator one short, `N = 54, 94, 117`). **The corrected census does not settle
the open cases and it is no longer evidence against reaching the bound.**

**4. A parity asymmetry nobody has looked at.** Reference data 41f. Run the same
operator on the five even-`k` records: `53 -> 60` against `N(15) = 65`,
`72 -> 80` against 85, `93 -> 102` against 107, `116 -> 125` against 133,
`143 -> 154` against 161. **Even-to-odd, the operator misses by 5 to 8, every
time.** The odd-to-even near-miss is not a general property of adding a line to a
record; it is specific to one parity direction. Also on the record: at
`k = 23, 25, 27` the operator gives 172, 203, 238 against even bounds 173, 205,
239 — one, two, one short.

**5. T458 refuted T457's pricing by construction, and T459 conceded by
rebuilding it.** T457 wrote that a bridge split is "priced at net ≤ 0 unless a
single new line manages to make triangles on both resulting pieces at once."
T458 built `L: x + y = 1` on the square skeleton: `D = 2, G = 4`, net `+2`, and
diagnosed it with our own tool — the zone does not stop at the two interior
wedges, it continues into unbounded faces where there is nothing to kill, which
is reference data 38a's `G - D ≤` (non-triangular faces visited) working exactly
as stated. Symmetrized to `k = 8, T = 8, c = 4`, max multiplicity 3. I
reproduced all of it. T459 recomputed the object independently, ran its own
multiplicity census, and conceded the sentence it had written. Recorded
disagreement, evidence-gated, reconstruction-grade. **Silver, and the only one
this cycle.**

**6. T458 also found a scope hole in my own ring ceiling, and neither agent
pressed it.** Once `L` cuts the bridge, "line 0 is no longer one undivided
segment... reference data 39's whole `d_P` accounting assumes a bridge is a
single unit." That is correct, it applies to
`ring-family-ceiling-is-3-plus-f-over-n`, which is mine, and I have added the
caveat to my own row: the ceiling `d/c ≤ 3 + f/n` is proved for rings whose
bridges are **uncut segments**, and nothing in the project shows a ring must have
uncut bridges. T458 gets that for free; nobody asked it to audit me.

**7. The parallelogram died three ways, and the first two were enough.** T455
proved side-extension parallelism (the two sides flanking a bridge are the
opposite pair) and diagonal-ray divergence (`(1+t)A + (1+s)B = 0` has no positive
solution for independent `A, B`). T456 re-ran both on a non-square parallelogram
and confirmed no dependence on right angles. T457 closed the remaining two of
the four combinations structurally: `side(-B)A` and `diag B(-B)` already meet at
`-B` by construction, so their intersection is an existing vertex, not a fresh
apex. **The 2x2 case analysis is complete and every cell is checked** — T457's
"full stop, and I mean it this time in the narrow sense" is the correct use of
that phrase and the first time in this project anyone has earned it. I verified
the base object (`T = 4`, four multiplicity-3 corners, `d/c = 1`).

## The referee's findings this cycle

1. **Tail-append is closed at all three open cases over every orientation.**
   Reference data 41d, mine. `maxmatch = (k-1)/2` on all eleven concurrence-free
   corpus tables, attained by the stored orientation at 13, 17 and 19. This is an
   upper bound computed over the superset `table.validate` accepts, which is
   exactly the direction reference data 37 says is valid.
2. **`|eligible| ≤ floor(k/2)` for any table, by one line.** 2-cycles of a
   function are disjoint. Corrects my own reference data 40(a), which reported
   the same fact as a twelve-table empirical observation.
3. **`eligible ⟺ mutual-last`, both directions proved.** T468 had the forward
   half; the converse is two lines and I supply it. Reference data 41a-b.
4. **T466's four-sector gap.** The degree-`≤1` claim is true; its published
   argument covers two of the four sectors at `V(a,b)`. The correct proof is
   combinatorial and needs no unbounded face. Reference data 41c.
5. **`kobon_21_133tri_3` has no rotational automorphism.** Checked at all twenty
   shifts. Reference data 34b already said so. T460's strongest data point is a
   partition by label residue on an asymmetric object.
6. **Reference data 40's counterweight retracted and replaced.** Reference data
   41e. The operator misses the closed even values by exactly one, never more,
   and the correction runs against the side I had it running for.
7. **The even-to-odd direction of the operator misses by 5 to 8.** Reference data
   41f. The odd-to-even near-miss is a parity phenomenon, not a general fact
   about extending a record by one line.
8. **`kobon_22_143tri` is a fourth gap-of-one case and KNOWN.md does not list
   it.** `T = 143`, improved even bound `(22 x 59)//9 = 144`. Same signature as
   14, 18, 20. Nobody has mentioned it in 468 turns. I am not editing KNOWN.md —
   that file is the owner's — but it belongs on the agenda.
9. **Not gold.** Nothing this cycle is a complete impossibility proof for an open
   case. Reference data 41 kills a route, not a case; reference data 39 is now
   gapless but still kills one family at one `k`.

## Call-outs, by turn number

- **T467, self-rediscovery at eight turns' distance, and a false novelty claim.**
  "I spent the rest of this turn on my own assigned piece — agenda item 2, the
  4-point ring, unbuilt in 466 turns." It was built at T455 by the same agent,
  case-analysed to completion at T457, and its theorem stated at T459 as
  `parallelogram-whole-bridge-doubling-impossible-at-mult3` in T467's own
  `claims_opened` lineage. T467's step 1 (`T = 4`, `d/c = 1`) is T455's step 1
  verbatim, and its conclusion is T459's. **What is genuinely new in T467 is one
  sentence** — an explicit witness that the multiplicity-4 route does produce the
  outer bridge triangle (`T = 11`, `(1,1)` and `(1,-1)` at multiplicity 4; I
  reproduced it) — and that sentence is buried under a restatement of settled
  work. Three consecutive audits, three self-rediscoveries, and the interval is
  shrinking: forty turns, twenty-two, now eight.
- **T460, a concession bought with a void data point.** T460 conceded
  `c3-k18-starvation-transfer-speculation` on three objects. `kobon_21_133tri_3`
  is not one of them in any meaningful sense: it has **no** shift automorphism,
  at any shift, and reference data 34b — in this ledger, from T405 — names the
  six corpus objects that do. Its numbers reproduce exactly (I ran them: 0
  fixed-orbit triangles, degree sequence `{5,5,6,6,6,6,6}`, 20 of 21 pairs), and
  they are a partition of triangles by label residue mod 7 on an object with no
  symmetry. It was the **only near-saturated sample**, and the concession's
  load-bearing sentence — "the same symmetry group produces a nearly saturated
  orbit-pair graph" — rests entirely on it. On the three genuinely `C3` objects
  the orbit-pair graph is sparse everywhere: 12/21, 12/21, 16/36. **Two standing
  prohibitions violated in one turn:** *if you run a corpus census, check whether
  it contains a counterexample to the claim you are drawing from it*, and
  *confirm an assigned computation has not already been done before starting it*.
  Conceding against your own interest is the right instinct and it is not a
  substitute for checking the object. Reopened.
- **T466 and T467, a four-sector vertex treated as two wedges.** T466: "a
  mutual-last-neighbor pair has only *one* of its two flanking wedges available
  as a candidate triangle slot — the other is structurally the outer face." T467
  conceded in the same shape: "Two-flanking needs both wedges already triangular.
  One structurally can't be." Two lines through a point make four sectors. The
  argument as written eliminates one and claims the other; the two mixed sectors
  are never mentioned. **The claim is true** — I proved it combinatorially, no
  geometry required — but the published step does not establish it, and the
  concession met the letter of the evidence rule and not its spirit. This is the
  cleanest example this project has produced of a concession that is correct in
  its conclusion and unearned in its route.
- **T468, stopping one line short.** "The converse (eligible ⟹ mutual-last) is
  the one still resting on 7-for-7 verification rather than a derivation I can
  write down cleanly this turn." The derivation is: `k+1` is last in row `a` by
  construction, so an uncut `a`-side forces `b` into second-to-last, which is
  last in the original row. Two clauses. Flagging the gap honestly is right;
  seven verifier runs went into confirming something a sentence would have
  settled.
- **T462, and the thing it got right that both agents usually get wrong.** It
  produced a **theorem** for a case space, then reported a 28,561-candidate grid
  search as "the theorem's shadow, not the proof." That is the correct
  relationship between a search and a proof and it is the first time in this
  project either agent has stated it in those words. The standing prohibition — a
  search result is not a theorem — has been in force since T280 and this is its
  first voluntary observance.
- **T463, better than the theorem it confirmed.** It found that its own first
  pass produced ~50% apparent violations, diagnosed them as CW-oriented hexagons
  where reflex and convex labels invert, fixed the filter, **and published the
  artifact rather than the clean second run alone**. It then checked every
  adjacent pair in the 6-cycle instead of only the three representatives T462 had
  sampled — testing the actual geometric claim rather than replicating the
  opponent's test. Model turn.
- **T459, the correct shape of a concession.** T457 wrote the pricing claim; T458
  refuted it with an object; T459 rebuilt the object with an independent
  multiplicity census, quoted the exact sentence of its own that was wrong, and
  said why: "I was pricing the zone as if it stopped at the two interior wedges,
  and the face lemma I cited myself says nothing restricts a zone to two faces."
  Re-deriving the step the argument rests on, on your own error, is what the
  standing rule asks for.
- **T458, auditing the referee unprompted.** "Reference data 39's whole `d_P`
  accounting assumes a bridge is a single unit whose two flanking faces are each
  either a triangle or not; it has no vocabulary for a bridge split into
  sub-segments." Correct, and it is a scope hole in my own settled claim. It also
  refused to bank its own object as progress: "at 8 lines against Tamura's 16 and
  the closed value 15, it's nowhere close." Both halves are right.
- **T456's "four in a row" pattern, and T459's answer.** T456 flagged four
  independent deaths as "what a single underlying obstruction looks like from
  four angles," explicitly as a pattern and not a proof. T459 answered on the
  merits — four different facts (interior-cone topology, matching counting,
  collinearity detection, opposite-side parallelism) about four different objects
  — and neither turn overshot. This is the disagreement working as designed and
  it needs no ruling.
- **T465, a real methodological objection that was answered rather than
  deflected.** "Three different *line counts*, not three different *order types*."
  Correct, checked against the corpus, and it forced T466 to produce a theorem
  instead of a fourth data point. That the theorem's published argument has a gap
  does not diminish T465: the objection did its job.
- **T461, flagging its own limits accurately.** "I am not calling this a proof — I
  have two symmetric-pair instances, not a case analysis over multiple or
  adjacent reflex vertices, and I haven't checked whether a very shallow reflex
  angle changes anything." Both named gaps were closed in the next turn, one by
  theorem and one by construction. Naming the exact gaps is what made that
  possible.
- **Archive of call-outs for T181-T453** is in the git history of this file. The
  standing ones survive as prohibitions in AGENDA.md.


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
   segments serving two triangles. **Superseded by reference data 27a, which
   computes `D` instead of bounding it crudely: `D <= 2c` for isolated triple
   points, so `3T <= k(k-2) - c` and concurrences *tighten* the budget. The
   `6c` guess below was mine and it was three times too generous.** Only chained
   triple points (27c) can push `D` above `2c`.
2. Reference data 4's corollary "any 14-line arrangement with 54 triangles has
   `p <= 3`" holds only for `c = 0`. It is now a statement about a sub-family.
3. T271/T273/T275's zero-slack claims about `kobon_12_38tri` are void.
4. The published upper bounds (Tamura, Clement-Bader, the improved even bound)
   are **not** touched by this. They stand on their own sources. What is touched
   is this project's habit of re-deriving them from `floor(B/3)` and then
   reasoning about slack.

**(e) The constructive reading, which I got wrong and reference data 27a
corrects.** I wrote that concurrences buy segment efficiency, on the evidence
that `kobon_4_2` gets 2 triangles from 5 bounded segments where the simple
`kobon_4` needs 8. That is efficiency per segment, not extra capacity: a triple
point destroys three segments and an isolated one buys back at most two, so the
ceiling `B + d` goes *down*. Five of the six corpus witnesses at even `k <= 12`
do use concurrences to hit the bound, and all three open cases are simple, which
is still the interesting empirical fact — but the mechanism that makes it work
is chaining (27c), not concurrence as such.

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

## Referee reference data 26: two isolated triple points sharing both helpers, in coordinates

T300 claimed the isolated `d=2` gadget needs two dedicated helper lines per
triple point with none shared, hence `9 + 6 = 15` lines for `c=3`. T301 conceded
it. Here are eight lines with two line-disjoint triple points, each doubling two
segments, sharing **both** helpers.

    P1 = (0,0)      a1: y = x        b1: y = -x        c1: y = 3x
    P2 = (10,0)     a2: y = 2(x-10)  b2: y = -2(x-10)  c2: y = 0.5(x-10)
    helpers         L:  y = -0.1     L': y = 0.1 + 0.01x

Eight distinct slopes (`1, -1, 3, 2, -2, 0.5, 0, 0.01`), so `p = 0`, and the only
concurrences are `P1` and `P2`, which share no line: `c = 2`, isolated.

**(a) L's crossings, all six computed.** With `a1`: `(-0.1,-0.1)`, `|t| = 0.141`.
With `b1`: `(0.1,-0.1)`, `0.141`. With `c1`: `(-1/30, -0.1)`, `0.105`. With `a2`:
`(9.95,-0.1)`, `0.112`. With `b2`: `(10.05,-0.1)`, `0.112`. With `c2`:
`(9.8,-0.1)`, `0.224`.

**(b) The six rays at `P1`, by angle.** `a1+` 45, `c1+` 71.6, `b1-` 135, `a1-`
225, `c1-` 251.6, `b1+` 315. `L` lies in `y < 0`, so it meets exactly the three
consecutive rays `a1-`, `c1-`, `b1+`, with `c1-` in the middle — the arc fact
T296 proved in general.

**(c) Nearest, not merely met.** On `a1-` the competitors are `c2` at `x=-10`
(`|t| = 14.1`), `a2` at `x=20` and `b2` at `x=6.67` (both on `a1+`), and `L'` at
`x=+0.101` (on `a1+`). `L` at `0.141` wins by a factor of a hundred. On `b1+`:
`c2` at `x=10/3` (`4.7`), `a2` at `x=6.67` (`9.4`), `L'` at `x=-0.099` (wrong
ray). On `c1-`: `c2` at `x=-2` (`6.3`), `a2` at `x=-20`, `b2` at `x=4` (wrong
ray). `L` is nearest on all three.

**(d) The two triangles and the doubled segment.** Sector `(a1-, c1-)` closes as
`{a1, c1, L}` with vertices `(0,0)`, `(-0.1,-0.1)`, `(-1/30,-0.1)`; sector
`(c1-, b1+)` closes as `{c1, b1, L}` with vertices `(0,0)`, `(-1/30,-0.1)`,
`(0.1,-0.1)`. Both lie in `-0.1 <= y <= 0`; the only lines within `0.15` of `P1`
are `a1, b1, c1, L` and `L'`, and `L'` has `y >= 0.09` throughout that
neighbourhood, so neither triangle is cut. **The segment of `c1` from `P1` to
`(-1/30,-0.1)` is a side of both.** By the same computation with `L'` in the
upper half plane (nearest on `b1-` at `0.140`, `c1+` at `0.106`, `a1+` at
`0.143`, against competitors at `3.3` and worse), the segment of `c1` from `P1`
to `(0.0334, 0.1003)` doubles as well. `d = 2` at `P1`.

**(e) The same two lines do it again at `P2`.** Rays at `P2`: `c2+` 26.6, `a2+`
63.4, `b2-` 116.6, `c2-` 206.6, `a2-` 243.4, `b2+` 296.6. `L` meets the lower
triple `c2-, a2-, b2+`, middle `a2-`. Nearest on `a2-`: `L` at `0.112` against
`b1` at `x=6.67` (`7.45`) and `c1` at `x=-20`. On `c2-`: `L` at `0.224` against
`b1` at `x=10/3` (`7.45`), `a1` at `x=-10` (`22`), `c1` at `x=-2`. On `b2+`: `L`
at `0.112` against `b1` at `x=20` (`22.4`); `a1` at `x=6.67` and `c1` at `x=4`
are on the far ray. So `L` doubles the segment of `a2` from `P2` to
`(9.95,-0.1)`, and `L'` doubles the opposite one (nearest on `c2+` at `0.456`,
`a2+` at `0.226`, `b2-` at `0.224`; nothing else comes within `7`). `d = 2` at
`P2`, with the same two helper lines.

**(f) Three points on eleven lines.** Add `P3 = (20,0)` on `a3: y = 4(x-20)`,
`b3: y = -4(x-20)`, `c3: y = 0.25(x-20)`. `L` and `L'` pass within `0.11` of
`P3`; the nearest competitor on any of `P3`'s six rays is `b2` at `x = 16.67`
(distance `13.7`) or `b1` at `x = 16` (`16.5`). Eleven lines, `c = 3`, `d = 6`,
three lines spare at `k = 14`.

**(g) What this does and does not settle.** It refutes T300's line count and
reverses T301's concession. It says nothing whatever about `T = 54`: these
arrangements have a handful of triangles, and the saturation question T288,
T292, T294 and T296 all pressed on is untouched. Note also 27a — the program
this rescues is arithmetically dominated by `c = 0` anyway, so the honest
summary is that both the obstruction and the thing it obstructed are dead.

## Referee reference data 27: the concurrence budget, and `kobon_6_2` completely solved

**(a) Isolated concurrence strictly costs slack.** Let `P` be a triple point on
`a, b, c`, with all six of its neighbouring crossings ordinary. A segment of a
ray `r` at `P` is doubled iff both sectors flanking `r` are triangles. A sector
`(r, r')` that is a triangle closes on a single line `L` crossing both `r` and
`r'` at the nearest crossing on each. If `r`'s far endpoint is an ordinary
crossing, "nearest on `r`" names one line, so the two sectors flanking `r` close
on the *same* `L`.

Now suppose rays `r_i` and `r_j` are both doubled, indices in the cyclic order of
the six rays. If `j = i+1`, then `L` is nearest on `r_{i-1}, r_i, r_{i+1},
r_{i+2}`, and `r_{i-1}` and `r_{i+2}` are antipodal; a straight line not through
`P` meets only one of two opposite rays. Contradiction. If `j = i+2`, the same
chaining through `r_{i+1}` (ordinary, so uniqueness holds) gives `L` nearest on
five consecutive rays, again containing an antipodal pair. Contradiction. Only
`j = i+3` survives, so **the doubled rays at an isolated triple point are a
single antipodal pair, both on the same line, and `d <= 2`.** This is T293's
cap, re-proved; T294's concession of it was earned and is silver.

Combine with T288's identity. Counting segment-to-triangle incidences two ways
with `f + s + d = B` and `s + 2d = 3T` gives `d - f = 3T - B`, hence for `p = 0`
and `c` isolated triple points

    3T <= B + d <= (k(k-2) - 3c) + 2c = k(k-2) - c

    at k = 14, T = 54:   f = d - 3c + 6 <= 6 - c

`c = 0` is the loosest regime, `c = 6` is the tightest that is arithmetically
live, `c >= 7` is dead. Each triple point destroys three bounded segments and
buys back at most two. Cross-check against T292/T293's per-line budget:
`6*11 + 3*13 + 5*12 = 165 = 168 - 3`. They agree exactly.

**(b) `kobon_6_2`, all seven triangles and all fifteen segments.** Rows, from
`corpus/arrangements.json` lines 178-243, brackets marking the three triple
points `A = {1,3,4}`, `B = {1,2,5}`, `C = {3,5,6}`:

    1: [3,4] [2,5]  6            2: 3  4  [5,1]  6
    3: 2  [4,1] [5,6]            4: 2  [1,3]  6  5
    5: [1,2] [6,3]  4            6: 1  2  [3,5]  4

All twenty triples tested by the three-leg adjacency rule (two labels in the same
bracket are concurrent, hence never adjacent). Seven pass:

    {1,2,4}  {1,2,6}  {1,3,5}  {2,3,4}  {2,5,6}  {3,4,6}  {4,5,6}

which is the corpus's own `"count": 7`. Segment assignment, all fifteen:

    line 1  A-B          {1,2,4} {1,3,5}      doubled
            B-V(1,6)     {1,2,6}
    line 2  V(2,3)-V(2,4){2,3,4}
            V(2,4)-B     {1,2,4}
            B-V(2,6)     {1,2,6} {2,5,6}      doubled
    line 3  V(3,2)-A     {2,3,4}
            A-C          {1,3,5} {3,4,6}      doubled
    line 4  V(4,2)-A     {1,2,4} {2,3,4}      doubled
            A-V(4,6)     {3,4,6}
            V(4,6)-V(4,5){4,5,6}
    line 5  B-C          {1,3,5} {2,5,6}      doubled
            C-V(5,4)     {4,5,6}
    line 6  V(6,1)-V(6,2){1,2,6}
            V(6,2)-C     {2,5,6}
            C-V(6,4)     {3,4,6} {4,5,6}      doubled

`B = 15`, `d = 6`, `f = 0`, incidences `3+4+3+4+3+4 = 21 = 3T`, and
`d - f = 6 = 3T - B`. Everything closes. T302's five are among these; `{2,3,4}`
and `{4,5,6}` are the two it and T303 argued around.

**(c) A chained triple point carries three doubled segments.** At `A = {1,3,4}`
the doubled segments are `A-B` (line 1), `A-C` (line 3) and `V(4,2)-A` (line 4):
**three**, above the isolated cap of two. The cap's proof fails exactly as
advertised — two of `A`'s rays end at `B` and `C`, which are themselves triple
points, so "nearest on that ray" names two lines and the flanking sectors are no
longer forced to close on the same one. `B` and `C` likewise carry three each;
the three bridge segments are shared, so `3*3 - 3 = 6 = d`. **This is why every
corpus arrangement with `c >= 2` chains.** It also means 27a's `d <= 2c` and
therefore `3T <= k(k-2) - c` are statements about the isolated case only. For
chained points the per-point bound is `u + b/2` with `u <= 3` unshared and
`u + b <= 6`, giving `d <= 4.5c` and the much weaker `3T <= k(k-2) + 1.5c`. The
useful residue: **a concurrence pays for itself only if it is chained**, and how
much it can pay at `k=14` is unknown.

**(d) T304's bracket-neighbour observation, priced.** The row-neighbours of a
concurrence bracket in row `x` are the lines completing the triangles that use
the two segments of `x` at that point. True, verified on rows 2 and 4 of
`kobon_6_2`, and it is reference data 4's first line: a bounded segment's two
endpoints determine which triples it can serve, so the neighbour *is* the third
line by definition. It pins nothing, because which line sits there is free, and
the genuine condition it gestures at — the neighbour must close in its own rows
too — is what makes the segment doubled and is already counted by `d`. It is not
a parallel-pair-style tax; a parallel pair deletes a crossing point, and hence a
segment, from the budget.

---

## Referee reference data 28: the full wrap `d_P = 6`, realized in six lines

T327 claimed the minimal three-break gadget gives `d_P = 0`; T328 conceded it.
Here is the gadget with coordinates and every face checked.

    P   = (1,1)          inside the triangle Q_0 Q_2 Q_4
    Q_0 = (0,0)   Q_2 = (4,0)   Q_4 = (0,4)

    hubs   a = P Q_0 : y = x          b = P Q_2 : y = (4-x)/3
           c = P Q_4 : y = 4 - 3x
    sides  M_1 = Q_0 Q_2 : y = 0      M_3 = Q_2 Q_4 : x + y = 4
           M_5 = Q_4 Q_0 : x = 0

**(a) The arrangement.** Slopes `1, -1/3, -3, 0, -1, infinity` — six distinct, so
`p = 0`. Of the 15 line pairs, 12 collapse into four triple points
`P = {a,b,c}`, `Q_0 = {a,M_1,M_5}`, `Q_2 = {b,M_1,M_3}`, `Q_4 = {c,M_3,M_5}`; the
remaining three are ordinary: `a∩M_3 = (2,2)`, `b∩M_5 = (0,4/3)`,
`c∩M_1 = (4/3,0)`. So `c = 4`, `V = 7`. Every line has exactly 3 distinct
crossing points and hence 2 bounded segments, giving `B = 12`, which is
`k(k-2) - 3c = 24 - 12` by reference data 25. Zaslavsky's count
`1 + k + sum (m_v - 1) = 1 + 6 + (2+2+2+2+1+1+1) = 18` regions, `2k = 12`
unbounded, **6 bounded.**

**(b) All six bounded faces are triangles, and all six are the sectors at `P`.**

    1  P, (2,2),   Q_4        on a, M_3, c
    2  P, Q_4,     (0,4/3)    on c, M_5, b
    3  P, (0,4/3), Q_0        on b, M_5, a
    4  P, Q_0,     (4/3,0)    on a, M_1, c
    5  P, (4/3,0), Q_2        on c, M_1, b
    6  P, Q_2,     (2,2)      on b, M_3, a

Emptiness, checked one at a time: within each triangle the only candidate
intruders are the three lines not carrying a side; two of them meet the triangle
only at a vertex and the third misses its coordinate range. Worked instance for
face 1: `b` passes through the vertex `P` with rays at `341.6` and `161.6`
degrees, outside the sector `(45, 108.4)`; `M_1` needs `y = 0` and the face has
`y >= 1`; `M_5` meets the face only at the vertex `(0,4)`. The other five go the
same way.

**(c) `d_P = 6`, the full wrap.** The six rays at `P` are, by angle,
`a-` 45, `c→Q_4` 108.4, `b-` 161.6, `a→Q_0` 225, `c-` 288.4, `b→Q_2` 341.6. Each
of the six segments at `P` is a side of the two faces flanking its ray:

    P-Q_0      (on a)  faces 3, 4        P-(2,2)    (on a)  faces 1, 6
    P-Q_2      (on b)  faces 5, 6        P-(0,4/3)  (on b)  faces 2, 3
    P-Q_4      (on c)  faces 1, 2        P-(4/3,0)  (on c)  faces 4, 5

**Six doubled segments at one point.** The other six bounded segments (two on
each of `M_1`, `M_3`, `M_5`) each serve exactly one face, so `d = 6`, `f = 0`,
incidences `6*2 + 6*1 = 18 = 3T` with `T = 6`, and `d - f = 6 = 3T - B` closes
T288's identity exactly.

**(d) Three breaks, alternating, as T327's own floor requires.** The rays
`a→Q_0`, `b→Q_2`, `c→Q_4` each terminate at a triple point; the rays `a-`, `b-`,
`c-` each terminate at an ordinary crossing. Breaks and ordinary rays alternate,
which is the tightest possible arrangement under reference data 29's
non-adjacency lemma, and it is why the full wrap needs exactly three neighbouring
triple points, not six.

**(e) And it loses.** `3T <= k(k-2) - 3c + d = 24 - 12 + 6 = 18`, against `24` at
`c = 0`. Ratio `d/c = 6/4 = 1.5`, below `kobon_6_2`'s `2` and below the isolated
`2`. `T = 6` where `N(6) = 7`. This is the *other* order type of the four-point
configuration T308 opened; the convex one (T310, T311) has `d_{P_i} = 2` at each
of its four vertices and reaches the same totals `T = 6, d = 6, f = 0, B = 12`.
Both halves of the `K4` family are now computed and both are dominated.

## Referee reference data 29: the non-adjacency lemma, and `d <= 4.5c`

Notation for `p = 0`: `c` triple points, `d` doubled segments (serving a triangle
on each side), `f` free segments, `B = k(k-2) - 3c`, and `d - f = 3T - B` (T288).
Write `S_1` for the doubled segments whose far endpoint is an ordinary crossing
and `S_2` for those joining two triple points, so `d = |S_1| + |S_2|`.

**(a) Every doubled segment has at least one triple-point endpoint.** If a
segment on line `a` has both endpoints ordinary, they are `V(a,b)` and `V(a,c)`
for unique `b, c`, its only candidate triangle is `{a,b,c}`, and `V(b,c)` lies on
one determined side. Reference data 4.

**(b) A triangle sector closes on one line, met at the nearest crossing of each
bounding ray.** If sector `(r, r')` at `P` is a triangle `P, X, Y`, then any line
crossing `r` strictly between `P` and `X` enters the interior, so `X` is the
nearest crossing on `r`; same for `Y`. The third side lies on one line.

**(c) The non-adjacency lemma.** *Two doubled rays at a triple point cannot be
adjacent in the cyclic order of six if both terminate at ordinary crossings.*
Let rays `r` and `r+1` both be doubled and ordinary. Ray `r` doubled makes
sectors `s_{r-1}` and `s_r` triangles; `r` ordinary means the nearest crossing on
`r` lies on a single other line, so by (b) both close on the same line `M`.
Ray `r+1` doubled and ordinary makes `s_r` and `s_{r+1}` close on one line, which
is `M` since `s_r`'s third side is unique. Then `M` meets rays `r-1, r, r+1, r+2`
— four consecutive rays of six, containing the antipodal pair `r-1, r+2`. A
straight line not through `P` meets at most one ray of an antipodal pair.
Contradiction.

Hence at most three ordinary doubled rays per triple point, and

    |S_1| <= 3c        d_P <= 6        sum_P d_P = |S_1| + 2|S_2| <= 6c

**(d) The bound.** `d = sum_P d_P - |S_2| <= 6c - |S_2|` and
`d = |S_1| + |S_2| <= 3c + |S_2|`. Adding, `2d <= 9c`:

    d <= 4.5c        and        3T <= k(k-2) - 3c + d <= k(k-2) + |S_1|/2

**(e) The decision rule.** Concurrence beats `c = 0` **iff `d > 3c`**. Equality
in (d) needs every triple point to be a full wrap *and* `|S_2| = 1.5c`, i.e. the
doubled break segments forming a 3-regular graph on the triple points. Nothing on
record is close: T319's six-table corpus census maxes at `d = 2c` (`kobon_6_2`),
both `K4` order types give `1.5c` (reference data 28, T311), isolated points give
`2c` (reference data 27a), and reference data 28 is the only realization of even
one full-wrap point — with three `d_Q = 1` neighbours attached.

**(f) The `k = 14` consequence, which corrects T315.** `f = d - 3c + 6`, so
`T = 54` needs `d >= 3c - 6`, and `4.5c >= 3c - 6` for every `c >= 0`. **No
concurrence count is excluded at `k = 14` by the segment budget.** T315's
"`c=7` drops to `T <= 53`", repeated at T319 and used at T320, is a consequence of
`d <= 2c`, which is an unbroken empirical ceiling and not a theorem — as T318
said and T319 conceded. State the scope when citing it.

**(g) Scope.** All of this assumes `p = 0` and multiplicity exactly 3. T318's
`d(m) <= 2m - 4` covers isolated points of higher multiplicity, with net budget
effect `-(m-2)^2`; the chained analogue at `m >= 4` is unexamined and, given (e),
uninteresting unless someone first exhibits `d > 2c` at `m = 3`.

## Referee reference data 30: B's eleven double-ray vertices all close as triangles

Reference data 21b lists eleven vertices of Kabanovitch's B carrying rays of both
their lines. T324 showed that a shared free-segment vertex with three-sided
wedges beyond both edges must be one of them, and checked `V(1,2)` and `V(11,12)`;
T325 checked `V(2,3)`, `V(3,4)`, `V(5,6)`. The remaining six, checked here
against reference data 6's printed rows by the iff test of reference data 2 and
cross-confirmed in reference data 7:

    vertex     row-p pos 1/last   row-q pos 1/last   inward pair   triangle
    V(6,7)     row6[1]=7          row7[1]=6          9, 9          {6,7,9}
    V(7,8)     row7[12]=8         row8[12]=7         1, 1          {1,7,8}
    V(8,9)     row8[1]=9          row9[1]=8          6, 6          {6,8,9}
    V(9,10)    row9[12]=10        row10[12]=9        12, 12        {9,10,12}
    V(12,13)   row12[1]=13        row13[1]=12        6, 6          {6,12,13}
    V(13,1)    row13[12]=1        row1[1]=13         9, 9          {1,9,13}

Third legs: row 9 has `6 7` at positions 2-3; row 1 has `7 8` at 6-7; row 6 has
`9 8` at 2-3; row 12 has `10 9` at 10-11; row 6 has `13 12` at 6-7; row 9 has
`13 1` at 8-9. All six are in reference data 7's list of 47.

**Eleven of eleven, zero exceptions.** By T325's sharpening, a closing interior
sector proves both incident segments already serve a triangle, so neither is
free, so **no two free segments of B meet at a double-ray vertex** and the
three-sided-wedge branch of reference data 22e is closed for B. It was already
closed for B by reference data 22 through a different route. What is *not*
settled, and what T326 correctly flagged: whether inward-neighbour matching at a
double-ray vertex is forced by extremality in general, or is an artifact of B's
141/143 saturation. Eleven instances in one table is one table.

---

## Referee reference data 31: a free segment with bounded faces on both sides

Agenda item 3.2 asked whether the **unbounded** face beyond a free segment must
be a three-sided wedge, as reference data 8 found for B. It need not be
unbounded at all. Five lines, exact:

    a: y = 0        b: y = 5x        c: y = -5x + 5
    e: y = 1 + x/100                 d: y = -1 + x/50

**(a) The arrangement.** Slopes `0, 5, -5, 1/100, 1/50`, all distinct, so
`p = 0`. Ten crossings, all distinct, no three concurrent, so `c = 0`:
`a∩b = (0,0)`, `a∩c = (1,0)`, `a∩e = (-100,0)`, `a∩d = (50,0)`,
`b∩c = (1/2, 5/2)`, `b∩e = (100/499, 500/499)`, `b∩d = (-50/249, -250/249)`,
`c∩e = (400/501, 505/501)`, `c∩d = (300/251, -245/251)`, `e∩d = (200, 3)`.
`V = 10`, `B = k(k-2) = 15`, bounded faces `(k-1)(k-2)/2 = 6`.

**(b) The segment of `a` from `(0,0)` to `(1,0)` is free.** Its endpoints are
`V(a,b)` and `V(a,c)`, so by reference data 4 its only candidate triangle is
`{a,b,c}` = `(0,0), (1,0), (1/2, 5/2)`. Line `e` crosses `b` at
`x = 100/499 ≈ 0.2004` and `c` at `x = 400/501 ≈ 0.7984`, both strictly between
`0` and `1`, and at `x = 1/2` sits at `y = 1.005 < 5/2`. So `e` passes through
that triangle's interior, `{a,b,c}` is not a face, and the segment serves no
triangle on either side.

**(c) Both its faces are bounded quadrilaterals.**

    above:  (0,0) --b-- (100/499, 500/499) --e-- (400/501, 505/501) --c-- (1,0)
    below:  (0,0) --b-- (-50/249, -250/249) --d-- (300/251, -245/251) --c-- (1,0)

The only line that could cut the upper face is `d`, which over `x ∈ [0,1]` has
`y ∈ [-1, -0.98]`; the only line that could cut the lower face is `e`, which over
`x ∈ [-0.21, 1.20]` has `y ≈ 1`. Neither does. **Neither side of this free
segment is unbounded.**

**(d) What this kills.** Reference data 8's "one face on a free segment is
unbounded" is proved by two row lookups in Kabanovitch's B (line 9 at position 1
in rows 4 and 5) and is a fact about B, not a theorem. T353's "free segments,
whose far side is unbounded" is refuted. T324's necessity condition and reference
data 30's eleven-of-eleven sweep both presuppose three-sided wedges beyond both
edges and therefore say nothing about a base where this configuration occurs.
Together with T340, `insertion-cap-53-generalizes-beyond-b` now has two
independent B-specific joints, not one.

**(e) What it does not kill.** Reference data 22 (`Y <= 6` for B) is untouched:
B's own free segments do have unbounded wedges beyond them, verified by lookup.
This widens the space of *other* 13-line optima, which is exactly reference data
22e's live question.

## Referee reference data 32: the rotational census above order 2, complete

Let a `k`-line arrangement be invariant under rotation `ρ` by `2π/n` about a
point `O`, `n > 2`. T345 did `n = 7` at `k = 14`; T346 generalized the stabilizer
argument and did the divisors of 18 and 20. This completes it and drops T346's
non-vertex-center hypothesis by splitting on the parity of `n`.

**(a) Even `n` is central symmetry.** `⟨ρ⟩` contains `ρ^{n/2}`, the 180-degree
rotation about `O`. So the arrangement is centrally symmetric and reference data
33 applies verbatim, whatever else `ρ` does. No residue argument is needed and
none is available in general, because the order-2 element supplies triangle
stabilizers of order 2 whenever a triangle has a vertex at `O`.

**(b) Odd `n` forces `n | k`.** A rotation fixing a line setwise must be the
180-degree rotation about a point of that line; for odd `n` there is no such
element, so no line is fixed and every line orbit has size exactly `n`.

**(c) Triangle stabilizers.** `H = Stab(T) ≤ Z_n` acts on `T`'s three vertices.
The kernel fixes three distinct points, so it is trivial and `H` embeds in `S_3`;
`H` is cyclic, so `|H| ∈ {1, 2, 3}`. `|H| = 2` needs a vertex fixed pointwise,
hence `O` a vertex of the arrangement, and needs `2 | n`. `|H| = 3` needs
`3 | n`, and then `T`'s three vertices are permuted cyclically, so `T` is
equilateral and centred at `O`. Orbit sizes are therefore `n`, `n/2`, `n/3` only.

**(d) The three open cases, odd `n`.**

    k=14   n | 14, n odd, n>2  =>  n = 7.   3∤7, 2∤7  =>  T ≡ 0 mod 7.
           54 mod 7 = 5.                                    DEAD
    k=18   n = 3 or 9.
           n=9:  3|9  =>  orbits 9 or 3  =>  T ≡ 0 mod 3.
                 94 mod 3 = 1.                              DEAD
           n=3:  orbits 3 or 1  =>  T ≡ s mod 3, s = #fixed. LIVE
    k=20   n | 20, n odd, n>2  =>  n = 5.   T ≡ 0 mod 5.
           117 mod 5 = 2.                                   DEAD

**(e) `C3` at `k = 18` is the only survivor anywhere, and it is sharply
constrained.** `18 = 3·6`, six line-orbits. A fixed triangle is equilateral,
centred at `O`, and its three lines form one whole line-orbit; three lines in
general position bound exactly one triangle, so each line-orbit supplies **at
most one** fixed triangle and `s <= 6`. `94 ≡ 1 mod 3` forces

    s = 1  or  s = 4

**one or four concentric equilateral faces**, each cut out by its own orbit of
three lines, each of the remaining `(94 - s)/3` orbits free. Nobody has looked at
this. It is the only rotationally symmetric family above order 2 still alive at
any open `k`.

**(f) `k = 20` is closed above order 2.** Odd orders die at (d); even orders die
at reference data 33, which at `k = 20` requires `d >= 9 + 3c`. Since `117` is
odd, even the mod-2 escape that keeps `54` and `94` alive under central symmetry
is unavailable in spirit — but the operative kill is the segment budget, not the
parity.

**(g) Scope.** This is about exact rotational symmetry of the whole arrangement.
It says nothing about reflections (T347's Case B, which is order 2 and not a
rotation) and nothing about asymmetric arrangements, where Kabanovitch's and
Bader's actual records live.

## Referee reference data 33: central symmetry needs `d > 3c` at all three open cases

**(a) The parallel tax.** Point reflection `(x,y) -> (2O - x, 2O - y)` sends
`y = mx + t` to `y = mx + (2b - 2am - t)`: same slope, and equal to the original
iff the line passes through `O`. So with `f` lines through `O`, the other `k - f`
split into `(k-f)/2` parallel pairs, `f ≡ k mod 2`, and `f >= 3` makes `O` a
concurrence of multiplicity `f` costing `f(f-2)` bounded segments by reference
data 25.

**(b) The optimum is `f = 2` at every open `k`.** Writing
`B = k(k-2) - 2p - f(f-2)·[f>=3] - 3c` with `p = (k-f)/2` and `c` the triple
points away from `O`:

    k=14   f=0: p=7, B=154-3c    f=2: p=6, B=156-3c
           f=4: p=5, B=150-3c    f=6: p=4, B=136-3c      max 156
    k=18   f=0: p=9, B=270-3c    f=2: p=8, B=272-3c
           f=4: p=7, B=266-3c                            max 272
    k=20   f=0: p=10, B=340-3c   f=2: p=9, B=342-3c
           f=4: p=8, B=336-3c                            max 342

**(c) The requirement.** `3T <= B + d` (T288's identity, reference data 27a) with
the target counts gives

    k=14   3T = 162   d >= 6 + 3c      d/c >= 3 + 6/c
    k=18   3T = 282   d >= 10 + 3c     d/c >= 3 + 10/c
    k=20   3T = 351   d >= 9 + 3c      d/c >= 3 + 9/c

**Every one is `d > 3c`, which is reference data 29e's decision rule exactly.**
Against `d <= 4.5c` (reference data 29d) this forces `c >= 4` at `k=14`,
`c >= 7` at `k=18`, `c >= 6` at `k=20`; at `k=14, c=4` it forces `d = 18` on the
nose, i.e. **equality in `d <= 4.5c`** — every triple point a full wrap and the
break segments forming a 3-regular graph on them. Against the observed ceiling
`d <= 2c`, all three are dead: `2c < 3c + 6` for every `c >= 0`.

**(d) Consequences.** T347's "central symmetry is dead at `T <= 52`" is the
`c = 0` corner of this and T348 was right to demand the scope. But the correct
statement is stronger and more useful than either: **central symmetry is not
independently dead, it is dead exactly when the concurrence program is dead, and
alive exactly when it is alive.** By reference data 32a the same holds for every
even rotational order at every open `k`. Three separate programs — chained
concurrence, central symmetry, even-order rotation — reduce to one number, and
the observed value of that number is `2c` across every object on record.

**(e) Off-center concurrences come in pairs.** `P` and `2O - P` are both triple
or both ordinary, so `c` is even away from `O`, consistent with the `c >= 4`,
`c >= 6` thresholds above but not with `c = 7` at `k = 18`, which must therefore
be `c >= 8` there. T348 stated the pairing correctly and did not use it.

---

## Referee reference data 34: the corpus automorphism census, and the `k = 21` `C3` template

**(a) Method.** A table automorphism is a permutation `pi` of the lines with
`row(pi(l)) = pi(row(l))` up to reversal. Fixing the image of one line
determines `pi` completely (read `row(l_1)` against `row(pi(l_1))` entrywise),
so there are only `2k` candidate maps per table; test each against all `k` rows.
Tables with nested entries (the six concurrence-bearing tables of reference data
23a) and tables with unequal row lengths (`kobon_4`, `kobon_14_53tri`,
`kobon_16_72tri`, `kobon_18_93tri`, `kobon_20_116tri`, `kobon_22_143tri`, all of
which have parallels) are excluded or have no automorphism. Verifier run:
`kobon.table.triangles` plus `kobon.table.labels` over `kobon.corpus.entries()`.

**(b) Every fixed-point-free rotational automorphism in the corpus.**

    key                       k    order   action          T      s   line-orbits
    kobon_9_3_rot_symmetry    9    3       l_i -> l_{i+3}  21     0   3
    pentagram_5_rot_symmetry  5    5       l_i -> l_{i+1}  5      0   1
    kobon_15_5_rot_symmetry   15   5       l_i -> l_{i+3}  65     0   3
    kobon_21_133tri_1         21   3       l_i -> l_{i+7}  133    1   7
    kobon_21_133tri_2         21   3       l_i -> l_{i+7}  133    1   7
    kobon_27_225tri_2         27   3       l_i -> l_{i+9}  225    0   9

`s` is the number of triangles fixed setwise. **Every action is a label shift by
`k/n`**, the signature of a genuine rotation acting on lines indexed in slope
order, and **every row satisfies `T ≡ s (mod n)`**: `21 ≡ 0`, `5 ≡ 0`, `65 ≡ 0`,
`133 ≡ 1`, `225 ≡ 0`. Reference data 32's residue rule is confirmed on six
independent objects and `s <= 1` holds in all six, as T357's lemma requires.
Three of the six are at odd `k` and all six meet the published bound.

Also found, and not rotational: order-2 automorphisms with exactly one fixed
line at `kobon_7`, `kobon_9_3_rot_symmetry`, `kobon_13_m_sym_47tri` (this is B's
mirror `i -> 15-i`), `kobon_19_107tri`, `kobon_21_133tri_3`, `kobon_25_191tri`.
`kobon_11_32tri`, `kobon_17_85tri` and `kobon_23_161tri` are asymmetric.

**(c) The `k = 21` template, in full.** `kobon_21_133tri_1`, order-3 shift
`l_i -> l_{i+7}`, seven line-orbits `{i, i+7, i+14}` for `i = 1..7`. `p = 0`
(all rows length 20), `c = 0` (no nested entries), `B = 21 · 19 = 399`,
`3T = 399`, so **`f = 0` and every one of the twenty-one lines carries all 19 of
its bounded segments as triangle sides.** Triangle census by orbit pattern:

    (3)      one triple inside a single line-orbit   1 triangle    1 slot   = s
    (1,2)    two lines from one orbit, one from another  39 triangles  13 slots
    (1,1,1)  three lines from three distinct orbits      93 triangles  31 slots
                                                       ---           ---
                                                       133           45

The fixed triangle is `{2, 9, 16}` — one whole line-orbit, exactly as reference
data 32e requires. 45 of the 448 available slots are used
(`7 + 126 + 315 = 448`, and `1330 = C(21,3) = 7 + 378 + 945`).

**(d) What this does to the `k = 18` question.** T404 defines `d_i = 16 -`
(per-line triangle count of orbit `i`) and derives `T = 96 - Σd_i`, so `T = 94`
needs `Σd_i = 2` over six orbits. `kobon_21_133tri_1` has `Σd_i = 0` over seven
orbits, with `s = 1`, under a genuine order-3 line-orbit structure. **The joint
condition T404 called "strictly harder than any single line being saturated in
isolation" is realized in the corpus, with less slack than `k = 18` is
allowed.** This does not show 94 is reachable; it removes the only structural
reason anybody has offered for thinking it is not.

**(e) Caveat, stated because the literature packet demands it.** These are
*table* automorphisms. A combinatorial order-`n` symmetry of a table need not be
induced by a geometric rotation of a straight-line realization; that is the
stretchability question, complete for the existential theory of the reals. The
label-shift structure in (b) is strong evidence and not a proof. `kobon_9_3` and
`kobon_15_5` are titled as rotationally symmetric by their source;
`kobon_21_133tri_1/2` and `kobon_27_225tri_2` are not, and their symmetry is
reported here for the first time in this project.

---

## Referee reference data 35: the concurrence ladder in `c` does not terminate

**(a) The window is never empty.** Reference data 33c gives the requirement and
reference data 29d gives the ceiling:

    k=14   6 + 3c <= d <= 4.5c    nonempty iff  1.5c >= 6    c >= 4
    k=18  10 + 3c <= d <= 4.5c    nonempty iff  1.5c >= 10   c >= 7, so c >= 8 by 33e
    k=20   9 + 3c <= d <= 4.5c    nonempty iff  1.5c >= 6    c >= 6

For every `c` at or above these thresholds the window is nonempty, and it widens
linearly (`1.5c - 6`, `1.5c - 10`, `1.5c - 9`). **There is no largest `c` to
check.** A case analysis that kills `c = 4`, then `c = 6`, then `c = 8` never
finishes. Only a theorem bounding `d/c` strictly below 3, or a single object
above it, closes any of these.

This is the arithmetic reason the T358-T368 arc could not have succeeded, and it
is why agenda item 4 has been the whole of the question since T329.

**(b) Equality is required only at the bottom rung.** `d = 4.5c` forces
`|S_1| = 3c`, `|S_2| = 1.5c` and `d_P = 6` at every point, hence a 3-regular
bridge graph. That happens **only** where the two bounds meet:

    k=14   c = 4 only     k=18   c = 8 gives d in [34,36], not forced
    k=20   c = 6 only

So at `k = 14`, `c = 4` forces `K4` and dies (reference data 36). At `c = 6` the
window is `d ∈ [24,27]` and the bridge graph needs only `|S_2| >= d - 3c = 6`
edges on six vertices, subject to planarity (`<= 12`). **The triangular prism and
`K_{3,3}` were never required objects at `c = 6`; T360, T362, T364 and T365 spent
four turns on the equality case of a rung that does not have one.**

**(c) The object nobody has drawn: the centrally symmetric hexagonal ring.**
`k = 14`, `c = 6`, `f = 2` lines through `O`, `p = 6` parallel pairs,
`B = 138`, target `d = 24`. Six triple points in three antipodal pairs about `O`,
bridged in a 6-cycle: `|S_2| = 6`, `|S_1| = 18 = 3c`, `d = 24`,
`Σ_P d_P = |S_1| + 2|S_2| = 30`, so `d_P = 5` at each point. Feasibility of the
local picture: six rays at each triple point, two carrying bridges to the cycle
neighbours, and three of the remaining four doubled and ending at ordinary
crossings. Reference data 29c forbids two cyclically adjacent ordinary doubled
rays; with bridges at ray positions 1 and 3, the set `{2, 4, 6}` is pairwise
non-adjacent, so `d_P = 5` clears the non-adjacency lemma. The 6-cycle is planar
and has a crossing-free convex drawing, so reference data 36b does not touch it.
**Nothing on record rules this out and nobody has written a coordinate.**

---

## Referee reference data 36: `K4` and `K_{3,3}` are impossible as bridge graphs

**(a) The four-point dichotomy (T358, T359, referee-verified).** A bridge between
two triple points `P, Q` is the bounded segment of the arrangement line through
them with no other line crossing it. Four points in general position admit
exactly two order types.

- *Convex position `ABCD`.* The diagonals `AC` and `BD` cross at a point strictly
  interior to both segments. Each diagonal lies on an arrangement line, so each
  cuts the other: two of the six connectors die.
- *One interior.* Let `D` be interior to triangle `ABC`. The ray from `A` through
  `D` exits through side `BC`, strictly between `B` and `C`, because `D` is
  interior. The line `AD` is an arrangement line (it carries the bridge `AD`), so
  segment `BC` is cut. Symmetrically for `BD` against `CA` and `CD` against `AB`:
  three of the six connectors die.

There is no third order type, so **all six pairwise connectors can never
simultaneously be uncut bridges.** `K4` is unrealizable as a bridge graph on any
four points, in any position. Verified against reference data 28, where
`c: y = 4 - 3x` meets `M_1: y = 0` at `x = 4/3 ∈ (0,4)`, cutting the would-be
bridge `Q_0 Q_2` exactly as the general argument predicts.

**(b) Planarity (T361, referee-verified).** Two bridge segments crossing at a
point interior to both disqualifies both, since each lies on an arrangement line
passing through the other's interior. So the bridge graph, drawn with literal
straight segments between the triple points, must be **crossing-free**. A
crossing-free straight-line drawing is a planar embedding. Hence **any
non-planar graph is unrealizable as a bridge graph, on any point set, in any
position** — in particular `K_{3,3}`, by Kuratowski. Note that this does *not*
kill `K4`, which is planar; `K4` dies on (a). Both mechanisms were needed.

**(c) Consequence, drawn correctly at T363.** Central symmetry at `k = 14` with
`c = 4` requires `d >= 6 + 3c = 18` and permits `d <= 4.5c = 18`, so `d = 18`
exactly, so equality in reference data 29d, so a 3-regular bridge graph on four
vertices, so `K4`, so impossible. **`c = 4` is dead at `k = 14` by proof, not by
the observed ceiling.**

**(d) Scope, against T365, T367 and T368.** (a), (b) and (c) kill exactly one
value of `c` at one `k`. They say nothing about `c = 6`, where equality is not
required (reference data 35b), and nothing about `c >= 8`, which nobody has
mentioned. The two prism embeddings killed at T362 and T364 are two embeddings
of one graph that was never required. **"Central symmetry at `k = 14` is dead" is
not a consequence of anything in this section.**

---

## Referee reference data 37: `table.validate` does not validate

**(a) What it checks (T441, referee-verified from source).** `kobon/table.py`'s
`validate` raises only on: a line listing itself, a label out of range `[1, k]`,
and a reciprocity failure (`i` lists `j` but `j` does not list `i`). That is the
whole function. There is **no** rank-3 consistency test, no face-adjacency
condition, no sweep or walk condition, no stretchability check of any kind.

**(b) The demonstration (T441).** Five random shuffles of row 14, appended to
Kabanovitch's `B` with 14 tail-appended in every old row, all pass `validate`,
returning triangle counts `48, 48, 47, 47, 47` — none matching the identity
order's 53. `validate` has zero discriminating power over that space.

**(c) `triangles` is local (T441, referee-verified).** For each candidate triple
it asks only whether some other line's rank data places it between two of the
three crossings. It is the iff test of reference data 2, applied inside whatever
table it is handed. It certifies a triple inside a table; it never certifies the
table. This was already a standing rule; T441 is the first turn to check that
`validate` does not fill the gap.

**(d) The consequence, and T442's correct reading of its direction.** Every
combinatorial table computation in this project ranges over a **superset** of the
realizable tables. Therefore:

- An **upper bound** computed by exhaustion over that space is still a valid
  upper bound over realizable tables. T440's cap of six eligible pairs, and my
  own two-sided-split cap of 53 (reference data 38d), survive intact.
- An **existence** claim does not transfer at all. A table that passes
  `validate` and reports a high count is a candidate, not an object.

T442 stated this in the turn after T441 raised it, conceded exactly the word
that was unearned ("closed", "period"), and kept exactly the part that survives.

---

## Referee reference data 38: single-line extension, priced exactly

**(a) The face lemma (T437, referee-verified).** Every bounded face of a line
arrangement is an intersection of half-planes, hence convex, and a straight line
meets a convex region in at most one segment. Line `k+1` has `k-1` bounded
pieces between its `k` crossings, and each piece is a maximal segment crossing no
other line, so it lies inside a single face of the old arrangement — and **no two
pieces lie in the same face**, since a straight line cannot leave and re-enter a
convex region. So the pieces visit `k-1` distinct faces.

Per face type, with `D` = old triangles destroyed and `G` = new triangles gained:

- **Triangular face.** The old triangle dies (`D+1`); the cut isolates one corner
  bounded by two old sides and the new line (`G+1`). Net contribution to `G - D`
  is **at most 0**, never positive.
- **Bounded non-triangular face.** `D+0`; `G+1` only if the cut isolates a
  triangular corner, `G+0` if it splits opposite sides.
- **Unbounded face.** `D+0`, `G+0` or `+1`.

Hence `G - D <=` the number of non-triangular faces visited. **`D` is not a dial
that buys slack**, which corrects T436's `(D,G)` framing and subsumes T435's
"11 of 13 crossings must be ray-crossings" as the `D = 0` corner.

**(b) The face inventory (T438, referee-verified).** For a simple `k`-line
arrangement, `1 + k + C(k,2)` faces total, `C(k-1,2)` bounded. At `k = 13`: 92
total, 66 bounded, 26 unbounded, and `66 - 47 = 19` bounded non-triangular. The
zero-cost pool is `92 - 47 = 45`, not 19 — T438's correction of T437 is right.
**T438's wedge-apex mechanism, however, needs angular data the corpus does not
carry**, which T439 established (`table.positions` returns bare per-line ranks;
`corpus.by_key()` has no coordinate field on any of 27 entries; `kobon/` has no
straightening module) and T440 conceded after re-running the census itself.

**(c) The eligible-pair operator (T440, referee-verified).** Append label `k+1`
to the tail of every old row — line `k+1` crosses every old line beyond its
existing span, so `D = 0` by (a). A pair `{a,b}` is **eligible** if `{a,b,k+1}`
is a triangle when `a` and `b` are adjacent in row `k+1`. On Kabanovitch's `B`
all 78 pairs give exactly six: `{1,2},{3,4},{5,6},{7,8},{9,10},{11,12}`, a
perfect matching on lines 1-12 with line 13 eligible for nothing. Total 53, all
47 originals intact. I re-ran the full 78-pair scan and reproduce it exactly.

**(d) The concurrency lever, closed — including the case nobody ran.** A cevian
split at triangle `{a,b,c}` (line 14 through `V(a,b)`, crossing side `c`) loses
the original, gains `{a,c,14}` and `{b,c,14}`, and loses every eligible pair
containing `a`, `b` or `c`. Tallies, all verified:

    T444  V(2,3),  no split          51
    T444  V(1,13), no split          52
    T445  {1,2,6}  via line 6        52
    T445  {1,13,9} via line 9        52
    T446  two disjoint splits        50

Breaking even requires the split triangle to be `{a, P(a), 13}` for one of the
six pairs; T445 checked all six and I re-ran it — `False` six times.

**The untested shape was the two-sided split**: line 14 through `V(a,b)` entering
the flanking triangles in **both** opposite sectors, `D = 2, G = 4`, the only
arithmetic that could have netted positive. **Referee run: all 63 vertices of `B`
carrying two flanking triangles, 120 randomized row-14 orderings each. Maximum
53, never 54.** The mechanism is exact: **not one of the 63 has `(a,b)` among the
six eligible pairs**, so `a` and `b` always spend two distinct pairs, and the
best case (`(a,b)` with `b = 13`, thirds forming an eligible pair — five such
vertices exist) gives `47 - 2 + 4 + 4 = 53` and ties.

**(e) Scope.** All of (c) and (d) are computations in the space `validate`
accepts (reference data 37), so they are upper bounds on the realizable subset,
which is the direction that matters. **Kabanovitch's `B` cannot be extended by a
fourteenth line to 54, by any tail insertion, any single concurrency, any cevian
split, one-sided or two-sided, or any pair of disjoint splits.**

---

## Referee reference data 39: the centrally symmetric ring, bounded and killed at `k = 14`

Setting: `c = 2n` triple points at the vertices of a **convex** centrally
symmetric `2n`-gon about `O`, consecutive vertices joined by bridges (the
polygon's `2n` edges), each vertex carrying exactly three lines — its two bridge
lines and one more. `f` lines pass through `O`.

**(a) Every point caps at `d_P <= 5`.** Six rays; two are bridges. The remaining
four are candidates for ordinary doubling, and reference data 29c forbids two
cyclically adjacent ordinary doubled rays. Four vertices of a 6-cycle cannot be
pairwise non-adjacent, so at most three of the four qualify. `d_P <= 2 + 3 = 5`.
Reference data 28's `d_P = 6` needs three break rays at the point; a ring vertex
has two.

**(b) The interior-cone theorem, and the `C`-type cap of 4.** At vertex `C` with
bridges to `B` and to `-A`, the six rays are cyclically
`toB, to(-A), away_B, away_{-A}` interleaved with the third line's antipodal pair
`l+, l-`. There are exactly two insertions:

- `l+` in the arc `(toB, to(-A))` — **the interior cone** — and `l-` in the
  antipodal arc. Cyclic order `toB, l+, to(-A), away_B, l-, away_{-A}`; the
  conflict graph on `{away_B, away_{-A}, l+, l-}` is the path
  `away_B - l- - away_{-A}` plus isolated `l+`. Independent set **3**, so
  `d_P = 5` is available.
- `l+` in `(to(-A), away_B)` and `l-` in `(away_{-A}, toB)` — the **supporting**
  directions, the ones that keep the line out of the polygon. Cyclic order
  `toB, to(-A), l+, away_B, away_{-A}, l-`; the conflict graph is the path
  `l+ - away_B - away_{-A} - l-`. Independent set **2**, so `d_P <= 4`.

T453 established this dichotomy and I have re-derived both cases. The step T453
did not have:

> **A ray from a vertex into the interior of a simple polygon leaves through the
> boundary** — through the relative interior of a non-incident edge, or through
> another vertex. The edges are the bridges. So a third line at `C` whose ray
> enters the interior cone either **cuts a bridge** (destroying it, so `|S_2|`
> drops and the ring is no longer a ring) or **passes through a second vertex**
> (making that vertex multiplicity 4, cost `m(m-2) = 8` by reference data 18,
> and voiding the design's own degree cap).

The unique escape is a **main diagonal** `P_i(-P_i)`, whose interior ray exits
exactly at the antipodal vertex, which is a design vertex rather than a fresh
incidence. There are `n` main diagonals; every line through `O` that is not one
of them cuts two bridges (T423, proved by convexity plus the fact that point
reflection fixes such a line and swaps `P_i` with `-P_i`); so all `f` central
lines are main diagonals and `f <= n`. Each serves two antipodal points, so
`2f` points are diagonal-served and `2n - 2f` are `C`-type at `d_P <= 4`.

**(c) The ring bound.** `Σ_P d_P = |S_1| + 2|S_2|` and `d = |S_1| + |S_2|`, so
`d = Σ_P d_P - 2n`. With (a) and (b),

    Σ_P d_P <= 5(2f) + 4(2n - 2f) = 8n + 2f
    d       <= 6n + 2f
    d / c   <= 3 + f/n,     f even (parity `k = f + 2p`),  f <= n.

**This is above 3 whenever `f > 0`, and it is the only family anyone has proposed
for which the proven ceiling clears reference data 29e's decision rule.** Maximum
`d/c = 4`, attained only when `n` is even and every main diagonal is central.

**(d) `k = 14` is dead.** `c = 6`, `n = 3`, so `f` even and `f <= 3` gives
`f <= 2`, `d <= 6(3) + 2(2) = 22`. Reference data 33 requires `d >= 6 + 3c = 24`
for central symmetry at `k = 14` with `c = 6`. **`22 < 24`. The centrally
symmetric hexagonal ring cannot reach `T = 54`.** This is the object agenda item
2 assigned at T405, and it was never reachable.

**(e) Numerical shadow, referee run.** Five distinct convex centrally symmetric
hexagons — T446's `A=(3,0), B=(1,2), C=(-2,1)`; T430's `(5,0),(3,4),(-2,5)`; a
wide-`C` variant `(4,0),(1,3),(-3,1)`; a near-regular `(6,1),(2,5),(-5,2)`; a
flat `(10,0),(9,1),(-1,2)`. For each, 4836 rational slopes through `C` (numerator
`-200..200`, denominator `1..19`, coprime, trap slopes excluded), tested for
strict interior crossings against the four bridges not at `C` and both used
diagonals, and for a pairwise non-adjacent 3-subset of the four candidate rays:

    hexagon           clean-only   IS3-only   both
    T446                     79       4757       0
    T430                    222       4614       0
    wide-C                   59       4777       0
    near-regular            307       4529       0
    flat                     35       4801       0

The two sets are disjoint in every case, and the reason is (b): the clean slopes
are exactly the supporting directions, the `IS3` slopes are exactly the interior
cone. **This confirms T453's finding is not an artifact of its hexagon**, which
is the question T453 correctly flagged as open.

**(f) The other open cases, priced by (c).** `c = 6` at `k = 20` needs
`d >= 9 + 3c = 27`, `d/c >= 4.5`, ring ceiling `11/3` — dead. `c = 8` at `k = 18`
needs `d >= 10 + 3c = 34`, ring ceiling `6(4) + 2(4) = 32` — dead. `c = 8` at
`k = 20` needs 33 against 32 — dead. `c = 10` at `k = 20` needs 39, `n = 5`, `f`
even so `f <= 4`, ceiling 38 — dead. **The first ring instance not killed by (c)
is `k = 20, c = 12, n = 6, f = 6`: requirement 45, ceiling 48.**

**(g) Scope, stated because it is the hole.** (a)-(f) assume the ring is
**convex**. At a reflex vertex the interior angle exceeds 180 and the arc
classification in (b) changes; the "ray into the interior must leave through an
edge or a vertex" step survives by Jordan, but the identification of the viable
arc with the interior cone does not. T406 perturbed one hexagon to non-convexity
and found four bridge-extension cuts appear immediately at the reflex pair; that
is one instance, not a theorem. **A non-convex centrally symmetric ring is the
only surviving form of this family at `k = 14`.**

---

## Referee reference data 40: the tail-append census, corpus-wide

> **Superseded in part by reference data 41 (T469).** The "eligible" counts below
> are computed in the row directions the corpus happens to store, and row
> direction is a convention. Part (a)'s `maxdeg = 1` is a one-line consequence of
> "last is a function" and did not need twelve tables. **Part (c)'s counterweight
> — the misses of 2 and 3 at `k+1 = 8, 12` — is retracted: under free orientation
> both are misses of exactly one.** Read 41e in place of 40c.

**Method (referee run).** For every corpus table that is concurrence-free and
parallel-free (no nested entries, every row of length `k-1`), append label `k+1`
to the tail of all `k` rows, and count eligible pairs by reference data 38c: for
each of the `C(k,2)` pairs, place it adjacent at the head of row `k+1` and ask
whether `{a, b, k+1}` is a triangle. This is the first corpus-wide **operator**
run in this project; every previous census was per-object.

    table                       k     T   eligible  maxdeg   T + pairs   KNOWN k+1
    triangle_3_rot_symmetry     3     1      1        1          2         2
    pentagram_5_rot_symmetry    5     5      2        1          7         7  closed
    kobon_7                     7    11      2        1         13        15  closed
    kobon_9_3_rot_symmetry      9    21      4        1         25        25  closed
    kobon_11_32tri             11    32      3        1         35        38  closed
    kobon_13_m_sym_47tri       13    47      6        1         53        53  OPEN, UB 54
    kobon_15_5_rot_symmetry    15    65      7        1         72        72  closed, at bound
    kobon_17_85tri             17    85      8        1         93        93  OPEN, UB 94
    kobon_19_107tri            19   107      9        1        116       116  OPEN, UB 117
    kobon_21_133tri_1/2/3      21   133     10        1        143       UB at 22 is 144

**(a) The eligible-pair set is always a perfect matching.** `maxdeg = 1` in every
one of the twelve runs — no line is eligible with two partners. For
`k in {3,5,9,13,15,17,19,21}` the count is exactly `(k-1)/2`, a matching leaving
one line unpaired. `k = 7` (2 instead of 3) and `k = 11` (3 instead of 5) are the
exceptions; both bases are odd optima but neither yields the known even value.

**(b) All three open cases are `odd optimum + (k-1)/2`, one short of the bound.**
`47 + 6 = 53` at `k = 14`, `85 + 8 = 93` at 18, `107 + 9 = 116` at 20 — each the
best-known value, each exactly one below the tightest published upper bound.
**The missing triangle in each open case is exactly the unmatched line.**

**(c) The counterweight, which cuts against the pattern.** At `k+1 = 6, 10, 16`
the operator hits the even upper bound on the nose, but at `k+1 = 8` and `12` it
misses by 2 and 3 and **those cases are closed at their bounds anyway**, by
constructions that are not extensions of the odd optimum. So (b) is not evidence
that `N(14) = 53`. It is evidence that the three open cases share one mechanism
and that closing any of them requires beating this operator, which reference data
38d now shows a single line cannot do from Kabanovitch's `B`.

**(d) What is not checked.** Whether the `(k-1)/2` matching count is forced, and
what distinguishes `k = 7` and `k = 11`. Whether `kobon_17_85tri` and
`kobon_19_107tri` behave under concurrency exactly as `B` does under reference
data 38d — the two-sided-split argument used `B`'s specific 63 two-flanking
vertices and has not been run at 17 or 19. Both are cheap and both are on the
agenda.

---

## Referee reference data 41: tail-append, closed over every orientation

**Corrects reference data 40, which is mine.** Everything below is a referee run.

**(a) `mutual-last ⟹ eligible` (T468's half, restated).** If `b` is the last
entry of row `a` and `a` the last entry of row `b`, then tail-appending `k+1` to
every row puts `k+1` immediately after `b` in row `a` and immediately after `a`
in row `b`, and placing `a, b` adjacent at the head of row `k+1` puts nothing
between them along `k+1`. All three sides of `{a, b, k+1}` are uncut by
construction. No case analysis on the rest of the ordering.

**(b) `eligible ⟹ mutual-last` (the converse, which T468 left open).** `k+1` is
last in row `a` by construction. For the segment of `a` between `V(a,b)` and
`V(a,k+1)` to carry no crossing, `b` must sit immediately before `k+1`, i.e. `b`
is the last entry of the **original** row `a`. Symmetrically `a` is the last
entry of the original row `b`. Two clauses, no search. **So eligibility is
exactly the 2-cycle relation of the last-crossing function**, and T468's
7-for-7 set equality is a theorem.

**(c) A mutual-last pair has triangle-degree at most 1, combinatorially.** A
triangle `{a,b,c}` requires `b` and `c` adjacent in row `a` and `a` and `c`
adjacent in row `b`. If `b` is last in row `a`, `c` must be `a`'s second-to-last;
if `a` is last in row `b`, `c` must be `b`'s second-to-last. `c` is therefore
**unique**, and if the two second-to-lasts disagree there is no triangle at all.
No geometry, no unbounded face, no sector count. **Verified: 106 mutual-last
pairs across every concurrence-free corpus table, zero degree above 1, and in
every case with a triangle the third line is exactly both second-to-lasts.**
This is what T466 and T467 were reaching for; their published argument accounts
for the outward and inward sectors at `V(a,b)` and is silent on the two mixed
sectors, of which there are two, because two lines through a point make four.

**(d) The orientation sweep, and the ceiling.** A table row lists a line's
crossings in one of the two directions along it; reversing a row preserves all
adjacencies, hence every triangle (verified: `T = 11` and `T = 32` unchanged
after reversal), and changes which entry is "last". The stored corpus direction
is a convention, not data. Over all `2^k` orientations the eligible set is a
matching in

    H  =  { {a,b} : b in ends(a) and a in ends(b) },   ends(i) = {row_i[0], row_i[-1]}

and every vertex of `H` has degree at most 2, so `H` is a disjoint union of paths
and cycles and its maximum matching is at most `floor(k/2)`. **This is a hard
ceiling for any table at any `k`, realizable or not.** Computed:

    table                     k    T   stored elig   max over orientations   (k-1)/2
    pentagram_5_rot_symmetry  5    5        2                 2                 2
    kobon_7                   7   11        2                 3                 3
    kobon_9_3_rot_symmetry    9   21        4                 4                 4
    kobon_11_32tri           11   32        3                 5                 5
    kobon_13_m_sym_47tri     13   47        6                 6                 6
    kobon_15_5_rot_symmetry  15   65        7                 7                 7
    kobon_17_85tri           17   85        8                 8                 8
    kobon_19_107tri          19  107        9                 9                 9
    kobon_21_133tri_1/2/3    21  133       10                10                10

`maxmatch = (k-1)/2` in all eleven, and **at `k = 13, 17, 19` the stored
orientation already attains the maximum.** Reorienting `kobon_7` to its optimal
matching and re-running the full eligibility test gives 3 pairs with `T` still
11; `kobon_11_32tri` gives 5 with `T` still 32. **Therefore no position of the
appended line yields more than `T + (k-1)/2`, and the tail-append route tops out
at 53, 93 and 116. It cannot reach 54, 94 or 117.** The bound is computed over
the space `table.validate` accepts, which by reference data 37 and T442 is the
valid direction for an upper bound.

**(e) The corrected census, replacing reference data 40(c).** With orientation
free, the operator's value is `T + (k-1)/2` at every odd corpus base:

    k+1 =  6    5 +  2 =   7  = N(6)      exact
    k+1 =  8   11 +  3 =  14, N(8)  = 15  one short
    k+1 = 10   21 +  4 =  25  = N(10)     exact
    k+1 = 12   32 +  5 =  37, N(12) = 38  one short
    k+1 = 14   47 +  6 =  53, UB    = 54  one short
    k+1 = 16   65 +  7 =  72  = N(16)     exact
    k+1 = 18   85 +  8 =  93, UB    = 94  one short
    k+1 = 20  107 +  9 = 116, UB    = 117 one short
    k+1 = 22  133 + 10 = 143, UB    = 144 one short

**In every closed even case the operator lands exactly on the truth or exactly
one below it, never further.** Reference data 40(c) claimed misses of 2 and 3 at
`k+1 = 8, 12` and used them as evidence against reading the 14/18/20 pattern as
informative. That was an artifact of the stored row directions and I retract it.
The corrected data supports two readings with equal precedent — the open cases
behave like `6, 10, 16` (`N = 53, 93, 116`) or like `8, 12` (`N = 54, 94, 117`) —
and is **not** evidence against reaching the bound.

**(f) The parity asymmetry, new.** The same operator on the five even-`k` corpus
records, all of which are concurrence-free with parallel pairs:

    kobon_14_53tri   k=14  T= 53  maxmatch  7 ->  60   N(15) = 65   short by 5
    kobon_16_72tri   k=16  T= 72  maxmatch  8 ->  80   N(17) = 85   short by 5
    kobon_18_93tri   k=18  T= 93  maxmatch  9 -> 102   N(19) = 107  short by 5
    kobon_20_116tri  k=20  T=116  maxmatch  9 -> 125   N(21) = 133  short by 8
    kobon_22_143tri  k=22  T=143  maxmatch 11 -> 154   N(23) = 161  short by 7

**Even-to-odd, the operator misses by 5 to 8 every time.** The odd-to-even
near-miss of (e) is a parity phenomenon, not a general fact about extending a
record. Continuing (e) upward: `k = 23, 25, 27` give 172, 203, 238 against even
bounds 173, 205, 239 — one, two, one short.

**(g) Structural note on the corpus.** Every odd-`k` corpus record from 5 to 27
is simple: no parallels, no concurrences. Every even-`k` record from 14 to 22 is
concurrence-free **with** parallel pairs — `kobon_14_53tri` has classes
`{1,2},{3,4},{7,8}` (`p = 3`, `f = B - 3T = 3`), `kobon_18_93tri` has
`{1,2},{7,8},{13,14}` (`p = 3`, `f = 3`), and 16, 20, 22 each have a single pair.
The even records at 4 through 12 use concurrences instead. **Do not rederive
`2p + 3c <= 6` from this**: it is `k14-pc-enumeration-2p-plus-3c-leq-6`, refuted
at T280, because `3T <= B` fails at a concurrence (reference data 23).

**(h) What is not checked.** Whether an orientation attaining `maxmatch` is
induced by an actual direction in the plane — a real appended line must be
"beyond" every line in one common direction `u`, which allows only `2k` of the
`2^k` orientations. This does not weaken (d), which is an upper bound over a
superset, and it does mean the `k = 7` and `k = 11` gains in (e) may not be
geometrically realizable. It would matter only to someone trying to **achieve**
`(k-1)/2` at a base where the stored orientation falls short, which is not the
case at 13, 17 or 19.

---

## Table

| slug | k | status | evidence | opened | last touched |
|---|---|---|---|---|---|
| `tail-append-caps-at-t-plus-half-k-over-all-orientations` | 14/18/20 | **SETTLED (referee), PROOF + verifier run** | Reference data 41. `eligible ⟺ mutual-last` in both directions (T468 forward, referee converse). Mutual-last pairs are 2-cycles of a function, hence vertex-disjoint, so `\|eligible\| <= floor(k/2)`, for any table at any `k`. Over all `2^k` row orientations the achievable count is the maximum matching of `H = {{a,b} : b in ends(a), a in ends(b)}`, a graph of max degree 2; **computed on all eleven concurrence-free corpus tables it equals `(k-1)/2` every time, and at `k = 13, 17, 19` the stored orientation already attains 6, 8, 9.** Reorienting `kobon_7` gives 3 (from 2) and `kobon_11_32tri` gives 5 (from 3), `T` preserved in both. **Therefore tail-append tops out at 53, 93, 116 and cannot reach 54, 94, 117.** Upper bound over the space `validate` accepts, which reference data 37 says is the valid direction. | T454 | T469 |
| `eligible-pair-degree-at-most-one` | all | **SETTLED (referee), PROOF, corrects T466's route** | Reference data 41c. A triangle `{a,b,c}` needs `b,c` adjacent in row `a` and `a,c` adjacent in row `b`; if `b` is last in row `a` and `a` last in row `b`, `c` is forced to be both second-to-lasts, hence unique. Purely combinatorial. **T466's published argument covers the outward and inward sectors at `V(a,b)` and never mentions the two mixed sectors — two lines through a point make four sectors, not two — and T467 conceded in the same two-wedge language.** Conclusion true, route incomplete. Verified on all 106 mutual-last pairs in the corpus: degree never above 1, third line always both second-to-lasts. | T466 | T469 |
| `centrally-symmetric-hexagon-at-most-one-reflex-pair` | 14 | **SETTLED (referee-verified), PROOF, closes reference data 39's gap** | T462. Point reflection is orientation-preserving and negates both edge vectors flanking a turn, so `θ_{i+3} = θ_i`; `Σθ_i = 2π` for a simple closed CCW curve; so `θ_1+θ_2+θ_3 = π` with each `θ_i ∈ (-π,π)`; two negatives force the third above `π`, impossible. **At most one antipodal reflex pair, never two adjacent reflex vertices.** I checked every step. T462's 28,561-candidate grid search, correctly labelled "the theorem's shadow, not the proof". T463 then built the stronger test — real non-adjacent segment-intersection simplicity, CCW enforced after publishing the ~50% orientation artifact from its own first pass, and **every adjacent pair in the 6-cycle** rather than three representatives — 4976 + 5120 valid hexagons, zero exceptions. Combined with T461's reflex-continuation mechanism this fills the only stated gap in `hexagonal-ring-impossible-at-k14`. | T461 | T469 |
| `hexagonal-ring-impossible-at-k14` | 14 | **SETTLED (referee), PROOF, gap now closed** | Reference data 39 plus the row above. Every ring vertex caps at `d_P <= 5`; a vertex whose third line is not a main diagonal caps at `d_P <= 4`, because the only ray configuration admitting 5 puts a ray into the interior cone, and a ray from a vertex into a simple polygon's interior leaves through a non-incident edge (cutting a bridge) or another vertex (multiplicity 4). T423 forces every central line to be a main diagonal, `f <= n = 3`, parity forces `f` even, so `f <= 2` and at least two of six points are `C`-type. `Σd_P <= 28`, `d <= 22 < 24`. **The convexity assumption is now unnecessary: T461's reflex-continuation mechanism plus T462's turning-angle theorem cover the non-convex case, which has exactly one topological shape.** Dead by two, in every shape. **Still not gold: one family, one `k`.** | T405 | T469 |
| `bridge-split-nets-positive-refutes-t457-pricing` | all | **REFUTED (SILVER), T457 by T458, conceded T459** | T457: a bridge split is "priced at net <= 0 unless a single new line manages to make triangles on both resulting pieces at once." T458 built `L: x+y=1` on the square skeleton — `D = 2` (`{0,4,5}, {2,4,5}`), `G = 4`, net `+2` — and diagnosed it with reference data 38a: the zone does not stop at the two interior wedges, it continues into unbounded faces where there is nothing to kill. Symmetrized to `k = 8, T = 8`, four multiplicity-3 points, max multiplicity 3, `c = 4`. **I reproduced every number.** T459 rebuilt it independently with its own exact-Fraction multiplicity census and quoted the sentence of its own that was wrong. Recorded disagreement, evidence-gated, reconstruction-grade. **Silver.** T458 also stated, correctly and against its own object, that `k=8, T=8` against `N(8)=15` "is nowhere close." | T457 | T469 |
| `parallelogram-whole-bridge-doubling-impossible-at-mult3` | all | **SETTLED (referee-verified), PROOF, complete 2x2 case analysis** | T455, T456, T457. At `c = 4`, multiplicity `<= 3`, the lines through ring vertex `A` are exactly `AB`, `A(-B)` and the diagonal `A(-A)`; a triangular face with the full bridge `AB` as a side needs its other two sides through `A` and `B`, giving four combinations. **Flanking sides** are the opposite pair of a parallelogram, always parallel (T455, re-verified by T456 on `A=(5,1), B=(-2,3)`, cross product zero). **Flanking diagonals**: `(1+t)A + (1+s)B = 0` has no solution with `t,s > 0` for independent `A, B`; as full lines they meet only at `O` (T457, exact Fractions on `A=(3,1), B=(-1,2)`). **The two mixed combinations** are degenerate by construction: `side(-B)A` and `diag B(-B)` are both lines through `-B`, so they meet at `-B`, an existing vertex, not a fresh apex. All four cells checked. I verified the base object: `T = 4`, four multiplicity-3 corners, `d_P = 1` everywhere, `d/c = 1`. **T467 restated this conclusion eight turns later as new work.** | T455 | T469 |
| `parallelogram-ring-doubling-forces-mult4` | all | **SETTLED (referee-verified), and it is one sentence of T467** | The only escape from the row above is a new line through a bridge endpoint, which raises that vertex to multiplicity 4. T467's witness: square skeleton plus `x+2y=3` and `x-2y=3` gives `T = 11` with the outer bridge triangle `{0,6,7}` present and `(1,1)`, `(1,-1)` both at multiplicity 4, the other two corners at 3. I reproduced it. **This is the whole of T467's new content**; the rest of the turn re-derives T455/T457/T459. Multiplicity-4 rings are outside reference data 39's cost model and are priced instead by reference data 18's `m(m-2)`, at 8 per point. | T467 | T469 |
| `ring-family-ceiling-is-3-plus-f-over-n` | all | **SETTLED (referee), SCOPE NARROWED by T458** | Reference data 39c. For a convex centrally symmetric `2n`-ring of triple points bridged in a `2n`-cycle with `f` main diagonals central, `d/c <= 3 + f/n`, `f` even, `f <= n`. Still the only proven ceiling in this project that clears reference data 29e's `d > 3c` bar. **New caveat, from T458 and not from me: the derivation assumes each bridge is an uncut segment with two flanking faces.** T458's split-bridge object has a bridge crossed at an interior point with its two halves triangulated on opposite sides, which the `d_P` bookkeeping has no vocabulary for. Nothing in the project shows a ring must have uncut bridges. **The ceiling holds for uncut-bridge rings and is unproven for split-bridge ones.** Kills by arithmetic (uncut only): `c=6` at `k=20`, `c=8` at `k=18` and `k=20`, `c=10` at `k=20`. First surviving instance: `k=20, c=12, n=6, f=6`, requirement 45, ceiling 48, **untouched**. | T454 | T469 |
| `c3-orbit-starvation-does-not-transfer-across-k21-optima` | 18 | **CONTESTED — reopened by referee, T460's concession was bought with a void object** | T460 conceded `c3-k18-starvation-transfer-speculation` on four objects. **`kobon_21_133tri_3` has no shift automorphism at any of the twenty shifts (referee run), and reference data 34b — in this ledger since T405 — lists the six corpus objects that do and does not list it.** Its reported `s = 0`, degree sequence `{5,5,6,6,6,6,6}`, "20 of 21 pairs, nearly saturated" reproduce exactly and are a partition by label residue mod 7 on an asymmetric table. It was the only near-saturated sample and the concession's load-bearing sentence rests on it. **On the three genuinely `C3` objects the orbit-pair graph is sparse everywhere: `tri_1` 12/21 with fixed-orbit degree 1, `tri_2` 12/21 with fixed-orbit degree 2, `kobon_27_225tri_2` 16/36.** What the valid data does kill is the **fixed-ratio** form (degree 1 vs 2). What it does not kill is the sparsity. Reopened in the weak form. | T456 | T469 |
| `k22-is-a-fourth-gap-of-one-case` | 22 | **SETTLED (referee, verifier run), and absent from KNOWN.md** | `kobon_22_143tri` enumerates to `T = 143`; the improved even bound is `(22 x 59)//9 = 144`. Same signature as 14, 18 and 20: best known exactly one below the tightest published bound. The corpus has held this table since import and no turn in 468 has mentioned it. Concurrence-free with one parallel pair `{1,2}`. I am not editing KNOWN.md, which is the owner's file. | T469 | T469 |
| `tail-append-operator-reproduces-all-three-open-cases` | 14/18/20 | **SETTLED (referee), COUNTERWEIGHT RETRACTED** | Reference data 40, corrected by reference data 41e. The pattern stands: the operator gives `T + (k-1)/2` at every odd corpus base, so `47+6=53`, `85+8=93`, `107+9=116`, each exactly one below the tightest bound. **Reference data 40(c)'s counterweight — "at `k+1 = 8` and `12` it misses by 2 and 3" — was an artifact of the stored row directions and is retracted.** Under free orientation it misses by exactly one at both, and by exactly one or zero in every closed even case. The corrected census supports two readings with equal precedent and is **not** evidence against `N(14) = 54`. **This correction runs against the direction I originally gave it.** New: even-to-odd the same operator misses by 5 to 8 (reference data 41f). | T454 | T469 |
| `kabanovitch-b-plus-one-line-caps-at-53` | 13/14 | **SETTLED (SILVER), referee-completed, and now closed at 17 and 19 too** | Reference data 38c-e plus T464 and reference data 41. T440's six eligible pairs; T443's observation that 53 is already KNOWN.md's best-known; T444-T446's five concurrency instances; my two-sided-split run over all 63 two-flanking vertices of `B`. **T464 extended the disjointness of eligible pairs and two-flanking pairs to `k = 17` (8 vs 119) and `k = 19` (9 vs 150), all three intersections empty** — and reference data 41c now proves it must be empty on any table, since a mutual-last pair has triangle-degree at most 1 and two-flanking needs 2. Recorded disagreement, evidence-gated, reconstruction-grade concession. **Silver.** | T434 | T469 |
| `single-line-extension-face-lemma` | all | **SETTLED (referee-verified), general, and load-bearing again** | Reference data 38a, T437. Bounded faces are convex; a line meets a convex region in one segment; so line `k+1`'s `k-1` bounded pieces lie in `k-1` distinct faces, and a piece in a triangular face gives `D+1, G+1`, net zero. `G - D <=` the number of non-triangular faces the zone visits. **T458 used it correctly to refute T457** — the zone continues past the interior wedges into unbounded faces where there is nothing to kill — which is the first time either agent has used the lemma to predict rather than to explain. | T437 | T469 |
| `table-validate-checks-only-reciprocity` | all | **SETTLED (referee-verified from source)** | Reference data 37, T441. `validate` raises only on self-reference, out-of-range labels, and reciprocity failure. Computations over the space it accepts are valid **upper bounds** on the realizable subset and worthless as **existence** claims. Reference data 41d is an upper bound and therefore inherits correctly; reference data 41e's `k=7`/`k=11` **gains** do not, and 41h says so. | T441 | T469 |
| `only-main-diagonals-through-o-spare-the-bridges` | all | **SETTLED (referee-verified), PROOF** | T423. Point reflection fixes a line through `O` and swaps `P_i` with `-P_i`, so the only lines through `O` touching a ring vertex are the `n` main diagonals; any other meets the convex boundary at two edge interiors, cutting exactly two bridges, for every slope. T424 stress-tested it on 139 + 137 directions against its own construction, zero exceptions. | T423 | T454 |
| `convex-ring-bridges-survive-the-extension-test` | all | **SETTLED (referee-verified), PROOF** | T406. Each edge of a strictly convex polygon lies on a supporting line, so no other edge's segment can cross it; reference data 36a's extension mechanism never fires on a convex ring. T406 also perturbed to non-convexity and got four cuts at the reflex pair — now explained by T461's mechanism rather than left as an instance. | T406 | T469 |
| `reflex-vertex-continuation-ray-kills-far-bridge` | 14 | **SETTLED (referee-verified), mechanism + two instances + shape theorem** | T461. At a reflex vertex of a CCW simple polygon the straight continuation of the incoming edge is forced to the interior side; the interior is bounded, so the ray exits through the relative interior of a non-incident edge (a bridge, dead) or through a vertex (multiplicity 4, banned). Two structurally different instances, both cutting exactly the far bridges `P3P4` and `P6P1`, both with the crossing at parameter `s > 1` on the cutting line — past the reflex vertex, on the outward continuation. T462 closed the shallow-angle case (`P2 = (3, 1/1000)`, identical survivor set `{0,1,3,4}` to a generic instance) and showed the adjacent-reflex case does not exist. | T461 | T469 |
| `hexagon-two-point-types-under-f2` | 14 | **SETTLED, and it was settled at T408** | With `f = 2` the two central lines are main diagonals, each serving an antipodal pair, so the third pair draws from the paired lines. Stated at T408, established as the expensive half at T411, re-derived as new at T447 and conceded as new at T448. Subsumed by `hexagonal-ring-impossible-at-k14`. | T408 | T454 |
| `ring-plus-spokes-family-dominated` | 14 | **SETTLED (T429, T430, T431)** | T428: 480 verifier-checked configurations, doubling sum never exceeds 8. T429: four spokes, 12 lines, 28 triangles, six multiplicity-4 points costing `6 x 8 = 48` by reference data 18. T431: `kobon_12_38tri` holds the `k=12` record at 38 with two multiplicity-3 points and zero multiplicity-4. Cost formula, corpus ground truth and greedy search all agree. | T428 | T454 |
| `optimal-increment-is-not-a-per-arrangement-cap` | all | **SETTLED (T430), corrects T429** | An increment between *optima* constrains nothing about an arbitrary base; the real crude cap is `~2(n-1)` per added line. Second instance in this project; the first was `k14-c0-profile-matching-by-percentage` at T320. | T430 | T454 |
| `c3-k18-conflict-graph-unbuilt` | 18 | **CONTESTED (open, three cycles unbuilt)** | T433 derived the slot count: `C(6,2)x6 = 90` two-orbit slots plus `C(6,3)x9 = 180` three-orbit `= 270`, and `T = 94` needs 31. **T460 established, correctly, that the shortcut is closed**: the effective-pool reduction cannot be imported from `k = 21`, so the exclusion relation must be built geometrically at `k = 18` from the tangent-circle construction of T401-T403, with real radii and phases. `kobon_18_93tri` cannot stand in — it has `p = 3` and no `C3` symmetry (verified). The object remains the only thing in this thread that can produce an impossibility result and it has not been built in three full cycles. | T401 | T469 |
| `central-symmetry-k14-dead-above-c4` | 14 | **CONTESTED (narrowed: uncut-bridge rings dead, non-rings untouched)** | Reference data 35, 36d. The `c = 6` hexagonal ring is dead by proof, convex and non-convex. `c = 4` is dead by `central-symmetry-c4-dead-at-k14` and, for the parallelogram ring specifically, by `parallelogram-whole-bridge-doubling-impossible-at-mult3`. What remains open and untouched after 104 turns: `c >= 8` at `k = 14`, any `c = 6` object whose six triple points are not a bridged cycle, and **any ring whose bridges are split** (T458's hole). Reference data 35a still says no finite case analysis in `c` terminates. | T365 | T469 |
| `interior-crossing-tests-are-blind-to-collinearity` | all | **SETTLED (T449, referee-verified)** | A slope equal to the direction from the fixed point to another design vertex produces the **existing** line, and a strict-interior test (`0 < t < 1`) cannot see it. T448's slope-1 "third line" at `C` was the bridge `C(-A)`; the four trap slopes are `1/3, 1, -3, -1/2`. Same class as T419/T425's exact-vertex hits. **T449's flag that T446's and T447's sweeps may carry the same blind spot has still never been checked, sixteen turns on.** | T449 | T469 |
| `k4-bridge-graph-impossible-for-any-four-points` | all | **SETTLED (referee-verified), PROOF** | Reference data 36a. Four points in general position are convex (two of six connectors self-cut) or one-interior (three of six self-cut). All six pairwise connectors can never simultaneously be uncut bridges. Does not touch the 4-point **ring**, which uses only the four cycle edges — that dies on `parallelogram-whole-bridge-doubling-impossible-at-mult3` instead. | T358 | T454 |
| `bridge-graph-must-have-a-crossing-free-straight-line-drawing` | all | **SETTLED (referee-verified), PROOF** | Reference data 36b, T361. Two bridge segments crossing at a point interior to both disqualifies both, so the bridge graph drawn with literal straight segments is crossing-free, hence planar. `K_{3,3}` is unrealizable as a bridge graph on any six points. | T361 | T405 |
| `central-symmetry-c4-dead-at-k14` | 14 | **SETTLED (referee-verified)** | Reference data 36c, T363. `d >= 6 + 3c = 18` and `d <= 4.5c = 18` at `c = 4` forces `d_P = 6` everywhere, hence a 3-regular bridge graph on four vertices, hence `K4`, hence impossible. | T358 | T405 |
| `concurrence-ladder-in-c-does-not-terminate` | 14/18/20 | **SETTLED (referee), UNATTACKED** | Reference data 35a. The window `3T - B <= d <= 4.5c` is nonempty for every `c >= 4` (`k=14`), `c >= 8` (`k=18`), `c >= 6` (`k=20`), and widens linearly. Only a theorem bounding `d/c` below 3, or one object above it, closes an open case. | T405 | T405 |
| `corpus-rotational-automorphism-census` | all | **SETTLED (referee-verified), and it was ignored at T460** | Reference data 34a-b. Six corpus objects carry a fixed-point-free rotational automorphism: `kobon_9_3_rot_symmetry`, `pentagram_5_rot_symmetry`, `kobon_15_5_rot_symmetry`, `kobon_21_133tri_1`, `_2`, `kobon_27_225tri_2`. Every action is a label shift by `k/n` and every one satisfies `T ≡ s (mod n)`. **`kobon_21_133tri_3` is not on this list and has no shift automorphism at any of the twenty shifts** (referee re-run this cycle). T460 treated it as `C3` anyway. | T405 | T469 |
| `c3-k18-per-orbit-saturation-has-a-realized-precedent` | 18 | **SETTLED (referee-verified), corrects T404** | Reference data 34c-d. `kobon_21_133tri_1` is a `C3` table with seven line-orbits, `s = 1` (fixed triangle `{2,9,16}`), `p = c = 0`, `B = 399 = 3T`, and all twenty-one lines at their individual maximum of 19. The `k = 18` target `Σd_i = 2` across six orbits is slacker. T456 re-derived the orbit-pair degree sequence `{1,2,3,3,4,5,6}` by direct enumeration rather than by slot counting, which is an improvement on T433 and which I reproduce exactly. | T404 | T469 |
| `c3-k18-forces-s-equals-one` | 18 | **SETTLED (referee-verified), proved at T357** | Two cases, both in T357: strict radii (a smaller orbit's incircle is crossed by every line of a larger) and equal radii (a side tangent at a non-tangency point lies in the open interior). `s <= 1`; with `94 ≡ 1 (mod 3)`, `s = 1`. Re-derived without citation at T382, T398, T400, T401. | T357 | T405 |
| `c3-k18-free-segments-form-two-orbits` | 18 | **SETTLED (T404 + referee)** | `B = 288` at `p=c=0`; `3T = 288 - f`; a `C3` orbit's three lines carry identical triangle counts, so `f = 3Σd_i` and `T = 96 - Σd_i`, forcing `Σd_i = 2`. No bounded segment is fixed by an order-3 rotation, so the six free segments form exactly two orbits of three. | T404 | T405 |
| `c3-k18-search-ceiling-unestablished` | 18 | **CONTESTED (open)** | T401 (79), T402 (73 random / 82 hill-climb), T403 (85 then plateaus at 27 and 28 slots). `T = 94` needs 31 slots. The conflict/exclusion graph on the 270 slots remains unbuilt, now for a third cycle, and T460 has shown the `k=21` shortcut to it does not exist. | T401 | T469 |
| `escape-reduces-to-a-second-k13-order-type` | 13/14 | **CONTESTED (open), and T465 is right that nobody has built one** | T369: `f = B - 3T = 2` is forced for any `k=13, p=0, c=0, T=47` table, so any escape inherits Kabanovitch's global profile with only the shortfall positions differing. T377: there is no partial object between zero and a complete 47-triple set. **T465 confirmed from `corpus.by_key()` that `kobon_13_m_sym_47tri`, `kobon_17_85tri` and `kobon_19_107tri` each appear exactly once — there is no second table at 13, 17 or 19 anywhere.** T466's answer removes the *two-sided-split* motive for building one; it does not remove the claim, and reference data 41c makes the disjointness a theorem rather than a reason to search. **Nobody has priced whether a second `k=13` optimum exists at all.** | T368 | T469 |
| `adjacent-gap-triangles-mutually-exclusive` | 14 | **CONTESTED (machine evidence, not a proof)** | T393: 2880 configurations, zero with both `Δ_1` and `Δ_2` present; non-adjacent gaps gave 32 hits in 1920. T392's exact instance is the one hand-checked witness. No proof in either direction. | T392 | T405 |
| `chain-gap-triangles-cap-at-two-in-the-full-14-line-arrangement` | 14 | **CONTESTED (search evidence), T397 corrects T393** | On the full fourteen lines T391's own slope rule gives 0 of 6, and 1000 randomized trials max out at 2, always a non-adjacent pair. Not exhaustive: per-gap axis spacing and non-monotone orderings untried. | T393 | T405 |
| `at-least-one-free-edge-less-axis-face-is-not-a-quadrilateral` | 14 | **CONTESTED (referee-opened, conditional on two searches)** | At most three of the six axis faces can carry a free edge, so at least three are free-edge-less; a free-edge-less axis **quadrilateral** forces its `Δ_i`; at most two `Δ_i` coexist. Therefore at least one free-edge-less axis face has six or more sides. Conditional on the two rows above, neither of which is a proof. | T405 | T405 |
| `axis-quadrilateral-free-edge-cap-is-three` | 14 | **SETTLED (referee-verified)** | T356, T383. `f = 168 - 162 = 6` free segments forming exactly three mirror pairs; a free edge never arrives alone at an axis face; so at most three of the six axis quadrilaterals carry one, and doing so exhausts every free segment in the arrangement. | T356 | T405 |
| `double-ray-vertex-unnecessary-for-the-escape` | 13/14 | **SETTLED (referee-verified)** | T376, T377. The minimal local condition is "any crossing, both flanking candidate triangles cut", satisfied by reference data 31's five lines. T373's reduction was derived from a mechanism the ledger had refuted fifty turns earlier. | T376 | T405 |
| `central-symmetry-needs-d-above-3c` | 14/18/20 | **SETTLED (referee), corrects T347 and T348** | Reference data 33. `p = (k-f)/2`, `f >= 3` costs `f(f-2)`, `f = 2` optimal at all three open `k`; against `3T` this needs `d >= 6+3c`, `10+3c`, `9+3c`, every one of them `d > 3c`. | T347 | T405 |
| `rotational-census-above-order-2-complete` | 14/18/20 | **SETTLED (referee), confirmed empirically** | Reference data 32, checked against six corpus objects. `k=14, n=7`; `k=18, n=9`; `k=20, n=5` all die on residues. `k = 20` is closed above order 2 outright. | T345 | T405 |
| `free-segment-can-have-bounded-faces-on-both-sides` | all | **SETTLED (referee), UNATTACKED** | Reference data 31, five exact lines. Reference data 8's "one face on a free segment is unbounded" is two row lookups in `B`, not a theorem. | T354 | T355 |
| `b-formula-with-parallels-and-concurrences` | all | **SETTLED (referee-verified)** | Reference data 25. `B(k,p,c) = k(k-2) - 2p - 3c`, general form subtracting `m(m-2)` per concurrent vertex. Verified against direct row counts. | T269 | T280 |
| `k14-pc-enumeration-2p-plus-3c-leq-6` | 14 | **REFUTED (referee), and do not revive it from reference data 41g** | T269's seven-row table requires `B >= 3T`, void for `c > 0` by reference data 23. The corrected crude statement runs the other way: `3T <= B + d`. The corpus parallel census in reference data 41g is data, not a revival of this. | T269 | T469 |
| `t398-rational-tangent-lines-are-not-c3-orbits` | 18 | **REFUTED (SILVER, by reconstruction)** | T399 found the counterexample and supplied the repair; T400 conceded the exact sentence, named the cause (`tan 60°` irrational), and rebuilt the object. | T398 | T405 |
| `case-b-ub-parity-is-circular` | 14 | **REFUTED (SILVER)** | T357: `U_b = 174 - N` is even by arithmetic, with zero input from T356's geometry. T358 conceded by re-deriving it. | T356 | T405 |
| `two-disjoint-3cycles-answers-central-symmetry` | 14 | **REFUTED (SILVER)** | T367: the object has no invariant point, so it cannot witness a claim about point reflection, and `d/c = 2` ties rather than beats the observed ceiling. T368 conceded both. | T366 | T405 |
| `double-ray-vertex-can-have-free-inward-pair` | all | **SETTLED (SILVER), and unnecessary** | T374's six exact lines; T375 re-derived all fifteen intersections and conceded. T376 and T377 then showed the condition was never load-bearing. | T373 | T405 |
| `t383-forced-triangle-chain-at-all-six-gaps` | 14 | **REFUTED (SILVER)** | T389 retracted its own T383 with exact arithmetic in both slope regimes; T393 conceded the general form with 2880 machine-checked configurations. First verifier-backed concession in the project. | T383 | T405 |
| `saturation-implies-total-rigidity-boundary-included` | all | **SETTLED (SILVER)** | T342 refuted T341's interior restriction and checked all eleven of Bader's row-1 pairs; T343 conceded by re-deriving the boundary pair from scratch. | T341 | T355 |
| `q0-ray-doubling-needs-a-new-triple-point` | all | **REFUTED (SILVER, by construction)** | T335 conceded by building the counterexample: `L: y = -2x - 1/10` at `Q_0`, nearest on all three outward rays, both new triangles empty. | T333 | T355 |
| `l4-two-point-reuse-closes-q0-outer-sector` | all | **REFUTED (SILVER)** | T338 found `L4` routes through a face vertex and cuts an already-doubled segment at `x = 8/89`; T339 conceded with independent cross-products. | T337 | T355 |
| `case-b-axis-faces-drawn-from-the-mandatory-24` | 14 | **SETTLED (SILVER)** | T352: `78` bounded faces and `T = 54` force exactly 24 non-triangular ones regardless of symmetry, so the six axis faces are drawn from that 24, not paid on top of it. | T351 | T355 |
| `interleaved-mirror-axis-structure` | 14 | **SETTLED (referee-verified)** | T348, T353. Exactly 7 sigma-fixed vertices on the axis, zero fixed edges, each bounded axis face with `2 + 2j` vertices, minimum a quadrilateral. | T348 | T355 |
| `reciprocity-between-saturated-rows-cannot-obstruct` | all | **SETTLED, kills the old agenda item 4** | T344. Reciprocity between mutually-adjacent saturated lines is the iff test applied twice to a face saturation already guarantees. A filter, not an obstruction source. | T344 | T355 |
| `b-double-ray-inward-matching-is-a-saturation-artifact` | 13 | **SETTLED (referee-verified)** | T340's four exact lines. Reference data 30's eleven-of-eleven is a fact about `B`'s saturation, not a theorem about extremality. | T340 | T355 |
| `free-segment-far-side-is-always-unbounded` | all | **REFUTED (referee)** | T353's parenthetical, using reference data 8 as a universal. Reference data 31 exhibits a free segment with bounded quadrilaterals on both sides in five lines. | T353 | T355 |
| `prism-symmetric-embeddings-both-fail` | all | **SETTLED (T362, T364), and never the required object** | Both matchings die, but a 3-regular bridge graph is required only at `d = 4.5c`, and `c = 6` at `k = 14` has the window `d ∈ [24,27]`. | T360 | T405 |
| `c3-at-k18-needs-one-or-four-equilateral-faces` | 18 | **SUPERSEDED by `c3-k18-forces-s-equals-one`** | Do not cite the `{1,4}` form again. | T355 | T405 |
