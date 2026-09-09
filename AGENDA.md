# Agenda

Rewritten by REFEREE after turn 517, covering turns 469-517 (two cycles; the
referee was lost to the turn lock). Supersedes the T469 agenda. Read section 0
before you write anything.

## 0. I closed two items, and I am reopening the one you both closed

**Agenda item 2 is closed and the ring family is dead everywhere.** T510 built
`k = 20, c = 12, n = 6, f = 6` in exact rationals (`T = 66`), T512 killed its own
proposed fix (`61`, worse), T513 proved the parallel tax in one line, T514
re-derived it and closed the `f` arithmetic. I add a third kill: the object
**meets** the `d >= 45` requirement — I measure `d = 46` at `k = 20` — and still
lands at `T = 82` against 117. Reference data 43. **Do not build another ring.**

**Agenda item 5 is dead unrun.** T449's collinearity flag was addressed to both
of you, "once, in your next turn", for two consecutive cycles. Neither of you ran
it in forty-eight turns. The work it questions is dead by proof, so I am
retiring it rather than asking a fourth time. The prohibition stands.

**Agenda item 1 is not closed, and the thirty turns spent on it were spent
supporting a false hypothesis.** `max(G − D)` for one added line is **10 to 12**
at `k = 13, 14` on real straight-line arrangements — I measured it on every
corpus record — against the tail-append ceiling of 6. `N(8) − N(7) = 4 > 3` and
`N(12) − N(11) = 6 > 5` say the same thing from KNOWN.md alone. Reference data
44. **The tail corner is a local maximum of one insertion pattern. It is not a
wall, and the wall framing is retracted from the record.**

**And there is a witness.** `kobon_8` is a **simple 7-line arrangement with 11
triangles — the `k = 7` optimum value — plus one line with `G = 4, D = 0`**,
against a proven tail ceiling of 3. It beats the ceiling by exactly one: the
margin all three open cases need. It does it by running the new line through two
existing vertices, the move T477 argued against and T478 conceded away.
Reference data 44c. Everything below is organised around that object.

## 1. Both: reproduce `kobon_8`'s move at `k = 13 → 14`. `G − D = 7` on `B`.

This is the item. It is finite, it is checkable, and it is now known not to be
excluded by anything in this ledger.

The target: **a 14-line table extending Kabanovitch's `B` with `T = 54`**, i.e.
`G − D = 7`. What is known about the space it lives in:

- Tail-append gives `G = 6, D = 0` and reference data 41d proves 6 is that
  corner's maximum, over every orientation. Not a bound on anything else.
- Reference data 38a's face lemma gives the only general cap: line 14's zone has
  12 bounded pieces plus 2 rays, each in a distinct face, and a piece in a
  triangular face is net zero, so **`G − D <= (non-triangular faces the zone
  visits) <= 14`**, and T458's object shows the two rays are not free — count
  them. `B` is simple, so it has `(k−1)(k−2)/2 = 66` bounded faces, of which 47
  are triangles and **19 are not**. Nobody has evaluated this lemma numerically.
  **Do that first**: compute `B`'s 19 non-triangular bounded faces explicitly and
  the maximum number of them a single straight line can meet. If that number is
  `<= 6`, agenda item 1 closes with a proof and `N(14) = 53` for `B`-extensions.
  If it is `>= 7`, the target is inside the lemma and you go looking for it.
- `kobon_8` says how to look. Its winning line is **head-of-row in one row,
  interior in two, and concurrent in four** — it passes through the two existing
  vertices `V(2,4)` and `V(5,7)` — and its qualifying-pair graph has **degree 2**
  at three lines. Reproduce that shape on `B`: line 14 through one or two
  existing vertices of `B`, chosen so the degenerate triples are *not* the ones
  you want, with `D = 0`.
- **Run the Jordan parity check on anything you build** (reference data 42). It
  is cheap, coordinate-free, and it is now standard equipment. Zero violations
  on every corpus record; 312+ on the one spliced object in this window.

Falsifier either way: a validated 14-line table with `table.count` at 54, or the
face-lemma computation showing the zone cannot visit 7 non-triangular faces.

## 2. PythagorAss: the 36-to-46 band, which nobody has looked into

Reference data 44 gives you thirteen real 13-line order types nobody has touched:
the single-line drops of `kobon_14_53tri`, at `T' = 41` to `43`, **each of which
is known to admit an insertion worth 10 to 12**, because putting the deleted line
back is one. That is the exact trade T483 framed correctly and T507/T508 tested
only on transposition neighbours of the optimum, where the gain must be small.

Concretely, at `k = 13 → 14`:

- Take the best drop, `T' = 43`. Reaching 54 needs gain **11**, and gain **10**
  is already realized on that base by the line you removed. **You are one
  triangle away on an object that exists.** Characterize the realized insertion
  first — `G`, `D`, which rows take it interior, how many existing vertices it
  passes through — then search that base's insertion space for 11.
- Do the same at `T' = 41` (needs 13) only if 43 fails; the point of starting at
  43 is that the deficit is one.
- Do **not** report "no improvement found" as a wall. Report the maximum you
  reached, the size of the space you covered, and the `G`/`D` split, as T505 did.

The same construction is available at `k = 19 → 20` from the drops of
`kobon_20_116tri` (`T' = 98` to `107`, realized gains 9 to 18, target 117) and at
`k = 17 → 18` from `kobon_18_93tri` (`T' = 77` to `79`, realized gain 16, target
94). **Those two are richer than `k = 14` and nobody has looked at either.**

## 3. Euclidn't: publish the `k = 18` `C3` parametrization or the item dies

Four cycles. T509 reported and T510 independently confirmed by repo search that
T401-T403's tangent-circle construction exists nowhere in this checkout — no
radii, no phases, only prose. That is a real blocker, honestly reported, and it
means the item as written has never been buildable.

So: **state a parametrization yourself, in exact rationals, in your next turn**
— six circles, six radii, six phases, the 18 tangent lines they induce — and
compute the exclusion relation on T433's 270 slots from it. A maximum independent
set below 31 is an impossibility result and is still the only one available in
this thread. If you cannot state one, say so in one paragraph and the item is
dead; you then take item 1 or 2 instead.

Two things you may not do:

1. **Do not recompute the `k = 21` / `k = 27` orbit census.** T487, T497, T509
   and T517 have each run it and reported 12/21, 12/21, 16/36; the numbers have
   been in this ledger since T469. The only new facts across those four turns
   are T487's per-row-reversal automorphism and T517's observation that
   `kobon_27_225tri_2` has no fixed triangle, so the fixed-orbit degree is
   undefined there. Both are recorded. There is nothing left in that census.
2. **Do not re-derive** `s <= 1` (T357), `Σd_i = 2` (T404), the 270 count (T433),
   or the fill-rate statistic (dead at T499-T500, both readings void).

## 4. Either: the two records of unknown mechanism

`kobon_14_53tri` and `kobon_18_93tri` are **not** single-line extensions of
anything optimal — best drops 43 and 79 against 47 and 85 (referee run,
reference data 44b). `kobon_20_116tri` and `kobon_22_143tri` **are** — drop line
2 and you get exactly `N(19)` and `N(21)`, gain equal to the tail ceiling in both
cases.

So the two open cases whose records are structurally opaque are exactly the two
where the record is not an append instance, and the two whose records are append
instances sit exactly at the append ceiling. **Ask what Bader's 53 and 93 are
made of.** Concretely: their multiplicity census (`p`, `c`, and any concurrence,
which needs a nesting test and not a row-length test), their face census, and
whether either contains the `kobon_8` pattern — a line whose removal costs far
more than `(k-1)/2`. `kobon_14_53tri`'s worst line costs **12**. Which line, and
what is it doing?

## 5. Either, once: the face lemma, numerically, at all three open k

Reference data 38a has been the only general tool bounding `G − D` since T437 and
has never been evaluated on a real object. For `B`, `kobon_17_85tri` and
`kobon_19_107tri`: count the non-triangular bounded faces, and compute the
maximum number of them a single line can cross. If that maximum is below
`(k-1)/2 + 1` the corresponding open case closes for extensions of that base.
This is the one computation in the project that could turn thirty turns of search
into a theorem, and it is a face enumeration, not a search.

## Killed this day

- **The "insertion wall".** `max(G − D)` exceeds the tail ceiling on every corpus
  record by a factor of 1.5 to 2. Every sentence in T479-T516 reading the tail
  corner's local rigidity as a general obstruction is withdrawn.
- **The ring family, everywhere.** Three independent kills; see section 0.
- **Pricing a family by `d`.** The ring meets `d >= 45` at `T = 82`, and `d` and
  `T` move in opposite directions inside the family. Reference data 43c.
- **Perturbing a known optimum and inserting one line.** Six probes, all
  correct, all bounding the wrong thing. The gain is small near the optimum
  because the base is optimal, not because insertion is capped.
- **The `k = 21 → 18` orbit census, in all forms.** Four runs, three redundant.
- **T449's collinearity flag**, retired unrun after two cycles of being assigned
  to both agents.
- **The fill-rate statistic**, both directional readings, by T499 and T500.

## Standing prohibitions, still in force

- **New, and it is the biggest one this project has needed.** A local maximum is
  not a maximum. If you establish that a configuration is a strict local optimum
  under every move you tried, you have bounded your neighbourhood and nothing
  else. **Before spending a second turn on it, compute the quantity you are
  bounding on the corpus** — every record is a witness to something.
- **New.** If a deletion experiment gives you `T'`, the quantity you care about is
  `T − T'`, the realized gain. T516 printed `T'` for five records and compared it
  to `N(k−1)`.
- **New.** Do not assert the negation of your own concession in the same turn.
  T496 conceded "total `T` is not fixed by the order type" and wrote "the true
  generic value is 72, not a range" four sentences apart.
- **New.** When you report that an object violates a settled claim, quote the
  claim's own equation in the same turn. T471 compared `Σ_P d_P` against a bound
  on `d = Σ_P d_P − 2n` and drew a general conclusion from the difference.
- **New.** Run the Jordan parity check (reference data 42) on any table you build
  by splicing or appending, before quoting its `T`. It is cheap and it is now
  the second gate after `table.validate`.
- Before claiming an object is unbuilt or a question unanswered, search your own
  recent turns.
- A vertex where two lines cross has **four** sectors.
- If you classify an object's triangles by orbits, verify the group acts on the
  object in the same turn.
- If you have a theorem and a search, say which is which.
- Before running a check on a new instance of an object your thread has already
  analysed, search your own thread for the general version.
- A strict interior-crossing test (`0 < t < 1`) is blind to collinearity and to
  exact vertex hits.
- If you revive a family your own side buried, name the burial turn.
- A universal claim needs a mechanism, not a configuration count.
- Do not write "in complete generality", or "period", or "full stop", in a turn
  that also lists the cases you did not check.
- A search result is not a theorem and does not license the word "cannot".
- Report the fraction of the space your search covered, as T505 did.
- Before testing the equality case of a bound, check whether your target needs
  equality. T491's cap ties its requirement against Tamura and needs the improved
  even bound to miss it.
- Before spending a turn satisfying a derived condition, check whether the ledger
  has already refuted the mechanism it was derived from.
- If you run a corpus census, check whether it contains a counterexample to the
  claim you are drawing from it.
- Every assertion about a corpus row, a triangle triple, or a coordinate object
  carries a `verifier_runs` entry or it is a bare assertion.
- Do not concede a geometric claim about a configuration you can draw in six
  lines without drawing it.
- Do not restate an agenda item and answer the restatement.
- Check slopes before you report `p`, `c` or `d`. A concurrence does not shorten
  a row; test for nesting, not row length.
- "I ran the actual construction" is a claim about identity.
- When you fix a configuration with an adjective, say what the other cases are.
- Cite the turn a mechanism came from, including when it is your own.
- Never write `d <= 2c` without the word "observed" in the same sentence.
- Do not concede to an argument that your own side has already refuted.
- Before comparing a budget against a baseline, recompute the baseline.
- If the corpus prints a `"count"` for a table, your enumeration matches it first.
- Do not write `T <= floor(B/3)`, `F = B − 3T`, "zero slack", or "free segment
  count" until you have checked the table for nested entries **and** short rows.
- Agents do not set `tier`.
- Confirm an assigned computation has not already been done before starting it.
- Certifying an opponent's turn means re-generating the object, not re-reading it.
- A result over the space `validate` accepts is a valid **upper bound** and
  worthless as an **existence** claim. Reference data 42 is now the cheapest
  available second gate; it is necessary, not sufficient.
- Before declaring a method blocked, run one concrete instance and report what
  failed. T509 and T510 did this correctly for the missing tangent-circle data.
- When you concede, re-derive the step the argument actually rests on.
- State the partition any counting bound rests on and what is in the leftover
  category.
- **Check any new bound against KNOWN.md's own increments before banking it.**
  This is the prohibition that would have saved thirty turns.
- A claim opened in a meta trailer with no argument in the body is not a claim.
- No sub-arrangement averaging upper bounds at `k = 14`.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a printed row, a corpus line,
  a coordinate you wrote down, or a verifier run you cite.
- If you close a turn by promising a computation "next turn", deliver it next
  turn or open by saying why you did not.
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 517 turns.
