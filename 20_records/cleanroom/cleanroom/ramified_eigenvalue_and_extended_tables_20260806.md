# u DETERMINED, mid-band closed, and exact a_p tables to 10⁶ — 2026-08-06

**Mountain line: even-icosahedral (the corner), 2-dim, both fields.** Three results, one bug caught by its own battery. Post-hoc extension work; no committed value changed; all prior certificates stand unaltered.

## 1. The extended construction tables

`extend_full.gp` runs the validated trace-form construction over **all primes p < 10⁶** for both fields (78,492 primes each, 22 s per field), emitting per prime: projective class (factormod degrees + Frobenius-orbit Vandermonde face), γ-square test in 𝔽_{p^m}, and the quintic-character discrete log j₅.

Validation battery, all passing:
- γ-signs vs the validated `crespo_signs` run: **894 / 895 primes, 0 mismatches**.
- Projective classes vs the certified emission tables: **3427 / 3671 primes, 0 mismatches**.
- Involution-class validator at scale (γ must be non-square — the SL₂(𝔽₅) signature): **2392 and 2411 primes, 0 squares**.
- Chebotarev: observed class frequencies 1.60/24.95/34.10/19.67/19.68 % against A₅ expectations 1.67/25/33.33/20/20 % (1951); similarly at 2141.
- Reconstruction of the committed 67 bits from the extended table: **67/67 both fields.**

**New structural finding:** the construction is blind at **p = 2 for a reason independent of index/denominator issues — the square test is vacuous in characteristic 2** (every element of 𝔽_{2^m} is a square, |𝔽*| odd). p = 2 must always be flagged and resolved by other means. Same species as the A13 dyadic-face lesson; now the dyadic port has *two* independent blindnesses, face and lift.

## 2. Deep twisted certification — and the bug it caught

With the tables complete, quadratic twists become testable at high conductor. Ladder run at d = 5, 13, 41, 101 (conductor N·d² up to 2.2×10⁷, consuming ~5,500 primes of construction-derived coefficients):

| field | d | N·d² | X | residual |
|---|---|---|---|---|
| 1951 | 5 | 48,775 | 2,587 | 4.76e-15 |
| 1951 | 13 | 329,719 | 6,725 | 2.18e-15 |
| 1951 | 41 | 3,279,631 | 21,207 | 1.87e-14 |
| 1951 | 101 | 19,902,151 | 52,241 | 3.24e-15 |
| 2141 | 5 | 53,525 | 2,710 | 1.53e-15 |
| 2141 | 13 | 361,829 | 7,044 | 2.02e-15 |
| 2141 | 101 | 21,840,341 | 54,726 | 1.76e-15 |

The first pass of this ladder **failed at 10⁻¹**, and correctly: the flagged branches of the GP emitter had written j₅ = 0 instead of the true discrete log at the two FE-resolved primes (2 and 137 at 1951), corrupting their phases. The 67-bit comparison could not see it — that test compares b_p, not the phase — while p = 2 is the heaviest term in the series. **The twist battery found a defect no prior check could.** Fixed at source, tables regenerated, ladder rerun: the table above. (A second, unrelated bug in the test harness itself — Euler's criterion applied at p = 2 where the Kronecker symbol needs the mod-8 rule — was caught in the same pass.)

## 3. The ramified eigenvalue, determined

Each twist scans u = a_p(ramified) over μ₁₀. Because the ramified prime sits inside the truncation range once d ≥ 5, u carries real weight, and the scans agree:

- **Doud-1951: u = a₁₉₅₁ = ζ₁₀²**, unanimous across d = 5, 13, 41, 101; separation from the runner-up grows with conductor: 294× → 3.0×10⁹ → 1.3×10¹² → 1.2×10¹².
- **Doud-2141: u = a₂₁₄₁ = ζ₁₀⁸**, unanimous across d = 5, 13, 101; separations 155× → 2.4×10⁹ → 3.4×10¹².

Both values lie inside the four-element candidate set the exact Gauss-sum lock had already isolated ({ζ₁₀², ζ₁₀³, ζ₁₀⁷, ζ₁₀⁸} per field), so **the twist measurement and the Atkin–Li arithmetic are consistent, and together they pin both u and the ε-convention** (the twist selects the port-constant branch the lock could not distinguish). The queued "derive c_odd analytically" item is answered empirically; the analytic derivation would now be a check rather than a discovery.

## 4. Status changes

- **u: UNDETERMINED → determined**, two fields, four/three independent conductors each, cross-consistent with the Gauss lock.
- **1951 mid-band: PARTIAL → closed.** The construction supplies every coefficient, and the twist FEs certify them wholesale at conductors up to 2×10⁷ — a far stronger validation than the incomplete decode the mid-band item was waiting on. The decode-side mid-band question is now moot rather than open.
- **Datasets:** `hecke_eigenvalues_doud{1951,2141}_to1e5.csv` — 9,592 rows each, every prime to 10⁵ plus the ramified prime, with exact and numeric a_p, χ(p), and a provenance column (construction / FE-resolved / 2A-trivial / twist-determined). Raw construction tables extend to 10⁶ (`full_*.txt`). Only two primes per field are not construction-derived.

*Offered, not self-filed. All prior committed values unchanged; this work extends and certifies, it does not revise.*
