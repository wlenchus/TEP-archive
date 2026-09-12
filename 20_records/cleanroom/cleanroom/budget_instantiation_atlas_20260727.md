# Budget instantiation atlas — Will's final check, machine-pinned — 2026-07-27 (~22:30Z)

**Method:** every identity below was derived from the settled conventions (x = sin A = tanh η; u = 1−x²; G = 1/√u; SNR = x²/u; amplitude coin (1±x)/2; G_new = 2/(1−x)) and machine-verified this turn at 30–40 dps (all PASS; session shell log). Tier flags: [V-here] derived+verified now; [held] from this session's deep-layer reads; [recon] reconstruction offered for grading — the instantiation record itself unread.

## 1. The chart chain and its Jacobian ladder [V-here]

dA = G·dx, dη = G·dA, hence dη = G²·dx — **each chart ascent is one factor of G**; A = gd(η) (Gudermannian), and the three ledgers ∫dx, ∫G dx (= Fisher–Rao arc of the amplitude coin, per 07-19), ∫G² dx are the x-, angle-, and rapidity-ledgers of one motion. **G = cosh η; xG = sinh η = √SNR** — the "signal amplitude" is sinh of the rapidity. Derivative ladder of the gain: dG/dη = xG (= sinh), dG/dA = xG², dG/dx = xG³; G″ = G³(1+3·SNR); G(0)=1, G′(0)=0, G″(0)=1 — unit curvature at the seam. **Entropy conjugacy [V-here]: dS/dx = −η exactly** (coin entropy's gradient is minus the rapidity); dS/d(x²) = −η/2x, which equals the errata's −1 **exactly at the tanh fixed point r\* = tanh 2r\*** (η = 2x there) — B3's "one nat per unit explained variance" is the fixed-point specialization of a general conjugacy.

## 2. The two budgets, one identity [V-here]

SNR = x²/u = x²G² = sinh²η. Dividing the elliptic budget x² + u = 1 by u: **G² − SNR = 1 = cosh²η − sinh²η** — the hyperbolic dual budget IS the elliptic budget renormalized to the transmitted/surviving frame (division by the residual mass = the boost to the through-going frame); elliptic in chart A, hyperbolic in chart η, meeting at the seam (x=0, A=η=0, G=1). Companion pair [held, 07-19]: G² = 1 + SNR (power coin) ↔ G_new = 1 + SWR (amplitude coin); SWR = e^{2η} = D², D = e^η = √((1+x)/(1−x)) the **Doppler factor** — the odds are the two-way (radar) Doppler.

## 3. Transfer matrix and the purity instantiation [V-here on structure; [recon] on W]

The unimodular passive two-port: **T = G·[[1, x],[x, 1]] = exp(η·σ₁)**: det T = 1 *is* the budget; eigenvalues e^{±η} (Doppler pair); eigenvalue ratio = SWR; trace/2 = G; off-diagonal = sinh η = √SNR. Qubit/purity dictionary [V-here]: ρ's eigenvalues are the amplitude coin (1±x)/2 (x = Bloch radius); purity γ = (1+x²)/2 ⟺ x² = 2γ−1; linear entropy = u/2 with D_γ = 2(1−γ) = u (errata B4's dictionary recovered); **G_new = inverse minority eigenvalue of the state**. [recon, flagged]: the purity papers' W in H_opt = iW/√F is the rank-2 antisymmetric (Anandan–Aharonov) generator of the transfer plane — the corpus's (trace, wedge) = (2·AM, GM²) slot pair with the wedge in the GM²/det slot; the papers themselves are unread.

## 4. T¹ of T⁴ = id [recon/id — and canon itself holds this link at [id] weight, per 07-19]

T is the SL₂ lift of the Fricke inversion ([[0,−1],[1,0]]: order 4, T² = −id). On the budget disk, T¹ = the quarter Wick turn **η ↦ iA** — exchanging hyperbolic and elliptic sectors (boost ↔ rotation, resistive ↔ reactive); T² = −id = the face/pole swap x ↦ −x — **the sign bit the Kron conflation forgets**; four quadrants = two gauges × two bits (07-19's reading). Offered, not asserted.

## 5. Nesting [V-here]

G∘G is **ill-typed**: G(x) ≥ 1 exits the domain and 1−G² = −SNR < 0 — immediately imaginary (the documented G²-slot collision error class; the activity exit x² > 1 is its fence). (1/G)∘(1/G) = |x| — the amplitude involution, identity **up to the sign bit** (T² = −id again). Legitimate nesting is slot-disciplined: R3.1's wiring SNR_d = G(x_{d−1}) has its interior fixed point from the hyperbolic budget directly: SNR = G ⟹ G² − G − 1 = 0 ⟹ **G\* = φ exactly**, u\* = 1/φ² [V-here, matching 07-19's recorded values].

## 6. Imaginary and affine budget terms [V-here on algebra; [recon] on the register mapping]

x = iy: u = 1+y² > 1, G < 1, SNR < 0, η = iA — pure rotation, no boost: the **reactive sector**. Affine (normalization relaxed): the Campbell cone/mass sector, 1/u as mass bookkeeping [held: foundations block + fourth-review A3]. Offered reading: the two budget deformations (phase-imaginary; mass-affine) are precisely the two forced extension axes of the metric theorem (Petz/shape; Campbell/scale) — the foundations' decomposition seen from the budget side.

## 7. DHO and the Doppler reading of reactive crossings [V-here on structure; [recon] on the record]

The DHO is an elliptic-budget instantiation outright: **ζ² + (ω_d/ω₀)² = 1** with x = ζ. Critical damping (ζ=1) = the arbiter/parabolic point — the same repeated-root discriminant structure as λ = ¼ (s(1−s): r = 0), i.e. **critical damping is the seam-family point of the Laplace register**. Butterworth ζ = 1/√2 = **the self-dual point**: x² = u = ½, A = π/4, G = √2, SNR = 1 — and its rapidity is silver: e^η = tan(3π/8) = 1+√2 = δ_s (artanh(1/√2) = ln δ_s = arcsinh 1) — the Gudermannian bridge landing on the silver chain/π/8 port. Reactive crossing, Doppler-read [V-here]: the pole ratio s₊/s₋ is **pure phase e^{2iA} (|ratio| = 1) underdamped and real Doppler-type e^{2η̃} overdamped** — the crossing at ζ = 1 converts phase into Doppler, which is the imaginary-budget sector exchange (η ↔ iA) read on the pole pair. The corpus's specific reactive-crossings record is unread; this reconstruction is offered for grading.

## 8. Honest inventory

Held from reads: settled conventions; the G_new dictionary entire; the wiring taxonomy incl. R3.1's golden fixed point; the purity-dictionary fragments (errata B3/B4); the foundations block. Derived-and-verified this turn: everything marked [V-here] (≈35 identities, all PASS). Reconstructed, unread, flagged: the purity papers' W specifics; the canonical T¹ statement; the Petz/Campbell↔budget-deformation mapping; the DHO reactive-crossings record; Theorem P's proof text. *Scripts preserved in session shell log; atlas offered for countersign as the instance's graded answer sheet.*
