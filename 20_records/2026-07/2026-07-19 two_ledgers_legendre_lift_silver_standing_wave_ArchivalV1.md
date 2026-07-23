# 2026-07-19 (late) — Two ledgers (convergent waste placed); the Legendre lift as a budget-valued operation; the silver standing wave [ActiveV1]

*Reins session following the seam/ledger record (same date). Three results: the convergent-waste property corresponded to existing framework roles (with one of my own conjectures refuted en route); a new budget-associate operation with a new rate constant; and an exact chart translation showing the Liu partition's standing-wave signature is the silver inventory. All [V] via `audit4.py` (mpmath, 30 dps). Tiers per convention.*

---

## 1. Convergent waste, corresponded [V/id/T]

**1.1 The two ledgers.** Along any cascade schedule, two quantities ride together: **capacity spend** c_m = −Δln u (first-order, exact/potential-like — telescoping; U1's "per-rung ledger is chart, the total is invariant" [07-03]) and **waste** KL_m = KL(rung_{m+1} ‖ rung_m) (second-order, metric/quadratic — ½·Fisher·Δθ² in the small-step regime [V: KL·2m³ → 1]). Correspondences to existing roles:

- **Waste = the step's sufficiency deficit = DPI gap = per-step anholonomy** — U3's "one number, three names" [07-03], applied to the schedule itself. **Convergent waste = summable step-anholonomy = asymptotic sufficiency of the schedule**: adjacent rungs become asymptotically sufficient statistics (Petz-recoverable) for one another while the invariant ledger grows without bound.
- **Thermodynamic reading [T, id]:** capacity = reversible work along the symplectic conjugate; waste = dissipation along the gradient flow (the metriplectic split, 6-17); convergent waste = **asymptotic reversibility** — the horse–carrot structure (excess dissipation ~ ½·Fisher·Δ² per step; a fixed thermodynamic length traversed in shrinking steps dissipates finitely). R3.7's "asymptotically quasi-static" acquires its precise grounding.
- **Chart-dependence:** total capacity is order-invariant across chains [U1]; total waste is *not* — waste is the price of the particular chart/schedule. The two ledgers are the invariant/chart split of the cascade, in currency form.

**1.2 The waste-regime trichotomy [V].** Computed: harmonic tower — divergent spend (ln(M+1)), **summable waste** (Σ KL = 0.091365 nats total, converged at 2·10⁵ rungs); halving tower (golden start) — both ledgers finite (0.2496 waste, 0.9624 = spend); constant/GMC tower — linear spend, **exactly zero drift waste** (adjacent budgets identical); the Sturmian seam — **linear waste** (constant toll 0.0500 bits/symbol: the stationary tax, priced by Baker/irrationality). Three waste regimes: zero / summable / linear-stationary.

**1.3 Refutation, logged (drift-honesty).** My 07-19 aside conjecture — "divergent waste = where certificates must fail / the GMC discriminant" — is **refuted as stated** [V]: the GMC-class (constant) wiring has *zero* drift waste. Chaos load is carried by the *spend* axis (cumulative increment variance), orthogonal to roughness. Corrected classification: schedules live on a two-axis plane (spend growth × waste sum); GMC needs linear spend and is indifferent to waste; the certificate question, if it connects at all, connects elsewhere [O, deflated]. Consolidation inflection: prior (conjecture, exploratory) → new (refuted by direct computation) | trigger: computing the constant tower's adjacent KL | σ: medium | healthy reversal, evidence-coupled.

## 2. The Legendre lift: a budget-valued operation with a new rate constant [V; nowhere-in-corpus]

For any amplitude x, the fair-coin cross-entropy decomposition induces a **meta-budget**: with p = (1+x)/2,

  x_meta² := KL(Bern(p) ‖ Bern(½)) (bits), u_meta := H₂(p), and **x_meta² + u_meta = 1 exactly for every x** [V to 12 digits] — CE to the fair coin is identically 1 bit.

So the Legendre transform of the capacity potential (parent §5) is not just a number at each point — it is a **budget-valued map** x ↦ x_meta: the meta-signal is the tilt's divergence, the meta-noise its entropy. (The seam instance is faces_seam's own dictionary: toll = x²_meta, dimension = u_meta — the seam's "D = u transplant" is this lift evaluated at x_s = log₃(4/3).) Properties [V]:

- **Contraction:** x_meta < x on (0,1), fixed points only {0, 1}; a new peel ("the Legendre peel").
- **Rate constant:** x_meta/x → **1/√(2 ln 2) = 0.849321800** at the noise pole (verified to 9 digits; Pinsker-adjacent quadratic regime). Rate inventory placement: halving rung 1/√2 = 0.7071 < Legendre peel 0.8493 < 1; beside the recorded self-dual contraction 1/(2√2) = 0.354 [errata C2]. The inventory of contraction constants is growing a structure of its own [O: is 1/√(2 ln 2) the noise-pole rate of a recognizable corpus family? Note (2 ln 2) is the fair-coin Fisher information at p = ½ in the x-chart — the constant is 1/√Fisher, so the Legendre peel's rate is the fair coin's own Cramér–Rao scale; id-grade, stated no stronger.]
- Orbit from the seam amplitude: 0.26186 → 0.22371 → 0.19081 → 0.16255 → … (geometric tail at 0.8493).

## 3. The silver standing wave [V, exact; the Smith-thread payoff]

Translating the recorded Liu/silver partition (A, R, T) = (2√2−2, 3−2√2, 0) [R3.5 F5; interior spine "silver partition"] into the standing-wave chart (x = |Γ|, per the committed dictionary):

| standing-wave observable | exact value | recorded identity |
|---|---|---|
| |Γ| = √(3−2√2) | **√2 − 1** | the silver modulus k₂ — a recorded CM value |
| |V|max/|V₊| = 1+x | **√2** | one halving rung below the presumptive 2 |
| |V|min/|V₊| = 1−x | **2−√2** | **γ\*** — the node depth at the Liu point is the framework's central constant |
| SWR = max/min | **1+√2** | the silver ratio; e^{2η} with η = ½ln(1+√2) = **ρ\*/4** [R3.9's silver rapidity, quartered] |
| max·min | **2√2−2** | = u = A (T = 0): the product invariant *is* the Liu absorption |

All machine-exact [V]; pure chart algebra, no new physics computed — so the CCEM pre-registration (previous record §D) is untouched: calls remain to be locked before any electromagnetic computation.

**Reading.** The two presumptive limits are S-dual numerators of one passivity statement (½ for the dissipative chart, 2× for the amplitude chart). Their extremal points sort by partition: the *symmetric* shunt extremum (g = 2: A = ½, R = T = ¼) sits at **|Γ| = ½, u = ¾ — the trivial-cycle partition** [faces_seam §1]; the *asymmetric two-channel* (Liu) extremum sits at **silver**. Lore point = trivial cycle; broken-lore point = silver [id, pattern-grade]. And Will's translated players resolve exactly: "amplitude ≤ ~2×" is the passivity numerator; the Liu-analogue does not break 2× — it lands the amplitude on √2, the *half-rung* of 2, with the minimum bottoming at γ\*. The break of the ½-lore in one chart is the *halving* of the 2-lore in the dual chart.

## 4. Queue

(1) Lock the CCEM calls (parabolic-failure call primary) in a dedicated derivation pass; then run. (2) The Legendre peel's composition with the halving rung and the nesting map (does the rate inventory {0.354, 0.7071, 0.8493} close under composition into a recognizable family?). (3) Whether summable-waste is the property that licenses U1-style order-freedom in practice (waste bounds the chart-dependence of physical implementations) [C]. (4) Carried from previous record: G²(x₁)·x₂ wiring recheck; convergent-waste vs formation-ledger discrete rungs. Scripts: `audit4.py`.
