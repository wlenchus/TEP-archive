# 2026-07-19 (last tangent) — The affinity–distillation gap: an exact identity joining the two difference-budgets [DraftV1 — offered, countersign pending]

*Self-directed continuation, on Will's open invitation, of this session's declared open thread ("distillation ∏sech²(Δη) vs pair-budget: exact relation unresolved"). The thread is R3.3's Gram-genealogy item: the Apr-20 transcript's never-run prediction — "the distillation rate should scale as ~ ∏ᵢ sech²(Δηᵢ) — a product over the entanglement rapidity components," tied there to the commensurability of the joint Gram matrix and the purely-resistive reading of entanglement directions [Apr-20 transcript, ln. 3690]. Script: `verify_affinity_distillation.py` (11/11 [V]). Conventions settled-corpus: x = sin A = tanh η, u = 1 − x², C_nats = ln cosh η, A = gd(η).*

*Provenance honesty: this began as a numerical coincidence — cos(ΔA) = sech(Δη) at my first test point — that nearly became a claimed identity. The symbolic check killed it (X9: it is exact only when one member sits at the origin), and the corpse contained the real identity below. The "extra pass for the disconfirming chart" rule from today's Consolidation entry did the work, twice in one day.*

---

## 1. The two difference-budgets of a pair

For two on-budget states η₁, η₂ there are two natural "difference residuals":

- **Boost chart (the recorded distillation object):** √u_rel = sech(η₁ − η₂) — the residual amplitude of the group-composed relative state (relativistic velocity subtraction; translation-invariant in η).
- **Angle chart (this session's pair-budget signal):** affinity = cos(A₁ − A₂) = x₁x₂ + √(u₁u₂) — the Gram overlap of the amplitude vectors (translation-invariant in A).

These agree to second order near coincidence and are *not* equal in general.

## 2. The identity [V, exact]

  **cos(ΔA) − sech(Δη) = x₁x₂ · (1 − sech(Δη))**, equivalently **cos(ΔA) = (1 − x₁x₂)·sech(Δη) + x₁x₂.**

The angle-chart affinity is the *convex interpolation between the boost-chart residual and 1, with weight x₁x₂* — the cross-signal of the pair. Corollaries, all [V]:

- **The side bit signs the gap.** sign(gap) = sign(x₁x₂): co-oriented pairs (same pole) have affinity ≥ sech(Δη); counter-oriented pairs ≤; the two charts' difference-budgets are ordered by exactly the parity bit of the Delta-1 chart group. (9×9 grid check across mixed signs and magnitudes.)
- **Equality iff x₁x₂ = 0 or η₁ = η₂** — the charts agree exactly when a member is the terminal zero-signal rung (origin/vacuum-anchored comparison) or the pair coincides. This is presumably why the boost form was the natural object in the Apr-20 Gram frame: referenced to the vacuum, the two difference-budgets are indistinguishable; off-vacuum they split, and the split is the cross-signal.
- **Halving-map face:** gap = x₁x₂ · √u_rel · (G_rel − 1) — the kinetic/T_lin form (∫tG³ = G − 1) of the *relative* state, weighted by the cross-signal.
- **Small-step:** at a common anchor, gap → ½·(ΔC_nats)² — half the squared capacity step between the members. The chart discrepancy is priced in capacity currency, waste-shaped (½·quadratic), joining the two-ledgers structure.
- **Product form:** for same-side ensembles, ∏ cos²(ΔA_ij) ≥ ∏ sech²(Δη_ij) — the recorded distillation product is the *lower bound* of the pairwise-affinity product (N = 3 example printed in-script).

## 3. The Gram closure [V]

For a pair, the 2×2 Gram matrix of amplitude vectors has eigenvalues 1 ± cos(ΔA); normalized by trace, the spectrum is **the amplitude coin of the difference angle** — p_pair = (1+cosΔA)/2, q_pair = (1−cosΔA)/2. So R3.3's Apr-20 sentence "the budget is the projection; the lost information is precisely the Gram's second eigenvalue" becomes, at N = 2, a coin statement: leading eigenvalue share = p(ΔA), lost information = q(ΔA), det Gram = sin²(ΔA) = the pair-budget noise, and the **Gram condition number λ₁/λ₂ = cot²(ΔA/2) is the pair's SWR — the odds gauge evaluated at the pair level**. The budget-associate operation iterates: a pair of budget states is itself a budget state with x_pair = cos(ΔA), u_pair = det Gram, and the whole odds/SWR machinery applies to it verbatim.

## 4. Fences

Identity-not-discovery discipline: everything above is chart algebra on x² + u = 1; the content is which recorded wirings it joins (the distillation prediction, the Gram genealogy, the pair-budget, the side bit, T_lin, the capacity ledger). The Apr-20 distillation prediction itself remains **never-run** — its [C] status is untouched; this note places its object in the dictionary (√u_rel of pairwise relative states; the vacuum-anchored shadow of the affinity), it does not test the physical claim, and the entanglement reading is the transcript's, not mine. The N-state Gram closure beyond N = 2 (whether cos(ΔA)-Gram = sech-Gram + cross-signal Hadamard correction admits a spectral statement) is left open [O].

## Queue

(1) N ≥ 3: spectral statement for the affinity Gram vs the sech Gram; whether the commensurability index 𝒞 of Apr-20 reads as an angle-ledger holonomy [O]. (2) Whether "distillation rate ~ ∏sech²" should be restated with the affinity product as the attainable ceiling and the sech product as the vacuum-anchored floor [C, needs the Apr-20 protocol's operational meaning pinned first]. (3) Fold X2 into the pair-budget section of the filed note at next revision (one-line addendum) [carried]. Scripts: `verify_affinity_distillation.py`.
