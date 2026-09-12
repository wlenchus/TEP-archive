# Aside — the inventory of ignorance, plus two new measurements (rigidity, and where "icosahedral" lives) — 2026-08-12

**Trigger.** Will: "if that's the case, then what is it that we don't know or can't recover about these Maass forms?"

## Two measurements run to draw the line precisely

**1. Rigidity — automorphy alone recovers a held-out Hecke coefficient.** F is *linear* in each cₙ, and for p > 200 (so p² > n_max) the dependence on c_p is exactly linear. Deleting a_p from the input entirely and solving the automorphy relations for it, over 18 (z, γz) pairs:

| p | class | committed a_p | recovered from automorphy alone | rel. err |
|---|---|---|---|---|
| 211 | 5A | 1.30901699 − 0.95105652i | 1.30901699 − 0.95105652i | **3.8×10⁻¹³** |
| 401 | 2A | 0 | −0i | 2.5×10⁻⁹ |
| 1009 | 5A | −1.30901699 + 0.95105652i | −1.30901699 + 0.95105652i | 8.0×10⁻¹² |
| 2003 | 3A | −0.80901699 − 0.58778525i | −0.80901699 − 0.58778525i | 7.3×10⁻¹¹ |
| 4001 | 5A | −1.61803399 | −1.61803399 | 2.2×10⁻⁹ |

Read precisely: this is **not** independent confirmation of a_p (the other 39,999 coefficients came from the committed set). It is a **rigidity** statement — automorphy plus the rest of the table determines the missing coefficient to thirteen digits, including forcing a_401 = 0 exactly. The arithmetic has no slack. It also shows the direction is invertible: the analytic side *determines* arithmetic, not merely records it. The natural continuation is Hejhal's algorithm — extend the table from automorphy alone, beyond where the Galois computation has reached, and grade against fresh Galois values.

**2. The fourth moment — where "icosahedral" must live analytically.** The two-point function is *universal* (previous aside: it is φ_{1/2}(d) for any form). The four-point function is not. Measured ⟨|F|⁴⟩/⟨|F|²⟩², against the Gaussian random-wave value 2 and the diagonal (self-pairing) correction:

| y | measured | excess over 2 | diagonal term predicts | off-diagonal residue |
|---|---|---|---|---|
| 5×10⁻³ | 1.71705 | −0.28295 | +0.40559 | **−0.689** |
| 1×10⁻³ | 2.01348 | +0.01348 | +0.10662 | −0.093 |
| 2.2×10⁻⁴ | 2.02763 | +0.02763 | +0.03076 | −0.003 |

The excess is *not* the diagonal term — at the shallow height it has the wrong sign and is 2.4× larger in magnitude. The difference is the off-diagonal contribution: shifted-convolution sums Σ c_{n₁}c_{n₂}c̄_{n₃}c̄_{n₄} over n₁+n₂ = n₃+n₄. **That is where the icosahedral structure lives** — the Hecke angles here are not equidistributed on a circle but take five discrete values (|a_p| ∈ {2, 0, 1, φ, 1/φ}), so higher moments must carry a signature the two-point function cannot. As y → 0 the field Gaussianizes and the residue shrinks toward zero; the *rate* and *sign* are arithmetic. Nobody has this data because these objects did not exist a week ago. **This is the inclined direction.**

## The inventory — what we genuinely do not know

1. **Artin holomorphy. Untouched, and it is the actual conjecture.** Every result in this program is numerics at finitely many points. That L(s, ρ) is entire is not addressed by any of it, and no amount of this kind of work will address it.
2. **Cuspidality / L² membership.** We verified F(γz) = χ(d)F(z) at 18 pairs to 10⁻²⁴. We have *not* verified F ∈ L²(Γ₀(N)\H) — that it lies in the discrete spectrum at all. This matters especially here: λ = 1/4 is exactly Selberg's bound and exactly the bottom of the continuous (Eisenstein) spectrum. Our forms sit *on* that edge.
3. **Coefficients past the table.** A function at height y knows only n ≲ 1/(2πy); our tables stop at 10⁵. Measurement 1 shows automorphy can bootstrap past this, but we have only held out, not extended.
4. **The Petersson norm ⟨F,F⟩** — never computed. It normalizes the symmetric-square L-value and everything downstream of it.
5. **Mass distribution.** We have the two-point function. We do *not* have QUE/equidistribution of |F|², the sup-norm, the extreme-value statistics, or the nodal geometry.
6. **The four-point function** — measured today, substantially non-Gaussian, unexplained. Open.
7. **Zero statistics.** No Turing-method count; we cannot certify we have all the zeros or that none lie off the line.
8. **2141's dyadic port** — arithmetically obstructed (χ₋₂₄ ramified at 2); a_2 there is not algebraically reachable by our route.
9. **The four remaining Doud fields** (3701, 3821, 8501, 9461) — dossier loaded, uncomputed.
10. **Multiplicity.** We have not computed the dimension of the relevant newform space; whether these are the *only* such forms at these levels is unverified.

*Exploratory diagnostics, unregistered; no committed value touched. Script inline (rigidity + fourth moment). Offered, not self-filed.*
