# 2026-07-19 — The Gaussian witness of the budget: chain audit, capacity ledger, and the cross-rank landing [ActiveV1]

*Single-session record. Question: the three manipulation chains around I = ∫_{k=u}^{1} (1−k)/k dk, the "constrained normal Gaussian" (CNG), and the x²-offset to C/B. Convention fixed per the settled corpus: x = sin A = tanh η, u = 1−x², G = 1/√u, SNR = x²/u, C/B = log₂(1+SNR) = −log₂ u [06-28 §L, V]. Tier marks per corpus convention: **[V]** machine-verified this session (script: `chain_audit.py`, mpmath 50 dps, four sample points x² ∈ {0.2, 0.5, 0.75, 0.9}, quadrature cross-checks); **[T]** standard result, cited; **[id]** identification; **[C]** conjecture; **[O]** open. Companions: 5-9 circuit-calculus record §6 (gaussian-from-budget cascade), 6-10 O-b closure note (theta normalization), 6-20 GMC bridge, 06-28 consolidation record, 07-02 coding-theorem conservation ledger, metriplectic note 6-17 §3.*

**Definitions.** CNG := φ_u(x) = (1/√(2πu))·e^{−x²/(2u)} — the density of N(0, u) evaluated at the on-budget point x. I := ∫_{k=1−x²}^{1} [(1−k)/k] dk = u − 1 − ln u = −x² − ln u **[V, closed form + quadrature]**.

---

## 1. Audit of the chains

**Chain 1 (the Integral chain) [V].** Exact from L1 through L12, with one isolated slip at L5, then a structural break at L13; the tail (L14–L27) is mostly-consistent algebra downstream of the broken line and does not return to I.

| line | verdict | note |
|---|---|---|
| L1–L4 | exact | I = −x² + ln G² = 2 ln(e^{−x²/2}·G) |
| L5 | off by +ln 2 | "2 × (1/√(2u))" should be "√2 × (1/√(2u))"; the slip costs exactly one halving rung |
| L6–L12 | exact | includes the CNG introduction; L12: I = 2[ln CNG − x² ln(e^{−x²/(2u)})] + ln 2π |
| L13 | **break** (dev −5.934 at x²=½) | 2[A − x²B] was rewritten as [(2/x²)A − B]/x²; correct factoring is 2[A − x²B] = x²·[(2/x²)A − 2B] — multiplied by x², not divided |
| L14–L20 | consistent rewrites of broken L13 | the algebra after the break is internally fine |
| L21 | second break (dev −2.434) | ln e^{x²/(2u)} − ln e^{1/u} = (x²−2)/(2u) ≠ x²/2; the collapse to ln e^{x²/2} needs x⁴ = 2 |
| L24–L26 | minor tail shuffles (net −0.03) | sign/exponent bookkeeping in the (2π)^{1/x²} terms; a stray second ln 2π enters |
| L27 | ≠ I | final displayed form does not equal the integral |

**Corrected closed form [V]:** continuing correctly from L12,

  **I = ln 2π + 2 ln CNG + x²·SNR**  (exact; equivalently −2 ln CNG = ln 2πu + SNR).

**Chain 2 (the x²-offset chain) [V]: exact end-to-end.** All seventeen displayed steps M0–M17 verified exact, including the final form C/B = 2[ln e^{I/(2u)} − (ln CNG + ln √(2πu))]/(ln 2 · G²). The parenthesis nesting in the transcription ("ln((1/√(2πu) ×") is unbalanced but the charitable reading is the correct one.

**Chain 3 (the CNG block): conclusion correct, one bookkeeping slip, two invalid final steps [V].**
- N1/N2: ln CNG + ½ln(2πu) = −SNR/2 exactly (the standardized log-likelihood; z := x/√u = √SNR).
- N2 → N3 drops ½ln 2π (measured gap −0.918939 = −½ln 2π at every sample point). N3 = N4 is internally consistent, and the derived identity is nonetheless **true**:

  **ln G² − 2 ln CNG = SNR + ln 2π**  (exact).

- The step to "= ln[2π·SNR]" is invalid: SNR + ln 2π ≠ ln(2π·SNR) — SNR enters bare, not logged. (This bareness is not a defect; it is the signature of the Shannon form: ln(1+SNR) is what gets logged, and 1+SNR = G² already absorbed it.)
- The step to "ln[2π·SNR + CNG²]" is a second, independent invalidity (sum of logs → log of sum).
- **Does the closure pin G(x) = 1, or hide a presumption? No [V].** Nothing is pinned and no presumption exists; the two final steps are simply non-identities. The product repair 2π·SNR·CNG² = G² would need SNR·e^{−SNR} = 1, impossible (max s·e^{−s} = 1/e < 1); the sum form 2π·SNR + CNG² = G² holds only at one accidental crossing, x² ≈ 0.13756, an isolated root, not an identity. The true closure is:

  **G² = 2π · e^{SNR} · CNG²**  (exact) — equivalently √(2π)·G·... no presumption, no free constant.

## 2. The referential landing (the part that was already in the corpus)

The corrected closure is not new to the framework — it is the **5-9 gaussian-from-budget cascade** identity in different clothing. 5-9 §6 [V then, re-verified now]: the wiring η₁ = ln(1+SNR₁), e^{η₁} = G²(x₂) = 1/u₂, reassigned cross-rank via η₁ := SNR₃, yields √u₂ = e^{−SNR₃/2} = the unnormalized Gaussian at x₃ with variance u₃, normalization factor 2π·u₃. In present notation:

  **u_next = 2π·u·CNG² = e^{−SNR}**  [V, re-stamped this session]

which is the closure above rearranged (G² = e^{SNR}/… ⟺ 1/u = 2π e^{SNR} CNG²). The 6-10 O-b sentence "pdf² · 2πu₃ = u₂" [V] is the same sentence theta-instantiated; the 6-20 GMC bridge (rapidity increments N(0, ln 2), carrier dimension u) is its continuum face. So the present tangent independently rederived the recorded cross-rank rung law — and the SNR-vs-ln SNR near-miss in chain 3 is the shadow of exactly that wiring: the cascade's defining move converts a *logged* quantity at one rank (η = ln G²) into a *bare* one at the next (SNR). The conflation is a one-rung address error, which is also the honest answer to "was that really not supposed to be ln SNR?" Three legitimate homes for ln SNR exist and none is this identity: (i) ln SNR = 2 artanh(x² − u) [V] — the logit/natural parameter of the power coin (x², u), the centered-rapidity face (equivalently x² = 1/(1+e^{−ln SNR}), Fermi–Dirac/logistic form of the budget); (ii) the high-SNR asymptote ln G² = ln(1+SNR) → ln SNR; (iii) the misspecification gap in §4 below.

## 3. The x²-offset, completed cleanly [V]

The offset is not a trick; it completes the integrand:

  x² = ∫_u^1 1 dk,  I = ∫_u^1 [(1−k)/k] dk  ⟹  **x² + I = ∫_u^1 dk/k = −ln u = C/B · ln 2.**

Reading k as the running residual (noise floor swept from 1 down to its achieved value u), (1−k)/k = SNR(k) is the *budget's own SNR function evaluated along the sweep* — not the endpoint constant x²/u. The question's instinct ("conflates a status and a dependent SNR") is correct [V]: ∫_u^1 (x²/u) dk = x⁴/u ≠ I (0.5 vs 0.193 at x²=½). The reconciliation is Leibniz: dI/du = −SNR(u) — status is the endpoint, the integrand is the sweep. Three exact sweep readings in SNR coordinates (change of variables k = 1/(1+γ)) [V]:

- −ln u = ∫₀^SNR mmse(γ) dγ with mmse(γ) = 1/(1+γ): **the I-MMSE theorem** (Guo–Shamai–Verdú 2005) [T] — capacity in nats = ½∫ mmse; equivalently dC_nats/dSNR = u/2 = 1/(2G²) [V].
- x² = ∫₀^SNR mmse(γ)² dγ [V] (the offset term is the integral of MMSE-squared; du/dγ = −u², the MMSE Riccati law — the budget's residual is logistic along the SNR sweep).
- **I = ∫₀^SNR [x²u](γ) dγ [V]** — the integral of the light-cone invariant pq = x²u (interior spine §11.2's observer-invariant Minkowski product) over the SNR sweep.

And the invariant itself acquires an estimation meaning: for the jointly-Gaussian budget pair (signal x², noise u, total 1), the **absolute minimum mean-square error of best-matching is exactly x²·u** [V] — the corpus's observer-invariant is the conditional-expectation error, and u is the *normalized* MMSE. This wires the foundational anchor "best-matching = conditional expectation = L² projection = the budget" [interior spine §11.1; 06-29] to a celebrated exact theorem of information theory: **the capacity's derivative is the best-matching residual.** [id]

## 4. The constrained Gaussian, interpreted [V/id]

What the CNG is: the density of the **noise law N(0, u) evaluated at the typical signal amplitude x**, on the budget surface x² + u = 1. Its standardized argument is z = x/√u = √SNR: the budget places the typical signal exactly √SNR noise-sigmas from the origin. Its negative log is a surprisal: −ln CNG = ½ln(2πu) + SNR/2 [V].

- **MaxEnt witness [id].** The corpus fences the budget as L²/variance, not modular [06-28 §L: ρ=u exact for linear entropy, false for von Neumann]. The CNG is precisely where the two ledgers meet without violating that fence: N(0,u) is the maximum-entropy law at variance u, the unique distribution for which the variance budget and the entropic ledger agree. Nothing modular is claimed of u itself.
- **KL structure [V/T].** I = 2·D_KL(N(0,u) ‖ N(0,1)) exactly — the integral is twice the divergence between the noise law and the unit-total law; equivalently I = d_IS(u, 1), the Itakura–Saito divergence (the Bregman divergence of the Burg/log barrier −ln u). The capacity splits as **C_nats = x²/2 + D_KL(N(0,u)‖N(0,1))** [V]: mean-shift term + variance-mismatch term. This is the AWGN mutual-information decomposition I(X;Y) = E[D(P_{Y|X} ‖ P_Y)] evaluated on the budget: with prior N(0, x²), E_prior[D(N(m,u)‖N(0,1))] = C_nats exactly, and the typical point m² = x² already achieves it [V]. Chain 1's corrected closed form is this decomposition rearranged.
- **Misspecification reading [V].** ln φ_{x²}(x) − ln CNG = ½[SNR − 1 − ln SNR] = ½·d_IS(SNR, 1) ≥ 0: the likelihood cost of the budget constraint (variance u) against the single-observation MLE (variance x²) is again Itakura–Saito, now of SNR against 1. The CNG is stationary in u exactly at SNR = 1 ⟺ x² = ½ — **the self-dual point is where the constrained Gaussian is variance-MLE-consistent** [V; ties to the recorded self-dual locus x² = ½, distinct from rate-saturation per interior spine §227].
- Score/Stein face [V/T]: the CNG's score is −x/u = −x·G²; Fisher information of N(0,u) is 1/u = G² = dη/dx — **the budget rapidity's derivative is literally the Fisher information of the noise law**, Cramér–Rao saturating at variance u. Stein's identity E[f′(X)] = E[X f(X)]/u re-verified [V]; it is the derivative-equals-integral characterization that pins the Gaussian uniquely.

## 5. The terminal-binary / Legendre face [V/id]

ln G = ln cosh η exactly [corpus-known subtlety; early synthesis §69]. New reading: **ln cosh η is the log-partition function (free energy) of a fair ±1 spin at field η** — so capacity-in-nats is the cumulant generating function of the terminal binary distinction [id; the d = 2 terminal port of the transmission functor]. Then:

- d(ln cosh η)/dη = tanh η = x: **the signal amplitude is the magnetization** [V].
- Legendre transform: η·x − ln cosh η = D_KL(Bern((1+x)/2) ‖ Bern(½)) [V] — the binary divergence of the *amplitude coin* (1±x)/2, whose odds are the Cayley map w = (1+x)/(1−x) = e^{2η} [V; the cyclotomic face's coordinate, 06-28 §N]. Two coins, two logits: amplitude coin ↔ 2η; power coin (x², u) ↔ ln SNR.
- So one identity set carries **both** divergences: Gaussian KL (variance channel, §4) and Bernoulli KL (terminal binary), joined by ln G = ln cosh η. Work form: **dC_nats = x dη** [V] — capacity increment = magnetization × rapidity increment (dU = T dS-shaped), integrating to C_nats = ∫₀^x t·G²(t) dt.
- Cascade face [id]: rapidity additivity η_tot = Ση is the LLR additive combining rule; the induced tanh-sum x₁∘x₂ = (x₁+x₂)/(1+x₁x₂) [V] is simultaneously relativistic velocity addition and the Bayes-optimal soft-bit combination of independent binary evidence (the variable-node rule of iterative decoding; the check-node rule is the tanh-product). The dormant thin-film/channel-additivity thread and the 07-02 ledger's series-rung telescoping (∏u, per-rung capacity −ln u) both live here; the 07-02 discrete rungs u = 1/|Q| get a continuous Gaussian twin with the same chain-rule spine [id].

## 6. Maxwell-like derivative = integral equations [V/T/id]

The request has a corpus tenant already: the metriplectic note's **Δ_g 𝒞 = |K| = 1** [6-17 §3, V; re-stamped symbolically this session on 𝒞 = 2 ln cosh(ρ/2)] — capacity as a potential sourced by curvature, whose Gauss-law/integral face is the verified holonomy = capacity chain (boundary flux = enclosed area = Wigner rotation; Gauss–Bonnet). dC = x dη is its radial section. The information-theoretic trio of derivative-equals-integral laws, all exact here:

1. **I-MMSE**: dC_nats/dSNR = mmse/2 = 1/(2G²) ⟺ C = ½∫₀^SNR mmse dγ [T, V].
2. **de Bruijn** [T]: ∂h/∂t of a Gaussian-smoothed law = ½·Fisher; on-budget, h(N(0,u)) = ½ln(2πeu) with dh/du = G²/2 — entropy's derivative is the budget's Fisher information.
3. **Stein** [T, V]: E[f′] = E[Xf]/u — the integral identity whose solitary solution is the CNG's law.

The closed integral family of the gain [V]: ∫₀^x G = A (angle), ∫₀^x G² = η (rapidity), ∫₀^x G³ = xG (momentum form), ∫₀^x tG² = ln G = C_nats (work/capacity), ∫₀^x tG³ = G − 1 (kinetic form). One ladder, ∫G^n, in which angle, rapidity, momentum, capacity, and energy are the first rungs.

## 7. Status, threads, and queue

- **Honest framing.** Every identity above is exact for *any* quantity satisfying x² + u = 1 — per the corpus's own discipline this is identity-not-discovery [06-28: "G²−SNR=1 realization-independent but tautological"]; the content is which wirings are load-bearing. What this session adds that is not tautological-in-that-sense: the sweep/KL/MMSE readings attach the budget to *theorems with content* (I-MMSE, de Bruijn, Chentsov-adjacent Fisher facts), i.e., they say what the budget's calculus *is* — the exact differential calculus of Gaussian-channel information — rather than adding a new physical claim. No physical claim is made here.
- **Litmus checks passed en route [V]:** naive-constant integrand refuted (x⁴/u ≠ I); no G = 1 pin; product-form closure impossible (1/e bound); accidental sum-form root isolated at x² ≈ 0.1376 and flagged as noise, not structure.
- **Queue.** (i) Diff the u_next = 2πu·CNG² = e^{−SNR} landing against 6-10 O-b's theta-instantiated pdf²·2πu₃ = u₂ at the wiring level (same sentence or cousin?) [O]. (ii) The Gudermannian-bridge queue item (07-15 faces_seam, iv) is partially served: A = gd(η) with dA = G dx, dη = G² dx gives the Mahalanobis-vs-natural-parameter reading of the two self-consistencies; the tanh(dr) = r join proper remains [O]. (iii) Continuous-vs-discrete rung ledger: place u ∈ (0,1) Gaussian rungs beside 07-02's u = 1/|Q| formation rungs under one chain-rule statement [O]. (iv) Whether the Bernoulli/Gaussian KL pair (one Legendre structure, §5) relates to the two-families fractional-statistics involution note (5-18) [C, unexamined].
- **Scripts:** `chain_audit.py` (this record's [V] basis: 3 chains line-by-line at 4 sample points, 50 dps; 5 quadrature cross-checks; 14 extension identities; symbolic Laplacian re-stamp).
