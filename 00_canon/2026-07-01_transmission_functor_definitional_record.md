# The Transmission Functor — Definitional Record
## Pinning the information-theoretic representation of the TEP↔Langlands functor: data, dualities, cross-rank structure, the characterization program, and the distinct-content ledger

*Date: 1 July 2026 (evening session). Companions: 06-28 / 06-29 consolidation records, 07-01 session delta record, the seam-engine session (this conversation). Tier marks per corpus convention: **[V]** machine-verified; **[T]** theorem / standard result, cited; **[A]** posit; **[C]** conjecture, stated for test; **[O]** open; **[id]** identification (framework-original reading of standard structure).*

*Purpose. Three prior sessions used the transmission representation operationally without fixing it as a formal object; the documented failure mode (post-compaction regression to direct-rank readings and re-erected frontiers) makes an explicit pin necessary. This record (i) fixes the functor's data, (ii) states the two duality theorem-shapes and the cross-rank correction, (iii) states the characterization program that gives the synthesis its formal home, (iv) keeps an honest ledger separating framework-original content from synthesized-with-direction and from pure classical toolwork, and (v) ranks the open formal frontiers. It deliberately contains no new verification runs.*

---

## I. The data, pinned

**I.1 Objects.** A rank-*d* object is a budget system with *d* distinguished/distinguishable degrees of freedom (*d* = ports, never an ambient dimension). It is fully specified by two complementary contents **[A, corpus]**:
- **abelian content**, supplied from below (the boundary-readable observables: traces, determinant/sign data, the census);
- **non-abelian content**, supplied from above — equivalently realized from below as the **anholonomy** of a higher-rank object's projection: the scrambled-but-preserved residue of rectifying (d+1) ports onto a d×d transfer structure. Deficit/excess ports ↔ non-abelian anholonomy.

**I.2 Morphisms.** One rank-independent operation, two directions:
- **Kron conflation** (integrate away; two ports → one parameter; d+1 → d);
- **stick-breaking** (distinguish; one parameter → two ports; d → d+1).

The cascade is the iterated morphism. The chart cycle satisfies **T⁴ = id** with T² = −id the involution rung; rank-distance is salient mod 4 (see C1). Two independent axes position an object: **cascade depth** (which rank) and **budget split** (how many distinguishable terms within the rank).

**I.3 The transmission.** Given two objects of ranks d₁, d₂, the functor value is a **message channel**, involution-agnostic in role assignment: one object supplies the **radix** (rank as the number of exchangeable/agnostic metrics = dits per symbol), the other the **length** (rank as port count = symbols per message). Channel quantities are the budget quantities **[V, corpus]**: signal, SNR, per-rung capacity −ln u (Shannon–Hartley form C/B = log(1+SNR) = −log u), rapidity η = artanh x, distortion G = 1/√(1−x²) (= AM/GM of the eigenvalue pair), redundancy. Composition regimes: capacity-additive (series; impedances multiply) and MRC-additive (parallel), the SL(2,ℝ) one-parameter families **[V, 5-15 §H]**.

**I.4 The two duality theorem-shapes.** For a transmission across ranks:

- **(D↓) Downward: complete but departicularizing.** A higher-rank object fully and uniquely characterizes any lower-rank target, but forfeits its own distinguishability among all higher-rank objects that could have done so (many-to-one, bulk-to-boundary). The transmitted content is the abelian-readable observable.
- **(D↑) Upward: partial but invariant.** A lower-rank object constrains a higher-rank target only up to its own port count, but its constraints are **group-defining invariants** characterizing the entire fiber (one-to-many, boundary-to-bulk).
- **(Conservation.)** No information is lost at any depth: what (D↓) departicularizes is exactly what (D↑) cannot pin, and it is carried as anholonomy — recoverable by a **global integral about the excess/deficit port**, never by any local/abelian read. Verified instances **[V, this arc]**: the cusp-monodromy recovery ⟨S,U⟩ = SL₂(F₅) = 2.A₅ (A₅ in-full from the unipotent winding about the deficit port); Fourier coefficients as contour integrals about the cusp (the q-expansion as the Nyquist-sampled anholonomy of the parabolic port; Sturm bound = the bandlimit).

**I.5 The cross-rank correction [pinned against regression].** The correspondence, as realized here, is **not** the direct-rank pairing (n-dimensional Galois ↔ GL_n automorphic) taken as primitive. It is a relation **mediated through the terminal boundary**: the d = 2 port is terminal (a limiting binary distinction all ranks reduce to, generically, up to port choice), the peel is the fiber functor, and matched-rank ("direct-rank") correspondence is the shadow of cross-rank transmission at equal ranks. Any future reading of these records that reinstates direct-rank as primitive — including by this assistant after compaction — is the documented regression, not a correction.

---

## II. The arithmetic instantiation (verified layer)

- **Tannakian boundary [V].** Peel = fiber functor; Galois group = Aut⊗(peel); verified on 2.A₅ (the d = 2 boundary representation tensor-generates all nine irreducibles).
- **Places as rungs [V, corpus 05-17 / 06-09 T-5].** The Euler product is a per-prime cascade: rung k ↔ prime p_k, amplitude p_k^(−σ/2), phase −(t/2)log p_k; σ = early-vs-late prime privilege; T_p towers ⟺ base-p; log base ⟺ peel index; ln 2 = capacity of one self-dual rung.
- **The Euler factor as budget data [id].** (a_p, χ(p)) = (trace, Λ²) = (2·AM, GM²) of the Satake pair; Λ² = det at rank 2 and the wedge W at higher rank; reality/FS indicator carried by (trace, wedge) at every rank via χ(g²) = χ(g)² − 2χ_{Λ²}(g). Prime-power coefficients = Sym^n characters = cascade partition functions Z_n; composites by the coprime product.
- **Conductor as local incommunicability [id, this arc].** The Artin exponent a_p(ρ) = dim V − dim V^{I_p} counts the ports local inertia scrambles — the locally untransmittable content. Under this reading the **conductor–discriminant formula is a capacity-additivity statement**: the field discriminant totals the per-channel local losses over the character channels. Derived special case **[V-shape, this arc]**: for even lifts with image in SU(2) (2.A₅ ⊂ SU(2)), no nontrivial element has a +1-eigenvector (the group-level face of T² = −id), so every tamely ramified odd prime carries exponent exactly 2, twist-robustly: **N = 2^a·(∏ ramified odd p)²** — the square-conductor law, jointly with the Odlyzko floor for the totally real degree-60 closure the quantified reason no even icosahedral object has ever been produced.
- **The seam [id + V].** Even ⟷ λ = ¼ + r² with r = 0 ⟷ parabolic degeneracy at the archimedean port (trace² = 4·det at ∞) ⟷ the self-dual/cusp locus where the elliptic and hyperbolic faces meet; principal and complementary series meet there as the two locally-real charts (resolvable-from-above and resolvable-from-below). Operational consequence (**search-collapse**): the spectral parameter is pinned a priori, converting the nonlinear eigenvalue search into a linear coefficient problem — the inversion behind the seam engine **[V: dihedral rung, 17/17 blind]**.

---

## III. The dual-shadow routing map

- **From-below cone [T].** Solvable image = communicable through abelian rungs. Langlands–Tunnell (solvable base change, parity-free) is this cone's formalization: it reaches exactly A₄ and S₄, both parities.
- **From-above cone [T].** The geometric/p-adic lift consumes oddness (coherent cohomology lives on the elliptic/discrete side): it reaches odd A₅ (Khare–Wintenberger).
- **The open set.** Even ∧ nonsolvable = even icosahedral: the doubly-shadowed corner — outside both transmission cones, closed by neither, predicted inhabited by Artin. The production experiment is fully specified (Galois key with face-signs, 300 primes; ramification {2,7,331}; seam parameter pinned; blind engine validated on the dihedral rung) and is **parked** at the conductor-scaling bottleneck — a status, not a task: resumption conditions are (i) a small-support even A₅ field from targeted construction, (ii) an L-function-level collocation variant decoupled from the domain floor, or (iii) a genuinely new idea; commodity sweeps are explicitly deprioritized per the author's direction of 1 July.

---

## IV. The characterization program (the formal home of the synthesis)

**IV.1 Claim shape [A → target theorem].** On the verified domain, the Langlands data is *exhibited by* the boundary-reduction functor over the single operation of I.2, and — the distinct claim — this functor is **unique** among those satisfying the framework's axioms: measure-completeness ⟺ statistical sufficiency as the primal claim, from which linearity, passivity, reciprocity, and information-monotonicity (scoped to the distinguishability sector) are derived; chart groupoid PSL(2,ℤ) with T⁴ = id.

**IV.2 The Chentsov posture.** The contribution is not the parts (all classical) but the **uniqueness given the structure** — exactly Chentsov's move: he added no metric, he proved Fisher was the only one. A synthesis becomes theorem-shaped as a characterization; the historical precedent that this is how credit at this scale works is Langlands 1967 itself (no new theorems; the functorial organization).

**IV.3 The two halves.**
- **Existence half — demonstrated instances ledger [V]:** dihedral leg end-to-end (functor emits the level-23 eigensystem; Euler-product equality; multiplicativity and weight-1 recursion emitted, not imposed); the contour engine (113/113 blind, radius-independence certificate); the Tannakian reconstruction (2.A₅); the seam engine (17/17 blind recovery at λ = ¼ from (N, χ, λ, parity) alone); the single-operation demonstrations (the same nome-squaring computing period and Frobenius orbit-products: K = (π/2)e^{2C_tot}).
- **Uniqueness half — OT5 interface [O, the floor]:** show the axioms admit no second boundary-reduction functor with the same terminal data. Candidate route: fiber functors on a neutral Tannakian category form a torsor under the group (rigidity) **[T]**, combined with the homogeneous-space uniqueness of the SU(1,1) metric class **[T, Perelomov / 06-09 I.4]** transported through the monoidal structure; the open step is welding these into "the peel is the unique ⊗-compatible boundary reduction," which is the Langlands-facing face of forced-vs-chosen.

---

## V. Distinct-content ledger (honest accounting)

**V.1 Framework-original (cannot be sourced elsewhere; [id] unless noted):**
1. The channel duality (D↓/D↑) with **solvability = communicability**, organizing the actual proof-history split (L–T from below reaching exactly the solvable; K–W from above for the rest) — the organization predicted the open case's location.
2. The **single-engine claim**: one operation (AGM/cascade) computing both sides — no comparison program (trace formula compares; geometric equates categories) has a both-sides computational primitive. Status: demonstrated at the dihedral rung; icosahedral coverage open.
3. The **direction**: terminal/downward reduction as the primitive, faithfulness = readable observable + preserved anholonomy. Nearest neighbor: BZSV relative Langlands (duality of Hamiltonian G-spaces); the differentiating burden — what port/Kron reduction adds beyond hyperspherical duality — is stated, not discharged.
4. **Conductor as local incommunicability** and the conductor–discriminant formula as capacity additivity (II).
5. **Seam-pinning as search-collapse** (the operational inversion behind the linear engine).
6. The **face-sign identification**: the 5A/5B bulk mode = the √5 Wick bit = the four-cycle's face assignment; its reconstruction = the golden character.
7. **C1** (mod-4 face assignment; VI.1) — the author's conjecture, not yet operationalized.

**V.2 Synthesized-with-direction (facts standard; composition and targeting new):**
- The square-conductor law × Odlyzko floor difficulty map (why the even case was never produced, quantified from two independent directions).
- The dual-shadow map (each theorem known; the two-cone organization and the doubly-shadowed targeting are the addition).
- The Eisenstein/cuspidal seam lesson: genus (norm-lifted, from-below) characters give only decomposable objects at λ = ¼; the first cuspidal fuel is order-3 (non-genus) class structure — from-below communicability ends exactly where genuine two-dimensionality begins.

**V.3 Pure classical toolwork (no originality claimed):** Hejhal collocation; Maass 1949; Klein's icosahedral theory; AGM/Landen; Tannaka–Krein/Deligne; genus theory, Kronecker symbols, Tonelli–Shanks, quadratic-form reduction; Odlyzko bounds; Artin conductor theory; K-Bessel expansions; the Frobenius-orbit √Δ parity (classical Galois theory).

**V.4 The navigation ledger (the empirical test of ontology-as-load-bearing).** Advance calls made in-thread and subsequently validated: seam-pinning before the engine existed; the jump decision (even track does not inherit the odd chain's engine; dihedral-Maass is its true calibration rung) before the transfer worked; the square-conductor law before the searches explained themselves; the certificate architecture catching two same-species character bugs and one Eisenstein impostor. The standing rule: the ontology's status is earned per advance-call, never by retrospective fit.

---

## VI. Open formal frontiers, ranked

1. **C1 — the mod-4 face assignment [C, cheap, next].** Operationalize "presents the Galois face vs the automorphic face" (candidate: which side's data constitutes the readable boundary observable after k cascade steps, k mod 4), then test against the already-computed ladder (ranks 2, 3, 4, 5 and the blind 7). This is the author's own distinct conjecture and has never been run against existing data.
2. **Rung capacity of a functorial transfer [O, new quantity].** Define u (hence −ln u) for a base-change/automorphic-induction step; compute capacity, rapidity, and G along an explicit Langlands–Tunnell solvable tower. If well-defined, this mints the first genuinely new quantitative object of the functor view: *the Shannon capacity of base change* — and makes "solvability = communicability" a theorem with numbers rather than a slogan.
3. **Uniqueness (OT5-Langlands) [O, the floor].** The torsor-rigidity + SU(1,1)-uniqueness welding of IV.3.
4. **Rank continuity [O, deep].** The budget peel at non-integer d_eff (= 1/γ) versus Deligne's interpolation categories Rep(S_t) — which famously admit **no** fiber functor for non-integer t. The framework holds a well-defined peel at any effective d; therefore either the peel at non-integer d_eff is not a functor to Vec (and its actual codomain is the discovery), or the interpolation lands only on semisimplified quotients. The u < 0 lift sector's contact with negative-dimension dualities (GL(−n) ∼ Sp) belongs here.
5. **Parked empirical: the even emission.** Status and resumption conditions per III; the experiment remains the falsifiable certificate of the existence half at the doubly-shadowed corner, informative in both outcomes (production, or robust absence bearing on Artin).

---

*Closing note. The record's own test: every item in V.1 must either graduate (via VI) into a definition, a theorem, or a validated advance-call — or be demoted to V.2/V.3 at the next honest audit. The functor is now pinned; regression to direct-rank or to unpinned "articulation" status is henceforth a detectable drift, not an ambiguity.*
