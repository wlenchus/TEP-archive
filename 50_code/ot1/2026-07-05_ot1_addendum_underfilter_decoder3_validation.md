# Addendum — underfiltering audit resolved; order-4 branch validated
**2026-07-05** · tiers: [V]erified · [T]classical · [A]rgued · [O]pen

## Prompt
Challenge (Will/Gemini): could the N=8000 rejections be false negatives from decoder
*underfiltering* for a ramification reason — the exact mechanism that produced the
Buhler control's initial miss (his a₅ ≠ 0 broke the ram={5:None} assumption)?

## Resolution — two layers
### Ramification filtering (a₂ = a₅ = 0): PROVEN safe [V/A]
The Buhler miss required a₅ ≠ 0, which needs I₅ abelian (C₅) → reducible local rep.
Our quintic forbids this: if I₅ = C₅ then a₅(ρ₄) = 4b+4 with b the single break, so
b = (v₅(disc) − 4)/4 = (6 − 4)/4 = **1/2** — non-integer, impossible for an abelian
extension (Hasse–Arf, applied correctly this time). Hence I₅ = D₅ (nonabelian), the
local rep at 5 is irreducible/supercuspidal, and **a₅ = 0 is a theorem, not an
assumption.** Buhler's v₅ = 8 gives b = 1 (integer) → C₅ permitted → a₅ ≠ 0: the two
quintics sit on opposite sides of exactly this integrality line. At 2, Q₈ is nonabelian
for every lift, so a₂ = 0 robustly across the whole conductor ladder. The ram-filtering
cannot cause a false negative for our quintic.

### Nebentypus completeness: extended, all reject [V given validated instrument]
Buhler's actual failure was a *character* miss. So the grid was widened at N=8000:
quadratic {χ₋₄,χ₋₈,χ₋₂₀,χ₋₄₀} (complete for quadratics — 2-conductor ≤ 8), order-4-at-5
(ψ-family), and now **order-4-at-2 (ψ₁₆-family: ψ₁₆, ψ₁₆·q5, ψ₁₆·χ₋₄, ψ₁₆·χ₋₂₀, ψ₁₆·χ₄₀)**,
both embeddings. Every configuration REJECTS.

## Order-4 decoder (decoder3, ℚ(ζ₈,√5)) — external component validation [V]
The order-4 branch was the one instrument piece lacking a true-positive control (no A₅
order-4 form exists at hostable conductor — scan of 1200/1600/2000/2352 found only
dihedral order-4 forms). Its builder is instead validated component-by-component against
ground truth:
- **ζ₈ algebra**: runtime asserts i² = −1, ζ₈² = i, ζ₈⁴ = −1, and √χ·√χ = χ for every
  character code — PASS.
- **order-4 character**: decoder3's ψ reproduces PARI's real order-4 mod-5 character
  *exactly* (n≡2→i, 3→−i, 4→−1); ψ₁₆ verified multiplicative, order-4, odd.
- **Eisenstein leg**: E1_conj(ψ) matches an independent divisor-sum implementation using
  the validated character to 4×10⁻¹⁶.
- **magnitude model + sign-solve**: shared with decoder2 (CM control [V]) and decoder4
  (Buhler control [V]).
Residual [O]: no single end-to-end decoder3-on-A₅-order-4 control (such forms are absent
at hostable scale). Every constituent is validated, so an integration-only bug is the
sole residual risk — low, and it sits atop the proven ram-filtering + fully-validated
quadratic branch.

## Net epistemic status of the N=8000 exclusion
- Ram-filtering (a₂=a₅=0): [V/A] proven.
- Quadratic nebentypus: [V] (decoder2, CM-controlled on host8000).
- Order-4 nebentypus (5-part and 2-part): [V-components] (decoder3 validated as above).
- The form, if it existed at 8000, would have A₅ magnitudes (Buhler-validated) and land
  in S₂(Γ₀(8000)) by weight-lifting. It does not, for the entire natural nebentypus space.
Conclusion: N=8000 exclusion stands on validated footing. Ladder: a₂ ≥ 7, rungs 16000
then 32000.

## 16000 status
Uploaded host16000 was the **new subspace only** (dim 384 of the full 2321; flag 0 not 1,
plus a stray header) — its rejections carry no information. Corrected generators shipped
(gen16000.gp / gen16000_chunked.sh, flag 1, no header) plus the generic run_level.py
(quadratic + both order-4 branches). Regenerate on your machine, CM-control first (level
20 | 16000 → residual 0), verify row count 2321, then sweep.

## Shipped this addendum
decoder3.py (ψ₁₆ added, algebra-asserted), ord4char.gp, this record.
