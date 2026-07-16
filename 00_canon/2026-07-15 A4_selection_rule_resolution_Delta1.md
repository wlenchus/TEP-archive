# 2026-07-15 — A4 delta: selection-rule resolution (no-go + replacement law) [ActiveV1]

Tiers: [V]erified this session · [T]classical · [A]rgued · [C]onjecture · [O]pen · [id]entification.

## 0. Corpus updates consulted (per direction)

07-05 (Buhler control PASS): the live sign channel works by **certificate** — 35/35 sign bits decoded from membership data, with residual gauge = exactly one involution orbit (the Galois-conjugate pair, exchanged by the σ-flip set under ζ₂₀ ↦ ζ₂₀¹¹). 07-05 addendum: decoder3 validated component-wise; ram-filtering proven safe by the Hasse–Arf integrality line. 07-03: the Fricke selection rule Wv_D = −χ_D(−N)v_D and the ι-parity law are verified **on twisted modular symbols** (376/376) — completed spectral objects, not points. Template extracted: in the corpus's working practice, sign data is *certified* or read on *cohomology*; it is never a pointwise symmetry eigenvalue. A4 resolves in exactly that shape.

## 1. Two no-go lemmas [V-hand / T]

**Character no-go.** The anholonomy lattice Λ ⊂ ⟨D, U⟩ is 2- and 3-divisible (conjugation by D and U scales translations by 1/2 and 3). Every homomorphism ⟨D,U⟩ → ℤ₂ therefore kills Λ (characters annihilate divisible groups) and factors through the scale quotient ⟨2,3⟩ ≅ ℤ²; the surviving characters (K-parity, halving-parity) are **end-blind**. The end-separating character — odd on translations — exists on the mirror subgroup D_∞ = ⟨s₊, s₋⟩ (whose translation lattice 2ℤ is not divisible) and **does not extend** to the transformation group.

**Involution no-go.** Continuous self-maps of ℤ₂ commuting with the shortcut map = pullbacks through the Lagarias conjugacy of shift-commuting maps; the automorphisms of the one-sided full 2-shift are the symbol permutations [T, Hedlund]. So the unique nontrivial continuous commuting involution is the **parity-flip F̃** — and F̃ does not preserve ℤ (§2: −5 ↦ 4/5). Combined with ν (exchanges the ends, does not commute) and s± (grade the generators, character does not globalize): **every candidate involution loses exactly one of {commutes with T, preserves ℤ, separates the ends}. No pointwise Fricke analogue exists.**

## 2. The bulk involution F̃ and the flip census [V]

**Construction.** F̃ = stream-flip through the conjugacy (reconstruct ∘ complement ∘ parity-stream). Verified mod 2²⁶ on 150 random points: stream/reconstruct roundtrip exact; F̃² = id; F̃T = TF̃; F̃(1) = 2 (the trivial cycle is phase-shifted — self-paired); F̃(−5) = 4/5 in ℤ₂ exactly.

**Action on the cycle equation.** Word-complement w ↦ w̄: (n, K) ↦ (n, n−K), denominator 2ⁿ − 3ᴷ ↦ 2ⁿ − 3ⁿ⁻ᴷ. Haar-preserving.

**Census (all parity words, n ≤ 13).** Integral orbits found = exactly the known five:
{0}, {−1}, {1,2}, {−5,−7,−10}, {−17,−25,−34,−37,−41,−55,−61,−68,−82,−91,−136}.
Flip pairing: **{0} ↔ {−1}**; **{1,2} self-dual** (flip = phase shift); **−5-orbit ↦ {4/5, 2/5, 1/5}** (denominator 5 = 2³−3); **−17-orbit ↦ 5296/1967** (denominator 1967 = 2¹¹−3⁴).

**Word-space geometry.** The flip mirror sits at K/n = 1/2; the seam at K/n = log₃2 ≈ 0.6309 — non-concentric mirrors again, now in word space. The flip maps the entire negative-denominator region (K/n > 0.631) into the positive; self-dual necklaces require K = n/2 and hence all sit strictly positive-side; **the negative integer inventory flips to interior points of (0,1) ∩ ℚ** — boundary-to-interior, literally.

## 3. The selection law that exists [V, exact, trivial once seen]

On integral cycles: **end = sign(2ⁿ − 3ᴷ)** — verified across the census (numerators S(w) > 0 for every nonzero word, so sign(x) = sign(d)). The Collatz Fricke-analogue eigenvalue is **ledger-valued (the seam side of the word), not character-valued**. It selects the end *given* integrality and never grants integrality — the orthogonality verdict holds at the exact point predicted.

## 4. Adjudication — anchor updates

**A4 splits:**
- **A4a [promoted: firm].** The mirror grading is load-bearing as *bulk structure*: the F̃ duality (the unique nontrivial commuting involution), the word-complement action on the cycle equation, the non-concentric word-space mirrors, and the seam-sign law.
- **A4b [retired, with proof].** A global end-separating character / pointwise Fricke-type eigenvalue law is impossible (divisibility no-go; Hedlund uniqueness + integrality violation). Any richer selection rule must live on completed spectral data — convergent with the corpus's own practice (certificates, gauge pairs, symbols).

**Queue change.** The "selection-rule hunt" closes as posed. The (B)-instrument reduces to the **certificate program** (the OT1-methodology transplant), full stop; the two-radix theta tower and the (A)-side certificate/thinning computation stand unchanged.

**Consolidation inflection.** [I6] A4 | prior: symmetry-eigenvalue law sought → new: no-go proved; seam-sign law + F̃ duality installed as replacement | Axis: direction reversal + specificity | Trigger: divisibility computation, Hedlund uniqueness, flip census | σ: high | Provenance: a4_flip_census.py; 07-05/07-03 corpus consult.

**Drift watch.** A4's resolution is a direction reversal carried entirely by new evidence (two proofs + one census) — the healthy kind; no accommodation content.

## 5. Scripts and inputs

a4_flip_census.py (census, flip pairing, seam-sign law, F̃ verification mod 2²⁶). Classical inputs [T]: Hedlund (one-sided full-shift automorphisms); Lagarias (conjugacy). Corpus inputs: 07-05 Buhler PASS + addendum; 07-03 Fricke/ι laws. Parent record: 2026-07-15_collatz_tep_division_of_labor_record_ActiveV1.md (§4 superseded by this delta).
