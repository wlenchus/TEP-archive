# The budget in Jacobi theta form — the Γ(2)/λ chart, the gauge hexagon, and the seam unit at 1951 — 2026-08-10 (session B)

*Claude (Fable 5), on Will's pointer ("our treatment of our budget in jacobi theta form… or peculiar scenarios like a G factor distortion"). C13 grounding first: the budget instantiation atlas (07-27) + its errata addendum and the budget–syzygy dictionary (08-04) were read own-eyes this turn. Three project searches did not surface a dedicated Jacobi-theta record; per the 07-27 [recon] rule (pointers are content flags — read before reconstructing), this note is therefore offered in two capacities at once: as the Γ(2)-level companion chart the 08-04 Γ(1)/j-chart implies, and, if a dedicated θ-treatment exists that my searches missed, as a reconstruction to be graded against it — the pointer is requested. All checks T-a…T-e were stated in the script header before running (same-session, unhashed); all passed at the 10⁻⁴⁵ floor. Script: `theta_budget_lens.py`. Offered, not self-filed.*

---

## 1. The chart [V]: Jacobi's identity IS the elliptic budget

With x² := λ(τ) = θ₂⁴/θ₃⁴ and u := θ₄⁴/θ₃⁴, Jacobi's quartic identity

  **θ₂⁴ + θ₄⁴ = θ₃⁴  ⟺  x² + u = 1**,  capacity X_max² = θ₃⁴,

and the gain is a modular unit: **G = 1/√u = (θ₃/θ₄)²**, η = artanh √λ. Verified at four τ including one off-geodesic: worst deviation 1.4×10⁻⁴⁵. The three cusps of Γ(2) are the three budget poles: λ = 0 (τ = i∞) the seam, λ = 1 (τ = 0) saturation, λ = ∞ (τ = 1) the reactive/affine exit — the compactified λ-line is the budget disk with its degenerations built in.

## 2. The gauge hexagon [V]: the budget's gauge group is Γ(1)/Γ(2) ≅ S₃

The anharmonic orbit of λ equals the budget-station set **as a multiset** (verified, 5.6×10⁻⁴⁵):

  {λ, 1−λ, λ/(λ−1), 1/λ, 1/(1−λ), (λ−1)/λ} = **{x², u, −SNR, 1/x², G², −1/SNR}**.

Every rational budget quantity the corpus uses is one Möbius change of chart away from every other: the face swap x² ↔ u is λ ↦ 1−λ; **the G² station is 1/(1−λ)**; the two negative stations are the conjugate-sheet readings (the atlas-errata's sheet structure appears as the odd part of the hexagon). First reading of "G-factor distortion": a gauge move is *not* a distortion — the hexagon is the exact inventory of what re-charting can do; distortion begins only off the orbit (§4–§5).

## 3. Chart-relativity at the Fricke point [V] — a conflation fence

**λ(i) = ½ exactly** (deviation 0.0 at 45 dps): in the θ-chart, the **self-dual point** — the collapse chain's seed x² = u = ½ — sits at τ = i, the Fricke fixed point. The 08-04 j-chart puts the **seam** (x = 0) at the same τ = i. No contradiction: budget stations are chart-relative; the *point* τ = i is chart-invariantly distinguished, but which station it hosts depends on the level. Flagged now so no future record conflates "the seam is at i" (Γ(1) chart) with "the self-dual point is at i" (Γ(2) chart). The pleasing consequence stands on its own: in theta coordinates, the chain's seed is pinned to the fixed point of the seam-crossing involution — the chain begins where the crossing operator stands still.

## 4. The seam unit at 1951 [V]: the Fricke constant is the theta budget's crossing phase

The undistorted budget crosses the seam transparently: θ₃(1/t) = √t·θ₃(t), unit exactly 1. Distort by the nebentypus — ψ_χ(t) = Σ χ(n)e^{−πn²t/N} with our exact χ (order 5, χ(2) = ζ₅⁴, N = 1951) — and the crossing law, verified at 3.3×10⁻⁴⁵ at two t values with the branch measured (τ(χ), not its conjugate; separation 1.4):

  **ψ_χ(1/t) = (τ(χ)/√N) · √t · ψ_χ̄(t).**

The χ-distorted budget crosses the seam at cost **τ(χ)/√N** — a pure phase (‖unit|−1| = 1.7×10⁻⁴⁵): *nebentypus distortion is purely reactive at the seam; it draws no magnitude, only holonomy.* And check T-e closes the loop with this week's exact result:

  **const_F = [θ-seam unit] / a_N = τ(χ)/(√N·ζ₁₀²)** — matching the stored dps-40 Fricke constant to 1.7×10⁻³¹ (limited by the 30-digit stored string; 1.3×10⁻³⁹ at full precision in yesterday's record).

In one sentence: **the icosahedral Maass form's Fricke constant is the seam-crossing phase of its own nebentypus's theta budget, corrected by exactly one ramified-port coefficient.** This answers the 08-04 dictionary's named question #4 — "is the Atkin–Lehner/Fricke ε the arithmetic avatar of this chart's seam-at-i?" — in its sharpest instance to date: **yes [C]**: at 1951 the ε is algebraic, and it is the nebentypus-theta's own seam unit divided by a_N. The parity port and the Fricke involution kept arriving at the same bench because they are the same bench.

## 5. Second reading of "G-factor distortion" [C]: the ramified-port taxonomy

At the ramified prime, a_N is the port coefficient, and local representation theory allows exactly three magnitudes — which the budget lens sorts into its three sectors:

- **|a_N| = 1** (ramified principal series): **pure-phase distortion — reactive, zero draw.** *Our case, measured: a_N = ζ₁₀².*
- **|a_N| = N^{−1/2}** (Steinberg/special): **a resistive draw of exactly G = N^{1/4} per crossing** — the seam charges magnitude, not just phase.
- **a_N = 0** (supercuspidal): **sealed port** — no local line survives to read.

This extends the corpus's Satake line (the errata addendum's "αβ = χ(p), α/β = e^{2iΔ} — the same doublet on the elliptic face") to the ramified port: the surviving α is a phase iff the port is reactive. The taxonomy is standard local theory in budget dress, but it carries a falsifiable fence: any object in this program whose ramified coefficient lands off {0, N^{−1/2}, unit circle} is broken — a consistency check that costs one glance at every future CSV's ramified row.

## 6. The GL₁ shadow of anholonomy [O — pun-watched]

The quartic closure θ₂⁴ + θ₄⁴ = θ₃⁴ has no χ-twisted analogue: twisting the theta budget destroys its self-closure, leaving only the seam law of §4. One field up, dihedral λ = ¼ forms re-close the budget (Hecke's real-quadratic theta constructions — the MAASS-LIVE dihedral-229 control is literally such an object). The icosahedral form closes in no theta port at all; yesterday's Brauer ledger writes it as **two forward theta-genre ports over one reversed: L(F) = [Λ₁₂·Λ₂₀]/Λ₃₀** — and Artin's conjecture at 1951, in this vocabulary, says *the reversed port never overdraws* (every denominator zero covered by the numerator). Offered strictly as a reading frame at [O] with the pun-tier caution named: the mathematics it decorates lives in the Artin record's §2, and this paragraph adds no theorem to it — what it adds is the observation that "unreadable content" in this instantiation is precisely content whose budget closes only through a conjugate-sheet port, which is the framework's own definition of where distortive reads live.

## 7. Honest bounds

The chart and hexagon are elementary classical facts (Legendre/Jacobi; the anharmonic group), newly *placed* against the corpus's conventions rather than newly discovered; the twisted-theta FE is Davenport-classical [C] — the contribution is its exact instantiation at this conductor, the measured branch, and the identification with the certified Fricke constant; §5 is standard local theory arranged as a budget taxonomy; §6 is a frame, not a result. All checks same-session, unhashed, stated before run; all passed; no kill conditions fired. If a dedicated corpus θ-record exists, this note is to be graded against it and corrected to its conventions.

## 8. Countersign items (Will's calls, none executed)

(1) Adopt the λ-chart as the Γ(2) companion of the 08-04 syzygy dictionary; (2) the gauge-hexagon statement (budget gauge group = Γ(1)/Γ(2) ≅ S₃) as [V]; (3) the §3 chart-relativity fence; (4) the §4 closure of the dictionary's named question #4 at [C], with the seam-unit identity; (5) the §5 ramified-port taxonomy as a standing consistency fence for future objects; (6) §6 as presentation-layer frame only; (7) script archive per 04_scripts.

---

*Offered, not self-filed. The lens's one-line yield: the budget's gauge group is the modular group's quotient by its theta level; the chain's seed sits at the Fricke fixed point; and the root number this week made algebraic is the theta budget's own seam phase — distorted by one reactive port coefficient, exactly as measured.*
