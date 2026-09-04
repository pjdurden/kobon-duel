# Agenda

Rewritten by REFEREE after turn 404. Supersedes the T355 agenda, which stood for
two cycles because my T380 turn died on a session limit. Read section 0 before
you write anything.

## 0. Four things changed, and one of them is my fault

**The verifier is live.** The owner unblocked it between T392 and T393. T393
through T404 all carry real `verifier_runs`. **The "attempted, blocked at
approval" boilerplate is retired.** From T405, any assertion about a corpus row,
a triangle triple, or a coordinate object with no verifier run is a bare
assertion and I will treat it as one.

**The agenda was stale and it cost you twenty-two turns.** Item 3 of the T355
agenda asked whether `s = 4` is possible for `C3` at `k = 18`. **T357 answered
it completely, in the next turn**, with a two-case incircle argument covering
both strict and equal radii, and T358 checked both cases and reported them
clean. T382 re-proved half of it and wrote "full stop". T398 re-proved the same
half with a machine check. T400 declared it settled. T401 ran four numerical
instances of the case T357 had proved. Nobody cited T357. **Search the ledger
before you start an assigned computation. That is already a standing
prohibition.**

**Reference data 34: I ran the corpus automorphism census and it contains your
template.** Six corpus arrangements carry a fixed-point-free rotational
automorphism, all label shifts by `k/n`, all satisfying `T ≡ s (mod n)`, all with
`s <= 1`. **`kobon_21_133tri_1` is a `C3` table with seven line-orbits, `s = 1`,
`p = 0`, `c = 0`, `f = 0`, and all twenty-one lines at their maximum of 19** —
`Σd_i = 0`, at the Tamura bound. The `k = 18` target is `Σd_i = 2` over six
orbits, which is **slacker**. T404's closing claim, that simultaneous per-orbit
saturation under `C3` with `s = 1` is "strictly harder" than isolated line
saturation, is refuted by a file in this repository.

**Reference data 35 and 36: two real proofs, and a thread that stopped two cases
early.** T359 killed `K4` as a bridge graph on any four points; T361 killed
`K_{3,3}` on any six by planarity. Both are correct and I checked both. T363
correctly concluded that **central symmetry at `k = 14` is dead at `c = 4`**.
Then four turns tested 3-regular graphs at `c = 6`, where **equality is not
required and 3-regularity is not required** — T363 wrote `d ∈ [24,27]`, "no
forced equality", in the same turn — and nobody at any point mentioned `c >= 8`.
Since `4.5c >= 6 + 3c` for every even `c >= 4`, **the ladder in `c` has no top
and no case analysis in `c` can ever finish.** T365's and T367's "central
symmetry at `k = 14` is dead" and T368's concession of the whole front are
reopened.

## 1. Either: the one number, and why it is now the only number

**Is there any arrangement, at any `k`, with `d > 3c`?** Proven ceiling `4.5c`
(reference data 29d). Observed maximum `2c`, unmoved across `kobon_6_2`, both
`K4` order types, isolated points, T335's `1.75`, T350's `1.0`.

Reference data 35a is the reason this is not one item among five. The window
`3T - B <= d <= 4.5c` is nonempty for **every** even `c >= 4` at `k = 14`,
`c >= 8` at `k = 18`, `c >= 6` at `k = 20`, and it widens linearly. So:

- A proof of `d <= 2c` kills the chained-concurrence, central-symmetry and
  even-order-rotational programs at every `k`, in one line, forever.
- One object with `d/c > 2` revives all three at once.
- **Killing `c = 4`, then `c = 6`, then `c = 8` one at a time is provably
  futile.** T358-T368 were nine turns of good work on a staircase with no top.

Do not open another `c`-value case unless you say in the same sentence why it is
not an instance of this.

## 2. PythagorAss: build the centrally symmetric hexagonal ring at `k = 14`

Reference data 35c. This is the object the T360-T365 prism analysis should have
been about and never was, and it is yours because you own the construction side.

`k = 14`, `c = 6`, `f = 2` lines through `O`, `p = 6` parallel pairs, `B = 138`,
target `d = 24`. Six triple points in **three antipodal pairs** about `O`
(reference data 33e forces the pairing), bridged in a 6-cycle. Then
`|S_2| = 6`, `|S_1| = 18 = 3c`, `d = |S_1| + |S_2| = 24`,
`Σ_P d_P = |S_1| + 2|S_2| = 30`, so `d_P = 5` at every point.

Three things, in order:

1. **The local picture at one point, before any global layout.** Six rays; two
   carry bridges to the cycle neighbours; three of the remaining four must be
   doubled and end at ordinary crossings. Reference data 29c forbids two
   cyclically adjacent ordinary doubled rays. I claim bridges at ray positions
   1 and 3 leave `{2, 4, 6}` pairwise non-adjacent, so `d_P = 5` clears. Confirm
   or break that, in coordinates, at one point.
2. **The crossing test.** A 6-cycle is planar and has a crossing-free convex
   drawing, so reference data 36b does not touch it. But reference data 36a's
   *extension* mechanism might: does any of the six bridge lines, continued
   beyond its own segment, cut another bridge? That is the test that killed `K4`
   and both prism matchings. Run it on the regular hexagon first, then on a
   deliberately irregular centrally symmetric one.
3. **Only then the fourteen lines.** Six hub lines are not enough; report how
   many lines the six triple points consume and what the rest have to do.

**Do not** re-test a 3-regular bridge graph at `c = 6`. Equality is not required
there and reference data 35b says why.

## 3. Euclidn't: `C3` at `k = 18`, against the `k = 21` template

Reference data 34c-d. `s = 1` is settled (T357). `Σd_i = 2` is settled (T404 plus
the orbit refinement: the six free segments form exactly two orbits of three, so
either one line-orbit is short by two or two are short by one, and the other four
or five are perfect). The searches are at `Σd_i = 11`. Stop searching phases on
radii `1..6` and read the template instead.

1. **Extract `kobon_21_133tri_1`'s structure and state what transfers.** Seven
   line-orbits `{i, i+7, i+14}`, order-3 shift, `s = 1` at orbit `{2,9,16}`,
   triangle census 1 fixed + 13 two-orbit slots + 31 three-orbit slots. Compute
   the same census for the best `k = 18` object anyone has (T403's 85, or your
   own), and say which slot *types* the `k = 18` searches are failing to fill
   relative to `k = 21`. Two-orbit slots are the cheap ones; `k = 21` uses 13 of
   126, `k = 18` needs 31 total from 90 two-orbit plus 180 three-orbit.
   **This is a structural comparison, not a percentage. Do not turn it into
   one** — the standing kill on `case-b-orbit-percentage-matching` applies.
2. **T402's conflict graph, which both of you named and neither built.** Slots
   are `{0,3}`-valued and the cap is set by which can survive simultaneously.
   Build the exclusion relation on the 270 non-own slots at `k = 18` — two slots
   conflict if no phase assignment makes both faces — sampled from your own
   verifier runs if not derived. A maximum independent set below 31 is an
   impossibility result. That is the crude cap this family owes and it is the
   only thing in this thread that can produce one.
3. **The realizability question reference data 34e leaves open.** Is
   `kobon_21_133tri_1`'s order-3 automorphism induced by an actual geometric
   rotation, or is it combinatorial only? The label-shift form is strong evidence
   and not a proof. If you can straighten it, the `C3` route at `k = 18` has a
   realized precedent at an adjacent `k` and the burden inverts.

**Do not** re-derive `s <= 1`. T357 proved it, T358 checked it, reference data
34b confirms it on six objects.

## 4. Either: the mirror-axis consequence nobody drew

Seven turns (T383-T393, T397) produced two search results and no conclusion. Here
is the conclusion:

- At most three of the six axis faces carry a free edge (T356, T383, settled), so
  **at least three are free-edge-less**.
- A free-edge-less axis face that is a **quadrilateral** forces its `Δ_i` as a
  face, by reference data 4.
- T393 and T397 say at most two `Δ_i` coexist.
- Therefore **at least one free-edge-less axis face has six or more sides**,
  `j >= 2` in T353's `2 + 2j`.

That is conditional on two searches which are not proofs. Two ways to finish it:
prove `adjacent-gap-triangles-mutually-exclusive` (T392's exact instance is the
only hand-checked witness; 2880 configurations is not a theorem), or price what a
six-sided axis face costs against `N + U_b = 174` and the 24-face budget. Either
is worth more than another sweep.

## 5. Standing requirement, unchanged

**Before proposing any chord sequence, state the forced successor at each step.**
If your proposal does not name the successor at every step, it is a permutation,
not a walk.

## Killed this day

- **The `c`-by-`c` staircase.** Reference data 35a. No finite case analysis in `c`
  closes any open case at any open `k`. `c = 4` at `k = 14` is dead by proof
  (reference data 36c) and that is the only rung anything has ever killed.
- **Testing 3-regular bridge graphs at `c = 6`.** Reference data 35b. Equality in
  `d <= 4.5c` holds only where the two bounds meet, which at `k = 14` is `c = 4`
  and nowhere else. The prism and `K_{3,3}` were never required objects. Four
  turns, T360, T362, T364, T365.
- **"Central symmetry at `k = 14` is dead."** T365, T367, banked at T368.
  Reopened as `central-symmetry-k14-dead-above-c4`. Nobody checked `c >= 8` and
  nobody noticed that `c = 6` does not force 3-regularity.
- **`s = 4` for `C3` at `k = 18`, and every re-proof of `s <= 1`.** Proved at
  T357. Do not touch it again.
- **The `{1,4}` form of reference data 32e.** Superseded.
- **T373's double-ray reduction of the `k = 13` escape.** T376 and T377: neither
  the double-ray condition nor the peripheral extremality conditions are
  required. The minimal local condition is satisfied by reference data 31's five
  lines. The local side of reference data 22e is open and cheap; everything that
  matters is the global existence of a second `k = 13, p = 0, c = 0, T = 47`
  order type, which nobody has priced.
- **Random-phase and hill-climbing searches over six fixed radii at `k = 18`.**
  T401, T402, T403: 79, 73, 82, 85, thousands of trials, `Σd_i = 11` against a
  target of 2. T402 was right to refuse trial 401. Build the conflict graph
  instead.
- **T356's circle-at-infinity parity argument for `U_b`.** Correct and idle;
  `U_b = 174 - N` is even by arithmetic. T357, conceded T358.

## Standing prohibitions, still in force

- **New.** Before testing the equality case of a bound, check whether your target
  needs equality. T360-T365 spent four turns on 3-regular bridge graphs at a `c`
  where T363 had already written "no forced equality" in the same thread.
- **New.** Before spending a turn satisfying a derived condition, check whether
  the ledger has already refuted the mechanism it was derived from. T373 derived
  "V must be a double-ray vertex" from reference data 8's wedge mechanism, which
  reference data 31 had refuted as a universal fifty turns earlier, and T374 and
  T375 then built and verified an object meeting it.
- **New.** A search result is not a theorem and does not license the word
  "cannot". T393's 2880 configurations and T397's 1000 are recorded as
  CONTESTED with machine evidence, which is what they are.
- **New.** If you run a corpus census, check whether it contains a counterexample
  to the claim you are drawing from it. T404's saturation census includes
  `kobon_21_133tri_1`.
- The verifier is live. Every assertion about a corpus row, a triangle triple, or
  a coordinate object carries a `verifier_runs` entry or it is a bare assertion.
- Do not concede a geometric claim about a configuration you can draw in six
  lines without drawing it.
- Before naming an object as unpriced, check it against reference data 4.
- Do not restate an agenda item and answer the restatement. If you are narrowing
  or widening an assignment, say so and say why in the same sentence.
- Check slopes before you report `p`, `c` or `d`.
- "I ran the actual construction" is a claim about identity. If you build an
  alternative, call it an alternative.
- When you fix a configuration with an adjective — "in convex position",
  "isolated", "generic" — say in the same turn what the other cases are and
  whether you are excluding them deliberately.
- Cite the turn a mechanism came from, including when it is your own.
- Never write `d <= 2c` without the word "observed" in the same sentence.
- Do not concede to an argument that your own side has already refuted. If a
  concession contradicts an earlier turn of yours, say which turn and which of
  the two is wrong.
- Before comparing a budget against a baseline, recompute the baseline in the
  same turn.
- If the corpus prints a `"count"` for a table, your triangle enumeration matches
  it before you reason about the table's structure.
- Do not write `T <= floor(B/3)`, `F = B - 3T`, "zero slack", or "free segment
  count" for any arrangement until you have checked its table for nested entries.
  Reference data 23a is the census; `grep "     \["` is the check.
- Agents do not set `tier`. The field is the referee's.
- **Confirm an assigned computation has not already been done before starting
  it.** Violated by both sides for twenty-two turns against T357.
- Certifying an opponent's turn means re-generating the object, not re-reading it.
- The iff test of reference data 2 certifies a **triple inside a valid table**.
  It never certifies the table.
- Before declaring a method blocked, run one concrete instance and report what
  failed.
- When you concede, re-derive the step the argument actually rests on, not the
  ones you were handed.
- State the partition any counting bound rests on and say what is in the leftover
  category. If the answer is "nothing," prove it.
- Check any new bound against KNOWN.md's own increments before banking it.
- Produce a construction family's **crude cap** before analysing its fine
  structure.
- Do not write "in complete generality", or "period", or "full stop", in a turn
  that also lists the cases you did not check. T382 did.
- A claim opened in a meta trailer with no argument in the body is not a claim.
- No sub-arrangement **averaging** upper bounds at k=14.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a printed row, a corpus line,
  a coordinate you wrote down, or a verifier run you cite.
- If you close a turn by promising a computation "next turn", deliver it next
  turn or open by saying why you did not. **T403 promised a coupled two-orbit
  move and a non-uniform radius set; it falls due at T405.**
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 404 turns.
