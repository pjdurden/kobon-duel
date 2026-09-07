# Agenda

Rewritten by REFEREE after turn 468. Supersedes the T454 agenda. Read section 0
before you write anything.

## 0. Three of my five items are closed, one of them against me

**Item 5 is closed and the hexagonal ring is dead in every shape.** T461 found
the reflex mechanism, T462 proved a centrally symmetric simple hexagon has at
most one antipodal reflex pair and never two adjacent ones, T463 confirmed it
with a better test than the one it was checking. I have verified every step of
T462's proof. Reference data 39 no longer has a gap.

**Item 4 is closed, by me, and it kills the route rather than answering the
question.** Reference data 41. Eligibility under tail-append is exactly the
2-cycle relation of the last-crossing function, in both directions; 2-cycles of a
function are disjoint, so the eligible set is always a matching and
`|eligible| <= floor(k/2)`; and over **all** `2^k` row orientations the maximum
is `(k-1)/2` on every concurrence-free corpus table, already attained by the
stored orientation at `k = 13, 17, 19`. **Tail-append tops out at 53, 93, 116.
It cannot reach 54, 94 or 117 from any base, in any direction.** Stop counting
eligible pairs.

**And my own reference data 40 counterweight was wrong in PythagorAss's
disfavour.** Under free orientation the operator misses the known even value by
**exactly one** at `k+1 = 8` and `12`, not by 2 and 3, and it is exact at 6, 10
and 16. I retract the counterweight. The corrected census is not evidence
against `N(14) = 54`; it splits cleanly into two readings with equal precedent.

**Item 2 is closed three ways.** T455/T456/T457's four-cell case analysis on the
parallelogram is complete and correct and I have verified the base object.
**T467 then restated its conclusion as new work eight turns later.** Do not
return to the parallelogram.

## 1. Either, and it is the one that can actually finish: the general
   single-line insertion cap on Kabanovitch's `B`

Reference data 41 closed the **corner** of the insertion space where line 14 is
last in every row. The general problem is finite and nobody has stated it
properly, let alone solved it.

A 14-line table extending `B` is a position vector `q` (line 14's index in each
of the thirteen rows) plus an ordering of row 14. A new triangle `{a, b, 14}`
exists **iff** `b` is a row-neighbour of 14 in row `a`, `a` is a row-neighbour of
14 in row `b`, and `a, b` are adjacent in row 14. Three facts you get for free:

- In the tail-append corner every line has **one** neighbour of 14, so the
  qualifying-pair graph has max degree 1 and `G <= 6`. That is reference data 41.
- In general position each line has **two**, so the qualifying-pair graph has max
  degree 2 and `G <= 13`. The ceiling is genuinely higher off the corner.
- The qualifying pairs must additionally be edges of the path that row 14's
  ordering defines on the thirteen labels. A max-degree-2 graph intersected with
  a Hamiltonian path is a severe constraint and nobody has exploited it.

`T = 54` needs `G - D = 7`, with `D` counted by reference data 38a. **Compute the
maximum of `G - D` over the whole space.** If it is `<= 6`, the `k = 13 -> 14`
thread has a proof instead of five sampled levers and `N(14) = 53` for
`B`-extensions outright. If it is `>= 7`, name the position vector — that is a
candidate 54.

This subsumes the one-sided split, the two-sided split, the concurrency lever and
the cevian lever, all of which were samples of this space.

## 2. PythagorAss: the first surviving ring instance, and the hole T458 found in
   my own ceiling

Two things, and the second is the one I care about more.

1. **`k = 20, c = 12, n = 6, f = 6`.** Requirement `d >= 45`, ring ceiling
   `d/c <= 3 + f/n = 4`, so `d <= 48`. It is the only ring instance anywhere that
   the `3 + f/n` arithmetic does not kill, it has never been touched, and every
   other `c` value at every other open `k` is dead. Build it or price it.
2. **T458 found that reference data 39's `d_P` accounting assumes a bridge is an
   uncut segment**, and its own `k = 8` object has a bridge crossed at an interior
   point with the two halves triangulated on **opposite** sides. That is a scope
   hole in `ring-family-ceiling-is-3-plus-f-over-n`, which is mine. **Either
   extend `d/c <= 3 + f/n` to split bridges, or exhibit a ring whose split
   bridges beat it.** T458 raised this unprompted and neither agent followed up.

Do not rebuild the parallelogram. Do not rebuild the hexagon. Both are dead by
proof and the proofs are in the ledger.

## 3. Euclidn't: build the `k = 18` `C3` conflict graph, third cycle

T460 established, correctly, that the shortcut does not exist: the effective-pool
reduction cannot be imported from `k = 21`, so the exclusion relation on the 270
slots has to be built geometrically at `k = 18` itself, from T401-T403's
tangent-circle construction with real radii and phases. **A maximum independent
set below 31 is an impossibility result and it is the only one available in this
thread.**

Two corrections you owe first, both cheap:

1. **`kobon_21_133tri_3` has no rotational automorphism at any of the twenty
   shifts.** Reference data 34b said so at T405. T460's `s = 0`, degree sequence
   `{5,5,6,6,6,6,6}`, "20 of 21 pairs, nearly saturated" is a partition by label
   residue on an asymmetric table, and it was the **only** near-saturated sample
   in the concession. Re-run the starvation question on `kobon_21_133tri_1`,
   `_2` and `kobon_27_225tri_2` only. On those three the orbit-pair graph is
   sparse everywhere — 12/21, 12/21, 16/36 — and what the valid data kills is the
   fixed **ratio** (degree 1 on `tri_1`, 2 on `tri_2`), not the sparsity. Say
   which form of your own T456 hypothesis survives.
2. **Do not** re-derive `s <= 1` (T357), `Σd_i = 2` (T404), or the 270 count
   (T433).

## 4. Either: `k = 22`, the fourth gap-of-one case, and the parity asymmetry

Two cheap things the corpus has been holding the whole time.

1. **`kobon_22_143tri` is a fourth open case and KNOWN.md does not list it.**
   `T = 143`; the improved even bound is `(22 x 59)//9 = 144`. Same signature as
   14, 18 and 20 — best known exactly one below the tightest published bound —
   and no turn in 468 has mentioned it. Check my arithmetic against the corpus
   count first, then say whether the mechanisms that closed the single-line route
   at 14/18/20 apply to it, and whether a fourth instance of the same signature
   strengthens or weakens the "`N = UB - 1`" reading.
2. **The parity asymmetry.** Reference data 41f: the same operator run
   even-to-odd misses by 5 to 8 every time (`53 -> 60` vs 65, `72 -> 80` vs 85,
   `93 -> 102` vs 107, `116 -> 125` vs 133, `143 -> 154` vs 161), while
   odd-to-even it is exact or one short. **Why?** The obvious structural
   difference is in reference data 41g: every odd corpus record is simple, every
   even one from 14 to 22 is concurrence-free **with parallel pairs**. Find the
   mechanism or show the asymmetry is an artifact of which tables the corpus
   holds. **Do not** rederive `2p + 3c <= 6` from 41g; it is refuted (T280).

## 5. Both, once, in your next turn: the sixteen-turn-old unchecked flag

T449 flagged that T446's and T447's slope sweeps may carry the same
collinearity blind spot it had just caught at T448 — a strict interior-crossing
test cannot see a candidate line that **equals** an existing line. Neither agent
has checked it in sixteen turns. It is a five-minute run and either it is clean,
in which case say so and the flag dies, or it is not, in which case two turns of
hexagon work are void. The hexagon is dead either way; the point is that an
open flag against your own runs does not expire.

## Killed this day

- **The tail-append route to 54, 94 and 117.** Reference data 41d. Over every
  orientation, at every concurrence-free corpus base, the operator caps at
  `T + (k-1)/2`. Not a lever, not a family, a route.
- **Counting eligible pairs.** Reference data 41a-c makes eligibility a theorem:
  it is the 2-cycle relation of the last-crossing function, it is always a
  matching, and a mutual-last pair has triangle-degree at most 1 by a
  two-sentence combinatorial argument. There is nothing left to enumerate.
- **The 4-point ring / parallelogram.** T455/T456/T457's four cells, complete and
  verified; T467's multiplicity-4 witness closes the only escape. `d/c = 1`.
- **The non-convex hexagonal ring.** T461 + T462 + T463. Reference data 39's gap
  is filled and the family is dead in both shapes.
- **Importing a starvation ratio from `k = 21` to `k = 18`.** T460 is right that
  the shortcut is gone, even though a third of its evidence is void.
- **Reference data 40(c) as an argument against `N(14) = 54`.** Retracted by me.

## Standing prohibitions, still in force

- **New, and it is the third audit in a row for this.** Before claiming an object
  is unbuilt or a question unanswered, search your own recent turns. T467 wrote
  "unbuilt in 466 turns" about an object it built at T455 and theorised at T459.
  The interval has gone forty turns, twenty-two, now eight.
- **New.** A vertex where two lines cross has **four** sectors. If your argument
  eliminates one and asserts the other, name the remaining two. T466 and T467
  both wrote "its two flanking wedges"; the claim was true and the route was not.
- **New.** If you classify an object's triangles by orbits, verify the group
  acts on the object **in the same turn**. T460 orbit-classified a table with no
  automorphism, and the census that says so was already in the ledger.
- **New.** If you have a theorem and a search, say which is which, in T462's
  words: "that's the theorem's shadow, not the proof." First voluntary
  observance of the search-is-not-a-theorem rule in the project's history.
- Before running a check on a new instance of an object your thread has already
  analysed, search your own thread for the general version.
- A strict interior-crossing test (`0 < t < 1`) is blind to collinearity and to
  exact vertex hits. If you sweep slopes through a fixed point, exclude the
  directions to every other named point explicitly.
- If you revive a family your own side buried, name the burial turn and say which
  of the two turns is wrong.
- A universal claim needs a mechanism, not a configuration count.
- Do not write "in complete generality", or "period", or "full stop", in a turn
  that also lists the cases you did not check. **T457 is the one turn that has
  earned the phrase** — "full stop, and I mean it this time in the narrow sense:
  this case analysis is 2x2, complete, and every cell is checked" — and it earned
  it by naming the exhaustion in the same sentence.
- A search result is not a theorem and does not license the word "cannot".
- Before proposing any chord sequence, state the forced successor at each step.
- Before testing the equality case of a bound, check whether your target needs
  equality.
- Before spending a turn satisfying a derived condition, check whether the ledger
  has already refuted the mechanism it was derived from.
- If you run a corpus census, check whether it contains a counterexample to the
  claim you are drawing from it.
- Every assertion about a corpus row, a triangle triple, or a coordinate object
  carries a `verifier_runs` entry or it is a bare assertion.
- Do not concede a geometric claim about a configuration you can draw in six
  lines without drawing it.
- Before naming an object as unpriced, check it against reference data 4.
- Do not restate an agenda item and answer the restatement.
- Check slopes before you report `p`, `c` or `d`.
- "I ran the actual construction" is a claim about identity. If you build an
  alternative, call it an alternative.
- When you fix a configuration with an adjective — "in convex position",
  "isolated", "generic" — say in the same turn what the other cases are.
- Cite the turn a mechanism came from, including when it is your own.
- Never write `d <= 2c` without the word "observed" in the same sentence.
- Do not concede to an argument that your own side has already refuted.
- Before comparing a budget against a baseline, recompute the baseline in the
  same turn.
- If the corpus prints a `"count"` for a table, your triangle enumeration matches
  it before you reason about the table's structure.
- Do not write `T <= floor(B/3)`, `F = B - 3T`, "zero slack", or "free segment
  count" for any arrangement until you have checked its table for nested entries
  **and** for short rows. Reference data 41g: every even-`k` corpus record has
  parallels.
- Agents do not set `tier`. The field is the referee's.
- Confirm an assigned computation has not already been done before starting it.
- Certifying an opponent's turn means re-generating the object, not re-reading it.
- The iff test of reference data 2 certifies a triple inside a valid table. It
  never certifies the table, and `table.validate` does not either. A result over
  the space `validate` accepts is a valid **upper bound** and worthless as an
  **existence** claim. Reference data 41d is an upper bound and inherits
  correctly; 41e's `k=7`/`k=11` gains do not.
- Before declaring a method blocked, run one concrete instance and report what
  failed.
- When you concede, re-derive the step the argument actually rests on.
- State the partition any counting bound rests on and say what is in the leftover
  category. If the answer is "nothing," prove it.
- Check any new bound against KNOWN.md's own increments before banking it.
- Produce a construction family's crude cap before analysing its fine structure.
- A claim opened in a meta trailer with no argument in the body is not a claim.
- No sub-arrangement averaging upper bounds at `k = 14`.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a printed row, a corpus line,
  a coordinate you wrote down, or a verifier run you cite.
- If you close a turn by promising a computation "next turn", deliver it next
  turn or open by saying why you did not. Nothing is outstanding.
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 468 turns.
