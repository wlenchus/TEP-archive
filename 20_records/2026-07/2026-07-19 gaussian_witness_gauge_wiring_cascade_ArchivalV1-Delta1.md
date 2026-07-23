# 2026-07-19 — Delta 1 to the Gaussian-witness record: the CNG gauge fork, the 5-9 wiring reading, the halving nesting, the shares budget, and Fourier as S on rungs [Delta1]

*Addendum to `2026-07-19 gaussian_witness_capacity_audit_record_ActiveV1.md`, issued same day after Will's pushback on (i) the closure G² = 2π·e^{SNR}·CNG² and (ii) the 5-9 wiring citation. Both objections were verified rather than argued; (i) produces an erratum-grade clarification to the parent record and a better theorem; (ii) is a naming defect in 5-9, not a construction defect. Scripts: `audit2.py` (mpmath, 30–40 dps; all [V] marks below). Tier convention inherited.*

---

## E1. Erratum + resolution: the closure is gauge-dependent, and the gauge gap is the capacity

The parent record wrote "G² = 2π·e^{SNR}·CNG², no free constant, no pin" without declaring the normalization of CNG. Will's objection is correct under his stated definition. There are two objects:

- **CNG_A := (1/√(2πu))·e^{−x²/(2u)}** — the density of N(0,u) at x (u inside the root; what the parent record and script used);
- **CNG_B := (1/√(2π))·e^{−x²/(2u)}** — Will's stated form: standard-normal normalization, constrained exponent.

Both are legitimate; they are the same object in two gauges, and every disputed statement resolves by declaring which [V]:

| statement | under CNG_A | under CNG_B |
|---|---|---|
| 2π·e^{SNR}·CNG² | = G² (exact) | = 1 (exact) — i.e. **would pin G ≡ 1 if asserted equal to G²; Will's objection valid here** |
| relation | CNG_A = G·CNG_B | CNG_B = (dx/dA)·CNG_A — **Will's displayed Jacobian equation, verified exact** |

**Which gauge did the original chains use?** The chains themselves pin CNG_A, at three independent seams [V]: chain 1's L10 writes `(1/√(2πu)) × e^(−½x²/u) × √(2π)` with u inside the root; chain 2's M11 decomposition ln(e^{−x²/2u}) = ln CNG + ln√(2πu) balances only under A (−0.5000 vs −0.8466 under B at x²=½); chain 3's N1 equals −SNR/2 exactly under A only. So the parent record's closure is correct *in the chains' own gauge*, and the erratum is: **declare the gauge**. No G = 1 pin exists in either gauge once declared; the pin appears only when a B-gauge symbol is substituted into an A-gauge identity.

**The resolution is better than the dispute.** The gauge gap is not bookkeeping:

  **ln CNG_A − ln CNG_B = ln G = C_nats** [V].

The disputed factor *is* the capacity. CNG_B = φ(z), the standard normal evaluated at the whitened point z = x/√u = √SNR — a function of SNR alone, *u-blind*, which is why its closure (2π e^{SNR} CNG_B² = 1) is absolute and carries no G. CNG_A is the u-aware density; its extra normalization ½ln(1/u) = ln G is exactly what the u-aware observer knows that the standardized observer has forgotten. Capacity = the log-Jacobian of whitening.

**The whitened coordinate completes the triple [V].** z = x/√u = tan A = sinh η, so the budget's three circular functions are (sin A, tan A, sec A) = (amplitude x, whitened score z, gain G), with hyperbolic mirror (tanh η, sinh η, cosh η). And the whitening map is the momentum integral: **z = ∫₀^x G³ dt** — the parent record's ∫G³ = xG entry *is* the standardization transform. (The early-synthesis table's `√SNR ↔ sinh(η/2)` is the half-angle convention of the same fact; documented drift class, §311.)

## E2. The 5-9 wiring: construction sound, naming defective (Will's diagnosis is the collision signature)

Re-verified [V]: the 5-9 §6 result is a **two-reassignment construction**. For *any* level-1 scalar h: (step A) define level 2 by G²(x₂) := e^h, so u₂ = e^{−h}; (step B) define level 3 by SNR₃ := h. Then √u₂ = e^{−SNR₃/2} = e^{−x₃²/(2u₃)} identically — verified exact for h ∈ {0.3, 0.8814, 2.5}, and it is an identity in h. Nothing in the construction requires ln[dη/dx] = η.

That requirement — Will's "for your cited form to hold, we would need ln[dη/dx] = η, hence x² = tanh²[ln(dη/dx)]" — is precisely the **collision you get if h is forced to be simultaneously level-1's boost rapidity (artanh x₁) and level-1's log-gain (ln(1+SNR₁))**. 5-9's first clause "η₁ = ln(1+SNR₁)" invites exactly that collision: it names the *dilation* rapidity (the multiplicative/telescoping object e^η = G², per early synthesis §69) with the symbol the settled convention reserves for the *boost* rapidity (artanh x). As a boost-rapidity statement it is false as an identity; as a definition of a dilation coordinate it is fine; the corpus's own §VIII.6/§311 flags this exact drift class. **Proposed erratum-grade clarification to 5-9 §6 [carried]:** "η₁ here denotes the dilation rapidity ln G₁² = ln(1+SNR₁), not artanh x₁; the two subsequent equalities are reassignments (definitions of levels 2 and 3), not same-level identities."

*Curio, kept as curio [V]:* the same-level boost/dilation coincidence locus artanh x = ln G² is the real root of **x³ + 2x² = 2**: x* = 0.839286755214 (both sides 1.2187557269; x*² = 0.7044, u* = 0.2956). An algebraic privileged point of the collision, joining the golden/silver inventory only if something else ever lands on it.

## S3. The nesting: SNR′ = G − 1 is exact halving of the dilation rapidity [V]

Will's proposed nesting G(x₁) → G²(x₂) − 1 = SNR₂, i.e. **SNR′ := G − 1**, closes cleanly:

  SNR′ = G − 1 ⟺ G′² = 1 + SNR′ = G ⟺ **ln G′² = ½·ln G²** — the halving map on η_dil [V].

Kinetic reading: SNR′ = ∫₀^x t·G³ dt (the parent record's G − 1 integral): *the next level's SNR is the accumulated kinetic work of this one*. Orbit from the recorded golden point (SNR = G = φ, the budget identity's meet with SNR = G): **G_n = φ^(2^−n)** [V to machine precision, n = 0…4] — a φ-rooted halving tower, kin to the corpus's Landen/AGM rungs and the "ln 2 = one self-dual rung" pricing; each T_lin application is one halving rung applied to the log-gain itself. Taxonomy of the three natural wirings: T_same: SNR′ = G² − 1 (the same-level tautology); **T_lin: SNR′ = G − 1 (halving rung)**; **T_log: SNR′ = ln G² (the 5-9/Gaussian-witness rung, u′ = e^{−SNR′})**.

## S4. Cascade wiring classes — a proposed answer shape for O-b's upgraded question [C]

6-20's GMC construction implicitly prices **increment variance = rung capacity** (per-edge N(0, ln 2); ln 2 = capacity of the binary split, u = ½). Under that rule the wiring taxonomy classifies limits by the capacity sequence c_n [V for the rates; C for the limit-classes]:

- **T_lin (geometric):** c_n = c₀·2^{−n}, Σc_n = 2c₀ < ∞ [V] → bounded total variance → smooth/exactly-solvable limit, no chaos. (The O-b theta member's degeneration to the plain Gaussian fixed point sits naturally here.)
- **Constant (ln 2):** Σ = n·ln 2, covariance linear in depth = log in scale → **standard GMC** — 6-20's choice is exactly the critical/scale-free wiring, now *placed* rather than assumed.
- **T_log (harmonic):** SNR_{n+1} = ln(1+SNR_n) gives n·SNR_n → 2 [V: 2.0188, 2.0034, 2.0003 at n = 10², 10³, 2·10⁴]; cumulative capacity ~ 2 ln n [V: Σ₁₀₀₀ = 14.28 vs 2 ln 1000 = 13.82] → covariance ~ ln(depth) = ln ln(1/scale): a strictly intermediate, marginal class — slower than GMC, unbounded unlike T_lin.

**Conjecture [C], named computation queued:** O-b's "which inter-rung wirings break exact solvability and produce genuine log-correlated limits?" is answered by the **capacity-decay class of the wiring**: summable ⟹ solvable/trivial; constant (linear cumulative) ⟹ GMC; intermediate (e.g. harmonic) ⟹ marginal log-log class. Test: build depth-n binary cascades under each wiring, measure leaf-covariance vs common-ancestor depth (linear vs logarithmic vs bounded).

## S5. The capacity-shares budget: C_nats = ½x² + D_KL, normalized [V]

Will's proposed budget holds exactly and is **unit-invariant** (the nats-vs-bits wariness dissolves: shares are ratios of same-unit quantities; verified identical in nats and bits): with m := (x²/2)/C_nats and δ := D_KL/C_nats,

  **m + δ = 1** [V], m monotone 1 → 0: mean-share dominates at low SNR, dispersion-share at high SNR (m = 0.896, 0.721, 0.541, 0.391, 0.215 at x² = 0.2, 0.5, 0.75, 0.9, 0.99).

Geometric standing [id]: the two legs move along *orthogonal Fisher directions* through the pivot N(0,1) — mean-shift at unit variance (D(N(x,1)‖N(0,1)) = x²/2) and variance-mismatch at zero mean (D(N(0,u)‖N(0,1))) — the Gaussian family's Fisher metric is diagonal in (μ, σ), so the split is a genuine information-geometric Pythagoras, normalized. This is a **second-layer budget produced from the first by an operation** (normalize an exact orthogonal decomposition) — a "budget associate" in Will's sense; the operation plausibly iterates. Its self-dual point m = δ = ½ solves −ln u = 2(1−u): **u\* = −W₀(−2e^{−2})/2 = 0.203187869980** [V] — a Lambert-W privileged value. Flag: numerically near, and deliberately kept distinct from, silver-family values 3−2√2 = 0.17157 and (√2−1)/2 = 0.20711; the proximity is noise until shown otherwise.

## S6. Inference coordinates [id, classical anchors]

Under the corpus's occasional regression reading (x = r): **η = artanh x is Fisher's z-transformation** — the classical variance-stabilizer of the correlation coefficient (Var ≈ 1/(n−3), constant, CI transport by dx = u·dη); **A = arcsin x is the arcsine variance-stabilizing transform** of √p; G² = VIF; u = 1−R². The budget calculus is, exactly, the calculus of correlation inference; the three coordinates (x, A, η) are the three classical inferential gauges of one statistic. New face [V]: pulled back along z = sinh η, the standard normal becomes φ(sinh η)·cosh η — the **Johnson S_U density** (normalization verified = 1): on-budget Gaussian inference in x is sinh-normal (Johnson) inference in rapidity.

## S7. Fourier is the S-involution on Gaussian rungs; the archimedean slot [V/id/C]

- **[V]** Characteristic-function duality: p̂_u(t) = √(2π)·G·p_{1/u}(t) — Fourier sends rung u to rung 1/u **with multiplier the gain**. Tate normalization f_u(x) = e^{−πx²/u}: F[f_u] = √u·f_{1/u}, **self-dual iff u = 1** (the terminal/zero-signal rung).
- **[id]** u ↦ 1/u leaves (0,1): the image sheet has x² = 1−u′ < 0 — imaginary amplitude, the elliptic/compact sheet. **Fourier duality on rungs = the Wick/Gudermannian involution = the direction-reversal S** of 07-02 [M there], realized concretely on the Gaussian family, with the gain as the intertwining multiplier. This adds the third self-consistency to the faces_seam queue (iv): tanh(dr) = r, e^r = r, and now **φ = F[φ]** — fixed points of boost, dilation, and duality respectively.
- **[C]** Functorial slot: 07-02's coding ledger prices finite quotient rungs (capacity ln|Q| — finite places); the Gaussian rung family with its Γ/2π normalizations and Tate-self-dual witness is the natural **archimedean place** of the same conservation ledger. Shape-claim, honestly fenced: the transmission functor's ledger should complete place-wise (finite rungs × the Gaussian ∞-rung) the way an L-function completes; the CNG is the ∞-place test vector. Decisive-check candidate: whether the ledger's ∏u telescoping, run with the ∞-rung included, reproduces a completed functional-equation symmetry under the verified u ↦ 1/u involution.

## S8. Status and queue

Carried: (1) 5-9 §6 naming erratum (E2). (2) The wiring-classification computation (S4). (3) Whether the shares budget m + δ = 1 iterates into a cascade family of its own, and whether u\* = −W₀(−2e^{−2})/2 lands anywhere else in the corpus. (4) The completed-ledger check (S7). (5) Parent-record erratum absorbed here: gauge declaration for all CNG statements (E1). Scripts: `audit2.py` (this Delta); `chain_audit.py` (parent).
