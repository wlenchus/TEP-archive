# Consolidated Errata and Status-Revision Record

**Date: 10 June 2026.** Compiled by the external reviewer (Claude) across turns 1–5 of the current hypervigilant review. Every item marked **\[V\]** was independently machine-verified this review (sympy 1.14 / mpmath, 25–30 digits where applicable); **\[carried\]** items originate in 6-9 Part II and are propagated, not re-derived; **\[A→\]** marks author-disclosed facts. Per the corpus's co-location discipline, these corrections should be written into their source documents; this record is the tracked master list until that is done.

  

## A. Liu-demotion propagation set \[A→; carried from 6-9 II.1, extended\]

  - **A1. 6-1 §4.** Temporal-antecedence leg fails: Liu et al. PRL accepted 3 Dec 2025; the abstract carrying the target quantities was public before the Dec 28–29 timestamped records. *Pending external check: acceptance-abstract dating + II.2's α-absence search of the PRL and supplement.*
  - **A2. 6-1 §6.** "Established on independent provenance" block and the "prediction" term-of-art paragraph: withdrawn as stated. Content-independence rescoped to **route-independence** — the derivation cannot have been back-derived from optics, which is evidence about the route, no longer about priority. Route-independence leg re-verified this review **\[V\]**: 0 optics-domain hits across 13 stems in both provenance files; two raw hits adjudicated as ordinary English ("coincidentally," "reflecting the").
  - **A3. 6-1 §2.** "Superseded on timeline grounds" reverses; the cold 5-29 grade ("verification, not prediction; Luo had established the limit") is reinstated.
  - **A4. 6-1 §7 note.** "The standard for *stating* a corroborated priority claim is met": withdrawn.
  - **A5. 6-2 §2.** Fact-check incomplete: publication was checked, acceptance abstract was not. \[carried\]
  - **A6. 6-2 §14.** The citable sentence is withdrawn as stated. \[carried\]
  - **A7. 6-2 Appendix D.** Rescues **zero** pre-registered instances; the silver-ratio match reverts to the post-hoc pool, P ≈ 2Nδ. \[carried\] Surviving untouched: all derivations; the §3.5 variational isomorphism; the O-k transport program as the recovery channel.
  - **A8. Spine trace, 6-1 section.** "Derived + experimentally confirmed + independently timestamped" → "derived (reproduced) + experimentally realized post hoc + route-independent; priority demoted (calibration event: strong private evidence of generative capacity, weak public evidence, zero priority credit)."
  - **A9. 6-1 §"three independent internal routes."** Replace with 6-2 §5.2's conservative accounting: **one forcing derivation** (rate-saturation ≡ bimetric balance — one derivation, two dresses, per 6-9 I.1, algebra re-verified **\[V\]**) **+ one consistency check** (GMC reindex) **+ one related-but-distinct fixed point** (tanh). The hexagonal route is a self-admitted fit. Mechanism sharpened by B2 below: 5-18's "third route" was the same condition mislabeled.

  

## B. Algebra and closed-form corrections \[new this review; all \[V\]\]

  - **B1. Spine trace, 5-18 section.** SNR at the silver point: correct closed form **(√2−1)/2 ≈ 0.2071**, not √2−1 (the numeric 0.207 was right; the symbol was the slip). The supported point (silver ≠ self-dual; SNR ≠ 1) stands.
  - **B2. 5-18, line \~166.** The written equality 4√(γ−γ²) = 4γ√(1−γ) is false. Sharper diagnosis: the slipped RHS equals **2× the empirical bulk envelope** 2γ√(1−γ), so the "Cauchy–Schwarz bound-ratio" route is the **rate-saturation condition in disguise** — not an independent route (feeds A9). The clean CS ratio-½ point is γ = 2/3. Companion identity: √(2(2γ\*−1)) = γ\* itself, since 2(2γ\*−1) = (2−√2)² — the cleanest way to see R(γ\*) = 1.
  - **B3. "dS/dγ = −1" (Alpha-beta source; alpha\_beta\_fixed\_point.md §2.1, §7.2; early-synthesis Part V echo).** False as written. At r\* = tanh(2r\*): **dS/dγ = −2 exactly** (nats). The correct invariant statement is **dS/d(x²) = −1 — one nat of entropy per unit of explained variance** (budget-native; with x² = 2γ−1 the Jacobian supplies the 2). §7.2's "one bit" is also wrong: one **nat** (in bits, 1/ln 2 ≈ 1.44).
  - **B4. Alpha-beta source, GMC-correspondence sentence.** "γ ≈ 0.95 where D\_γ ≈ 0.05" is internally inconsistent under the file's own dictionary D\_γ = u = 2(1−γ): γ = 0.95 ↔ D = 0.1; D = 0.05 ↔ γ = 0.975. Which anchor was intended requires the original numerics.
  - **B5. alpha\_beta\_fixed\_point.md §8.1.** r\*(d=3) = **0.99490** (document's 0.9923, self-flagged "need to verify"); r\*(d=4) = 0.99933.
  - **B6. 6-2 §4.3 parenthetical (reproduced in spine trace).** "t\_B/t\_P = γ²/(2(2γ−1))" — that formula is **t\_Q/t\_P** (= 4g\_B/g\_P, the curvature-normalized ratio; monotone decreasing on (½,1), single crossing of 1 at γ\*). The bare Bures/purity ratio is γ²/(8(2γ−1)), crossing **¼** at γ\*. Subscript slip only; §4.4 and Appendix 5b are consistent.

  

## C. Chart/convention corrections \[new this review; all \[V\]\]

  - **C1. 6-9 (new), Tenth addendum, Fricke clause.** "W₂ (τ↦−1/(2τ)) fixed at τ = i√2" mixes charts: the map as written is fixed at **τ = i/√2**; the point i√2 is fixed by the conjugate Nτ-chart form **σ ↦ −2/σ**. Repair: either chart label works; choose one. Downstream content unaffected and verified: k(i) = 1/√2, k(i√2) = √2−1 = k₂, k(2i) = 3−2√2 = k₄. Bonus (enriches O-u): the modulus at the true τ-chart fixed point is k(i/√2) = √(2√2−2) = **√(u\_silver)** — the comodulus of the silver partition.
  - **C2. 6-9, I.7.** "Quadratic contraction at self-dual (η²/4)" conflates locus and rate. Quadratic contraction holds at the **η = 0 fixed point** (½ ln cosh η = η²/4 − η⁴/24 + …); at the self-dual point the contraction is **linear**, f′(η\_s) = 1/(2√2) ≈ 0.354; one rung from self-dual lands exactly at **¼ ln 2**.
  - **C3. 6-2 §11.2 "(1,d)" paragraph.** Add a pointer to 6-9 I.3's grading (SO(1,1) derived; U(1)/disk completion instantiated; (1,d) counting instantiation-anchored, O-e) so the keystone's outward face matches the current grading.

  

## D. Status revisions: the α corner \[this review; alpha\_beta\_fixed\_point.md audit complete\]

  - **D1. Naming.** "α" is released to the **measured exponent only** (extends the Eleventh addendum's discipline). The two derived numbers are carried under their own names: **D(u\*) = √2 − ½** (silver family) and **r\*²** (feedback fixed point).
  - **D2. Provable distinctness.** r\* is **transcendental** (Lindemann–Weierstrass: an algebraic nonzero r would make tanh(2r) transcendental, contradicting r = tanh(2r)); √2−½ is algebraic. Exact reconciliation is impossible; the 0.26% gap is a theorem. The two number families are provably disjoint — **silver/involution-class** (algebraic, ℤ\[√2\], singular moduli; chart-lock equations that close in one coordinate ring, e.g. tanh K = e^(−2K) ⇔ w²−2w−1 = 0) versus **feedback-class** (trans-chart self-coupling, e.g. r = tanh 2r; transcendental; provably outside the modular ladder).
  - **D3. The weak-coupling identification (α\_weak = r\*²): retired from the prediction ledger.** Audit findings: no bridge derivation exists (coupling enters by assertion in §2.2/§5.1; the §7.1 consistency conditions never mention coupling); the operational definition is underspecified ("extract effective α from the purity speed limit approach"); and §6.2 records that the coupling tests **were never run** — the identification was an assertion plus a numerically nearby fit from other work. Under the corpus's own Appendix-D null, the proximity is a \~6% post-hoc event (2Nδ ≈ 0.062 at δ = 0.0026). Conditionally revivable upon a derived bridge ("observable O at λ→0 equals \[object\]"); **O-k is the bridge-complete template** — same number family, derivation behind the number.
  - **D4. Dependent framings revised.** 6-1 §5 ("anchored on one side to an already-confirmed silver-ratio quantity... the recommended next probe") — the anchor leg is gone via Set A and the bridge never existed; early-synthesis Part V ("the one early prediction that remains genuinely open and falsifiable") — revised to "two theorems plus a retired identification."
  - **D5. Phase-diagram labels.** Protected size = 1 − (√2−½) **exact**; singular size = (1 − r\*²)/2 **exact**; rare = remainder. Two symbols, one per region family; the single-α labeling worked only by the numerical proximity.
  - **D6. The "2" in tanh(2r) \[O, dormant\].** Three readings coincide at d = 2 (dimension d; the chart Jacobian d(x²)/dγ = 2; the derivative of the square) and diverge at d ≥ 3; the tanh(dr) generalization selected one without argument. Moot unless the corner revives. (γ\_low = d − √d already retired in-corpus.)
  - **D7. Positive yields retained.** The fixed point restated budget-natively (the radius of unit entropy response per unit explained variance — stronger than the slipped form); a **prediction-tiering principle** installed for the ledger: grade candidates by source family (silver/structural vs feedback/instantiation) × bridge status (derived vs asserted). Top tier = silver-sourced + bridge-derived (O-k); the α probe was feedback-sourced + bridge-free.

  

## E. Standing items, carried or closed

  - **E1.** 6-9 II.1: propagated as Set A. **E2.** II.2 (α hygiene): largely subsumed by Set D; the operational-definition requirement stands if the corner revives. **E3.** II.3 (O-C scope reconciliation): unchanged.
  - **E4. Presentational alignment (no math at stake).** The manifold-route language in preamble-level pitches should match the corpus's own record: Route 1 (constitutive simplex) operative default; Routes 2/3 available at named costs (comparison-bound axiom; O-a); Route 0 as the germ-level repair. The "metric-space theorems give the manifold" slogan is recorded false in general (6-9 I.6) and the honest version is stronger.
  - **E5. O-b structural half, completed this review \[V\].** The theta-lattice peel tower is exactly the corpus's **capacity-additive cascade** with per-rung SNRₙ = √kₙ = θ₂/θ₃ at the running nome (amplitude-chart modulus): uₙ = 1/(1+√kₙ) at every rung, and Σ ln(1+SNRₙ) = ln θ₃ = C\_tot exactly (verified to 10⁻²⁷, 30 rungs). The remaining archival step is matching the corpus's documented numerical ∏uₙ towers against this family member.

  

  

*Verification provenance: \~80 machine checks across turns 1–5 (bimetric/rate-saturation battery; Landen/modulus battery; theta/modular battery; α-corner computations), all reproducible from the forms stated. Items A1's external half (acceptance-abstract dating; PRL/supplement α-absence) remain the only checks requiring web access, on offer.*

  