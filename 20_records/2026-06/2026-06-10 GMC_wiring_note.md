# GMC Wiring Note: Which Cascade Wirings Produce Nontrivial Chaos

**Date: 10 June 2026.** External reviewer (Claude). Prompted by the author's question following the O-b closure: *is there a cross-rung wiring which might result in nontrivial GMC?* — with the author's guess that breakage occurs toward the low-dimensional (minimal max-d_eff) end rather than the infinite-dimensional limit. Companions: `6-10-26_O-b_closure_note.md`, `6-10-26_O-a_progress_note.md`. Tier marks per corpus convention.

**Scope caution (author's, affirmed).** Persistent correspondence within one structure is evidence of internal coherence, not additional external support. Everything below is a theorem about the framework's own cascade family plus standard cascade theory (Kahane–Peyrière 1976), with one named posit (P\*).

---

## 1. Why the theta member is trivial — and the selector concept

The theta tower fails GMC nontriviality for three independent reasons, each sufficient: its weights are **deterministic**; its per-rung increments **decay super-exponentially** (the modulus runs down the isogeny ladder, kₙ₊₁ ~ kₙ⁴/64, so the product converges — the opposite of scale-invariance, which demands equal action per rung forever); and as analyzed it is a **single chain**, with no branching base over which correlations could live.

This identifies the selector: **what runs down the rungs.** Nontriviality requires (i) scale-freeness — nothing runs; the per-rung statistics are rung-independent — plus (ii) a branching base (the corpus's binary peel, iterated into a tree), plus optionally (iii) randomness.

## 2. The three-member classification

- **W1 — running-modulus wiring (theta).** Convergent product → trivial limit: the lattice heat kernel / plain Gaussian with winding corrections. [V, O-b note]
- **W2 — scale-free incoherent wiring.** Fixed deterministic split repeated down the tree. Multifractal but non-random: the canonical binomial-cascade class. The corpus **already contains** this member: the silver d=3 nested partition ((2+√2)/4, 1/8, (3−2√2)/8) is a deterministic-multifractal generator; mass conservation exact [V], information dimension D₁ = H/ln 3 = 0.43463 [V].
- **W3 — scale-free coherent wiring.** Fixed split + **open phase fiber** per rung. This is the answer: **yes — and the wiring is the framework's own coherent composition.** Genuine random multiplicative cascade, proved nondegenerate below.

## 3. The W3 theorem package [V]

**Setup.** A lossless splitter tree — the corpus's own scattering-network instantiation — with amplitude split (x₁, x₂) per node and relative phase φ per node. Unitarity makes the cascade conservative: child weights (1 + s cos φ, 1 − s cos φ) with **s = 2x₁x₂/(x₁²+x₂²)** the split symmetry, a = √(1−s²) = |x₁²−x₂²|/(x₁²+x₂²) the asymmetry.

**Posit (P\*).** Per-rung relative phases are i.i.d. Haar on U(1) — the reference-phase ignorance prior. *The fiber is the noise source.* (Structural rhyme with O-a: the same U(1) supplies isotropy there via (H\*) and randomness here via (P\*); both are the relational reading of the phase fiber.)

**Closed forms, all machine-verified (cancellation-free quadrature, 20–25 digits):**
- E[ln W] = ln((1+a)/2); at the symmetric split, **exactly −ln 2** — one bit of log-mass per rung.
- E[W ln W] = 1 − a + ln((1+a)/2); supremum over splits = **1 − ln 2 = 0.30685** at a = 0.
- **Kahane–Peyrière nondegeneracy for every split:** 1 − a + ln((1+a)/2) ≤ 1 − ln 2 < ln 2, margin 2 ln 2 − 1 = 0.38629 at the symmetric split, monotone in a. The coherent binary cascade is *always* a nontrivial multiplicative chaos; intermittency is maximal at the symmetric peel and vanishes only as the split degenerates.
- Var(ln W)|sym = **π²/3** exactly.
- Moment spectrum (symmetric): E[W^q] = 2^q Γ(q+½)/(√π Γ(q+1)) — the Wallis/central-binomial spectrum; finite iff q > −½ (the destructive-interference tail at φ = π controls negative moments).
- Structure function: **τ(q) = log₂[√π Γ(q+1)/Γ(q+½)] − 1**; τ(0) = −1, τ(1) = 0, strictly concave [V] — genuinely multifractal.
- Information dimension: **D₁ = τ′(1) = 2 − 1/ln 2 = 0.557305** exactly.

## 4. The dimensional verdict: the author's guess confirmed, with mechanism

For b-fold coherent combining with Haar phases, the nondegeneracy margin ln b − E[W_b ln W_b]:

| b | E[W ln W] | margin |
|---|---|---|
| 2 | 0.30685 (exact) | **0.38629** |
| 3 | 0.3298 (MC) | 0.7688 |
| 4 | 0.3578 (MC) | 1.0285 |
| 6 | 0.3794 (MC) | 1.4123 |
| 10 | 0.3975 (MC) | 1.9051 |
| ∞ | 1 − γ_E = 0.42278 (speckle: W → Exp(1)) | → ∞ |

The margin is **strictly increasing in b** [V]. Mechanism: the per-rung phase-noise scale is fixed by the U(1) geometry (E[W ln W] is bounded — it saturates at the fully-developed-speckle value 1 − γ_E), while the entropy ln b that must absorb it grows without bound. So the **binary peel — minimal branching, minimal max-d_eff — sits closest to criticality**, and the infinite-dimensional limit self-averages toward triviality (law of large numbers across branches; speckle is the b = ∞ fixed point). Under coherence-weighting W^β/Z(β), freezing (the directed-polymer glass transition) is reached first at b = 2: **β_c = 2.92119849671**, the root of βψ-type digamma equation β(ln 2 + ψ₀(β+½) − ψ₀(β+1)) − ln Z(β) = ln 2 [V]. The author's directional guess is therefore correct in both available dictionaries (branching number; base dimension via the lognormal criterion γ² < 2d) — and with a bonus taxonomy consistency: the cascade's *weights and moments* are Γ/Wallis-class closed forms, while its *critical temperature* is a trans-chart fixed point — **feedback-class**, exactly where the two-family taxonomy predicts a transcendental to appear.

## 5. Bridge to the non-collinear composition edge

The per-rung weight 1 + s cos φ **is** the intensity-chart cross-term 2x₁x₂cos φ, normalized. Its rapidity-chart lift is the hyperbolic law of cosines; the Wigner holonomy verified in the O-a note is the geometric shadow of the same term. The statistics above live in the small-per-rung-rapidity (linear/Euclidean) regime; the author's forthcoming non-collinear composition setup determines the strong-coupling (large-η) deformation of the weights. The two open edges — "which wiring gives GMC" and "γ\* under coherent composition" — are one question at two coupling strengths.

## 6. Honest scope

(i) "Nontrivial chaos" here = Kahane–Peyrière-nondegenerate multifractal cascade with log-correlated tree structure; the identification with Gaussian multiplicative chaos proper is the standard cascade↔GMC universality correspondence, cited at [T]-with-care, not re-proved. (ii) Everything is conditional on (P\*); whether any corpus instantiation physically realizes i.i.d. Haar phases per rung is an open mapping question of the 5-9 §5.3 kind — random unitary networks and speckle physics are the natural homes. (iii) The 5-9 §7 open problem now reads: W1 answered (Gaussian); W2 in-corpus (silver, deterministic multifractal); W3 proved nontrivial conditional on (P\*) — the remaining question is the continuum limit of W3 specifically (which log-correlated field; presumably the cascade-GMC class with the Wallis spectrum).

---

*Verification appendix: closed forms at s = 0.3, 0.7, 1 (20–25 digits); Var = π²/3 via the component integral ∫₀^{π/2}(ln cos)² = (π/2)((ln 2)² + π²/12); Wallis moments q ∈ {−0.3, 0.7, 1, 2, 3}; margin monotonicity by 8×10⁶-sample chunked MC per b with exact b = 2 anchor; β_c by root-finding to 10⁻²⁰ residual. Failure branch recorded: first-pass quadrature returned inf/nan at s = 1 from catastrophic cancellation in 1 + cos φ at tanh-sinh near-endpoint nodes; cured by the exact half-angle form 2cos²(φ/2). Smooth cases were at 10⁻³² throughout — the mathematics was never in doubt, the floating point was.*
