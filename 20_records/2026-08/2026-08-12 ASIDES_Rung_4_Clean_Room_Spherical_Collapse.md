# Aside — the correlation function IS the λ=1/4 spherical function; the horizon; the s ↔ 1−s fixed point — 2026-08-12



**Trigger.** Will, on the straightened frame: (i) what happens looking further out for universal collapse, (ii) what if we multiply/divide by √ρ or √ρ³, (iii) "is there a reflective phase relation, as in an s ↔ (1−s) involution?" All three have one answer.



## The identity (derived, then verified to machine precision)



Both correlation directions of the previous aside are **the same function of hyperbolic distance**. Using ∫₀^∞K₀(at)K₀(bt)dt = (π²/4a)·₂F₁(½,½;1;1−b²/a²) and ₂F₁(½,½;1;m) = (2/π)K(m):



**C_horizontal(Δξ) = R_vertical(ρ) = φ_{1/2}(d) = P₋₁⁄₂(cosh d) = (2/π)·K(1−sech²(d/2))/cosh(d/2)**



where d is hyperbolic distance: cosh d = 1 + Δξ²/2 (horizontal), cosh d = (ρ²+1)/(2ρ) (vertical). Machine-checked: elliptic-K form vs Mehler–Dirichlet quadrature **3.0×10⁻¹⁵**; horizontal continuum vs φ **6.0×10⁻¹⁴**; vertical continuum vs φ **1.3×10⁻¹³**. So the anisotropy of the earlier aside was an artifact of the coordinates: **the limiting field is isotropic in the hyperbolic metric**, and its correlation function is the radial λ = 1/4 eigenfunction of the hyperbolic Laplacian — the Harish-Chandra spherical function at s = 1/2.



## (ii) The √ρ question — exactly right, and the exponent is the spectral parameter



Asymptotically φ_{1/2}(d) = (4/π)e^{−d/2}(d/2 + ln2) + …, so **e^{d/2}φ(d) is linear in d with slope 2/π**: fitted **0.63661 vs 2/π = 0.63662**, intercept **0.8826 vs (4/π)ln2 = 0.8825**. In the two coordinates:



**√ρ·R(ρ) → (2/π)·ln(4ρ)** and **Δξ·C(Δξ) → (4/π)·ln(2Δξ)**



So √ρ is the right multiplier and √ρ³ overshoots: the exponent is **e^{−d/2} = ρ^{−1/2}**, i.e. **exactly Re(s) = 1/2**. The decay rate of the correlations is the spectral parameter itself; the residual logarithm is the fingerprint discussed below.



## (iii) The involution — it is there, and our forms sit at its fixed point



The spherical function satisfies **φ_s = φ_{1−s}** exactly (Legendre P_ν = P_{−1−ν} with ν = −s), the *same* s ↔ 1−s as the functional equation. In the c-function expansion φ_s ~ c(r)e^{(ir−1/2)d} + c(−r)e^{(−ir−1/2)d} with s = 1/2+ir, the involution swaps the two terms. **At the fixed point r = 0 the two exponentials coalesce — a degenerate pair — and the coalescence produces the logarithm.** So the ln that appears in both directions of the previous aside is not incidental: it is the observable signature of sitting at s = 1−s. Off the fixed point one would see oscillation of period 2π/r instead (panel 3 shows r = 0.35, 0.7 curves turning over and crossing zero where the data runs straight).



This affords **an independent measurement of the archimedean parameter, from the eigenfunction's spatial correlations alone — no L-function, no functional equation**: fitting r over the φ_{1/2+ir} family gives **best-fit r = 0.000, |r| < 0.18 at twice the best RMS** (169 points). Weak next to the 10⁻²⁰ from the L-function route, but *methodologically disjoint* — it uses only the shape of correlations in the hyperbolic metric.



Note two distinct reflections, not to be conflated: the **global** s ↔ 1−s (functional equation ↔ Fricke involution, measured pointwise as F(−1/(Nz)) = −ε·G(z) at 10⁻²⁶) and this **archimedean** one (r ↔ −r ↔ s ↔ 1−s of the spherical function, measured as the absence of oscillation). Both are reflections; they live in different places.



## (i) Looking further out — universality has a HORIZON, set by the fundamental mode



Empirically (0.92-wide window, cross terms do not cancel, so this is a real test):



| y | active modes | horizon d\* = 2ln(1/2πy) | max\|emp − φ\| for 0.5 < d < d\*/2 | at the horizon |

|---|---|---|---|---|

| 2.2×10⁻⁴ | 23,149 | 13.17 | **0.0100** | 0.285 |

| 1×10⁻³ | 5,092 | 10.14 | **0.0080** | 0.380 |

| 5×10⁻³ | 1,018 | 6.92 | **0.0909** | 0.605 |

| vertical ladder ρ ≤ 20 | — | governed by the **shallower** member | **0.0011** (20/20 pairs) | — |



**Collapse in regime: 203 points, three heights plus the vertical ladder, d ∈ [0.05, 6.55], max deviation 0.091 (0.010 at the two deep heights).** Past d\* it fails — and the cause is exact: the mode sum has no frequencies below u₁ = 2πy, while the continuum limit's tail ln d/e^{d/2} is generated precisely by the u → 0 region. **The universal regime ends where the correlation would need modes below the fundamental Hecke frequency n = 1.** The horizon scales as 2ln(1/y): each octave down buys exactly 2 more units of hyperbolic distance. This also explains the vertical ladder's limit — a pair's horizon is set by its shallower member, which is why ρ must stay modest even when y₀ is deep.



**Correction carried forward:** the previous aside reported "vertical: max |measured − discrete model| = 0.00000" as a confirmation. It is not one — that average was taken over the **full period**, where distinct Fourier modes are exactly orthogonal, so the agreement is an algebraic identity (a useful harness check on the FFT/Bessel machinery, nothing more). The windowed numbers above are the genuine tests. Filed at headline volume.



**Status.** Exploratory diagnostics, unregistered; predictions derived analytically before measurement. **No novelty claimed**: that random-wave limits of Maass forms are governed by the spherical function is standard (Berry's random-wave model; the c-function/Harish-Chandra theory is classical). What is ours is the objects, the machine-precision identity check, the horizon law, and the disjoint r = 0 measurement. Script `spherical.py`; figure `maass_spherical_collapse.png`.



*Drift-watch: my initial run reported a collapse failure (0.45) that was entirely a measurement-design error — lags comparable to the window, and averaging far past the horizon. Two harness errors caught in one sitting by insisting the disagreement be explained rather than reported. Offered, not self-filed.*
