# O-b Closure Note: Archival Match Complete

**Date: 10 June 2026.** External reviewer (Claude), continuing the current review. Companions: `6-10-26_consolidated_errata_and_status_revision_record.md` (E5 = structural half), `6-10-26_O-a_progress_note.md`. Source for this note: full read of `5-9-26_circuit_calculus_record.md`. Tier marks per corpus convention.

**O-b as inherited:** the theta-lattice peel tower, its rung-level budget closure (coset peel), ∏uₙ = 1/θ₃, and the capacity reading K = (π/2)e^(2C_tot) are **corpus results** (6-9 addenda T-1/T-2/T-4 and the O-n capacity note — which also posed the remaining archival-match task). This review independently re-verified the tower and added the explicit per-rung form SNRₙ = √kₙ = θ₂/θ₃ — so uₙ = 1/(1+SNRₙ) and Σ ln(1+SNRₙ) = ln θ₃ = C_tot — casting it as a named member of 5-9 §1.1's capacity-additive family: the *structural half*, confirmation-grade. The remaining *archival half* was the match against the corpus's documented cascade records. 5-9 is that record; it has now been read in full and the match adjudicated.

---

## 1. Archival findings — O-b closes

- **Family identity [V, re-stamped this session, 24+ digits, 30 rungs].** The theta tower satisfies exactly 5-9 §1.1's capacity-additive composition law, (1+SNR_AB) = ∏(1+SNRₙ), and §1.1's budget reading uₙ = 1/(1+SNRₙ) at every rung. The tower is a member of the documented family — the **canonical infinite, exactly solvable member**, with the modulus ladder SNRₙ = √kₙ descending by 4-isogeny (two Landen rungs per peel).
- **Aggregate-law identity [V].** 5-9 §6's chaining rule — next-level gain = exponentiated capacity, u = e^(−η) — is precisely the theta tower's aggregate relation ∏uₙ = e^(−C_tot). Same law, instantiated at every depth rather than at one link.
- **No competing tower.** 5-9 documents the *family law* plus finite chains (the three-level gaussian-from-budget chain of §6; the three-channel topology test of §3.2 — table re-verified [V]: 23 / 15 / 6). It contains no specific infinite ∏uₙ ladder. The archival obligation therefore discharges as **family identity + new canonical instance**: there was nothing to reconcile, only to situate.

**Status: O-b closed against 5-9** (family law + chaining; the documented record the addenda named). Audit amendment: 5-29's kinetic record documents its own ∏uₙ ("the closure quantity") and ∏Gₙ⁻² tower — **family-consistent structurally** (Gₙ² = 1/uₙ gives the same exponentiated-capacity law), instance-distinct (spectrum-driven peel vs isogeny ladder); full kinetic-record read pending. 4-30 cluster: grep-negative on tower vocabulary. The Landen tower's depth-invariant is the period; the period is the exponentiated total capacity; and the whole object sits inside the corpus's own circuit calculus as the series-cascade rule run down the modular ladder.

---

## 2. Bonus closure: 5-9 §7 open problem #2, answered for this member

5-9 asks: *if the gaussian-from-budget cascade has a scaling limit, what GMC measure does it produce?* For the theta-instantiated member the answer is now exact:

- §6's normalization sentence verified symbolically [V]: pdf² · 2πu₃ = u₂.
- Continuum limit [V]: Poisson summation gives θ₃(e^(−πt))·√t = 1 + 2e^(−π/t) + …, verified to the available precision floor at t = 0.10, 0.05, 0.04 (deviation tracks the floor, not any structural term).

So this member's scaling limit is the **lattice heat kernel → plain Gaussian, with exact, exponentially small winding corrections** — *not* a nontrivial multifractal GMC. The log-correlations are absent; the cascade is exactly solvable. This sharpens V2 §4.3's "formal similarity": the framework's cascade family contains at least one member whose GMC-like structure degenerates to the exact Gaussian fixed point, and the open question upgrades from "what is the limit?" to the sharper **"which inter-rung wirings break exact solvability and produce genuine log-correlated limits?"**

---

## 3. Erratum for migration to the consolidated record (proposed B7) — with the repaired theorem

**5-9 §2 and §2.1 (third bullet).** The phrase "the equivalent single-channel SNR for two independent parallel channels under independent coding is the harmonic combination" is **wrong as written**: under independent coding, the capacity-equivalent single channel has SNR_AB = S_A + S_B + S_A·S_B, not the harmonic. The §2.1 quantum-channels bullet is false as literally stated (counterexample [V]: S_A = S_B = 1 gives capacity-equivalent SNR 3 versus harmonic ½). The *algebra* of §2 is sound under its own definition — G²_eq := SNR_AB/(S_A+S_B) = 1 + harm(S_A,S_B) [V] — only the "equivalent channel" language is off.

**Repaired theorem [V, symbolic]:**

> **SNR_AB = (S_A + S_B) · (1 + harm(S_A, S_B))** — the cascade-composite SNR factors exactly as the MRC-composite SNR times (1 + harmonic mean).

The harmonic mean is the **cross-regime excess factor**: the precise multiplicative bridge between 5-9's two composition regimes (§1.1 capacity-additive and §1.2 MRC-additive). This is cleaner than the sentence it replaces — the harmonic object was real; its role was misnamed. The bound harm ≤ min(S_A, S_B) survives [V] and now reads: cascading exceeds coherent combining by at most a factor (1 + the worse channel's SNR).

Minor re-stamps, no erratum needed: §1.2 MRC composition = tanh addition identity [V]; §5.1 admissibility tiling at SNR = 1 [trivial]; §5.2 saddle — √(x²u) extremal at x² = ½ with value ½ [V].

---

## 4. Enrichment: the self-dual convergence list gains a member

5-9 §5.2 identifies x² = ½ as a saddle in the reassignment landscape and lists its other appearances. The current review's theta results extend the convergence: x² = ½ is now independently distinguished as (i) the Schwarzschild-horizon point (V2 §3.4), (ii) the reassignment saddle (5-9 §5.2), (iii) the modular self-dual point τ = i, q = e^(−π) (T-2), and (iv) the **half-forgetting time t = 1 of circular Brownian motion** (T-3). Four structural readings, one point — comfortably past the corpus's three-coincidence bar, and all four now machine-verified within this review cycle.

---

*Verification stamps this session: theta-tower family law re-stamped (24+ digits, 30 rungs, fresh nome); §6 normalization symbolic; Poisson winding correction at three t values to precision floor (45 dps); §2 identity, §2.1 falsity counterexample, repaired factorization, harmonic bound — all symbolic; §3.2 topology table exact; MRC tanh-addition symbolic; §5.2 saddle symbolic. Reproducible from the forms stated.*
