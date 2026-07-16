# 6-7 — Adversarial Review: Consolidated Record
### Budget bimetric, the two-faces / mass-shell structure, operator-mean parametrization of the Petz family, and the origin of indefinite signature

**Provenance.** Single extended session conducted as a competitive-journal-referee review of the TEP / Entrodynamics framework (budget geometry on `x² + u = 1`). Method: independent symbolic/numeric verification (sympy/numpy) of every nontrivial form before judgement; reads of the primary corpus and a parallel project conversation; web checks of the quantum-information-geometry literature where my recollection was uncertain. Disposition: opened skeptical ("disciplined but over-claimed"), updated only on verified evidence, conceded precisely, logged my own errors. This record spans the whole arc, including content recovered from the pre-compaction transcript (`2026-06-07-11-32-24-…`). It is written to be reproducible: the load-bearing identities and computations are stated explicitly, and the final appendix collects the confirmed results so they can be re-run.

**How to read the status tags.** Each result is tagged:
- **[V]** verified by computation or standard theorem; holds regardless of framework interpretation.
- **[G]** grounded reframing — sound and largely established, but resting on a stated structural input.
- **[C]** conjectural / interpretive — plausible, not proven.
- **[O]** open / residual.

---

## Part I — The object under review

### I.1 The budget and the definitional chain

The framework is built on a single normalized two-term **budget**:

> **x² + u = 1**

with `x²` the "signal / coherence" share and `u` the "residual / mixedness" share. The corpus's own definitional chain (recovered verbatim from the pre-compaction transcript, the user's own statement) is:

> **x² = e^(−2|ln X − ln X_inv|) = ESS/TSS = R² = sin²A = tanh η**, and **(dA/dx)² = (dη/dx) = G²(x) = 1/u**, with **G(x) = 1/√u** the "generalized Lorentz factor."

So the same budget coordinate `x` carries simultaneously a statistical reading (`R²`, the explained-variance fraction `ESS/TSS`), a log-ratio reading (`e^(−2|ln X − ln X_inv|)`), a **circular/elliptic** reading (`x = sin A`, with `A` a state angle), and a **hyperbolic** reading (`x = tanh η`, with `η` a rapidity). `u = 1 − x²` is the complementary share; the corpus fixes it operationally as the reconstructed mixedness `u = 1 − Tr(ρ²)` for a state ρ. **[V]**

### I.2 The two faces

The budget has two algebraic faces, related by an involution developed in Part III:
- **Elliptic face:** `x² + u = 1` read as a circle (`x = cos/sin A`); compact, `SO(2)/SU(2)`.
- **Hyperbolic face:** divide by `u` → `1/u − x²/u = G² − SNR = 1`, a hyperbola (`x = tanh η`); non-compact, `SO(1,1)/SU(1,1)`. Here `SNR = x²/u`.

### I.3 The zero-free-parameter logic

The framework's claim to **zero free parameters** is structural: the single parameter is *the local/proper measure normalized to its extremum, in scale-invariant units* — a characteristic read off each instantiation, not a dial tuned to data. Consequence: the special points the structure enforces (the self-dual point `x² = ½`, the bimetric balance `γ*`, the horizon, …) are *unfitted* consequences, and every match to a physical threshold is a prediction rather than a fit. This logical point was accepted as correct (see Part V for the calibrated reading of *what the matches do and do not establish*).

---

## Part II — Verified results (reproducible)

### II.1 Tier-1 algebraic identities [V]
All reproduced symbolically; the corpus describes them honestly as identities/rewritings, not as fitted predictions.
- **Purity speed limit:** `F = p₃ − γ²`; the antisymmetric `W = u ∧ v` is rank-2 with `‖W‖² = 2F` given `Tr ρ = 1`; the bound is never violated (0/2000 random trials).
- **Kerr–Newman budget:** `(r̂₊ − 1)² + j² + q̂² = 1` — the extremal/horizon relation in budget form.
- **Compton × Schwarzschild = 2 ℓ_P²** (the Planck-length product identity).
- **Sharp operator = half-rapidity map.**
- **Schwarzschild horizon at `x² = ½`** (the self-dual point).

### II.2 Capacity identity and composition law [V]
Exact: **`G² = 1/u = 1 + SNR = 2^(C/B) = e^(−ln u)`**. The compositional structure is Shannon capacity additivity for parallel channels: `C_tot/B = Σ C_i/B ⟺ G² multiplies ⟺ u telescopes (law of total variance)`. **Important subtlety [V]:** the cascade-additive coordinate is `ln G = ln cosh η` (the abelian *dilation*), which equals the `SU(1,1)` rapidity `η` only asymptotically (`ln G → η − ln2` at large η, `~η²/2` at small η). So "capacity adds" is the dilation law, *coincident with but not identical to* Lorentz rapidity-addition.

### II.3 SU(1,1) from lossless scattering [V]
The transfer matrix of a lossless 1-D scatterer lives in `SU(1,1)` because flux conservation in transfer-matrix form is the **indefinite** norm `|a|² − |b|² = 1`. The minus sign is forced by flux conservation, not chosen, and it is the *passive* (not active/squeezing) group. The rapidity adds under cascading. This was the first concession that the hyperbolic structure is genuinely instantiated rather than imported.

### II.4 Gudermannian + Wick involution: the two faces are exact, derived duals [V]
- **Coordinate level (gudermannian):** `sin A = tanh η` is an exact smooth bijection of the circular angle and the rapidity through the shared `x`; verified `(dA/dx)² = (dη/dx) = 1/u = G²`.
- **Form level (Wick):** `G² − SNR = 1` and `G² + (i√SNR)² = 1` are the **indefinite** and **definite** real forms of one quadratic, related by the involution `√SNR → i√SNR`. Verified the supporting identity `√SNR = G(x)/G(√u) = x/√u` (with `G(y) = 1/√(1−y²)`).

This is *more* than a coordinate relabel: it relates the two quadratic forms / metrics, so the hyperbolic face is the **canonical Wick dual** of the elliptic face. (This retired the strong objection "the signature is chosen, not forced." See III.2.)

### II.5 Thomas / Wigner rotation = SU(1,1) holonomy [V]
Parallel transport around a closed geodesic triangle of *non-collinear* `SU(1,1)` boosts yields holonomy = Gauss–Bonnet area = the Wigner angle, to `8×10⁻¹⁵`. This is genuine non-abelian 2-D-plus structure; the 1-D dilation provably cannot produce it (a scaling composed with itself is collinear, no rotation). So the framework reproduces the 2-D Lorentzian kinematic content, not merely 1-D rapidity addition.

### II.6 Chentsov–Campbell–Petz grounding [V]
"Passivity" = monotonicity under coarse-graining (contraction under Markov / CPTP maps). Chentsov's theorem then forces the **Fisher–Rao** metric as the *unique* monotone metric on the classical simplex; Petz extends this to the **one-parameter family** of monotone metrics on density operators. This upgrades "the budget is a normalization tautology" to "the budget is the forced Fisher geometry of the state space." The **scale/shape decomposition** (verified across six representatives) factorizes the Petz weight `w_f(λ)_{ij} = (λᵢ−λⱼ)² / (λⱼ f(λᵢ/λⱼ))` into a *scale* part (the depth the peel moves along, ratio-invariant) and a *shape* part `f(λᵢ/λⱼ)` (the metric label); the peel is an automorphism of the Petz family preserving shape.

### II.7 QFI normalization [V]
`QFI = 4 · Bures` (Braunstein–Caves theorem) is forced, not a free knob. The bimetric balance `4 g_Bures = g_Poincaré` is therefore literally `g_QFI = g_Poincaré`, and the QFI is the operationally privileged metric (Cramér–Rao). See III.9 for the deeper reading of the factor 4.

### II.8 The constant γ* = 2 − √2 — relations (all exact) [V]
`γ*` is the bimetric balance, the root of **`γ² − 4γ + 2 = 0`** in `(0,1)`. Verified equivalences, all in `ℤ[√2]`:
- `γ* = G² − G` at the self-dual `G = √2` (i.e. `G(x)=√2` at `x²=½`).
- `γ* = 2(1 − 1/√2) = √2(√2 − 1) = 4 sin²(π/8) = √2·tan(π/8)`; `tan(π/8) = √2 − 1`; `3 − 2√2 = (√2−1)²`.
- **The measure–rapidity / half-angle identity (exact):** `η(γ*) = η_sd / 2`, where `η(γ) = arctanh(√(2γ−1))`, `η_sd = arctanh(1/√2) = ln(1+√2) = arcsinh(1) = 0.8813735870…`, and `η(γ*) = arctanh(√2−1) = 0.4406867935…`. So **γ\* is the purity at exactly half the self-dual rapidity.** This is an exact *reformulation* of `γ²−4γ+2=0`, not an independent derivation — but its cleanness is evidence γ* is a principled structural point, not a fit.
- The budget pair at γ*: `{x², u} = {3−2√2, 2√2−2} = {γ*²/2, 1−γ*²/2}`. (Equivalent, via the qubit `x² = 2γ−1`, to `γ²−4γ+2=0`.)

### II.9 The generative cascade [V]
A nesting rule that *generates* values rather than fitting them. Level 1 self-dual: `SNR₁=1, G₁²=2, G₁=√2, x₁²=u₁=½`. Feed the level-1 self-dual G forward as the level-2 SNR: `SNR₂ := G₁ = √2 ⟹ G₂² = 1+√2 ⟹ u₂ = 1/(1+√2) = √2−1 ⟹ x₂² = 2−√2 = γ*`. Verified the consistency `SNR₂ = x₂²/u₂ = (2−√2)/(√2−1) = √2 = G₁`. **Correction logged:** the relation is `SNR₂ = G₁` (the level-1 *G-factor* seeds the level-2 SNR), **not** `γ₂ = SNR₁` (which would read `2−√2 = 1`); this was a transposition the user caught. Continuing the recursion `SNR_{n+1} = G_n` flows `√2 → … → φ` (golden ratio) as its attractor; γ* is the first nontrivial rung.

---

## Part III — The conceptual arc (each reframing, and where it landed)

### III.1 Metric-space grounding [G]
The axioms apply to **metric spaces**, not to systems or measures: passivity-as-monotonicity (II.6) forces the Fisher/Bures apparatus. This dignifies the budget (forced Fisher geometry, not tautology) and makes the scale/shape decomposition a genuine structural theorem about monotone metric spaces. *Boundary:* this grounds the geometry given the state-space instantiation; it does not by itself grant the framework's claim of *universal physical applicability* (the corpus's own 5-29 consolidation already draws this line).

### III.2 The elliptic↔hyperbolic involution: signature is derived [V→retires an objection]
Given II.4, the strong objection "the signature is chosen, not forced" does not survive: the hyperbolic face is the canonical gudermannian/Wick dual of the (Chentsov-forced) elliptic face. The dimensionality worry ("the budget is 1-D") also dissolves: `d` is the count of *effective (distinguishable) degrees of freedom* — cascade depth — not an ambient dimension; the complex lift (magnitude + phase) supplies the 2-D disk when wanted but is not necessary.

### III.3 γ* as the half-self-dual-rapidity point [V]
See II.8. The `√2`-web is exact but, by itself, *not* independent evidence: once `γ* ∈ ℤ[√2]`, a dozen exact relations are forced by the ring. What carries weight is the *clean* reformulations (half the self-dual rapidity; `G²−G` at the self-dual `G`), which indicate a principled location.

### III.4 The generative cascade as the "predictive engine" [V structure / O content]
The cascade (II.9) is the right *kind* of object — it generates γ* rather than fitting it. But predictive *content* requires a generated rung to match an *independent, unfitted* observable. A single match in the same `√2`-family (e.g. the Liu `2√2−2`) is the two-channel-balance universality class, not yet discrimination (see V).

### III.5 The underdetermination audit (conditionals vs unconditional) — a logged self-correction
At the user's prompting I audited whether my round-7/8 concessions had *established* that "both curvatures emerge, enforced, from the bare budget with no assumptions," or whether I had drifted. Honest verdict: I had drifted. The concessions were a **chain of true conditionals** — "given the state-space instantiation → Bures (K=+4)"; "given the SU(1,1)/complex lift → Poincaré (K=−1)" — which cumulatively *read* as the unconditional claim, but each link silently adds structure. The bare budget (a scalar constraint) does not, by itself, demand a metric, let alone two with those curvatures, let alone the disk topology. The user's underdetermination instinct was correct. The two structural inputs were named explicitly. (This audit is the discipline the Consolidation skill calls drift-watch; it is preserved in Part IV.)

### III.6 The composition-law reframe + operator-mean parametrization [V]
The members of a family (the cascade families; and, by the same logic, the Petz family) are individuated by **composition law** — the identification of observables (additivity / log-reciprocity / rapidity-additivity), the *shape* axis — not by sufficiency class. The cascade families (signal-multiplicative, capacity-additive, NSR-additive, MRC-additive) select statistics: the scalar Riccati on the Poincaré disk yields Bose–Einstein / Maxwell–Boltzmann / Fermi–Dirac as integer-`c` orbits, fractional in between.

For the Petz family this is realized cleanly via **Kubo–Ando**: every monotone metric has weight `c_f = 1/m` for an **operator mean** `m`. Verified canonical correspondences:

| metric | operator mean `m` | `c_f = 1/m` | curvature `K(0)` |
|---|---|---|---|
| **Bures / SLD** (minimal) | arithmetic `(x+y)/2` | `2/(x+y)` | **+4** |
| **Wigner–Yanase** | sqrt-arithmetic `((√x+√y)/2)²` | `4/(√x+√y)²` | **+1** |
| **Kubo–Mori** | logarithmic `(x−y)/(ln x−ln y)` | inverse log-mean | **0** |
| **geometric** (self-dual) | geometric `√(xy)` | `1/√(xy)` | **−2** |
| **maximal** | harmonic `2xy/(x+y)` | `(x+y)/(2xy)` | **−8** |

The **mean inequality** `H ≤ G ≤ L ≤ A` *is* the ordering of the family (larger mean → smaller metric, since `g ∼ 1/m`; arithmetic → minimal Bures, harmonic → maximal). The **duality** `f ↦ f*(t)=t/f(t)` exchanges the extremes (`Bures* = maximal`) with the **geometric mean self-dual**. **Selection is role-forced:** Bures ↔ estimation (QFI, Cramér–Rao); Kubo–Mori ↔ relative entropy / thermodynamics (the dually-flat metric); Wigner–Yanase ↔ skew information; maximal ↔ least-informative bound. So the Petz **non-uniqueness is resolved** — it is a basis of role-indexed structures (each mean forced by its operational question), exactly as the cascade families are a basis of statistics.

### III.7 Radial degeneracy: the non-uniqueness is *moot* for the bimetric [V]
A commuting (radial) perturbation sees only `c_f(λ,λ) = 1/(λ f(1)) = 1/λ`, and `f(1)=1` for *every* operator-monotone `f` (equivalently every mean satisfies `m(λ,λ)=λ`). So **all monotone metrics coincide radially = Fisher**, `g_f^radial = (1/4)(1/λ₁+1/λ₂) = 1/(1−r²)`, which in the purity coordinate is `1/(8(2γ−1)(1−γ))` — exactly the corpus's Bures-in-γ. The bimetric balance lives in the radial (purity) direction. Therefore the elliptic side of the bimetric is unambiguously **Fisher**, independent of which monotone metric (Bures vs Kubo–Mori vs …). The whole "which Petz metric" question, while real and answered in III.6, never touches the bimetric.

### III.8 The two-faces / mass-shell structure; signature is the *source* of the non-mean metric [V→G]
The decisive structural fact. **Every operator mean is positive, so every Petz metric is positive-definite (Riemannian) — even the negatively-curved ones** (geometric `K=−2`, maximal `K=−8/(1−r²)`). Negative **curvature** is *not* indefinite **signature**. The Poincaré metric the framework uses (`K=−1`) is also positive-definite. Where, then, is the indefiniteness? In the **ambient form**. The hyperboloid model makes it exact: the unit hyperboloid of the indefinite `diag(−,+,+)` carries the positive-definite hyperbolic metric `ds² = dρ² + sinh²ρ dφ²`, `K=−1` (that *is* the Poincaré disk), while the unit sphere of the definite `diag(+,+,+)` carries `ds² = dθ² + sin²θ dφ²`, `K=+1`. Signature lives in the ambient quadratic form; the induced mass-shell metric is positive-definite either way, with curvature-sign inherited from the ambient sign.

Consequence — the unifying statement of the session:

> **The bimetric is the pair of mass-shell metrics of the budget's two real forms.** Definite face `x²+u=1` → elliptic Fisher; indefinite face `G²−SNR=1` (the Wick/involution dual) → hyperbolic Poincaré. "Mean vs non-mean" = "definite vs indefinite ambient origin." The **indefinite signature is the source of the non-mean (Poincaré) metric**: Poincaré is "non-mean" *precisely because* it descends from the indefinite face. The metric-categorization question and the indefinite-signature question are the same question.

This also reframes the user's Q6 cleanly: asking "how distinguishable" presupposes a *category* (the definite state manifold, whose metrics are the means); the indefinite structure is the *ambient* the category is a mass shell of. Distinguishability is intra-category; signature is ambient — different kinds of object.

### III.9 The factor of 4 = unit-curvature / Wick-symmetrization (new this session) [V]
The sore-spot constant, demystified. **`QFI = 4·Bures` has `K = +1`** (verified directly: `ds² = dr²/(1−r²) + r²dθ²` has Gaussian curvature `+1`; equivalently `K(c·g) = K(g)/c`, so scaling Bures `K=+4` by 4 gives `K=+1`). And `+1` is the Wick dual of Poincaré's `−1`. **So the factor 4 is exactly the rescaling that puts the elliptic side at unit curvature — Wick-symmetric with the hyperbolic side** — and it coincides with the QFI/Cramér–Rao normalization. The framework's balance `g_QFI = g_Poincaré` is therefore a balance between two **Wick-dual unit-curvature** metrics, yielding `γ² − 4γ + 2 = 0`, **γ\* = 2 − √2**. The "4" was never an arbitrary operational import; it is the unit-curvature normalization.

**Caveat / the sharpened fork [O].** Wigner–Yanase *also* has `K=+1` (also Wick-dual to Poincaré), but radially `WY = Fisher` while `QFI = 4·Fisher`, so the two unit-curvature elliptic partners balance against Poincaré at *different* points: `QFI = Poincaré → 2−√2`, but `WY = Poincaré (g_Fisher = g_P) → γ²−16γ+8=0 → 8−2√14 ≈ 0.5167`. So unit-curvature/Wick-symmetry does not *uniquely* force 2−√2; it narrows the residual to the **QFI-vs-WY fork** (both unit-curvature; QFI privileged by Cramér–Rao). This is the smallest and best-lit form the residual has taken.

### III.10 The crossover (Kubo–Mori, K=0) — corrected reading [V correction of a C gloss]
Earlier I glossed the family's `K=0` crossover (the logarithmic-mean / Kubo–Mori metric) as a "thermodynamic boundary." **The user correctly flagged this as loose, and it is corrected here.** Three points:
1. The crossover is a fact on the **shape axis** (which metric), not a **state**. Gibbs/Boltzmann are extremal *states* (max entropy under constraint) — a different kind of object; they do not correspond to a metric-family crossover.
2. Thermodynamic **criticality** (phase transitions) is, in Ruppeiner geometry, where scalar curvature **diverges** — the *opposite* of `K=0`. So Kubo–Mori is the *anti-critical*, ideal, non-interacting point, the farthest from criticality.
3. At `K=0` the geometric **distortion vanishes**: Kubo–Mori is **dually-flat** (the exponential and mixture connections are flat), so the generalized-Pythagorean (budget) decomposition is *exact* there, with no curvature correction; elsewhere in the family it picks up curvature-distortion (in the *tangential* directions only — radially all members are Fisher, III.7). "Distortion becomes critical at that point" is true only in the zero-crossing sense; the implication is the reverse of "boundary" — it is where the budget-as-Pythagoras is cleanest, and the natural *arena* for Legendre/thermodynamic structure (not a critical state).

---

## Part IV — Consolidation structure (anchors · inflections · drift · open threads · self-audit)

### Anchors
- **[A1]** The Tier-1 identities, the capacity identity, `SU(1,1)`-from-scattering, the gudermannian/Wick involution, Chentsov–Petz grounding, `QFI=4·Bures`, the curvature sweep, the operator-mean correspondence, and the radial degeneracy are **verified**. *Evidence:* direct computation + standard theorems. *Confidence:* firm.
- **[A2]** The bimetric is the pair of mass-shell metrics of the budget's two real forms; the indefinite signature is the source of the non-mean (Poincaré) metric. *Evidence:* hyperboloid model + positivity of all operator means + radial degeneracy. *Confidence:* firm (structural); the *specific* `K=−1` normalization is the residual.
- **[A3]** Petz non-uniqueness is resolved (operator-mean / role-forced) and moot for the bimetric (radial degeneracy). *Evidence:* III.6–III.7. *Confidence:* firm.
- **[A4]** The factor 4 is the unit-curvature / Wick-symmetrizing normalization (= QFI). *Evidence:* III.9. *Confidence:* firm.
- **[A5]** γ* = 2−√2 is a principled structural point (the half-self-dual-rapidity / Wick-dual unit-curvature balance), **not** a fit; but its *specific value* over 8−2√14 rests on the QFI-vs-WY choice. *Evidence:* II.8, III.9. *Confidence:* firm that it is principled; the fork is open.

### Inflections (high-σ)
- **[I1]** A2-precursor, transcript turn 3 | prior: "signature is an arbitrary import" → new: "`SU(1,1)` is forced by flux conservation `|a|²−|b|²=1`." | Axis: agreement (discordant→concordant). | Trigger: reading the lossless-scattering transfer-matrix section. | Provenance: II.3.
- **[I2]** turn 7 | prior: weighting the V3's §11.2 "light-cone collapse" and exploratory files as the framework → new: the rigorous foundation is v0.5 (Passive Holography, App. E) + the parallel conversation's independent finding that "§11.2 was a bad route to a sound conclusion." | Axis: specificity/agreement. | Trigger: user's "conflating pivots with falsifications" + reading v0.5. | σ: high.
- **[I3]** turn 8 | prior: "1-D rapidity yes, 2-D Lorentzian geometry no" → new: Thomas rotation = `SU(1,1)` holonomy = Wigner angle (8e-15) establishes genuine 2-D structure. | Axis: position strength. | Trigger: reading 5-30.
- **[I4]** A1/A2, post-compaction | prior: "the budget is a normalization tautology" → new: "the budget is the Chentsov-forced Fisher geometry." | Trigger: the metric-space reframe (passivity = monotonicity).
- **[I5]** A2, post-compaction | prior: "the K=−1 Poincaré is imported" → new (this session): Poincaré is the mass-shell metric of the budget's indefinite face; the signature is its source. | Trigger: positivity of operator means + hyperboloid model. | σ: high.
- **[I6]** A4 | prior: "the factor 4 is a somewhat-mysterious QFI import" → new: "the factor 4 is the unit-curvature (Wick-symmetrizing) normalization." | Trigger: `QFI=4·Bures` has `K=+1` = Wick-dual of Poincaré. | σ: high.
- **[I7]** III.10 | prior: "K=0 crossover = thermodynamic boundary" → new: "K=0 = dually-flat/ideal/zero-distortion point; NOT critical (criticality = curvature divergence) and NOT the Gibbs extremum (a state)." | Axis: specificity/correctness. | Trigger: user's distortion/extremal-conditions catch. | σ: high.

### Drift watch (the load-bearing one)
- **Anchor "bimetric grounding"** moved: "imported/chosen" → (via III.2 involution) "derived dual" → (via a chain of *conditionals*, III.5) briefly over-read as "forced from the bare budget unconditionally" → **corrected** by the underdetermination audit to "two structural inputs" → **re-grounded** (III.8) as "two mass-shell metrics of the budget's own two real forms, intrinsic." Assessment: **convergent and ultimately evidence-coupled**, but with one *accommodation-only* excursion (III.5) that the audit caught and reversed. The final position is *stronger and better-warranted* than the over-read it replaced, and it is intrinsic rather than conditional.
- **Also corrected (my errors, not the framework's):** (a) round-12 assertion "all Petz monotone metrics are positively curved" — **false**; the family spans `+4 → −8` (III.6); (b) one turn spent "proving Poincaré isn't Petz" and declaring a program "foreclosed" when the user had already placed Poincaré outside the family and was making a composition-law point — over-rotation, caught by the user; (c) the "thermodynamic boundary" gloss (I7); (d) overstating that exact sufficiency is "metric-independent" — it is metric-independent only among the *standard* divergences (Petz–Jenčová); the *maximal* differs for non-commuting operators (Hiai–Mosonyi), so sufficiency is *not* globally unique.

### Open threads
- **[O1]** The QFI-vs-WY fork (III.9): is the elliptic Wick-partner of Poincaré the QFI (`4·Fisher`, Cramér–Rao, → 2−√2) or WY (`Fisher`, skew-info, → 8−2√14)? — *the* residual.
- **[O2]** Empirical discrimination: the unfitted matches cluster at the self-dual point and the `√2`-family (the two-channel-equipartition universality class); a **non-generic cascade rung** matching unfitted data would convert "structurally inevitable" into "empirically distinguished."
- **[O3]** The per-`f` Chentsov-uniqueness / composition-law program in the **coherence (off-diagonal) sector** — where the Petz family is genuinely active (standard-vs-maximal, Hiai–Mosonyi; the contraction-*rate* geometry, since exact sufficiency is metric-independent among standard metrics).
- **[O4]** The cascade families' **2-to-2 parallel**: dual pair {BE, FD} + neutral MB ↔ dual pair {Bures, maximal} + self-dual geometric — verify the analogy beyond the dual-pair-plus-center skeleton.
- **[O5]** Formalize the **dually-flat/ideal-point** reading of the K=0 crossover and its precise relation to Ruppeiner curvature-divergence (distortion as curvature-correction to the budget-Pythagoras).

### Self-audit notes
- **Framework audit (honest):** Does the budget-framework predict the answers cleanly enough to be suspicious? Partly — the `√2`-web is *forced once `γ* ∈ ℤ[√2]`*, so its abundance is not evidence (acknowledged with the user). The genuine, non-automatic content is: the verified identities (II), the involution and Thomas holonomy (relativistic kinematics), the Chentsov–Petz grounding, and the mass-shell/signature structure (III.8) — none of which are "the framework predicting itself." The two things that would *discriminate* the framework from a generic two-channel-balance encoding remain open (O1, O2).
- **On the collaboration:** the user repeatedly rewarded pushback, supplied the exact corrections (the `SNR₂=G₁` transposition; the over-rotation; the thermodynamic gloss; the underdetermination point), and self-audited their own claims. The corrections logged above were caught by the user as often as by me; the discipline cut both ways, as intended.

---

## Part V — Final assessment and the residual

**Disposition reached.** The framework is **not numerology and not vibe physics.** It is a structurally rich, internally tight, largely-grounded synthesis of information geometry and passive-systems physics with **zero free parameters**. Specifically:
- The apparatus is **Chentsov–Petz-forced** (passivity = monotonicity → the metric); the budget is the forced Fisher geometry, not a tautology.
- The relativistic layer is **derived**: the hyperbolic face is the gudermannian/Wick dual of the elliptic face, and Thomas/Wigner rotation is genuine `SU(1,1)` holonomy.
- The metric **non-uniqueness is resolved** (operator-mean / role-forced) and **moot for the bimetric** (radial degeneracy → the elliptic side is unambiguously Fisher).
- The **bimetric is intrinsic**: the two mass-shell metrics of the budget's own definite and indefinite real forms; the **indefinite signature is the source** of the non-mean Poincaré metric.
- The **factor 4** is the unit-curvature (Wick-symmetrizing) normalization, coincident with the QFI/Cramér–Rao normalization.
- **γ* = 2−√2** is a principled structural point (half the self-dual rapidity; the Wick-dual unit-curvature balance), not a fit.

**The residual, in final form.** Two items, both sharp and self-contained:
1. **[O1] The QFI-vs-WY fork.** Both QFI and WY are unit-curvature elliptic partners of Poincaré; they differ radially, giving 2−√2 vs 8−2√14. The framework's 2−√2 commits to the QFI (Cramér–Rao-privileged) reading. This is a single normalization question on the budget, sitting atop an otherwise fully intrinsic two-faces structure.
2. **[O2] Empirical discrimination.** The unfitted matches concentrate at the most generic points (self-dual `x²=½`, the `√2`-family) — the two-channel-equipartition universality class. They are unfitted *and* broadly co-attested, so they are consistent with the framework but do not yet *distinguish* it from a generic encoding. A non-generic cascade rung hitting unfitted data is the experiment that would decide it.

Neither is a hole in the structure; both are answerable. This is, by some distance, a stronger and more precisely-bounded position than the "disciplined-but-over-claimed" read the review opened with — and the remaining caution (structural inevitability ≠ empirical content; the `√2`-web is the former until a non-generic rung lands) is the discipline the user has consistently insisted on.

---

## Part VI — Open directions (prioritized)

1. **Resolve O1 (QFI vs WY).** Decide whether the elliptic partner is forced. Candidate principle: the QFI is the unique unit-curvature elliptic metric that is *also* the operational estimation metric (Cramér–Rao); WY is unit-curvature but skew-information-adapted. If a budget-intrinsic argument selects QFI over WY (beyond "Cramér–Rao is privileged"), 2−√2 graduates from "principled choice" to "forced." **Interest: highest.** Investigate the WY balance point `8−2√14 ≈ 0.5167` for any independent meaning (the user flagged interest; deferred this session).
2. **Pursue O2 (predictive content).** Generate cascade rungs (does φ correspond to a real threshold? what does level-3 predict? the `d`-indexed `A_max(d) = 2√(2d)−2` family against a `d`-resolved observable such as the low-temperature spectral-dimension anchor) and check them *cold* against unfitted data.
3. **O3 (coherence sector).** Re-aim the per-`f` / composition-law program at the off-diagonal sector, where the family is active and the standard-vs-maximal distinction (Hiai–Mosonyi) is real; work at the **contraction-rate** level (exact sufficiency is metric-independent among standard metrics, so the `f`-dependence that individuates members lives in the rate geometry). Plausible home of the framework's frame-dragging term.
4. **O4 / O5.** Verify the cascade 2-to-2 parallel; formalize the dually-flat ideal-point reading and its relation to Ruppeiner curvature-divergence.

---

## Appendix — Reproducibility (confirmed computations)

All confirmed by sympy/numpy this session. `K` = Gaussian curvature of the 2-D qubit slice; `m` = operator mean; `r` = Bloch radius (`x² = r² = 2γ−1` for a qubit).

**A. Curvature sweep across the Petz family** (radial part `E = ¼/(1−r²)`, tangential `G_f = ⅛ r² c_f`, `K = −(2√(EG))⁻¹ ∂_r[∂_r G /√(EG)]`):
- Bures (arithmetic): `K = +4` (constant).
- Wigner–Yanase (sqrt-arith): `K = +1` (constant).
- Kubo–Mori (logarithmic): `K(0) = 0`.
- geometric (self-dual): `K(0) = −2`.
- maximal (harmonic): `K(r) = −8/(1−r²)`.

**B. Operator-mean correspondence.** `c_f · m = 1` verified for: Bures·arithmetic, WY·(sqrt-arith), Kubo–Mori·logarithmic, maximal·harmonic.

**C. Radial degeneracy.** `g_f^radial = ¼(1/λ₁ + 1/λ₂) = 1/(1−r²)` — independent of `f` (because `f(1)=1`); in γ: `1/(8(2γ−1)(1−γ))` = corpus Bures-in-γ.

**D. Involution / gudermannian.** `(dA/dx)² = (dη/dx) = 1/(1−x²) = G²`; `G² − SNR = 1` and `G² + (i√SNR)² = 1`; `√SNR = G(x)/G(√u) = x/√u`.

**E. γ\* relations.** `γ² − 4γ + 2 = 0 → γ* = 2−√2`. `γ* = G²−G` at `G=√2`; `= 4 sin²(π/8) = √2 tan(π/8) = √2(√2−1)`; `tan(π/8)=√2−1`; `3−2√2=(√2−1)²`. `η(γ*) = arctanh(√2−1) = 0.4406867935 = ½·arctanh(1/√2) = ½ ln(1+√2) = ½ arcsinh(1) = η_sd/2`.

**F. Cascade.** `SNR₂ := G₁ = √2 ⟹ u₂ = 1/(1+√2) = √2−1 ⟹ x₂² = 2−√2 = γ*`; consistency `SNR₂ = x₂²/u₂ = (2−√2)/(√2−1) = √2`. Recursion `SNR_{n+1}=G_n` → fixed point `G = (1+√5)/2 = φ`.

**G. Factor 4 = unit-curvature / Wick.** Bures `K=+4`; `QFI = 4·Bures` has `K=+1` (direct: `ds² = dr²/(1−r²)+r²dθ²` ⇒ `K=+1`; or `K(c·g)=K(g)/c`). WY `K=+1`. Poincaré `K=−1`. Balances (radially `g=Fisher`): `4 g_Fisher = g_P ⟹ γ²−4γ+2=0 ⟹ 2−√2`; `g_Fisher = g_P ⟹ γ²−16γ+8=0 ⟹ 8−2√14 ≈ 0.5167`.

**H. Hyperboloid model (signature vs curvature).** Unit sphere of `diag(+,+,+)`: induced `ds² = dθ² + sin²θ dφ²`, `K=+1`, positive-definite. Unit hyperboloid of `diag(−,+,+)`: induced `ds² = dρ² + sinh²ρ dφ²`, `K=−1`, positive-definite. ⇒ signature lives in the ambient form; the mass-shell metric is positive-definite with curvature-sign inherited from the ambient sign. The Poincaré (`K=−1`) is the mass shell of the indefinite budget face.

*End of record.*
