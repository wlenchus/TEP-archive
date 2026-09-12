# PRE-REGISTRATION — the self-dual crease locus (Charge 1, prediction P-R)

*Filed 2026-08-06, **before computing any of the quantities below** beyond the two already-published degree-2 values noted in §5. Claude (Opus 5), following Will's reflectance/transmission-duality framing of the Delta 5 result. Supersedes nothing; P-H remains open and unrescued. Offered, not self-filed. Bars are not moved after this filing.*

---

## 1. The port budget (derived, not predicted)

For a disk domain, Delta 5 gives `T = f(A) + f(z₀)I` and `I = Re[conj(f(z₀))·⟨f(A)x,x⟩]`. Expanding `‖Tx‖²` with `‖f(A)x‖ = c`:

  **‖Tx‖² = c² + 2I + |f(z₀)|².**

Setting `τ := c²/4` (transmission share), `r := |f(z₀)|²/4` (reflectance share), `ι := I/2` (interference share), `u_eff := 1 − ‖Tx‖²/4` (absorption), this is the identity

  **τ + r + ι + u_eff = 1,**

and `‖T‖ ≤ 2` is exactly `u_eff ≥ 0`. A **crease is negative interference share**: the interference channel running in deficit against the other three. In amplitude-phase form, `I = |f(z₀)|·|⟨f(A)x,x⟩|·cos Δ`, so `ι` is (reflectance)×(direct read)×(phase) — the cross-term the port picture says it is.

This section is bookkeeping. It is stated first so the prediction below is not confused with it.

## 2. The prediction

Will's structure: at d = 2 self-duality, transmission is constrained and absorption/reflectance become mutually-constraining duals. Translated to this budget, the self-dual balance is **τ = r**, i.e. `|f(z₀)| = ‖f(A)‖`.

**P-R1 [novel — load-bearing].** For every A that admits a crease, the **global** minimiser of `I` (unconstrained by level) sits at the self-dual balance:

  **|f(z₀)| / c = 1.**

**P-R2 [novel].** At that minimiser the port read annihilates the maximising vector:

  **‖Tx‖ = 0, equivalently u_eff = 1 — total absorption.**

**P-R3 [novel].** At that minimiser the depth is exactly minus the transmission:

  **I = −c², equivalently ι = −2τ.**

P-R2 and P-R3 follow from P-R1 *given* exact anti-phase (`Δ = π`); they are listed separately because anti-phase is itself part of the claim and could fail independently.

**P-R4 [control, costless — labelled so].** `J₂` shows no crease at all (`min I = 0`), since Delta 5 §5 proves `I = |x₂|²|a₀|²(1+α) ≥ 0` there. Its confirmation is not evidence for anything.

**No prediction is made** about: which A admit creases; the depth's dependence on n; whether the minimiser is unique; or anything off the disk.

## 3. Why this is discriminating

The competing fold/spectral reading (Delta 1.1) locates crease behaviour in interior Jordan structure — multi-sheet wrapping of `∂W` by `f = z^{n−1}`. **That reading gives no reason whatever for the deepest crease to occur where the reflected amplitude equals the operator norm.** `|f(z₀)| = c` is a statement relating a boundary-centre value to a global operator norm; it is a port condition or it is a coincidence. If P-R1 holds across dimensions and across normal/non-normal cases, the port reading is doing work that the spectral reading cannot account for.

## 4. Kill conditions

- **K-R1.** If, for two or more crease-admitting test matrices, `|f(z₀)|/c` at the global minimiser deviates from 1 by more than 10%, **P-R1 is falsified** and the self-dual reading of the crease locus dies. No weakened form is available.
- **K-R2.** If P-R1 holds but `‖Tx‖ > 0.1·c` at the minimiser for two or more matrices, P-R2 is falsified independently (balance without total absorption).
- **K-R3.** If `I/(−c²)` deviates from 1 by more than 10% for two or more matrices, P-R3 is falsified independently.
- **K-R4 (coverage).** A matrix contributes to the verdict only if ≥ 20 restarts converge and at least one yields `I < −10⁻¹⁰`. Matrices failing this are reported as *no crease found at this degree*, excluded from the verdict, and **not** counted as support.
- **K-R5 (optimiser limit).** If doubling the restart budget moves any reported `|f(z₀)|/c` by more than 5%, the run is inconclusive and no verdict is issued.

**No rescue.** If K-R1 fires, the record will say the reflectance reading of the crease locus resolved against TEP.

## 5. Disclosures

**Not blind, and exactly how.** P-R1–P-R3 were *derived from* two values already computed and published in Delta 5 Addendum 1: the degree-2 family optimum on `A = diag(ρ,0)`, where `t\* = (1−√(1−ρ⁴))/ρ²` gives `f(ρ) = −f(0)` and `I = −c²`. I noticed `|f(z₀)| = c` there while writing this file. So **the 2×2 normal, degree-2 case is retrodiction, not prediction**, and is excluded from the verdict.

The prediction is genuinely blind for: all nilpotent `A_n` (n ≥ 3), all non-normal 2×2, all degrees > 2, and all normal cases beyond the single family above. Nothing about any of those has been computed.

**Training-prior.** The interference functional is this corpus's construction (2026-08-01) and the port budget of §1 was derived in-session today. There is no literature on any of it to recall.

**Method.** Unconstrained minimisation of `I` over degree ≤ 4 Blaschke products — no level constraint, hence none of the thin-feasible-shell pathology that made P-H run 1 inconclusive. That is the methodological reason to prefer this test, and it is a reason of convenience; it is not evidence for the prediction.

---

*Offered, not self-filed. Countersign items: the §1 budget identity as [T]; the §2 prediction classes; §4 as binding; the §5 disclosure that the 2×2 normal degree-2 case is retrodiction and excluded.*
