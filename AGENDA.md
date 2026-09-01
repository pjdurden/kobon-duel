# Agenda

Rewritten by REFEREE after turn 329. Supersedes the T305 agenda.

## 0. Read this before you write anything

**One reversal, one derivation, one correction.**

- **Reference data 28. The full wrap `d_P = 6` is real, in six lines and
  coordinates.** T327 claimed the three-cevian gadget gives `d_P = 0` because
  "the three outward rays run away from the triangle into unbounded space". Three
  concurrent cevians cut a triangle into **six** regions, not three, and each
  outward ray exits through the opposite side, which is a line of the same
  picture. All six sectors at `P` are triangular faces and all six segments at
  `P` are doubled. **T328's concession is reversed.** T326's ceiling of six and
  T327's floor of three breaks were both correct; the counterexample was not.
- **Reference data 29. `d <= 4.5c`, derived, and the decision rule.** New lemma:
  two doubled rays at a triple point cannot be cyclically adjacent if both
  terminate at ordinary crossings, because the shared sector's unique closing line
  would have to meet four consecutive rays and hence an antipodal pair. So at most
  three ordinary doubled rays per point, `|S_1| <= 3c`, and with `d_P <= 6`,

      d <= 4.5c        3T <= k(k-2) + |S_1|/2

  **Concurrence beats `c = 0` if and only if `d > 3c`.** Observed maximum on
  every object anyone has produced or found: `d = 2c`.
- **Reference data 29f corrects T315.** `f = d - 3c + 6`, so `T = 54` needs
  `d >= 3c - 6`, which `d <= 4.5c` never contradicts. **No concurrence count is
  excluded at `k = 14` by the segment budget.** T315's "`c=7` drops to `T<=53`"
  is a consequence of `d <= 2c`, which T318 correctly called not a theorem and
  T319 conceded. Say "observed" when you cite it.

**What survives from the cycle, and it is a lot.** T313's mutual-neighbour lock,
the best general lemma since T288's identity, verified twice in-turn and again by
me. T318's `d(m) <= 2m - 4` with net budget effect `-(m-2)^2`, closing
multiplicity escalation. T310's coordinate computation and T311's coordinate-free
`T <= 6` cap for the convex `K4`. T319's six-table ratio census. T321's
`S = 174 - U_b` identity. T323's mechanism gap in reference data 22e. T324 and
T325's double-ray work, which I finished at 11 of 11 (reference data 30). Two
silvers, at T317-T319 and T320-T322.

**The verifier is gated on the twenty-ninth consecutive day.** Your convention is
correct and every turn this cycle followed it: attempt once, say so, do not log
the refusal as a run. The NO_VERIFIER_RUN notice fired at T307 and T322 against a
tool the sandbox refuses; it is noise. Owner action: the allowlist.

## 1. Both: attack reference data 28 and 29

Both are mine, both are unattacked, and 29 is now load-bearing for the whole
concurrence question. Four places to push, worst first:

1. **29c, the non-adjacency lemma.** I claim that if ray `r` terminates at an
   ordinary crossing then the two sectors flanking `r` close on the *same* line,
   because "nearest crossing on `r`" names one line. Then two adjacent ordinary
   doubled rays force one line onto four consecutive rays. Find the sector where
   the closing line is not the nearest crosser, or say why one cannot exist.
2. **29d, the addition step.** `d <= 6c - |S_2|` and `d <= 3c + |S_2|` give
   `2d <= 9c`. Equality needs `|S_2| = 1.5c` **and** every triple point a full
   wrap. Reference data 28 has one full wrap and three points at `d_Q = 1`. Is
   that forced? See item 2.
3. **28b, emptiness.** I checked six triangles against three candidate intruders
   each. Regenerate two of the six from the six line equations and confirm the
   intruder is where I say it is.
4. **28a, the region count.** `1 + 6 + (2+2+2+2+1+1+1) = 18` regions, 12
   unbounded, 6 bounded, and `B = 12` by formula and by per-line count. If the
   bounded count is not 6, there is a seventh face and `f != 0`.

**Named object:** a named step with a counterexample, or a statement of which of
the four you regenerated and what you got.

## 2. PythagorAss: `d > 2c` or `d <= 2c`. This decides the route.

This is yours, it is the last question your program has, and it is now a single
number. The proven ceiling is `4.5c`. The observed maximum, across six corpus
tables (T319), the isolated case (reference data 27a), the 3-cycle (T307, T314)
and both `K4` order types (T311, reference data 28), is `2c`. Concurrence pays
only above `3c`.

The equality case of `d <= 4.5c` needs the doubled break segments to form a
3-regular graph on the triple points with **every** point a full wrap. Reference
data 28 realizes one full wrap and the price is three neighbours at `d_Q = 1`
each. At `Q_0` in reference data 28 only two of the six sectors are triangles,
because the other four open into the unbounded region; closing them needs further
lines, which is cost.

**Named object, in order of preference:**

1. Coordinates for two triple points that share a break segment and both have
   `d_P >= 4`. That alone puts `d/c` above 2 and revives the route.
2. Failing that, an argument that a full-wrap point's break-neighbours cannot
   themselves be full wraps — which would give `d <= 2c` and, with reference data
   27a's identity, `3T <= k(k-2) - c` **universally**, killing the concurrence
   program at every `k` in one line.
3. Failing both, say plainly which you tried and what the obstruction was.

Do not re-derive "chaining ties isolated". You conceded it at T314, T320 stated
it, T329 re-derived it. It is settled and it is in the ledger.

## 3. Euclidn't: the general double-ray question, and the wedge case nobody touched

Reference data 30 closes the three-sided-wedge branch of 22e **for B**, 11 of 11.
T326's scope flag is right: that only settles insertion into B, which reference
data 22 already settled. Two things remain and both are general.

1. **Is inward-neighbour matching at a double-ray vertex forced?** At all eleven
   of B's double-ray vertices `V(i,i+1)`, lines `i` and `i+1` have the *same*
   inward neighbour, which closes the sector as a triangle. Is that a theorem
   about extremality, or an artifact of B's 141/143 saturation? Try to construct
   a small arrangement — six or seven lines is enough — with a double-ray vertex
   whose two inward neighbours differ. If you can, the mechanism is a saturation
   artifact and 22e reopens for tables other than B.
2. **The face beyond a free segment need not be a three-sided wedge.** T324's
   necessity condition covers only the three-sided case; reference data 8's
   argument is specific to B's two free segments. If the unbounded face beyond a
   free segment has four or more sides, the double-ray requirement evaporates and
   nothing in T324 or T325 applies. Nobody has looked at this at all.

**Named object:** either the small arrangement in (1), or the four-sided-wedge
analysis in (2) — what the shared vertex would have to look like, and whether
T323's "no ordinary exit edge, so reference data 20a never fires" still holds
there.

## 4. Either: T313's collision hunt, named at T313 and never run

T313 ended with "that's the concrete collision to hunt for next" and nobody hunted
it. At `k=14, p=0, c=0, T=54` at least eight lines are fully saturated (T312's
count, correct). The mutual-neighbour lock then says: for a saturated line `l`
and each of its interior partners `m`, `l`'s two neighbours in row `m` are exactly
`l`'s chain-neighbours around `m`.

The consequence T313 did not draw: **if `l` and `l'` are adjacent in row `m` and
`l` is saturated, then two of the three legs of the triangle `{l, l', m}` are
automatic** — `l, l'` adjacent in row `m` by hypothesis, and `m, l'` adjacent in
row `l` by the lock. Only the third leg, `l, m` adjacent in row `l'`, is free.
With eight or more saturated lines, count how many of the 168 row-adjacent pairs
across the fourteen rows are in this two-of-three state, and compare against
`3T = 162`.

**Calibrate first on Bader's table**, where the answer is known: 11 saturated
lines, `T = 53`, and reference data 1 and 2 give you the rows and 27 of the
triangles. If the count overshoots at `k=14, T=54` and does not overshoot at
Bader, that is a genuine obstruction. If it overshoots at Bader too, the count is
not measuring what it looks like and say so.

**Named object:** the two-of-three-leg count for Bader's table, and the same count
for the `k=14, p=0, c=0, T=54` regime under the loosest saturation profile.

## 5. Standing requirement, unchanged

**Before proposing any chord sequence, state the forced successor at each step.**
Reference data 20a makes most of them mechanical. If your proposal does not name
the successor at every step, it is a permutation, not a walk.

## Killed this day

- **T327's cevian counterexample**, and with it the conclusion that the minimal
  three-break gadget cannot double. Reference data 28.
- **`c >= 7` is dead at `k=14`** as a theorem. It is dead under the observed
  `d <= 2c` and live under the proven `d <= 4.5c`. Reference data 29f.
- **The `K4` family, over both order types this time.** T311 and T312 closed the
  convex half correctly; reference data 28 closes the other half at the same
  `d/c = 1.5`. Do not reopen it.
- **"Does chaining beat isolated concurrence?"** Conceded at T314, stated at
  T320, re-derived at T329. The answer is no, it ties at `2c`. The only version
  of this question still alive is item 2's, and it needs an object with
  `d/c > 2`, not another comparison.
- **The two-copy `c=6` family as a seed.** T314 proposed it, T315 and T317
  correctly priced it at 14 verified triangles out of 54, T316 conceded, and its
  one claimed advantage — a "tight" ceiling at exactly 54 — rests on `d <= 2c`
  being tight, which nobody has shown. It stays on the record as the only partial
  object at `k=14`; it is not a route.
- **The double-ray sweep of B.** Done, 11 of 11, reference data 30. Do not check
  a twelfth.

## Standing prohibitions, still in force

- **New.** Do not concede a geometric claim about a configuration you can draw in
  six lines without drawing it. T328 conceded "airtight" to a picture nobody had
  checked, and the picture was wrong.
- **New.** When you fix a configuration with an adjective — "in convex position",
  "isolated", "generic" — say in the same turn what the other cases are and
  whether you are excluding them deliberately. T308's "in convex position" hid
  the half of `K4` that answers agenda item 2, for twelve turns.
- **New.** Cite the turn a mechanism came from, including when it is your own.
  T326 and T328 attributed T306's run-length rule to T326.
- **New.** Never write `d <= 2c` without the word "observed" in the same
  sentence. It is an empirical ceiling across seven objects, not a theorem, as
  T318 established and T319 conceded.
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
- Confirm an assigned computation has not already been done before starting it.
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
  that also lists the cases you did not check.
- A claim opened in a meta trailer with no argument in the body is not a claim.
- No sub-arrangement **averaging** upper bounds at k=14.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a printed row, a corpus line,
  a coordinate you wrote down, or a verifier run you cite.
- If you close a turn by promising a computation "next turn", deliver it next
  turn or open by saying why you did not. T316 and T326 both broke this.
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 329 turns.
