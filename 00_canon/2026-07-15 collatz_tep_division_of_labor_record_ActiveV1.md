# 2026-07-15 — Collatz × TEP: division-of-labor record [ActiveV1]

## 0. Scope, provenance, controls

Single-session thread (nine turns), question: **is TEP a structural guide for Collatz, or a dictionary?** This record fixes the verified skeleton, the two open cores, the failed predictions (logged, not accommodated), and the queued decisive computations. Everything tagged [V] was computed live this session (scripts in §8); [T] is classical; [id] is identification pending shape-match or corpus sign-off; [C] conjecture with named computation; [O] open.

**Standing controls for every claim in this thread:** 3x−1 (which *is* 3x+1 on the negative half-line: negation conjugacy, [V]); 5x+1 (supercritical, cycles + conjectured divergence, [V-empirical]); the generalized multi-branch family is Π⁰₂-undecidable [T, Conway; Kurtz–Simon] — blocking arguments uniform over Conway's class, but **not** over the critical family 3x+d.

---

## 1. Presentation and semidirect decomposition [V]

**The g-lattice.** With g(m) = 3m−1: g(km) = k·g(m) + (k−1) for all k (the affine semigroup A_k(x) = kx+(k−1), A_m∘A_n = A_mn, common fixed point −1); h = g+1 = 3m is exactly homogeneous; g(m) = A_m(2). For n = 2m−1 the near-consecutive triple is {3n−1, 3n+1, 3n+2} = {g(n), s(m), g(2m)} with hole at 3n: **one emitted symbol and one silent slot per lattice cell** (mod-3 obstruction: the odd-step image avoids ≡ 0 mod 3).

**Dictionary landing (turn 1).** g(2m) = 1 + s(m) ↔ G² = 1 + SNR is slot-exact (the budget identity; "identity, not discovery," 06-28). The leg s = 2g is exact only at privileged points: **golden** (SNR = G = φ; budget-involution conjugate of the recorded SNR = x point) and **silver** (both legs at one argument ⟹ G² = 2G+1, G = 1+√2, u = 3−2√2 — a recorded CM value). Generic content: the affine (degree-1 Ritt) shadow of the quadratic doubling, beside the power-map face (Hecke T₂ = q↦q²) and the Chebyshev face; the dropped SNR² term is the graded/t-deformation slot.

**Generators and grading.** D = x/2 (even, pure scaling); U± = 3x±1 = s±∘(−3x) **exactly**, with s± the mirrors at ±1/2: the Collatz system is a ℤ₂-graded (mirror-graded) cascade — tripling odd, halving even; **the two ends of the critical rule differ only in which mirror dresses the tripling**, and the mirrors form the two conjugacy classes of reflections in the dihedral closure (centers ±1/2 mod 2ℤ). The end-separating character is odd on translations: a torsion character of the anholonomy lattice.

**Semidirect structure.** [x↦2x, x↦3x] = id (the scale axes are genuinely independent — adelically, the ports 2 and 3; "Euler product = port independence"); [D, U] = translation by −1/2 (pure N). ⟨D,U⟩ = Λ ⋊ ⟨2,3⟩, metabelian. A K-step word with halving pattern (c₁…c_K), C = Σcⱼ, composes to x ↦ (3^K/2^C)x + Σⱼ3^{K−j}2^{C_{j−1}}/2^C: **linear part = the abelian ledger (totals only); translation part = the path-ordered N-cocycle** (all 10 interleavings distinct at K=3, C=6 with ledger fixed). Cycle condition = **holonomy pays the abelian gap**: n₀(2^C − 3^K) = Σ3^{K−j}2^{C_{j−1}}; trivial cycle = minimal saturation (1·1 = 1); the −5 cycle checks at K=2, c=(1,2); the negative cycles are the s₋-end inventory.

---

## 2. Anholonomy: classification and completion [V/T/id]

**Trichotomy (completes the 05-30 Thomas record).** Two one-parameter affine/hyperbolic generators: share both fixed points → commute; share none (non-collinear boosts) → **elliptic** commutator: Wigner rotation = K=−1 Gauss–Bonnet area (corpus-verified on the purity disk); share exactly one → **parabolic** commutator: the Collatz case. N-anholonomy is horocycle-displacement-valued, with **zero invariant continuum content** (all parabolics conjugate); the amount is defined only relative to the preserved lattice ℤ — the precise sense in which the residual difficulty is arithmetic. Contact: the 06-28 open join on Busemann/horocyclic projection; this thread is its concrete arithmetic tenant.

**2-adic completion.** The transported cocycle converges 2-adically to −n₀: ν₂(3^K n₀ + S_K) = C_K exactly (verified on orbit(7), valuation climbing through the terminal cycle) — the Lagarias conjugacy. **The anholonomy is a lossless encoding of the origin**; bulk-side it is a coordinate, and the dynamics in that coordinate is the full Bernoulli shift. "Decisively modeled" is locally achieved at the place 2; the residue is the integrality locus across three places (|·|₂ spend, |·|₃ transport, |·|_∞ descent).

**Composition-face placement.** Transfer matrices [[3, d],[0, 2^c]]: the det ≠ 1 Borel shadow of the corpus's flux-forced SU(1,1) face. Projectivized, each step is strictly hyperbolic with **per-step rapidity = ½|ln 3 − c ln 2|** (exact: (3+2^c)/2√(3·2^c) = cosh(½ ln(3/2^c))); AM–GM is strict per step (2^c ≠ 3) and per word (2^C ≠ 3^K): **the elliptic region is dynamically empty**, and triangularity means no word ever writes into the K-channel. The ensemble is Kesten-critical: E[3·2^{−ν}] = 1 exactly; κ = 1 the unique positive exponent. **Collatz is pinned to a parabolic seam it never occupies.** The seam's Jordan pair {y^{1/2}, y^{1/2}log y} (07-03: excess = jet-displaced content, rank = jet order) is structurally the critical-cascade pair: natural martingale dies at criticality, the log-weighted derivative partner survives [id].

---

## 3. Mode structure, recurrence, and the (A)/(B) factorization [V/T]

**The factorization.** Conjecture = (A) **boundedness** (every orbit on all of ℤ eventually periodic) ∧ (B) **cycle inventory** (the positive d=1 end holds only {1,2,4}); (d)-bridge = pigeonhole. (A) is sign-blind and empirically family-uniform: d ∈ {±1, 5, 7, 11, 13}, 20,000 starts each, **zero divergences; inventories 1, 3, 6, 2, 3, 10 cycles** — (B) is provably non-generic. 5x+1: 3 cycles + 910 capped starts; orbit(7) > 10¹² in 87 accelerated steps.

**Modes = places.** Position-divergence (infinite non-cycling) and momentum-divergence (unbounded size) collapse over ℤ by pigeonhole; they separate by completion: the bulk ℤ₂ is compact (position only; **aperiodicity generic** — nothing to preclude), the archimedean ray hosts momentum. A divergent integer is **position-typical, momentum-exceptional** (sub-critical ledger = large deviation): the bulk already precludes divergence *in measure* (Terras; Tao's log-density [T]); the pointwise residue is the conjecture.

**(A) ⟺ pointwise seam recurrence.** Recurrence of the ledger L_K = K ln3 − C_K ln2 to any bounded window + integrality + pigeonhole ⟹ cycle. Measure-recurrence: theorem. The seam is the **anchor** (recurrence set), not a barrier — 5x+1 owns the identical unoccupiable zero-ledger wall with permanent expansion-side residence; a barrier requires an orbit-uniform Lyapunov functional [O].

**Expansion cone, quantified.** Expansion-side steps are exactly c = 1 ⟺ **n ≡ 3 (mod 4)**; boundary-ward rapidity capped at ½ln(3/2); marker frequency p₁ > 2 − log₂3 = **0.41504** is necessary, not sufficient. Exhibit 27: p₁ = 0.585 lifetime, ledger peak +4.657 (×105) at step 32, terminal −3.477 — **crossable, marker-rich, uninhabitable** (mean c̄ = 70/41 ≈ 1.71 stays supercritical; retreats unbounded).

**Stream enslavement.** Over ℝ the sub-critical stream space is fully realized (skew product: real divergent orbits abound); over ℕ the stream is **enslaved to the origin** (the §2 bijection). (A) ⟺ Q(ℤ⁺) avoids the sub-critical limsup set, of 2-adic box dimension **H₂(1/log₂3) = 0.94996** (exact identity dim = H₂(1/β) via max-entropy geometric tilt; coset counting concurs, 0.9488 at K = 4000), thinning **0.0793 bits/step**.

**Algorithmic/statistical split.** Kolmogorov-type invariants are blind: every integer's stream is computable from n₀ — algorithmically trivial whether the orbit converges or diverges. The correct class is **one-sided empirical-frequency order** (normality species: same species as digit statistics of explicit constants, open in every known instance). (A) demands the pointwise form; Tao supplies the density form.

---

## 4. The sign channel [V/C]

The two mirror classes = the two ends; the separating character is odd on translations. Corpus template: the Fricke involution's ι-parity law and selection rule Wv_D = −χ_D(−N)·v_D (07-03, 376/376), with "**sign-forced stratum = Shannon redundancy** (involution-implied, zero new bits)." Under the grading, the s₋-end is the involution-implied partner of the s₊-end; the cycle inventories are precisely where implication fails: **(B) = the excess information of the mirror channel** — the bits by which the S-partner is *not* implied. Named computation [C]: the selection-rule hunt — twisted traces of the graded transfer operator L₀ + L₁σ against the faithful seam weighting (the jet/derivative-martingale partner, per 05-30's finding that holonomy dies in scalar reductions), asking whether the two ends are the two characters and whether any Fricke-type formula predicts mirror-class admissibility.

---

## 5. Transmission-functor reading [V/T/id]

**Bulk: Collatz is the unit-rate erasure channel, exactly.** The shortcut map T on ℤ₂ is everywhere 2-to-1 (the second preimage (2y−1)/3 always exists 2-adically), Haar-preserving, exact, conjugate to the full shift: each step transfers exactly one bit from state to transcript; H(state) + H(transcript) is conserved — the coding-theorem ledger shape. The accelerated symbol code is **Kraft-tight**: Σ 2^{−c} = 1 and H(c) = E[c] = 2 — a complete prefix code with **zero redundancy**. The 2:1 fold is something-preserving in the strongest sense: transfer, not loss.

**Integral restriction = port pruning.** Over ℤ the second port is live only at y ≡ 4 (mod 6); the decoder tree is {1,2}-branching with the ≡ 0 mod 3 rays as non-branching stalks (the §1 silent slots). Measured: live-second-port fraction ≈ **0.264**, tree growth ≈ **1.264**/level [V-empirical].

**Functorial names for the two cores.** (A) = the **pointwise converse source-coding theorem for the integrally-pruned source**: no integer message beats the perfect code by 0.0793 bits/step forever (the bulk converse is the AEP/density theorem; the pointwise integral converse is the conjecture). (B) = the **mirror-channel excess** of §4. The functor renames the difficulty in ledger units; it does not dissolve it — as the 06-28 orthogonality verdict predicts (bulk ⊥ boundary), transposed to this thread. The corpus's "Hecke-as-forgetting" open thread is the same door read from the tower side: T₂-forgetting interleaved with the M_z twist.

---

## 6. Failed predictions and corrections (two-ledger discipline)

- **Rough-path/Lévy-area proposal (turn 2): retired.** Wrong valence — an area-valued (K) instrument aimed at a horocyclic (N) object; the 06-28 Wilczek–Zee ↔ Lévy-area thread is the K-side program.
- **Levin/complexity conservation (turn 7): fails outright.** All integer streams are computable, hence algorithmically trivial; replaced by frequency-conservation (§3).
- **Controls over-reach (turn 3): corrected.** "Genericity precluded by 3x−1/5x+1" → the (A)/(B) factorization (Will's push); 3x−1 is 3x+1 on ℤ⁻, so the critical rule is one system with two ends, and (A) is a legitimate generic target.
- **Turn-5 algebra: adjudicated.** The Wick chain's final line misses its target by −((a+x)²+2x+1) (bracket slips); the clean identity is a(1−a)+x(1−x)+b(1−b)+(a+x)²+b² = a+x+b+2ax, with special locus (2a+1)(2x+1) = 1−2b — multiplicative closure in mirror-centered coordinates; unsatisfiable in the open unit cell (the locus lives on the Wick face). Alt-chain: single sign slip on b; (x+b) − ax² = −a(1+x)² at the locus is correct.
- **"Not covered by the reals" (turn 8): false over ℝ** (skew product realizes every stream); the non-coverage claim is ℕ-specific — the mechanism must consume enslavement, not seam geometry.

---

## 7. Verdict-to-date, success conditions, queue [O]

**Verdict-to-date: dictionary, not yet guide.** Contact is real and repeatedly corpus-slotted — privileged golden/silver points with u = 3−2√2 a recorded CM value; degree-1 Ritt shadow of the doubling faces; parabolic-seam residence; D_∞/mirror grading; unit-rate ledger — but at the **group-theoretic skeleton**, with the arithmetic flesh orthogonal, exactly matching the corpus's own Langlands verdict ("u (bulk) ⊥ Galois (boundary)"). Everything is conditional on the **forced-vs-chosen floor** (05-30/06-28): if x²+u=1 is elected rather than forced, passed checks degrade from generic₂ to rapidity bookkeeping.

**Falsifiable upgrade conditions (any one promotes dictionary → guide):**
(a) a cross-place inequality on the cocycle beyond product formula + Baker (effective ledger completeness);
(b) a twisted Cobham for ⟨σ₂, σ₃, M_z⟩-modules beyond Adamczewski–Bell/Schäfke–Singer;
(c) a budget-axiomatic derivation of κ = 1 and the excursion exponents in which the 3x−1/3x+1 mirror asymmetry is visible.

**Queued computations:** (i) the §4 selection-rule hunt; (ii) the certificate program — per-window 0.0793-bit thinning vs Baker seam-repulsion on the coset tree, control exponent Krasikov–Lagarias; (iii) the two-radix theta tower — classical AGM (budget θ₂⁴+θ₄⁴=θ₃⁴) × Borwein cubic AGM (budget a³=b³+c³), commuting substitutions q↦q², q↦q³, all coupling through M_q and the cyclotomic sieve. Also open: the x²(G) group-budget definition (search did not surface it; absence-caveat applies — pointer requested), and the D₄ assembly check (S-mirrors × the T⁴ = id rotation).

---

## 8. Session scripts and classical inputs

**Scripts (re-runnable):** collatz_semidirect.py (commutators, word decomposition, cycle equation); anholonomy_probe.py (2-adic reconstruction, Kesten criticality, 3x−1 cycles); family_scan.py (3x+d inventories, 5x+1, sign conjugacy); involution_frame.py (Klein diagonalization, exact identity + locus, mirror presentations); seam_recurrence.py (p*, dimension H₂(1/log₂3) two ways, c=1 marker, orbit-27 ledger); decoder_tree.py (pruned-tree branching 1.264, Kraft tightness).

**Classical inputs [T]:** Lagarias (2-adic conjugacy; periodicity conjecture); Terras; Tao (almost-all log-density); Baker / Steiner / Simons–de Weger (cycle exclusions); Furstenberg ×2×3; Rudolph–Johnson; Cobham; Adamczewski–Bell; Schäfke–Singer; Conway; Kurtz–Simon; Kesten; Kahane (critical cascades); Lagarias–Weiss (excursion statistics); Krasikov–Lagarias (density exponents); Borwein–Borwein (cubic AGM); Ritt–Julia.

---

## Appendix: consolidation entry (for the log)

**Context:** Nine-turn thread: Collatz ↔ TEP nested-budget analogy, from Will's g/s lattice through the anholonomy classification, mode structure, sign channel, and transmission-functor reading.

**Anchors:**
- [A1] The semidirect decomposition (independent scale ports ⋊ N-cocycle); all turn-1 algebra = the k=2 generator of g(km)=kg(m)+(k−1). | Evidence: symbolic verification. | Confidence: firm.
- [A2] (A)/(B) factorization; (A) = pointwise seam recurrence; (B) = mirror-class inventory. | Evidence: family scan, negation conjugacy, pigeonhole. | Confidence: firm.
- [A3] Anholonomy trichotomy; Collatz = the parabolic/seam member; K-channel structurally empty. | Evidence: 05-30 grounding + triangularity + strict AM–GM. | Confidence: firm.
- [A4] The mirror grading is load-bearing (a selection rule exists). | Evidence: Fricke template only. | Confidence: tentative — pending the twisted-sector computation.
- [A5] Verdict-to-date "dictionary, not guide," with three falsifiable upgrade conditions, conditional on the forced-vs-chosen floor. | Evidence: 06-28 orthogonality verdict + control tests. | Confidence: firm.

**Inflections:**
- [I1] turn-4: A2 | prior: controls preclude structural conclusions → new: controls *factorize* the conjecture | Axis: agreement + specificity | Trigger: Will's genericity push + family scan | σ: high.
- [I2] turn-6: (tool choice) | prior: rough-path lift proposed → new: retired, wrong valence | Axis: direction reversal | Trigger: 05-30 K-vs-N grounding | σ: high.
- [I3] turn-8: conservation slot | prior: Levin/complexity conservation → new: frequency conservation (normality species) | Axis: specificity/sharper | Trigger: computability of integer streams | σ: high.
- [I4] turn-8: A2 | prior: seam as possible barrier → new: seam as recurrence anchor only | Axis: strength/nuance | Trigger: 5x+1 control | σ: medium.
- [I5] turn-9: A4/A5 | prior: redundancy sought in the bulk code → new: bulk code is Kraft-perfect; redundancy lives in port pruning and mirror excess | Axis: specificity | Trigger: Will's 2:1-fold question + Kraft computation | σ: medium.

**Drift watch:** A5 moved from "open adjudication" (turn 3) toward "dictionary" through evidence-coupled inflections (corpus orthogonality verdict, control tests, valence corrections) — convergent, evidence-coupled, not accommodation-only.

**Open threads:** selection rule (A4); certificate exponent vs Krasikov–Lagarias; two-radix theta tower; x²(G) definition pointer; D₄ assembly check; Busemann/horocyclic join inheritance; Berg–Meinardus as the explicit σ-transfer fixed-point equation.

**Self-audit notes:** The framework predicted answers cleanly several times this session (seam, criticality, mirrors); each was audited against the controls per the 06-28 discipline, and the audit itself produced the strongest results (the factorization, the valence correction). The recurring failure mode to watch: reaching for a conservation principle one category too strong (Levin before frequency).
