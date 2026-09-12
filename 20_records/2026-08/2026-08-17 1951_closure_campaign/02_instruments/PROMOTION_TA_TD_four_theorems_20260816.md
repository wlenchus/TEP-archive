# PROMOTION — T-A/T-B/T-C/T-D: four theorem-grade statements on Φ(y), with proofs, explicit constants, and located caps — 2026-08-16

*Session external to both August lineages; charge: promote three on-record working-note statements (plus the easy direction) to theorem grade. All Bessel identities, group data, and inequalities below were verified this session (mpmath dps 30 / exact icosian arithmetic / scipy quadrature); every numerical claim is reproducible from `/home/claude/promo/v1–v6*.py`. Model-based numbers (Chebotarev-sampled coefficients) are flagged as MODEL — the actual 1951-field coefficient tables were not available to this session. Offered, not self-filed.*

## 0. Object, normalization, standing facts

Φ(y) = √y · Σ_{n≥1} n c_n K₀(2πny), with (c_n) multiplicative, c_1 = 1, |c_n| ≤ d(n). Ladder unit: G = y^{−1/2}; trivial tier G³ = y^{−3/2}, random tier G² = y^{−1}, criterion G = y^{−1/2}. Write L = log(1/y), t_n = n c_n K₀(2πny), S₁ = Σ|t_n|, S₂ = (Σ|t_n|²)^{1/2}, γ = Euler's constant, φ = (1+√5)/2.

**Lemma 0 (K-Bessel toolkit; all verified to 20+ digits).**
(a) ∫₀^∞ u^μ K_ν(u) du = 2^{μ−1}Γ((1+μ+ν)/2)Γ((1+μ−ν)/2) (μ+1 > |ν|). In particular ∫ uK₀ = 1, ∫ u²K₁ = 2, ∫ u³K₁ = 3π/2.
(b) ∫₀^∞ u² (ln u) K₁(u) du = 2ln2 + 1 − 2γ = 1.2318630…
(c) ∫₀^∞ u^{s−1}K₀(u)² du = (√π/4)Γ(s/2)³/Γ((s+1)/2); in particular ∫ uK₀² = 1/2, ∫ u²K₀² = π²/32 = 0.30842514…, ∫ K₀² = π²/4.
(d) ∫₀^∞ u³K₀(u)K₁(u) du = (3/2)∫u²K₀² = 3π²/64 (integrate d(K₀²)/du = −2K₀K₁ by parts).
(e) K₁(u) < 1/u for all u > 0. Proof: (uK₁(u))′ = −uK₀(u) < 0 and uK₁(u) → 1 as u → 0⁺.
(f) √(π/2x)·e^{−x}(1 − 1/(8x)) ≤ K₀(x) ≤ √(π/2x)·e^{−x} for all x > 0, and K₀(x) ≤ √(π/2x)e^{−x}(1 − 1/(8x) + 9/(128x²)); the asymptotic series for K₀ is enveloping (Watson §7.34: remainder has the sign of, and is majorized by, the first omitted term). Verified at x ∈ [0.5, 31.4].
(g) K₀(x) ≥ log(2/x) − γ for 0 < x ≤ 2e^{−γ} (from K₀ = −(log(x/2)+γ)I₀(x) + Σ_{k≥1} H_k x^{2k}/(4^k k!²): both correction terms are ≥ 0 in this range, I₀ ≥ 1).
(h) K₀ is positive and strictly decreasing; K₀(x) ≤ (1/2)x^{−1/2}√π·e^{−x}·(2π-form used below: K₀(2πny) ≤ (1/2)(ny)^{−1/2}e^{−2πny}).

---

## Theorem A (trivial tier, explicit and sharp).

**Hypothesis: |c_n| ≤ d(n) only** (c₁ = 1 and multiplicativity are not needed). Then for all 0 < y ≤ 1/(2π):

  |Φ(y)| ≤ (1/(4π²)) · y^{−3/2} · (log(1/y) + 1).

The constant 1/(4π²) is optimal in the class: for c_n = d(n),
  Φ(y) = (1/(4π²)) y^{−3/2}(log(1/y) + γ − log π) + O(y^{−1/2}),
so no bound c·y^{−3/2}(L+O(1)) with c < 1/(4π²) can hold on the class. Consequently, for 0 < ε ≤ 1/(1+log 2π), |Φ(y)| ≤ C(ε) y^{−3/2−ε} with C(ε) = e^{ε−1}/(4π²ε).

**Proof.** (i) A(t) := Σ_{n≤t} n d(n) = Σ_{ab≤t} ab = Σ_{a≤t} a Σ_{b≤⌊t/a⌋} b ≤ Σ_{a≤t} a·(1/2)(t/a)(t/a + 1) = (t²/2)Σ_{a≤t}1/a + (t/2)⌊t⌋ ≤ (t²/2)(log t + 2) for t ≥ 1; and A(t) = 0 ≤ (t²/2)(log₊t + 2) for 0 < t < 1, so A(t) ≤ (t²/2)(log₊ t + 2) for all t > 0.
(ii) Since K₀(2πy·) is smooth, decreasing, exponentially small at ∞, Riemann–Stieltjes partial summation gives Σ_n n d(n)K₀(2πny) = ∫₀^∞ K₀(2πyt) dA(t) = 2πy ∫₀^∞ A(t) K₁(2πyt) dt (boundary terms vanish; K₀′ = −K₁).
(iii) Insert (i), substitute u = 2πyt, and use log₊(u/(2πy)) ≤ log(1/(2πy)) + log₊u (valid for 2πy ≤ 1):
 Σ ≤ (1/2)(2πy)^{−2} ∫₀^∞ u²(log₊(u/(2πy)) + 2) K₁(u) du ≤ (1/2)(2πy)^{−2}[ (log(1/(2πy)) + 2)·2 + ∫₀^∞ u² log₊u · K₁(u) du ].
By Lemma 0(b,e), ∫ u² log₊u K₁ du = ∫ u² ln u K₁ du + ∫₀^1 u²(−ln u)K₁ du ≤ (2ln2+1−2γ) + ∫₀^1 u(−ln u)du = 2ln2 + 1 − 2γ + 1/4 = 1.48186….
(iv) Collect: Σ_n n d(n)K₀(2πny) ≤ (2πy)^{−2}[ log(1/(2πy)) + 2 + 0.74093 ] = (2πy)^{−2}[ L − log 2π + 2.74093 ] ≤ (2πy)^{−2}(L + 1), since log 2π = 1.83788 > 1.74093. Multiply by √y. ∎ (numerics: bound holds with ratio 0.46–0.85 on y ∈ [10⁻⁴, 0.159], ratio ↑ 1 as y ↓ 0.)
**Sharpness.** Mellin: ∫₀^∞ Σn d(n)K₀(2πny) y^{s−1}dy = (2π)^{−s}2^{s−2}Γ(s/2)²ζ(s−1)². The double pole at s = 2 has expansion (2π)^{−2}y^{−2}(L + γ − log π) (residue computation using ζ(1+w) = 1/w + γ + O(w), Γ(1+w/2)² = e^{−γw+O(w²)}); shifting the contour to Re s = 3/2 past no other poles gives the O(y^{−3/2}) Mellin remainder, i.e. O(y^{−1/2}) for Φ. Verified: 4π²y²Σ at y = 10⁻⁴ equals 8.642826 against predicted L + γ − log π = 8.642826 (6 digits). ∎

*Cap: none. T-A is closed, with the ε-free form strictly stronger than the on-record ≪_ε y^{−3/2−ε}.*

---

## Theorem B (the incompressibility law, promoted honestly).

**B1 (universal lower bound — no arithmetic input).** Assume |c_n| ≤ d(n) and c₁ = 1. Then for all 0 < y ≤ 1/(2π):

  S₂/S₁ ≥ (1/2) √( πy / (2 log(1/y) + 1) ).

**Proof.** Let T = ⌈2L/(πy)⌉. Cauchy–Schwarz on n ≤ T: Σ_{n≤T}|t_n| ≤ √T·S₂. Tail: by Lemma 0(h) and nd(n) ≤ n², Σ_{n>T}|t_n| ≤ (1/2)y^{−1/2}Σ_{n>T} n^{3/2}e^{−2πny}. The summand decreases for n ≥ 3/(4πy) (≤ T since L ≥ log 2π), so the sum is ≤ ∫_T^∞ t^{3/2}e^{−2πyt}dt ≤ e^{−2πyT}·√2[T^{3/2}/(2πy) + Γ(5/2)/(2πy)^{5/2}] using (T+s)^{3/2} ≤ √2(T^{3/2}+s^{3/2}). With e^{−2πyT} ≤ e^{−4L} = y⁴ this gives Σ_{n>T}|t_n| ≤ y(0.0572·L^{3/2} + 0.0095), which is ≤ (1/2)(L − log π − γ) ≤ (1/2)K₀(2πy) ≤ (1/2)S₁ for all y ≤ 1/(2π) (Lemma 0(g); the extreme case y = 1/(2π): 0.0333 < 0.0580; LHS increases and RHS decreases in y, so the endpoint is the worst case; c₁ = 1 gives S₁ ≥ |t₁| = K₀(2πy)). Hence S₁ ≤ √T S₂ + S₁/2, so S₂/S₁ ≥ 1/(2√T) ≥ (1/2)√(πy/(2L+1)). ∎ (numerics: holds with factor 3.5–6.8 of slack on the extremal c = d; equality-order not claimed.)

This is the incompressibility statement in pure form: the K₀-window at height y has effective dimension T ≍ y^{−1}L, and no magnitude pattern below the divisor bound can spread ℓ¹-mass beyond √dimension times the ℓ²-mass. The ratio can never fall below the √y-tier by more than √L — for any coefficients whatsoever.

**B2 (two-sided ≍ √y under matched hypotheses; explicit constants).** Assume |c_n| ≤ d(n), c₁ = 1, and
 (U2) Σ_{n≤X}|c_n|² ≤ Δ²X for all X ≥ 1;
 (L1) Σ_{X<n≤2X}|c_n| ≥ δ₁X for all X ≥ X₀;
 (L2) Σ_{X<n≤2X}|c_n|² ≥ δ²X for all X ≥ X₀.
Then for 0 < y ≤ min(0.0849/X₀, 1/(2π)):
 (upper, from (U2)+(L1)):  S₂/S₁ ≤ 20.03 · (Δ/δ₁) · √y ;
 (lower, from (L2)):    S₂/S₁ ≥ 0.374 · δ · √y / (log(1/y) + 1).
**Proof.** Upper: B(t) := Σ_{n≤t}n²|c_n|² ≤ t²·Δ²t = Δ²t³; Stieltjes against the decreasing K₀²: S₂² = ∫K₀(2πyt)²dB ≤ 4πyΔ²∫t³(K₀K₁)(2πyt)dt = 4πyΔ²(2πy)^{−4}·(3π²/64) = (3/(256π))Δ²y^{−3} (Lemma 0(d)). For S₁, take one block X = a/y with a = 0.12356 (maximizing a²K₀(4πa) = 0.003049): S₁ ≥ Σ_{X<n≤2X} n|c_n|K₀(2πny) ≥ X·K₀(4πXy)·δ₁X = 0.003049·δ₁y^{−2}. Ratio: √(3/(256π))/0.003049 = 20.03. Lower: one block at a = 0.08495 (maximizing a³K₀(4πa)² = 8.9744·10⁻⁵): S₂² ≥ δ²·a³K₀(4πa)²y^{−3}, so S₂ ≥ 0.009473·δ·y^{−3/2}; and S₁ ≤ Σ n d(n)K₀ ≤ (2πy)^{−2}(L+1) (Theorem A, step iv). Ratio constant: 0.009473·4π² = 0.374. ∎

**B3 (weakest arithmetic input, graded).** The lower bound in the √y-tier needs only (L2) — a dyadic mean-square lower bound — and (L2) is the weakest natural input: with no lower hypothesis the ratio can be 1 (c_n = 0 for n ≥ 2, S₂/S₁ ≡ 1), and with only prime-supported Chebotarev input (Σ_{X<p≤2X}|c_p|² ≫ X/log X) one gets the intermediate S₂/S₁ ≫ δ√y/(L+1)^{3/2}. The ratio upper bound in the clean √y-tier needs (L1) — an ℓ¹ linear lower bound — and this is exactly where the icosahedral case fails to be clean (B4(iii)).

**B4 (icosahedral instantiation: exact class data, corrections, and the located cap).**
(i) *Image and densities (exact; verified by explicit icosian construction of 2.A₅, order 120, and exact ℤ[√5] arithmetic).* If ρ̃ has projective image A₅ and determinant of order 5, then by Goursat (2.A₅ is perfect; C₅ abelian; no common quotient) the image is the full direct product 2.A₅ × C₅, and since the C₅ factor is central unimodular it does not move |tr|. The |a_p| distribution over unramified p (Chebotarev) is exactly:
  |a_p|:  2   1   0   φ   1/φ
  density: 1/60 1/3 1/4 1/5 1/5
(signed classes: ±2 ↦ 1+1, +1 ↦ order-6 (20), −1 ↦ order-3 (20), 0 ↦ order-4 (30), traces −φ, +1/φ ↦ order-5 (12+12), +φ, −1/φ ↦ order-10 (12+12).)
**Correction to the record:** density(|a_p| ≥ 1) = 1/60 + 1/3 + 1/5 = **11/20 = 0.55**, not 19/30 ≈ 0.633. No natural count of these classes produces 19/30; the likeliest source of the garble is the *exponent* constant below, 1 − κ = (19 − 6√5)/30, whose displayed integers are 19 and 30. Also: density(|a_p| > 0) = 3/4.
(ii) *Moments (exact).* κ := mean|a_p| = (1/120)(2·2 + 40·1 + 24φ + 24/φ) = **(11+6√5)/30 = 0.8138802622**; mean|a_p|² = (1/120)(8 + 40 + 24(φ²+φ^{−2})) = **1 exactly** (⟨χ,χ⟩ = 1; irreducibility). Hence, unconditionally (Chebotarev for the fixed field of ker Ad ρ̃; Brauer meromorphy; classical holomorphy and nonvanishing of Artin L-functions on Re s = 1; Ad ρ̃ is the 3-dimensional irreducible with image A₅, unchanged by the C₅ twist):
  Σ_n |c_n|² n^{−s} = ζ(s)·L(s, Ad ρ̃)·ζ(2s)^{−1}·E_N(s)  (E_N the p = N Euler correction, |a_N| = 1),
which is holomorphic and nonvanishing on Re s ≥ 1 except the simple pole at s = 1; Wiener–Ikehara gives Σ_{n≤X}|c_n|² = C_RS·X(1+o(1)) with C_RS = L(1,Adρ̃)·E_N(1)/ζ(2) ∈ (0,∞). **So (U2) and (L2) hold unconditionally** (any Δ² > C_RS > δ², X ≥ X₀), and B1, B2-lower, B3 all apply to the icosahedral Φ with no unproven input.
(iii) *The located cap: the clean ≍ √y is false as a strict asymptotic.* Since κ < 1, Wirsing/Selberg–Delange (Σ|c_n|n^{−s} = ζ(s)^κ H(s), H holomorphic ≠ 0 near s = 1 by Chebotarev with classical zero-free regions) gives
  Σ_{n≤X}|c_n| = c₁* · X (log X)^{κ−1} (1 + O(1/log X)),  c₁* = H(1)/Γ(κ) > 0,
so S₁ = c₁*(2πy)^{−2}(log(1/(2πy)))^{κ−1}(1+o(1)) while S₂ = (C_RS π²/32)^{1/2}(2πy)^{−3/2}(1+o(1)). Therefore the true law is
  **S₂/S₁ = (π^{3/2}/4)·(√C_RS / c₁*) · √y · (log(1/(2πy)))^{1−κ} · (1+o(1)),  1−κ = (19−6√5)/30 = 0.1861197…**
The on-record "S₂/S₁ ≍ √y" survives promotion only as: (a) the two-sided bound √y/(L+1) ≪ S₂/S₁ ≪ √y·L^{1−κ} (unconditional), i.e. S₂/S₁ = y^{1/2+o(1)}; and (b) an exact asymptotic with the slowly-varying factor L^{0.18612} attached. The "constant" c in S₂/S₁ = c√y is not a constant; it drifts by (log ratio)^{0.18612} ≈ +24% per two decades of y.
(iv) *Reconciliation of the measured c ≈ 2.23 and of the moment assembly.* The correct assembly is
  c(y) = √(2π) · ( ∫u²K₀(u)²du · A₂ )^{1/2} / ( ∫uK₀(u)du · A₁(y) ) = (π^{3/2}/4)·√A₂/A₁(y),
with A₂ = C_RS and A₁(y) = c₁*(log(1/(2πy)))^{κ−1} the *effective* first moment at depth y. Two normalization corrections to the working note: the S₂ weight is u²K₀² with ∫u²K₀² = π²/32 (the note's ∫uK₀² = 1/2 is a true identity but the wrong moment — using it misassembles c by 4/π ≈ 1.27); and the √(2π) arises from (2πy)^{−3/2}/(2πy)^{−2} = (2π)^{1/2}y^{1/2} — with both in place the K-moment prefactor is π^{3/2}/4 = 1.3925. MODEL (six Chebotarev-sampled coefficient sets, n ≤ 6·10⁴, exact Chebyshev lifts c_{p^k} = U_k, ramified 1951 degree-1): at the deep end y = 6·10⁻⁴ ≈ 1.17/N the direct measurement gives c(y) = 2.27 ± 0.23 — **the on-record 2.23 sits at the center of the ensemble**; the drift across y ∈ [6·10⁻⁴, 0.1] measures 2.273/1.823 = 1.247 against the Selberg–Delange prediction (log ratio)^{1−κ} = 1.243 (agreement to 0.3%); and the assembled formula with truncated averages A₁ ≈ 0.43, A₂ ≈ 0.55 reproduces c = 2.2–2.4. The ±10% seed spread is real, not noise: c₁* and C_RS depend on the actual Frobenius classes at small primes (the 1/p-sums converge slowly), so the exact constant for conductor 1951 requires the field's own coefficient table — the model certifies the *structure* and brackets the value. ∎

*Cap on T-B, stated exactly: promoted as B1 + B2 + B4(iii). What resists: a clean two-sided c₁√y ≤ S₂/S₁ ≤ c₂√y for the icosahedral coefficients themselves — provably unavailable, since the sharp law carries (log 1/y)^{(19−6√5)/30}. The measured 2.23 is the local value of that slowly-varying prefactor near Ny = 1, now derived and reconciled.*

---

## Theorem C (the random tier and the exclusion).

Fix magnitudes μ = (μ_n), μ_n ≤ d(n), μ₁ = 1, and let (ε_n) be i.i.d. Haar on the unit circle; set Φ_ε(y) = √y Σ n μ_n ε_n K₀(2πny). (Multiplying any fixed unimodular phases into ε_n leaves the law invariant, so this is exactly "c_n with independent uniform random phases.")

**C1 (second and fourth moments; the ladder value of the random tier).** Exactly:
  E|Φ_ε(y)|² = y Σ_n n²μ_n²K₀(2πny)² = y·S₂(y)²,  E|Φ_ε(y)|⁴ = y²(2S₂⁴ − Σ_n n⁴μ_n⁴K₀⁴) ≤ 2(E|Φ_ε|²)².
Under (L2)+(U2) (icosahedral: unconditional by B4(ii)):
  8.97·10⁻⁵·δ² · y^{−2} ≤ E|Φ_ε(y)|² ≤ (3/(256π))Δ²·y^{−2}  for y ≤ min(0.0849/X₀, 1/(2π)),
with the asymptotic E|Φ_ε(y)|² = C_RS·(π²/32)·(2π)^{−3}·y^{−2}(1+o(1)) = (C_RS/(256π))·y^{−2}(1+o(1)). **This confirms rigorously the on-record ladder entry: the random tier is G² = y^{−1}** (rms Φ_ε ≍ y^{−1}; MODEL check: y²·E|Φ_ε|² ≈ 6.6·10⁻⁴ flat over y, MC/theory = 1.00 ± 0.02; fourth-moment identity verified by MC to 2%).

**C2 (almost-sure upper bound: the random tier is not exceeded).** Assume μ_n ≤ d(n). Almost surely there is Y₀(ω) > 0 such that for all y ≤ Y₀:
  |Φ_ε(y)| ≤ 5 (E|Φ_ε(y)|²·log(1/y))^{1/2} + 1 ≤ C y^{−1}(log(1/y))², and under (U2): ≤ C′ y^{−1}(log(1/y))^{1/2},
in particular a.s. Φ_ε(y) = O(y^{−1−ε}) for every ε > 0.
**Proof.** Hoeffding on real and imaginary parts (independent, mean 0, |Re(a_nε_n)| ≤ |a_n|): P(|Φ_ε(y)| ≥ λ√(yS₂²)) ≤ 4e^{−λ²/4}. Deterministic oscillation control: |Φ_ε′(y)| ≤ (2√y)^{−1}Σnd(n)K₀ + 2π√yΣn²d(n)·nK₁(2πny) ≤ Ky^{−4} for y ≤ 1/(2π) (Lemma 0(a): ∫u³K₁ = 3π/2; crude d(n) ≤ n). Take the net y_{j,i} = 2^{−j}(1 + i·2^{−j·4}), i.e. spacing y⁵ within each dyadic block: at most y^{−4} points per block; λ_j = 5√(log 2^{j+1}) gives block failure probability ≤ 4·2^{4j}·e^{−λ_j²/4} = 4·2^{4j}·2^{−25(j+1)/4} ≤ 4·2^{−9j/4}, summable; Borel–Cantelli, plus |Φ_ε(y) − Φ_ε(net)| ≤ Ky⁵·y^{−4} = Ky. The stated forms follow from S₂² ≤ (3/(256π))Δ²y^{−3} under (U2), and in general from Σ_{n≤X}d(n)² = Σ_{a,b}⌊X/[a,b]⌋ ≤ X(log X + 1)³ (since Σ_{a,b≤X}1/[a,b] ≤ Σ_{g≤X}(1/g)(Σ_{m≤X}1/m)²), whence S₂² ≤ Cy^{−3}(L+1)³ by the B2 Stieltjes argument. ∎

**C3 (almost-sure lower bound: the random tier is attained).** Assume (L2) with constant δ (icosahedral: unconditional). Then almost surely
  limsup_{y→0} y·|Φ_ε(y)| ≥ (1/2)·(8.9744·10⁻⁵)^{1/2}·δ = 0.004737·δ > 0.
**Proof.** Λ := limsup_{y→0} y|Φ_ε(y)| is measurable w.r.t. the tail σ-field of (ε_n): changing ε_1,…,ε_M changes y|Φ_ε(y)| by at most 2y^{3/2}Σ_{n≤M}nd(n)K₀(2πny) ≤ C_M y^{3/2}log(1/y) → 0. By Kolmogorov's 0–1 law Λ is a.s. constant. Paley–Zygmund with C1's fourth moment (E|Z|⁴ ≤ 2(E|Z|²)²): for each y, P(|Φ_ε(y)|² ≥ (1/4)E|Φ_ε(y)|²) ≥ (3/4)²/2 = 9/32. Along y_k → 0, P(Λ ≥ (1/2)liminf (y_k³S₂(y_k)²)^{1/2}) ≥ limsup_k P(A_k) ≥ 9/32 > 0 (Fatou for limsup of events), and y³S₂² ≥ 8.9744·10⁻⁵δ² by the B2-lower block. A tail event of positive probability has probability 1. ∎
Together, C2+C3: **a.s. the random-phase object sits exactly at the random tier**, y^{−1} = G², up to sub-polynomial factors — sharp in both directions.

**C4 (the exclusion, citable form).** *Definition.* Fix magnitude data μ (μ_n ≤ d(n), μ₁ = 1) and let P_μ be the law of (μ_nε_n) with (ε_n) i.i.d. Haar on the circle. A function B: (0,y₀] → (0,∞) is a **phase-blind (measure-theoretic) bound** for μ if P_μ( |Φ_ε(y)| ≤ B(y) for all y ∈ (0,y₀] ) > 23/32. (This class contains every bound derived from: the values |c_n| alone; any statistic of the Chebotarev/Sato–Tate distribution of |a_p|; Rankin–Selberg mean squares; and any "square-root cancellation of Σ c_n e(nθ)"-type input transferred through the K₀ weight — since square-root cancellation holds P_μ-a.s., such derivations prove their conclusion P_μ-a.s. or with high P_μ-probability, uniformly in the phases.)
**Theorem.** If μ satisfies (L2) with constant δ, then every phase-blind bound satisfies
  limsup_{y→0} y·B(y) ≥ 0.004737·δ.
In particular B(y) = o(y^{−1}) is impossible, and the criterion tier B(y) ≪ y^{−1/2} = G is unreachable by a margin of exactly one factor of G.
**Proof.** By C3 the event {limsup y|Φ_ε| ≥ 0.004737δ} has probability 1 ≥ 9/32; if B were phase-blind with limsup yB < 0.004737δ, the two events (each of P_μ-probability > 23/32 and ≥ 9/32… ) would be disjoint with total probability > 1. ∎
**Corollary (null-set form).** For μ satisfying (L2), the set { phase vectors φ ∈ 𝕋^∞ : Φ_φ(y) = O(y^{−1/2}) } is P_μ-null. *If the icosahedral Φ satisfies the criterion, its Frobenius phase vector lies in a set of measure zero for the magnitude ensemble: the criterion is not a property of the distribution of the |c_n| — it is a property of their ordering.* No refinement of Chebotarev one-point statistics, however sharp, changes this: the exclusion is information-theoretic, not technical. ∎

*Cap: none within the stated class. The class definition deliberately excludes inputs that correlate phases at distinct n (shifted convolutions, functional-equation/trace-formula identities, multiplicative long-range rigidity used as a joint constraint): those are exactly the inputs the exclusion certifies as necessary.*

---

## Theorem D (the easy direction: exact deep-boundary asymptotic under automorphy).

**Hypothesis (FOLD).** There exist N ≥ 1, ε with |ε| = 1, and dual coefficients (b_n) with b₁ = 1, |b_n| ≤ d(n), such that with Ψ(u) = √u Σ_{n≥1} n b_n K₀(2πnu):
  Φ(1/(Nu)) = ε·N·u²·Ψ(u)  for all u ≥ 1  (defect ≡ 0).
(Provenance: if F(z) = √y Σ_{n≠0} c_{|n|}sgn(n) K₀(2π|n|y)e(nx) is an odd eigenvalue-¼ Maass form with Fricke fold F(−1/(Nz)) = −ε·G(z), then ∂_x at x = 0, z = iy, with (d/dz)(−1/(Nz)) = −1/(Ny²) at z = iy, gives exactly FOLD for Φ = (4πi)^{−1}∂_xF(iy) with the committed fold constant −ε; for the record's even case the same computation applies to the odd derivative object. Here FOLD is taken as the hypothesis, exactly as certified on-record.)

**Theorem.** Under FOLD, for all 0 < y ≤ 1/N, writing u = 1/(Ny):
  **Φ(y) = (ε/(2N)) · y^{−2} · e^{−2π/(Ny)} · [ 1 − 1/(16πu) + r(u) ],  |r(u)| ≤ 9/(512π²u²) + 2.84·e^{−2πu}.**
In particular Φ(y) = (ε/(2N))y^{−2}e^{−2π/(Ny)}(1 + O(Ny)), and |Φ(y)| → 0 faster than any power of y.
**Proof.** Ψ(u) = √u·K₀(2πu) + √u·R with |R| ≤ Σ_{n≥2}nd(n)K₀(2πnu) ≤ (1/(2√u))Σ_{n≥2}√n d(n)e^{−2πnu} (Lemma 0(h)) ≤ (1/(2√u))e^{−4πu}·Σ_{n≥2}√n d(n)e^{−2π(n−2)} = (1/(2√u))e^{−4πu}·C* with C* = 2√2 + 2√3e^{−2π} + … < 2.836 (computed; series dominated by its first term). For the main term, Lemma 0(f) (enveloping series): √u·K₀(2πu) = (1/2)e^{−2πu}(1 − 1/(16πu) + θ·9/(512π²u²)), θ = θ(u) ∈ [0,1]. Hence Ψ(u) = (1/2)e^{−2πu}[1 − 1/(16πu) + r], |r| ≤ 9/(512π²u²) + 2·1.418·e^{−2πu}. Multiply by εNu²: since u = 1/(Ny), Nu² = 1/(Ny²), so εNu²Ψ(u) = (ε/(2N))y^{−2}e^{−2π/(Ny)}[1 − 1/(16πu) + r]. ∎ (numerics, MODEL dual: the bracket matches 1 − 1/(16πu) within the stated |r| bound at every u ∈ {1,…,8}; e.g. u = 5: η_measured = −3.9099·10⁻³ vs −1/(80π) = −3.9789·10⁻³, difference 6.9·10⁻⁵ < 7.1·10⁻⁵ = bound.)

**Corollary D1 (reconciliation of the 0.4% deep-boundary verification).** A measurement comparing Φ(y) to the bare leading term (ε/(2N))y^{−2}e^{−2π/(Ny)} at depth u = 1/(Ny) = 5 must find a deficit of 1/(16π·5) = 0.398%, with everything beyond that bounded by 7.1·10⁻⁵. The on-record 0.4% agreement is therefore not measurement error: it *is* the next-to-leading Bessel term, predicted to two more digits by the two-term formula above. (If the record's depth was other than u ≈ 5, the two-term formula supplies the prediction at any u ≥ 1.)

**Corollary D2 (the easy direction, stated exactly).** FOLD ⇒ |Φ(y)| ≤ (1/(2N))y^{−2}e^{−2π/(Ny)}·(1 + 0.03) for y ≤ 1/(2N) ⇒ the criterion |Φ(y)| ≪ y^{−1/2} holds with room to spare: automorphy does not merely reach the criterion tier G, it collapses Φ to exponential decay — every power tier at once. The transition happens exactly at Ny = 1 (u = 1), where the dual n = 1 mode takes over: this is the on-record two-regime boundary, now with its constant and error term. ∎

*Cap: none. T-D is closed; the fold does all the work, and the 0.4% is now an identity, not a residual.*

---

## Closing: what T-A–T-D jointly pin down, and the missing statement

Measured in the ladder unit G = y^{−1/2}: T-A proves the magnitude data alone cap Φ at G³·log, with the extremal constant 1/(4π²) attained — no measure-theoretic refinement below the divisor bound moves the trivial tier. T-C proves that *every* phase-blind method — anything consuming only the distribution of the |c_n| plus exchangeable or independent phases, which includes all square-root-cancellation inputs — lands exactly on G², almost surely and two-sidedly: the random tier is a floor, not a technique deficit. T-B locates why: through the K₀ window the ℓ¹/ℓ² geometry is incompressible — S₂/S₁ = y^{1/2+o(1)} with the exact slowly-varying law (π^{3/2}/4)(√C_RS/c₁*)L^{(19−6√5)/30}√y — so cancellation harvested magnitude-blind is worth exactly one factor of G below trivial and no more. T-D proves automorphy delivers not the criterion tier G but exponential collapse, with the 0.4% measurement now an identity. The criterion G therefore sits strictly inside the gap that only ordering information can cross: **one factor of G of coherence**, exactly as the two threads' independent negatives (C-3) asserted.

What a proof of |Φ(y)| ≪ y^{−1/2} must supply, written as sharply as I can make it. Let
  D(y) = Σ_{n≥1} n²|c_n|² K₀(2πny)²,  O(y) = Σ_{n≠m} nm c_n c̄_m K₀(2πny)K₀(2πmy),
so |Φ(y)|² = y·(D(y) + O(y)) ≥ 0, and unconditionally D(y) = (C_RS π²/32)(2πy)^{−3}(1+o(1)) (B4(ii)).

**Conjecture (COH — the one-factor-of-G coherence law).** There exist C > 0 and y₀ ∈ (0, 1/N] such that
  for all y ∈ (0, y₀]:  0 ≤ 1 + O(y)/D(y) ≤ C·y.
Equivalently: for every y ≤ y₀ the off-diagonal Frobenius correlation sum O(y) — a shifted-convolution sum Σ_{h≠0} Σ_n c_n c̄_{n+h} w_y(n,h) against the explicit positive kernel w_y(n,h) = n(n+h)K₀(2πny)K₀(2π(n+h)y) — equals −D(y) to relative precision Cy: total anticoherence, "cos Δ = −1 + O(y)" in the corpus dictionary. Quantifier accounting: (COH) ⟺ |Φ(y)|² ≤ C·y·D(y)·(1+o(1)) ≍ y^{−2}·y·… ⟺ |Φ(y)| ≪ y^{−1/2} — it *is* the criterion, rewritten to expose its information content. Against the baselines: the random-phase ensemble has E[1 + O/D] = 1 with O(1) fluctuations (T-C: this is G²); (COH) demands suppression to O(y) = O(G^{−2}), i.e. one factor of G on amplitudes; and FOLD implies (COH) overwhelmingly, with 1 + O(y)/D(y) = |Φ(y)|²/(y·D(y)) ≤ C′·y^{−2}·e^{−4π/(Ny)} → 0 faster than any power (T-D). (COH) is thus strictly implied by automorphy, strictly unreachable phase-blind (T-C4: the set where it holds is P_μ-null), and exactly equivalent to the criterion given the unconditional diagonal asymptotic. It is the minimal ordering statement the ladder leaves open: two-point, sign-definite, window-explicit — one factor of G of coherence, no more, and provably no less.

*Verification artifacts: v1 (moments, envelopes, K₁ < 1/u), v2 (T-A bound + Mellin constant γ − log π to 6 digits), v3 (exact 2.A₅ icosian table; 11/20; κ; mean square 1), v4 (MODEL c(y): 2.27 ± 0.23 at y = 6·10⁻⁴ vs record 2.23; drift 1.247 vs predicted 1.243), v5 (E|Φ_ε|² = yS₂² MC; fourth moment; T-D bracket vs bound at u = 1…8; u = 5 ↦ 0.398%), v6 (block-constant optimization; B1 tail constants). Offered, not self-filed.*
