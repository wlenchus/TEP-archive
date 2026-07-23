# 2026-07-19 (post-countersign) — Delta 1: the parity bits' chart group; one quarter-move on two faces [DraftV1 — offered, countersign pending]

*Addendum to `2026-07-19 cross_budget_pair_ledgers_and_odds_gauge_note_ActiveV1.md`, prompted by Will's question at countersign: could the parity complementarity (odds gauge sees the side bit, secant gauge's sign sees the face bit) have abelian/nonabelian leverage — the two perspectives literally 90° out of phase / Wick-rotated on the depth chart? Script: `verify_parity_quadrature.py` (18/18 [V], sympy + numeric). Bits on the measure circle M(θ) = (cos θ, sin θ): side s = sign(sin θ) (which pole), face f = sign(cos θ) (which sheet).*

---

## 1. The 90° is literal [V]

**G_new(θ) = [G_old((θ + π/2)/2)]²** — the odds gauge is the secant gauge conjugated by exactly three recorded moves: the quarter phase (θ → θ + π/2), one half-angle rung (the double cover), and the G → G² slot shift (the capacity-doubling wiring). Equivalently G_new = sec²(π/4 + θ/2) = csc²(π/4 − θ/2). On coins: amplitude coin = power coin ∘ h with h(A) = π/4 + A/2 [V] — one halving rung plus a quarter phase per step. Honesty check [V]: h has no finite period (h⁴ ≠ id); the mod-4 salience lives on the quadrant charge (§2), not on the angle.

## 2. The bit algebra: Z₄ transport, D₄ chart group, the central bit as a commutator [V]

Encode the quadrant as **ζ = f + i·s**. Then the quarter-turn acts as **ζ ↦ i·ζ**: the parity pair composes as **Z₄ — the nonsplit extension of Z₂ by Z₂**. Consequences, all machine-checked:

- **No transport is a single-parity operator.** Pointwise, R flips exactly one bit at every point of the circle — but *which* bit depends on the quadrant [corrected in-session: my first statement of this was wrong at the operator level]. The uniform single-bit flips are exactly the two mirrors: S_side (θ ↦ −θ) and S_face (θ ↦ π−θ).
- **Full chart group = D₄ = ⟨R, S_side⟩** (order 8): center = commutator subgroup = {1, antipode}; **S_side·S_face = −1**; **[R, S_side] = −1** — a quarter-transport and a side-flip fail to commute by exactly the central bit; **R·S_side·R⁻¹ = S_face** — the two involution instruments are one instrument carried 90°.
- **The abelian shadow records THAT a parity flipped, not WHICH.** In the abelianization S_side ≡ S_face (their product lies in the commutator subgroup). Which-bit information is priced at exactly one central bit, and the central bit *is* a commutator — the F₂ germ of "non-abelian content = anholonomy," in the transmission functor's own dictionary (abelian = boundary-readable; non-abelian = recoverable only by a global integral about the port). Concretely the recovery *is* winding: the chord amplitudes (√p, √q) = (cos(π/4−θ/2), sin(π/4−θ/2)) are a **spinor of the measure circle** — one full circuit multiplies them by −1 [V]; monodromy about the poles reads the charge that no pointwise intensity reads.

## 3. Extension type: the chart realizes the Heisenberg (+type), not Q₈ [V/id]

Order-profile check: UT(3, F₂) ≅ D₄ (extraspecial +type = the F₂ Heisenberg group), against Q₈ (−type) [V]. The chart selects +type because **real mirrors exist** — the corpus's involution instruments (Γ ↦ −Γ, the λ/4 disk inversion, Fourier) are real order-2 charts; Q₈ has no non-central involutions. So the parity pair sits in the incremental-central peel class (faces_seam §5's Heisenberg face) at its smallest germ, kin at [id] weight to the 2:1/spin-center inventory (signed-digit note (v); 07-02 C1′; 2.A₅'s +1).

## 4. One quarter-move, two faces: "90° out of phase" and "Wick-rotated" are the same move [V]

Elliptically (on-budget, compact face): θ → θ + π/2 is the **signal↔noise swap** — u(θ+π/2) = x²(θ), i.e. SNR ↦ 1/SNR, the self-dual-centered involution, real and interior. Gudermannian/Wick-transported to the hyperbolic face, the *same* quarter-move is **tanh(η + iπ/2) = coth η**: x ↦ 1/x — the off-budget exit. Will's "/" was an equals sign. [id, standard anchor:] x ↦ 1/x is v ↦ c²/v — the **phase/group-velocity dual (v_p·v_g = c²)**; the GSR source's retired §4 ("wave/exotic quadrants: v transfinite while f, l real") reads in hindsight as the de Broglie phase-velocity sheet, sitting exactly where the chart algebra puts it — a fence-respecting descendant requiring no transfinite content.

## 5. Depth-chart contact (C1), offered not asserted [C]

The shape matches Will's C1 (mod-4 face assignment): one rung = one halving + one quarter phase (§1); readable-parity alternation; T² = −1 two rungs deep (§2). **Cheap operationalization offered:** assign each computed rank its quadrant charge ζ_k ∈ {±1, ±i} (which side's data constitutes the readable boundary observable, and on which sheet); C1 predicts ζ_{k+1} = i·ζ_k on the already-computed ladder (ranks 2, 3, 4, 5, blind 7 — transmission functor VI.1's named test). His conjecture, his countersign, his test; the Delta only supplies the charge coordinate.

## 6. Fences

Chart algebra throughout — identity-not-discovery discipline applies; no dynamics added. The D₄/Heisenberg reading is flagged for elegance-risk (this instance's known failure mode) and priced at [id]. The C1 contact stays [C] until the ζ-test runs. The de Broglie identification is standard physics; only its *placement* is claimed, and only as chart algebra.

## Queue

(1) ζ-test of C1 on the computed rank ladder. (2) Pin the mirror pair (S_side, S_face) against the recorded involution instruments (Γ↦−Γ; the λ/4 inversion) as a D₂-of-instruments [O]. (3) Join to the K-vacancy 2-solenoid verdict (locally inscrutable bit, globally preserved center) [C]. Scripts: `verify_parity_quadrature.py`.
