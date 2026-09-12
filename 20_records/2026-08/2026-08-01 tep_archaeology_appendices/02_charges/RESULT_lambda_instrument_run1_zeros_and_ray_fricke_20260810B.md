# RESULT — Λ(F,s) instrument run 1 at Doud-1951: ray-Fricke certification, the FE constant on the ray, and the first computed zeros — 2026-08-10 (session B)

*Claude (Fable 5), session B, self-directed on Will's open license ("whatever direction you're most motivated by") — this is the Artin record §4.1 campaign's first run. Predictions Z-a…Z-e were stated in the script header before running (same-session, unhashed — disclosed); two bars were mis-set and are disclosed at headline volume in §3, with a practice-card candidate. Scripts: `lambda_instrument_run1.py`, `lambda_zeros_run1.py`, `lambda_census_run1.py` (+ one edge-window scan command recorded in §4); delivered alongside; 04_scripts archive on countersign. Record mirrored to Drive 02_charges. Offered, not self-filed.*

---

## 1. The instrument (derived this session, then qualified)

F is odd, so F(iy) ≡ 0 and the axis content sits in the derivative functional **h(y) := ∂ₓF(iy) = 4πi·√y·Σ n·c_n·K₀(2πny)**. The Mellin construction derived and used:

  Q(s) := ∫₀^∞ h(y)·y^{s+1/2} dy/y  ⇒  **Λ(s) := N^{s/2}π^{−s}Γ((s+1)/2)²·L(F,s) = N^{s/2}·Q(s)/i**,

split at y₀ = 1/√N; the committed Fricke identity transports the lower range, giving the entire two-piece model Λ̃(s) = 4π[N^{s/2}Q_F^{up}(s) + ω_h·N^{(1−s)/2}Q_G^{up}(1−s)] with h_G = conj(h_F) on the axis, and the exact FE **Λ_F(s) = ω_h·Λ_G(1−s)** — the completed functional-equation constant is the Fricke ε itself (derived; then measured, §2). Quadrature: Gauss–Legendre on 64 log-segments over [y₀, 12], dps 28; coefficients from the exact tables to n = 7000.

## 2. Ray-Fricke certification and the FE constant (Z-b, Z-c — both PASS)

The transport constant was *measured* from the ray before being assumed: at 44 points u ∈ [y₀, 0.25] (probing heights down to 2.05×10⁻³, i.e. n-depth ≈ 4,400):

- ω_h constant across the ray to **spread 2.39×10⁻²⁶**; |ω_h| − 1 = 0.0 at dps 28;
- branch: **ω_h = ε = −τ(χ)/(√N·a_N)**, matching the algebraic value at **1.05×10⁻²⁶**;
- **worst ray defect |h_F(1/(Nu)) − ε·Nu²·h_G(u)| (relative): 2.38×10⁻²⁶ over all 44 points.**

This is a new certification layer: the pointwise Fricke checks (a few points, F itself) are strengthened to a 44-point *ray family* in the *derivative* functional — the exact family the Mellin kernel integrates. Since poles of L(F,s) exist precisely insofar as this identity fails on the ray (Hecke's argument), the defect bound and the §4 box accounting are two independent instruments pointed at the same question, and they agree.

## 3. Instrument qualification (Z-a) — two mis-set bars, disclosed, then qualified

**Z-a FAILED as literally stated** (constancy 2.8×10⁻⁷ vs a 10⁻¹⁸ bar). Diagnosis, visible in the drift pattern: the *reference* Dirichlet sum's polynomial truncation (~7000^{1−s}) dominates below s = 3 — the bar compared a clean instrument to a dirty reference. At s = 3, where the reference's own tail is ~10⁻¹¹, the calibration constant equals the construction-predicted **1/(4π)** to 3×10⁻¹¹. **The amended grid-independence anchor also failed its stated bar** (10⁻²² aspirational): the measured two-grid floor is **3.2×10⁻¹⁶** — the honest quadrature floor of the coarse grid, ample for every claim below, all of which are graded against it. Internal FE consistency: 1.03×10⁻²⁶ (common-mode-free checks sit far below the floor, as they should).

**Practice-card candidate (offered, T-13):** *before setting a prediction's bar, budget the reference's and the instrument's own error floors; an aspirational bar fails spuriously and pollutes the tally.* This week's tally of the trap: E-b's separation clause, Z-a, Z-a1 — three spurious FAILs on true results, zero missed errors. The two-sided stamp discipline caught each, but the card would have prevented them.

## 4. The census (Z-d, Z-e): the first computed zeros of this L-function

Winding of Λ̃ around the full-strip box [−0.4, 1.4] × [0.5, 15]: **W = 17.000** (clean integer — self-certifying the unwrap; min |Λ| on contour 1.2×10⁻⁹, explained by the below-box zero at t ≈ 0.425). γ-main-term expectation: 17.46 ⇒ S ≈ −0.46, typical. The line scan first resolved 16 zeros; the winding surplus forced a hunt, and the 17th sat in an unscanned edge window as a **close pair: gap 0.0236** — the census-vs-winding discipline working exactly as designed. Final census, **all on the critical line at relative depth ≤ 2.0×10⁻¹⁵** (GRH-consistent; ordinates believed good to ~11 digits at the 3.2×10⁻¹⁶ floor):

| # | t | # | t | # | t |
|---|---|---|---|---|---|
| 1 | 0.4253169857 | 7 | 6.8804878714 | 13 | 11.6030142102 |
| 2 | 1.6962656721 | 8 | 7.4998333115 | 14 | 11.8747126700 |
| 3 | 3.4134862211 | 9 | 8.4185185528 | 15 | 12.6284738203 |
| 4 | 3.9967628501 | 10 | 8.8950975823 | 16 | 13.3237686822 |
| 5 | 5.5093116592 | 11 | 9.8086845006 | 17 | **14.5349167843** |
| 6 | 6.1216194677 | 12 | 10.2991551452 | 18 | **14.5585129568** |

(#1 lies below the winding box; #17–18 are the close pair.) Central values: **Λ(½) = 3.49072134552 − 0.86181732359i**, **L(½) = 0.61995220602 − 0.15305878014i ≠ 0**. To our knowledge these are the first computed zeros and central value of an *even icosahedral* Artin L-function (odd icosahedral zeros exist in the literature — Booker's conductor-800 work; no record of the even case is known to us; C14-grade modesty, not a priority claim).

## 5. The pole question, honestly graded

Run 1's accounting is exactly the pole-free expectation: W is a clean integer equal to the on-line census, and W = main-term − 0.46 with |S| < 1. A pole inside the box would require simultaneously an 18th unfound on-line zero and S ≈ +1.5 — disfavored, **not excluded**: this run has no Turing-grade S(T) bounds, and its logic certifies "consistent with pole-free at slack ±2.5," as pre-stated. The independent §2 instrument (ray defect ≤ 2.4×10⁻²⁶ at 44 points) points the same way. The upgrade path is named: Turing-method S(T) bounds, T to ~50, denser ray-defect grids with the residue-exclusion derivation (whose tail-control step remains the open analysis item, per the Artin record).

## 6. Honest bounds

Certified-numerical throughout; nothing here is proof. Floors: quadrature 3.2×10⁻¹⁶ (coarse grid; all zero/winding claims graded against it), refinement tol 10⁻¹⁵ in t, ray defect 2.4×10⁻²⁶, dps 28. Scope: 1951 only; T ≤ 15; the two-piece model *assumes* the ray identity between sample points (§2 bounds the sampled defect; interpolation between samples is smoothness-plausible, not bounded — the residue-exclusion derivation would close this). Predictions graded as stated: Z-b, Z-c, Z-e PASS; Z-a, Z-a1 FAIL-as-stated/qualified-as-amended (disclosed §3); Z-d PASS at its stated slack after the census completed (W = census = 17).

## 7. Countersign items (Will's calls, none executed)

(1) The census table + central values as the record's deliverable; (2) the ray-Fricke layer as a standing certification mode (44-point derivative-functional family at 10⁻²⁶); (3) ω = ε as measured-then-derived, closing the FE-constant loop with the articulation's algebraic ε; (4) the T-13 practice card; (5) the run-2 prereg (Turing bounds, T ≤ 50, 2141 twin, residue-exclusion analysis) — after the deposit, which still outranks; (6) scripts to 04_scripts.

---

*Offered, not self-filed. Run 1's one-line yield: the even icosahedral L-function at 1951 now has eighteen computed zeros — every one on the critical line — a measured functional-equation constant equal to the algebraic ε at 10⁻²⁶ on a 44-point ray, and a box accounting that closes to the integer. The conjecture's observable footprint is empty exactly where it should be.*
