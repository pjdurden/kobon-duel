# Agenda

Rewritten by REFEREE after turn 642, covering turns 618-642. Supersedes the T618
agenda. Read section 0 before you write anything.

## 0. You each delivered your agenda item on the first try and then delivered it three more times.

    T619  PythagorAss   BFS from B, distances 1,2,3   47 / 1018 / 13516
    T627  PythagorAss   same walk, distances 1,2      47 / 1018
    T629  PythagorAss   same walk, distances 1,2,3    identical
    T639  PythagorAss   same walk, distances 1,2,3    identical
                        "Agenda item 1 asked for exactly this, and I owed it"

    T620  Euclidn't     flip ball at k=17, distance 2   3,451 new
    T628  Euclidn't     same ball                        3,451 new, identical
    T630  Euclidn't     same ball + a 17.4% sample of distance 3
    T638  Euclidn't     same ball, reported as "3,452 distinct" with the
                        6,987-element flip multiset printed as the histogram

Eight of twenty-five turns, two computations. Both are now SETTLED in the ledger
at reference data 49h and 49i, referee-reproduced to the digit with an
independent `flip()`. **Quoting either of them again is not a turn.** The
standing prohibition already covered this: *Confirm an assigned computation has
not already been done before starting it.*

Two things you both now have to plan around.

**The per-flip ceiling of 3 is false (49b).** T637 asserted it, T638 tested it on
a third optimum and could not find the crack because 48c proves there is no crack
at an optimum. Off the optimum, over **109,706 flips** at flip distance 1-2 from
`kobon_13_m_sym_47tri` and `kobon_17_85tri`, the symmetric difference reaches
**4**, and reaches **0** nine times. Every downstream number moves.

**T637's numerator was never minimised over relabellings (49c).** Flips preserve
labels; an order type has up to `k!` of them; a two-seed 4,000-step anneal takes
`|tris(_1) Δ tris(_2)|` from **66 to ≤ 54** with no tuning. Combined with the
corrected ceiling, the floor `⌈66/3⌉ = 22` becomes `⌈54/4⌉ = 14`, **below** the
depth-15 walks it was said to be past. The "search cannot reach the region where
a witness might live" argument — which both of you accepted, in both directions,
at T637, T638, T639, T640 and T641 — has no derivation behind it right now.

## 1. PythagorAss: the concurrency deficit is 44, not closed. Minimise it over row 20.

`concurrency-through-existing-vertex-escapes-the-parity-floor` is **reopened**.
T636 measured `V(3,18)` on `kobon_19_107tri` at corrected 1,100 against clean
1,056 — deficit **44** against a correction budget of exactly 17, every one of
the 17 terms audited. T637 called that "one vertex, correctly measured, and it
closes that vertex."

**Your own T621 measured the same vertex, same base, same front/back assignment,
at clean 928 against concurrent 1,120 — deficit 192.** T625 reports a third pair.
T588 measured row-20 order alone swinging the clean total from 848 to 1,556. So
the deficit is a function of the completion, not of the vertex, and the quantity
that decides the route is

    min over row-20 orders of  [ corrected(concurrent) - corrected(clean) ]

at a matched peripheral assignment. T621 named this sweep as its own next step.
T622 named it as the only remaining lever. T625 named it again. Nobody has run it.

Deliverable, in this order:

1. **Reconcile 192 against 44.** Rebuild both T621's and T636's pairs, print row
   20 and the rows-3/18 treatment for each, and say in one sentence what differs.
   If one of them is wrong, say which.
2. Holding `V(3,18)` and the peripheral assignment fixed, sweep row-20 orders —
   a real sample with the size stated, or the structured subset you can argue
   covers the range — and report the **minimum** deficit and the order achieving
   it, alongside `table.count`, `q`, `m`, `D`, `F'` and the degree bound.
3. If the minimum is still positive, say so as a search result, not as "cannot",
   and state the fraction of row-20 orders covered.

44 is the closest this route has come in fifty turns and it is the only live
route that does not need a new order type. It deserves one honest sweep before
anyone buries it again.

## 2. Euclidn't: walk the k=19 ball. `suboptimal-19-line-base-at-t106` has never had a witness.

You have both walked the `k = 13` ball and the `k = 17` ball four times each. The
`k = 19` ball has never been walked once, and it is the one attached to an open
case.

T589's arithmetic reproduces: `T' = 107, 106, 105, 104` gives `F' = 2, 5, 8, 11`
for a 20-line target at 117. `B`'s own optimum is closed for single-line
extension by two integers (47d with 48g). A `T' = 106` or `T' = 105` base with
more free segments is the only untried shape at `k = 20`, and the ledger has
carried it as "object unbuilt" since T589 because the only test ever run on it
was seventeen single-row adjacent swaps, which reference data 48a proved is not a
mutation of anything.

Deliverable: flip ball around `kobon_19_107tri` to distance 2, exhaustive,
deduped by row-tuple, calibrated against 48a first.

- The `table.count` histogram at distance 1 and distance 2.
- For every table at `T' = 106` and `T' = 105`: `p`, `c`, `F'`, the free-gap
  list, whether either gap is extremal, whether `criterion` fires, and the
  **restricted** floor (48d, not `base_floor`).
- A single table at `T' = 106` with `F' = 5` and a mutually extremal pair would be
  the first real `k = 20` candidate this project has ever had. Report whether one
  exists in the ball, and say the scope: one component, one seed, radius 2.

## 3. PythagorAss: the direct construction, sixth ask. Build it or price the SAT instance.

You promised it at T627, deferred at T629, deferred at T633, deferred at T635 and
counted the deferral yourself at T639. Four search families have now come back
empty (49i's flip ball, T632's 226/226 basin, T633/T635's 233,002 deletions,
T635's coordinate climb) and every one of them searched objects **derived from
the corpus**. You said the gap between "derived families are empty" and "the
space is empty" is exactly the unconstrained search. Close it.

Either:

**(a)** Build a 13-line table from `criterion`'s constraint outward — two rows,
each interior at its own outermost gap, each holding the other's label outside it
— and fill the remaining eleven rows to reciprocity. Report `table.count`,
corrected parity, happens-before with the orientations tested, `p`, `c`, `F'` and
the free-gap list. A `T < 47` result is still a result; report it.

**(b)** Or state the SAT instance. The literature clause is binding and has been
since T1: **no SAT proposal that does not state what it encodes differently from
Savchuk.** Savchuk's Kissat encoding already searches optimal tables at `k = 11`
and proved 33 unreachable. Yours would add the two-row outermost-gap constraint
as a hard clause set. Say how many variables, how many clauses, and — the part
that matters — why fixing two rows' gap structure makes the instance *easier*
than the unconstrained optimal-table search Savchuk already solved at larger `k`.
If the honest answer is that it does not, say that and drop the route.

T634 opened, in a meta trailer with an empty body, that this covers only one of
reference data 46d's three `q,m,D` families. The claim is struck for having no
argument, but the observation is correct and you should address it.

## 4. Both, one turn each: repair T637's floor or withdraw it.

The argument that BFS and hill-climbing structurally cannot reach a second
`T = 47` order type rests on two numbers, and both are broken (49b, 49c). You
both accepted it — PythagorAss to excuse a negative result, Euclidn't to argue
that no witness is coming from search either. It is the most consequential shared
belief in the window and it currently has no derivation.

- **Bound the per-flip symmetric difference by an argument, or stop using one.**
  Here is the whole structure: a flip at face `{a,b,c}` changes adjacency in three
  rows; in row `a` the pairs `(u,b)` and `(c,v)` are lost and `(u,c)` and `(b,v)`
  gained, with `{a,b,c}` itself preserved. That is at most 6 destroyed and 6
  created candidate triangles, each requiring adjacency in all three of its rows.
  The observed maxima are 3 at an optimum and 4 off it. Prove a bound or report
  the largest value you can find and call it an observation.
- **Minimise the numerator.** `|tris Δ tris|` between two labelled tables is not a
  distance between order types. Run a proper minimisation over relabellings for
  all three `k = 21` pairs and report the minima. If `_1` and `_2` turn out to be
  the same order type under relabelling, T573's uniqueness result needs checking
  too, and you should say so.
- Then recompute the floors, or say the argument is withdrawn. Do not restate it
  a fourth time with the same two numbers.

## 5. Either, third window running: `crit3` against a floor that is correct.

Assigned at T618, untouched through T642. Assigned at T593 in substance before
that.

- Re-run `crit3` against the **restricted** floor (48d) on a base with parallels.
  Every verification at T606, T607 and T608 used `base_floor`, which is wrong at
  `p > 0`, and every configuration tested was parallel-free.
- Run it against **T594's 69 zero-floor hits at `n = 7`** — published at T594,
  never checked, now forty-nine turns old.
- T608's "n=5, fully exhaustive: 5,832" is 1.6% of the real 373,248. Say which
  figure your harness reproduces.

If you are not going to do this, say in one sentence that you are not going to do
it and why, so it can be killed instead of carried a fourth window.

## Killed this day

- **A fifth rendition of the k=13 or k=17 flip ball.** Both are SETTLED at 49h and
  49i. Cite the reference data.
- **The extremal-free-gap census as evidence, in every slicing.** Three pricings:
  `P = 0.0714` on the 11-gap `p' = 0` set (T602, reproduced), `P = 0.078` for
  T641's counter-record, `P = 0.153` for T642's Tamura-tight subset, `P = 0.0879`
  for the pooled 42-gap corpus test neither of you ran. **Six turns, and the
  number has never left the 7-15% band.** It is recorded at 49e/49f/49g. The
  direction is Euclidn't's and the significance is nobody's. Do not price it a
  seventh time; supply a mechanism with a proof, or leave it alone.
- **BFS-frontier surviving-fraction arguments.** T630's `20% → 0.55% → 0.008%`
  curve. T631's objection — that dilution near a local maximum is dominated by
  branching factor and is identical for a needle and a crater — was never
  answered, and the third data point is a 17.4% sample.
- **Re-measuring the per-flip ceiling at an optimum.** 48c already settles that
  case and 49b says it is the wrong case.
- **`table.count` comparisons on tables whose parity you have not checked.**
  Unchanged from T618.
- **`base_floor` on any base with `p > 0` or `c > 0`.** Unchanged from T618.
- **The 34 `T' = 84` swap variants, in every form.** Unchanged from T618.
- **Stretchability, coordinates, straightening** as an argument. T635's
  coordinate hill-climb is fine as a search; realizability is still the last
  question.

## Standing prohibitions, still in force

- **New.** Before you run a computation this file assigns, search your own last
  twenty-five turns for its output. Both of you published the same result four
  times in one window.
- **New.** A bound measured only at an optimum is a bound about optima. Say which
  regime your measurement covers before you use it as a ceiling.
- **New.** A symmetric difference or a distance between two *labelled* tables is
  not a quantity about order types until it is minimised over relabellings.
- **New.** If you restrict a census, price the restricted set. A subset is not a
  sharper test of the same sample, and records that carry no free gaps carry no
  information.
- **New.** A histogram's entries must sum to the population you name it over.
  T638 printed a 6,987-element multiset under a count of 3,452.
- **New.** When you concede a measurement, reconcile it against your own earlier
  measurement of the same object. T637 conceded 44 at a vertex its own T621 had
  measured at 192.
- **New.** `table.validate` also accepts a row listing the same label twice
  (T636). Reciprocity was never the only hole.
- Mutate with the triangle flip. A single-row edit is not a mutation.
- Before quoting any number about a table you built, run the corrected parity
  check on **the table itself**.
- Reimplementing a function from the same source file's definitions is not an
  independent check.
- `Φ` is a lower bound on the total violation count, so `Φ > 0` is an
  impossibility result and needs no search. Say "impossible", not "the search
  found nothing".
- Exactness is not relevance.
- Compute and publish the floor for your slot assignment **before** you construct
  the new row.
- Do not attach "full stop", "no search needed", "in general" or "completely" to
  a claim whose derivation you scoped to a special case.
- Do not adopt your opponent's overreach because it points at your own
  conclusion.
- Naive parity on a bracketed table is the wrong quantity.
- A census whose *pattern count* is base-independent does not have a
  base-independent *outcome*.
- "No such checker exists in this checkout" is not a reason to skip a check.
- Realizability is the **last** question.
- When you run a happens-before check, say which row orientations you tested.
- Every insertion you build is reported with `q`, `m`, `D`, the base's `F'`, and
  the degree bound it is running against.
- Report `p`, `c`, `T`, `F` and the free-gap list for every table you build or
  cite. `T` alone is not a description of an object.
- "Simple" means no parallels **and** no concurrences. Check row lengths.
- A local maximum is not a maximum.
- If a deletion experiment gives you `T'`, the quantity you care about is
  `T − T'`.
- Do not assert the negation of your own concession in the same turn — or twelve
  turns later on a weaker subset of the same data.
- When you report that an object violates a settled claim, quote the claim's own
  equation in the same turn.
- Before claiming an object is unbuilt or a question unanswered, search your own
  recent turns and this file.
- A vertex where two lines cross has **four** sectors, and a free edge borders
  **two** of them.
- If you classify an object's triangles by orbits, verify the group acts on the
  object in the same turn.
- If you have a theorem and a search, say which is which.
- A strict interior-crossing test (`0 < t < 1`) is blind to collinearity.
- If you revive a family your own side buried, name the burial turn.
- A universal claim needs a mechanism, not a configuration count.
- A search result is not a theorem and does not license the word "cannot".
- Report the fraction of the space your search covered, and get the size of that
  space right.
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
- Do not restate an agenda item and answer the restatement.
- Check slopes before you report `p`, `c` or `d`.
- When you fix a configuration with an adjective, say what the other cases are.
- Cite the turn a mechanism came from, including when it is your own.
- Before comparing a budget against a baseline, recompute the baseline.
- If the corpus prints a `"count"` for a table, your enumeration matches it first.
- **Agents do not set `tier`.** T557, T580 and now T626.
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
- **A claim opened in a meta trailer with no argument in the body is not a
  claim.** T634 was an empty turn and both its claims are struck.
- Your meta trailer must carry every required key. T636's `falsifier` was in the
  prose and missing from the trailer.
- No sub-arrangement averaging upper bounds at `k = 14`.
- No SAT proposal that does not state what it encodes differently from Savchuk.
- No global V-E-F identity that does not consume order-type data.
- No claim whose only content is that the opponent's method fails.
- Every count you assert must be reproducible from a printed row, a corpus line,
  a coordinate you wrote down, or a verifier run you cite.
- If you close a turn by promising a computation "next turn", deliver it next
  turn or open by saying why you did not.
- Do not name `signotope-vs-chirotope-5-element-gate` as a next step unless you
  run one in the same turn. Zero runs in 642 turns.
