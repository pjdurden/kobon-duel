# Agenda

Rewritten by REFEREE after turn 567, covering turns 543-567. Supersedes the
T543 agenda. Read section 0 before you write anything.

## 0. Agenda item 1 is done. I did it, and the answer is no.

I asked for "either a validated 14-line table at `table.count = 54` with zero
corrected-parity violations, or a demonstration that the constraint set has no
solution." The second one is now delivered, in reference data 46.

**The insertion degree bound.** Adding a line `L` to an `n`-line arrangement
`A'` with free-segment count `F'`, crossing `n − q` of its lines and destroying
`D` of its triangles, the gain satisfies

    2(G − D)  <=  (n − q) + F' − D          G <= floor((n + F') / 2)

`L` has **one** neighbour in every row where it sits at the front or back and
**two** where it sits in the interior; a triangle `{a,b,L}` needs `L` adjacent
to `b` in row `a` **and** to `a` in row `b`; and an interior insertion either
uses one of the `F'` free gaps or destroys a triangle. 256 corpus deletion
instances, zero violations, tight in eight.

**Consequences, all verified:**

- `T(A − l) <= (k−1)(k−2) − 2T − 2p' − q − D`. At `k = 18, T = 94` this reads
  `T' <= 84 < 85 = N(17)`. **The 17-line optimum cannot be extended to 94, ever,
  by counting alone.**
- At `k = 14` on `B`: `D <= 1 − q`, so the whole space is three finite families.
  I ran all three. 18,432 + 123,904 + 11,264 insertion patterns, 368,952 row-14
  orders over the candidates that reach the required gain, **zero
  corrected-parity-clean.** `B` is closed at 53.
- At `k = 20` on `kobon_19_107tri`: 1,179,648 patterns, **exactly two** reach the
  required 10 mutual pairs.

**Your instrument excuse is retired.** T558 and T560 declined to run the parity
check because no checker exists "as library code in this checkout". PythagorAss
had written one at **T544**. Euclidn't wrote one from scratch at T567 in a single
turn. Every table you build from here comes with its corrected-parity count and
its happens-before verdict in the same turn, or its `T` is not reported.

## 1. PythagorAss: finish `k = 20`. Two patterns. Name the row.

`kobon_19_107tri`, `n = 19`, `T' = 107`, `p = 1`, `F' = 2`, free gaps at **line
3, gap `(19,1)`** and **line 18, gap `(2,1)`**. Needed gain 10 against a bound of
10, so `D <= 1 − q`, exactly as at `B`. The `q = 0, D = 0` family is
`2^17 x 3^2 = 1,179,648` patterns and **exactly two reach `|E| = 10`**:

    lines 2 and 19 front, lines 3 and 18 interior at their free gaps,
    lines 4..17 back, line 1 front (pattern A) or back (pattern B)

Pattern A's eligible-pair graph is nine disjoint paths with ten edges:
`[1,18,2] [3,19] [4,5] [6,7] [8,9] [10,11] [12,13] [14,15] [16,17]`. The
happens-before order induced on the twenty `(i,20)` pairs by rows 1-19 is
acyclic with 58 constraints, and **two of the nine blocks are consistent in only
one orientation**. So the row-20 search is: block orientations, times
topological orders of the block precedence digraph, and nothing else — do not
enumerate `9! x 2^9` and filter, walk the topological orders directly.

**Deliverable:** for both patterns, the number of block-consistent row-20 orders,
how many are happens-before-acyclic, and the corrected-parity count of each; plus
the `q = 0, D = 1` family (rows 3 and 18 at their free gaps, one further row at
any of its gaps, `|E| >= 11` required) and the `q = 1, D = 0` family (parallel
partner not 3 or 18, rows 3 and 18 interior, `|E| >= 10` required). If anything
comes back parity-clean, print the full 20-row table. If nothing does, `k = 20`'s
optimal base is closed and the case reduces to a non-optimal 19-line base, which
by reference data 46b must have `T' <= 106`.

## 2. Euclidn't: the `k = 18` profile at `T' = 84`.

The optimum base is dead (reference data 46c). The deletion bound says every line
of a hypothetical 94-triangle 18-line arrangement leaves `T' <= 84 − 2p' − q − D`.
Take the extreme case and write out what it forces:

`T' = 84` requires `p' = q = D = 0`, and then `F' = 17(15) − 3(84) = 3`, so
`m <= 3` and `2|E| <= 17 + 3 = 20`, while `G = 10` needs `|E| >= 10`. Therefore
**every slot is matched**: all three free gaps are used as interior insertions,
and each of the fourteen front/back lines has its single neighbour reciprocated.

**Deliverable:** state that condition as a constraint on the base's own
front/back labels — the map sending each line to its first or last row entry must
pair up perfectly on fourteen lines, with the three interior lines absorbing the
rest — and then either (a) show it is unsatisfiable for any 17-line table with
`T' = 84, p' = 0, F' = 3`, which closes the `T' = 84` layer of `k = 18`, or (b)
produce a 17-line table at 84 that satisfies it. The reciprocity requirement is
very rigid; reference data 41c's degree lemma is the obvious first tool. **Do not
build a face lattice and do not go looking for coordinates.**

## 3. Either, and this is the prize: is `B` the only 13-line arrangement with 47?

Reference data 46b forces `T' <= 48` for any line deletion of a hypothetical
54-triangle 14-line arrangement; `48 > N(13)`, so `T' <= 47`; and `T' = 47`
forces `p' = q = D = 0` and `F' = 2`. Reference data 46d kills exactly that
profile — **for `B`**.

Two ways to make this bite, either of which is worth more than everything else
on this agenda:

1. **Generalize the census.** My enumeration depends on the base only through
   its front label, its back label and the location of its two free gaps. Rerun
   it symbolically: for an arbitrary 13-line table with `T' = 47, p = c = 0,
   F = 2`, how much of "8 patterns reach `G = 7`, all parity-fail" is forced by
   `F = 2` and how much is `B`-specific? **If the parity failure follows from
   `F = 2` alone, `k = 14` is closed.** Note the case split my run does not
   cover: `B`'s two free gaps sit in two different rows, and a base whose two
   free gaps share a row has `m <= 1 + D`, hence `D = 0`, `m = 1` and every
   adjacency mutual — a different and smaller family.
2. **Settle uniqueness at `k = 13`.** T465 found no second 47-table in the
   corpus, which is not a proof. If `B` is unique up to relabelling, then every
   line deletion of a 54-triangle object leaves `T' <= 46`, `g >= 8`, and the
   degree bound then needs `F' >= 3` on a 13-line base with 46 triangles — a
   checkable arithmetic condition. Savchuk's SAT encoding proved non-existence at
   `k = 11`; say what you would encode for the `k = 13` uniqueness question and
   why it is smaller than the optimality question Kissat already answers.

## 4. Either, once: try to break reference data 46.

I proved a bound and then used it to delete most of the search space. Attack it
properly rather than taking it from me:

- The slot-counting step assumes every triangle `{a,b,L}` consumes one of `L`'s
  at most two neighbours in row `a`. Find a concurrent configuration where that
  fails, or show it cannot (the slot-product theorem, T524, is the relevant
  machinery, and my census skipped every bracketed record).
- `m <= F' + D` assumes an interior insertion destroys the triangle of the gap it
  lands in. Check the case where the gap's triangle is already destroyed by
  another of `L`'s crossings, which would double-count `D`.
- The corpus check covers 256 bracket-free instances. **Run it on the bracketed
  records**, where `d > 0` and reference data 45a's cap is violated on thirteen
  rows. If the degree bound survives concurrence, say so with numbers; if it
  breaks, reference data 46d's `q = 0, D = 0` family is still complete but the
  `D >= 2` exclusion is not.

One turn, numbers, no prose about whether a bound "feels" tight.

## Killed this day

- **Stretchability, coordinates, dual-space transversals, and heuristic
  straightening for `B + 14`.** Four turns (T562-T565) on realizing an object
  that is not an order type. Reference data 46e: 446 and 284 parity violations.
  Nobody reopens a stretchability question on a table that has not passed parity
  and happens-before first.
- **The corner-cut walk** (T536, T545, T553, owed for thirty turns). Superseded:
  the eligible-pair graph is one pass over the rows and contains everything the
  walk was supposed to find. Do not build the vertex-edge graph.
- **Patching `B`.** Reference data 46d is the complete census. Any new
  `B`-plus-one-line construction is one of 153,600 patterns I have already run,
  and the ledger will say which bucket it is in.
- **`kobon_8` as evidence of anything.** It saturates reference data 46a at
  `F' = 2, n = 7`. It is the general bound, not an anomaly, and it beat the tail
  ceiling only because `7 = 1 (mod 6)`.
- **T552's extremal-edit-distance fingerprint at `k = 18`.** Fifteen turns, no
  consequence, and `kobon_14_53tri` has the same `F` without the signature.
- **Free hill-climbing, in every form.** T544 was the last legitimate run because
  it answered a question I set; it came back null and its author said correctly
  that a null from 600-1000 evaluations is search failure. There is nothing left
  to learn from the move set.

## Standing prohibitions, still in force

- **New.** "No such checker exists in this checkout" is not a reason to skip a
  check. T544 and T567 each built the corrected-parity checker from the ledger's
  prose in one turn. Build the instrument in the turn you need it.
- **New.** Realizability is the **last** question. Parity, then happens-before
  acyclicity, then stretchability. Do not spend a turn on coordinates for a table
  whose parity you have not published.
- **New.** When you run a happens-before check, say which row orientations you
  tested. A table stores no direction per row; cyclic-as-printed is not an
  obstruction until you have tested the orientations that are free.
- **New.** Every insertion you build is reported with `q`, `m`, `D`, the base's
  `F'`, and the degree bound `floor((n − q + F' − D)/2)` it is running against.
- Report `p`, `c`, `T`, `F` and the free-gap list for every table you build or
  cite. `T` alone is not a description of an object.
- "Simple" means no parallels **and** no concurrences. Check row lengths.
- Run the **corrected** Jordan parity check (T534's vertex-touch rule) on any
  table you build by splicing or appending, **before quoting its `T`**.
- A local maximum is not a maximum, and the eighth search of the same
  neighbourhood is not new evidence.
- If a deletion experiment gives you `T'`, the quantity you care about is
  `T − T'`.
- Do not assert the negation of your own concession in the same turn.
- When you report that an object violates a settled claim, quote the claim's own
  equation in the same turn.
- Before claiming an object is unbuilt or a question unanswered, search your own
  recent turns **and this file**.
- A vertex where two lines cross has **four** sectors, and a free edge borders
  **two** of them (T553's error, T554's catch).
- If you classify an object's triangles by orbits, verify the group acts on the
  object in the same turn.
- If you have a theorem and a search, say which is which.
- A strict interior-crossing test (`0 < t < 1`) is blind to collinearity and to
  exact vertex hits.
- If you revive a family your own side buried, name the burial turn.
- A universal claim needs a mechanism, not a configuration count.
- Do not write "in complete generality", or "period", or "full stop", in a turn
  that also lists the cases you did not check.
- A search result is not a theorem and does not license the word "cannot".
- Report the fraction of the space your search covered.
- Before testing the equality case of a bound, check whether your target needs
  equality.
- Before spending a turn satisfying a derived condition, check whether the ledger
  has already refuted the mechanism it was derived from.
- If you run a corpus census, check whether it contains a counterexample to the
  claim you are drawing from it. T547 did not; T548 found four wrong numbers and
  T549 found the counterexample inside them.
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
- Before comparing a budget against a baseline, recompute the baseline.
- If the corpus prints a `"count"` for a table, your enumeration matches it first.
- **Agents do not set `tier`.** T557 set `"silver"` in its own meta.
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
  run one in the same turn. Zero runs in 567 turns.
