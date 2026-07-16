# 2026-07-15 — A4 delta addendum: direction duality, reversal, chirality [ActiveV1]

Prompted by Will's audit question (directional messages; abelian vs non-abelian content per perspective; recoverable resolvents; rank/Galois). Honest scope admission up front: the review had **not** been thorough — the A4 no-go covered pointwise involutions only, and the direction-reversal involution (an anti-automorphism on words/cycles, hence outside Hedlund's scope) had not been checked. Checking it produces the sharpest catch of the session.

## 1. The direction × content ledger [V/T]

G = Λ ⋊ ⟨2,3⟩ is metabelian: **G^ab = ℤ² = the ledger** (rank 2 = the two ports); **[G,G] = Λ = the anholonomy**. Hence:

| | abelian content (ledger) | non-abelian content (cocycle) |
|---|---|---|
| **forward (encode)** | drift, criticality, seam side — conveyed as totals | the coset n₀ mod 2^{C_K} — conveyed progressively, losslessly in the limit |
| **backward (decode)** | tree growth 1.264, Kraft/capacity | the pruning pattern (which cosets live over ℤ), inventory, basins |

**Losses per perspective:** forward-at-finite-time loses the archimedean representative (the integer among the coset); backward-at-finite-depth loses everything outside the basin; abelianization loses everything but the ledger; direction-symmetrization loses chirality (§3); flip-symmetrization loses end orientation. **"Indistinguishable," sharpened:** cyclicity and divergence are *tail events* of the symbol stream; under the Bernoulli bulk they are 0–1 by Kolmogorov, and no finite-time observable in either direction decides a tail event. All prior indistinguishability claims survive in this form, strengthened.

## 2. Two senses of "end" — the law statement refined [V]

The delta's §3 conflated two questions the audit separates:
- **Solution-locus end** (which half-line hosts an integral word's cycle): **abelian, exact** — end = sign(2ⁿ − 3ᴷ), a ledger functional. This is the seam-sign law, correctly stated.
- **System/mirror end** (which mirror dresses the tripling; 3x+1 vs 3x−1 as abstract systems): **non-abelian**, and provably not character-readable (the divisibility no-go).
The two are extensionally matched on inventories because ν conjugates the systems — but they are different questions, and only the first is abelian-recoverable. The delta's law is the first sense.

## 3. The reversal involution R and the chirality catch [V]

**Definition.** R = word reversal = the anti-automorphism M ↦ JMᵀJ on the transfer matrices (letters map to inverse-scale letters; diagonal (3ᴷ, 2ⁿ) direction-invariant; the S-entry direction-covariant). R acts on cycles/spectral data, not on points — exactly the level the A4 delta said richer structure must inhabit, and exactly what had not been checked.

**Findings (integral inventory, census-complete to n = 13):**
- {0}, {−1}, {1,2}, {−5,−7,−10}: **achiral** — the reversed word is a rotation; the R-image is a phase of the same cycle (verified by phase membership).
- **The −17 orbit is chiral** (block pattern 1⁴0¹1³0³ vs reversed 1⁴0³1³0¹): its R-partner is **−20632/139** — expelled from ℤ with denominator 139 = |2¹¹ − 3⁷|. Composites: F̃ ↦ 5296/1967, F̃R ↦ 121/1967.
- **Background:** at (n,K) = (11,7), 20/30 necklaces are chiral (67%). The inventory's 4/5 achirality is the anomaly, not the −17's chirality.

**The chirality bit is the precise lost information of direction-symmetrization:** every dihedral-invariant (resolvent) observable is blind to which of the −17 pair is the integral one. And the involution ecology now reads: F̃ (commutes pointwise, breaks ℤ), R (spectral-level, breaks ℤ on the chiral member), ν (exchanges systems, no commutation), s± (grade generators, no global character) — **checked one level up, the A4b conclusion stands: no reading is simultaneously dynamical, integral, and separating.** A4a strengthens: the duality structure now includes R, with characteristic expulsion denominators {5, 139, 1967}.

## 4. Resolvents, rank, Galois [V/id]

**Recoverability = solvability, literally.** Derived length 2 ⟹ two-read recovery: first the abelian quotient (the ledger), then the abelian-but-twisted kernel (the coset) — from *either* direction alone the full datum is recoverable in the limit (forward: coset stream → n₀ by the boundary formula; backward: the point is held). The framework's "solvability as communicability" is instantiated word-for-word: this Galois-like group is solvable, and that is *why* the anholonomy is recoverable rather than inscrutable — opacity here is Diophantine, never A₅-type.

**The resolvent tower:** invariants of ⟨rotation⟩ ⊂ ⟨rotation, R⟩ ⊂ ⟨rotation, R, F̃⟩ acting on words at fixed ledger — cycle point-sets, then dihedral classes (losing chirality), then flip-paired classes (losing end orientation) — bottoming out in the ledger. Forward messages carry cyclotomic-congruence (abelian class-field-corner) data exactly per the 06-28 verdict; the census-level "Galois group" is combinatorial (necklace dihedral × flip), consistent with all cycle solutions being rational.

## 5. Anchor/inflection updates

- [I7] A4 | prior: no-go treated as closing the involution question → new: no-go scope annotated *pointwise*; spectral-level ecology {R, F̃, F̃R} checked, all integrality-violating on parts of the inventory; chirality bit identified as the direction-loss | Axis: specificity + scope | Trigger: Will's audit question | σ: high | Provenance: a4_reversal_audit.py.
- Drift watch: the correction stream on A4 remains evidence-coupled (each step carried a proof or a census); no accommodation drift.

## 6. Script

a4_reversal_audit.py (chirality test per orbit, R-partners and denominators, composites, background chirality rate). Parent: 2026-07-15_A4_delta_selection_rule_resolution_ActiveV1.md (§1 scope note, §3 refinement per §2 above).
