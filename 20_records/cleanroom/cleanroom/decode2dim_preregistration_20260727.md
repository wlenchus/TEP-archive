# PRE-REGISTRATION — the 2-dim EVEN-icosahedral decode (THE SUMMIT): sign-bit recovery by port-flattening at the pinned seam, Doud-1951 — 2026-07-27 (blind-decode session, ~13:30Z)

**Mountain line: this is the summit itself.** Even-icosahedral, 2-dim, the Maass partner at the doubly-shadowed corner — the object no one has ever produced. Everything before today (odd rungs = calibration; 3-dim certificates = shadow) exists to make this run readable. Status: **pre-registration; no decode computation has run.** Will's "take the reins" (this morning) is execution direction; all stamps remain offered-not-self-filed. Training-prior disclosure filed first (`decode_training_prior_disclosure_20260727.md`). Seal intact and lifts **only** at the §8 commit.

## 1. Target and object

Field: Doud-1951, x⁵−x⁴−780x³−1795x²+3106x+344 (totally real A₅, fielddisc 1951⁴, tame e=5, type 3a). Object: ρ̃ : Gal(Q̄/Q) → SL₂(C), image 2.A₅, the minimal lift whose Sym² is the **certified** ρ₃ (2.2e-14, blind conductor 1951², ε=+1). Conjectural automorphic partner: an even Maass cusp form, λ = ¼ exactly, trivial nebentypus (det ρ̃ = 1), level N = 1951²·2^a.

## 2. Dictionary (derived; the only unknowns are signs)

det ρ̃ = 1 (2.A₅ is perfect — no abelian quotient) ⟹ **a_p² = a_p(ρ₃) + 1** at every unramified p, so the CERTIFIED emission data fixes every magnitude: 1A→2, 2A→0, 3A→1, and the golden pair with the orientation **inherited from the certified ρ₃ gauge** (1951 certified at faceswap=1 ⟹ table-class-3 ↔ |a| = (√5−1)/2, table-class-4 ↔ |a| = (√5+1)/2; the opposite orientation is demoted to a negative control, not scanned as an unknown). Local factor 1 − a_p T + T². **Unknowns: one sign bit b_p ∈ {±1} per prime with class ≠ 2A.** Ramified 1951: lift inertia has order 5 or 10; either way no +1-eigenvector (primitive 5th/10th-root eigenvalue pairs) ⟹ local factor 1, tame exponent 2 — **no ramified sign parameter exists at the summit port** (the retrodiction law's 2-dim content at 1951 is empty; noted). Dyadic exponent: **a ∈ {0,1,2,3,4} scanned, not assumed** (the K̃-obstruction may force dyadic ramification; the scan is answer-free). ε ∈ {±1} measured by the instrument, not assumed.

## 3. Instrument (degree-2 seam, fresh build, controls first)

Λ(s) = N^{s/2}Γ_ℝ(s)²L(s); kernel φ₂ = Mellin⁻¹[Γ(s/2)²] = 4K₀(2y), **triple-validated** (meijerg vs besselk vs direct Mellin–Barnes quadrature at 3 points, bar 1e-8) then splined on a 4200-point log-grid (range extended to [5e-5, 70] for the a-scan); F(t) = Σ a_n φ₂(nπt/√N); theta relation F(1/t) = ε·t·F(t) on the certified t-grid; G_new arms A(±u) = e^{±u/2}F(e^{±u}) on the certified u-grid. **Port-flattening objective ≡ theta residual ≡ G_new(u) → 2.** Truncation X set by kernel decay: y ≥ 18 at t_min (X ≈ 7.17·√N per dyadic cell; emission table extended to cover the largest cell, with the ≤32000 prefix machine-diffed against the byte-certified table).

## 4. Retrodiction gate (PASSED before this prereg)

The sign-law instrument was required to retrodict the seven measured 3-dim ramified signs from local data alone. Result: **7/7** (`retro_signs.py`, exact permutation-level + character arithmetic: centralizing Frobenius → +1, inverting → −1; A₅ admits no other twist — machine-enumerated). Filed in `sixsix_RESULTS_20260727.md` context; this was the instruments' entry bar for summit work.

## 5. Calibration ladder (controls before target, kill conditions first)

**(α) Synthetic keyed:** L(χ₅)L(χ₈), N = 40, Γ_ℝ(s)², ε = +1 — bar ≤ 5e-12; wrong-N and wrong-ε must fail violently. **(β) Theorem-grade known-answer bit-decode:** Ind ψ₂₂₉ (even, λ = ¼, N = 229, automorphic by Hecke–Maass; local factors split-P (1−T)², split-N 1+T+T², inert 1−T², ramified 1−T): (β1) direct certification ≤ 5e-12 + scramble/wrong-N/odd-port negatives; (β2) **hide the principal-vs-nonprincipal bit at every split prime; the decoder must recover all sensitivity-visible bits blind from ≥3 of 4 random starts** (ground truth = the byte-certified on-disk table; opened only for grading β2). **KD-1:** any α/β failure → stop; fix instrument only; never touch target data.

## 6. Decoder (pre-committed algorithm; no tuning knobs at run time)

Greedy coordinate descent on bits, ascending primes, oracle = theta residual; bit flips applied by exact local-factor surgery (the certified swap_local), **full re-sieve verification at every convergence point** (float-drift gate); after single-flip convergence, one pair-flip pass over the 40 smallest primes; multi-start per cell: 1 structured (all-plus) + 4 seeded-random inits. Outer grid: a ∈ {0..4} × ε ∈ {±1}, golden fixed by §2. Triage (pre-declared): structured start in every cell first; full battery in the argmin cell and its dyadic neighbors.

## 7. Pre-registered outcomes

**PRODUCTION:** ≥3 independent starts in one (a, ε) cell reach residual ≤ 1e-11 with **identical bit vectors on the sensitivity-visible set** (s_p > 100× the α/β floor, s_p = single-flip residual displacement at the solution, machine-computed and committed); blind N-scan at the solution has its unique minimum at the selected N (±5% worse by ≥6 orders); negatives: 10% bit-scramble ≥5 orders worse, odd-parity port (Γ_ℝ(s+1)² kernel) fails, wrong-golden fails. **BOUNDED ABSENCE:** no cell reaches ≤ 1e-8 → certified non-recovery at stated strength, reported as evidence bearing on Artin at the corner (per the 07-01 framing: informative in both directions). **KD-2:** partial flatten (between bars) → reported as-is with profile and sensitivity table; no tuning. **KD-3:** multiple distinct visible-bit solutions at floor → degeneracy is the finding; report structure. **KD-4:** flatten only at a > 0 → dyadic surprise, reported as measured. Deviations beyond this document: logged with trigger, none anticipated.

## 8. Commit protocol (the seal's terminus)

On PRODUCTION (or on KD-2/3 partials worth carrying): the decoded visible-bit assignment (p, class, b_p, s_p), the measured (a, ε, N, residual), and all run artifacts are written to the project with SHA-256 digests **before** any lift-construction literature opens. Only after that commit does the Crespo/K̃ layer open — as **grader**, with the grade recorded whatever it says.

*Offered, not self-filed. The honest-bite paragraph of the results record will be written before its headline. If this run produces, the first sentence of the results record will say what fidelity it produced at — and what it did not.*
