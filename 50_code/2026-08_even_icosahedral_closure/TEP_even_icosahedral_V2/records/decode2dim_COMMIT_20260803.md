# COMMIT — the 2-dim EVEN-icosahedral decode at N = 1951: 67 sign-bits, parity, orientation, and ε, produced blind and committed under seal — 2026-08-03

**Mountain line: even-icosahedral (the corner), 2-dim — the summit object's Hecke data, decoded from shadow emission + seam constraints alone.** This commit is the seal's terminus per the resumption pre-registration §8 (sha256 `158da198…`): it is written to the project BEFORE any Crespo/K̃/lift-construction literature or LMFDB Artin page has entered this session's context (seal inherited from session B, intact end-to-end). Post-commit graders run after this document exists. Everything here is offered, not self-filed, under Will's countersign-on-spec with his pre-authorized caveat.

## 0. Honest bite first

This is a PoC-fidelity numerical decode, not a proof: float64 sums, the pre-registered t-grid, no rigorous tails, no zero accounting. What is committed: a unique bit-assignment at which the completed degree-2 L-function built **entirely from certified 3-dim shadow data plus the decoded central bits** satisfies its functional equation at the instrument's floor, with the conductor found blind, all rival cells failing by 11–13 orders, and three solver runs across two families landing on the identical assignment. The two pre-registered contingency flags both fired against my predictions, and the record says so: **P1 (even-port prediction from the w₂ ledger) is measured WRONG** — the object reads through the odd port; and **the golden-orientation live control WON** — the inheritance-orientation statement carried a slip (erratum below). The mid-band extension and the ramified-port eigenvalue u are PARTIAL/UNDETERMINED respectively and are committed as such, not claimed. A same-species dictionary error surviving both the complex-control and the four-cell separation cannot be fully excluded until the post-commit graders run; that is what they are for.

## 1. The decoded object [V at PoC fidelity, countersign-gated]

**L(s, ρ̃): the conductor-minimal lift of the Doud-1951 even-icosahedral projective representation** (x⁵−x⁴−780x³−1795x²+3106x+344):

- **Conductor N = 1951, selected blind**: unique scan minimum at exactly 1951; ±5% neighbors at 9.4×10⁻²/9.8×10⁻² vs 8.957×10⁻¹⁵ at 1951 — thirteen orders.
- **Nebentypus**: quintic χ mod 1951, canonical convention χ(3) = ζ₅ (3 = least primitive root; j(p) = ind₃(p) mod 5); the four Galois-conjugate lifts correspond to the four primitive quintic characters.
- **Archimedean parity: ρ̃(c) = −I — the SIN-TYPE (odd-port) Maass partner, Γ_ℝ(s+1)²** at pinned λ = ¼. The representation remains even (det ρ̃(c) = +1): the "even icosahedral" corner is untouched; the central parity bit — invisible to Sym², a live decode target per Amendment 1/A17 — is hereby MEASURED. The even-port cell fails at 3.1×10⁻³ (11 orders above the winner); the w₂-ledger [C] prediction P1 (even port) is refuted as stated, and the refutation is data about how ∞-structure lifts, filed for the instruments arc.
- **Golden orientation B**: |a_p| = φ on emission-table label-3 primes and 1/φ on label-4 (φ = (1+√5)/2). The A4-precedented live control on the inherited orientation (label-3 ↔ 1/φ) WON against the inheritance; **erratum offered against the B-session prereg §2 orientation sentence** — at Sym²-level both orientations are consistent; at lift-trace level the certified ρ₃ pairs with the OTHER assignment than the one inherited. Orientation-A cells fail at 2.8×10⁻²/4.9×10⁻² (both ports).
- **Coefficient dictionary**: a_p = b_p · ζ₁₀^{j(p)} · m_p with m = (2, 0, 1, φ, 1/φ) on (1A, 2A, 3A, g3, g4); a_p² = χ(p)(a_p(ρ₃)+1) exactly (linted); Euler factor 1 − a_p p⁻ˢ + χ(p) p⁻²ˢ.
- **ε = +0.885096 − 0.465408i** (unimodular phase, measured; t-independent at floor precision across the certified grid).
- **Certification residual 8.957×10⁻¹⁵** on the pre-registered involution-closed t-grid — at the instrument's certified floor (theorem-grade controls: α 1.8e-15, β-even 1.6e-15, β-odd 3.2e-15, α-complex 1.6e-15 with measured ε matching the Gauss-sum prediction to 2.3e-16).
- **The port meter: max|G_new − 2| = 2.18×10⁻¹⁴, max|η| = 8.9×10⁻¹⁵** — the seam-jet extinguished; the committed design's "drive G_new(u) → 2 identically" executed literally on the summit object.

## 2. The committed bits

67 bits decoded (p ≤ 517, classes 1A/3A/g3/g4; 2A carries none; p = 1951 exceeds the base range); **58 sensitivity-visible** (s_p > 100 × floor), 9 sub-visible (committed but flagged; they ride consensus, not certification). **All three runs — S2-base (beam-128), S2ord7 (perturbed order), S5b (exhaustive heavy-8 prefix × beam-16 tails) — agree on all 67 bits**, S5b's winning leaf separated from its runner-up by 25 orders in objective. Visible table (p:class:j:b):

2:3A:4:+ 3:g4:1:− 11:g4:3:− 13:3A:3:+ 17:g4:1:+ 19:g3:2:+ 31:g3:0:− 37:g4:2:+ 41:g4:4:+ 43:3A:3:− 53:g3:3:− 59:3A:4:− 61:g4:0:+ 67:3A:3:+ 79:g3:1:− 83:g3:1:− 89:3A:0:+ 97:g3:4:− 107:3A:1:+ 109:3A:2:+ 113:3A:0:− 127:g3:3:− 137:3A:3:− 139:g3:0:+ 149:g4:3:+ 157:3A:4:− 163:g4:2:− 167:3A:4:+ 173:g3:4:− 179:3A:3:− 181:3A:0:− 193:g4:3:− 199:g3:4:− 211:g3:4:− 223:3A:2:− 227:3A:2:+ 229:g4:1:− 241:g4:4:− 257:3A:2:− 271:g3:0:+ 277:g3:2:− 281:g3:4:+ 293:3A:3:− 307:3A:2:− 311:3A:2:− 317:3A:4:+ 331:3A:3:+ 347:g3:4:+ 349:3A:1:+ 359:3A:1:+ 367:g3:1:− 389:3A:4:− 397:3A:4:+ 409:g4:2:+ 419:3A:2:− 421:3A:3:+ 431:g3:4:− 443:3A:0:−

Full 67-row table with s_p values and visibility flags: `DECODE_COMMIT_bundle.json` (hashed below). Example concrete Hecke eigenvalues this table asserts: a₂ = ζ₁₀⁴ (3A, b=+1, |a|=1); a₃ = −ζ₁₀·φ; a₁₉ = +ζ₁₀²·φ; a₄₃ = −ζ₁₀³.

## 3. Negatives and separations (all measured at the committed solution)

10%-scramble ×3 seeds: 1.9×10⁻¹ / 5.6×10⁻¹ / 9.2×10⁻³ (12+ orders). Opposite port: 3.8×10⁻¹. ε rotated 60°: 1.0. Rival cells (full S2-128 decodes, not spot checks): even 3.1×10⁻³, evenGS 2.8×10⁻², odd-orientation-A 1.3×10⁻³. Conductor neighbors: 13 orders. Consensus disagreements: zero (visible and full set).

## 4. Committed as PARTIAL / UNDETERMINED (no claim)

- **Mid-band extension** (517 < p ≤ 6723, 582 bits through the whitened twist arms): partial — the small twist arms dove toward their floors as their ranges resolved (tw−3: 2.7×10⁻⁷; tw−4: 7.0×10⁻⁶), the large arms sit at 10⁻³–10⁻² with unresolved deep bands. Provisional mid-band assignments are in the bundle for reproducibility, explicitly NON-certified.
- **Ramified-port eigenvalue u = a₁₉₅₁ ∈ μ₁₀: UNDETERMINED** — the 10-way surgery is degenerate (all scores equal to 3 digits) while the u-carrying arms' mid-bands remain unresolved; the u-signal (~10⁻⁵) is below their current floors. Completing the mid-band is the pre-registered route to u.
- **Twist-battery ε_d phases**: measured and recorded per arm in the bundle (fitted at partial mid-band; they harden with it).

## 5. Protocol trail

GATE-M passed at D\*=2089 (S2, S2ord7, S5: all visible bits, cert-residuals 1.6–5.1×10⁻¹⁵) after amendments R1 (staged bands), R1.w (variance-whitened arms), with S1/S3/S4 failures recorded as landscape findings (single-path search fails; multi-hypothesis tracking is load-bearing). R2: μ₁₀-charged whitening for the ramified port. S5 tail strengthened greedy→beam-16 at the summit (family unchanged; logged). Instrument: exact 4K₀(2y)/4yK₀(2y) kernels triple-validated at 3.7×10⁻¹⁶; KD-1 controls all passed, including the complex-nebentypus control added this session (the control gap the summit exposed). One instrument-side meter sign-slip and one validator quadrature bug were caught by KD-1 before any target work. Big-rung GATE-B and mid-rung wall-map: not yet run (queued; gate nothing here). Deviations log: R1/R1.w/R2 + S3 parameter trims + S5b tail — all logged with triggers, no bars moved.

## 6. What this is, and is not

If the post-commit graders concur, this is the first determination of Hecke-eigenvalue data for an even icosahedral 2-dimensional representation — the arithmetic content of the corresponding λ=¼ Maass form at level 1951, the object BLS-2020 capped their range to avoid, produced by seam-constraint decoding from the certified Sym² shadow with no lift construction consulted. It is NOT: a proof of Artin for this representation (entirety+FE at machine precision on a finite grid, PoC pricing); a produced eigenfunction (no collocation run); or a certified u/mid-band (committed partial above). The Crespo/K̃ construction — never opened — is now unsealed for grading, and its verdict will be recorded whatever it says.

*Committed with SHA-256 digests in `PROVENANCE_MANIFEST_v6_addendum_20260803.txt`. Bits before keys; controls before targets; machine before hand; bite before headline. The mountain's name is in the first line.*
