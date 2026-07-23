# 2026-07-19 (tangent) — Cross-budget pair ledgers; the invariant-poles construction identified as the odds gauge [ActiveV1 — filed same day with Will's countersign]

*Mobile-tangent session. Sources read: the four 07-19 records (gaussian-witness parent + Delta1, seam_toll, two_ledgers) + signed-digit and ħc notes; faces_seam Delta2; transmission-functor definitional record; 06-28 §L/§N via early-synthesis §69/§311; test rounds 2–3; the GitHub archive spine; and the GSR-era source of "G_new" — `Refined Foundations — Radical Relativity, Geometric Budget, and Transfinite Dynamics` (2025-05-20). Script: `verify_cross_budget_gnew.py` (sympy + mpmath 50 dps), 44 claims, all **[V]** (8 of the 44 are numeric-exact at ≤1e-12 where sympy's structural equality balked; noted inline in the script). Convention throughout: settled corpus — x = sin A = tanh η, u = 1 − x², G = 1/√u, SNR = x²/u [06-28 §L].*

*Pre-registration honesty: the half-angle/logistic hypotheses below were formed **before** the corpus reading, from the pasted GSR excerpt alone; the corpus landings (seam coin, SWR, drift-class §311) were found after. Every claim is an exact identity, not a fit, but the reading order is disclosed as a confirmation-bias flag.*

---

## 1. The cross-budget question: is there a constraint relating (u_{d−1}, x²_d), (u_d, x²_{d+1}), …?

**Corpus position, confirmed:** within-rank pairs are budget-constrained; cross-rank pairs are free wirings ("capacity-unconstrained… priced by bandwidth use" — signed-digit note §1; C.0's self-reference framing). No a-priori algebraic constraint ties u_{d−1} to x²_d. That stands.

**But the pairs are not lawless. Three wiring-independent exact structures [V]:**

**(i) The antisymmetric cross-ledger telescopes.** For *any* budget sequence, at every seam:

  u_{d−1}·x²_d − x²_{d−1}·u_d = x²_d − x²_{d−1}  (exact),

so Σ_d (u_{d−1}x²_d − x²_{d−1}u_d) = x²_D − x²_0 — a pure boundary term, schedule-independent in exactly U1's "per-rung ledger is chart, the total is invariant" sense. The antisymmetrized cross-budget terms are a spend-like ledger; only the endpoints survive.

**(ii) The pair-budget: each seam carries its own unit budget.** For any two budgets (Cauchy–Binet / Brahmagupta–Fibonacci two-square identity):

  (√(x²_{d−1}x²_d) + √(u_{d−1}u_d))² + (√(u_{d−1}x²_d) − √(x²_{d−1}u_d))² = (x²_{d−1}+u_{d−1})(x²_d+u_d) = 1.

The first square is the Bhattacharyya affinity² = fidelity of the adjacent rung coins; the second is built *entirely from the cross-budget terms*. So the cross terms are the noise legs of an exact budget associate (a budget-valued pairing operation, in the two_ledgers §2 "budget associate" sense — the family now has three members: Legendre lift, shares budget, pair-budget). The symmetric cross combination is constrained; only the wiring's *choice of point on this budget* is free — which is a sharpened form of "free but priced."

**(iii) The pair-budget is the waste ledger in closed form; its arc is the ∫G ledger.** Small-step regime [V]: cross-leg²/KL(rung_{d}‖rung_{d−1}) → ½ exactly (checked on the harmonic tower to m = 1000; R3.7's logged values 0.056633 / 0.016417 nats reproduced first). So **convergent waste [two_ledgers §1] = summable cross-legs**, and the waste trichotomy (zero / summable / linear-stationary) is readable directly off cross-budget terms. Globally: arccos(affinity) is the Fisher–Rao arc, and for **amplitude coins** (1±x)/2 it equals |ΔA| — the corpus's angle ledger A = ∫G dx *is* the Fisher–Rao metric of the amplitude coin — while **power coins** (x², u) give 2|ΔA|. (The elliptic half/double twin of √SNR ↔ sinh(η/2), §311.) Seam-to-seam, cross terms compose by the sine addition law: cross(1,3) = cross(1,2)·aff(2,3) + aff(1,2)·cross(2,3) — the constraint relating *consecutive* pairs is rotation composition on the coin sphere; the hyperbolic face composes by sinh under Δη.

**Wiring-specific closed forms [V], for the recorded wirings:** R3.1 nesting SNR_d = G(x_{d−1}) ⟺ x²_d = 1/(1+√u_{d−1}), interior fixed point u* = 1/φ² (G²* = φ², root of y²−3y+1 ✓); T_lin halving ⟺ u_d = √u_{d−1}; capacity doubling (k-chain wiring A) ⟺ u_d = u_{d−1}²; T_log ⟺ u_d = 1/(1 − ln u_{d−1}), terminal-pole flow with 1−u_n → 2/n (the recorded n·SNR_n → 2 [Delta1 S4], reproduced). Among recorded wirings only the nesting has an interior privileged point; halving/doubling are the two directions of one ladder [seam_toll C.1]. For a fixed wiring, the pair-to-pair "constraint" is stationarity in d — that d-independence is what mints the fixed points and towers (φ^(2^−n)).

**Summary sentence:** the constraint is not *on* the pairs (the corpus is right that they're the free/design axis) but *on their ledgers* — antisymmetrized: boundary-valued; symmetrized-squared: unit pair-budget (fidelity split); small-step: the waste ledger; composed: the angle ledger.

---

## 2. "G-new" (GSR, 2025-05-20), identified: it is the odds/SWR gauge — the amplitude coin's own gain

Source located: *Refined Foundations* §3 ("Geometric Derivation of the x²+u=1 Budget from Invariant Poles"), §8.1 queued its exploration; abandoned; later documents carry NO-G_NEW markers. The construction itself verifies end-to-end [V]: chords² from poles (0,±1) to M(θ) are 2(1∓sinθ), Thales right angle at M, normalization by the squared diameter yields the split exactly.

**Dictionary [V].** With the settled x = sinθ (so the old chart's amplitude), the G-new split is the **amplitude coin**:

  x²_GSR = p = (1+x)/2 = σ(2η),  u_GSR = q = (1−x)/2 = σ(−2η)  — logit = 2η [capacity-audit §5's "amplitude coin ↔ 2η"],

and the G-new gamma is not a G-slot object but a **G²-slot** (dilation-type) object:

  G_new := 1/q = 2/(1−x) = **1 + e^{2η} = 1 + SWR** = 2(1+x)G² = **2·G·e^{η}**,  ln G_new = ln 2 + C_nats + η.

So "height of rapidity" is exactly right: G_new − 1 = e^{2η} is the exponentiated double rapidity, and **heights multiply under rapidity addition while gains don't** — the §69 lesson (G not multiplicative; e^η is) holds perfectly with G_new − 1 as the multiplicative object. Half/double-angle relations, as recalled: p = cos²(π/4 − θ/2), q = sin²(π/4 − θ/2); e^η = tan(π/4 + A/2) — the **Gudermannian bridge** (faces_seam queue iv) is this chart's native identity. Both gauges satisfy the budget identity in their own coin: G² = 1 + SNR (power), G_new = 1 + SWR (amplitude); SNR = (SWR−1)²/(4·SWR).

**The corpus has already re-adopted it, namelessly, six times:** the Cayley/odds coordinate w = (1+x)/(1−x) = e^{2η} [06-28 §N]; the amplitude-coin logit [capacity-audit §5]; the standing-wave chart — SWR = (1+x)/(1−x) = e^{2η}, max·min = u, "the ratio reads the rapidity, the product reads the residual" [seam_toll D.1] — i.e. **G_new = 1 + SWR is the SWR gauge**; the seam toll's coin — **p(x_s) = (1+log₃(4/3))/2 = log₃2 = ρ exactly [V]** — the seam's Bernoulli parameter *is* the G-new certainty intensity of the seam amplitude; the Legendre lift's domain p = (1+x)/2 [two_ledgers §2]; and the drift-class documentation of "the self-dual-centered double angle x² = ½(1+tanh 2η)" [early synthesis §VIII.6/§311]. The mid-2025 abandonment was sound *then* (rival-gamma symbol collision, no port formalism, no gauge-declaration discipline); the object itself has been quietly load-bearing all month.

**The port/seam reading (the instinct behind revisiting it).** The Kron conflation (p, q) ↦ ((p−q)², 4pq) = (x², u) [V: u = 4pq, x = p−q] forgets exactly one bit — sign(x), which pole you face. So the settled budget is the **port-symmetrized/sign-blind face** (G = 1/(2√(pq)): the settled gain is the inverse geometric mean of the two port intensities, halved), and G-new is the **port-resolved face**. Complementary Z₂ readouts [V]: G_old = secθ flips sign across the face swap θ ↦ π−θ but is even in x (side-blind); G_new is invariant under the face swap but strictly monotone in x (side-seeing). Two gauges, two bits, four quadrants — consistent with the T⁴ chart cycle at [id] weight only. The double pole at the arbiter (G_new → 4G² as x → 1 [V]) is the gain-squared signature of a dilation-slot object, and G_new(x)·G_new(−x) = 4G² [V]: the canonical gain is the two-port geometric mean.

**Ptolemy: §1 and §2 are one object [V].** On the invariant-poles circle, for two measure points: L_C(1)·L_U(2) = L_C(2)·L_U(1) + 2·|M₁M₂| — Ptolemy's theorem on the pole-chord quadrilateral. In coin terms the M-to-M chord is 2·(√(p₁q₂) − √(q₁p₂)): **the cross-budget terms are the chords' Ptolemy legs, and the pair-budget of §1(ii) is the angle-subtraction identity in the abandoned geometry.** The cross-budget constraint is a classical theorem in G-new's chart. That is, I think, the actual content the 2025 construction was reaching for.

**Fences.** (a) Adopt as *coordinate* (odds/SWR gauge, amplitude coin), never as a rival gamma — the G²-slot collision is exactly the E2/§311 error class, now with a documented home. (b) It does not reach the off-budget sheets: the u ↦ 1/u elliptic/Wick sheet and the x² > 1 activity exit have complex coin values; G-new's "other side" is the second sign-sector of the on-budget circle, not the off-budget lifts. (c) The source's §4–5 (transfinite investiture; X_inv dynamics) stays retired per the Tier-5.2 fence — nothing here reopens it, and the §5 "invariants as relational units" paragraph reads in hindsight as the address-vs-value discipline, stated early. (d) Curio, fenced per convention: G_new(x_s) = 1/(1−ρ) = log_{3/2}3 = 2.70951 — near e (2.71828) and 3/ln3 (2.73072), adjacent to the radix-economy bracket [signed-digit §1(ii)]; proximity is noise until shown otherwise.

---

## 3. Queue offerings

1. Serves seam_toll E.1 (the G²(x₁)·x₂-form wiring recheck): the taxonomy home proposed here — classify recorded wirings by which pair-budget point they select and which ledger (spend/waste/angle) they extremize.
2. Serves faces_seam queue (iv): the Gudermannian join is native to the odds gauge; tanh(dr) = r vs e^r = r vs φ = F[φ] can be read as fixed points on the three charts (x, odds, rung).
3. Budget-associate family: does the pair-budget iterate (pair of pairs), and does its contraction rate join the inventory {1/(2√2), 1/√2, 1/√(2 ln 2)}? [O]
4. [C, one-line check] Whether the twisted/Borel seam weighting (faces_seam queue i) is the odds-gauge holonomy — the ledger-weighted cocycle already composes multiplicatively, which is the height's composition law, not the gain's.

*Scripts: `verify_cross_budget_gnew.py` (44 [V] marks). Filed 2026-07-19 with Will's countersign (this conversation); Delta 1 (parity chart group, same day) offered separately, countersign pending.*
