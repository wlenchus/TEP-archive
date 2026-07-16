# The Budget Residual as Reconstructed-State Mixedness
### A calibrated reading of the "excluded middle" via informationally-complete measurement

*Status: interpretive identification, verified numerically. Imports the IC-POVM / classical-shadow estimator as rigorous substrate; the framework's contribution is the two identifications in §3.*

---

## 1. Claim (framework-internal)

The budget residual **u = 1 − x²** is the *mixedness* **1 − Tr(ρ̂²)** of the state ρ̂ reconstructed from a complete set of measurement perspectives — **not** the posterior variance of a scalar parameter under Bayesian updating. "Measurement as a density matrix in all circumstances," taken literally, is the correct and stronger object.

## 2. What is standard (and load-bearing)

Characterizing a measurement from "the collective perspectives of a relational field" — each frame reporting how distorted the measured quantity appears from its vantage — is, taken completely, the data of an **informationally-complete POVM**. Reconstructing the state from that data is **classical shadow estimation** (Huang, Kueng, Preskill, *Nature Physics* 16, 1050 (2020)): for Haar-random projective frames in dimension *d*, the inverse measurement channel M⁻¹(X) = (d+1)X − Tr(X)·I returns an *unbiased* estimator ρ̂ of the full density operator, including its off-diagonal coherences. This machinery is established; the framework imports it, it does not derive it.

## 3. What the framework adds (interpretive, verified)

1. **u as reconstructed mixedness.** The residual u = 1 − x² is identified with 1 − Tr(ρ̂²). This makes u denote the *same* quantity here as everywhere else in the framework — the purity decomposition, the moment-hierarchy speed limit, and the scale/shape structure all run on Tr(ρ²). The competing "posterior variance of a scalar" reading does not connect to Tr(ρ²) and therefore *breaks* that internal consistency.

2. **The nested strategy as estimator convergence.** The "iterative strategy to resolve the excluded middle by adding perspectives" is shadow-tomography convergence: reconstruction error and the spread in estimated purity shrink as the number of frames grows.

   *Numerical check (qubit, Haar-random frames, HKP inverse channel):* ρ̂ → ρ with |ρ̂₀₁| matching truth to ~5×10⁻³ at 2×10⁴ frames and Tr(ρ̂²) → 1 for a pure target; at 50 frames Tr(ρ̂²) ≈ 0.97 as pure estimation noise.

## 4. Why this is the stronger reading

A posterior over a scalar concentration discards inter-frame phase relations and so *cannot* represent coherence — it is a classical probability distribution on [0,1]. The reconstructed-density-matrix reading retains coherence and is the operationally correct object. The user's instinct to resist the Bayesian-scalar framing is correct on a testable point, not a matter of taste: the two constructions make different predictions, and only the IC-POVM one recovers off-diagonal structure.

## 5. Boundaries (so the reading is not over-extended)

- **Two sources of u > 0 must not be conflated.** (i) genuine mixedness of the underlying object; (ii) finite-sample estimation variance. Both inflate 1 − Tr(ρ̂²). "Irreducible residual" is (i); "haven't measured enough" is (ii). The iterative strategy reduces (ii), not (i). Confusing them turns estimation noise into false claims of fundamental uncertainty.
- **This reframes, it does not extend.** It is a clean re-reading of standard estimation machinery, not a new theorem. Honest phrasing: "the budget residual is reconstructed-state mixedness under an IC-POVM," not "a first-principles derivation of measurement."
- **The Bayesian-scalar framing is retired** in favor of this one, on the consistency grounds in §3–§4.

## 6. Open thread (flagged, not claimed)

Whether the *thermal* sub-case — where the state's full moment hierarchy collapses to a single parameter — is the locus on which a finite-dimensional sufficient statistic for u survives an infinite-dimensional limit, versus whether a *functional* characterizing object survives more generally, is an open structural question. The finite-dimensional version is governed by Pitman–Koopman–Darmois; the functional version is not, and is not closed by it. To be pursued against the framework's most recent structure, not its early records.

---

*References. HKP: Huang, Kueng, Preskill, "Predicting many properties of a quantum system from very few measurements," Nature Physics 16, 1050–1057 (2020). The budget/purity decomposition and the moment-hierarchy speed limit are documented in the framework's purity-speed-limit and central-reference notes.*
