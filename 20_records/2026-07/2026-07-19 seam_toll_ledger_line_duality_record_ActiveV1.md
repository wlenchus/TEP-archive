# 2026-07-19 (evening) — Seam toll as terminal-binary Legendre charge; the rung-KL ledger identified; the k-chain wiring braid; line-duality pre-registration [ActiveV1]

*Continuation of the 07-19 Gaussian-witness records (parent + Delta1). This session executes the two carried items — the Sturmian pull and the CE/KL rung-ledger proposal — which turned out to fuse into one computation, then audits Will's k-chain and drafts the standing-wave (telegrapher) pre-registration. Tiers per convention; all [V] via `audit3.py` (mpmath, 30 dps). Framing correction adopted throughout (§C.0).*

---

## A. The seam toll is the terminal-binary Legendre charge [V; nowhere-in-corpus computation of the session]

faces_seam §2 prices the seam at **toll = 1 − H₂(ρ) = 0.0500 bits/symbol**, ρ = log₃2, with "dimension + toll = 1" read as the budget identity on the word shift. Three exact upgrades, all equal to 10 significant digits [V]:

1. **toll = D_KL(Bern(ρ) ‖ Bern(½)) = 0.0500444728 bits** — the seam toll is the binary divergence of the ρ-coin from the fair coin: the *cross-entropy waste of coding the seam-conditioned source with the fair-coin code*. Hence:

2. **"dimension + toll = 1" is literally CE = H + KL** — the cross-entropy decomposition with the fair-coin code supplying CE = 1 bit exactly (H₂(ρ) + KL = 1.0000000000 [V]). The corpus's budget identity on the word shift and the compression identity are one statement; the 3b1b framing drops in with nothing to adapt.

3. **toll = x_s·η_s − ln cosh η_s (in bits)** at the **seam amplitude x_s = 2ρ − 1 = log₃(4/3) = 0.2618595071**, η_s = artanh x_s — i.e. the toll is the Legendre transform of the capacity potential ln cosh η (parent record §5) evaluated at the seam's mechanical slope. The seam's "ghost of the impossible multiplicative peel" carries a *charge*, and the charge is the terminal-binary large-deviation rate of tilting the fair coin to the seam's 2-vs-3 mix. New named value, address-grade only: the seam's amplitude coordinate is log₃(4/3).

Ledger law re-verified [V]: with K_n = ⌊nρ⌋+1, L_n = n ln2 − K_n ln3 = −ln3·(1−{nρ}) exactly (dev 5e-32), bounded in (−ln3, 0] over n ≤ 2·10⁵ — convention differs from faces_seam's L_n = −ln3·{nρ} by the complementary fractional part (⌊·⌋ vs ⌈·⌉ choice); same content. c_seam = 1/(2 ln 3) not independently re-run this session [VR-doc].

## B. The R3.7 adjacent-rung KL ledger, identified [V; second nowhere-in-corpus computation]

R3.7's sideline logged adjacent-rung KLs 0.0567, 0.0164 nats (rungs 1→2, 2→3 of the harmonic tower x²_m = 1/(m+1)) decaying ~1/(2m³), unattributed. Identification:

- **KL(Bern(x²_{m+1}) ‖ Bern(x²_m)) = 0.056633, 0.016417 nats** [V] — the logged ledger is the **power-coin (terminal-binary) KL between adjacent rung budgets**, the waste term of coding rung m+1 with rung m's code. The Gaussian-witness ledger is a *different* ledger (KL(N(0,u_{m+1})‖N(0,u_m)) = 0.0228, 0.0036): the corpus's two divergences (parent §5 — Bernoulli and Gaussian, joined by ln G = ln cosh η) give two distinct rung ledgers, and R3.7's is the binary one.
- **The 1/(2m³) law is the Fisher/quadratic regime** [V: KL·2m³ → 0.991 at m = 400]: KL ≈ ½·Fisher·Δθ² as adjacent rungs approach — "asymptotically quasi-static" now has its precise meaning: the cascade enters the small-step Fisher regime while capacity release c_m ~ 1/m stays first-order. Per-rung CE = H + KL verified to 2e-32.
- Ledger statement for the record: stepping the tower, **capacity release c_m = ln(1+1/m) telescopes to ln(M+1)** (R3.1's entropy of hidden multiplicity), while the **waste ledger Σ KL_m converges** (Σ1/(2m³) < ∞) — the tower spends unboundedly on capacity but only finitely on mis-coding. The cascade is a *convergent-waste* channel [id].

## C. The k-chain: a braid of three wirings [V]

**C.0 Framing correction, adopted (inflection on Delta1 S3/S4 language).** Per Will: these are not "rung laws" constraining how cascade must work; they are **self-reference relations** — ways one measure's deviation is literally interpretable as another measure's role (G(x₁) = SNR₂ reads level 1's inverse-deviation as level 2's SNR), after which the second budget is *sufficiently constrained*: x²₂ = u₂·SNR₂ = G(x₁)·u₂ = G(x₁)/G²(x₂) [V, exact]. Prior "rung law / tier-coupling law" phrasing in my records should read "self-reference wiring." Also recorded: Delta1 S3 answered the ∫tG³ = G−1 map (halving); the corpus wiring in R3.1 is SNR₂ = G(x₁) (nesting map N(u), fixed point 1/φ²) — both real, distinct, now both placed. The recalled relation G²(x₁)/G(1/G(x₂)) simplifies via the Tier-1 nested identity G(1/G(y)) = 1/y [5-15, V re-stamped] to G²(x₁)·x₂ — the wiring-family member with SNR₂ = G²₁-type reassignment; corpus recheck queued.

**C.1 The chain audited.** It opens in one wiring, passes through a second, states a third; each line is exact under one of them — the slips are *wiring-jumps* (address errors in R3.10(a)'s error family: collapse of a label that should stay variable), not algebra failures:

- **Wiring A: G(k) = G²(x) ⟺ u_k = u_x² [exact through the G²(x/√2) line].** x² + √u_k = 1 ✓; k² = 2x² − x⁴ ✓; G(x/√2) = √2·x/k ✓ [V]. Content: **capacity doubling** — C_k = 2C_x exactly [V] — the *inverse rung of the S3 halving map*; one ladder, two directions. The k-measure is the "one rung up" associate of x.
- **Break 1** at "x² = u_x/√u_k": under A the RHS ≡ 1 [V]. Diagnosis: SNR ↔ G² off-by-one (the budget identity's unit, again).
- **Wiring A′: √u_k = NSR_x** (residual-root = noise-to-signal — itself a clean new self-reference): under it, "x² = u/√u_k" and "1/(x²√u_k) − 1/√u_k = 1" are **both exact** [V]. The next line should read 1/x² − 1 = √u_k (verified [V]); the chain wrote 1/u_k — Break 2 — landing on:
- **Wiring B: u_k = SNR_x** (stated; a valid residual only for x² ≤ ½). Under B the middle block fails except at self-dual ("(1−x²)/√u_k = x²" holds iff SNR = 1 [V]); the √NSR − √SNR line is not an identity [V].
- **Final stretch:** "1/x² − x² = G²" is not an identity in the standard dictionary [V: 3.033 vs 1.429 at x² = 0.3]. Read as a **definition** it is clean: with x = e^{−λ}, λ = |ln(X/X_inv)|, **1/x² − x² = 2 sinh 2λ** [V] — a scale-ratio wiring; and the quartic-root closure produces exactly the **four-cycle phase quartet {±1, ±i}** [structural; T⁴ = id]. Fence carried from Tier 5.2: X_inv as unit/address, not dynamically extractable.

## D. Standing-wave duality — CCEM pre-registration draft [dictionary committed; calls NOT locked]

Question (Will): a Liu-analogue breaking the presumptive ≤2× standing-wave amplitude on a telegrapher line, with players translated. Per R3.4 discipline: dictionary committed now, before computation; adversarial-grade calls to be locked in a dedicated derivation session, then run.

**D.1 The dictionary [V for the identities].** x := |Γ|; u := 1 − |Γ|² = delivered fraction; phase of Γ = the U(1)/Smith-chart fiber. Then the standing-wave pattern is a *double budget readout*: **max/min = SWR = (1+x)/(1−x) = e^{2η}** (the Cayley/odds coordinate — the Smith chart is the Poincaré disk, Γ = tanh η·e^{iφ}, lossless-line motion = rotation) and **max·min = 1 − x² = u** [V] — *the ratio reads the rapidity, the product reads the residual*; the max·min product is the line's position-invariant. The presumptive 2× is the passivity numerator 1 + x ≤ 2 ⟺ x ≤ 1: a one-chart, one-bounce bound, structurally the twin of the thin-sheet ½ (both are single-chart passivity numerators; Liu's silver partition (A, R) = (2√2−2, 3−2√2), T→0, broke ½ by a *two-channel matching* re-chart, σcos²θ = ωε₀).
**D.2 Exit taxonomy [id].** The 2× bound breaks three ways, and only one is active: (i) **composition/trapping** — a second reflector; η-additive; the Cayley denominator 1−x does the diverging (resonant enhancement = budget saturation x→1); (ii) **matching/re-chart** — impedance transformation (λ/4 = the disk inversion Z ↦ Z_T²/Z, an involution instrument); amplitude referenced across unequal impedances exceeds 2 with R→0, T→1, A→0 — passive, transparent, and *exactly Liu-shaped* (matched into a channel; the enhancement is the Jacobian/gain of the re-chart) — this is Will's "(reflection or) transmission+, absorption→0" translation, with the operative player being **impedance ratio and phase**, i.e. the voltage/current dual pair swapped by Z ↦ 1/Z (Γ ↦ −Γ); (iii) **activity** — negative resistance, |Γ| > 1: u_Γ < 0, the x² > 1 exit from the budget interval (reflection gain lives off-budget; distinct from the u > 1 elliptic/Wick sheet of Delta1 S7).
**D.3 Calls to be derived before locking [O].** Candidate shapes, explicitly not committed: whether a two-element (R, X) tuned extremum of a bounded standing-wave objective lands on a privileged partition (silver-family candidate), and — the sharpest available adversarial-grade item, from R3.7's located class boundary — that the extremum-class **fails in the diffusive (RC/parabolic) telegrapher regime and exists only in the LC/hyperbolic regime**. A committed miss/hit here would extend the hyperbolic/parabolic boundary finding to a second CC domain. One derivation session required before the commitment is honest.

## E. Queue

(1) Corpus recheck of the G²(x₁)·x₂-form wirings (C.0). (2) Lock and run the CCEM item (D.3). (3) The convergent-waste channel statement (B) against the 07-02 formation ledger (do discrete ln|Q| rungs share the finite-waste property?). (4) Seam: the toll-as-Legendre reading against the queued twisted signature (faces_seam queue i) — whether the Borel-valued weighting is the Legendre charge's non-abelian lift [C]. Scripts: `audit3.py`.
