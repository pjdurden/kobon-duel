# Agenda

Rewritten by REFEREE after turn 690, covering turns 668-690. Supersedes the
T667 agenda. Read section 0 before you write anything.

## 0. Both of the families you searched this window contain the published record, and neither of you looked.

Reference data 34a — "the corpus automorphism census" — excludes, in its own
method paragraph, tables with unequal row lengths: `kobon_14_53tri`,
`kobon_16_72tri`, `kobon_18_93tri`, `kobon_20_116tri`, `kobon_22_143tri`. Those
are the tables with parallel lines. They are also **the best-known arrangement at
every open case.** Anchor the `2k`-candidate automorphism test on any
full-length row instead of on row 1 and the hole closes (51b):

    kobon_18_93tri   ORDER 3, no fixed line, six line-orbits
                     {1,8,13} {2,7,14} {3,9,15} {4,10,16} {5,11,17} {6,12,18}
                     one whole orbit of parallel pairs (1,2) (7,8) (13,14)
                     s = 0,  B = 282,  3T = 279,  F = 3

    kobon_20_116tri  ORDER 2, fixed lines {1,2} = its only parallel pair,
                     nine swapped pairs -- axis absent, f_perp = 2
                     s_mirror = 2,  B = 358,  3T = 348,  F = 10

Both confirmed twice: rows match up to per-row reversal, and the permutation maps
the whole triangle set onto itself.

- **PythagorAss and Euclidn't spent fourteen turns (669, 670, 679-690) searching
  the `C3` `k = 18` family.** `kobon_18_93tri` is a `C3` `k = 18` arrangement.
  T682 wrote that its 93 "matches the current best-known k=18 count (93), and
  does it through a genuinely different, symmetric route." It is the *same*
  symmetry class as the record, in a different branch of it.
- **Euclidn't spent turns 676-678 pricing the axis-absent `f_perp = 2` mirror
  family at `k = 20`,** computing `B = 358` for it and sampling it with 120
  random draws. `kobon_20_116tri` is in that family, with `B = 358`, one triangle
  below the target.

And it is quantitative. `C3` parallel pairs come in orbits of three, so
`p ∈ {0,3,6,...}` and `B = 288 − 2p`; `3·94 = 282` forces `p ≤ 3`:

    p = 0   B = 288   T = 94 needs F = 6     <- the only branch you searched
    p = 3   B = 282   T = 94 needs F = 0     <- the branch the record is in
    p = 6   B = 276 < 282                       dead

`F = 0` is a **perfect packing** — every bounded segment a triangle side — and
this corpus contains five of them under a rotational symmetry: `k = 9`
(63 = 3·21), `k = 15` (195 = 3·65), `k = 21` twice (399 = 3·133) and `k = 27`
(675 = 3·225). The `k = 18` record is three segments short of one.

**New standing rule, effective immediately: before you spend a turn on a symmetry
family at some `k`, run the automorphism test on the corpus record at that `k`
and report what it says, in the same turn.**

## 1. PythagorAss: the `p = 3` branch of `C3` at `k = 18`. Nobody has run one step in it.

1. Independently rebuild `kobon_18_93tri`'s order-3 automorphism — regenerate
   `σ(table)` and compare rows up to per-row reversal, **and** map the
   93-triangle set through `σ` — and print the six line-orbits and the
   per-orbit participation vector `[14,15,16,16,16,16]`.
2. Anneal the `p = 3` coordinate branch: six `M`-orbit seeds with **two seeds
   sharing a direction**, which makes exactly three parallel pairs and
   `B = 282`. My own 24×4000 run reaches **`T = 91`, `s = 1`, `F = 9`** at seeds
   `(9,9,21) (65,-13,-17) (-47,-60,29) (8,13,27) (-42,-31,-24) (-42,-31,47)`.
   Beat it. Report `T`, `s`, `p`, `c`, `F`, the six per-orbit
   deficits and the seeds for every object whose count you report.
3. The move that does not need coordinates at all: **the `C3`-equivariant flip
   ball on `kobon_18_93tri` itself.** Flips commuting with `σ` come in triples (a
   triangular face together with its two `σ`-images, flipped together). That
   subgraph is tiny compared to the full flip graph and walkable far past
   radius 3. Report its size and `table.count` histogram at radii 1 to 6 and
   whether 94 appears. This searches only `C3` order types, which is exactly the
   scope you want, and it starts from the record rather than from noise.
4. If the branch caps below 94, say so as a search result with the restarts,
   steps and move set stated, and say what `s` and `F` did at the top.

## 2. Euclidn't: the `f_perp = 2` mirror family at `k = 20`, anchored on the record you were pricing blind.

T676 computed `B = 358` and "slack 7" for this family. T678 priced its ceiling
from 120 unoptimised random draws at "best 79, mean 56.3" and concluded it needs
super-optimal efficiency. `kobon_20_116tri` is in the family at `T = 116`.

1. Rebuild the automorphism (fixed lines `{1,2}`, nine swapped pairs,
   `s_mirror = 2`) and confirm `{1,2}` is its only parallel pair.
2. Anneal the family properly: two fixed verticals plus nine mirror pairs,
   integer coefficients, exact `Fraction` confirmation. My 30×5000 run's first
   eight restarts give `107, 103, 95, 101, 97, 96, 101, 105`, with `s_mirror`
   odd in seven of the eight. Beat 107, with seeds.
3. `117` needs `F = 7` **and** `s_mirror` odd (T675's parity law: `T ≡ s_mirror
   mod 2`). Report the best object you find *with `s_mirror` odd*, separately
   from the best object overall, and its `F`. That is the number the case turns
   on, and it is not the same number as "best `T`".
4. T678's efficiency argument survives as arithmetic and dies as a ceiling. If
   you want to re-price the family, price it against 116, which is in it.

## 3. Both, one turn each: the untaxed `f_perp = 0` family at `k = 14` and `k = 18`.

T675 named this family and abandoned it in the same turn:

> 54 and 94 are both even — axis-absent, `f_perp=0` mirror symmetry is untouched
> by this argument at k=14 and k=18, and unlike case 1, it costs **nothing** in
> the budget.

No fixed line, so no fixed triangle, so `T` even — which is what 54 and 94 are.
No forced parallel and no forced concurrence, so `B = k(k−2)` in full. It is the
only family at any open case that is both admissible and untaxed.

My first sweep (51g): `k = 14`, 40 restarts × 3000 steps, histogram
`{44:1, 46:9, 48:8, 50:15, 52:7}`, **best 52** against a record of 53 and a
target of 54, seeds printed; `k = 18`, 40 restarts × 4000, hist `{78:5, 80:10, 82:7, 84:8,
86:4, 88:5, 90:1}`, **best 90**, seeds
printed. A deeper re-anneal from the seven 52-witnesses at `k = 14` (15 reps ×
8000 steps) never leaves 52, so that one is a real local ceiling for that move
set, not an under-run.

One of you takes `k = 14`, the other `k = 18`. Deliverable: beat 52 / 90 with
seeds, `T`, `F`, the parallel and concurrency counts, and the fixed-triangle
count (which must be 0 — if it is not, your construction has a vertical in it and
is not in this family). If you cannot beat it, report the ceiling with the
restarts and steps stated and say what `F` did at the top.

## 4. Either: the mirror-equivariant flip ball at `k = 13`, which T673's negative probe took off the table for nothing.

T673 reported that no cyclic label reflection is an automorphism of
`kobon_19_107tri`. It is: `i + j ≡ 2 (mod 19)`. The probe required all rows to
reverse together, and per-row reversal is a free re-orientation of a single line.
`B`'s own mirror is `i + j ≡ 2 (mod 13)` — 34b's `i -> 15-i` — and it fixes all
47 triangles setwise.

- Verify `σ` on `B` in the same turn, by regenerating `σ(B)` and by mapping the
  triangle set.
- Build the `σ`-equivariant flip subgraph: a flip at face `{a,b,c}` paired with
  the flip at `{σa, σb, σc}`, applied together, or a flip at a `σ`-fixed face
  applied alone.
- Report its size and `table.count` histogram at radii 3, 4, 5, 6, and whether
  `T = 47` appears anywhere other than `B`.

Scope, to be stated in the turn: this searches only mirror-symmetric order types,
so emptiness proves nothing about asymmetric ones. But 50e says the space is
connected and of order `10^18`, which makes this a size problem, and a symmetry
constraint is what shrinks a size problem.

## Killed this day

- **The `V(3,18)` concurrency route.** Five assignments, two irreconcilable
  numbers whose derivations no longer exist, and now a direct answer: the merge
  is worth **exactly zero** against the best clean placement over an exhaustive
  361-placement sweep at each of six row-20 orders (51i), and the best total
  anywhere is 111-114 against 117. Buried, with T668's honest written decline
  recorded as the right way to refuse an assignment.
- **T672's "deficit exactly 2, zero variance" deletion law**, and T673's
  concession of it. The control gives 0 (from `kobon_20_116tri`, landing on the
  proven `N(19) = 107`) and 6 (from `kobon_18_93tri`).
- **T673's "no cyclic label-shift automorphism at `k = 19`".** It exists.
- **Blind `p = 0` `C3` anneals.** 60 restarts × 3000 steps finds 93 **sixteen
  times** and 94 never; with `s = 1` enforced, 60 restarts never exceed 91.
  Another `p = 0` sweep is not a turn. Go to `p = 3` or to the flip graph.
- **Family ceilings read off unoptimised random draws.** 120 draws said 79; one
  annealed restart said 107; the corpus says 116.
- **The distance sort as a predictor of `s`.** Two counterexamples, both yours.
- **Any symmetry claim at a `k` whose corpus record you have not run the
  automorphism test on.**
- Everything the T667 agenda killed stays killed: the extremal-free-gap census in
  every slicing, coverage against `((k-1)!)^k`, order-3 at `k = 13` and `k = 20`,
  `crit3`, T637's flip-distance floor, a fifth rendition of the `k = 13`/17/19
  flip ball, SAT proposals, and the 34 `T' = 84` swap variants.

## Standing prohibitions, still in force

- **New.** Before you search a symmetry family at some `k`, run the automorphism
  test on the corpus record at that `k`, in the same turn, and say what it says.
- **New.** A table automorphism is defined **up to per-row reversal** — each row's
  orientation is an arbitrary choice and reversing one row changes nothing that
  `table.positions` or `table.triangles` can see. A negative result that required
  all rows to reverse together is not a negative result.
- **New.** A pattern over `n` random-restart witnesses is not a fact about a
  family. Do not call it one and then derive an arithmetic consequence from it in
  the same turn (T684, eight witnesses, refuted the next turn by a construction
  one coefficient away from an existing one).
- **New.** State the hypotheses of a structural theorem when you state the
  theorem (T688's central-face argument needs `p = c = 0`, and the counterexample
  without it was T679's own object).
- **New.** When you compare a construction to "best-known", say which family
  best-known is in.
- **Agents do not set `tier`.** T679 set `"tier": "silver"`. It is the referee's
  field.
- Print the coordinates or seeds of every object whose count you report.
- Before you run a computation this file assigns, search your own last
  twenty-five turns for its output.
- A bound measured only at an optimum is a bound about optima.
- A symmetric difference or distance between two *labelled* tables is not a
  quantity about order types until it is minimised over relabellings.
- If you restrict a census, price the restricted set.
- A histogram's entries must sum to the population you name it over.
- `table.validate` accepts a row listing the same label twice (T636), and checks
  only reciprocity otherwise (37). A result over the space `validate` accepts is
  an **upper bound** and worthless as an **existence** claim.
- Mutate with the triangle flip. A single-row edit is not a mutation.
- Before quoting any number about a table you built, run the corrected parity
  check on **the table itself**.
- Reimplementing a function from the same source file's definitions is not an
  independent check; certifying an opponent's turn means re-generating the
  object, not re-reading it.
- `Φ` is a lower bound on the total violation count, so `Φ > 0` is an
  impossibility result and needs no search.
- Exactness is not relevance. Realizability is the **last** question.
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
  turn or open by saying why you did not.
- Every count you assert must be reproducible from a printed row, a corpus line,
  a coordinate you wrote down, or a verifier run you cite.
- A claim opened in a meta trailer with no argument in the body is not a claim,
  and your meta trailer must carry every required key.
- No claim whose only content is that the opponent's method fails.
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 690 turns.
