# The Scale–Shape Decomposition of Monotone Metric Spaces under Spectral Rescaling

## A focused statement of the defensible mathematical core

*A standalone foundational document. It states, with verifications and explicit open ends, a single structural result about the geometry of monotone (Petz) metrics on the space of density operators: under a spectral-rescaling operation ("the peel"), the geometry factorizes into a scale axis and a shape axis that are orthogonal and commuting, the peel acts as an automorphism of the full monotone-metric family preserving the complete curved non-abelian fiber geometry up to a single scalar, and the natural foundational orientation is multiplicity-first (the Petz family is primary; Chentsov uniqueness is its low-dimensional degenerate limit).*

  

*This document is deliberately narrow. It is* ***not*** *a comprehensive statement of the broader research program (the TEP / Entrodynamics framework) from which it emerged. It excludes — by design, and names as out of scope — the program's physical interpretations (self-dual points, horizon identities, frame-dragging-as-gravitation), which are suggestive but whose realization depends on an open question stated in §7. What remains here is intended to be true at the level of the mathematics of monotone metric spaces as such, independent of any physical reading.*

  

*This is not "V3." It does not succeed the program's Central Reference; it is a different kind of object — a focused result that a comprehensive reference would be built around.*

  

*Notation and tier convention: claims are marked* ***\[V\]*** *verified to machine precision (method in the methods supplement),* ***\[M\]*** *established by a clear mechanism/argument short of a fully general proof, or* ***\[O\]*** *open. d denotes the dimension of the Hilbert space; the eigenvalue simplex is the (d−1)-simplex of spectra; the fiber is the flag manifold U(d)/U(1)^d of eigenbases at fixed spectrum.*

  

## 1\. The object and the operation

Let ρ be a density operator on a d-dimensional Hilbert space, with spectrum λ = (λ₁ ≥ λ₂ ≥ … ≥ λ\_d), Σλᵢ = 1. The **monotone (Petz) metrics** on the manifold of density operators are the Riemannian metrics contracted under completely-positive trace-preserving maps (quantum Markov morphisms). Petz's classification: they form a one-parameter family indexed by operator-monotone functions f with f(1)=1, f(t)=t f(1/t); the metric weight on the (i,j) eigen-plane is

  

w\_f(λ)\_{ij} = (λᵢ − λⱼ)² · c\_f(λᵢ,λⱼ),  c\_f(a,b) = 1/(b f(a/b)),

  

diagonal in the off-diagonal mode basis. The extreme members are the SLD/Bures metric (c\_f = 2/(a+b), the minimal element) and the maximal metric (c\_f = (a+b)/2ab).

  

**The peel.** Define the operation P on the spectrum that removes the dominant eigenvalue and renormalizes the remainder:

  

P(λ) = (λ₂, λ₃, …, λ\_d) / u,  u := Σ\_{i≥2} λᵢ = 1 − λ₁.

  

P maps a d-dimensional spectrum to a (d−1)-dimensional one. Iterating P generates a finite tower of height d−1, terminating at d = 2 (a single eigenvalue-pair) and then d = 1 (the pure state). The scalar u ∈ (0,1) at each step is the residual mass; the program from which this work arises reads u = 1/G² for a "budget" factor G, and the closure quantity is the cumulative product ∏ₙ uₙ. Nothing below depends on that reading; u is simply the renormalization scalar.

  

**Why P is natural.** P is the conditional-probability coarse-graining "condition on not being the dominant outcome," restricted to the spectrum. It is a Markov morphism on the simplex, so by Petz–Sudár it carries monotone metrics to monotone metrics — but this document's results are about *how* it does so (bijectively, geometrically, with a clean factorization), which the data-processing inequality alone does not give.

  

## 2\. The central structural fact: weights split into ratio (shape) and scale (depth) \[V\]

The single algebraic observation underlying everything below:

  

**In the Petz weight w\_f(λ)\_{ij} = (λᵢ−λⱼ)² / (λⱼ f(λᵢ/λⱼ)), the metric label f enters only through the ratio λᵢ/λⱼ, and the ratio is invariant under the peel's uniform rescaling λ → λ/u.**

  

Consequently the weight separates into two parts that the peel treats independently:

  

  - a **scale** part — the factors (λᵢ−λⱼ)² and 1/λⱼ, which carry the u-rescaling (net 1/u on the residual block); this is the *depth* the peel moves along; ratio-invariant.
  - a **shape** part — the factor f(λᵢ/λⱼ), a function of the scale-invariant ratios; this is the *metric label*; untouched by the peel.

  

**\[V\]** Verified that every Petz weight is degree-1 homogeneous in λ (so the residual block rescales by exactly u), across the SLD, Kubo–Mori, Wigner–Yanase, and maximal metrics — because operator-monotone f makes c\_f degree −1, a defining property of the family. This is not a Bures accident; it is forced by the structure that makes the monotone metrics a family.

  

This split is the spine of the document. The two axes are developed in §3 (shape: the automorphism) and §4 (scale: the geometric tower), shown orthogonal and commuting in §5, deformed in §6, and oriented foundationally in §7.

  

## 3\. The shape axis: the peel is an automorphism of the monotone family \[V\]

**Theorem-form claim \[V, on six representatives; M for the full family\].** The peel acts as a **bijection of the Petz family onto itself** — an automorphism, not merely a monotonicity-preserving map.

  

The metric *label* is encoded in the *shape* of the residual weights (their ratios, the scale-invariant part of §2). Three properties, verified:

  

  - **Injective \[V\]:** six genuinely-different operator-monotone metrics (SLD, maximal, Kubo–Mori, Wigner–Yanase, and two Wigner–Yanase–Dyson-α metrics, including Kubo–Mori which is not a finite mixture of the extremes) give *distinct* residual shapes (minimum pairwise shape distance bounded away from zero; ≈0.72 for a representative spectrum). The label survives the peel; no collapse.
  - **Invertible \[V\]:** the residual shape is strictly monotone in the family parameter, so the label is recoverable from the peeled metric.
  - **Extreme-point-preserving \[V, exact/structural\]:** the SLD metric peels to the SLD metric of the residual spectrum, and the maximal metric to the maximal, by the scale-covariance of their weight formulas — exact at all d. A bijection of a convex set that fixes its extreme points and is injective on the interior maps the set faithfully onto itself.

  

This is strictly stronger than "the peel preserves monotonicity" (which Petz–Sudár / data-processing already gives, and which permits collapse). The automorphism rules out collapse: the peel is a faithful self-map of the space of monotone metrics.

  

**\[O\]** A fully general proof over the entire infinite-dimensional operator-monotone family (beyond the six representatives) is open; the mechanism (label = peel-invariant shape) is general and suggests it holds.

  

## 4\. The scale axis: the peel is a geometric similarity of the fiber \[V\]

On the flag-manifold fiber (eigenbases at fixed spectrum), the peel sheds the dominant- attached modes and acts on the residual fiber. The result:

  

**The peel acts on the residual fiber as a pure geometric similarity by the scalar u: every dimensionful quantity scales by its appropriate power of u, while every dimensionless (shape) quantity — curvature operator, holonomy — is preserved.**

  

Verified, level by level, across the SLD/Kubo–Mori/Wigner–Yanase/maximal metrics:

  

  - **Metric weights \[V\]:** residual weights rescale by exactly u (degree-1, §2). Tested d = 3..6.
  - **Sectional curvature \[V\]:** the Bures sectional curvature K = −(b−a)/(ac) — a genuine geometric object with a product denominator that does *not* trivially rescale — scales by exactly u (covariant, degree-1). This survived an adversarial check designed to detect a trivial cancellation; the curvature genuinely transforms.
  - **Gauss–Bonnet holonomy \[V\]:** the geodesic-triangle angle deficit ∫K dA — a global integral, *not* scale-invariant on a curved space, so a genuine test — is **invariant** (the dimensionful deficit scales as u³ but the holonomy angle itself is preserved).
  - **Full non-abelian Riemann curvature \[V\]:** built faithfully via the Nomizu formula from the actual Bures metric (with the metric-adjoint computed from the metric, not hand-placed), the curvature operator R(X,Y) on the residual mode-frame is preserved **entrywise — an identity, not a frame rotation** (residual 1e-16, d = 4,5,6, multiple loop families including non-index-sharing ones). The connection was confirmed non-flat (120/216 nonzero curvature components at d=4) so the test could fail; it did not.

  

**The mechanism (the unifying cause) \[V/M\].** All four levels follow from the *single* homogeneity of §2: degree-1 weights → degree-0 (ratio-built) connection coefficients → degree-0 curvature operator (hence invariant, the identity result) and degree-1 scalar curvature (hence covariant ∼ u). The four results are **not four independent facts**; they are one homogeneity principle propagating through four levels of geometric structure. The honest weight of the evidence is therefore "one principle, verified to propagate," not "four miracles."

  

**Tower \[V\].** Iterating, a d-level fiber is a finite ladder of height d−1, each rung a similarity by its own uₙ, terminating at d ≤ 2 where the fiber vanishes. The residual fiber after one peel is *geometrically identical* to a (d−1)-level fiber up to the scaling by u — curvature, holonomy, and non-abelian structure included.

  

**Caution recorded (the d=3 trap) \[V\].** Rank/dimension claims about this fiber must be tested at d ≥ 4: at d = 3 the tangent space is 3-dimensional and several quantities coincide with their generic-maximal values, producing false confirmations. (Concretely: the generic curvature operator R(X,Y) is rank 2 at d=3 but rank 6, 10 at d=4, 5 — so a "rank-2 curvature" reading is a d=3 artifact, not a structural feature. The genuine rank-2 structures elsewhere — saturating bivectors of speed limits — are independently established and are not claimed here.)

  

## 5\. The two axes are orthogonal and commuting \[V\]

The shape axis (§3) and the scale axis (§4) are not merely distinct; they are orthogonal and they commute.

  

  - **Commuting \[V, exact\].** Because the metric label enters only through the ratios (scale-invariant) and the peel acts only on the scale (ratio-invariant), changing the metric and peeling act on complementary, non-overlapping parts of the weight. (Peel-then- relabel) = (relabel-then-peel), verified to 1e-15 across all metrics and spectra; the underlying reason is the algebraic separation of §2, not a numerical coincidence.
  - **Orthogonal \[V, with a caveat\].** On the eigenvalue simplex under the Fisher–Rao metric, the *boost* direction (increase the dominant, decrease the rest proportionally — a pure scale move preserving ratios) is orthogonal to the *shape* directions (rearrange the minority at fixed dominant — changing ratios): the Fisher–Rao cross-term vanishes to 1e-15, across random spectra and all shape directions.

  

**Caveat, recorded precisely \[V\].** The shape directions are *minority-rearrangement at fixed dominant*, which is **not exactly iso-purity**: purity changes along them (d(purity)/d(direction) ≈ 0.24, not 0). So the verified statement is *boost ⊥ minority- rearrangement*; the appealing identification "scale = SNR/capacity-changing, shape = iso- purity" is a good intuition but iso-purity (the fixed-γ surface) and the exact orthogonal complement of the boost coincide only approximately. The orthogonality result does not require, and should not be stated as, exact iso-purity orthogonality.

  

**Summary of the decomposition.** A density operator's geometry, relative to the monotone- metric family, decomposes as:

  

(boundary: the spectral data, metric-independent) × (scale axis: depth/u, the peel-similarity, ratio-invariant) × (shape axis: the metric label, the peel-automorphism, scale-invariant),

  

with the two non-boundary axes orthogonal and commuting.

  

## 6\. The deformation: a frame-dragging regime off the orthogonal limit \[V\]

The orthogonal/commuting structure of §5 is the *undeformed* limit. There is a one- parameter deformation of the peel — mixing a shape-rotation of strength t into the scale move — under which the two axes couple:

  

  - **A scale–shape cross-term linear in t \[V\]:** the Fisher–Rao inner product between the deformed scale direction and an independent shape direction is 0 at t=0 and grows linearly (−5.556 t for a representative spectrum) — an off-diagonal metric coefficient appearing in proportion to the deformation.
  - **Rung non-commutativity O(t) \[V\]:** the deformed peels fail to commute (the path- ordering commutator is 0 at t=0 and grows linearly).

  

Both turn on together and linearly in t — the structural signature of a rotating (frame-dragging) metric, where a single rotation parameter simultaneously sources the off-diagonal cross-term and the non-commutativity of the would-be-orthogonal directions. The undeformed peel (t=0) is the static/associative/orthogonal limit; t≠0 is the frame-dragging regime.

  

**\[V, structural / O, physical\]** The correspondence to the structure of a rotating metric (off-diagonal cross-term + non-commutativity, both linear in a rotation parameter) is verified as mathematics. Whether this *is* gravitational frame-dragging of a physical system — rather than sharing its structure — is part of the open question of §7 and is not claimed.

  

## 7\. Foundational orientation, and the open questions

**Orientation: multiplicity-first \[M\].** The standard orientation treats Chentsov's uniqueness theorem (and its quantum extension) as foundational, with the Petz multiplicity as the awkward failure of uniqueness in the quantum case. The structure here suggests the reverse is more natural:

  

The **shape axis — the Petz family, the multiplicity** — is the primary object (nontrivial for d ≥ 3: the shape degrees of freedom are 0 at d=2, 2 at d=3, 5 at d=4). **Chentsov uniqueness is the d ≤ 2 degenerate limit** of this axis, where the shape degrees of freedom vanish (one eigen-plane, no ratio to vary, hence a unique metric) — the *terminus* of the peel-tower, not its foundation.

  

Under this orientation, multiplicity is the content and uniqueness is its low-dimensional collapse — which removes the apparent tension between "Fisher–Rao is unique" (classical / d≤2) and "monotone metrics are many" (quantum / d≥3): they are the boundary and interior of one structure.

  

**The price, which is the central open question \[O\].** Multiplicity-first foundations make the **metric-selection problem fundamental rather than derived.** Uniqueness-first foundations answer "which metric?" for you (uniqueness selects it). Multiplicity-first does not: for d ≥ 3, *which* monotone metric is the physically- or operationally-correct one is **not fixed by the structure** — it is an external input. This is the genuine open frontier, and it is sharpened, not created, by the orientation: the framework's open content lives at the selection question, not at a boundary where the mathematics runs out.

  

**The open questions, stated for the record:**

  

  - **\[O-A\] (the general theorem).** Promote the §4 mechanism to a stated proposition with hypotheses and proof: *for any monotone metric, the spectral-rescaling peel is an isometry-up-to-scale of the residual fiber, hence its curvature operator and holonomy are invariant* — because the monotone-metric connection is scale-invariant (degree-0). The computation strongly indicates this and supplies the mechanism (degree-counting); the general (all-d, all-loop, all-f) proof is open.
  - **\[O-B\] (the full-family automorphism).** Extend §3's bijection from six representatives to the entire operator-monotone family.
  - **\[O-C\] (metric selection).** The central open problem above: what selects the physical monotone metric at d ≥ 3.
  - **\[O-D\] (the deformation's fixed-point structure).** The two-parameter deformation of §6 (the scale axis carries a fixed point at the ℤ₂-swap-symmetric spectrum; the shape axis terminates at Chentsov): does the *joint* deformed structure have a "rotating" fixed point or limit cycle — a stationary-but-not-static configuration, the analog of an ergosphere — where the frame-dragging coupling balances the scale flow? Unexamined.

  

## 8\. What this document does and does not claim

**Claims (the defensible core):**

  

  - The Petz weight separates into scale (ratio-invariant) and shape (scale-invariant) parts; the peel acts on them independently \[V\].
  - The peel is an automorphism (bijection) of the monotone-metric family \[V on six representatives; O in full generality\].
  - The peel is a geometric similarity of the fiber by the scalar u, preserving the full curved non-abelian geometry (curvature operator entrywise, holonomy) and rescaling the metric — driven by one homogeneity principle propagating through four levels \[V\].
  - The scale and shape axes are orthogonal and commuting \[V\], with the iso-purity caveat of §5.
  - A one-parameter deformation produces a frame-dragging regime (linear cross-term + non-commutativity) \[V as structure\].
  - Multiplicity-first is the natural foundational orientation; Chentsov is the d≤2 terminus \[M\]; and this makes metric-selection the fundamental open problem \[O\].

  

**Explicitly NOT claimed here (out of scope by design):**

  

  - Any physical interpretation of u, the scale axis, or the frame-dragging deformation as the dynamics of a specific physical system (the instantiation / selection question, O-C).
  - The program's self-dual-point, horizon, and anomaly claims — these belong to the broader framework and are not part of this core; some are established-as-standard, some contested, and they are documented and tiered elsewhere.
  - Novelty beyond "stated this cleanly": the ingredients (Petz classification, Nomizu curvature, Riccati/sl(2,R), Kubo–Ando) are standard. The contribution is the *decomposition* — the scale/shape factorization, the peel-as-automorphism, the similarity-of-the-fiber, and the multiplicity-first orientation — assembled into one structure. To the author's and reviewer's knowledge this assembly is not stated this cleanly in the standard information-geometry literature; that is a claim about the literature, made without certainty, and is itself checkable.

  

**The honest one-sentence summary.** Under spectral rescaling, the geometry of monotone metric spaces factorizes into a scale axis (along which the rescaling acts as a curvature- and-holonomy-preserving similarity and a finite tower) and a shape axis (the metric label, along which the rescaling acts as a faithful automorphism of the Petz family), the two orthogonal and commuting in the static limit and frame-dragging-coupled off it, with Chentsov uniqueness the low-dimensional collapse of the shape axis — and the one thing this structure does not fix, the selection of the physical metric at d ≥ 3, is exactly where its open content lies.

  

  

*End. A focused statement of the defensible core, with verifications marked, mechanisms distinguished from proofs, the periphery named as out of scope, and the open questions — chiefly metric-selection (O-C) — kept prominent. Reproduction methods for every \[V\] claim are in the methods and reproducibility supplement. This document is intended to stand on its own and to be the spine around which a comprehensive reference is later built; it is deliberately not that reference, and deliberately not versioned as one.*

  