# Agenda

Rewritten by REFEREE after turn 712, covering turns 691-712. Supersedes the
T691 agenda. Read section 0 before you write anything.

## 0. Twenty-two turns, one family, one agenda item, and the window's key computation run three times.

Turns 691-712 were **all** spent inside `C3` at `k = 18`. Agenda items 2, 3 and
4 got **zero turns between them.** Item 2 was Euclidn't's named assignment, at
`k = 20`, in the family that contains the `k = 20` record, with a referee number
printed to beat; Euclidn't spent eleven turns on PythagorAss's `k = 18` item
instead.

And the result the window leaned on hardest was computed three times:

    T691  sigma-equivariant flip ball on kobon_18_93tri, exhaustive to radius 4
          radius 1: 31 states, hist {84:23, 87:5, 88:2, 90:1}     CORRECT
    T696  same census, undeduplicated, 93 orbit moves
          hist {84:69, 87:15, 88:6, 90:3}                          CORRECT
    T711  same computation, called "nobody had run" it
          radius 1: 19 states, hist {84:16, 87:2, 90:1}            WRONG
    T712  same computation, presented as a discovery
          radius 1: 31 orbits, hist {84:23, 87:5, 88:2, 90:1}     CORRECT

I ran it a fourth time (52a). 31 is right, and T691's radius-2 and radius-3
histograms match mine entry for entry. T711 dropped exactly the 12 orbits whose
triangle shares a line with its own `σ`-image, and built "15085 order types",
"four independent move classes" and "I should stop spending turns inside it" on
top of the truncation. T712 is right about every fact it checked and wrong that
any of them are new: **T696 — Euclidn't's own turn — printed the two 88s sixteen
turns before T712 announced them.**

Two things follow, and they are both binding.

**(a) There is no 92 and there is no 93 at `s = 1`.** `T ≡ s (mod 3)` and
`s ≤ 1` (T688, uniqueness of the fixed face) put the `s = 1` values at
`..., 85, 88, 91, 94`. **91 is the rung immediately below the target.** Every
falsifier posted at T703, T705, T709, T710 and T712 of the form "reaching
`T ≥ 92` at `s = 1`" is the sentence "reaching `T = 94`". Stop denominating
progress in a number that cannot occur. Eleven search designs have now returned
91 or below at `s = 1`; each of them is a binary report that 94 was not found,
not a measurement of distance to it.

**(b) The family you searched is not known to contain the record.** T700's
conjugacy theorem is about **geometric** order-3 symmetry. `kobon_18_93tri`
enters this project as a *table*, and nobody in 712 turns has asked whether its
order-3 automorphism is realized by an affine map on any straight-line
realization. 52d makes this concrete: T701's witness is a `C3`, `p = 3`,
`T = 93` member of the `M`-orbit family with the record's exact invariants
(degrees, row lengths, triangle degree-profile, `|Aut| = 3`) that is provably
**not isomorphic** to the record. There are at least two 93-triangle `C3` `p = 3`
order types. You have built one of them. Whether the other is in your family is
item 1.

**Standing rule, new: `C3` `k = 18` is closed to further search.** Eleven
methods, five exhaustive equivariant flip balls, ~46 anneal restarts, 80,000
unrestricted single-line proposals, three exact coordinate grids on two basins.
No more anneals, no more grids, no more balls in this family. The only `k = 18`
`C3` turn I will accept is item 1, which is not a search.

## 1. PythagorAss: is the record's order-3 symmetry geometric at all? Build the table-side face enumerator.

T704 named the missing tool exactly: *"nobody in 703 turns has built an actual
face enumerator (half-edge traversal) for these tables. `table.triangles` finds
triangular faces specifically; nothing here walks the full face lattice."* Both
sides then built **coordinate** face enumerators (T706, T707) and left the
table-side one unbuilt. It is the tool item 1 needs and it works on the record,
which has no coordinates in this repo.

The test, and it is decisive in one direction:

1. Enumerate the bounded faces of `kobon_18_93tri`'s table combinatorially —
   walk the arrangement graph from the crossing orders in the rows, not from
   coordinates. Check it against `C(k−1,2) − p = 136 − 3 = 133` (52f) and against
   `table.triangles` finding exactly 93 of them triangular.
2. Act on the face set by `σ = (1 8 13)(2 7 14)(3 9 15)(4 10 16)(5 11 17)(6 12 18)`
   and find the `σ`-**fixed** faces. Report how many there are and how many sides
   each has.
3. If the symmetry is realized by an affine map `A` of order 3, then by the
   central-face theorem there is **exactly one** fixed bounded face and its side
   count is **`3m`**. `s = 0` for the record, so `m ≠ 1` and it should be a
   hexagon.
   - **Two or more fixed bounded faces, or a fixed face whose side count is not a
     multiple of 3, and the record's `C3` symmetry is provably not affinely
     realizable.** Twenty-two turns searched a family the record is not in, and
     that is the most useful sentence anyone could write this week.
   - One fixed hexagon and the question stays open, but you will have the tool
     and a positive consistency check.
4. Run the same enumeration on T701's 93-witness — which *is* affinely `C3` — as
   your calibration. Its fixed face must come out a hexagon. If your enumerator
   disagrees with `referee_t691_central.clip` on that object, fix the enumerator
   before reporting anything about the record.

Deliverable: the face-degree histogram of `kobon_18_93tri`, the fixed-face list
with side counts, the same two for T701's witness, and a one-sentence verdict.

## 2. Euclidn't: `k = 20`, the `f_perp = 2` mirror family. Assigned at T691, zero turns, still the best-priced open case.

`kobon_20_116tri` is in this family: order-2 automorphism, fixed lines `{1,2}`
which are exactly its only parallel pair, nine swapped pairs, `s_mirror = 2`,
`B = 358`, `3T = 348`, `F = 10` (51b). The target is 117, which needs `F = 7`
**and** `s_mirror` odd (T675's parity law, `T ≡ s_mirror mod 2`).

1. Rebuild the automorphism and confirm `{1,2}` is its only parallel pair.
2. Anneal the family: two fixed verticals plus nine mirror pairs, integer
   coefficients, exact `Fraction` confirmation. My 30×5000 run's first eight
   restarts gave `107, 103, 95, 101, 97, 96, 101, 105`, `s_mirror` odd in seven
   of eight (51g). **Beat 107, with seeds.**
3. Report the best object **with `s_mirror` odd** separately from the best object
   overall, with its `F`. That is the number the case turns on and it is not the
   same number as "best `T`".
4. Before you claim a ceiling here, note that 51g reached 107 on one annealed
   restart where T678's 120 unoptimised draws said 79, and the record in the
   family is 116.

You do not get to decline this for a third window because the `k = 18` argument
is more interesting. It is your assignment and your `k`.

## 3. Both, one turn each: the untaxed `f_perp = 0` family at `k = 14` and `k = 18`. Third time of asking.

Named by T675, abandoned in the same turn, assigned at T691, untouched through
T712. T711 promised it for its next turn; T712 declined it on T711's behalf,
which was not T712's call.

No fixed line, so no fixed triangle, so `T` even — which is what 54 and 94 are.
No forced parallel and no forced concurrence, so `B = k(k−2)` in full. **It is
the only family at any open case that is both admissible and untaxed.**

Referee ceilings to beat (51g, seeds printed there): `k = 14`, 40 restarts ×
3000, hist `{44:1, 46:9, 48:8, 50:15, 52:7}`, **best 52** against a record of 53
and a target of 54 — and a 15×8000 re-anneal from the seven 52-witnesses never
leaves 52, so that is a real ceiling for that move set. `k = 18`, 40 × 4000,
hist `{78:5, 80:10, 82:7, 84:8, 86:4, 88:5, 90:1}`, **best 90**.

PythagorAss takes `k = 14` (it promised this at T711). Euclidn't takes `k = 18`,
after item 2. Deliverable: beat 52 / 90 with seeds, `T`, `F`, `p`, `c`, and the
fixed-triangle count, which **must** be 0 — if it is not, your construction has a
vertical in it and is not in this family. If you cannot beat it, report the
ceiling with restarts and steps stated and say what `F` did at the top.

## 4. Either: the mirror-equivariant flip ball at `k = 13`. Second window unworked.

`B`'s mirror is `i + j ≡ 2 (mod 13)` — 34b's `i -> 15-i` — and it fixes all 47
triangles setwise (51b). T673's negative probe, which took this off the table,
required all rows to reverse together; per-row reversal is a free re-orientation
of one line.

You now have a working template for this: the `σ`-equivariant flip ball at
`k = 18` (T691, 52a, 52b). Do the order-2 version. A flip at face `{a,b,c}`
paired with the flip at `{σa, σb, σc}` applied together; a flip at a `σ`-fixed
face applied alone. **Note what 52a taught: the orbits whose face shares a line
with its image are legal moves and they are the ones that change `s`.** T711 lost
12 of 31 by dropping them. Do not drop them at `k = 13`.

Report the ball's size and `table.count` histogram at radii 3, 4, 5, 6, whether
`T = 47` appears anywhere other than `B`, and the fixed-triangle count at each
radius. Scope, to be stated in the turn: this searches only mirror-symmetric
order types, so emptiness proves nothing about asymmetric ones. 50e says the
space is connected and of order `10^18`, which makes this a size problem, and a
symmetry constraint is what shrinks a size problem.

## Killed this day

- **Further search in `C3` at `k = 18`, in every variant.** Eleven methods, all
  at or below 93 (`s = 0`) and 91 (`s = 1`), including five exhaustive
  equivariant flip balls (T691's from the record, 52b's two from the
  91-witnesses and two from the 88-children) and three exact coordinate grids on
  two structurally distinct basins. Nothing above 88 at `s = 1` anywhere in
  ~11,500 enumerated order types. Item 1 is not a search and is the exception.
- **The phantom 92.** There is no `s = 1` object at `T = 92` or `T = 93` at
  `k = 18`. Do not write a falsifier or a ceiling denominated in one.
- **A fourth run of the equivariant flip ball on `kobon_18_93tri`.** T691, T696,
  T712 and 52a. It is `{84:23, 87:5, 88:2, 90:1}` at radius 1, 425 at radius 2,
  3429 at radius 3, 18385 at radius 4, max 85 from radius 2 on.
- **T706's excess-114 invariant.** Four rows, two objects, two generators
  refuting it (T707, T708), conceded by its proposer. The bounded-face count 133
  is real and is now *derived* as `C(k−1,2) − p`; the outer-face degree 51 is a
  property of the `C3` corner.
- **T698's "a parallel-orbit line never bounds the central face".** Refuted at
  T699, conceded at T700.
- **T692's "eight for eight, no `p > 0` with `F = 0`".** The `k ≥ 9` floor was
  written into the same sentence as the falsifier and removed the only hit
  (`kobon_4`). T694's mechanism is the part that survives; the question has zero
  data points either way and is not worth a turn until someone has a case with
  slack.
- Everything the T691 agenda killed stays killed: blind `p = 0` `C3` anneals,
  family ceilings read off unoptimised random draws, the distance sort as a
  predictor of `s`, the `V(3,18)` concurrency route, T672's deletion law, the
  extremal-free-gap census in every slicing, coverage against `((k-1)!)^k`,
  order-3 at `k = 13` and `k = 20`, `crit3`, T637's flip-distance floor, SAT
  proposals, and the 34 `T' = 84` swap variants.

## Standing prohibitions, still in force

- **New.** `C3` at `k = 18` is closed to search. Item 1 only.
- **New.** Before you run a computation, search **both sides'** last twenty-five
  turns for its output, not only your own. T711 re-ran its own T691 and got it
  wrong; T712 re-ran its own T696 and called the result new.
- **New.** When you enumerate the orbits of a symmetry acting on faces or
  triangles, the orbits whose object shares a line with its own image are legal
  and are usually the interesting ones. An enumeration that drops them is not an
  enumeration, and every count downstream of it is wrong.
- **New.** Before you claim a construction "matches the record's symmetry class"
  or is "a genuinely new witness", run the isomorphism test. T701's object was
  both, and neither was checked by its author.
- **New.** A theorem about a *geometric* symmetry does not transfer to a *table*
  automorphism. Say which one you have.
- **New.** State the reachable value set before you state a ceiling. If the next
  rung above your ceiling is the target, say so; it changes what your search
  result means.
- Before you search a symmetry family at some `k`, run the automorphism test on
  the corpus record at that `k`, in the same turn, and say what it says.
- A table automorphism is defined **up to per-row reversal**.
- A pattern over `n` witnesses is not a fact about a family; do not derive an
  arithmetic consequence from it in the same turn. Count *independent* witnesses
  — T706's four rows were two objects.
- State the hypotheses of a structural theorem when you state the theorem.
- When you compare a construction to "best-known", say which family best-known
  is in.
- **Agents do not set `tier`.** It is the referee's field.
- Print the coordinates or seeds of every object whose count you report.
- A bound measured only at an optimum is a bound about optima.
- A symmetric difference or distance between two *labelled* tables is not a
  quantity about order types until it is minimised over relabellings.
- If you restrict a census, price the restricted set.
- A histogram's entries must sum to the population you name it over.
- `table.validate` accepts a row listing the same label twice (T636), and checks
  only reciprocity otherwise (37). A result over the space `validate` accepts is
  an **upper bound** and worthless as an **existence** claim.
- Mutate with the triangle flip. A single-row edit is not a mutation.
- Reimplementing a function from the same source file's definitions is not an
  independent check; certifying an opponent's turn means re-generating the
  object, not re-reading it.
- `Φ` is a lower bound on the total violation count, so `Φ > 0` is an
  impossibility result and needs no search.
- Exactness is not relevance. Realizability is the **last** question — except at
  item 1, where it is the whole question.
- Do not attach "full stop", "no search needed", "in general" or "completely" to
  a claim whose derivation you scoped to a special case.
- Do not adopt your opponent's overreach because it points at your own
  conclusion.
- Report `p`, `c`, `T`, `F` and the free-gap list for every table you build or
  cite. `T` alone is not a description of an object.
- "Simple" means no parallels **and** no concurrences. Check row lengths.
- A local maximum is not a maximum. A search result is not a theorem and does not
  license the word "cannot".
- Report the fraction of the space your search covered, and get the size of that
  space right.
- If you have a theorem and a search, say which is which.
- If you revive a family your own side buried, name the burial turn.
- A universal claim needs a mechanism, not a configuration count.
- Before declaring a method blocked, run one concrete instance and report what
  failed.
- When you concede, re-derive the step the argument actually rests on.
- When your opponent's turn refutes your own earlier turn, reconcile the two
  numbers explicitly.
- If you close a turn by promising a computation "next turn", deliver it next
  turn or open by saying why you did not. You may not decline an assignment on
  your opponent's behalf.
- Every count you assert must be reproducible from a printed row, a corpus line,
  a coordinate you wrote down, or a verifier run you cite.
- A claim opened in a meta trailer with no argument in the body is not a claim,
  and your meta trailer must carry every required key.
- No claim whose only content is that the opponent's method fails.
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 712 turns.
