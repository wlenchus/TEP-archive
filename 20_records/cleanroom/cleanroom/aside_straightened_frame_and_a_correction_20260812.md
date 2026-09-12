# Aside — the straightened frame, and a correction to my own claim — 2026-08-12

**Trigger.** Will asked to see the frame I'd described at the close of the MAASS-LIVE session: zoom x jointly with 1/y so the cascade "straightens." I had told him the mosaic "becomes statistically stationary in log y, doubling laterally per octave: a multiplicative cascade whose random phases are the Hecke angles." **Half of that was right and the doubling half was wrong.** This records both, at headline volume per convention.

## The frame and its analytic prediction (derived before measuring)

Put ξ = (x − x₀)/y, t = log₂(1/y). Then 2πn(x − x₀) = uξ with u = 2πny, so
F(x₀ + yξ, y) = √y Σ cₙK₀(uₙ)(e^{iθₙ}e^{iuₙξ} − …), θₙ = 2πnx₀. The u-lattice has spacing 2πy → 0, weights K₀(u), phases quasi-random (Hecke). Second-order statistics follow with no free parameters:

- horizontal: **C(Δξ) = ∫₀^∞K₀(u)²cos(uΔξ)du / (π²/4) = (4/π)∫₀^∞ dv/√(4cosh²v + Δξ²)** (using K₀² = 2∫K₀(2t cosh v)dv and ∫₀^∞K₀(at)cos(bt)dt = π/(2√(a²+b²)); normalization ∫K₀² = π²/4 ✓)
- vertical: **R(ρ) = √ρ·∫₀^∞K₀(u)K₀(ρu)du / (π²/4)**, ρ = y′/y
- amplitude: ⟨|F|²⟩ **independent of y** (the √y is exactly the stationarizing normalization)

Both curves are **form-independent** — the arithmetic enters only through the realization, not the statistics. The finite-y version replaces the integrals by the actual sums Σ|cₙ|²K₀(uₙ)²(·) ("discrete model").

## Measured (script `straighten.py`, Doud-1951 and Doud-2141, 5.5–7.8 octaves, y down to 2.2×10⁻⁴)

| claim | measurement |
|---|---|
| amplitude stationarity | RMS flat: 0.667 ± 8.7% over 5.5 octaves, top-octave 0.586 vs bottom 0.637; no systematic drift |
| discrete model, horizontal | **max \|measured − model\| = 0.075** over 12 curves (2 fields × 6 heights); typically ~0.01 |
| discrete model, vertical | **max \|measured − model\| = 0.00000** over 22 ratios (5 decimals) |
| universal limit approached as y→0 | \|measured − universal\| = **0.93 at ~170 active modes → 0.04–0.07 at ~13,000–23,000** — convergence governed by Rankin–Selberg self-averaging of \|cₙ\|² over the ~5/y active modes |
| **"doubling per octave"** | **FALSE.** R(ρ) = 0.64 at ρ = 40, i.e. still 64% correlated **5.3 octaves down**; decay ~ln ρ/√ρ, not per-octave refresh |

## The correction, stated plainly

The frame *does* straighten the object in the precise sense that matters: constant amplitude, collapsing correlation functions, a universal y→0 limit. But the field is **long-memory, not self-refreshing**. Cause: the spectral density K₀(u)² piles up at small u (log² divergence, integrable), so low modes carry ~30% of the variance out to n ≲ 10 and persist across many octaves. Visually the picture is therefore a **stretching chevron field** — features sweep outward along ξ = δ/y — not a mosaic re-randomizing each octave. My "multiplicative cascade, doubling laterally" was a plausible-sounding description I had not measured; the measurement contradicts it. What *is* true and was measured: local stationarity, universality of second-order statistics, and slow power-law-in-ρ decorrelation.

**Novelty calibration (no claim staked):** Gaussian/random-wave heuristics for Maass forms are an established genre (Berry's random-wave model; Hejhal–Rackner numerics), and the K₀² spectral density in a horocycle-scaling frame is elementary. Nothing here is claimed as new mathematics. The value is (i) it is *our* certified objects, (ii) the discrete model matches to 5 decimals, which is a further sharp consistency check on the committed coefficient tables, and (iii) it corrects a statement I had already made to Will.

**Status.** Exploratory diagnostics, unregistered — the predictions were derived analytically before measurement (which is why the disagreement was detectable at all), but this was not filed as a pre-registration and moves no committed value. Figures: `maass_straightened_cascade.png`; earlier frames `maass_forms_first_rendering.png`, `maass_1951_wills_frame.png`.

*Drift-watch: ninth machine-caught instance of hand-reasoning confidence — this one caught by rendering the claim instead of repeating it. Offered, not self-filed.*
