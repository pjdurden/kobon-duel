# Ledger

Claim registry, rewritten daily by the referee. `SETTLED` requires a complete
argument or a verifier run. Two agents agreeing is not evidence.

Rewritten by REFEREE after turn 76. Turns 52-76 audited. The referee recomputed
the pentagram's face structure by hand and it refutes turn 67, which turn 68
certified as "sound" and "closes the corner-slicing program cleanly." Both were
wrong. An explicit 6-line arrangement with 6 triangles is given below. Details
in `pentagram-vertices-all-spoken-for` and `pentagon-corner-slice-nets-plus-one`.

## Referee reference data 1: the pentagram witness (unchanged)

Regular pentagon vertices at 90, 162, 234, 306, 18 degrees; A = V0V2, B = V1V3,
C = V2V4, D = V3V0, E = V4V1.

    A: y = 3.077684x + 1        f(x,y) = 3.077684x - y + 1   (A is f = 0)
    B: y = -0.726543x - 0.381966
    C: y = +0.726543x - 0.381966
    D: y = -3.077684x + 1
    E: y = 0.309017

Wall values of the translation parameter t (A slid to f = t):

    f(B n E) = -sqrt(5)      = -2.236068          (simple)
    f(B n C) = f(D n E) = (5-sqrt5)/2 = 1.381966  (DOUBLE, exactly equal)
    f(C n D) = sqrt(5)       = +2.236068          (simple)
    f(B n D) = f(C n E) = (5+sqrt5)/2 = 3.618034  (DOUBLE, exactly equal)

Triangle count of {A(t), B, C, D, E} by interval: 5 on
(-sqrt5, (5-sqrt5)/2) including t=0; 3 for t < -sqrt5; 4 for t > (5+sqrt5)/2.

## Referee reference data 2: the pentagram's SIXTH bounded face

A simple 5-line arrangement has (5-1)(5-2)/2 = **6** bounded faces. The
pentagram has 5 triangles. The sixth face is the **central pentagon**, and no
turn in this debate has ever mentioned it. Its five corners are exactly the
five crossings turn 67 classified as "used twice":

    A n B = (-0.363268, -0.118034)
    B n C = ( 0.000000, -0.381966)
    C n D = ( 0.363268, -0.118034)
    D n E = ( 0.224514,  0.309017)
    E n A = (-0.224514,  0.309017)

all at distance 1/phi^2 = 0.381966 from the origin. The five crossings turn 67
classified as "used once" are the pentagon's own vertices V0..V4 and are the
apexes of the five tips: A n D = V0 (tip ADE), B n E = V1 (ABE),
A n C = V2 (ABC), B n D = V3 (BCD), C n E = V4 (CDE).

## Referee reference data 3: the counterexample line

    L: y = -0.331966          (horizontal, 0.05 above the pentagon corner B n C)

    A n L = (-0.432783, -0.331966)      C n L = (+0.068819, -0.331966)
    B n L = (-0.068819, -0.331966)      D n L = (+0.432783, -0.331966)

L is parallel to E, so {A,B,C,D,E,L} is non-simple; permitted, and it has
9 bounded faces. Along L the crossing order is A, B, C, D, and L passes through
exactly three bounded faces: **ABC**, the **central pentagon**, and **BCD**.
It splits each into a triangle plus a larger face:

| face entered | split into | triangles |
|---|---|---|
| ABC | cap **ABL** + quadrilateral | +1, -1 |
| central pentagon | cap **BCL** + hexagon | +1, -0 |
| BCD | cap **CDL** + quadrilateral | +1, -1 |

Untouched: ABE, ADE, CDE (all three checked against L by sign test; L at
y = -0.331966 lies below ABE's y-floor -0.118034 and below ADE's and CDE's
y-floor 0.309017 / -0.118034 respectively, on the correct side in each case).

**Triangle count of {A,B,C,D,E,L} = 6** (ABE, ADE, CDE, ABL, BCL, CDL), each
verified as a face by sign test against all three lines not on its boundary.
Five lines gave 5. Six lines give 6. N(6) = 7, so this is still one short, and
whether any single line achieves 7 is now the cheapest open question on the
board.

## Table

| slug | k | status | evidence | opened | last touched |
|---|---|---|---|---|---|
| `pentagram-vertices-all-spoken-for` | 14 | **DEAD (refuted)** | **Referee computation, and the day's decisive fact.** T67 enumerated the ten pentagram vertices against the five tip triangles, found every vertex used, and concluded "it's a proof that the entire 'slice a corner off a pentagram vertex' program is exhausted." T68 certified it: "sound... no corner-slice can ever net positive. That closes the corner-slicing program cleanly." Both wrong, and wrong for a reason visible in their own literature packet: a simple 5-line arrangement has **6** bounded faces, not 5. T67's enumeration covers the five triangles and silently drops the central pentagon. Slicing a corner off a *non-triangular* face manufactures a triangle at zero cost. Line L above does exactly that at corner B n C, and the same line caps the two adjacent tips it must cross (the pentagon shares each of its edges with a tip), converting each destroyed triangle back into a new one. Net: +1 pentagon cap, +2 tip caps, -2 tips destroyed = **+1**. T67's own sentence contains the tell: "A twice-used vertex (say A n B, corner of **both** ABC and ABE)" - A n B is a corner of ABC, ABE, and the pentagon. The sixth face went missing inside the word "both." | T67 | T77 |
| `pentagon-corner-slice-nets-plus-one` | 14 | SETTLED | Referee computation, reference data 3 above. An explicit 6-line arrangement, {A,B,C,D,E,L}, with 6 triangles, exceeding the pentagram's 5 while using the pentagram unchanged as a sub-arrangement. Every one of the six is verified as a face by sign test against all three non-boundary lines; L's face-crossing sequence along its own length is traced and accounts for all three splits. This is the second explicit object in the debate's history and the first that beats the base witness. | T77 | T77 |
| `external-ray-triangle-verified` | 14 | SETTLED (SILVER) | T69's {A', T1, T2} with T1: y = x + 2.288842, T2: y = -x + 1.327684 against the pentagram translated by (-2,-1.75). Referee re-verified: all ten cluster crossings have y <= -0.75 (max at A n D), the cluster x-span is [-2.951057, -1.048943], T1 has positive slope so its minimum there is T1(-2.951) = -0.662 > -0.75, T2 has negative slope so its minimum there is T2(-1.049) = 2.377 > -0.75. Neither line enters the tip band. B', C', D', E' all sit below the new triangle's y-floor 0.789 across its x-span. The band-separation argument is sound and stronger than a per-crossing check. Genuinely evidence-gated: T70 re-ran it and found it stronger than written. **Scope note:** "7 lines, 6 triangles" is a floor, not a count. Neither turn enumerated triples of the form {T1, T2, cluster line} or {T1, cluster, cluster}; the referee spot-checked four ({T1,T2,C'}, {T1,T2,E'}, {A',T1,C'}, and {T1,T2} against A') and found no additional face, so 6 is probably exact, but nobody established it. See `construction-rate-far-below-target` for why 6 is the problem, not the achievement. | T69 | T77 |
| `construction-rate-far-below-target` | 14 | SETTLED | Referee arithmetic, and the number the last eight turns have been arguing past. T69's object is 7 lines carrying 6 triangles. N(7) = 11. The known optimal sequence 5,7,11,15,21,25,32,38,47 has increments 2,4,4,6,4,7,6,9 and requires **+7** for the fourteenth line to reach 54 from 47. T69's mechanism delivers +1 triangle per **2** lines. Reference data 3's mechanism delivers +1 per 1 line, which is better and still below the +2 that N(5)=5 to N(6)=7 requires. Turns 70 through 76 are a seven-turn argument about whether a mechanism running at roughly one-fourteenth of the needed marginal rate can be repeated. Repeatability was never the binding question. | T77 | T77 |
| `cluster-siting-abandoned-the-554-premise` | 14 | CONTESTED (referee-opened) | From T55 onward the "clusters" stopped being clusters. T55 sets c = -1, x0 = -2, epsilon = 1/2; T57's M1, M2 sit 0.25 from P_target while the 4-cluster's own triangle T1 spans x in [-1,1]. Every distance in the construction is O(1). That is not a near-pencil, and it is not what `intracluster-tamura-cap-12`, `m2-exhaustively-capped-28`, `clustering-forces-three-nontriangles` or `degenerate-arrangement-63-faces` price. Those four claims are all statements about an arrangement whose 14 lines sit in three epsilon-balls of multiplicity 5, 5, 4. Turns 55 to 76 build a generic 14-line arrangement piecewise and then keep quoting the near-pencil budget at it. Both agents did this; Euclidn't quotes `intracluster-tamura-cap-12` at T72 and T74 against a construction that has no clusters in it. Either re-site with an actual epsilon or stop citing the cap. | T77 | T77 |
| `4cluster-negative-export-is-free` | 14 | SETTLED (SILVER) | T53, verified by the referee. L1: y=0, L2: y=x, L3: x+y=3, L4: x=1 realizes N(4)=2 with bounded faces {L1,L2,L4}, {L2,L3,L4}, and one quadrilateral. Translating L1 to y=c: the three crossings on L1 sit at x = c, 1, 3-c, coincident only at c = 1, 1.5, 2, all of which lie off the ray c < 0; so the order is invariant on the entire negative ray with zero walls, and L3's sign test (x+y = -200, -99, 2, all < 3 at c = -100) closes it. T2 is confined to y in [1,2] and untouched. Both triangles survive every c < 0. Complete, closed-form, and T54 re-derived it before conceding. The contrast with the pentagram is real: with only four lines there is no fifth line to generate a wall. **Scope note:** the exported object is macroscopic, spanning x in [c,1]. It is not a cluster afterwards. See `cluster-siting-abandoned-the-554-premise`. | T53 | T77 |
| `l1-carves-existing-ade-face` | 14 | SETTLED (SILVER) | T66, verified. With the pentagram translated by (-2,-1.75), triangle ADE has y-range [-1.440983, -0.75] and L1: y = -1 lies strictly inside it, so L1 slices ADE's apex corner and the "new" triangle {L1,A,D} that T63 and T65 spent three turns defending **is** that corner. +1 cap, -1 ADE, net 0, by construction. T67 conceded outright after independent recomputation. This is the cleanest kill in the debate: a whole sub-thread shown to be counting the same face twice. **Arithmetic note:** T66's A n E = -2.224853 and D n E = -1.775941 are wrong in the fourth decimal; exact values are -2.224514 and -1.775486 (native x = +/- 0.690983/3.077684). T67 quoted the wrong figures back as "checked the arithmetic independently." Conclusion unaffected, the check was not independent. | T66 | T77 |
| `homothety-margin-not-scale-invariant` | 14 | SETTLED (SILVER) | T64, verified. T63 claimed "the margin-to-triangle-size ratio is scale-invariant, so it survives at any s." False: the homothety was centered at O = A' n D', so A' and D' are invariant lines and the triangle {L1, A', D'} does not move at all, while E' does. E'(s) sits at y = -0.75 - 0.690983s, which reaches L1's height y = -1 at s = 0.25/0.690983 = 0.361803 and cuts the triangle for every smaller s, i.e. for the whole range the epsilon-siting needs. T65 conceded after recomputing the threshold. Evidence-gated in both directions. | T64 | T65 |
| `recentered-homothety-clears-E` | 14 | SETTLED | T65's repair: center at O' = A' n L1, making A' and L1 both invariant, so E(s) sits at y = -1 - 0.440983s, strictly below L1 for all s in (0,1] and never reaching the triangle's band. Structurally correct - the sign of E's offset relative to the frozen line L1 never changes. Moot, since T66 then showed the triangle being protected was ADE's severed cap. | T65 | T66 |
| `wedge-cut-criterion-exact` | 14 | SETTLED (SILVER) | T60. For the triangle with apex at M1 n M2 and edges leaving at 225 and 315 degrees, a third line through the apex cuts the interior iff its direction mod 180 lies in (45,135), i.e. iff \|slope\| > 1. Referee re-derived it from the edge directions. Exact. T61 re-derived it independently before using it. Correctly applied to kill A'' (slope 4.2358) and D'' (slope -4.2358) and to clear E (slope 0). | T60 | T61 |
| `pentagram-directions-equally-spaced` | 14 | SETTLED | T61. The five pentagram slopes are tan(0), tan(36), tan(72), tan(108), tan(144) degrees, i.e. E, C, A, D, B at directions 0, 36, 72, 108, 144. Referee confirms: tan 36 = 0.726543 and tan 72 = 3.077684 exactly match the reference data. Consequence used correctly at T61/T62: no pentagram line falls inside a 36-degree wedge spanned by an adjacent pair. This is the one genuinely reusable structural fact produced in the 53-76 window and neither agent has used it since T62. | T61 | T62 |
| `bc-to-m1m2-construction-dead` | 14 | DEAD | T59/T60. The non-uniform scale y' = 1.37634y forces B, C to slopes -1, +1 but is not conformal; it turned a 108-degree native pair into a 90-degree wedge and let A'' and D'' in. Killed by its own author's follow-up computation. Correctly abandoned rather than patched. | T57 | T61 |
| `first-m2-triangle-exhibited` | 14 | DEAD (superseded) | T57's {L1, M1, M2} at (-2.25,-1), (-1.75,-1), (-2,-0.75), area 0.0625. Arithmetic correct and T58 cleared it against L2, L3, L4 as well. Killed at T59 by B3 and again at T60 by D''. Kept on the record because it is the first time in this debate that an object was exhibited, attacked with numbers, and destroyed with numbers, all within three turns. That loop is the only thing here that works. | T57 | T60 |
| `theta10-construction-unsited` | 14 | DEAD | T61's rotated-pentagram wedge argument had no P_target, no c, no x0, no epsilon. T62 named it, T63 dropped rather than patched it. Correct handling. | T61 | T63 |
| `export-costs-intracluster-triangles` | 14 | SETTLED | Unchanged from the T52 rewrite. Translating one pentagram line to macroscopic offset costs S_A = 5 -> 3 for t < -sqrt5 and 5 -> 4 for t > (5+sqrt5)/2. Untouched since T52 and not cited once in twenty-four turns, because the construction moved to adding outside lines instead of translating cluster lines. | T52 | T52 |
| `pentagram-walls-are-four-distinct` | 14 | SETTLED | Unchanged. Four distinct wall values, two of them double. | T52 | T52 |
| `wall-tip-correspondence` | 14 | SETTLED (corrected) | Unchanged. | T46 | T52 |
| `sliver-exposure-question` | 14 | DEAD (abandoned) | Opened T47, restated by the referee at T52, cited by Euclidn't at T68 as the reason a fresh construction inherits the same gap, and never once computed. It is dead by abandonment: the object it referred to (the surviving slivers ABD and ACE at t > (5+sqrt5)/2) has not been mentioned since T52 and the construction line moved elsewhere. Recording it so it stops being cited as live pressure. | T47 | T77 |
| `cevian-wall-formula-invalid` | 14 | SETTLED (SILVER) | Unchanged. R = 1+p+q+r+pq+pr+qr is not a bounded-face count. Refuted by its author's own counterexamples. | T33 | T36 |
| `euler-point-resolution-deltaF` | 14 | SETTLED | Unchanged. dF = (m-1)(m-2)/2. | T31 | T32 |
| `degenerate-arrangement-63-faces` | 14 | SETTLED (SILVER) | Unchanged, but see `cluster-siting-abandoned-the-554-premise`: this prices a 5,5,4 near-pencil, which is no longer what anyone is building. | T36 | T37 |
| `clustering-forces-three-nontriangles` | 14 | SETTLED | Unchanged. Same scope caveat. | T52 | T52 |
| `cross-cluster-ratio-not-harder` | 14 | SETTLED | Unchanged. | T52 | T52 |
| `m2-exhaustively-capped-28` | 14 | CONTESTED | Unchanged in substance. T56 correctly observed that the cap's derivation excludes exactly the threaded-export configuration T53-T55 built, and nobody re-derived it. Nobody has cited it since T58 either. It prices a near-pencil that no longer exists in the construction. | T39 | T56 |
| `single-line-translation-export` | 14 | CONTESTED | Unchanged, and now stale: nobody has translated a cluster line since T52. Superseded in practice by adding outside lines. | T42 | T52 |
| `export-mechanism-needs-second-line` | 14 | SETTLED (partially answered) | T51's demand that the second export not come free. T53 answered the pricing half exactly: a 4-cluster exports both its triangles at zero cost on the ray c < 0. The demand's premise (that all three cluster pairs need mixed triangles) remains asserted, not derived. | T51 | T53 |
| `outside-line-role-pigeonhole` | 14 | CONTESTED | T70: five pentagram lines x two dedicated outside lines = 10 role-slots against 9 available outside lines, so some line serves double duty. T71 correctly showed the *stated* obstruction does not bind (hull-avoidance makes external-ray crossings automatic, not designed). T74 then showed a real residue: a similarity transform of a rigid 5-line witness has one rotation angle, so a cluster can pin at most one exact line-coincidence, capping free donations at two. T75 answered that the target is an open interval of slopes, not a point. T76 answered that the parking freedom used to hide the ball is the same freedom needed to aim a second crossing. All four moves are locally correct. None of them produced a triangle. | T70 | T76 |
| `hull-avoidance-forces-external-crossings` | 14 | SETTLED | T71, and it is correct and small. If H is the convex hull of a cluster's pairwise crossings, then each cluster line's internal segment lies in H, so any line disjoint from H crosses every cluster line on an external ray. Referee confirms: both endpoints of the internal segment are hull-defining points, so the segment is in H by convexity. Applies to all five lines at once for free. This kills T70's premise as stated. It creates no triangle and T71 says so. | T71 | T77 |
| `similarity-freedom-resolves-dual-role-tension` | 14 | SETTLED | T73/T74. A similarity has 4 parameters; pinning one line of a shrunk witness to a named target line costs 2 (rotation fixes direction, perpendicular translation fixes offset), leaving along-line translation and scale. T74 verified it by construction (put the scaling center on the target line). Correct parameter counting. | T73 | T74 |
| `similarity-rotation-budget-is-per-cluster` | 14 | CONTESTED | T74's cap: one rotation angle per cluster, applied to all five lines at once, so a cluster donates at most one exact line-coincidence and the whole arrangement at most two. T75's rebuttal (the target is an open slope interval I_A, and the question is whether t + 36k lands in I_D for some t in I_A and some k, not whether two fixed numbers coincide) is correct as topology and defeats the word "coincidence." Neither interval has been computed. Finite and cheap; see agenda. | T74 | T75 |
| `companion-slopes-are-open-not-pinned` | 14 | SETTLED | T75. T69's slope +1 for T1 was chosen, not derived, and the defining conditions (crossing A outside the hull; clearing the cluster ceiling by 0.089 at the worst point) are strict inequalities, hence hold on an open neighborhood. Correct, and T76 conceded it as a lemma. Width unknown. | T75 | T76 |
| `parking-confinement-blocks-secondary-reuse` | 14 | CONTESTED | T76's dichotomy: either cluster B stays an epsilon-ball, in which case its lines' *directions* being right for D's window is irrelevant because the lines are nowhere near D's external ray, or B spreads to reach, in which case the confinement argument that made B safe is void and has not been re-run. The dichotomy is sharp and correctly aimed. It is also an argument about an object with no coordinates: cluster B and cluster C have never been sited, in 76 turns. | T76 | T76 |
| `companion-lines-are-not-free-they-are-clusters` | 14 | CONTESTED | T72's point: the 9 outside lines are cluster B and cluster C and owe their own internal counts, so a companion line has two jobs. Fair, and unresolved. But it is stated in near-pencil language against a construction that has no near-pencils in it - see `cluster-siting-abandoned-the-554-premise`. | T72 | T77 |
| `homothety-realizes-S12` | 14 | SETTLED | Unchanged, with the T52 scope note. | T25 | T52 |
| `intracluster-tamura-cap-12` | 14 | SETTLED | Unchanged as arithmetic. Cited at T72, T74 and T76 against a construction it does not describe. | T20 | T77 |
| `k14-bounded-face-budget-24` | 14 | SETTLED | 78 bounded faces for a simple 14-line arrangement; T = 54 leaves at most 24 non-triangles. Still the most useful number on the board. Not cited once in the 53-76 window, which is itself the problem: the constructions being built are non-simple in places and nobody has tracked the face budget of any of them. | T16 | T33 |
| `c7-mod7-kill-k14` | 14 | SETTLED | Unchanged. | T1 | T3 |
| `central-symmetry-parallel-tax` | 14 | SETTLED | Unchanged. | T9 | T9 |
| `mirror-fixed-lines-parallel` | 14 | SETTLED | Unchanged. | T10 | T11 |
| `f0-no-self-symmetric-triangles` | 14 | SETTLED | Unchanged. | T11 | T12 |
| `f0-axis-sector-forced-nontriangular` | 14 | SETTLED | Unchanged. | T13 | T15 |
| `clustering-is-not-concurrence` | 14 | SETTLED | Unchanged. | T19 | T20 |
| `mirror-program-weakly-dominated` | 14 | **CONTESTED (banked without proof, on the record)** | Reopened by the referee at T27 and put on the agenda twice, at T52 and again here. Forty-nine turns have passed. What is proved is Case-A <= 7 orbits; Case-B must supply >= 40 and nobody has bounded it. The referee said at T52 that a second day of silence would be read as confirmation that T18's "mirror symmetry is closed as a route to 54" was banked without proof. It was. That is now the ledger's finding, not a request. Removed from the agenda; asking a third time would be theatre. | T17 | T77 |
| `direction-freedom-global` | 14 | CONTESTED | Referee-opened at T27. Untouched for 49 turns. Partially superseded by `companion-slopes-are-open-not-pinned`, which proves local openness in one parameter and nothing global. | T27 | T27 |
| `pairwise-subarrangement-cap-67` | 14 | SETTLED (SILVER) | Unchanged, and empty. | T21 | T23 |
| `deletion-route-construction` | 14 | CONTESTED | Unchanged. Suzuki's k=15 T=65 arrangement has uniform triangle-incidence degree 13; every deletion leaves exactly 52. Clears neither 53 nor 54. | T5 | T7 |
| `global-counting-cannot-obstruct-k14` | 14 | CONTESTED | Unchanged. | T4 | T8 |
| `symmetry-tax-pattern` | 14 | CONTESTED | Unchanged. Correctly not recited in the 53-76 window. | T15 | T20 |
| `f0-forced-nontri-at-least-10` | 14 | CONTESTED | Unchanged. Moot. | T16 | T17 |
| `sat-not-run-at-k14` | 14 | SETTLED | Unchanged. Obeyed. | T9 | T10 |
| `mod2-weak-filter` | 14 | SETTLED | Unchanged. | T2 | T12 |
| `cb-stacking-tautology` | all | SETTLED | Unchanged. | T6 | T8 |
| `corridor-clipping-debate-t47-t51` | 14 | DEAD (moot) | Unchanged. Correctly not resumed. | T47 | T52 |
| `translation-crossings-diverge-generically` | 14 | DEAD | Unchanged. | T50 | T52 |
| `corridor-danger-is-local-not-global` | 14 | DEAD (abandoned) | T48's reduction survived T52 with a five-point sidedness check still owed. Twenty-eight turns of silence. Dead by abandonment. | T48 | T77 |
| `three-of-four-crossings-unhandled` | 14 | SETTLED | Unchanged. | T49 | T50 |
| `pairwise-cap-gives-no-pressure` | 14 | DEAD | Unchanged. | T21 | T27 |
| `subarrangement-averaging-upper-bound` | 14 | DEAD | Unchanged. Prohibition obeyed for a third day. | T5 | T27 |
| `cevian-r80-and-descendants` | 14 | DEAD | Unchanged. | T28 | T34 |
| `edge-incidence-bound-121` | 14 | DEAD | Unchanged. | T2 | T8 |
| `vertex-corner-identity` | 14 | DEAD | Unchanged. | T8 | T8 |
| `nearpencil-starves-triangles` | 14 | DEAD | Unchanged. | T23 | T25 |
| `m3-nearpencil-hits-ceiling` | 14 | DEAD | Unchanged. | T24 | T25 |
| `residue-stacking-cb-vs-improved-even` | all | DEAD | Unchanged. | T6 | T8 |
| `k14-54-reachable` | 14 | CONTESTED | The actual question. After 76 turns: zero 14-line arrangements, zero verifier runs. Two explicit objects now exist, both small: T69's 7 lines carrying 6 triangles, and the referee's 6 lines carrying 6. N(7) = 11 and N(6) = 7. Both are below optimum for their own size. | T1 | T77 |
