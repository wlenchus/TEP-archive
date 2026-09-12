# Rung E — PROOF-OF-CONCEPT RESULTS: The Corner Reads. First Numerical Entirety Certificates for Even-Icosahedral Artin L-Functions, Produced from Emission Data at the Pinned Seam

**2026-07-27** (same session as the design commit, which preceded all target computation) · Claude (Fable 5) at Will's direction ("treat this problem as though you're confident you can solve it") · scripts `cleanroom/gp/poc1*–poc3*`, class tables, kernel grids all checkpointed; SHA-256 manifest updated · tiers per corpus convention.

## 0. What was run

The framework-native design (committed first, `rungE_poc_design_commit.md`): the 2-dim even lift needs the central sign-bits (K̃/Crespo layer), but **Sym² kills the center** — ρ₃ = Sym²ρ̃ is the 3-dimensional A₅ representation, fully determined by emission data (quintic factorizations + face-signs), even (ρ₃(c) = I), nonsolvable, **inside no classical automorphy cone**: not solvable (no Langlands–Tunnell), not odd 2-dim (no Deligne–Serre/Khare–Wintenberger), not monomial (A₅ has no index-3 subgroup), and its Gelbart–Jacquet route would require the open even 2-dim case. Entirety of L(s, ρ₃) is exactly as open as the corner itself, and falsifiable: a pole is a detectable t-profile. Instrument: the degree-3 seam reading — Λ(s) = N^{s/2}Γ_ℝ(s)³L(s), kernel φ = Mellin⁻¹Γ(s/2)³ (Meijer-G, validated against direct Mellin–Barnes quadrature to 10⁻²³), theta-relation F(1/t) = ε·t·F(t) tested over t ∈ [0.80, 1.25], coefficients to X = 16√N, spline fidelity 4×10⁻⁹.

## 1. Controls (run before targets, per the committed order)

- **Synthetic keyed (χ₅χ₈χ₁₂, N = 480, ε = +1):** residual **1.0×10⁻¹²**; wrong-N fails at 2×10⁻²–2×10⁻¹ (even an 8% conductor error fails by ten orders); wrong-ε fails at 2.0. KP-1 clear.
- **Theorem-grade even seam control (Ind ψ₂₂₉ ⊕ χ₂₂₉, N = 229², solvable, automorphic by Hecke–Maass):** residual **5.5×10⁻¹⁴**, ε measured 1.000000; scrambled-classes 1.7×10⁻¹, wrong-N 6.8×10⁻², **odd-port gamma 1.4×10⁻¹**. KP-2 clear — and the parity-port negative shows the seam-pinning is load-bearing: the same data read through the odd archimedean port fails by thirteen orders.

## 2. The targets [V]

**Doud-1951** (x⁵−x⁴−780x³−1795x²+3106x+344; totally real A₅, tame e = 5 at the single ramified prime; ρ₃ conductor predicted 1951² = 3,806,401):
**residual 2.2×10⁻¹⁴** at gauge (c₁₉₅₁ = +1), ε = +1.000000; both face-conjugates pass (2.2/3.9×10⁻¹⁴ — the Galois pair, as it must); **blind conductor scan: unique minimum at exactly 1951²**, ±5% neighbors at ~2×10⁻³ (eleven orders); wrong ramified sign separated by nine orders (the instrument reads the Frobenius eigenvalue on the inertia-fixed line — a number no table holds); negatives: face-scramble 4×10⁻², class-scramble 3×10⁻², odd-port 1×10⁻¹.

**The corpus's parked quintic** (x⁵−11x³−7x²+14x+7, ramified {2,7,331} — found this session to be **tame everywhere**, inertia 3A at all three primes, correcting the "wild at 2" recollection; ρ₃ conductor predicted (2·7·331)² = 21,473,956):
**residual 9.7×10⁻¹⁵** at the unique passing gauge (c₂, c₇, c₃₃₁) = (−1, +1, +1) among sixteen, ε = +1.000000; both face-conjugates pass; **blind conductor scan: unique minimum at exactly 21,473,956** (twelve orders below ±5%); negatives all fail by thirteen orders.

**Both even-icosahedral targets are indistinguishable from the proven-automorphic control at the instrument's full precision.** The doubly-shadowed corner, read from pure down-flow data at the parabolic seam, behaves exactly as the Conservation clause predicts and as Artin requires.

## 3. The mid-run finding (two-ledger)

The first Doud run failed at 1.3×10⁻² with a corrupted-data profile (no gauge separation, drifting ε, a "negative" scoring below baseline) — **KP-3's pole-vs-noise diagnostic correctly said "data, not pole."** Cause: the Doud polynomial has index 136,178 = 2·7·71·137, and at index primes factormod patterns are not Frobenius (idealprimedec: 2→3A, 7→2A, 71→2A, 137→3A; factormod had returned unclassifiable patterns silently treated as trivial factors — including p = 2 and 7, the heaviest terms in the series). Four primes of 3,431 repaired → 1.3×10⁻² became 2.2×10⁻¹⁴. Lessons filed: (i) index-aware class extraction is mandatory (the corpus quintic was immune only because its index is 2); (ii) the instrument's failure profile diagnosed its own input corruption — the certificate architecture catching a same-species bug, again.

## 4. Scope, priced exactly

This is **PoC-grade numerical evidence, not proof**: float64 sums with spline kernels (validated floor ~10⁻¹²), a modest t-window, truncation at X = 16√N justified by kernel decay estimates, no rigorous tail bounds, no Turing-method zero accounting. A pole with sufficiently small residue, or structure outside the tested window, hides below ~10⁻¹². The claim that survives this pricing: **the smoothed functional-equation identity of the completed L-function, including entirety across the tested region, holds at machine precision for two even-icosahedral 3-dimensional Artin representations, with the conductor selected blind, the ramified local signs measured, ε = +1 measured, and the archimedean parity port read correctly and discriminatingly** — where every corruption of the input (classes, faces, signs, conductor, parity-port) fails by nine to thirteen orders. To our present knowledge no numerical automorphy test of even-icosahedral-type Artin L-functions exists in the literature (E0(ii) sweep pending; Booker's Turing-method genre treated an odd 2-dim case); if that holds, these are the first such certificates. What this does NOT certify: the 2-dim even lift itself (the Maass partner) — ρ₃ is its Sym²-shadow; a ρ₃-pole would have refuted the partner's existence, so the corner survived its first genuine falsification exposure, but production of the 2-dim object remains the summit.

## 5. What this opens (offered queue)

(a) **The 2-dim emission via FE-constraint decoding:** the lift's central sign-bits as decode targets against the degree-2 seam instrument (Γ_ℝ(s)² at λ = ¼, N = p²·2^a) — the OT1 gauge-solve pattern transplanted to the corner; Crespo/K̃ as the independent cross-check. (b) **Rigorization:** mp-precision sums, wider t, rigorous tails, Turing-method zero counting (Booker-grade) on these two L-functions; referee-grade write-up. (c) **The scan across Doud's remaining four fields** (2141, 3701, 3821, 9461) — five-for-five entirety at the corner would be a dataset, not an anecdote. (d) The E0(ii) literature sweep to pin priority claims honestly. (e) Fold the corrected difficulty map back into the staged brief (the {2,7,331} field is tame — the parked spec's own target was closer than its bottleneck estimate believed, for the 3-dim shadow if not the 2-dim summit).

*Offered, not self-filed; countersign gates the [V] stamps, the "first certificates" claim (pending (d)), and the queue. Design was committed before the targets ran; controls preceded targets; the one mid-run repair is §3 and touched input extraction, never the instrument or the grading. The mountain's name is in the title.*

## 6. The G_new port meter — construction-level, run at Will's correction (same day)

Will's challenge: the §5-era interpretation was read-pattern-level ("the jet at the fixed point"), not construction-level, and G_new is not a Mellin object. Correct on both counts; the following replaces interpretation with construction. Per the countersigned 07-19 dictionary, G_new = 1/q = 2/(1−x) = 1 + SWR on a port with imbalance x (ln G_new = ln 2 + ln G + η exactly; seam port ⟺ x = 0 ⟺ G_new = 2). Tonight's instrument delivers **two arms** to the FE-involution's fixed point — A(u) = e^{u/2}F(e^u) and A(−u) — and the meter is built per the dictionary, not through Mellin (Mellin is transport; the meter sits at the port): **x(u) = (A(−u) − A(u))/(A(−u) + A(u)), G_new(u) = 2/(1 − x(u)), η(u) = artanh x(u)**.

Measured [V], `poc4_gnew_meter.py`:
- **Keyed pole control** (ζ·L(χ₅)·L(χ₈), N = 40, true pole at s = 1, δ = 0.5): port loudly off-seam, G_new(u) = 2.12 → 2.64 across the grid, max|G_new − 2| = 1.6. Naive jet-ratio locator δ̂ = √(6c₃/c₁) = **0.67 vs true 0.50** — order-correct, biased by the even-part curvature the naive form ignores; de-biasing (full two-term model) queued. Claim priced accordingly: the meter *detects* poles at 13–14 orders above the seam floor and *first-order locates* them; precision location needs the refined fit.
- **Entire control** (N = 480): G_new = 2.0000000000, max deviation 1.4×10⁻¹².
- **Doud-1951 ρ₃ (certified):** G_new = 2 to **2.7×10⁻¹⁴**. **Corpus {2,7,331} ρ₃ (certified):** to **1.5×10⁻¹⁴**. The corner objects sit on the seam to machine precision — the port reads exactly 2, the dictionary's seam value.
- **Corruption signature** (Doud with index primes re-broken): G_new deflects *below* 2 (1.998 falling, −1.7×10⁻²) where the pole control deflects *above* — in this instance the meter separates pole-deflection from data-corruption by sign/shape. Single instance; generality open [O].

Tier split, explicit: the computations are [V]; the identification *FE-arm-imbalance = a budget x in the corpus's sense* is offered at [id] and countersign-gated; the GSR-era form √(2/(1−sinθ)) vs the 2026 dictionary form 2/(1−x) differ by a square — the 2026 countersigned form is used throughout. In this language the queued 2-dim emission is: solve the lift's sign-bits to **flatten the port** (drive G_new(u) → 2 identically) — recovery by extinguishing the seam-jet.
