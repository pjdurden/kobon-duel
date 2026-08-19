# Agenda

Rewritten daily by the referee. Written after turn 26.

Standing observation before the items: in 26 turns neither agent has written
down a single line of a single arrangement. No coordinates, no angles, no
offsets, no face-by-face count of anything. Every turn has been a bound, a
residue, or a critique of a bound or a residue. Three of the five items below
demand an object with numbers in it, and the referee will not credit another
structural property in place of one.

## 1. PythagorAss: the exact-pencil limit count for the 5,5,4 family

Owed since turn 19, restated in sharper form because "count the mixed triangles"
has now been deferred five turns running.

Work in the limit where each cluster is an *exact* pencil at P_A, P_B, P_C
(sizes 5, 5, 4) and then perturb. In that limit an M3 triangle is a triple
(a, b, c), one line per cluster, with vertices a∩b, a∩c, b∩c. State and apply the
survival criterion: for the triangle to be elementary after perturbation, no
other cluster line may cut it, and the first thing to check is whether P_A lies
inside or outside the segment [a∩b, a∩c] on line a, and likewise for P_B, P_C.
If P_A lies inside, every other A-line passes through that segment and destroys
the triangle.

The named object: a count of how many of the 100 candidate M3 triples
(5·5·4) survive, and how many of the 240 candidate M2 triples
(C(5,2)·5 + C(5,2)·4 + C(5,2)·5 + C(5,2)·4 + C(4,2)·5 + C(4,2)·4 = 50+40+50+40+30+30)
survive. Target is 42. A number, not a mechanism.

## 2. Euclidn't: bound Case-B in the f=0 mirror family, or withdraw turn 18

`mirror-program-weakly-dominated` is back to CONTESTED. Turn 17 conceded the
mirror program at every p on an expectation argument and turn 18 banked it
without reservation. What is proved is Case-A ≤ 7 orbits; what is needed to
close the family is a cap on Case-B below 40 triangles. Either produce that cap
for k=14, p=7, or state on the record that "mirror symmetry is closed as a route
to 54" was accepted without proof and stop citing it in tax-pattern tallies.

## 3. Either side: is every 5-tuple of directions S-maximal?

`direction-freedom-global`, the only live remnant of turn 26. Local direction
freedom is settled by openness of the combinatorial type, which refutes turn
26's three-scalars claim. The global question is not settled and is small enough
to finish in one turn:

> Given 5 pairwise-distinct directions in the plane, arbitrary, can offsets
> always be chosen so the resulting 5-line arrangement has 5 triangles?

Produce either a proof for all 5-tuples, or one explicit 5-tuple of angles with
an argument that no offsets reach 5. Note that PGL(2,R) is only 3-transitive on
the line at infinity, so 5 directions carry real moduli and the answer is not
free. This decides whether S = 12 genuinely costs the near-pencil family
anything in aiming.

## 4. Killed: sub-arrangement averaging as an upper-bound tool

Do not propose another recursive Tamura or delete-a-line bound at k=14. Averaging
any s-subset bound gives T ≤ C(14,s)·N(s)/C(11,s−3), and the best case is s=13
at 14·47/11 = 59.8, i.e. T ≤ 59. s=12 gives 62.9, s=11 gives 70.6, s=10 gives
75.8. Every one is above 54. The whole family of bounds turns 20, 21 and 22 were
exploring cannot beat the bound that is already published. Turn 22's correction
of 26 to 25 was right and changed nothing that mattered.

The one thing in this area still worth producing is the per-line
triangle-incidence degree sequence of a known k=15, T=65 optimum, which has been
owed since turn 5 and would settle `deletion-route-construction` as a
*construction* in one line of arithmetic.

## 5. Killed: global V-E-F counting, and the symmetry-tax tally

Euclidn't has conceded twice (turns 6, 8) that Euler-relation counting cannot
produce an obstruction at k=14 without order-type input. No further edge-split,
corner-count, or face-degree identity will be credited unless it consumes actual
order-type data.

Also: the tax tally in turns 15, 18 and 20 counts five taxes, of which three
(C_7 arithmetic, central symmetry's C(f,2), the f>0 mirror restriction) are taxes
on *particular symmetry groups*. A 54-triangle arrangement, if one exists, is
almost certainly asymmetric, and nothing in the tally touches asymmetric
arrangements. Stop reciting the tally as evidence about N(14). Tax an asymmetric
family or drop the argument.
