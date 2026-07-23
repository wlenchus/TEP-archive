# Test Round 2 — surviving proposals executed; corrections absorbed

**Date:** 2026-07-17 · **Tester:** Claude (Fable 5) · **Companion to:** the 2026-07-16 nativity battery
**Scope:** every test proposed in the review conversation that survived Will's corrections unreconsidered. Tiering: [V] machine-verified this round; [C] corrected/withdrawn; [O] open item handed to the corpus.

---

## R2.1 — PT gain-loss chains: the zero-knob threshold prediction [V]

**Pre-registration (in-conversation, before computation):** from the 4-30 Schur reduction (K_eff = √(N−1)·k₀ for N ≤ 3, polynomial boundary) plus the gain-sector dictionary entry written in advance (dimer EP = budget saturation, splitting = 2k√u), the PT-breaking threshold of a uniform chain with gain/loss at the ends is γ_EP = √(N−1)·k for N ≤ 3 **exactly**, deviating at N ≥ 4 where Feshbach poles switch on, in the direction of *reduced* threshold.

**Result:** N=2: γ_EP = 1.00000000·k (exact). N=3: γ_EP = 1.41421350·k = √2·k (exact — the corpus's K_eff constant materializing as a PT threshold in a sector the corpus never visited). N=4: 1.000·k (−42.3% vs naive √3). N=5: 1.22474·k. N=6: 1.000·k. N=7: 1.15470·k. Both halves of the prediction land: exactness through N=3, breakdown at exactly N=4, correct direction.

**New pattern handed to the corpus [O]:** broken-regime thresholds have closed forms — even N pins at γ = k; odd N follows γ = √((m+1)/m)·k with m = (N−1)/2 (√2, √(3/2), √(4/3), …). Derivation target: the 4-30 Feshbach pole structure should reproduce this. If it does, this is a publishable note (*PT thresholds of boundary-gain chains from Schur reduction, including the polynomial→rational breakdown*). Caveat: PT-chain thresholds are studied (Joglekar et al. lineage); the claim is not that the numbers are new to physics but that the TEP/Schur dictionary predicts them with zero knobs and predicts its own failure point.

## R2.2 — Null tests: one mis-designed, one converted by Will [C→V]

**GMC surrogate null [C]:** phase-randomizing a *Gaussian* field returns the same process; the null was tautologically unable to discriminate. Salvaged insight: the 6-20 record's [V] checks certify universality-class *membership*, not mechanism *uniqueness* — consistent with its own [M] tiering. A proper null must break the cascade *hierarchy*, not the phases. [O: design and run the hierarchy-breaking null.]

**False-budget classifier [C→V]:** the strawman version (complementarity-only) showed 100% false-positive rate — quantifying the necessity of the 5-21 guardrail the corpus already had, not discovering a flaw. Will's sufficiency framing then *closed* the open item: a budget claim is a triple (Y, 𝔅, A) with A = ‖E[Y|𝔅]‖²/‖Y‖²; truth = **fixed-projection realizability with Pythagorean closure**; non-exhibition = rejection. Implemented and verified [V]: true budgets residual ≈ 0.02, arbitrary complementary pairs 0.08–0.40 — clean fourfold separation. (Threshold wants a proper ROC on larger ensembles before use.)

**Recognizer v2 proposal [O, Will's]:** typed output, not boolean — the 2×2 (sub-/super-additive × probabilistic/affine) mapped onto the corpus's e/m dual-budget fork (KL/e-flat vs L²/m-flat realizations of the same Pythagorean identity), with the d=2 W-reduction ([V9]) as canonical form.

## R2.3 — The edge scan: QSL–EP–GMC triangle [V]

QSL–EP side: partially claimed (trapped-ion PT-qubit QSL experiment, NJP 2024) — but not via moment-observable/budget structure. EP–GMC side and the full triangle (*all three transitions = one budget-saturation point*): no literature found. **The edge stands unclaimed**, sharpened into a pre-registrable statement: the PT-breaking threshold and the GMC freezing point are the same saturation transition, therefore a shared critical signature (to be specified precisely — candidate: the marginal 1/√n·log n finite-size slowdown appearing at EP coalescence) must hold across both.

## R2.4 — Will's point 4 resolved: the discriminating "2-point" object [V, corpus 6-29]

The 6-29 record's Thread A identifies it: the **two-frequency boundary-screen commutator** ‖[M(λ₁), M(λ₂)]‖ of the Schur-complemented chain — identically zero for N ≤ 3, igniting at exactly N=4, *conditional on broken mirror symmetry (κ_first ≠ κ_last) and connected interior*. This is a 2-point statistic with full discriminating power because its two points are *evaluation frequencies of one operator*, not spatial samples of one field — no surrogate construction preserves it. No contradiction with R2.2's Gaussian-surrogate limitation; different objects entirely.

**Correction absorbed into Test 1 of the 07-16 battery:** the battery's Feshbach-kernel operationalization ([P_a, P_b] at one frequency, two ports) and the corpus's own ([M(λ₁), M(λ₂)], one boundary operator, two frequencies) are distinct faces of the same N=4 anholonomy — both ignite at N=4, under different symmetry conditions (the battery's fires even for mirror-symmetric chains; the corpus's requires asymmetry). Reconciling the two conditions is a small open item [O] with real content: which commutator is the *invariant* face of the onset?

---

*All numerics single-file Python, seeds fixed. Corrections in this record trace to Will's interventions of 07-16/07-17; the sufficiency predicate is his, implemented.*
