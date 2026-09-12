# Mode-0 Fricke kernel I_n(y): exact structure, expansion law, and the located cap — 2026-08-16

Derivation attempt on the arithmetic-free kernel I_n(y) of the mode-0 (constant-term) functional of F∘(Fricke) on the horocycle Im z = y₀, level N = 1951, eigenvalue 1/4. Conventions re-derived from scratch (the 08-13B horocycle_fourier / ERRATUM_mode0 records were not on disk in this environment). All numerics mpmath dps 30–40; scripts in session workspace (s1–s9).

## Conventions (fixed)
e(t) = e^{2πit}; F(z) = √y Σ_{n≥1} c_n K₀(2πny)·2i sin(2πnx); w(x) = −1/(N(x+iy₀)) = u+iv, u = −x/(N(x²+y₀²)), v = y₀/(N(x²+y₀²)). Termwise integration of c₀(y₀) = ∫₀¹F(w(x))dx is justified by v ≥ y₀/(N(1+y₀²)) > 0 on [0,1] and Σ d(n)e^{−2πn v_min} < ∞. Then c₀(y₀) = Σ c_n I_n(y₀), I_n = 2i·J_n, J_n(y) = ∫₀¹ √v K₀(2πnv) sin(2πnu) dx real; c₀ ∈ iℝ for real c_n.

## Lemma 1 (geometry). 
The horocycle Im z = y maps to the circle |w − i/(2Ny)| = 1/(2Ny) (tangent to ℝ at the cusp 0). With x = y tan(α/2), r = 1/(2Ny), p = πn/(Ny): v = r(1+cos α), u = −r sin α, and
J_n(y) = −(1/2)√(y/N) ∫₀^{α₁} K₀(p(1+cos α)) sin(p sin α) sec(α/2) dα, α₁ = 2 arctan(1/y).
x ∈ [0,1) is exactly a fundamental domain for γ₀ = [1 0; N 1] (x ↦ x+1 ⇔ γ₀⁻¹ on the circle). [Certified: two parametrizations agree ≤ 1e−40, n=1..6, y ∈ {1/2,1,2}.]

## Lemma 2 (parity). 
The full-line integral ∫_ℝ (full circle) vanishes identically: u odd, v even in x. Equivalently Σ_{j∈ℤ}(γ₀-translates of the arc integral) = 0 — the only exact kernel-level duality, holding mode-by-mode; it constrains the γ₀-orbit sum, never the single j = 0 term.

## Theorem 3 (mode expansion; Graf-type law with Whittaker-product coefficients).
On the circle, e^{2πin·u} K₀(2πn·v) = Σ_{m∈ℤ} H_m(p) e^{imα} with
H_m(p) = (−1)^m Γ(1/2 + (|m|−m)/2)/(p·|m|!) · W_{m/2,|m|/2}(p) · M_{m/2,|m|/2}(p)
= (−1)^m ∫₀^∞ e^{−p cosh t} I_{|m|}(p sinh t) coth(t/2)^m dt;  H₀(p) = I₀(p/2)K₀(p/2).
Proof: Laplace rep of K₀ + L¹ truncation (rigorous Fubini), substitution τ = log coth(t/2) (swaps cosh t ↔ coth τ, sinh t ↔ 1/sinh τ, e^τ = coth(t/2)) landing on the classical Whittaker Green's-function transform [GR 6.653.2] in its confluent case x = y = p/2, 2κ = m, 2μ = |m|. [Certificates: t-integral = closed form ≤ 3.5e−36 (m = −8..8, p = 0.3, 1.2, 3.7); Fourier quadrature = closed form ≤ 4.6e−29; GR 6.653.2 at generic (x,y,κ,μ) ≤ 1.2e−41.] For m ≠ 0 no rational-in-p Bessel reduction exists (log p enters via integer-b Kummer U); m = 0 is exactly I₀K₀(p/2).
Consequently (Parseval; kernel ∈ L², test function 1_{[0,α₁]}sec(α/2) bounded):
I_n(y) = i√(y/N) Σ_{m≥1} D_m(p) S_m(α₁), D_m = H_m − H_{−m},
S_m(α₁) = 4 Σ_{ℓ=0}^{m−1} (−1)^{m−1−ℓ} (1 − cos((2ℓ+1)α₁/2))/(2ℓ+1) (elementary; certified 3.4e−41; recursion S_m = 4c_{m−1} − S_{m−1}).
Fast form of D_m via K₀-singularity split (log(2cos(α/2)) Fourier series; certified vs t-integral ≤ 1e−30). Assembled series vs direct quadrature: ~M^{−3} truncation; parity-averaged M = 3·10⁵ agrees to 6.5e−21 absolute (N = 1951, n = 3, y = 1/2; J = −8.140212408100662025522573e−4).

## Theorem 4 (exact ODE with automorphy defect).
y²J_n'' + ¼J_n = −y²[∂ₓg_n(1+iy) − ∂ₓg_n(iy)], g_n = (single-n Whittaker term)∘σ₀. [Certified 4.8e−35.] Eigenvalue 1/4 ⇒ indicial double root: homogeneous solutions √y, √y·log y. The inhomogeneity is exactly the γ₀-periodization defect; it vanishes identically iff F is γ₀-invariant. So c₀(y) = a√y + b√y log y holds iff the defect vanishes — the mode-0 functional is not even a homogeneous-ODE solution absent automorphy.

## Theorem 5 (Mellin: factorization for the half-line object; failure located at the endpoint).
A_n(y) = 2i∫₀^∞(...)dx satisfies A_n(y) = √y·Φ(πn/(Ny)) [scaling certified 2.3e−41], so its y-Mellin transform is (πn/N)^{s+1/2}·γ(s): manifest n-power factorization. For I_n (range [0,1]) the endpoint datum α₁(y) couples n and y after p-substitution (α₁ → 2 arctan(Np/(πn))): no factorization Ĩ_n(s) = n^{−s−...}γ(s). The failing term is the x = 1 endpoint = the γ₀-translate boundary. The Poisson/theta route in n meets the same wall: I_n(y) = √y·Φ_y(πn/(Ny)) is a fixed smooth function sampled at n/(Ny); a summation formula for Σc_nΦ(nδ) requires a functional equation for Σc_n n^{−s}, i.e. the automorphy under test (Voronoi ⇔ automorphy): circular.

## Theorem 6 (cap, decisive form — numerical counterexamples in the hypothesis class).
Systems with full Hecke recursion c_{p^{k+1}} = c_p c_{p^k} − c_{p^{k−1}}, Satake in μ₆₀, |c_n| ≤ d(n):
Σ1: c_p ≡ +1 (ζ₆); Σ2: c_p ≡ −1 (ζ₃); Σ3: c_p = 2cos(2π(p mod 60)/60); Σ1′ = Σ1 with c_{1951} = 1951^{−1/2}.
Σ_{n} c_n J_n(y₀), n ≤ 3·10⁴ (float64 validated vs mpmath ≤ 8.7e−19 per term; rigorous tail bound < 2.6e−12; total error < 1e−11):
y₀ = 1/2: −2.1056031261 (Σ1), +0.0423208320 (Σ2), −3.1784514289 (Σ3), −2.1057140561 (Σ1′)
y₀ = 1: −1.6868613445 (Σ1), +0.0253558347 (Σ2), −1.8519600308 (Σ3), −1.6868370863 (Σ1′)
All nonzero with margins 10⁹–10¹¹ over certified error; distinct across systems. Hence NO kernel transformation law of {I_n} combined only with Hecke relations + μ₆₀ + divisor bound can force Σc_nI_n = 0: such a proof would apply verbatim to Σ1–Σ3. Mode-0 vanishing at cusp 0 is part of the automorphy datum of the specific coefficient system, not a kernel consequence.

## Honest scope
Mode-0 vanishing (even for all y₀) is only the x-average of the single relation F|γ₀ = F; full γ₀-invariance needs all Fourier modes; Γ₀(1951) needs more generators than T, γ₀; converse-theorem certification would need twisted functional equations. For a true odd cuspidal newform the constant term at cusp 0 vanishes identically, so the test has the correct null answer on automorphic input. Caps on the numerics: assembled-series check 17 significant digits (provable O(M^{−3}) truncation), component identities 29–41 digits; GR 6.653.2 cited + verified numerically, not re-proved.
