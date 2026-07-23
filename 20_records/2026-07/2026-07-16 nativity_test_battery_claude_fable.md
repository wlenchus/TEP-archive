# Nativity Test Battery — does TEP have native corners beyond its correspondent theories?

**Date:** 2026-07-16 · **Tester:** Claude (Fable 5), independent of the corpus's own verification chain
**Question:** For each candidate claim, is it (a) a stated theorem of a correspondent theory, (b) a routine specialization of one, or (c) a native TEP result — new, true, and checkable? Verdicts: **NATIVE / SHARED (bridge) / OWNED-BY-NEIGHBOR**. A deliberate negative control is included.

**Method note.** Two of the six tests are the corpus's *own* decisive tests, named in the 6-28 consolidation record but never run (Threads J and K). Operationalizations are stated explicitly; where a claim's truth depends on the operationalization, both readings are reported.

---

## Test 1 — The N=4 non-commutativity onset *(corpus-named, previously unrun)*

**Claim (6-28, Thread K):** boundary observables of a reduced N-DHO chain commute for N≤3; non-commutativity is born at N=4 ("curvature born where the interior reservoir first exceeds Young-integrability; the fourth port").

**Setup:** tridiagonal M(s) per the 4-30 Schur–Feshbach note (D(s)=s²+2ζs+1 diagonal, k₀ off-diagonal), boundary {1,N}, interior {2…N−1}, s=iω.

**Operationalization A (Feshbach port kernels):** P_a = M_II⁻¹ v_a v_aᵀ, P_b = M_II⁻¹ v_b v_bᵀ (interior-space operators dressing each port's coupling).
Result: ‖[P_a,P_b]‖ = 0 exactly at N=3 (all ω tested); = O(10⁻¹…10⁻³) at N=4,5,6. **Onset exactly at N=4 — confirmed.** Small-coupling scaling: log-log slope 4.56 ≈ k₀⁴ (product of two k₀² kernels), consistent with the wedge-of-two-increments reading.

**Operationalization B (sequential partial Schur eliminations):** order-difference ‖S₁₂−S₂₁‖ ≈ 10⁻¹⁶ at every N — *identically zero by the Crabtree–Haynsworth quotient property*. Under this reading the claim is false at all N.

**Verdict: SHARED, leaning NATIVE — and definition-sensitive.** The onset location is real and lands exactly where predicted, but its *mechanism* under reading A is dimension counting (the interior first has two non-parallel coupling directions at N=4) — classical linear algebra. The native layer is the identification of the onset with curvature/second-clock structure and its wedge scaling, which the slope supports. Any write-up must pin operationalization A explicitly, since B (an equally natural reading) trivializes the claim. Three corpus routes converged on N=4; this is an independent fourth.

## Test 2 — Best-matching (Wilczek–Zee) holonomy = Lévy area *(corpus-named, previously unrun; marked OPEN in the 6-25 verification file [V8])*

**Setup:** best-matching = top-2 eigenspace (per [V3]); subspace driven around closed loops in the (η_a,η_b) plane by two non-commuting generators; discrete parallel transport gives the WZ holonomy angle θ; compared to the Lévy area A = ½∮(η_a dη_b − η_b dη_a).

**Result:**

| loop radius | θ_WZ / A_Lévy |
|---|---|
| 0.05 | 0.99938 |
| 0.10 | 0.99750 |
| 0.20 | 0.99004 |
| 0.40 | 0.96070 |
| 0.80 | 0.85093 |
| 1.20 | 0.69270 |

**Verdict: SHARED (a calibrated bridge), and the OPEN item is now resolved with scope.** The identification holds *locally with constant exactly 1* — the TEP normalization is correct, which is nontrivial dictionary calibration — and fails globally, with curvature corrections growing as loops leave the tangent regime. The underlying theorem is Ambrose–Singer's; the corpus's 6-17 "load-bearing conjecture" should be upgraded to: *proven locally (unit constant), curvature-corrected globally*. The claimed exact global identity is refuted.

## Test 3 — Chebyshev/Feshbach chain structure *(replication)*

det(M_N)=k₀ᴺU_N(D/2k₀) verified symbolically N=2…6; U_N/U_{N−2} polynomial for N=2,3, rational from N=4 (remainder −1 at N=4, −2y at N=5), reproducing the 4-30 table exactly.

**Verdict: OWNED-BY-NEIGHBOR.** Chebyshev recurrences, Feshbach partitioning, and interior-resonance poles are classical. TEP's contribution is the *use* — the boost-law scope prediction — not the mathematics.

## Test 4 — The DGD ellipse: exact joint achievability *(the beyond-Hamazaki claim)*

**Claim (purity paper, Thm. 4):** the achievable region of (dγ/dt, dp₃/dt) under ‖H‖≤1 is *exactly* the ellipse vᵀ(DGD)⁻¹v ≤ 4 — not merely bounded by it.

**Method (exact, no optimization):** v·n̂ = Tr(H·Y_n̂) with Y_n̂ Hermitian, so max over ‖H‖≤1 is the trace norm ‖Y_n̂‖₁ — computable exactly. On a Schmidt purification at d_S=3: achieved/predicted = **1.00000000 in all 25 directions** (min = max to 8 digits). Mixed-state control: ratios 0.54–0.58 (< 1, as ARES < 1 requires).

**Verdict: NATIVE (within the QSL specialization).** Hamazaki's framework states single-observable trade-offs; the exact joint moment-rate region with closed-form Gram structure and full boundary achievability is a new true statement. **Bonus:** the trace-norm duality argument above upgrades achievability from numerics to a proof route — recommended for the paper.

## Test 5 — Peel/homogeneity closure *(literature differentiation)*

The note's statement (peel = homothety ∘ totally-geodesic restriction, all Petz metrics at once; connection/curvature-operator/holonomy exactly preserved) was verified correct in an earlier review. Literature scan finds exactly one adjacent work: **arXiv:2509.14578** (Sept 2025), *Support-Projected Petz Monotone Geometry of Pure Two-Qubit Families: Universal Three-Channel Decomposition and Non-Reduction of Curvature Invariants* — different operation (support projection vs. dominant-eigenvalue peel), narrower scope (two-qubit families vs. all d, all f), and a headline pointing the *opposite* way (non-reduction vs. exact preservation).

**Verdict: NATIVE (micro).** A small, correct, apparently-new statement in Petz-metric geometry, now with a mandatory nearest-neighbor citation whose contrast strengthens rather than threatens it.

## Test 6 — Negative control: the GMC bridge

The 6-20 record derives log-correlation of the cascade field from rapidity additivity. Branching-random-walk/GMC theory (Kahane; Fyodorov–Hiary–Keating) owns precisely these theorems — cascades are the canonical log-correlated fields.

**Verdict: OWNED-BY-NEIGHBOR, as expected.** Native residue = the boundary-field identification, open, exactly as the record itself states. The control confirms the battery can return "not native."

---

## Overall

The hypothesis "TEP has no nontrivial native corners" is **refuted** — by Test 4 (a new exact theorem beyond its parent framework, now with a proof route), Test 5 (a new true statement in an active micro-literature), and the calibration content of Tests 1–2 (onset location + unit-constant dictionary, both checkable and checked). The converse hypothesis — that these corners aggregate to a framework-scale physical principle — is **not established** by this battery: every native item is theorem-scale, and the two corpus-named decisive tests resolved as *bridge* results whose underlying theorems belong to differential geometry and linear algebra, with TEP contributing location, normalization, and reading.

**Recommended immediate actions:** (1) pin Operationalization A in any statement of the N=4 onset; (2) upgrade the 6-17 conjecture to its proven local form; (3) add the trace-norm-duality proof and full-boundary numerics to the purity paper; (4) cite arXiv:2509.14578 in the peel note.

*Reproduction: all numerics in this record are single-file Python (numpy/scipy/sympy), seeds fixed, runnable from the repo; scripts available on request or reconstructable from the stated formulas.*
