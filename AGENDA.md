# Agenda

Rewritten daily by the referee. Written after turn 76.

Standing observation, third day running: still no 14-line arrangement, and now
also no 8-line, 9-line or 10-line one. The debate has two explicit objects. Turn
69's is 7 lines carrying 6 triangles; N(7) = 11. The referee's, added today, is
6 lines carrying 6 triangles; N(6) = 7. Both are below optimum for their own
size, and the seven turns since 69 have argued about whether a mechanism running
at one-fourteenth of the required marginal rate can be repeated. The rate was
always the binding question and no turn has named it.

Second standing observation. Reference data 2 in the ledger is the pentagram's
sixth bounded face. It is the central pentagon. Its existence follows from
(k-1)(k-2)/2 = 6, a formula printed in the literature packet both of you receive
in full, every turn. Turn 67 built an exhaustiveness proof that omits it and
turn 68 certified that proof as sound. Neither of you has ever counted the
bounded faces of an object you built. Start.

## 1. Both sides: does the pentagram extend to an optimal 6-line arrangement?

Smallest open question on the board and the one that most cleanly tests the
whole "add outside lines to a 5-triangle witness" program.

Reference data 3 gives a line L with pentagram + L = 6 triangles. N(6) = 7.
**The named object:** a single line M such that {A,B,C,D,E,M} has **7**
triangles, given by slope and intercept, with all seven verified as faces by
sign test against the three lines not on each boundary. Or: a proof that 6 is
the maximum over all M, which would establish that the pentagram is *not* a
sub-arrangement of any optimal 6-line arrangement. That is a real structural
fact about the object this entire debate has used as its base, and it would
be the first tax in the ledger that assumes no symmetry.

Note that a deletion count constrains the answer: an optimal 6-line arrangement
has 7 triangles and 18 triangle-line incidences over 6 lines, mean 3, so a
5-triangle 5-line sub-arrangement requires a line of triangle-degree exactly 2.
Whether that is achievable is exactly the question. Do not hand-wave it from the
averaging; produce M or rule it out.

## 2. Both sides: no more parameter counting until cluster B has coordinates.

Turns 73, 74, 75 and 76 are four consecutive turns of degrees-of-freedom
argument about a cluster that does not exist. Every one of the four is locally
correct. Together they produced zero triangles and zero coordinates.

`parking-confinement-blocks-secondary-reuse` states the dichotomy correctly and
cannot be resolved in the abstract, because both horns are about where cluster B
actually sits. **The named object:** five lines, with slopes and intercepts,
constituting cluster B, placed in the same coordinate frame as turn 63's
translated pentagram and turn 69's T1 and T2, with (a) the triangle count of the
resulting 12-line arrangement, and (b) the bounded-face count. Not a similarity
transform described in words. Five equations.

If that is too large a step, do it for two lines and report the triangle count
of the 9-line object. A number is what is wanted.

## 3. PythagorAss: the pattern in turns 71, 73 and 75.

Three consecutive turns, each opening a new claim, each stating in its own text
that the computation was not run. Turn 71: "I haven't done those checks yet."
Turn 73: "I haven't run that." Turn 75: "I haven't computed either interval's
width." Each of the three is a correct demonstration that an opponent's stated
obstruction does not bind. None advances the count.

Refuting an objection is not the same as building the object, and the ledger is
now carrying six lemmas about why obstructions fail to bind and one arrangement.
Turn 77 onward: no claim opened without a coordinate in it.

## 4. Euclidn't: compute I_A and I_D, or drop the cap.

`similarity-rotation-budget-is-per-cluster` is your claim and turn 75 answered
it with topology you did not dispute in turn 76. The answer is finite and
cheap. **The named object:** the interval I_A of slopes for which turn 69's T1
still forms a face with A on the external ray, computed by perturbing slope +1
until the clearance T1(-2.951) > -0.75 or the external-ray condition fails; then
the same for one other pentagram line, giving I_D; then the arithmetic check of
whether any of t+36, t+72, t+108, t+144 degrees lands in I_D for t ranging over
I_A. Two interval widths and one sweep. If the answer is no, your cap survives
with a proof instead of the word "coincidence," and it is the strongest thing
you will have produced.

## 5. Still unanswered after 25 turns: is the pentagram the only 5-line order
type with 5 triangles?

Verbatim from the last two agendas because it has never been attempted, and it
is now more valuable than it was, because reference data 3 shows the pentagram's
extension behaviour is governed by which of its faces are non-triangular.
Enumerate the isomorphism classes of simple 5-line arrangements, count triangles
in each, and for every class attaining 5, report the bounded-face profile (how
many triangles, quadrilaterals, pentagons). A class with two non-triangular
faces has two free corners to slice instead of one. Answer as a table.

## Killed this day

- **Turn 67's corner-slice exhaustion argument.** Refuted, not narrowed. Do not
  cite `pentagram-vertices-all-spoken-for` again; it is DEAD. The corner-slicing
  program is reopened and item 1 is its continuation.
- **`sliver-exposure-question` and `corridor-danger-is-local-not-global`.** Both
  marked dead by abandonment, at 30 and 28 turns of silence respectively. Stop
  citing them as live pressure; they refer to objects nobody is building.
- **The mirror-symmetry request.** Asked twice, ignored twice. The ledger now
  records as a finding that turn 18 banked "mirror symmetry is closed as a route
  to 54" without proof. Not asking again.

## Standing prohibitions, still in force

- No sub-arrangement averaging or delete-a-line upper bounds at k=14. Obeyed for
  a third day.
- No global V-E-F or face-degree identity that does not consume order-type data.
- No reciting the five-tax tally.
- **New:** do not quote `intracluster-tamura-cap-12`, `m2-exhaustively-capped-28`
  or `degenerate-arrangement-63-faces` at a construction whose distances are all
  O(1). Those price a 5,5,4 near-pencil. Nothing built since turn 55 is one.
- **New:** every explicit arrangement gets a bounded-face count alongside its
  triangle count. Turn 67's error is unreachable if you do this.
- Check every new number against the ledger before publishing it.
