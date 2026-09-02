# Ledger

Claim registry, rewritten daily by the referee. `SETTLED` requires a complete
argument or a verifier run. Two agents agreeing is not evidence.

Rewritten by REFEREE after turn 354. Turns 330-354 audited.

**Twenty-five turns, four earned concessions, the best symmetry work in the
project's history, and nine turns spent closing sectors at one spare vertex of a
six-line gadget that tops out at `T = 6` against `N(6) = 7`.** T331 through T339
is a complete cycle in miniature: a real lemma (T331's vertical-angle
confinement), a real correction (T334's citation of reference data 26 against
T333's necessity claim), a real construction (T335's line `L`, which I have
checked and which is correct), a real refutation (T338's exact wedge argument at
`C`), and a real concession (T339, with exact cross-products). Every one of those
turns is honest and most of them are right. The best number any of them produced
is `d/c = 1.75`, at `k = 7`, in a gadget nobody claims scales. Nine turns for
0.25 of a ratio on an object the ledger already recorded as dominated.

**Then the cycle found the thing it should have been doing all along, and I am
going to say plainly that it is one thing, not two.** T345 killed the `C7`
pinwheel at `k = 14` by a residue. T346 generalized the stabilizer argument to
`k = 18` and `k = 20`. T347 turned to order 2 and found that central symmetry
forces parallel pairs. T348 correctly scoped T347's kill to `c = 0`. What nobody
computed is what central symmetry actually needs, and it is exactly the quantity
this project has been chasing since T305. Under point reflection every line off
`O` pairs with a parallel, so `p >= (k-f)/2`; the best case is `f = 2` and then

    k=14   B <= 156 - 3c   3T = 162   needs  d >= 6 + 3c
    k=18   B <= 272 - 3c   3T = 282   needs  d >= 10 + 3c
    k=20   B <= 342 - 3c   3T = 351   needs  d >= 9 + 3c

**Every one of them is `d > 3c`, which is reference data 29e's decision rule
verbatim.** And every even rotational order contains the 180-degree rotation, so
every even-order symmetric route at every open `k` inherits this. The symmetry
program and the concurrence program are the same program. They stand or fall on
one number, the observed ceiling on that number is `2c`, and it has not moved in
fifty turns. Reference data 33.

**The rotational census is now complete, and `k = 20` is closed.** Reference data
32. For odd `n` no rotation fixes a line, so `n | k`; for even `n` the
central-symmetry budget above applies. Odd survivors: `n = 7` at `k = 14`
(`T ≡ 0 mod 7`, `54 ≡ 5`, dead), `n = 5` at `k = 20` (`117 ≡ 2 mod 5`, dead),
`n = 9` at `k = 18` (`94 ≡ 1 mod 3`, dead), and `n = 3` at `k = 18`, which
survives. **`C3` at `k = 18` is the only rotationally symmetric family above
order 2 still alive at any open case**, and it carries a sharp condition nobody
has looked at: `T ≡ s mod 3` where `s` counts triangles fixed setwise, each of
which is equilateral and centred at `O` and uses one whole line-orbit, so
`s <= 6`; `94 ≡ 1 mod 3` forces **`s = 1` or `s = 4`**. One or four concentric
equilateral faces. That is an object, and it is on the agenda.

**Reference data 31, five lines: a free segment can have a bounded face on both
sides.** T344 was assigned agenda item 3.2 — can the *unbounded* face beyond a
free segment have four or more sides — and answered a restatement of it: "or can
it have a bounded face with four or more sides?" Its `k = 4` object has an
unbounded three-sided wedge on one side and a bounded quadrilateral on the other,
which is **structurally identical to B's own free segments** (three-wedge one
side, hexagon A or B the other, reference data 8 and 9). B already answers the
restated question. The real question is answered here: `a: y=0`, `b: y=5x`,
`c: y=-5x+5`, `e: y=1+x/100`, `d: y=-1+x/50`. Five distinct slopes, ten distinct
vertices, `p = 0`, `c = 0`. The segment of `a` from `(0,0)` to `(1,0)` is free
because `e` cuts the candidate triangle `{a,b,c}`, and **both** its faces are
bounded quadrilaterals. Neither side is unbounded at all.

**And T353 asserted the opposite as a general fact one turn after its opponent
had been assigned to test it.** "free segments, whose far side is unbounded" —
that is reference data 8, whose proof is two row lookups in Kabanovitch's B, not
a theorem. Reference data 31 refutes it. Combined with T340's counterexample,
which is correct and which I have checked, the whole defensive apparatus that
closed reference data 22e *for B* is now known to rest on B's 141/143 saturation
at two separate joints: inward-neighbour matching at a double-ray vertex is not
forced (T340), and the face beyond a free segment need not be an unbounded wedge
(reference data 31). `insertion-cap-53-generalizes-beyond-b` stays CONTESTED and
the gap is wider than it was.

**T354's segment tax is not a tax.** Its closing object asks whether the two
segments a mirror pair spends on the two flanking axis quadrilaterals are "a
genuine tax on `m_{i+1}`'s remaining budget, or free." Reference data 4 answers
it in one line: a bounded segment is a side of at most one triangle, and by
T321's `opposite-face-non-triangular-generalizes-beyond-b`, **bordering a
non-triangular face is exactly what a triangle side looks like from the other
side.** All 141 of B's triangle-sides do it. The segment is not consumed. The
real accounting is `N + U_b = 174` at `k = 14, p = 0, c = 0, T = 54` (T321's
identity, which I re-derived: `2E = 392`, minus `3T = 162`, minus `56` ray
incidences), and the six axis quadrilaterals pin `24` of `N`. That leaves 18
non-triangular bounded faces in 9 sigma-orbits and 27 triangle orbits, exactly
T352's arithmetic, with no obstruction anywhere.

## The referee's findings this cycle

1. **Central symmetry needs `d > 3c` at all three open cases.** Reference data
   33. Point reflection maps a line off `O` to a distinct parallel line, so with
   `f` lines through `O` the rest form `(k-f)/2` parallel pairs; `f >= 3` makes
   `O` a concurrence costing `f(f-2)` segments, so `f = 2` is optimal at every
   open `k`. The resulting requirement is `d >= 6 + 3c` (`k=14`), `10 + 3c`
   (`k=18`), `9 + 3c` (`k=20`). With `d <= 4.5c` (reference data 29d) this forces
   `c >= 4`, `c >= 7`, `c >= 6` respectively, and the required ratio is
   `3 + 6/c`, `3 + 10/c`, `3 + 9/c`, always strictly above 3. **T347's "dead at
   `T <= 52`" is right under the observed `d <= 2c` and wrong as stated; T348's
   correction identified the scope error and stopped one computation short of the
   number.**
2. **The rotational census above order 2, complete, and `k = 20` closed.**
   Reference data 32. Even `n` contains the 180-degree rotation and inherits
   finding 1. Odd `n` fixes no line, so `n | k`. Stabilizer of a setwise-fixed
   triangle embeds in `S_3` (its kernel would fix three distinct points), so it
   has order 1, 2 or 3; order 2 needs a fixed vertex, hence `O` a vertex; order 3
   needs `3 | n`. Residues: `k=14, n=7` dead; `k=18, n=9` dead; `k=20, n=5` dead;
   **every rotational order above 2 at `k = 20` is dead.** `k=18, n=3` survives
   with `s ∈ {1,4}` fixed equilateral faces. T346's enumeration by divisors of
   `k` is correct as far as it goes and its scope caveat ("needs a non-vertex
   center") is honestly stated; what it did not do is notice that the excluded
   case is exactly central symmetry, already on the record two turns later.
3. **Reference data 31: a free segment with bounded faces on both sides, five
   lines, `p = 0`, `c = 0`.** Answers agenda item 3.2 as asked. T344 answered a
   restatement of it that B itself already satisfies, and T353 asserted the
   refuted general form in the next turn but one.
4. **T354's axis-quadrilateral tax is zero.** Reference data 4 plus T321. A
   segment bordering a non-triangular face on one side is the normal state of a
   triangle side. The live accounting is `N + U_b = 174`, with the six axis
   quadrilaterals pinning 24 of `N`.
5. **T335's line `L` is correct and I re-derived it.** `L: y = -2x - 1/10` at
   `Q_0` of reference data 28. `L ∩ M_1 = (-1/20, 0)`, `L ∩ a = (-1/30, -1/30)`,
   `L ∩ M_5 = (0, -1/10)`; `b, c, M_3` meet `M_1` only at `x = 4, 4/3, 4` and `a`
   only at `x = 1, 1, 2`, all positive, so `L` is nearest on all three outward
   rays trivially. Both new triangles are empty and `L` never enters the closed
   first quadrant, where all six of `P`'s faces live, so nothing is disturbed.
   `k=7, c=4, d=7, T=8`, `d/c = 1.75`. The best number the nine-turn thread
   produced and the only durable object in it.
6. **T350's eight-line closure has two parallel pairs and its stated reason is
   false.** `L5: y = -1` is parallel to `M_1: y = 0` — T351 caught this one. `L4:
   y = -x - 2` has slope `-1`, **parallel to `M_3: x + y = 4`** — neither turn
   caught this. So `p = 0 -> 2` and neither turn's budget reflects it. And
   "`L4, L5` stay in the third quadrant, clear of `P, Q_2, Q_4`" is false: `L4`
   meets `b` at `(-5, 3)` and `c` at `(3, -5)`, and it cuts the second-quadrant
   wedge at `Q_0` into a bounded quadrilateral and an unbounded piece, so T350's
   "S3 (still a wedge)" is wrong too. **The conclusion survives** — `L4` has
   `y <= -2` throughout `x >= 0`, so `P`'s six faces are untouched, and
   `Δc = 1, Δd = 1` stands — but for a reason neither turn gave.
7. **T340's `k=4` counterexample is correct and I checked all four rows.**
   `L1: y=0`, `L2: y=3x`, `L3: y=-3x+12`, `L4: y=(x+50)/10`. Rows by
   `x`-coordinate: `1: L4, L2, L3`; `2: L1, L4, L3`; `3: L2, L4, L1`;
   `4: L1, L2, L3`. `V(1,3) = (4,0)` is a double-ray vertex, inward neighbours
   `L2` and `L4` differ, `{1,2,3}` fails the iff test in row 2, and `T = 2 =
   N(4)` via `{1,2,4}` and `{2,3,4}`, both verified on all three legs. **Inward-
   neighbour matching at a double-ray vertex is not forced.** Reported by
   Euclidn't against its own defensive position, which is the right instinct.
8. **T344's kill of agenda item 4 is correct and I am retiring the item.**
   Reciprocity between two mutually-adjacent saturated lines cannot fail in a
   valid table, because it is the iff test's necessity direction applied twice to
   a face saturation already guarantees exists. It is a construction filter, not
   an obstruction source. T313's "concrete collision to hunt for" does not exist.
9. **Case B's arithmetic is clean and its census is right.** `(k-1)(k-2)/2 = 78`
   bounded faces, `T = 54` leaves exactly 24 non-triangular, the six sigma-fixed
   axis faces are drawn from that 24, and the remaining 72 faces split as 27
   triangle orbits and 9 non-triangle orbits. T352's Euler arithmetic and T353's
   `2 + 2j` vertex-parity derivation of the quadrilateral minimum are both
   correct and I checked both. T348's seven fixed vertices and zero fixed edges
   are correct and follow from "no fixed line" exactly as claimed.
10. **The verifier is gated on the fifty-fourth consecutive day.** Every agent
   turn this cycle reported the gate and correctly declined to log the refusal.
   The NO_VERIFIER_RUN notice fired at T340 and T343 against a tool the sandbox
   refuses, and UNGROUNDED_CONCESSION fired at T343 against a turn that quotes
   its opponent and re-derives the step. Both are noise. Owner action: the
   allowlist. `python3`, `head`, `tail` and `wc` are all refused in this session
   as well, which is why this file is spliced rather than rewritten whole.
11. **Not gold.** Reference data 31 is a construction. Reference data 32 and 33
   are proofs, they are mine, and they are unattacked; breaking them is agenda
   item 1.

## Call-outs, by turn number

- **T331-T339, the nine-turn detour, priced.** Q_0 is one vertex of a six-line
  gadget whose whole triangle count is 6 against `N(6) = 7`. The thread produced
  T335's `L` (real, checked, `d/c = 1.75`), T338's wedge refutation (real,
  checked), and three retractions. It also produced T333's necessity claim, which
  was false and which T335 refuted by building the counterexample rather than
  agreeing — the strongest form a concession can take and I am marking it silver.
  What none of the nine turns did is ask, in advance, what the ceiling on the
  answer was. Reference data 28 was already at `d/c = 1.5` and the threshold is 3.
  **The standing rule "produce a construction family's crude cap before analysing
  its fine structure" applies to sub-vertices of a family too.**
- **T335, the model concession.** T333 (its own turn) had claimed doubling a ray
  requires promoting the far point to a triple point. T334 cited reference data
  26 against it. T335 did not concede in words; it wrote down `L: y = -2x - 1/10`,
  computed all three crossings, checked every competitor on all three rays,
  checked both new triangles for emptiness, and only then said "turn 333's
  necessity claim is wrong, and I'm conceding it." Every number in it checks.
  **Silver, and the best-executed concession in the ledger.**
- **T337 and T338, the exact-arithmetic exchange.** T337 built `L4` through the
  two already-fixed nearest points and declared "`L4` doesn't clip anything"
  after checking it only against the two triangles its own previous turn had
  built. T338 found `L4` routes through `C = b ∩ M_5`, a vertex of face 2, and
  gave the exact wedge test `80/3 > -1/3` plus the crossing `L4 ∩ c` at
  `x = 8/89 ∈ (0,1)`. T339 conceded with independent cross-products
  (`cross((0,1),(1/20,4/3)) = -1/20`, both signs matching) and named the
  configuration it was retracting. I re-solved `4 - 3x = 4/3 + 80x/3` and got
  `89x = 8`. **Silver.** T338 also invoked the right standing prohibition by
  name, against a fresh case rather than a stale one.
- **T341, T342, T343, the rigidity exchange.** T341 derived the two-of-three-legs
  claim through T313's lock and restricted it to `2 <= i <= n-2`. T342 pointed
  out that neither leg needs the lock: saturation says the segment serves a
  triangle, reference data 4 says which one, and the iff test's necessity
  direction gives all three legs for every `i`. It then checked all eleven of
  Bader's row-1 pairs against reference data 2 — I re-checked all eleven and they
  are all there — and, unprompted, said its own corrected count `5*11 + 6*12 =
  127` "is tautological... restating the hypothesis." T343 conceded by
  re-deriving the boundary pair `(11,4)` from scratch. **Silver, and the least
  valuable of the four**, because what it settles is a definition. T342 said so
  itself, which is why it gets the silver anyway.
- **T344, which killed its own agenda item and did it properly.** "Reciprocity...
  is automatically true in any valid table, full stop... it can only catch a
  construction attempt that was already broken for other reasons." Correct, and
  it retires agenda item 4 of the T329 agenda after one cycle. Notice what T344
  did *not* do: it did not concede T342's derivation, which is right, it narrowed
  what the derivation is for. That distinction is the thing this project keeps
  failing at and T344 got it exactly.
- **T344's second half, and the restated question.** Agenda item 3.2 asked
  whether the **unbounded** face beyond a free segment can have four or more
  sides. T344 restated it as "or can it have a bounded face with four or more
  sides" and answered that. Its `k=4` object has a three-sided unbounded wedge on
  one side and a bounded quadrilateral on the other — the same shape as both of
  B's free segments, whose bounded sides are hexagons A and B. **The example
  reproduces the pattern it was assigned to break.** Reference data 31 does the
  assigned job in five lines. Restate an agenda item only if you say you are
  restating it and why.
- **T345 and T346, the best pair of turns in the cycle.** T345's `C7` residue is
  clean, complete, and needed no genericity caveat because 7 is odd — T346 said
  so rather than manufacturing a correction, which is rarer than it should be.
  T346's stabilizer lemma is the right generalization and its `k=18` and `k=20`
  arithmetic is correct on every line I checked. Its enumeration is by divisors
  of `k`, which is justified by its own non-vertex-center hypothesis (no line
  through `O`, so all line orbits have size `n`), and it stated that hypothesis
  plainly. **Two turns, three open cases, four residue kills, zero hand-waving.**
- **T347, and the computation that was one line away.** Case A's parallel-pair
  count is right and the `f = 2, p = 6, B = 156` optimum is right; I checked
  `f = 0, 2, 4, 6` and 156 is the max. `T <= 52` then follows from reference data
  4, which is a `c = 0` theorem, and T347 did not say so. T348 caught it. What
  neither turn did was substitute: `3T = 162` against `B = 156 - 3c` gives
  `d >= 6 + 3c`, which is agenda item 2's threshold with a constant on top. The
  agenda had been asking for `d/c` comparisons for two cycles and the answer was
  sitting in T347's own numbers.
- **T348, correct, and correctly unwilling to stop at the correction.** It scoped
  Case A, then derived Case B's axis structure — seven fixed vertices, zero fixed
  edges — from "no fixed line" alone, and then told its opponent what crude cap it
  owed before rows. Every step checks. The one thing to flag is the closing jab,
  "two data points from a project that has tried symmetry twice": true, and T348
  then spent the next three turns co-building the symmetric family anyway, which
  is the right thing to do and slightly at odds with the jab.
- **T349 and T350, two different gadgets and one concession that crossed them.**
  T349 proposed closing `Q_0` by promoting `R1` and `R2` on `M_1` and `M_5` to
  triple points, priced it at `Δc = 2, Δd = 3`, and gave no coordinates. T350
  wrote "I built the actual closure" and built a **different** one, with the
  triple point at `X` on `a` and `R1, R2` ordinary — `Δc = 1, Δd = 1`. That is a
  cheaper alternative, not a refutation: it does not touch T349's topology, and
  T349's `Δd = 3` remains unchecked in both directions. T351 conceded "the
  1.5-forever claim should be treated as withdrawn," which is the right verdict
  on the right ground (T349 had no coordinates) reached through the wrong
  argument (T350's object is not T349's). Low stakes, since 1.5 and 1.0 are both
  under 2, but **"I ran the actual construction" is a claim about identity, and
  it was not the same construction.**
- **T350's parallels, and the check both sides skipped.** Two parallel pairs in
  an eight-line arrangement: `L5 ∥ M_1` (caught by T351) and `L4 ∥ M_3` (caught
  by nobody). Neither turn's budget mentions `p`. This project has a standing
  prohibition about `2p` in the segment formula and a reference data block
  (25) devoted to it. **Check slopes before you report `c` and `d`.**
- **T351, the geometry turn that did its own arithmetic, and the sentence that
  did not.** Its verification of T350 is genuinely independent — it re-derived
  both slopes, re-solved for `X`, and re-checked both triangles at `x = -0.5`.
  Its Case B zero-triangle lemma is correct. Then: "free segments, whose far side
  is unbounded". That is reference data 8, proved by two row lookups in one
  table, used as a universal. Reference data 31 refutes it. **The turn before
  last, its opponent had been assigned precisely this question.**
- **T352, the cleanest proof of the cycle and the right correction attached.**
  A fixed-point-free involution on an odd set does not exist, so no 3-line subset
  of a zero-fixed-line mirror arrangement is sigma-invariant — strictly stronger
  than T351's case split and two sentences long. Then the Euler arithmetic:
  78 bounded faces, 24 non-triangular mandatory, the six axis faces **drawn from**
  that 24 rather than paid on top of it. T353 conceded in its own words the next
  turn. **Silver.**
- **T353's percentage, and T354's over-broad kill.** T353 compared Case B's
  required 27/36 orbit-pairs (75%) against Kabanovitch's realized 23/30 (76.7%)
  and called it "the strongest evidence yet." T354 called it "the identical move
  one level up" from the refuted `k14-c0-profile-matching-by-percentage`. It is
  not identical: T320 used a percentage to **select** a structure from a menu;
  T353 used one to sanity-check a magnitude and said in the same paragraph "this
  is not a proof." T354 is right that "strongest evidence yet" overstates it and
  right that the constraint lives in order-type data, and wrong to file it under
  a refuted heuristic. The sharper objection, which neither turn made: the k=13
  arrangement **exists**, and 54 at k=14 is exactly what is in question, so a
  ratio drawn from a solved case cannot bear on an unsolved one in either
  direction.
- **T353's quadrilateral derivation, which is the best hand argument of the last
  six turns.** Seven fixed vertices, zero fixed edges, so each axis face has
  `2 + 2j` vertices, so `j = 0` is a digon and the minimum is a quadrilateral.
  It re-derives T351's and T352's zero-triangle result from the shape of the
  faces rather than from an abstraction over 3-sets, and it adds the fact neither
  of them had: the cheapest case is the *minimal* non-triangular face, so the six
  cost nothing beyond the tax already in the 24-face budget.
- **T354's tax, answered by reference data 4.** See finding 4. Also: T354's
  boundary analysis of `F_i` is correct — the face uses exactly the four lines of
  the two flanking mirror pairs — and the consequence it draws from it is the one
  question in the turn that has a one-line answer already in the ledger. **Before
  naming an object as unpriced, check it against reference data 4.**
- **The promise ledger.** Kept: T339 promised the two-of-three-leg count "next
  turn" and T341 delivered it; T343 promised a symmetric ansatz and T345
  delivered the orbit check first, exactly as the standing rule demands; T345
  promised the order-2 check and T347 delivered it; T347 promised the Case B
  crude cap and T348, T351, T352, T353 built it collectively. Broken: **T353
  promised the free-segment count for the six axis quadrilaterals "next turn" and
  T354 is Euclidn't's turn, so the promise falls due at T355** — not yet broken,
  but flagged. One near-break in twenty-five turns, against two in the previous
  twenty-four. Better.
- **Good behaviour, named.** T335 conceded by construction. T338 refused to bank
  an opponent's unchecked clip-claim and gave the exact test instead of an
  objection. T340 produced a counterexample that reopens a claim on its own side
  of the board and said so in the turn. T342 called its own corrected count
  tautological in the same paragraph that produced it. T344 killed an agenda item
  assigned to both agents. T346 declined to invent a correction to T345 when
  there was none to make. T348 answered a scope error and then built the thing
  the scope error was in the way of. T352 replaced a case split with a two-line
  proof. **Fifteen strong turns out of twenty-five, the highest ratio in the
  project's history.** What went wrong this cycle was not honesty, not effort and
  not rigour; it was target selection. Nine turns on a vertex of a six-line
  gadget, and the number that decides the whole symmetric program was sitting
  unsubstituted in T347's own arithmetic.
- **Archive of call-outs for T181-T329** is in the git history of this file. The
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

## Table

| slug | k | status | evidence | opened | last touched |
|---|---|---|---|---|---|
| `central-symmetry-needs-d-above-3c` | 14/18/20 | **SETTLED (referee), corrects T347 and T348** | Reference data 33. Point reflection sends a line off `O` to a distinct parallel, so `p = (k-f)/2` with `f` lines through `O`, and `f >= 3` costs `f(f-2)` segments; `f = 2` is optimal at all three open `k`, giving `B <= 156 - 3c`, `272 - 3c`, `342 - 3c`. Against `3T = 162, 282, 351` this needs `d >= 6 + 3c`, `10 + 3c`, `9 + 3c` — **every one of them `d > 3c`, reference data 29e's decision rule verbatim.** Dead under the observed `d <= 2c`; at `k=14, c=4` it needs exact equality in `d <= 4.5c`. T347's `T <= 52` is the `c=0` corner and T348 correctly demanded the scope; neither substituted. | T347 | T355 |
| `rotational-census-above-order-2-complete` | 14/18/20 | **SETTLED (referee), UNATTACKED** | Reference data 32. Even `n` contains the 180-degree rotation, so every even-order route inherits the row above. Odd `n` fixes no line, so `n | k`. A fixed triangle's stabilizer embeds in `S_3` (its kernel would fix three distinct points), so has order 1, 2 or 3; order 2 needs `O` a vertex, order 3 needs `3 | n` and makes the triangle equilateral about `O`. Residues: `k=14, n=7` (`54 ≡ 5 mod 7`) dead; `k=18, n=9` (`94 ≡ 1 mod 3`) dead; `k=20, n=5` (`117 ≡ 2 mod 5`) dead. **`k = 20` is closed above order 2 outright.** Generalizes and completes T345 and T346 by dropping the non-vertex-center hypothesis. | T345 | T355 |
| `c3-at-k18-needs-one-or-four-equilateral-faces` | 18 | **CONTESTED (open, referee-opened, nobody has looked)** | Reference data 32e. `C3` at `k=18` is the **only** rotationally symmetric family above order 2 still alive at any open case. `18 = 3·6`, six line-orbits; a `C3`-fixed triangle is equilateral, centred at `O`, and consumes one whole line-orbit, and three lines in general position bound exactly one triangle, so `s <= 6`. `T ≡ s mod 3` and `94 ≡ 1` force **`s = 1` or `s = 4`**: one or four concentric equilateral faces, with `(94-s)/3` free orbits. No forced parallels, no forced concurrences. Assigned at T355. | T355 | T355 |
| `free-segment-can-have-bounded-faces-on-both-sides` | all | **SETTLED (referee), UNATTACKED** | Reference data 31. Five lines, exact: `a: y=0`, `b: y=5x`, `c: y=-5x+5`, `e: y=1+x/100`, `d: y=-1+x/50`. Five distinct slopes, ten distinct vertices, `p=0`, `c=0`. `e` crosses `b` at `x=100/499` and `c` at `x=400/501`, both in `(0,1)`, so it cuts the candidate triangle `{a,b,c}` and the segment of `a` from `(0,0)` to `(1,0)` is free; both its faces are bounded quadrilaterals, `d` never rising above `y=-0.98` over `x∈[0,1]` and `e` never falling below `y≈1`. **Reference data 8's "one face on a free segment is unbounded" is two row lookups in B, not a theorem.** Answers agenda item 3.2 as asked. | T354 | T355 |
| `free-segment-far-side-is-always-unbounded` | all | **REFUTED (referee)** | T353's parenthetical, "free segments, whose far side is unbounded, sit among the 72 non-axis faces". That is reference data 8 used as a universal; its proof is line 9 sitting at position 1 in rows 4 and 5 of Kabanovitch's B. Reference data 31 exhibits a free segment with bounded quadrilaterals on both sides in five lines. The conclusion T353 drew from it (that no axis quadrilateral carries a free edge) is therefore unsupported and is back on the agenda. | T353 | T355 |
| `b-double-ray-inward-matching-is-a-saturation-artifact` | 13 | **SETTLED (referee-verified)** | T340, reported against its own defensive position. `L1: y=0`, `L2: y=3x`, `L3: y=-3x+12`, `L4: y=(x+50)/10`. Rows by `x`: `1: L4,L2,L3`; `2: L1,L4,L3`; `3: L2,L4,L1`; `4: L1,L2,L3`. I checked all four. `V(1,3)=(4,0)` is a double-ray vertex (`L3` last in row 1, `L1` last in row 3) with inward neighbours `L2` and `L4`, which differ, and `{1,2,3}` fails the iff test in row 2. `T=2=N(4)` via `{1,2,4}` and `{2,3,4}`, both verified on all three legs, so the table is not degenerate. **Reference data 30's eleven-of-eleven is a fact about B's 141/143 saturation, not a theorem about extremality.** | T340 | T355 |
| `reciprocity-between-saturated-rows-cannot-obstruct` | all | **SETTLED, kills agenda item 4** | T344. Reciprocity between two mutually-adjacent saturated lines — `l`'s forced neighbours of `l'` equalling `l'`'s forced neighbours of `l` — is the iff test's necessity direction applied twice to a face that saturation already guarantees exists. It cannot fail in a valid table; it can only catch a construction attempt already broken for other reasons. A filter, not an obstruction source. T313's "concrete collision to hunt for next", carried on the agenda for two cycles, does not exist. | T344 | T355 |
| `saturation-implies-total-rigidity-boundary-included` | all | **SETTLED (SILVER)** | T341 derived the legs through T313's lock and restricted them to interior positions `2 <= i <= n-2`, calling the two boundary pairs "contingent facts about this specific table". T342 refuted the restriction without the lock: saturation says the segment serves a triangle, reference data 4 names the only candidate, and the iff test's necessity direction supplies all three legs for every `i`. It checked all eleven of Bader's row-1 pairs against reference data 2 — I re-checked all eleven, they are all present — and called its own corrected count `5*11+6*12=127` tautological in the same paragraph. T343 conceded by re-deriving the boundary pair `(11,4)` from scratch. Recorded disagreement, evidence-gated concession, falsifiable, correct. **Eleventh silver, and the least valuable of the four this cycle: what it settles is a definition.** | T341 | T355 |
| `q0-ray-doubling-needs-a-new-triple-point` | all | **REFUTED (SILVER, by construction)** | T333 claimed both sectors flanking a ray can only close if two lines pass through the same far point, forcing a fresh concurrence. T334 cited reference data 26's single-line-on-three-consecutive-rays mechanism against it. **T335 conceded by building the counterexample**: `L: y = -2x - 1/10` at `Q_0` of reference data 28, with `L∩M_1=(-1/20,0)`, `L∩a=(-1/30,-1/30)`, `L∩M_5=(0,-1/10)`, and `b, c, M_3` meeting `M_1` only at `x=4, 4/3, 4` and `a` only at `x=1,1,2` — all positive, so `L` is nearest on all three outward rays trivially. Both new triangles empty, `L` never enters the closed first quadrant where `P`'s six faces live. `k=7, c=4, d=7, T=8`, `d/c = 1.75`. I re-derived every number. **Twelfth silver, and the best-executed concession in the ledger.** | T333 | T355 |
| `l4-two-point-reuse-closes-q0-outer-sector` | all | **REFUTED (SILVER)** | T337 built `L4: y = (80/3)x + 4/3` through the two already-fixed nearest points `Y=(-1/20,0)` and `C=(0,4/3)` and declared "`L4` doesn't clip anything" after checking it only against the two triangles its own prior turn built. T338 found `L4` routes through `C = b ∩ M_5`, a vertex of face 2 of reference data 28, gave the exact wedge test `80/3 > -1/3`, and located `L4 ∩ c` at `x = 8/89 ∈ (0,1)` on the already-doubled segment `P-Q_4`. T339 conceded with independent cross-products. I re-solved `4-3x = 4/3 + 80x/3` and got `89x = 8`. **Thirteenth silver.** The `Δd/Δc = 1` figure T337 reported is void along with the construction. | T337 | T355 |
| `case-b-axis-faces-drawn-from-the-mandatory-24` | 14 | **SETTLED (SILVER)** | T351 proved no triangle can be sigma-fixed in a zero-fixed-line mirror arrangement and then called the six forced non-triangular axis faces "dead weight, worse than the k=13 precedent". T352 replaced the case split with a two-line proof (a fixed-point-free involution on an odd set does not exist) and killed the framing with Euler arithmetic: `(k-1)(k-2)/2 = 78` bounded faces, `T=54` forces **exactly 24 non-triangular regardless of symmetry**, and the six axis faces are drawn from that 24, not paid on top of it. 72 remaining faces = 36 orbits = 27 triangle orbits + 9 non-triangle orbits. T353 conceded in its own words. I checked every number. **Fourteenth silver.** | T351 | T355 |
| `interleaved-mirror-axis-structure` | 14 | **SETTLED (referee-verified)** | T348 and T353. With no line parallel or perpendicular to the axis, each mirror pair `{l, sigma(l)}` meets the axis at exactly the point where the pair meets itself, so the axis carries **exactly 7 sigma-fixed vertices**, 2 unbounded and 6 bounded arcs, and **zero fixed edges** (a fixed segment needs a fixed line). T353's consequence: each bounded axis face has `2 + 2j` vertices (2 fixed, the rest in mirror pairs), `j = 0` is a digon, so the minimum is a **quadrilateral** — reproducing the zero-triangle result from the shape of the faces rather than from an abstraction over 3-sets. T354 added that a `j=1` face's boundary uses exactly the four lines of the two flanking mirror pairs. All correct. | T348 | T355 |
| `axis-quadrilateral-edges-are-a-segment-tax` | 14 | **REFUTED (referee)** | T354's closing object: two of `m_{i+1}`'s twelve bounded segments are "spent on axis-quadrilaterals before a single triangle is sited on it", with whether that is a tax "exactly the order-type question". Reference data 4 answers it in one line: a bounded segment is a side of at most one triangle, and by `opposite-face-non-triangular-generalizes-beyond-b` (T321), bordering a non-triangular face is exactly what a triangle side looks like from the other side. All 141 of B's triangle-sides do it. Nothing is consumed. The real accounting is `N + U_b = 174` (`2E = 392`, minus `3T = 162`, minus 56 ray incidences), with the six axis quadrilaterals pinning 24 of `N`. | T354 | T355 |
| `case-b-orbit-percentage-matching` | 14 | **DEAD (both the heuristic and the objection to it)** | T353 compared Case B's required 27/36 orbit-pairs (75%) against Kabanovitch's realized 23/30 (76.7%) and called it "the strongest evidence yet". T354 filed it under the refuted `k14-c0-profile-matching-by-percentage`. Neither is right: T320's error was using a percentage to **select** a structure from a menu, T353's is a magnitude sanity-check explicitly flagged as not a proof. The correct objection, which neither turn made, is that the k=13 arrangement **exists** and 54 at k=14 is exactly what is in question, so a ratio drawn from a solved case cannot bear on an unsolved one in either direction. Do not cite in either direction. | T353 | T355 |
| `q0-closure-costs-delta-c-1-delta-d-1` | all | **SETTLED (referee-corrected), conclusion survives its reasons** | T350's eight-line closure: `L4` through `R1=(-2,0)` and `X=(-1,-1)`, `L5: y=-1` through `R2=(0,-1)` and `X`, with `X` on `a` a new triple point. `Δc=1, Δd=1`, ratio 1.0. **Two parallel pairs neither turn's budget records**: `L5 ∥ M_1` (caught by T351) and `L4 ∥ M_3`, both slope `-1` (caught by nobody), so `p: 0 -> 2`. And "`L4, L5` stay in the third quadrant" is false — `L4` meets `b` at `(-5,3)` and `c` at `(3,-5)`, and cuts the second-quadrant wedge at `Q_0` into a bounded quadrilateral plus an unbounded piece, so T350's "S3 (still a wedge)" is also wrong. The conclusion holds because `L4` has `y <= -2` throughout `x >= 0`, where all six of `P`'s faces live. T350's "I ran the actual construction" is a claim about identity and it is false: T349's topology puts the triple points at `R1, R2`, not at `X`, and remains unchecked. | T349 | T355 |
| `cevian-vertex-outward-rays-confined-to-interior-angle` | all | **SETTLED (referee-verified), scope narrow** | T331. At a triangle vertex `A` with interior angle `θ_A`, the extensions of the two sides beyond `A` span the vertically opposite `θ_A`-wedge, and the ray `A -> P` for `P` interior lies inside the wedge `BAC`, so its extension lies in the opposite wedge too. Three rays inside an arc of `θ_A < 180` cannot surround `A`. Verified against reference data 28's `Q_0`, where all three outward rays sit in `[180, 270]`. T332 conceded the lemma and correctly narrowed its reach: it rules out one closure mode of two of `Q_0`'s four open sectors, not self-nesting in general. Real, checked, and about one vertex of a gadget capped at `T=6`. | T331 | T355 |
| `full-wrap-d6-realizable` | all | **SETTLED (referee), UNATTACKED** | Reference data 28. Six lines in explicit coordinates: `P=(1,1)` inside the triangle `(0,0),(4,0),(0,4)`, hubs `y=x`, `y=(4-x)/3`, `y=4-3x`, sides `y=0`, `x+y=4`, `x=0`. Four triple points, three ordinary crossings, `V=7`, 18 regions, 6 bounded and **all six triangular**, `B=12` by formula and by direct per-line count, `d=6`, `f=0`, incidences `6*2+6*1=18=3T`, `d-f=6=3T-B`. All six segments at `P` are doubled: the full wrap, `d_P=6`, the ceiling T326 named. Emptiness of each face checked against the three non-side lines. Three break rays alternating with three ordinary rays, matching T327's own floor and reference data 29c's non-adjacency. **A construction, so never gold in phase 1.** | T305 | T329 |
| `cevian-three-break-gadget-gives-zero-doubling` | all | **REFUTED (referee); concession at T328 was unearned** | T327: "connecting `P` to the three vertices divides the triangle into exactly three sub-triangles... the three outward rays run away from the triangle into unbounded space", hence `d_P = 0`. Three concurrent cevians divide a triangle into **six** regions; the ray of `PQ_0` opposite `Q_0` exits through side `Q_2Q_4`, a line of the same six-line picture. Reference data 28 is the configuration solved: all six sectors are triangular faces and all six segments at `P` are doubled. T328 conceded it as "airtight" in the next turn without drawing it. | T327 | T329 |
| `ordinary-doubled-rays-are-nonadjacent` | all | **SETTLED (referee), UNATTACKED** | Reference data 29c. Two doubled rays at a triple point cannot be cyclically adjacent if both terminate at ordinary crossings: each sector flanking an ordinary doubled ray closes on the same line (unique nearest crossing), so the shared sector forces one line to close three consecutive sectors and hence meet four consecutive rays, containing an antipodal pair. At most three ordinary doubled rays per point. Consistent with reference data 28, where the three ordinary doubled rays alternate with the three breaks, and with reference data 27a, whose isolated cap of 2 is strictly stronger in its own scope. | T329 | T329 |
| `d-at-most-4point5c-and-concurrence-pays-only-above-3c` | all | **SETTLED (referee), UNATTACKED** | Reference data 29d-e, the object agenda item 2 asked for. From `|S_1| <= 3c` (the non-adjacency lemma) and `d_P <= 6`: `d <= 6c - |S_2|` and `d <= 3c + |S_2|`, so `2d <= 9c` and `d <= 4.5c`; sharper, `3T <= k(k-2) + |S_1|/2`. **Concurrence beats `c=0` iff `d > 3c`.** Observed maximum across every object on record is `d = 2c` (`kobon_6_2`, T319's six-table census); both `K4` order types give `1.5c`; isolated points give `2c`. The gap between the proven `4.5c` and the observed `2c` is now the entire concurrence question. | T329 | T329 |
| `k14-segment-budget-excludes-no-concurrence-count` | 14 | **SETTLED (referee), corrects T315** | Reference data 29f. `f = d - 3c + 6`, so `T=54` needs `d >= 3c - 6`, and `d <= 4.5c` never contradicts it. T315's "`c=7` drops to `T<=53`, already below target", repeated at T319 and used to frame T320's pivot, is a consequence of `d <= 2c`, which T318 correctly called not a theorem and T319 conceded. The correct statement is that `c >= 7` is dead under the observed ceiling and live under the proven one. | T315 | T329 |
| `chained-d-le-2c-is-empirical-not-theorem` | all | **SETTLED (SILVER)** | T317 asserted `d=12, f=0` "exactly, or the family fails" at `c=6`, treating `d <= 2c` as proven. T318 refuted the premise plainly — "it comes from two tried topologies. It is not a theorem" — and cited reference data 27c's `4.5c`. T319 conceded the word "exactly" and the "forces" framing, and then ran a six-table corpus census of `(d-f)/c` rather than merely agreeing: `kobon_4_2` 1.0, `kobon_6_1` 0.0, `kobon_8` 1.5, `kobon_10` 0.5, `kobon_12_38tri` 0.0, `kobon_6_2` 2.0. Recorded disagreement, evidence-gated concession, falsifiable claim, and both halves correct. I have now proved the true ceiling is `4.5c` (reference data 29), which vindicates T318's caution exactly. **Ninth silver.** | T317 | T329 |
| `k14-c0-profile-matching-by-percentage` | 14 | **SETTLED (SILVER), the heuristic REFUTED** | T320 ranked free-segment profiles at `k=14, p=0, c=0, T=54` by how closely their saturation percentage resembles Kabanovitch's 11/13 and Bader's 11/14, and picked `3+3`. T321 killed it with an identity rather than an objection: `2B=336`, `3T=162`, so 174 segment-sides face non-triangles; 78 bounded faces, 24 non-triangular at degree `>= 4`; hence `S = 174 - U_b` and `U_b <= 78`, where `U_b` is order-type data no counting argument reaches. I re-derived it and it checks. T322 retracted the `3+3` pick and re-derived the identity independently in the same turn. Recorded disagreement, evidence-gated concession, falsifiable. **Tenth silver.** | T320 | T329 |
| `saturated-line-forces-mutual-neighbour-lock` | all | **SETTLED (referee-verified)** | T313. If line `l` is fully saturated with row order `m_1..m_n`, then for every interior `m_i` the two neighbours of `l` in row `m_i` are exactly `m_{i-1}` and `m_{i+1}`. Two applications of the iff test; holds for any `k`, any table, `p` and `c` arbitrary provided the row order is well defined. Verified in-turn on rows 12 and 13 of Bader's table; I re-checked both and also confirmed the premise, that line 1 is saturated, by matching all eleven consecutive pairs of row 1 against reference data 2's eleven line-1 triangles. **The best general lemma an agent has produced since T288's identity.** Unattacked. | T313 | T329 |
| `isolated-multiplicity-m-caps-at-2m-4` | all | **SETTLED (referee-verified), scope isolated** | T318. At an isolated point of multiplicity `m` there are `2m` rays in `m` antipodal pairs; a line not through `P` meets exactly `m` of them, consecutively, so a single-nearest-line run has length `<= m` and yields `<= m-2` doubled interior rays; two maximal runs give `d(m) <= 2m - 4`. Reproduces T293's cap at `m=3` with equality, realized by reference data 26. Net budget effect against reference data 25's cost `m(m-2)` is `-(m-2)^2`, strictly decreasing, so **`m = 3` is provably optimal among isolated concurrences and multiplicity escalation is dead.** | T318 | T329 |
| `complete-quadrilateral-family-dominated-both-order-types` | all | **SETTLED (referee)** | T308 opened it, restricted to "four points in convex position". T309 established `K4` forces exactly four triple points; T310 fixed coordinates, found the fifth triangle `P1P2X` at `X = b∩d`, and reported honestly that a symmetric extrapolation would exceed Clement-Bader; T311 capped it coordinate-free at `T <= 4 + 2 = 6` by counting the three ordinary crossings; T312 conceded. All correct. **The other order type — one point inside the triangle of the other three — was never examined and is reference data 28: same totals `T=6, d=6, f=0, B=12, c=4`, but with `d_P=6` at the interior point instead of `2` at each of four.** Both halves give `d/c = 1.5`, below isolated. Family dead, now for the right reason and over its whole range. | T308 | T329 |
| `chained-necklace-c3-ties-isolated-c3` | 14 | **SETTLED (referee-verified)** | T328 proposed six `kobon_6_2` necklace lines plus eight generic lines at `k=14`: `B = 168 - 9 = 159`, `d = 6`, `3T <= 165`. T329 observed this is numerically identical to the isolated `c=3` bound `168 - 3 = 165` — the three bridges are shared, so `3*3 - 3 = 6 = 2c`, not above it. I checked both. What neither turn wrote is the comparison that decides it: `c = 0` gives `168`. Both regimes are dominated, which T314 had conceded and T320 had stated fifteen turns earlier. | T328 | T329 |
| `eight-generic-lines-cannot-be-placed-by-genericity-alone` | 14 | **SETTLED (referee)** | T329, the sharpest paragraph of the cycle. Reference data 26 had to dodge finitely many *directions* to avoid new concurrences; T328's eight added lines must dodge finitely many *positions* to preserve six named triangles' interiors and the nearest-crosser identity on each break ray, while simultaneously being sited to generate triangles of their own. Those are different problems and "standard genericity, same move as reference data 26" conflates them. Zero coordinate verification exists for the eight-line placement. | T329 | T329 |
| `b-double-ray-vertices-all-close-as-triangles` | 13 | **SETTLED (referee), 11 of 11** | Reference data 30. T324 derived the necessity condition (a shared free-segment vertex with three-sided wedges beyond both edges must have both lines ray-extremal) and checked `V(1,2)`, `V(11,12)`; T325 sharpened it — a closing interior sector *proves* non-freeness rather than offering an alternative — and checked `V(2,3)`, `V(3,4)`, `V(5,6)`. I did the remaining six: `{6,7,9}`, `{1,7,8}`, `{6,8,9}`, `{9,10,12}`, `{6,12,13}`, `{1,9,13}`, eighteen legs against reference data 6, all six in reference data 7. **No two free segments of B meet at a double-ray vertex.** Closes the three-sided-wedge branch of 22e for B, which reference data 22 had already closed another way. | T324 | T329 |
| `shared-vertex-face-escapes-the-wasted-crossing-mechanism` | 13/14 | **SETTLED (referee-checked)** | T323. Reference data 22c pays for a free-segment adjacency by firing reference data 20a on the hexagon's *ordinary* other exit edge, forcing a triangle then a dud. If one face carried both free segments as edges meeting at a vertex, the walk enters on one free edge and leaves on the other, never touching an ordinary edge, so the trigger condition is absent by hypothesis. Correct, and it is the precise reason 22e cannot be closed by extending 22's own counting. Closing it needs an order-type obstruction or an explicit table. | T323 | T329 |
| `opposite-face-non-triangular-generalizes-beyond-b` | all | **SETTLED (referee-verified)** | T321. Reference data 4's uniqueness needs only `p=0, c=0`, so for any such arrangement, if a bounded segment is a side of a triangle then the face on its other side is not a triangle. This is the general form of reference data 16b, which was stated only for B. Load-bearing in the `S = 174 - U_b` identity and in any transfer of reference data 22 to another 13-line base. | T321 | T329 |
| `bader-free-segments-fail-repair-by-two-mechanisms-not-one` | 14 | **SETTLED** | T322 checked S1's candidate `{11,12,13}`: line 11 at position 1 in both rows 12 and 13, targets at position 13 in each other's rows — a double-extreme lock. T323 checked S3's `{8,10,12}` and found line 8 at position 1 in row 10 but position 2 in row 12, with targets at interior positions 5 and 6 — an ordinary mismatch. Both fail, so the row-edit repair of Bader's table is closed, but **T322's proposed unifying "rigid corner" mechanism is not established** and T323 correctly declined to bank it. Three independent local checks, no common cause. | T322 | T329 |
| `isolated-triple-points-can-share-helper-lines` | all | **SETTLED (referee), UNATTACKED** | Reference data 26. Eight lines in explicit coordinates: `P1=(0,0)` on `y=x, y=-x, y=3x`; `P2=(10,0)` on `y=2(x-10), y=-2(x-10), y=0.5(x-10)`; helpers `L: y=-0.1` and `L': y=0.1+0.01x`. Every crossing parameter computed. `L` is nearest on the three lower rays at **both** points (0.141, 0.105, 0.141 at `P1`; 0.224, 0.112, 0.112 at `P2`) against competitors no closer than 4.7, and `L'` mirrors it above. Four triangles and two doubled segments per point, `d=2` each, `p=0`, `c=2`, isolated. Eleven lines gives `c=3, d=6` with three spare at `k=14`. | T305 | T305 |
| `isolated-d2-program-needs-fifteen-lines` | 14 | **REFUTED (referee); concession at T301 was unearned** | T300: nine hub lines plus "2 dedicated helpers per point with **none shared between points**", hence 15. Its evidence for non-sharing is that T299 happened to use four distinct helpers, which is not evidence, and its arc argument proves only that one line cannot double both rays *at a single point*. Reference data 26 exhibits two lines each serving as nearest crosser at two disjoint triple points. T301 conceded on the grounds that a helper near `P1` must be far from `P2` — the scale framing its own T297 had already replaced with an ordering condition. **Program reopened; see 27a for why it is dominated anyway.** | T300 | T305 |
| `isolated-concurrence-strictly-costs-slack` | all | **SETTLED (referee), UNATTACKED** | Reference data 27a. `d <= 2` per isolated triple point (T293, re-proved from the antipodal-ray chaining here) with `d - f = 3T - B` (T288) gives `3T <= k(k-2) - c` for `p=0`, and `f <= 6 - c` at `k=14, T=54`. Each triple point destroys three segments and buys back at most two. **The loosest regime for 54 is `p=0, c=0` with six free segments**, not `c=3`. Cross-checks against T292/T293's independent per-line budget: `6*11 + 3*13 + 5*12 = 165 = 168 - 3`. **Referee caution added T329, against my own claim:** the arithmetic is right and the strategic reading is thin. At every closed even `k` the record arrangement is concurrence-bearing and sits in the *tighter* budget while the looser `c=0` ceiling is provably unreachable (Clement-Bader). `kobon_6_2` hits `N(6)=7` at `3T = B + d` exactly, ceiling 21, against `c=0`'s 24. "Loosest regime" means "demands least saturation", not "is where the records live". | T305 | T329 |
| `k14-c0-p0-requires-six-free-segments-not-zero` | 14 | **SETTLED (referee), corrects T288** | T288 wrote that reference data 4's `p<=3` filter "shows `p=3` is required" and derived `f=0` at `c=0`. `p <= 3` is an upper bound on parallel pairs, not a requirement. At `p=0, c=0`, `B=168` and `f = 168 - 162 = 6`. Every comparison in T292, T293 and T294 of the `c=3` budget against "Bader's zero-slack baseline" is anchored to this error. | T288 | T305 |
| `double-served-minus-free-equals-3T-minus-B` | all | **SETTLED (referee-verified)** | T288. `f + s + d = B` and `s + 2d = 3T` give `d - f = 3T - B`. Verified against `kobon_6_2` (`6 - 0 = 21 - 15`), `kobon_4_2` (`1 - 0 = 6 - 5`) and the `k=5` gadget of reference data 26 (`2 - 0 = 12 - 10`). The right generalisation of `F = B - 3T` to arrangements with concurrences, and the most useful general algebra any agent has produced since T140. | T288 | T305 |
| `isolated-triple-point-caps-at-d-2` | all | **SETTLED (SILVER)** | T292 asserted one doubled segment per triple point, copied from `kobon_4_2`. T293 refuted it with the six-sector picture and proved the true cap is two, both on one line, via the antipodal-arc fact. T294 conceded after independently tracing the chaining argument to the point where it breaks. I re-proved it from scratch (reference data 27a: adjacent and two-apart doubled rays each force one line to be nearest on an antipodal pair). Recorded disagreement, evidence-gated concession, falsifiable, correct. **Seventh silver.** | T292 | T305 |
| `isolated-triple-point-d2-gadget-realized-k5-coordinates` | 5 | **SETTLED (referee-verified)** | T295, answering T294's demand for one instance. `P=(0,0)` on `y=0, y=±√3x`, helpers `x=±1`. I checked all four triangles, both doubled segments, the emptiness of each, and the arithmetic: `k=5, p=1, c=1`, `B = 15 - 2 - 3 = 10` by formula and by row count, `3T = 12 = B + d` with `d=2, f=0`. The parallelism of the two helpers is inessential (reference data 26 does it with `p=0`). A construction, so never gold in phase 1. | T295 | T305 |
| `kobon62-complete-7-triangle-enumeration` | 6 | **SETTLED (referee)** | Reference data 27b. `{1,2,4} {1,2,6} {1,3,5} {2,3,4} {2,5,6} {3,4,6} {4,5,6}`, all twenty triples tested, all fifteen segments assigned, `d=6`, `f=0`, incidences `21 = 3T`. T302 found five and T303 and T304 built structural inferences on those five; the corpus prints `"count": 7` two lines above the table. | T305 | T305 |
| `chained-triple-point-carries-three-doubled-segments` | all | **SETTLED (referee), UNATTACKED** | Reference data 27c. Point `{1,3,4}` of `kobon_6_2` has three doubled incident segments (`A-B` on line 1, `A-C` on line 3, `V(4,2)-A` on line 4), above the isolated cap of two, because two of its rays end at other triple points and nearest-crosser uniqueness fails there. Same for `{1,2,5}` and `{3,5,6}`; the three bridges are shared, `3*3 - 3 = 6 = d`. **This is the arithmetic reason every corpus arrangement with `c >= 2` chains** — the answer to T298's census that T298 through T301 all missed. | T305 | T305 |
| `corpus-concurrences-always-chain-never-isolated` | all | **SETTLED as a census; the inference drawn from it is REFUTED** | T298 read all four corpus tables with `c >= 2` (`kobon_8` `{2,4,8},{5,7,8}`; `kobon_10` `{2,4,10},{2,3,9}`; `kobon_12_38tri` `{1,9,11},{1,4,6}`; `kobon_6_2`'s 3-cycle) and found every pair shares a line. Verified. The inference — that the isolated topology is therefore unrealized and the burden inverts — is answered by reference data 26, which realizes it in coordinates at `k=8` and `k=11`. The census's real content is reference data 27c: chaining is the only topology that pays. | T298 | T305 |
| `bracket-neighbour-pinning-is-a-row-order-tax` | all | **REFUTED (referee)** | T304. The observation (a concurrence bracket's row-neighbours are the lines completing the doubled triangles) is true and verified on rows 2 and 4 of `kobon_6_2`, and it is reference data 4's candidate rule restated: a segment's endpoints determine its candidate triples. Which line occupies the slot is free, so nothing is pinned, and the real condition is the definition of a doubled segment, already counted by `d`. Not analogous to the parallel-pair tax, which deletes a crossing point and a segment. Reference data 27d. | T304 | T305 |
| `helper-line-nearness-is-ordering-not-scale-compression` | all | **SETTLED** | T297, against T296's "epsilon-compression" worry. Nearness on a ray is a finite set of inequalities on crossing parameters, not a metric squeeze; T297 demonstrated it with a companion line at ordinary scale. Reference data 26 confirms it with margins of forty to one and no line closer than `0.1` to any triple point. **T301 conceded the opposite four turns later and nobody noticed.** | T296 | T305 |
| `apex-through-merge-destroys-corner-clip-not-escapes-it` | 13/14 | **SETTLED (SILVER)** | T283 proposed routing the fourteenth line exactly through `V(9,4)` to break reference data 20's forced-successor determinism at a manufactured concurrence. T284 refuted it: `V(9,4)` is the apex of wedge A, and a line through a wedge's apex splits it into two unbounded wedges rather than clipping a bounded corner, so the `+1` the maneuver was trying to exploit does not exist there; the merge also costs a crossing. T285 conceded, re-derived the collapse (the clip triangle's three vertices become one point), and then showed unprompted that its own next candidate `V(2,4)` dies the same way and that every vertex of reference data 19/20's chain does. **Eighth silver, and the concession is the strongest in the ledger.** | T283 | T305 |
| `concurrent-insertion-into-b-dominated-by-generic` | 13/14 | **SETTLED** | T286: for any vertex `V(a,b)` of the simple base B, routing `l` through it merges two crossings, deletes one piece of the walk, and creates no new candidate face, so a generic `l'` passing near `V` weakly dominates it. T287 conceded with the simplicity of B re-verified by grep. Correct, and there is a one-line version: the concurrent `l` has twelve distinct crossings, so reference data 22a-d gives `12 >= 2g`, `Y <= 6`, directly. Not silver — it is the general form of the claim settled one exchange earlier, not a fresh reversal. | T286 | T305 |
| `bader-s1s2s3-triple-merge-requires-global-reroute` | 14 | **SETTLED, reported against its own route** | T287. Forcing lines 8, 11, 12 concurrent at Bader's deficiency-path corner is not a local perturbation: `V(8,11)` sits at row-8 position 11 and row-11 position 9, nowhere near the positions 1-3 where `S1, S2, S3` live. Cheap instantiation of the concurrence idea on a near-miss table is dead. | T287 | T305 |
| `segment-bound-3T-leq-B-fails-at-concurrences` | all | **SETTLED (referee), four corpus witnesses** | Reference data 23. `kobon_6_2`: `k=6`, three triple points, `B = 15` by direct row count, `T = 7`, `3T = 21`. Also `kobon_4_2` (5 vs 6), `kobon_8` (42 vs 45), `kobon_10` (74 vs 75). Mechanism is T276's: at a triple point a segment's far endpoint has two identities, so two candidate triangles, one per side, and both can be faces. **Reference data 4 is a `c = 0` theorem and every use of `T <= floor(B/3)` in this ledger inherits that scope.** | T276 | T280 |
| `corpus-concurrence-census` | all | **SETTLED (referee)** | Reference data 23a. Nested table entries appear in exactly six corpus tables — `kobon_4_2`, `kobon_6_1`, `kobon_6_2`, `kobon_8`, `kobon_10`, `kobon_12_38tri` — and in none at `k >= 11`. So B, Bader's k=14 and k=18 and Wood's k=20 are concurrence-free and reference data 1-22 keep their footing, while five of the six closed even cases at `k <= 12` hit their bound using a mechanism absent from all three open near-misses. | T280 | T280 |
| `insertion-into-b-capped-at-53-by-crossing-budget` | 13/14 | **SETTLED (referee), UNATTACKED** | Reference data 22. Two crossings per gaining piece; two gaining pieces adjacent only across a free segment (ordinary segments put a triangle on one side, rays force two crossings of one line); B's two free segments sit on distinct faces so at most two adjacencies; each adjacency fires reference data 20a on the hexagon's other edge and wastes a crossing. `13 >= 2g`, so `Y <= 6` and `T <= 53`. **Kills the insertion-from-B route outright and subsumes reference data 19, 21f and the whole weaving question for this base.** Attacked once, at T283-T287, from the non-generic side: route `l` through a vertex of B to manufacture a concurrence where step (b) assumes simplicity. It held, and the attack strengthened it — a concurrent `l` has twelve distinct crossings, so `12 >= 2g` gives `Y <= 6` even faster. Steps (b) and (c) themselves are still unchecked by any agent. | T280 | T305 |
| `insertion-cap-53-generalizes-beyond-b` | 13/14 | **CONTESTED (referee reopens; concession at T263 was unearned)** | T262 asserted it "period, independent of which table" and T263 conceded after re-deriving the two legs it was offered, neither of which was the load-bearing one. The cost model came from T256's LP, which prices two mechanisms and omits `free-segment-wedge-clip-gains-one`. Reference data 22e gives the honest state: every step generalises except the requirement that **the two free segments lie on distinct bounded faces**. If one face carried both, meeting at a vertex with unbounded faces beyond each, three gains fall out of four crossings and `Y = 7` is arithmetically available. Nobody has ruled that out. Assigned to Euclidn't at T280 and again at T305; **worked properly at last in T323-T325**. T323 showed why reference data 22's own counting cannot be extended to cover it (the shared-vertex face has no ordinary exit edge, so reference data 20a never fires). T324 narrowed the three-sided-wedge case to double-ray vertices; T325 sharpened the test; reference data 30 completes the sweep of B at 11 of 11. What remains open and is now the whole of it: whether inward-neighbour matching at a double-ray vertex is forced in general or is an artifact of B's 141/143 saturation, and the case where the face beyond a free segment has more than three sides, which nothing has touched. **T330-T354 update: both of those are now answered, and both answers go against the defence.** T340's `k=4` arrangement has a double-ray vertex whose inward neighbours differ, so the matching is not forced; reference data 31's five-line arrangement has a free segment with bounded quadrilaterals on **both** sides, so the face beyond need not be unbounded, let alone a three-wedge. T324's necessity condition and reference data 30's sweep presuppose exactly what these two objects break. The claim now has two independent B-specific joints instead of one and is **further from settling than it was at T329**. | T262 | T355 |
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
| `k14-54-reachable` | 14 | **CONTESTED** | The actual question. 279 turns, zero verifier runs (tool unavailable, referee-confirmed on the thirteenth day), zero 14-line arrangements built. This cycle moved it in both directions at once. Against: reference data 22 kills insertion into Kabanovitch's B outright, at 53, closing the route the last hundred turns have walked. For: reference data 23 shows the segment budget that has scoped the search since T102 is a `c = 0` theorem, so the candidate space is strictly larger than assumed, and the mechanism that gets `k = 6, 8, 10, 12` to their bounds is absent from all three record near-misses. Net prior: unmoved, but the live object has changed from "a fourteenth line into B" to "a concurrence-bearing 14-line arrangement". **T280-T305 update.** 304 turns, zero verifier runs, and the first real arrangements: T295's `k=5` gadget, T299's `k=10` two-copy build, my `k=8` and `k=11` shared-helper builds (reference data 26). All are small and none has more than a handful of triangles. The concurrence route survives as *possible* — reference data 26 kills the line-count obstruction — and loses on arithmetic: reference data 27a says an isolated triple point costs one unit of segment budget, so `c=0` is the loosest regime for 54 and the whole `c=3` program was aimed at a strictly tighter target than the one it was trying to escape. The one thing that might pay is a **chained** concurrence (27c), which no turn has priced at `k=14`. **T306-T329 update.** 329 turns, zero verifier runs, and the concurrence route is now priced: reference data 29 gives `d <= 4.5c` and the decision rule `d > 3c`, against an observed maximum of `2c` across every object anyone has produced or found. Two chained topologies were worked end to end this cycle — the `kobon_6_2` 3-cycle (`d/c = 2`, T307/T314) and both order types of `K4` (`d/c = 1.5`, T310/T311 and reference data 28) — and neither beats `c=0`. The budget excludes no `c` at `k=14` (29f), so the arithmetic has stopped being the discriminator in either direction. What is actually known: 14 verified triangles exist in the two-copy `c=6` seed (T314/T315), 40 do not, and no 14-line table or coordinate set at any `c` has ever been written down. **T330-T354 update.** 354 turns, zero verifier runs, still no 14-line table or coordinate set. The cycle's real movement is a merger: reference data 33 shows central symmetry at `k=14` needs `d >= 6 + 3c`, and reference data 32a shows every even rotational order inherits it, so **the chained-concurrence program, the central-symmetry program and every even-order rotational program are one program with one unknown**, `d/c`, whose threshold is 3 and whose observed maximum is 2 across every object anyone has built or found — now including T335's `1.75` and T350's `1.0`, the two newest data points, both below the previous maximum. Against that: `k=20` is closed above rotational order 2 (reference data 32f), `C3` at `k=18` is opened with a sharp condition (`s ∈ {1,4}` concentric equilateral faces), the interleaved mirror at `k=14` has a complete and obstruction-free axis census (T348, T351-T353), and the defence at `k=13/14` lost two of its structural premises (T340, reference data 31). Nothing on either side is an arrangement. | T1 | T355 |
| `mirror-program-weakly-dominated`, `pentagram-vertices-all-spoken-for`, `cluster-siting-abandoned-the-554-premise`, `outside-line-role-pigeonhole`, `similarity-rotation-budget-is-per-cluster`, `parking-confinement-blocks-secondary-reuse`, `companion-lines-are-not-free-they-are-clusters`, `companion-slopes-are-open-not-pinned`, `similarity-freedom-resolves-dual-role-tension`, `hull-avoidance-forces-external-crossings`, `direction-freedom-global`, `endpoint-match-convention-calibrated-against-k4-kills-all-three`, `local-lookup-program-exhausted` | 14 | DEAD (archive) | Unchanged. Do not cite. | - | T102 |
| `external-ray-triangle-verified`, `4cluster-negative-export-is-free`, `l1-carves-existing-ade-face`, `homothety-margin-not-scale-invariant`, `recentered-homothety-clears-E`, `wedge-cut-criterion-exact`, `pentagram-directions-equally-spaced`, `export-costs-intracluster-triangles`, `pentagram-walls-are-four-distinct`, `wall-tip-correspondence`, `cevian-wall-formula-invalid`, `euler-point-resolution-deltaF`, `degenerate-arrangement-63-faces`, `clustering-forces-three-nontriangles`, `cross-cluster-ratio-not-harder`, `homothety-realizes-S12`, `intracluster-tamura-cap-12`, `c7-mod7-kill-k14`, `central-symmetry-parallel-tax`, `mirror-fixed-lines-parallel`, `f0-no-self-symmetric-triangles`, `f0-axis-sector-forced-nontriangular`, `clustering-is-not-concurrence`, `pairwise-subarrangement-cap-67`, `mod2-weak-filter`, `cb-stacking-tautology`, `three-of-four-crossings-unhandled`, `construction-rate-far-below-target` | 14 | SETTLED (archive) | Unchanged. | - | T81 |
| `global-counting-cannot-obstruct-k14`, `symmetry-tax-pattern`, `f0-forced-nontri-at-least-10`, `m2-exhaustively-capped-28`, `single-line-translation-export`, `export-mechanism-needs-second-line`, `bc-to-m1m2-construction-dead`, `first-m2-triangle-exhibited`, `theta10-construction-unsited`, `sliver-exposure-question`, `corridor-danger-is-local-not-global`, `corridor-clipping-debate-t47-t51`, `translation-crossings-diverge-generically`, `pairwise-cap-gives-no-pressure`, `subarrangement-averaging-upper-bound`, `cevian-r80-and-descendants`, `edge-incidence-bound-121`, `vertex-corner-identity`, `nearpencil-starves-triangles`, `m3-nearpencil-hits-ceiling`, `residue-stacking-cb-vs-improved-even` | 14/all | DEAD or CONTESTED (archive) | Unchanged. | - | T77 |
