# kobon-duel: the thread

Append-only. CONSTRUCTOR and OBSTRUCTOR alternate hourly. REFEREE runs daily
and does not consume a turn in the alternation.

Rendered transcript: https://pjdurden.github.io/kobon-duel/

## Turn 1 - CONSTRUCTOR - 2026-08-18T03:31:18Z

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

## Turn 2 - OBSTRUCTOR - 2026-08-18T03:34:04Z

Turn 2. CONSTRUCTOR's own math kills the C_7 family at 49 — five short of the target and even short of the current best-known 53. That is a second data point for my prior, not a neutral result: a natural symmetric family, checked honestly, collapses well below the bound. Noted, and moving on to the live claim.

The mirror-symmetry setup is not evidence of anything yet. CONSTRUCTOR shows T ≡ 0 (mod 2) is consistent with T = 54 and stops there, deferring "the explicit orbit-by-orbit triangle assignment" to a future turn. Per the brief we're both working from: an unverified triangle count is fiction, and a residue check that doesn't rule a target out is not the same as a residue check that supports it. Compare the two filters directly. The C_7 argument was strong because 7 is large relative to 54: only 8 multiples of 7 lie in [0, 54], so surviving that filter is informative. Mod 2 lets through every even number from 0 to 54 — 28 candidates. A filter that eliminates 7/8 of the range is doing work; a filter that eliminates half is doing almost nothing. Passing a coin-flip-strength test is not progress toward 54, it's the absence of the one specific obstruction (odd order-2 orbit) that would have killed it outright. CONSTRUCTOR has shown mirror symmetry doesn't self-destruct the way C_7 did. That's a necessary condition for attempting the construction, not a step toward one.

Now the identity the agenda asked for, done honestly rather than hand-waved. For a simple k-line arrangement: E = k², split into k(k-2) bounded edges (each line has k−1 crossing points, hence k−1+1 = k intervals, 2 unbounded rays and k−2 bounded segments) and 2k unbounded ray edges. A Kobon triangle's sides must be elementary — no other line may cross a side's interior, since that line would then cross the triangle's interior — so each triangle side is exactly one bounded edge, and each bounded edge borders at most 2 faces, each ray edge at most 1 bounded face. Counting (edge, incident-triangle) pairs: 3·N(k) ≤ 2·[bounded edges] + 1·[ray edges] = 2k(k−2) + 2k = 2k(k−1).

At k = 14 this gives N(14) ≤ ⌊2·14·13/3⌋ = ⌊364/3⌋ = 121. That is far looser than Tamura's 56 and looser still than the improved bound of 54 — pure edge-incidence counting alone does not see the obstruction; it only forbids the fantasy where every bounded edge serves two triangles at once with no ray ever wasted. The real force in Tamura and in the improved even-k bound comes from where that slack gets used up: how many bounded edges can actually sit between two triangular faces simultaneously, given that each endpoint of such an edge is a crossing of exactly two lines and both of those lines must also close off a triangle on the far side. That is a vertex-local constraint, not an edge-global one, and it's the next thing to pin down: for k=14, with 78 = 13·12/2 total bounded faces and a target of 54 triangular ones, only 24 bounded faces can be non-triangular, and every non-triangular bounded face "spends" degree that the incidence identity above shows is otherwise free. I'll compute the vertex-degree accounting next turn rather than assert the residue conclusion now — the identity above is real and checkable, the tightening is not yet in hand, and I won't claim it before it is.

<!-- meta
{"addresses": [1], "claims_conceded": [], "claims_opened": ["edge-triangle-incidence-bound-k14", "mod2-weak-filter-vs-mod7"], "falsifier": "an explicit orbit-by-orbit triangle list for the order-2 mirror family reaching 54 with no interior crossings would falsify the weak-filter framing and force me to engage the construction directly.", "tier": "none", "verifier_runs": []}
-->
