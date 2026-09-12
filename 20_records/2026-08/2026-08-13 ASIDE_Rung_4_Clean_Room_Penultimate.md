# Aside — reliability of the correlation results; two horizon scales; and recovering the arithmetic from the "thermalized" region — 2026-08-12



**Trigger.** Will, on the spherical-function collapse: what does it look like as a heat map; **is this reliable — sample-size based, measure based, or neither**; it appears to thermalize around d ≈ 7; how fitted is the data below the horizon; does the region above follow another functional form; and **can the "protected" orthogonal mode be found and the preserved data recovered in the proper perspective**.



## 1. Reliability — the taxonomy, because the answer differs by claim



| claim | what kind of statement | status |

|---|---|---|

| C(Δx) at finite y | **neither sampled nor measure-theoretic** — an *exact finite sum* Σwₙcos(2πnΔx)/Σwₙ over a full period, wₙ = \|cₙ\|²K₀(2πny)². No estimator, no noise, bit-reproducible | exact |

| the floor | **exact identity**: ⟨C²⟩ = Σw²/(2(Σw)²). Verified rel. dev **1.11×10⁻¹⁶** at two heights | exact |

| the horizon scales | **deterministic**, derived from the spectrum's low-frequency edge | exact |

| convergence to φ_{1/2} as y→0 | **measure-type** — relies on self-averaging of \|cₙ\|² (Rankin–Selberg mean value) over the ~5/y active modes | asymptotic |

| yesterday's windowed empirical checks | **sample-based** — used only to confirm the field realizes the exact object (it does, to 0.008–0.010 at the deep heights) | confirmatory |



So: the core results are *neither* sample-size nor measure based. Only the universality limit is measure-type, and it is honestly labelled as such.



## 2. Two scales, and a correction to "d ≈ 7"



The apparent thermalization Will spotted at d ≈ 7 in the previous figure was **my plotting threshold** (I greyed points past d\*/2, which is 6.6 at the deepest height) — not a physical scale. The physics has *two* scales, both drawn on the heat maps:



- **d_cross** — where the universal envelope φ_{1/2}(d) sinks below the fluctuation floor. This is the **observable** end of universality: 3.97 (y = 2×10⁻²) → **8.56** (y = 2.2×10⁻⁴).

- **d\*** = 2ln(1/2πy) — where the sum runs out of frequencies below the fundamental mode n = 1: 4.15 → **13.17**.



d_cross < d\* always; the previous aside conflated them under one name. **Corrected: the operative horizon is d_cross.** Binned RMS at y = 2.2×10⁻⁴ shows the transition cleanly — [4,6]: 0.330 vs φ = 0.334; [6,8]: 0.143 vs 0.161; then [10,12]: 0.075 vs 0.032; [12,14]: 0.072; [14,16]: 0.072. **Below: tracks φ. Above: flat at the floor — the decay simply stops.** That is the "other functional form": not a new decay law, but constant-RMS almost-periodic fluctuation at exactly the predicted amplitude.



Floor prediction vs the post-horizon-only RMS: ratio 0.69 → 0.82 across 150 heights (mean 0.721 ± 0.051), rising toward 1 as y → 0 — the deficit is the excluded peak near Δx = 0, as expected. The full-period identity itself is exact.



## 3. The orthogonal mode — recovering the arithmetic (Will's question, answered)



**The post-horizon region is not thermalized.** It is Σwₙcos(uₙΔ) with the *same* weights — the horizon marks where the universal *envelope* dies, not where the information does. Whether it can be *read* is a separate, precise question, and the answer is a counting theorem:



- A window covering fraction f of the period supports only ≈ f·M recoverable degrees of freedom out of M modes — the **Slepian concentration count**. Measured: window fraction 0.68 (the post-horizon region, at Δx > 1/2π — note this threshold is **y-independent**), numerical rank **187/254 = 0.74** and **599/854 = 0.70**. Naive least-squares therefore returns garbage, which is what my first attempt did: it is an ill-posed inversion, *not* information loss.

- **The physics supplies the missing constraint**: wₙ = \|cₙ\|²K₀² is non-negative. Imposing positivity (NNLS) on the post-horizon region **alone** recovers the Hecke coefficients:



| n | 1 | 2 | 3 | 6 | 8 | 9 | 11 | 13 | 16 | 19 |

|---|---|---|---|---|---|---|---|---|---|---|

| true \|cₙ\| | 1 | 1 | 0.61803 | 0.61803 | 1 | 0.61803 | 0.61803 | 1 | 1 | 1.61803 |

| recovered | 1.000001 | 1.00001 | 0.61806 | 0.61801 | 1.00005 | 0.61816 | 0.61783 | 1.00064 | 0.99417 | 1.60292 |

| rel. err | 1.1e-6 | 6.5e-6 | 3.7e-5 | 3.9e-5 | 5.0e-5 | 2.0e-4 | 3.2e-4 | 6.4e-4 | 5.8e-3 | 9.3e-3 |



Ten modes to better than 1%, the leading ones **to five or six digits**, and the true zeros (2A primes, cₙ = 0) come back as zeros. Recovery depth is set by the weight hierarchy against the rank deficit: it reaches n = 19, where wₙ/w₁ = 2.7×10⁻³.



**So: the horizon is a basis artifact.** In the distance basis the arithmetic looks thermalized; in the conjugate (spectral) basis, with the positivity the physics already guarantees, it reads straight back out. Stated without inflation: this is Wiener–Khinchin plus Slepian plus a positivity constraint — standard tools — applied to our objects. It is a clean instance of the pattern Will's framework names, and it is *not* evidence for the framework beyond that.



## 4. The r\* = tanh(2r\*) question — honest no



Nontrivial root r\* = **0.9575**. Our d\* is not a constant of any kind: d\*(y) = 2ln(1/2πy) ranges 4.15–13.17 across this figure, and d_cross likewise moves with y, so neither can equal a fixed-point constant. The scale-free constants this analysis *does* produce are 2/π = 0.6366, (4/π)ln2 = 0.8825, and the horizon in Δx-units 1/2π = 0.1592. **None matches 0.9575; no correspondence claimed.** If a fixed-point constant belongs anywhere here I have not found where, and I would rather say so than fit one.



**Status.** Exploratory diagnostics, unregistered; no committed value touched. Scripts `horizon_map.py`, `spherical.py`; figure `maass_horizon_map.png`. *Drift-watch: two more harness errors caught by refusing to report a disagreement without explaining it — a negative-index window, and a naive inversion mistaken for a physical result. Offered, not self-filed.*
