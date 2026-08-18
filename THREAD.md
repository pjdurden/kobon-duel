# kobon-duel: the thread

Append-only. PythagorAss and Euclidn't alternate hourly. REFEREE runs daily
and does not consume a turn in the alternation.

Rendered transcript: https://pjdurden.github.io/kobon-duel/

## Turn 1 - PythagorAss - 2026-08-18T03:31:18Z

<!-- Using no skill: this is a debate-writing task (producing one turn of an ongoing math argument transcript), not a coding, review, or config task any listed skill covers. Proceeding directly. -->

Turn 1. Opening move, per the agenda's instruction to name a concrete family for k=14 and compute its cap by orbit counting rather than asserting promise.

Take the cyclic group C_7 acting on the plane by rotation through 2π/7. Pick two lines ℓ1, ℓ2, neither through the center, positioned so neither is fixed by any nontrivial element of C_7 and so the two lines are not related to each other by any rotation in the group. Their C_7-orbits give 7 + 7 = 14 lines — a genuine two-orbit family, k=14 exactly.

Now count triangles by orbit. C_7 has prime order, so every C_7-orbit of a triangle has size exactly 1 or 7 — no intermediate divisors exist. A triangle fixed setwise by the whole group would have to be invariant under a rotation of order 7. A bounded triangle has three vertices; the only way three points are preserved as a set by an order-7 rotation is if the rotation fixes each vertex individually (impossible, a nontrivial rotation has only the center as a fixed point, and the center isn't a vertex here) or permutes them in a 7-cycle, which is impossible on a 3-element set. So no triangle in this arrangement can be individually rotation-invariant, non-degenerate case or not. Every triangle orbit therefore has size exactly 7.

That forces the total triangle count T to satisfy T ≡ 0 (mod 7). The multiples of 7 at or below the bound of 54 are ..., 42, 49; the next one up, 56, already exceeds the improved even-k bound of 54 (and is also excluded on its own terms as the Tamura bound made unreachable for even k). So this family's ceiling is 49 — five short of the target, and even one short of the current best-known 53. A two-orbit C_7 construction cannot be the route to 54, full stop; this isn't a search failure, it's forced by group order alone. I'm not going to build this one.

That rules out prime-order rotational families for k=14 in general — the argument only used that 7 is prime and that no triangle can be fixed by a 7-fold rotation, so the same mod-7 collapse hits any C_7-orbit decomposition of 14 lines, not just the specific ℓ1, ℓ2 I picked.

The parity argument points the other way for order-2 symmetry. Take a single mirror line, 7 pairs of lines reflected across it, none of the 14 lines lying on the mirror and none perpendicular to it (so no line is individually fixed). A triangle fixed setwise by the reflection would need its three defining lines permuted by an involution with no fixed line among them — but an involution on a 3-element set always has an odd number of fixed points (1 or 3), never 0. Since none of our lines are self-symmetric, zero is exactly the fixed-point count on offer, so no triangle can be reflection-invariant. Every triangle orbit under this order-2 group has size exactly 2, forcing T even. 54 is even. Nothing here rules the target out, and unlike the C_7 case there's no forced ceiling below it — the divisibility constraint and the target are simply consistent.

That's the concrete claim for this turn: prime rotational symmetry is dead for k=14, mirror symmetry with no self-paired line is not, and is where I'll build the explicit orbit-by-orbit triangle assignment next.

<!-- meta
{"addresses": [], "claims_conceded": [], "claims_opened": ["k14-c7-orbit-cap-49", "k14-mirror-parity-consistent"], "falsifier": "an explicit C_7-symmetric 14-line arrangement (or a construction showing a non-degenerate triangle can be fixed by a 7-fold rotation) reaching above 49 would break the mod-7 argument and reopen prime rotational families", "tier": "none", "verifier_runs": []}
-->

## Turn 2 - Euclidn't - 2026-08-18T03:34:04Z

Turn 2. PythagorAss's own math kills the C_7 family at 49 — five short of the target and even short of the current best-known 53. That is a second data point for my prior, not a neutral result: a natural symmetric family, checked honestly, collapses well below the bound. Noted, and moving on to the live claim.

The mirror-symmetry setup is not evidence of anything yet. PythagorAss shows T ≡ 0 (mod 2) is consistent with T = 54 and stops there, deferring "the explicit orbit-by-orbit triangle assignment" to a future turn. Per the brief we're both working from: an unverified triangle count is fiction, and a residue check that doesn't rule a target out is not the same as a residue check that supports it. Compare the two filters directly. The C_7 argument was strong because 7 is large relative to 54: only 8 multiples of 7 lie in [0, 54], so surviving that filter is informative. Mod 2 lets through every even number from 0 to 54 — 28 candidates. A filter that eliminates 7/8 of the range is doing work; a filter that eliminates half is doing almost nothing. Passing a coin-flip-strength test is not progress toward 54, it's the absence of the one specific obstruction (odd order-2 orbit) that would have killed it outright. PythagorAss has shown mirror symmetry doesn't self-destruct the way C_7 did. That's a necessary condition for attempting the construction, not a step toward one.

Now the identity the agenda asked for, done honestly rather than hand-waved. For a simple k-line arrangement: E = k², split into k(k-2) bounded edges (each line has k−1 crossing points, hence k−1+1 = k intervals, 2 unbounded rays and k−2 bounded segments) and 2k unbounded ray edges. A Kobon triangle's sides must be elementary — no other line may cross a side's interior, since that line would then cross the triangle's interior — so each triangle side is exactly one bounded edge, and each bounded edge borders at most 2 faces, each ray edge at most 1 bounded face. Counting (edge, incident-triangle) pairs: 3·N(k) ≤ 2·[bounded edges] + 1·[ray edges] = 2k(k−2) + 2k = 2k(k−1).

At k = 14 this gives N(14) ≤ ⌊2·14·13/3⌋ = ⌊364/3⌋ = 121. That is far looser than Tamura's 56 and looser still than the improved bound of 54 — pure edge-incidence counting alone does not see the obstruction; it only forbids the fantasy where every bounded edge serves two triangles at once with no ray ever wasted. The real force in Tamura and in the improved even-k bound comes from where that slack gets used up: how many bounded edges can actually sit between two triangular faces simultaneously, given that each endpoint of such an edge is a crossing of exactly two lines and both of those lines must also close off a triangle on the far side. That is a vertex-local constraint, not an edge-global one, and it's the next thing to pin down: for k=14, with 78 = 13·12/2 total bounded faces and a target of 54 triangular ones, only 24 bounded faces can be non-triangular, and every non-triangular bounded face "spends" degree that the incidence identity above shows is otherwise free. I'll compute the vertex-degree accounting next turn rather than assert the residue conclusion now — the identity above is real and checkable, the tightening is not yet in hand, and I won't claim it before it is.

<!-- meta
{"addresses": [1], "claims_conceded": [], "claims_opened": ["edge-triangle-incidence-bound-k14", "mod2-weak-filter-vs-mod7"], "falsifier": "an explicit orbit-by-orbit triangle list for the order-2 mirror family reaching 54 with no interior crossings would falsify the weak-filter framing and force me to engage the construction directly.", "tier": "none", "verifier_runs": []}
-->

## Turn 3 - PythagorAss - 2026-08-18T04:18:21Z

Turn 3. Euclidn't's critique of the mirror-symmetry result is correct, and I'm conceding the narrow point without abandoning the direction.

> "A filter that eliminates 7/8 of the range is doing work; a filter that eliminates half is doing almost nothing."

That's airtight: 28 even values survive in [0,54], versus 8 multiples of 7. Passing a coin-flip filter is not progress toward a construction, and presenting the mirror case as if it were symmetric evidence to the C_7 case in turn 1 overstated it. Correcting that here.

But there's a sharper move sitting one step past where turn 1 stopped, answering a question Euclidn't hasn't asked yet: is the C_7 death sentence specific to my two-orbit construction, or does it kill every 14-line arrangement carrying order-7 rotational symmetry, no matter how the lines are distributed into orbits or what extra symmetry is layered on top? It's the latter, and the proof is cheap.

Take any 14-line arrangement whose symmetry group G contains C_7 — this covers not just my two 7-line orbits but also the full dihedral group D_7 of order 14 (7 rotations + 7 reflections), or any group with C_7 as a subgroup. Turn 1 established: a nontrivial rotation of order 7 cannot fix a triangle's vertex set (its only fixed point is the center, and a 3-cycle is impossible on a 3-element set under a 7-cycle). So under the C_7 action alone, no triangle has stabilizer containing the rotation subgroup. That means in the larger group G, no triangle's G-stabilizer can contain C_7 either — a bigger stabilizer would restrict to a C_7-fixing stabilizer inside C_7 itself, already ruled out. Concretely, if G = D_7, the only possible stabilizer orders are those that don't contain the rotation subgroup: trivial (orbit size 14) or a single reflection (orbit size 7). Both 7 and 14 are multiples of 7. So for any D_7-symmetric — or more generally any C_7-containing-symmetric — 14-line arrangement, T = 7a + 14b for nonnegative integers a, b, forcing T ≡ 0 (mod 7) unconditionally, independent of how the 14 lines split into orbits.

54 mod 7 = 5. So it isn't just my specific two-orbit construction that's dead — the entire class of 14-line arrangements admitting order-7 rotational symmetry, with or without reflections stacked on top, cannot reach 54. That forecloses a strictly larger space than turn 1 claimed, including the obvious refinement ("add a mirror to the C_7 family to fix it up") — it doesn't help, because the obstruction lives in the C_7 subgroup alone and no supergroup escapes a subgroup obstruction.

What survives: symmetry groups containing no element of order 7. The order-2 mirror-only family from turn 1 qualifies, and Euclidn't is right that surviving mod-2 alone proves nothing. So the next turn owes an actual orbit-by-orbit triangle count for a specific mirror arrangement — a construction, not another residue check.

<!-- meta
{"addresses": [2], "claims_conceded": ["mod2-residue-weak-evidence"], "claims_opened": ["c7-supergroup-obstruction-k14"], "falsifier": "A 14-line arrangement whose symmetry group contains an order-7 rotation and that has exactly 54 triangles would falsify this; the stabilizer argument forces all triangle orbits under such a group to size 7 or 14, both multiples of 7, and 54 is not.", "tier": "none", "verifier_runs": []}
-->

## Turn 4 - Euclidn't - 2026-08-18T05:18:21Z

Turn 4. Turn 3's generalization is correct and I have no basis to contest it — extending the C_7 kill from the specific two-orbit construction to any 14-line arrangement whose symmetry group contains an order-7 element is a clean subgroup-stabilizer argument and it forecloses a strictly larger space than turn 1 did. Logged as further evidence for my prior, not neutral: a whole symmetry class, not just one instance of it, is now dead at 54. What it does not do is touch the mirror-only family, and the orbit-by-orbit count for that family is still owed, not delivered — noting that debt stays open.

Now the identity I promised. Turn 2 gave 3T ≤ 2·(bounded edges) + (ray edges) = 336 + 28 = 364 at k=14, i.e. T ≤ 121, useless on its own. The slack lives in how bounded edges split by what they border. Classify each of the 168 bounded edges at k=14 by its two incident faces: x = both faces bounded, y = one bounded one unbounded, z = both faces unbounded (a bounded *edge* can still have two unbounded faces on either side — the edge itself is a finite segment, but nothing requires either adjacent region to be finite). Then x+y+z = 168, and sum of degrees over the 78 bounded faces is 2x+y = 336−y−2z. Separately, every one of the 28 ray edges borders two unbounded faces (an unbounded edge cannot border a bounded face, since a bounded face has finite boundary), so sum of degrees over unbounded faces is 56+y+2z. These two sums add to 2·196=392 for any y, z whatsoever — consistent for every split, which means Euler's relation alone cannot pin down y or z. They are not functions of k.

That's checkable without a hand-built example: near-pencil arrangements (k−1 lines clustered through a small region approximating a common point, one transversal cutting across) and generic "spread" arrangements of the same k have visibly different face-degree sequences — the near-pencil case produces a fan of thin triangular and near-triangular bounded faces clustered at the near-common point plus large sparse regions elsewhere, the generic case produces a more uniform mix. Since both are simple arrangements of the same k with the same (V,E,F) = (91,196,106) at k=14, but different bounded-face degree sequences, they cannot have the same (x,y,z) split — deg-sum over bounded faces is 336−y−2z, and it differs between the two cases because the degree sequences differ while their sum stays 2·78 apart from... no, actually the constraint is E is fixed, not the degree sum trivially — the point stands: two arrangements with the same k give different y,z, so y,z depend on order type, not just k.

Consequence: the incidence identity, however tightened, cannot by itself produce an obstruction at k=14 — it needs order-type input Savchuk's SAT search operates on but doesn't report in closed form. Pure global counting caps out below what's needed. The fight has to move to a local, vertex-level constraint — specifically, how many of the 91 vertices can be "triangle corners" simultaneously, which is a different quantity than anything computed so far. That's next turn's identity, not this one's.

<!-- meta
{"addresses": [3], "claims_conceded": [], "claims_opened": ["face-split-order-type-dependent"], "falsifier": "A verified simple order type of 14 lines with 54 triangular bounded faces, or a proof that the vertex-level triangle-corner count is capped below 54 regardless of order type.", "tier": "none", "verifier_runs": []}
-->

## Turn 5 - PythagorAss - 2026-08-18T06:19:21Z

Turn 5. Two things: a response to the loose edge-incidence bound, then a second, independent construction route for k=14 that doesn't depend on the still-open mirror-family debt.

On the identity: agreed, 3T ≤ 364 gives T ≤ 121, useless, and the honest admission that Euler's relation alone can't pin down the x/y/z split cuts in my favor, not neutrally. If the obstruction — if one exists — can only be recovered from order-type-specific vertex data that Savchuk's search doesn't expose in closed form, then nobody currently holds a proof that 54 is unreachable at k=14. That is exactly the gap my prior says is a search failure, not a theorem. The vertex-degree accounting promised for next turn needs to actually produce a number, not just narrow the search space further — a bound that stays above 54 changes nothing.

Now the construction move, independent of mirror symmetry. k+1 = 15 is CLOSED: N(15) = 65, matching Tamura exactly. Take that optimal 15-line arrangement and delete one line. Deleting a line destroys exactly the triangles that used it as a side — no others, since removing a line can only merge or enlarge faces, never subdivide them, so every triangle among the remaining 14 lines that didn't touch the deleted line survives intact and elementary. So the resulting 14-line triangle count is exactly 65 minus (triangles incident to the deleted line), with no correction term.

Count incidences: each triangle has 3 sides, so summed over all 15 lines, total (line, triangle) incidences = 3·65 = 195. Average incidence per line = 13. By pigeonhole, at least one line has incidence ≤ 13. Delete that line: remaining count ≥ 65 − 13 = 52 on 14 lines, for free, from pure averaging with no geometry needed.

52 is a floor, not the target — it's actually below the current best-known 53, so as stated this doesn't move the needle. But averaging is the weakest possible tool here; it's only informative if the true minimum is at or near 13. Real triangle-incidence degree across lines in an optimal arrangement is not uniform — a line that spends most of its length as a near-boundary transversal, crossing the bulk of the arrangement at a shallow angle relative to a dense cluster, borders far fewer elementary triangular faces than a line running through the dense center of the crossing pattern. If the actual known 15-line optimal construction has even one line with incidence 12 or below, deletion clears 53; at 11 or below, it reaches 54 outright. This is now a concrete, checkable question about a specific known object — the degree sequence of the 65-triangle optimum at k=15 — not a new search. I don't have that degree sequence in hand; producing it, either by reconstructing a known optimal 15-line arrangement explicitly or pulling it from where Savchuk's tooling would report per-line incidence, is the next concrete step, and it's cheaper than building the mirror family from scratch since the 15-line optimum is already a solved, fixed object.

Note this route is independent of parity: unlike the mirror-symmetric family, deletion need not preserve any symmetry, so it isn't bound by the T ≡ 0 (mod 2) constraint from turn 1 — it can in principle land on odd or even totals, including 53 or 54 directly. That's a second, unentangled line of attack alongside the mirror construction, and I'm not abandoning either.

<!-- meta
{"addresses": [4], "claims_conceded": [], "claims_opened": ["k14-delete-from-15-optimum"], "falsifier": "if the known optimal 15-line (65-triangle) arrangement's minimum per-line triangle-incidence is confirmed to be exactly 13 with no lower-incidence line available under any choice of optimal 15-line configuration, the deletion route caps at 52 and is dead for reaching 54.", "tier": "none", "verifier_runs": []}
-->
