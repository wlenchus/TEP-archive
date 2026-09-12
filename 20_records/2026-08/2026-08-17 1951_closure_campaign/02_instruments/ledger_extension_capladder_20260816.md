> **NOTE (curated pack, 2026-08-17).** This record carries a co-located **ERRATUM at its foot** — its claimed window-1 identity revision (960.674 → 960.6240) was **refuted** by two method-independent recomputations; the correct value is **960.67184**. The ladder rows, all five controls, and the ramified certificate are unaffected. Read the erratum with the record.

---

# LEDGER EXTENSION — the cap ladder at (Γ₀(1951), χ): pricing the full χ-weighted class-number geodesic ledger, X ≤ 10 — 2026-08-16

*Future-ledger synthesis charged off `claude/closure_scattering_trace_pincer_cohh_20260816.md` (parent identity) and `charges/STAMP_adversarial_verification_closure_20260816.md` (verified conventions: elliptic DOUBLED, golden prefactor 1.721632 = 2·(4logφ)/√5). All computation this session, mpmath dps 20, scripts `/home/claude/ledger/led.py`. Offered, not self-filed.*

## 0. The identity as used (stamp-corrected conventions)

Test pair: h(r) = (sin Lr/Lr)⁴, window X = 4L; g(u) = (1/2L)·T(|u|/2L) exactly, where T = Λ*Λ is the cubic B-spline (T(x) = 2/3 − x² + x³/2 on [0,1], (2−x)³/6 on [1,2]); g(0) = 1/(3L), supp g = [0, X), g ≥ 0, cubic vanishing at the edge. Closed form verified against (1/π)∫h cos(ru)dr to 1e−9.

B(L) = (488/3)·2∫₀^∞ h·r·tanh(πr)dr **+ (4/(3√3))·2∫₀^∞ h·cosh(πr/3)/cosh(πr)dr** [doubled per stamp] + Ledger(L) + 1/2 − (3log1951 − 2logπ + 2log2)·g(0) − (2/π)∫₀^∞ h·Reψ(1+ir)dr − (2/π)∫₀^∞ h·Reψ(½+ir)dr + 4·Σ_{n=p^k, 2logn<X} Λ(n)Reχ(n)n⁻¹g(2logn).

Then m(0) + #{exceptional} ≤ B (h ≥ 0 on ℝ, h(ir) ≥ 1 for |r| ≤ ½, h(0) = 1). Character: primitive root 3, χ(3^k) = ζ₅^k, full index table built; checked ind₃(2) ≡ 4, ind₃(5) ≡ 1, ind₃(148) ≡ 0 (mod 5).

Quadrature: subdivided [0, 1/L, …, 20/L] tanh-sinh head + **exact oscillatory tail** for the identity term (sin⁴ = 3/8 − cos2Lr/2 + cos4Lr/8; ∫_T^∞ cos(ar)/r³dr in closed form via Ci; cross-checked against quadosc to 2e−8). Digammas on per-period panels to 100/L.

## 1. The ledger

Ledger(L) = Σ_D Σ_{k≥1, kℓ_D<X} h(D)·(ℓ_D/(2sinh(kℓ_D/2)))·2Re(χ(r_D^k))·g(kℓ_D), over non-square D ≡ 0,1 (mod 4) with (D|1951) = +1; (t₀,u₀) fundamental of t² − Du² = 4, ε_D = (t₀+u₀√D)/2, ℓ_D = 2logε_D = 2acosh(t₀/2); h(D) = number of reduction cycles of primitive reduced forms of disc D (proper/SL₂ classes); r_D = (t₀+u₀s)/2 mod 1951, s² ≡ D (root choice immaterial under 2Re). Primitive ℓ_D in the numerator for all powers k (Selberg standard). Ramified assert: **no D ≡ 0 (mod 1951) enters for X ≤ 8** — max relevant D < 3902 and neither 1951 (≡3 mod 4) nor 3902 (≡2) is a discriminant; asserted in code over the full enumeration.

**Provenance (honest bound of tonight's derivation):** the correspondence "primitive hyperbolic classes ↔ proper classes of primitive forms, one per (D, class), automorph ε_D from t²−Du²=4, Γ₀(N)-splitting ×2 by the two roots mod N with nebentypus weight χ(root)" is the Sarnak/Hejhal-standard ledger. It is CALIBRATED here by K1/K5 (and by the ACNF certification below), not re-derived. The cap rows below are conditional on that standard parametrization plus the stamp-verified identity.

## 2. Controls — all five resolved

- **K1 (calibration) PASS.** At X = 3.496 the general code finds exactly one line: D=5, h=1, k=1, ℓ = 1.9248473, value 1.721632·g = 0.1192009. B(3.496) = **276.4607** vs target 276.460 ± 0.02.
- **K2 (occurrence) PASS.** 12⁹⁷⁵ ≡ 21⁹⁷⁵ ≡ −1 (mod 1951): D = 12, 21 (traces 4, 5) excluded. 5⁹⁷⁵ ≡ 32⁹⁷⁵ ≡ 45⁹⁷⁵ ≡ +1: included.
- **K3 (edge continuity) PASS.** At X* = 3.52549 (D=8, 32 entry) and X* = 3.84969 (D=45 and D=5² entry): entering-line values at X*+0.002 are 5e−11–2e−10 (cubic edge); ΔB across the boundary (−0.6463, −0.4952) matches the smooth slope just after (−0.6441, −0.4936). No jumps.
- **K4 (class numbers) PASS after explicit convention reconciliation.** Cycle code: h(5)=h(8)=h(13)=1, h(40)=h(85)=2 as expected; but **h(12)=2, h(60)=4** against the charge's expected 1, 2. Resolution: the cycle count is the PROPER (SL₂ = narrow) class number by construction; the charge's 1 and 2 are the WIDE (ideal-class) values. The two conventions coincide exactly when N(ε₀) = −1 (true for 5, 8, 13, 40, 85) and differ by 2 when N(ε₀) = +1 (true for 12, 60). Certification: Dirichlet's formula h_cyc(D)·logε_D = √D·L(1,χ_D) verified numerically at all seven fundamental test discs, ratio 1.000000 (12: 2·log(2+√3) = √12·L(1,χ₁₂) ✓; 60: 4·log(4+√15) = √60·L(1,χ₆₀) ✓). Proper is the count the geodesic correspondence needs (γ and γ⁻¹ are separate conjugacy classes); proceeded on proper.
- **K5 (Pell + distinctness) PASS.** D=45: (t₀,u₀) = (7,1), ε = (7+3√5)/2 = φ⁴, ℓ = 3.8496946 = 8logφ. The ledger contains BOTH the primitive D=45 k=1 line (h=2, weight 2.0) and the imprimitive D=5 k=2 line at the same total length, as distinct entries. Bonus structure: r₄₅ ≡ r₅^±2 (1515 = (148²)⁻¹ mod 1951), so χ-coherence along the golden chain is forced.

**Refinement found during calibration (flagged):** the parent's window-1 identity term 960.674 is a tail artifact of mpmath's default [100/L, ∞) quadrature (shared by the stamp's blind replication); the tail-exact value is **960.6240** (closed-form Ci tail and quadosc agree to 2e−8). Corrected window-1 total: B = 946.62 (stamp's 946.67 − 0.05). Cap 946 unchanged. At window 2 the effect is 1e−3 (282.734 → 282.7351) and K1 is unaffected. **[WITHDRAWN — see ERRATUM below.]**

**Anchor autopsy (non-gating):** the charge's rough anchor B(8) ≈ 50–58 came from 1/L² extrapolation of the identity term (282.735·(0.874/2)² = 54.0); the true identity(L=2) = 46.8235 (verified two independent ways) because r·tanh(πr) is not yet saturated at L = 0.874 — the naive scaling overestimates. logblock(L=2) = −3.638 hits its anchor.

## 3. The ladder

| X | L | identity | elliptic(×2) | +½ | log-block | digamma(1) | digamma(½) | primes | **Ledger** | #discs | #lines | max h | **B(X)** | **⌊B⌋** | bulk budget B−1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.496 | 0.874 | 282.7351 | 0.76151 | 0.5 | −8.32385 | 0.09124 | 0.49306 | 0.08443 | **0.11920** | 1 | 1 | 1 | **276.4607** | **276** | 275.461 |
| 5 | 1.25 | 132.7653 | 0.68480 | 0.5 | −5.82003 | 0.14981 | 0.51426 | 0.09528 | **0.24250** | 7 | 8 | 4 | **129.1319** | **129** | 128.132 |
| 6 | 1.5 | 89.3322 | 0.63765 | 0.5 | −4.85003 | 0.15376 | 0.49553 | 0.07223 | **0.32028** | 14 | 16 | 4 | **86.6616** | **86** | 85.662 |
| 7 | 1.75 | 63.4173 | 0.59449 | 0.5 | −4.15717 | 0.14942 | 0.47027 | 0.03726 | **0.41893** | 19 | 21 | 8 | **61.4305** | **61** | 60.431 |
| 8 | 2.0 | 46.8235 | 0.55533 | 0.5 | −3.63752 | 0.14207 | 0.44371 | 0.00140 | **0.53030** | 45 | 51 | 12 | **45.3588** | **45** | 44.359 |
| 10* | 2.5 | 27.7739 | 0.48804 | 0.5 | −2.91002 | 0.12576 | 0.39373 | −0.05542 | **0.66118** | 153 | 163 | 32 | **26.9772** | **26** | 25.977 |

*Headline: m(0) + #exceptional ≤ **45** at X = 8 and ≤ **26** at X = 10, down from the parent's 276 — conditional only on the calibrated standard ledger parametrization.* The budget row is the conjecture-implied bulk mass Σ_{r_j>0} h(r_j) = B − 1 if the packet's single r = 0 form exists.

## 4. Ten largest |lines| at X = 8 — (D, h(D), ℓ_D, k, 2Reχ(r^k), value)

| D | h | ℓ_D | k | 2Reχ | value |
|---|---|---|---|---|---|
| 5 | 1 | 1.92485 | 1 | +2.000 | +0.21130 |
| 45 | 2 | 3.84969 | 1 | +2.000 | +0.10680 |
| 140 | 4 | 4.95578 | 1 | −1.618 | −0.04979 |
| 165 | 4 | 5.11796 | 1 | +2.000 | +0.04968 |
| 32 | 2 | 3.52549 | 1 | +0.618 | +0.04472 |
| 221 | 4 | 5.40715 | 1 | +2.000 | +0.03302 |
| 252 | 4 | 5.53732 | 1 | +2.000 | +0.02713 |
| 5 | 1 | 1.92485 | 2 | +2.000 | +0.02670 |
| 8 | 1 | 3.52549 | 1 | +0.618 | +0.02236 |
| 320 | 4 | 5.77454 | 1 | +2.000 | +0.01853 |

## 5. Structure — three defensible observations

1. **Golden-chain dominance; class numbers never dominate.** D=5's power tower plus D=45 (= φ⁴'s disc, χ-weight inherited via r₄₅ = r₅²) carry ~60% of the X=8 ledger. The eleven discs with h ≥ 6 — up to h(2300) = 12 at X=8, h = 32 at X=10 — contribute net −0.0037 at X=8. Mechanism, not accident: by the class number formula h(D)·logε_D = √D·L(1,χ_D), so per (D,k=1), h(D)·ℓ_D/(2sinh(ℓ_D/2)) ≈ 2√D·L(1,χ_D)/ε_D = O(L(1,χ_D)) = O(log D) since ε_D ≳ √(D−4): **a large class number forces a long automorph; every disc's line is capped at ~2L(1,χ_D)·g regardless of h.** The ledger is structurally tame.
2. **χ-interference is real but subdominantly destructive.** χ_j(r_D) over the 45 contributing discs at X=8 is near-equidistributed: {j=0: 11, 1: 8, 2: 9, 3: 9, 4: 8}. Coherence ratio (actual / all-weights-2) = 0.616 at X=8, falling to 0.419 at X=10 — cancellation grows with the window. Yet the NET ledger is positive at every rung, because the shortest geodesics — where g-mass sits — are quintic residues (j = 0: D = 5, 45, 165, 221, 252, 320); full-weight lines carry 94.7% of the X=8 net. Negative mass grows (−0.060 at X=8, −0.254 at X=10) but never wins. No conspiratorial cancellation; also no accumulation strong enough to matter.
3. **The ledger never fights the cap.** Ledger(X) grows roughly linearly (0.119, 0.243, 0.320, 0.419, 0.530, 0.661) while the identity term collapses ~X^{−2..−3}; the geodesic total stays a < 2.5% correction at every rung. The march of ⌊B⌋ (276 → 129 → 86 → 61 → 45 → 26) is identity-driven; extrapolating the parent's B ≈ 3607/X² law, B ≈ 10 still needs X ≈ 19, and nothing in the observed χ-equidistribution or the O(L(1,χ_D)) per-disc cap suggests the ledger will obstruct it. (Observation at X ≤ 10, not a theorem.) Minor: the prime-power term flips sign at X = 10 (−0.0554), first negative rung of that column.

## 6. Stretch X = 10 and the ramified certificate

D = 7804 = 4·1951 is a legitimate discriminant; its Pell x² − 1951y² = 1 has fundamental x₀ of 36 digits (y₀ 34 digits): **ℓ_7804 = 164.2045**. No ramified geodesic exists below X = 164; the exhaustive trace enumeration (t ≤ 148) confirms zero D ≡ 0 (mod 1951) with ℓ < 10. The X = 10 row is therefore clean — no one-sided allowance needed anywhere on this ladder. (For 3902: ℓ = 54.83, also irrelevant.)

## 7. Honest distance

What this ladder does NOT do: (i) no lower bound on m(0) — positivity runs one way, and nothing here forces the packet to exist; (ii) the cap charges m(0) and possible exceptional eigenvalues jointly — separating them, and any two-sided localization, needs certified eigenvalue lists at (1951, χ): Hejhal-algorithm computation with BS07-grade interval certification is the named remaining instrument; (iii) the ledger correspondence itself is calibrated (K1/K5, ACNF), not re-derived — a re-derivation from the Γ₀(N)-conjugacy side would upgrade the rows from "standard-conditional" to self-contained; (iv) the K4 convention finding means any future cross-check against wide class-number tables must apply the N(ε₀) = +1 doubling before comparison.

*Offered, not self-filed. 2026-08-16.*

## ERRATUM — same day, filed by the commissioning session on spot-check

The §2 "Refinement found during calibration" (window-1 identity 960.674 → "tail-exact" 960.6240; B₁ = 946.62) is **WITHDRAWN as refuted**. Two method-independent recomputations by the commissioning session both give identity(L = 0.4812) = **960.67184**: (i) exact decomposition — head on sub-period intervals [0,5] with tanh exact, tail via sin⁴ = 3/8 − cos(2Lr)/2 + cos(4Lr)/8 with the mean term in closed form and the two cosine integrals by quadosc at their true periods; (ii) composite Simpson with 600,000 nodes to r = 3000 (≈1300 nodes per oscillation period — aliasing impossible) plus an analytic remainder. The parent's 960.674 was therefore correct to 2·10⁻³; the corrected-convention window-1 total is **B₁ = 946.68** (doubled elliptic), integer cap 946 unchanged. This record's own window-1 quadosc/Ci computation could not be reproduced and its error was not localized (its scripts report agreement of two routes at 2e−8 with each other — a correlated-error signature, both routes evidently sharing the faulty tail expression).

Scope of the refutation: window 1 ONLY. The ladder is untouched — at the ladder's own windows the same two independent methods reproduce this record's identity values exactly (46.823535 at L = 2.0; 282.73509 at L = 0.874), K1 was calibrated at window 2 where all methods agree, and every other control, table, and observation stands as filed. The anchor-autopsy paragraph survives (46.8235 confirmed).

*Provenance: erratum by the session that commissioned this record (session C lineage), after decomposition + Simpson spot-checks run before relaying the record's claims. The refuted refinement had itself claimed to correct the parent and the stamp; the stamp's original figure stands. Filed at headline volume, co-located.*
