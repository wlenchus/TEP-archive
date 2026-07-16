# Circuit Calculus, Composition Regimes, and Role-Agnosticism

*A consolidated record of findings from the May 2026 thread. Working notes — not a paper.*

---

## Scope

This document records three connected results that emerged from testing the framework's role-agnosticism principle against concrete reassignments. The findings are:

1. **Two distinct composition regimes** are admissible within the framework's role-agnostic apparatus: capacity-additive (cascade physics) and MRC-additive (parallel coherent combining). Both produce Lorentz-structured budgets; they differ in which functional of SNR is the additive composition rapidity.

2. **Each regime corresponds to a real physical setup.** Capacity-additive matches Shannon-additive cascade physics where impedance multiplies. MRC-additive matches signal-power-additive coherent diversity combining.

3. **The framework provides an explicit circuit calculus** with topology-dependent reduction rules, structurally analogous to Kirchhoff's series-parallel duality.

These findings extend the role-agnosticism principle from "any info-monotone metric admits the framework's apparatus" to "the framework's apparatus generates distinct physical regimes from the same algebraic backbone, with the regime selected by the physical composition law operative in the system being described."

---

## 1. The two regimes

### 1.1 Capacity-additive composition

**Composition rule:** `(1 + SNR_AB) = (1 + SNR_A)(1 + SNR_B)`

Equivalently: `SNR_AB = SNR_A + SNR_B + SNR_A·SNR_B` (cross-term explicit).

**Additive rapidity:** `η_C = ln(1 + SNR)`, identifiable with Shannon channel capacity per bandwidth (modulo a factor of `ln 2`).

**Budget variable:** `x² = SNR/(1+SNR) = ζ²/(1+ζ²)` — the framework's standard reading.

**Lorentz factor:** `G²(x) = 1/(1-x²) = 1 + SNR`.

**Physical regime:** Cascade composition where impedances multiply. Capacities of subsystems add. Independent parallel channels under independent coding. Standard for DHO chains, optical impedance matching of cascaded sections, multi-stage transmission networks.

This is the framework's *standard* reading — the parameterization V2 uses by default. The cascade physics fixes the rapidity choice as `η_C = ln(1+SNR)`, which is why the standard parameterization works for DHO physics: cascade impedance multiplication forces capacity additivity.

### 1.2 MRC-additive composition

**Composition rule:** `SNR_AB = SNR_A + SNR_B`

**Additive rapidity:** `η_M = SNR` directly.

**Budget variable:** `x = tanh(SNR)`, with `x² = tanh²(SNR)`.

**Lorentz factor:** `cosh(SNR)`, with `1/γ² = sech²(SNR)`.

**Composition law for x:** Verified to machine precision —
`x_AB = (x_A + x_B) / (1 + x_A·x_B)`
exactly the special-relativistic velocity-addition formula.

**Physical regime:** Maximum-ratio combining (MRC) of independent parallel channels. Each branch contributes signal-power additively; rapidity = SNR adds directly. Coherent diversity combining in communication theory. Different from cascade composition.

### 1.3 Mapping table for MRC-Lorentz reading

| Standard SR | MRC-Lorentz reading |
|---|---|
| Rapidity η_SR | SNR (additive in MRC) |
| Velocity v/c | tanh(SNR) (soft decision magnitude) |
| Lorentz factor γ | cosh(SNR) |
| 1/γ² = 1−v²/c² | sech²(SNR) (residual uncertainty) |
| Velocity addition | MRC parallel composition |
| Boost ∘ boost | Combine diversity branches |
| Speed of light c | Hard-decision saturation (tanh(SNR)→1 as SNR→∞) |

The "speed-of-light limit" `tanh(SNR) → 1` is the hard-decision saturation regime where soft bits become deterministic ±1. Sub-luminal corresponds to soft (probabilistic) decision regime.

### 1.4 Relation between the regimes

Capacity-additive and MRC-additive are related by:

`η_C = ln(1 + η_M)`

This is a logarithmic relation, not a symplectic conjugacy. The two regimes are *structurally dual* in the multiplicative-vs-additive-on-(1+SNR) sense, with logarithm bridging them. They share the same budget identity x² + u = 1 but with different rapidity conventions and hence different composition laws.

The same algebraic backbone (the budget identity) supports both regimes simultaneously. Which regime applies in a given physical setup is determined by the physical composition law operative in that setup, not by anything internal to the framework's apparatus.

---

## 2. The parallel-resistance / harmonic-combination identification

A separate substantive observation under capacity-additive composition:

**Theorem (verified algebraically and numerically).** *Under capacity-additive composition, the equivalent single-channel SNR for two independent parallel channels combined under independent coding is the parallel-resistance / harmonic combination:*

`SNR_eq = SNR_A · SNR_B / (SNR_A + SNR_B) = 1/(1/SNR_A + 1/SNR_B)`

*and the corresponding Lorentz factor satisfies:*

`G²_eq = 1 + SNR_eq = SNR_AB / (SNR_A + SNR_B)`

This identifies three equivalent readings of the same structural object under capacity-additive composition:

- Capacity-additive Shannon composition (information theory)
- Parallel-resistance physical combining (electrical / impedance theory)
- Framework's affine-conservation identity G² − SNR = 1 in the new frame

The harmonic combination `SNR_A·SNR_B/(SNR_A+SNR_B)` is bounded above by `min(SNR_A, SNR_B)` (since harmonic ≤ minimum). So adding noisy channels in parallel under independent coding produces an effective channel whose SNR is bounded by the *worse* of the two — a real and intuitive result with structural backing.

### 2.1 Where parallel-resistance composition appears in the framework's known applications

- **Coupling-constant generator algebra (V2 §1.4).** `k_X · k_Y = k²_{√(XY)}`. The inverse couplings 1/k_X compose additively under specific operations, producing harmonic combinations of `X²` directly under parallel composition.

- **Optical impedance matching in scattering networks.** `Z_eff = Z_A·Z_B/(Z_A+Z_B)` is the standard parallel-impedance rule, structurally identical to the framework's harmonic-SNR combination under capacity-additive composition.

- **Equivalent-single-channel SNR for parallel quantum channels under independent coding.** Two parallel quantum channels with SNRs `S_A, S_B` and independent coding produce capacity `log(1+S_A) + log(1+S_B) = log((1+S_A)(1+S_B))`, equivalent to a single channel with `SNR_eq = S_A·S_B/(S_A+S_B)`. This is the framework's apparatus producing the standard quantum-channel parallel-capacity result via role-reassignment.

- **Lens / focal-length combinations.** `1/f_AB = 1/f_A + 1/f_B` for thin lenses in series — capacity-additive composition with focal-length-inverse as the rapidity.

- **Heat-conductance through parallel paths.** Conductances combine additively in parallel; resistances in series.

### 2.2 Retraction

I previously claimed Schur-Feshbach reduction in DHO chain analysis gives parallel-resistance form. **This was wrong** and is retracted. Schur reduction gives `κ_eff = κ_A·κ_B/(z − ω_intermediate)` which depends on detuning, not the harmonic combination. Parallel-resistance composition appears specifically under capacity-additive composition for SNR-like quantities, not in DHO-chain Schur reductions.

---

## 3. The circuit calculus

### 3.1 Statement

The framework's role-agnosticism produces a **circuit calculus** with two reduction rules:

**Series sections** (cascaded subsystems): capacity-additive composition.
`(1 + SNR_AB) = (1 + SNR_A)(1 + SNR_B)`

**Parallel sections** (coherent diversity combining): MRC-additive composition.
`SNR_AB = SNR_A + SNR_B`

**Mixed networks:** reduce by alternating these rules per topology — first apply parallel-MRC reduction within each parallel block to get effective SNR, then apply capacity-additive cascade reduction across the resulting series, etc.

### 3.2 Verification

For three channels with SNRs (1, 2, 3), the topology determines the total:

| Topology | SNR_total |
|---|---|
| All-series (cap-additive cascade) | 23 |
| Parallel(1,2) → series with 3 (MRC then cascade) | 15 |
| All-parallel (MRC) | 6 |

Computed exactly by alternating the two reduction rules. The framework's apparatus produces topology-correct combinations automatically.

### 3.3 Structural analogy with Kirchhoff's laws

The framework's circuit calculus is structurally identical to electrical impedance combination:

- **Series resistors:** `R = R_A + R_B` (additive impedances)
- **Parallel resistors:** `1/R = 1/R_A + 1/R_B` (additive conductances)

With the framework's identification:

- SNR ↔ conductance (inverse-resistance)
- (1 + SNR) ↔ impedance ratio for cascaded transmission lines

The parallel-MRC rule (`SNR additive`) corresponds to `conductance additive`. The series-cascade rule (`(1+SNR) multiplicative`) corresponds to `impedance ratio multiplicative` for chained transmission segments.

This is *structural* analogy in the framework's specific sense: same compositional duality, same topology-determined reduction structure. Whether the analogy is "operationally identical" or "structurally suggestive but physically distinct" depends on the application — for SNRs of channel composition, the framework's circuit calculus IS the standard communication-theory calculation. For other instantiations, the analogy is structural.

### 3.4 Why this matters

**Operational consequence.** The framework predicts the SNR of any series-parallel network from its topology and per-section SNRs, using the framework's reduction rules. This is empirically testable against known network-combining results in communication theory.

**Structural consequence.** The framework's role-agnosticism principle produces a network calculus, not just a generic budget identity. The same algebraic backbone yields the right reduction rule for each topology automatically, because the topology determines which composition rule (capacity-additive or MRC-additive) is operative on which sub-structure.

**Pedagogical consequence.** Framing the framework via the circuit calculus may be more accessible than starting from the budget identity. "TEP provides a generalized Kirchhoff calculus where the analog of resistance is 1/SNR and the analog of conductance is SNR, with topology selecting between series-impedance-multiplicative and parallel-conductance-additive" is a one-sentence summary that lands for someone with electrical-circuit intuition.

---

## 4. The role-agnosticism principle, refined

### 4.1 Applicability vs application

The principle has two distinct levels:

**Applicability:** The framework's apparatus applies wherever info-monotonicity holds for the chosen metric. This is dimension-agnostic — any metric that is monotone under coarse-graining / passive operations admits the framework's structural treatment. There is no "right way to apply" at this level; role assignment is genuinely free.

**Application:** Within applicability, any specific physical scenario fixes a *package* — the role assignment plus composition law that matches the physical regime under analysis. Cascade physics fixes the package as capacity-additive with `x² = ζ²/(1+ζ²)`. MRC physics fixes the package as MRC-additive with `x = tanh(SNR)`. Once the physical composition law is identified, the package is determined (modulo the budget's internal x ↔ u dual reading).

So role-agnosticism holds at the framework level (the apparatus admits any package). Specific applications are package-determined by the physical composition law operative in the system.

### 4.2 Implications

This resolves a long-running tension in V2's framing between "lens that applies broadly" and "specific physical applications with their own composition rules." The corrected framing is:

The framework provides a generic apparatus that admits multiple regimes. Each application's package is determined by the physical composition law operative in that system. The framework's structural content (budget identity, rank-2 wedge, DGD ellipse, ARES factorization, etc.) is invariant across packages; the specific composition law operative in a given application is package-specific.

Different "applications" are not different uses of the same package — they are uses of *different packages* drawn from the framework's apparatus. The framework is more genuinely scenario-generating than role-agnosticism alone would suggest: same algebraic backbone, different physical scenarios depending on which package is operative.

---

## 5. Reassignment-revealed structural points

The reassignment apparatus also surfaced two structurally privileged points:

### 5.1 SNR = 1 as admissibility transition

The reassignment `SNR → G(x')` is admissible (real x'²) only when SNR ≥ 1. Its complement `NSR → G(x')` is admissible only when SNR ≤ 1. **Together they tile the SNR axis at the boundary SNR = 1.**

So SNR = 1 emerges as a *transition point in the admissibility landscape* — the framework's role-assignment package switches at this boundary. This is a structural observation about the framework's reassignment apparatus, distinct from any specific physical interpretation.

### 5.2 x² = 1/2 as saddle in geometric-mean reassignment

Two complementary reassignments using the geometric mean `√(x²·u)`:

- `√(x²u) → x'²` makes new x'² peak at the original self-dual point x² = 1/2 (max value 1/2).
- `√(x²u) → u'` makes new x'² have a minimum at the original self-dual point.

**The self-dual point x² = 1/2 is a saddle in the role-reassignment landscape** — peaks under one assignment, minimum under its dual.

This strengthens the identification of x² = 1/2 as a genuine framework-structural object: it appears as the Schwarzschild-horizon point in V2 §3.4, near the HBAR γ* = 2−√2 in V2 §3.2, and now as a saddle in the reassignment apparatus. Multiple independent structural readings converge on the same point.

### 5.3 Caveat

These are *structural observations* about the framework's reassignment apparatus. The connection to specific physical thresholds (does SNR = 1 transition correspond to a known phase boundary?) is a working hypothesis, not an established correspondence. The structural content is real; the physical mapping requires case-by-case verification.

---

## 6. The gaussian-from-budget cascade

Adjacent finding from the same thread, briefly recorded.

The chain `η_1 = ln(1 + SNR_1) = ln(2) · (C/B)_1 → e^(η_1) = G²(x_2) = 1/u_2`, extended via `η_1 = SNR_3` (reassigning the level-1 rapidity to be the level-3 SNR), produces:

`√u_2 = exp(-(1/2) SNR_3) = exp(-(1/2) x²_3 / u_3)`

This is the unnormalized gaussian density at x_3 with variance u_3. The full normalized PDF is `(1/√(2π u_3)) · exp(-x²_3/(2 u_3))`, with the framework's `u_2` being the squared unnormalized form scaled by `2π·u_3`.

**Verified numerically** across x_3 ∈ {0.1, 0.3, 0.5, 0.707, 0.9, 0.95}: the chain produces gaussian densities at level 2 with variance set by the budget at level 3, with correct normalization factor `2π·u_3`.

This is structurally GMC-like — a constrained multiplicative cascade where each level's gaussian variance is determined by the next level's budget, rather than an arbitrary log-correlated process. Gives the GMC ↔ TEP connection (V2 §4.3 listed as formal-similarity research direction) a sharper structural anchor: the framework's apparatus generates a *specific class* of GMC-type measures with parameters fixed by framework constants. Whether the cascade has a meaningful continuum limit, and if so what specific GMC measure it produces, is open.

---

## 7. Summary positions

### What's verified

- Two distinct composition regimes (capacity-additive and MRC-additive) admissible within the framework, each producing Lorentz-structured budgets via different rapidity choices for the same budget identity.
- Capacity-additive ↔ Shannon-cascade ↔ parallel-resistance equivalent SNR triangulation under capacity-additive composition.
- Circuit calculus with topology-dependent reduction rules, structurally analogous to Kirchhoff's laws, verified for three-channel test cases.
- Role-agnosticism refined into applicability/application distinction, with package-determines-regime as the precise statement.
- SNR = 1 as admissibility transition; x² = 1/2 as saddle in reassignment landscape — structural observations.
- Gaussian-from-budget cascade verified numerically; structurally GMC-like.

### What's hypothesized but not verified

- Specific physical correspondents for each reassignment regime (SNR = 1 as a known phase boundary; geometric-mean reassignment as quantum coherence visibility, etc.).
- Continuum limit of the gaussian cascade as a specific GMC measure with framework-fixed parameters.
- Whether the MRC-Lorentz mapping is a known structural identification in communication theory literature or a novel observation.

### What's retracted

- "Schur-Feshbach reduction in DHO chain gives parallel-resistance form" — wrong, retracted. Parallel-resistance form lives in capacity-additive SNR composition, not in DHO chain Schur reductions.
- Earlier framing that capacity-additive and MRC-additive are "symplectic conjugates" — overstates. They are structurally dual via logarithmic mapping, not canonical conjugates in Hamilton-mechanics sense.

### What's worth doing next, if this work continues

1. **Literature check on MRC-Lorentz mapping and capacity-additive parallel-resistance.** Both have known mathematical backbones (tanh-of-sum identity, harmonic combination of conductances). Whether the framework-style structural identification has been made in communication theory, I haven't checked. If it hasn't, this could be a standalone short paper. If it has, the framework rederives it via role-agnosticism — still worth noting but not novel.

2. **Continuum limit of the gaussian cascade.** Open problem. If the cascade has a scaling limit, what GMC measure does it produce? Sharpens V2 §4.3 from formal similarity to specific structural identification.

3. **Circuit calculus as standalone short paper.** Operationally testable, accessible to readers without TEP context, structurally clean. Could appear in a communication theory or network theory venue. Worth scoping properly.

---

*Working notes from May 2026 thread. Pending literature verification on items in §7.*
