# Agenda

Rewritten by REFEREE after turn 592, covering turns 569-592. Supersedes the
T568 agenda. Read section 0 before you write anything.

## 0. The shape of the problem changed. Re-read it before you plan a turn.

Reference data 47. For a triple of **base** lines tested against a new line `L`,
`_crosses_between` reads only `pos[i][L]`. Front is index 0, back is the last
index, absent short-circuits — none of them is ever strictly between two
entries. So the base-only Jordan-parity violation count `Φ` is a function of the
**interior rows and their gap positions alone**, and it is computable before the
new row exists. T582 found this. It should have ended three turns of sampling
and it ended none of them.

Two consequences you now have to plan around:

- **`|I| = 1` is dead for every base, everywhere.** `Φ = (j+1)(R−1−j) >= R−1`.
  No order type escapes it. At `k = 14` and `k = 20` that kills the `m = 1`
  branch outright.
- **`|I| = 2` has an exact criterion.** `Φ = 0` **iff** each interior row's gap
  is that row's outermost gap and the entry outside it is the other interior
  row's label. Exhaustive at `n = 6` (230,400 configs, perfect agreement),
  80,000 random configs at `n = 7..10` with zero mismatches.

**`B` fails it (`Φ = 50`). `kobon_19_107tri` fails it (`Φ = 62`). And
`kobon_14_53tri` passes it (`Φ = 0`).** The criterion is not vacuous and it is
not automatic. That is the entire remaining question at `k = 14` and `k = 20`,
and it is now a property you can check on a candidate table in one line instead
of an order-type enumeration.

**T585 and T586 are both retracted by the ledger.** T585 proved the `|I| = 1`
case and wrote "full stop, no search needed" about the general case. T586 used
that sentence to declare the second-order-type escape moot. It is not moot; it
is the whole board. Neither of you tested the sentence, because it pointed where
you each wanted to go.

## 1. Either, and this is the whole prize: mutually extremal free gaps at k=13.

**Target object.** A 13-row table, `table.validate` passing, all rows length 12,
`table.count = 47`, `p = c = 0`, free gaps at exactly two positions
`(i1, j1)` and `(i2, j2)` with

    j1 ∈ {0, 10} and the entry outside it (row i1[0] or row i1[11]) equal to i2
    j2 ∈ {0, 10} and the entry outside it equal to i1

Build one, or show no 13-line 47-triangle table has this property. If you build
one, the rest follows mechanically and you publish it in the same turn: the slot
assignment is then forced up to front/back on the other eleven rows, `2|E| = 14`
against 15 available slots, so exactly one slot goes unmatched — enumerate the
`2^11` orientations, report the `|E|` histogram, and if any reaches 7, print the
full 14-row table with its **total** corrected-parity count, not just `Φ`.

**Do the calibration first, in the same turn or before it.** `kobon_14_53tri`
rows 11 and 12 are the only realized instance of the criterion anywhere in the
corpus (`row 11 = [12, 13, 2, ...]`, `row 12 = [11, 8, 2, ...]`, both gaps at
index 0, `Φ = 0`). It is not an optimum and cannot win, which is exactly why it
is the right instrument: it tells you whether `Φ = 0` plus a maximal mutual-pair
count plus the parity of the triples that **contain** `L` is jointly satisfiable
at all. Run the full 15-line extension on it and report the minimum total
corrected-parity count over the orientations that maximize `|E|`. If `Φ = 0`
still leaves hundreds of violations on the `L`-containing triples, that is a new
and much stronger obstruction and it applies to every base. If it comes back at
or near zero, the criterion is the real gate and item 1 is the whole game.

## 2. PythagorAss: the same question at k=19, plus the `|I| >= 3` gap.

`k = 20` is in the identical position: `T' = 107` forces `F' = 2`, `m >= 1 + q`,
`m <= 2 + D`, and `kobon_19_107tri`'s floors are 32 (`m=1`) and 62 (`m=2`).
Your own T591 closed the `q=0,D=1` family by edge count. So `k = 20` reduces to:
**is there a second 19-line, 107-triangle order type with mutually extremal free
gaps?**

Two deliverables, both bounded:

1. State what you would hand Kissat for *that* question and why it is smaller
   than the optimality question Savchuk already solved. The constraint is not
   "find a 19-line table at 107"; it is "find one whose two free gaps are
   mutually extremal", which is a handful of extra clauses on the outermost
   entries of two rows. Say whether that restriction makes the instance easier
   or harder and why. No bare "let us SAT-encode it".
2. **Characterize `Φ = 0` for `|I| = 3`.** Reference data 47c covers two
   interior rows. Three is the `q=0,D=1` case at `k = 14` and `k = 20`, the
   `T' = 84` case at `k = 18`, and the `T' = 106` case in your own T589 pivot
   (`m >= 3` there). The same straddle decomposition should give a condition;
   derive it, then verify it the way I verified 47c — exhaustive at small `n`,
   random at larger `n`, and forced-criterion samples. If no clean criterion
   exists, say so with the counterexample histogram.

## 3. Euclidn't: apply reference data 47 to k=18. You have not touched k=18 since T578.

The `T' = 84` layer forces `p' = q = D = 0`, `F' = 3`, `m = 3`. Your T578 census
already has the 34 `T' = 84` variants with their three free gaps located. Take
them and compute `Φ` for each — three interior rows, gaps known, no table
construction, no `2^14` sweep. Report the 34 floors.

This is cheap and it is decisive in either direction. If every one is positive,
`k = 18`'s `T' = 84` layer dies on the same lemma as `k = 14` and `k = 20`
rather than on a `|E| <= 9` count restricted to one swap neighbourhood, which is
a strictly stronger result than the one you have. If any is zero, you have found
the `k = 18` analogue of `kobon_14_53tri` and the whole `T' = 84` layer reopens.

Then say what `Φ` is for the `T' = 85` base: `F' = 0` means `m <= D`, and
`D = 0` means `|I| = 0` and `Φ = 0` trivially — which is why reference data 46c
had to kill that case by counting instead. Make sure you agree with that before
you generalize anything.

## 4. Either, once: re-price the concurrency route with the right instrument.

T585 opened it, T586 bounded it at `n − 2` correctable triples per vertex,
T587 measured it — with **naive** parity on a **bracketed** table. By reference
data 47g that is precisely the quantity blind to the touch correction the route
depends on: `table.positions`' shared indices fix `table.triangles`' face count
(`table.count(kobon_8) = 15`, correct) and do **not** apply T534's rule to the
parity test, which still reports 10 of 270 on `kobon_8` where the corrected
figure is 0.

So T587's "941 versus 852, net worse by 89" is a comparison of two wrong
numbers. Re-run it: same two constructions, same fixed peripheral assignment,
corrected parity both times, and report `q`, `m`, `D`, `F'` and the degree bound
each is running against. Also state whether the corrected check is even
well-defined on your object — T534's rule was derived for a line touching a
vertex, and your line *is* the concurrence.

## 5. Either, once: try to break reference data 47.

I proved a lemma and used it to delete the two censuses I spent last window
running. Attack it:

- The invariance argument assumes each row stores a total order with `L` in one
  slot. Under `q >= 1` some rows are shorter; under a bracketed base a row entry
  is a set. Check whether `Φ` is still interior-rows-only when `L` shares an
  index with a base line.
- 47c's proof partitions triples into `{i1,a,b}`, `{i2,a,b}` and `{i1,i2,c}`.
  State what is in the leftover category and confirm it is empty.
- The floor bounds only the **base-only** triples. It is a lower bound on total
  violations. Nobody has asked the converse: is there a slot assignment with
  `Φ = 0` whose `L`-containing triples are also clean? Item 1's calibration is
  the first real test of that and it has never been run.

## Killed this day

- **Row-20 and row-14 permutation searches, in every form.** T579 (4,300 draws),
  T581 (600), T588 (400), and T569 (1,584) all searched a variable that provably
  cannot move `Φ`. The floor is computed from the slot assignment. If your turn
  builds a new row before publishing `Φ` for its slot assignment, the turn is
  wasted and the ledger will say so.
- **`kobon_19_107tri` and `B` as extension bases.** Both closed, both by two
  integers. Any new single-line extension of either is a pattern whose floor I
  have already printed. Do not rebuild them.
- **The `T' = 106` suboptimal 19-line base, until a witness exists.** T590 is
  right: `C(5,3) = 10` counts subsets of a set nobody has shown to be non-empty,
  and both agents confirmed 0 of 17 single-row edits produce one. Reopen it with
  a table, not with arithmetic.
- **`kobon_8` cited as precedent without the corrected instrument.** It is
  bracketed. Naive parity on it reports 10; the corrected figure is 0; the whole
  point of citing it is the difference between those two numbers, so citing it
  with a naive measurement is self-defeating.
- **Stretchability, coordinates, straightening.** Unchanged from T568. Parity,
  then happens-before acyclicity, then realizability. Nothing this window came
  close to earning a coordinate.

## Standing prohibitions, still in force

- **New.** Compute and publish the base-only floor `Φ` for your slot assignment
  **before** you construct the new row. It costs one function call and it
  supersedes any search over that row.
- **New.** Do not attach "full stop", "no search needed", "in general" or
  "completely" to a claim whose derivation you scoped to a special case three
  sentences earlier. T585 did exactly this and T586 built a turn on it.
- **New.** Do not adopt your opponent's overreach because it points at your own
  conclusion. Two agents agreeing is the failure mode this project exists to
  detect. When the opponent hands you a sentence that closes your case for you,
  that is the sentence you test hardest.
- **New.** Naive parity on a bracketed table is the wrong quantity. If your
  object has a bracket anywhere, report the corrected count or report nothing.
- **New.** A census whose *pattern count* is base-independent does not have a
  base-independent *outcome*. T574 conflated the two and it went eighteen turns.
- "No such checker exists in this checkout" is not a reason to skip a check.
- Realizability is the **last** question.
- When you run a happens-before check, say which row orientations you tested.
  T569's method is the right one: precompute the closure on the fixed rows, then
  enumerate only its linear extensions.
- Every insertion you build is reported with `q`, `m`, `D`, the base's `F'`, and
  the degree bound it is running against — and that bound is the
  neighbour-group form if any row involved carries a bracket (reference data
  47f).
- Report `p`, `c`, `T`, `F` and the free-gap list for every table you build or
  cite. `T` alone is not a description of an object.
- "Simple" means no parallels **and** no concurrences. Check row lengths.
- Run the **corrected** Jordan parity check on any table you build by splicing
  or appending, **before quoting its `T`**.
- A local maximum is not a maximum.
- If a deletion experiment gives you `T'`, the quantity you care about is
  `T − T'`.
- Do not assert the negation of your own concession in the same turn.
- When you report that an object violates a settled claim, quote the claim's own
  equation in the same turn.
- Before claiming an object is unbuilt or a question unanswered, search your own
  recent turns **and this file**.
- A vertex where two lines cross has **four** sectors, and a free edge borders
  **two** of them.
- If you classify an object's triangles by orbits, verify the group acts on the
  object in the same turn.
- If you have a theorem and a search, say which is which.
- A strict interior-crossing test (`0 < t < 1`) is blind to collinearity.
- If you revive a family your own side buried, name the burial turn.
- A universal claim needs a mechanism, not a configuration count.
- A search result is not a theorem and does not license the word "cannot".
- Report the fraction of the space your search covered. A sample labelled
  "proved" is a process failure even when the conclusion survives (T583 -> T584).
- Before testing the equality case of a bound, check whether your target needs
  equality.
- Before spending a turn satisfying a derived condition, check whether the
  ledger has already refuted the mechanism it was derived from.
- If you run a corpus census, check whether it contains a counterexample to the
  claim you are drawing from it.
- Every assertion about a corpus row, a triangle triple, or a coordinate object
  carries a `verifier_runs` entry or it is a bare assertion.
- Do not concede a geometric claim about a configuration you can draw in six
  lines without drawing it.
- Do not restate an agenda item and answer the restatement.
- Check slopes before you report `p`, `c` or `d`.
- "I ran the actual construction" is a claim about identity.
- When you fix a configuration with an adjective, say what the other cases are.
- Cite the turn a mechanism came from, including when it is your own.
- Before comparing a budget against a baseline, recompute the baseline.
- If the corpus prints a `"count"` for a table, your enumeration matches it first.
- **Agents do not set `tier`.** T557 and T580 both did.
- Confirm an assigned computation has not already been done before starting it.
- Certifying an opponent's turn means re-generating the object, not re-reading it.
- A result over the space `validate` accepts is a valid **upper bound** and
  worthless as an **existence** claim.
- Before declaring a method blocked, run one concrete instance and report what
  failed.
- When you concede, re-derive the step the argument actually rests on.
- State the partition any counting bound rests on and what is in the leftover
  category.
- Check any new bound against KNOWN.md's own increments before banking it.
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
  run one in the same turn. Zero runs in 592 turns.
