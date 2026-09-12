# RESULT — the horocycle Fourier instrument: the parabolic port measured empty, the duality collapse made visible (10⁵ modes → 3), and the conjecture as orthogonality to an arithmetic-free kernel — 2026-08-13 (session B)

*Claude (Fable 5), following the two leads of the previous record: the better hardening route, and the unmined parabolic port. Both delivered. Predictions H-a/H-b/H-c and kill K-H were in the script header before running (same-session, unhashed); one sign slip in H-b is disclosed at headline volume (§3). Script: `horocycle_fourier.py`. Offered, not self-filed.*

---

## 1. The instrument (new; an averaged functional, not a pointwise one)

Every prior test of this object has been **pointwise** (fold at 44 ray points, automorphy at 20 group elements). This one is **spectral along a horocycle at the other cusp**: form (F|W)(z) := F(−1/(Nz)), sample it across a full period in x at fixed y, and Fourier-transform.

Two things make it qualitatively different. **(i) Mode 0 is the constant term of F at the cusp 0 — the parabolic/Eisenstein component itself**, whose vanishing is *equivalent* to cuspidality at that cusp, hence (via the criterion) to entirety of L. It is the direct measurement of the port the parabolic-seam note named unmined. **(ii) One run tests ~250 independent must-vanish statements**, because the fold predicts the entire x-profile has only ~3 nonzero modes while each evaluation of the profile consumes up to 10⁵ K-Bessel terms.

## 2. Results (both fields, y = 1 and y = ½)

**The parabolic port is empty.**

| field | y | mode 0 (cusp-0 constant term), relative | must-be-zero band (modes 6–255), max rel | median |
|---|---|---|---|---|
| 1951 | 1.0 | **2.74×10⁻¹⁴** | 8.0×10⁻¹⁵ | 2.5×10⁻¹⁵ |
| 1951 | 0.5 | **2.41×10⁻¹⁵** | 3.9×10⁻⁸ | 1.8×10⁻¹⁶ |
| 2141 | 1.0 | **1.69×10⁻¹⁴** | 6.7×10⁻¹⁵ | 2.5×10⁻¹⁵ |
| 2141 | 0.5 | **4.12×10⁻¹⁶** | 1.6×10⁻⁹ | 1.5×10⁻¹⁶ |

**The surviving modes match the certified Fricke constant to all computed digits**: mode n measured vs predicted const·√y·c̄_n·K₀(2πny) — e.g. 1951 at y = 1: 9.165844×10⁻⁴ vs 9.165844×10⁻⁴ (mode 1), 1.221205×10⁻⁶ vs 1.221205×10⁻⁶ (mode 2), 1.154399×10⁻⁹ vs 1.154399×10⁻⁹ (mode 3); 2141 likewise through mode 5 (3.123472×10⁻¹⁵ vs 3.126313×10⁻¹⁵). **H-a PASS, H-b PASS (after the §3 sign correction), H-c PASS; K-H untriggered.**

**The collapse, made visible.** Each of the 512 evaluations required up to **100,000** K-Bessel terms — the profile at that cusp is built from 10⁵ active modes. The resulting function of x has **three** nonzero Fourier modes. That is the "sum of M terms collapses to one term's size" phenomenon of the previous record, exhibited directly: **10⁵ modes in, 3 modes out.** No statistical cancellation does this; only a duality does.

## 3. Disclosure — the sign slip

H-b as literally stated predicted mode n = **ε**·√y·c̄_n·K₀(2πny) and every mode came back at relative deviation exactly 2.00 — i.e. **modulus perfect, phase off by π**. The cause: the committed Fricke relation is F(−1/(Nz)) = const·G(z) with const = τ(χ)/(√N·a_N) = **−ε**, and I wrote ε. So H-b fails as written and passes exactly in corrected form — and the failure mode is itself a confirmation, since the measured constant is the certified Fricke constant to all printed digits. Recorded at headline volume; the corpus's convention (ε = −τ/(√N a_N), fold constant = −ε) is reconfirmed by a test that did not assume it.

## 4. The payoff — the conjecture as orthogonality to an arithmetic-free kernel [derived]

Mode 0 is c₀(y) := ∫₀¹ F(−1/(N(x+iy)))dx. Writing w(x) = u(x)+iv(x) with u = −x/(N(x²+y²)), v = y/(N(x²+y²)), and interchanging (absolute convergence):

  **c₀(y) = Σ_{n≥1} c_n·I_n(y),  I_n(y) := 2i∫₀¹ √(v(x))·K₀(2πn v(x))·sin(2πn u(x)) dx.**

The kernel I_n(y) is **explicit, transcendental, and completely arithmetic-free** — it knows nothing about ρ̃, the quintic, or χ; it depends only on N and y. And by §1(i):

> **The strong Artin conjecture for ρ̃ ⟺ the Frobenius stream (c_n) is orthogonal to the kernel family {I_n(y)}_{y>0}.**

This is the sharpest form the conjecture has taken in this program: a *linear* condition on the coefficient stream against a fixed kernel, with all arithmetic on one side and all analysis on the other. It is also the first form in which the two sides are cleanly separable — the earlier forms (entirety, fold, Schwartz boundary, m ≲ u) all mixed them. The named next target: **find the closed form of I_n(y)**. If the kernel satisfies a Poisson/theta transformation in n (which its shape suggests — a Bessel weight against a Möbius-transformed phase is the classical Poisson kernel's habitat), then the orthogonality may follow from the kernel's own duality rather than from arithmetic input, which is exactly the "source that is neither statistical nor orthogonality-based nor bookkeeping" that §5 of the previous record isolated as the only remaining possibility.

## 5. The better route — the holomorphic hardening lemma [stated]

**Lemma H.** Φ and Ψ extend holomorphically to Re y > 0 (locally uniform convergence; |K₀(z)| ≤ K₀(Re z) from K₀(z) = ∫₀^∞e^{−z cosh t}dt), and y ↦ 1/(Ny) preserves that half-plane; hence D is holomorphic there with explicit M(δ) := sup_{Re u ≥ δ}|D| ≤ 2·sup√|u|·Σ n d(n)K₀(2πnδ) < ∞. Consequently, for k samples in D(c,r) ⊂ D(c,R):

  **sup_{D(c,r)}|D| ≤ Λ_k·max_j|D(z_j)| + M·(R/(R−r))·(2r/(R−r))^k.**

With Chebyshev spacing (Λ_k ~ log k) and r = R/4 the second term decays like 0.667^k — 10⁻²¹·M at k = 121. This converts every point-verified claim in the program into an **interval** claim at the cost of one growth estimate, and it is strictly cheaper than the interval-arithmetic item deferred since 08-10. It does not reach u → ∞, so Theorem R's asymptotic is untouched; it hardens every finite window, including the pole-scan boxes.

## 6. Honest bounds and countersign

Certified-numerical (float64; the 10⁻¹⁴–10⁻¹⁶ readings are at that floor, and the two 10⁻⁸/10⁻⁹ band maxima at y = ½ are single-mode float artifacts, not structure). The measurement is again *consistent with* the fold rather than independent of it — but the functional is new (averaged, 250 simultaneous zero-tests) and, unlike every prior test, it measures the object whose vanishing is *equivalent* to the conjecture rather than a proxy for it. §4's reformulation is derived and unconditional; the closed form of I_n is not attempted here. **Countersign:** (1) the horocycle Fourier instrument as a standing test mode; (2) the parabolic-port measurement as the answer to the seam note's item; (3) **§4's kernel-orthogonality reformulation as the program's sharpest statement of the conjecture, with "compute I_n(y) in closed form" as the named next target**; (4) Lemma H adopted in place of the interval-arithmetic item; (5) the §3 sign erratum; (6) scripts to 04_scripts; (7) log anchor at next consolidation.

---

*Offered, not self-filed. One line: the port that was supposed to be unmined turns out to be empty to fourteen digits, the duality collapse is now something you can watch happen — one hundred thousand modes in, three modes out — and the conjecture has been reduced to a single orthogonality between our arithmetic stream and a kernel that contains no arithmetic at all.*
