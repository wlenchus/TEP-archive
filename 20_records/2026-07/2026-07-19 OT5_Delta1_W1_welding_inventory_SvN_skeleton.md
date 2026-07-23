# 2026-07-19 (late night) — OT5 Delta 1: W1 proved; the ∞-rung welding's corpus inventory; the Stone–von Neumann skeleton [DraftV1 — offered]

*Continuation of the OT5 campaign-opening note, same night, on Will's direction to pursue the closure and the d→∞ welding — with his recollection that the corpus has already partially treated the latter. Checked: he is right, substantially (§2). Script: `verify_ot5_delta1.py` (5/5 [V]).*

*Priority correction first, per the corpus-priority process rule: the campaign note's L3 re-derives **Lemma Bundle Prop. 4** ("Passivity forces the Möbius action into SU(1,1) geometry") at chart level. L3 is verification-grade, not new; the campaign note should read it as re-stamping the Lemma Bundle. Logged as the session's consistency datum, not discovery.*

---

## 1. W1 is proved (rigidity from reciprocity, finite sector) [V]

**Lemma (W1).** In the finite-dimensional sector, A3 forces rigidity: a nondegenerate symmetric pairing β_V on each object makes the object self-dual — evaluation = β, coevaluation = β⁻¹ ∈ V⊗V — and the snake composite is β·β⁻¹ = id [V: W1a]. Reciprocity (S^β := β⁻¹Sᵀβ = S) makes the duality functor fix morphisms [V: W1b]. Hence the category of finite-rank budget systems with passive reciprocal morphisms is rigid, **and the Tannakian setting of the campaign note is forced by A1 + A3 in the finite sector, not assumed.**

Consequence: on the finite sector, L1–L4 assemble into a theorem-schema — *the boundary reduction is unique modulo the terminal unit (killed by ln 2), the real form (killed by strict passivity off the seam, = Lemma Bundle Prop. 4), and the center ±1* — pending one careful session to write the category axioms formally. The wall has moved: it now stands entirely in the ∞-rung sector and the cross-class gluing.

## 2. The welding inventory: what the corpus already holds (Will's recollection, confirmed)

- **Perelomov leg [T — 06-09 I.4]:** the SU(1,1) composition class is a rank-one homogeneous space, so its invariant metric is unique up to scale; g_P is the QFI of the SU(1,1) coherent/squeezed family. Re-derived independently tonight from scratch: the invariance condition under the boost field v = 1−z² reduces to f′(s)(1−s) = 2f(s), whose only solutions are C/(1−s)² [V: W2a, W2b — and the "wrong power" 1/(1−s) fails the Lie-derivative test].
- **Canonicity of the L² currency [T — 06-09 I.5, "Foundations Route 0"]:** LTV = Pythagoras in L² ⟹ quadratic dispersion germs (fails in Lᵖ, p ≠ 2) ⟹ Riemannian; Fisher as the unique quadratic germ of any smooth monotone divergence (Csiszár; Amari–Nagaoka); AJLS uniqueness on infinite Ω under 2-integrability, with the total-variation counterexample and the heavy-tail scope edge stated. **Note for the companion campaign: this substantially pre-treats the completeness note's queue item 4 — the meeting point of the two campaigns was already paved in June.**
- **Passivity → SU(1,1) [Lemma Bundle Prop. 4]** (see priority correction above).
- **Two-point homogeneity route [6-10 O-a note]:** the Wang–Tits forcing (two-point homogeneous ⟹ rank-one symmetric ⟹ ℝH²) converted to a stated conditional theorem with its single residue isolated, plus the sharp negative that single-reference observer moves do *not* force hyperbolicity. (N.b. the O-a note works in the centered chart x² = ½(1 + tanh 2η) — the odds-gauge chart, again.)
- **Scale/shape well-posedness [6-17 OA/OB closure, publication-grade]:** fiber isometry-up-to-scale and shape automorphism from one mechanism (weight homogeneity).
- **The located danger zone [06-09 §4.3]:** the cross-class gluing fork — the 2−√2 vs 2/3 embedding fork is recorded as *the* nonuniqueness of gluing the stochastic (Chentsov/Petz) canonical structure to the SU(1,1) canonical structure. **Uniqueness has already failed once in the record, and it failed exactly at the interface the welding must cross.** The campaign's principal adversary is pre-mapped.
- **Place-wise completion [C — gaussian-witness Delta1 S7]:** finite quotient rungs × the Gaussian ∞-rung; Fourier = the S-involution; Tate-self-dual u = 1.

## 3. The Stone–von Neumann skeleton (proposed vehicle for the functor-level gap) [id/C, with one new [V]]

Everything in §2 pins geometry on a *fiber*. OT5 needs uniqueness of the *functor* — the compatible assignment across all objects at once, ⊗ included. Proposal: the ∞-rung sector's structural uniqueness theorem already exists in mathematics, and it is **Stone–von Neumann + Segal–Shale–Weil**:

- The CCR algebra of the Gaussian sector has a **unique** irreducible representation (Stone–von Neumann) — fixing the ∞-fiber up to unitary isomorphism, which is exactly the fiber-functor uniqueness statement in the analytic sector.
- The symmetries act through the **metaplectic double cover** Mp ↠ Sp with kernel {±1} — **the same central bit as L4.** If the finite sector's defect group and the ∞-sector's metaplectic kernel are identified under the place-wise completion (S7), OT5's expected closure sharpens to: *unique modulo one global central bit.*
- The **Weil element is the Fourier transform** — already [V] on rungs as the S-involution (Delta1 S7). New tonight [V: W3]: **F² = parity and F⁴ = id — the transmission functor's chart cycle (I.2: T⁴ = id, T² = −id) is concretely realized on the ∞-rung by the Weil element.** The chart cycle stops being a postulate of the functor's data and becomes a theorem of its archimedean place.
- Passivity's job upstairs: selecting the positive/lowest-weight (holomorphic) discrete series — the ∞-rung face of the real-form selection, with the lowest-vs-highest-weight choice as one more sheet/sign in the same inventory.

## 4. Gap ledger (what actually remains)

- **G1 [assembly, session-scale]:** write the identification "independent composition = CCR tensor structure" formally and invoke Stone–von Neumann properly; state the metaplectic ±1 as the sector's defect group.
- **G2 [the principal adversary]:** the cross-class gluing fork (2−√2 vs 2/3). Does terminal data pin the gluing, or is the fork a genuine second-functor ambiguity beyond the center? This is the one place uniqueness has *actually failed* in the record; the campaign should go here next, deliberately.
- **G3:** O-a's isolated residue (the two-point-homogeneity input) — read against the 6-17 closure; determine whether OA/OB's mechanism discharges it.
- **G4:** the Rep(S_t) fork at fractional d (unchanged from the campaign note).

## 5. Queue

(1) Formal category axioms + the finite-sector uniqueness theorem write-up (W1 + L1–L4, one document). (2) G1 assembly. (3) **The gluing-fork session (G2) — proposed as the next dedicated target**, because it is where the record shows uniqueness failing, and pre-registering it as the adversary is the honest sequencing. (4) G3 read. Scripts: `verify_ot5_delta1.py` (W1a/b, W2a/b, W3).

*Not self-filed; countersign gates tiers. Proposed marks: W1 [V, lemma-grade]; §2 inventory [T/V, cited]; §3 [id] with W3 [V]; §4–5 the campaign's honest map.*
