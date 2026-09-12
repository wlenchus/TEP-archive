# The budget–syzygy dictionary (Will's Klein sheet, reconsidered post-wall and machine-verified) — 2026-08-04

**Verified exactly this session** (`klein_budget.gp`): Klein's icosahedral syzygy **T² = 1728·f⁵ − H³** (symbolically exact, f = vertex form deg 12, H = Hessian/121 deg 20, T = Jacobian/20 deg 30) and its modular twin **E₄³ − E₆² = 1728·Δ** (q-series). The budget chart these force, checked numerically to 30 digits on the geodesic z = it:

- **Icosahedral:** divide by 1728f⁵: **x² = J = H³/(1728f⁵), u = 1−J = T²/(1728f⁵)** — capacity/X_max = vertex form (order 5), signal = face share (order 3), noise = edge share (order 2). *(Corrects the sheet's assignment: the true syzygy puts 1728 with f⁵, making f the normalizer — the sheet's x² = f⁵/H³ with X_max = H^{3/2} carries a factor-3 slip ((72T)² = 5184T² ≠ 1728T²) and inverts the roles; the structure survives, the algebra chooses the chart.)*
- **Modular:** **u = 1728/j = 1728Δ/E₄³, x² = E₆²/E₄³**; budget and dual identity hold to 3e-30 along z = it. Special points: **cusp i∞ ⟺ x → 1 (saturation); z = i (j = 1728, the order-2 CM point, fixed point of Fricke z ↦ −1/z) ⟺ x = 0 — THE SEAM; z = ρ (j = 0) ⟺ u → ∞, the reactive sector.** The fundamental domain's real locus is the budget disk's axes; A = arcsin(E₆/E₄^{3/2}) is a compactified monotone coordinate i → i∞.

**Post-wall significances (offered, tiered):**
1. **[C] The seam sits at the Fricke fixed point** — the atlas §4 [id] already reads the budget's transfer matrix as the SL₂-lift of Fricke inversion with T² = −id = the face swap x ↦ −x; this chart places the seam AT that involution's fixed point on the actual modular curve. Sheet + atlas + classical uniformization close a triangle.
2. **[C] Eisenstein ⊕ cuspidal = x² ⊕ u.** In the modular chart the noise share is literally the cusp form's share (u ∝ Δ/E₄³): readable/boundary content = Eisenstein, bulk content = cuspidal — and the campaign's summit object IS a cusp form, read at the seam. The spectral decomposition is the budget split in this chart.
3. **[C] The exponent triple (2,3,5) is the decode's class alphabet.** Measured rhyme: 2A primes (order 2 = edge = the u-form's port) carry a_p = 0 — pure noise, no bit — exactly the class the chart assigns to the noise share.
4. **[O] Named question:** is the Atkin–Lehner/Fricke ε (the phase the decode measures at every conductor) the arithmetic avatar of this chart's seam-at-i? The parity port and the Fricke involution keep arriving at the same bench.

**Corrections to the sheet (kept vs cut):** keep the head (syzygy-as-budget — now exact in the corrected normalization); fix the factor-3/role inversion per above; the mid-chain expression G = 1/[√(f⁵/H³) − 1] goes negative on the physical branch (sign slip); **cut the nested tail G²[√(G(√u))] — it crosses the atlas §5 fence** (G∘G is ill-typed: G ≥ 1 exits the domain; the documented G²-slot collision class).

*Machine artifacts: `klein_budget.gp` output in session log; script appended conceptually to bundle-C lineage. Offered, not self-filed.*
