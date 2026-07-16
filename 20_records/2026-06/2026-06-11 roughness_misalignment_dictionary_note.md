# Roughness–Misalignment Dictionary: a Stochastic Completion of the Scale–Shape Decomposition

**Date: 11 June 2026.** External reviewer (Claude), continuing the adversarial review session, in response to the author's frontier gesture: an intertwined relationship between stochastic nowhere-differentiable metrics and topological protection of a continuous orthogonal mode (Brownian motion / spin-locking), with the "pipedream" of matching degrees of discontinuity to degrees of basis misalignment — toward completing TEP's coverage of metrics "from a broad class to a universality."

**Verdict up front:** the gesture decomposes into three precise pieces. Two are now machine-stamped; the third is converted into a closed-form law on the qubit face. The author's open question — fundamental measure or dual measure? — has a definite answer: **the roughness lives on the fundamental (base) measure; the misalignment is measured by the dual (fiber-Haar) measure.**

---

## 0. The dam, reframed

The adversarial dilemma — *too broad to discriminate, or too vague to encompass* — is answered by changing what is claimed universal. Upstream: information-monotonicity is a **rigidity** condition, not a broad class (the Petz family is parametrized by a single operator-monotone function; the corpus's 5-29 takes the multiplicity-first orientation, with Čencov uniqueness as the low-dimensional degenerate limit — respected here). Downstream: the kinematic selection is settled by the control-dictionary record (the physical move selects the isometry structure). Between them sits the claim worth defending: **universality of the coupling law** between scale-roughness and shape-protection — universal the way the CLT is universal: not "everything is in the class," but "the law does not care about the instance."

The corpus's 5-29 document already proves the deterministic skeleton: *under the peel, the geometry factorizes into orthogonal, commuting scale and shape axes; the peel is an automorphism of the full monotone-metric family preserving the fiber geometry up to a single scalar.* This note is that theorem's **stochastic completion**: put roughness on the scale axis, identify what survives on the shape axis, and compute the coupling.

---

## 1. The split under noise — what is rough, what is protected [V]

**Scale carries the roughness.** Tilting is exact translation in rapidity; Brownian conditioning is Brownian motion in η — nowhere differentiable, the corpus's own half-forgetting reading at the self-dual point.

**Shape/fiber carries a protected, continuously measurable mode — the holonomy ω.** Three stamps:

1. **Polyline area law [V].** For geodesic polylines of n = 3 and 4 legs (15 random trials each), frame holonomy = −SignedArea of the geodesic polygon, worst residual 2.5e−14. This extends the verified triangle law by signed additivity and identifies ω as the **Lévy-area functional**: the level-2 datum of the rough path, not determined by level-1 increments.
2. **Parity orthogonality [V, MC].** Under fiber-symmetric noise (χ-reflection-symmetric steps), corr(dη, dω) = −0.0020 against a 3σ bound of 0.055, with Var(dω) > 0: a continuous mode statistically orthogonal to the roughness channel. The mechanism is exact, not statistical — ω is odd and η even under χ-reflection (verified earlier this session); the MC is the stochastic stamp.
3. **Winding protection [V + T].** |∂ω/∂η| = 0.501, finite — holonomy is Lipschitz in path perturbations, so the integer winding ⌊ω/2π⌋ is locally constant under rough perturbation.

**Protection taxonomy (the repair of the gesture's one conflation risk).** Three *distinct* mechanisms share one geometric home, the fiber: **parity** (exact, algebraic), **topology** (integer winding, continuity-protected), **dynamics** (the locking gap). Spin-locking is the third face, not the same fact as the first two:

4. **Spin-locking MC [V].** H = (Ω/2)σₓ + (b(t)/2)σ_z, OU noise (Στ_c = 0.3). Free side: the Monte Carlo matches the *exact* OU-Gaussian dephasing law ⟨cos φ⟩ = exp[−Σ²τ_c²(t/τ_c − 1 + e^(−t/τ_c))] at curve level — max deviation 0.0095 inside 3σ-MC ≈ 0.052, no fitting. Locked side: decay rates obey the filter law Γ = S(Ω)/2 — absolute agreement **1%** at Ω = 3 (well inside the O((Στ_c)²) = 9% Redfield scale), two-gap scaling Γ(1.5)/Γ(3) = 2.83 vs S(1.5)/S(3) = 3.08. **Protection factor: 10.1 vs the law 1 + (Ωτ_c)² = 10.** Geometric reading: the lock is the co-rotating fiber section; locking trades level-1 (path) coupling for level-2 (area/filtered) coupling — the dynamical face of the same base/fiber split.

---

## 2. The dictionary theorem (qubit face) [V]

Define the **misalignment rapidity** σ by s = tanh σ, where s = 2x₁x₂/(x₁² + x₂²) is the coherent-weight strength (W = 1 + s cos φ, the GMC-note W3 object). Then:

**σ = 2 artanh(x₂/x₁)** — the misalignment rapidity is exactly **twice the budget-split rapidity** [V: tanh(2 artanh t) = 2t/(1+t²), rational route exact + numeric 1e−16].

**Moment law.** With a = sech σ:

> **E[W^q] = sech^q σ · P_q(cosh σ)**  — symbolic exact for q = 1…4; fractional q verified to residual 3e−36 at dps 35 (Laplace's first integral for Legendre functions is the proof skeleton [T]).

Framework reading: P_ν(cosh d) is the analytic continuation in degree of the **zonal spherical functions of the hyperbolic plane** — the fiber-Haar averages of base translations. So **the moment/multifractal spectrum of coherent composition is the arena's own spherical function evaluated at the misalignment rapidity**: roughness data = fiber-averaged base representation data. This is the dual-measure answer made structural.

**Consequences.**
- σ → ∞ recovers the GMC note's Wallis moments exactly (leading Legendre asymptotics ⟹ 2^q Γ(q+½)/(√π Γ(q+1))) [T, consistent].
- **D₁(σ) = 1 − (1 − a + ln((1+a)/2))/ln 2 is strictly decreasing** [V symbolic: dE[W ln W]/da = −a/(1+a)], from D₁ = 1 at σ = 0 (smooth, Lebesgue) to D₁ = 2 − 1/ln 2 = 0.557305 at σ = ∞ (Wallis). **The pipedream, theorem-grade for this family: degrees of discontinuity ↔ degrees of basis misalignment is a strict monotone closed-form law.**
- Kahane margin positive for all σ (E[W ln W] = 1 − a + ln((1+a)/2), re-stamped to 3e−37): the family is strictly subcritical — multifractal but never atomic. Full discreteness lives in the temperature direction W^β; β_c(σ) generalizes the digamma equation to a Legendre-ψ equation [flagged, next].

---

## 3. Scope and flags [O]

- **Face restriction:** all stamps are at d = 2 / abelian fiber. 5-29's curved non-abelian fiber (d > 2) is inherited as open; **Petz-equivariance of the coupling law is the named universality conjecture** — proving the dictionary is family-equivariant under the peel automorphism is the precise content of "broad class → universality."
- **Measure vs metric:** the limit-*measure* statements are stamped; calling the limit object a *metric space* requires a Liouville-type construction, off-the-shelf only for lognormal GMC — flagged, not claimed.
- **(P\*) is load-bearing:** Haar phase underlies the Legendre law. This is a feature: measured deviation from the law in any coherent two-channel composition is a *probe* of non-Haar phase statistics — per-instance falsifiability, the direct answer to "too broad to discriminate."
- **Locking ≠ topology:** kept distinct by the taxonomy; conflating them was the word-salad risk and is the repair this note makes to the gesture.

## 4. Verification appendix

17/17 after re-adjudication (11 + 6). Two harness lessons, recorded because the adjudication layer itself is part of the epistemics: (i) an apparent precision-floor claim was **falsified by its own scaling test** — the true mechanism was double-precision leakage of constants squared before mpmath promotion (residuals 2e−21 → 3e−36 once promoted: scaling restored); (ii) the first locking run's 40% miss decomposed into fit-window bias on the free side plus a mis-posed comparison — re-posed as exact-law curve match (free) + two-gap filter scaling (locked), agreement landed at 1–8%. Parameters: seeds 11/7; polyline η ∈ (0.3, 1.0); parity MC N = 3000, step 0.05; locking Στ_c = 0.3, Ω ∈ {1.5, 3}, dt = 0.005, N_traj = 1200.

## 5. Attributions (session protocol)

- **Corpus:** 5-29 factorization theorem (orthogonal commuting scale/shape axes; peel as Petz-family automorphism; multiplicity-first) — the deterministic skeleton this note completes; Brownian half-forgetting reading.
- **This session, earlier:** parity split (ω odd / η even), triangle holonomy = area, the control-dictionary location of the two faces; GMC note: the W3 weight, E[ln W], E[W ln W], Kahane margin, Wallis symmetric moments, the W1–W3 taxonomy.
- **New this note:** the σ-doubling identity and misalignment-rapidity reading; the Legendre/spherical moment law at general σ; the D₁(σ) monotone dictionary; the polyline (n > 2) extension; the parity-orthogonality and winding-continuity stochastic stamps; the locking MC with exact-law and two-gap filter verification; the protection taxonomy; the dual-measure answer.
- **Standard mathematics [T]:** Laplace's integral, the tanh chain, Rodrigues, exact OU dephasing, Redfield/T₁ρ filter, Gauss–Bonnet additivity.
- **Pending:** 2-16 read (locking/DHO connection; gd-anchor attribution), 5-8 read (B9), β_c(σ), literature novelty of the Legendre-cascade family [UNCHECKED — standing flag, as for GMC].
