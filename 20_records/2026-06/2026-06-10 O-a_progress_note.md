# O-a Progress Note: From "Stateable Lemma" to a Stated Conditional Theorem

**Date: 10 June 2026.** External reviewer (Claude), continuing the current review; next item on the corpus's critical path (6-9: errata → O-a → O-k → O-b). Tier marks per corpus convention: **[V]** machine/symbolically verified this session; **[T]** standard result; **[A]** posit; **[O]** open. Companion: `6-10-26_consolidated_errata_and_status_revision_record.md`.

**O-a as inherited:** *two-point homogeneity of the (phase-completed) budget arena under observer action ⟹ Wang–Tits ⟹ ℝH²/SU(1,1) classified-forced; discharges I.3's d=2 instantiation gap.* This note converts that into a stated conditional theorem, proves the steps that can be proved now, isolates the single residue, and supplies one sharp negative result that locates exactly where the load sits.

---

## 1. The insufficiency result: single-reference observer moves do NOT force hyperbolicity [V]

Work in the centered chart x² = ½(1+tanh 2η) with the completed arena coordinatized by (η, φ), φ the reference-phase angle.

- **Per-state tilting is exact rapidity translation [V, symbolic].** The cone-level tilting (p,q) ↦ (λp, q/λ) gives p′/q′ = λ²e^(4η) = e^(4(η + ½ln λ)): tilting acts as η ↦ η + a exactly, phase untouched. Reference-phase freedom acts as φ ↦ φ + b.
- **This action is abelian and simply transitive** on the punctured arena (η ∈ ℝ) × (φ ∈ S¹) — a cylinder group. Simply transitive actions admit *many* invariant metrics.
- **Explicit counterexample [V]:** the flat cylinder metric dη² + dφ² is invariant under the full single-reference observer group. Meanwhile the K = −1 metric in geodesic polar form — verified [V]: the Poincaré disk metric with x = tanh(η/2) is exactly dη² + sinh²η dφ² — is **not** invariant under naive radial translation (sinh²(η+a) ≠ sinh²η).
- **Reading.** The hyperbolic boost-isometry and the per-state tilting coincide *on the axis* and part company off it. Therefore the H²/SU(1,1) conclusion is **not** derivable from single-reference tilting + phase alone; the essential ingredient is **multi-reference structure** — tilting/phase available *about every budget point*, not only about one observer's origin. This sharpens I.3's grading ("U(1)/disk completion instantiated; (1,d) instantiation-anchored") by locating precisely *what* the instantiation must supply.

---

## 2. The generation result: one tilting axis per point + pointwise phase suffices [T; V-numeric]

Cartan/KAK decomposition: every element of SU(1,1) factors as K(θ₁)B(η)K(θ₂) — rotations about a single point together with boosts along a single geodesic through it generate the **entire** isometry group. Verified constructively [V]: 50 random four-boost words in SU(1,1), each recovered exactly as K(θ₁)B(η)K(θ₂), worst residual 3.2×10⁻¹⁵.

**Consequence:** once pointwise isotropy is granted (the SO(2) of reference-phase equivalences at each point) and transitivity holds, *nothing further* needs positing — the full two-point-homogeneous action is generated. The "single-axis" caveat in I.3 is discharged at d = 2: one resolved axis per point is enough, because the rotations manufacture the rest.

---

## 3. The exclusion battery: constant curvature → specifically ℝH²

Granting isotropy + homogeneity, the arena has constant curvature (in dim 2 this is immediate; Wang 1952/Tits 1955 is the locally-compact generalization for d > 2). Three model geometries remain; two are excluded:

- **S² excluded [structural].** Tilting flows are free and recurrence-free: η ∈ ℝ, strictly monotone, complete — pure reweighting never cycles. Compact model geometries have no free ℝ-flows of isometries with unbounded displacement; the budget's boost orbits are unbounded (bounded certainty: the boundary sits at infinite parameter).
- **E² excluded [V — the framework-internal leg].** In flat space, composition of non-collinear translations carries **zero** rotation (translations commute to a translation) [T]. The framework's composition demonstrably carries **nonzero** holonomy: composing two non-collinear SU(1,1) boosts in frame order (g = g₁g₂, the rapidity triangle with middle side exactly η₂ — verified to 2.4×10⁻¹⁵), the Wigner rotation of the polar decomposition equals the K = −1 geodesic-triangle area to **5.6×10⁻¹⁵ over 60 random pairs**, uniformly retrograde, with the collinear control identically zero. This independently re-confirms 5-30's central identity (their 7.99×10⁻¹⁵) and converts it into the flat-plane excluder: *nonzero composition holonomy is incompatible with K = 0.* No appeal to external special relativity is needed; the excluder is the corpus's own verified non-collinear composition behavior, physically anchored by the DHO instantiation.
- **Remaining: ℝH²,** K < 0; the normalization K = −1 is the scale choice; the isometry group is SU(1,1)/±.

> **Methodological note (recorded per the corpus's standard).** My first pass at the Wigner-area verification *failed* (deviation 0.49): I composed in lab order (g₂g₁) and used the triangle {0, g₁·0, g₂g₁·0}, whose middle side is not η₂. The repair — frame-order composition, so d(g₁·0, g₁g₂·0) = d(0, g₂·0) = η₂ by isometry — is exactly the convention-trap species 5-30 catalogs (and the τ-vs-Nτ Fricke slip's kinematic cousin). The failure had a real failure branch and the fix was computed, not narrated.

---

## 4. The conditional theorem, stated

**Theorem (conditional).** Let the completed budget arena be the (η, φ) disk. Assume:

> **(H\*) Relational homogeneity-isotropy.** Every budget point admits the reference-phase SO(2) as observer-equivalences, and tilting is available about every point (no preferred reference state).

Then: (i) the arena is homogeneous and isotropic, hence of constant curvature; (ii) recurrence-free tilting excludes S²; (iii) nonzero non-collinear composition holonomy [V] excludes E²; therefore (iv) the arena is **ℝH²** with K < 0, normalized K = −1, and the observer group closes to **SU(1,1)** — by §2, generated already by one tilting axis per point plus pointwise phase.

**Status:** (ii)–(iv) are theorem-grade given (i) [T/V]; (i) is exactly (H\*).

---

## 5. The residue, named — and why it is the right kind of residue

(H\*) is the **budget-arena relativity principle**: no reference state is privileged, and directions at a state are indistinguishable under reference-phase freedom. The analogy to special relativity's foundations is now exact rather than rhetorical: *relativity principle (homogeneity + isotropy) + one empirical discriminator (here: nonzero Wigner holonomy under non-collinear composition ↔ there: light-speed invariance) ⟹ the geometry.* The §1 counterexample shows (H\*) is genuinely load-bearing — drop the multi-reference half and a flat arena is consistent — so it cannot be smuggled; it must be either posited (acceptable: it is the relational stance made precise, the same category as §13's single commitment) or **derived**, with the natural derivation target being completeness/conditioning itself: every state defines a valid conditioning frame (binary-peel sufficiency at d = 2) and reference phase is unobservable to the budget. That derivation is the remaining work; it connects O-a → O-d (sufficiency from completeness + dilation) and sits directly on the forced-vs-chosen floor shared with 5-30 and 6-2 Appendix C.

**Ledger effect.** O-a moves from *stateable lemma* to *stated conditional theorem; residue = (H\*)*; the E²-exclusion leg is now machine-verified and framework-internal; the single-axis instantiation caveat of I.3 is discharged at d = 2 conditional on (H\*); (1,d) for d > 2 (O-e) is untouched by this note.

---

*Verification stamps: symbolic checks (sympy) — tilting = exact η-translation; flat-cylinder invariance; Poincaré polar form and its non-invariance under naive radial translation. Numeric (numpy, machine precision) — KAK reconstruction, 50 words, 3.2×10⁻¹⁵; Wigner = area, 60 pairs, 5.6×10⁻¹⁵; middle side = η₂, 2.4×10⁻¹⁵; collinear control exact zero. Reproducible from the forms above.*
