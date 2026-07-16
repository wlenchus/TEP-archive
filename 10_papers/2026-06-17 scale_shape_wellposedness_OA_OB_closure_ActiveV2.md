# Well-Posedness of Perspective-Agnosticism over the Scale/Shape Partition

## A single-mechanism closure of O-A (fiber similarity) and O-B (shape automorphism)

*Date: 17 June 2026. A focused note establishing that two previously-open structural
claims about monotone (Petz) metrics under the spectral-rescaling peel — the fiber-side
**isometry-up-to-scale** (curvature operator and holonomy preservation; the
scale-shape document's O-A, the kinetic-cascade record's O-5) and the shape-side
**family automorphism** (O-B) — are both consequences of a single elementary fact: the
degree −1 homogeneity of the Morozova–Chentsov weight. The note states the propositions
with proofs, records the machine verifications, scopes the result to the generic
(distinct-spectrum) stratum, and isolates what genuinely remains open.*

*Tier convention (corpus): **[V]** verified to machine precision this session; **[T]**
standard or elementary, immediate; **[M]** argument given, full formalization pending;
**[O]** open. The two propositions sit at the [T]/[M] boundary — the arguments are
complete modulo standard facts of homogeneous Riemannian geometry that a journal write-up
would cite precisely; the load-bearing algebraic and geometric steps are verified [V].*

*This note is deliberately narrow: it concerns the mathematics of monotone metric spaces
under the peel. The framework-level reading (perspective-agnosticism) appears only in §6,
clearly demarcated, and is a **consequence of** — not a premise for — the mathematics.*

---

## 1. Setup and notation

Let `ρ` be a faithful density operator on a `d`-dimensional Hilbert space with spectrum
`λ = (λ₁ ≥ … ≥ λ_d > 0)`, `Σλᵢ = 1`, and **distinct** eigenvalues (the generic stratum;
see §7). The manifold of density operators factors locally as

```
   (eigenvalue simplex Δ_{d-1})  ×  (flag fiber  M = U(d)/T,  T = U(1)^d ).
```

The **monotone (Petz) metrics** are the Riemannian metrics contracted under
CPTP/Markov morphisms. By Petz's classification they form a family indexed by
operator-monotone functions `f` with `f(1)=1`, `f(t)=t f(1/t)`; the **Morozova–Chentsov
weight** is

```
   c_f(a,b) = 1 / ( b · f(a/b) ).
```

In flag (eigenbasis-rotation) coordinates `θ_{ij}` the off-diagonal mode `(i,j)` carries
`dρ_{ij} = (λᵢ − λⱼ) dθ_{ij}`, so the fiber metric at fixed spectrum is

```
   g_λ  =  Σ_{i<j}  w_f(λ)_{ij} · |dθ_{ij}|²,     w_f(λ)_{ij} = (λᵢ − λⱼ)² · c_f(λᵢ, λⱼ).
```

`g_λ` is a **U(d)-invariant** metric on the flag `M = U(d)/T`: it is determined by one
positive weight `w_f(λ)_{ij}` per complex root space `m_{ij}` (the off-diagonal `(i,j)`
modes), with distinct root spaces `g_λ`-orthogonal. The reductive complement of
`t = Lie(T)` in `u(d)` is `m = ⊕_{i<j} m_{ij}`, the tangent space at the base point.

**The peel.** Remove the dominant eigenvalue and renormalize the remainder:

```
   P(λ) = (λ₂, …, λ_d) / u,     u := Σ_{i≥2} λᵢ = 1 − λ₁ ∈ (0,1).
```

On the fiber `P` sheds the dominant-attached modes `m_{1j}` and acts on the **residual
sub-flag** `M′ = U(d−1)/T′` (`T′ = U(1)^{d−1}` on indices `2..d`), embedded in `M` through
the base point with tangent

```
   m′ = ⊕_{2 ≤ i < j ≤ d} m_{ij}    (residual modes),
   m′^⊥ = ⊕_{j ≥ 2} m_{1j}          (shed, dominant-attached modes).
```

**The peel is post-selection, not a CPTP coarse-graining.** `P` conditions on *not* being
the dominant outcome — `Φ(ρ) = Π ρ Π / Tr(Π ρ Π)` with `Π` the residual projector — which
is **not** trace-preserving, so the data-processing inequality (monotone metrics contract
under CPTP maps) does **not** apply to it. Acting on tangent vectors, `Φ` annihilates the
shed modes (`Π X Π = 0`) and **inflates** each residual mode by `1/u`: `Φ_*X = X/u`, whence
`g_f(Φρ)(Φ_*X, Φ_*X) = (1/u)·g_f(ρ)(X,X)` **[V]** (verified to machine precision, all `f`,
all spectra). The scalar `u = 1 − λ₁ = Σ_{i≥2}λᵢ` is exactly the post-selection probability
`P(not-dominant)`, so the per-rung inflation is `1/u = G² = 1 + SNR` — the corpus's depth
scalar and the post-selection probability are the same number. The "isometry-up-to-scale"
and `f ↦ f` statements below are **algebraic facts about the restriction-renormalization**,
consistent with this post-selection inflation; they are *not* a data-processing contraction
and must not be read as one.

**The scale/shape partition.** Along the peel the geometry separates into a **scale axis**
(the depth scalar `u`; the closure quantity `∏ uₙ`) and a **shape axis** (the metric label
`f`). The two open completions this note closes are:

- **O-A / O-5** (scale side, fiber): *the peel is an isometry-up-to-scale of the residual
  fiber, hence preserves the curvature operator and holonomy exactly, for all `f`, all
  `d`, all loops.* (Verified at `d = 4,5,6` and five loop families; general proof flagged
  open as "essentially the homogeneity argument, not yet a proposition.")
- **O-B** (shape side, family): *the peel is a bijection of the entire operator-monotone
  family onto itself.* (Verified on six representatives; the general statement over the
  infinite-dimensional family flagged as "the natural completion (open).")

---

## 2. The single mechanism: weight homogeneity  [T / V]

> **Lemma (homogeneity).** For every operator-monotone `f`, the weight `c_f` is
> homogeneous of degree −1 and `w_f` of degree +1 in the spectrum:
> `c_f(σa, σb) = σ^{-1} c_f(a,b)` and `w_f(σλ)_{ij} = σ · w_f(λ)_{ij}` for all `σ > 0`.

*Proof.* `c_f(σa, σb) = 1/(σb · f(σa/σb)) = 1/(σb · f(a/b)) = σ^{-1} c_f(a,b)`, using only
`f(σa/σb) = f(a/b)`. Then `w_f(σλ)_{ij} = (σλᵢ − σλⱼ)² c_f(σλᵢ, σλⱼ)
= σ²(λᵢ−λⱼ)² · σ^{-1}c_f(λᵢ,λⱼ) = σ · w_f(λ)_{ij}`. ∎

This is the only non-trivial input. Both propositions below are corollaries of it, taken
with `σ = 1/u` (the peel's renormalization). **[V]** confirmed symbolically for a fully
symbolic `f` (`w_f(a,b) − u·w_f(a/u, b/u) = 0`), i.e. for the whole family at once.

---

## 3. Proposition A — fiber isometry-up-to-scale (closes O-A / O-5)

> **Proposition A.** On the generic stratum, the peel `P`, acting on the fiber, equals
> a constant homothety by `u` composed with restriction to a totally-geodesic submanifold.
> Consequently `P` preserves the Levi-Civita connection, the `(1,3)` curvature operator
> entrywise, and the holonomy of the residual fiber exactly (all loops), and scales the
> sectional curvature by `u`; and this holds for **every** operator-monotone `f` and every
> `d`.

The peel on the fiber factors as `P = (homothety by u) ∘ (restriction to M′)`. We treat
the two factors.

**Lemma A1 (homothety).** By the Lemma with `σ = 1/u`,

```
   w_f(λ)_{ij} = u · w_f(λ/u)_{ij}     for all residual (i,j),
```

so the d-flag metric **restricted to the residual modes** equals `u` times the intrinsic
`(d−1)`-flag metric — a *constant* (fiber-independent: `u = 1−λ₁` depends only on the
spectrum) rescaling. **[T]** A constant homothety `g ↦ c·g` has identical Christoffel
symbols `Γ^k_{ij} = ½ g^{kl}(∂_i g_{jl} + ∂_j g_{il} − ∂_l g_{ij})` (each `g` carries `c`,
each `g^{-1}` carries `c^{-1}`), hence the same connection `∇`, the same parallel transport
and holonomy, and the same `(1,3)` curvature `R^k_{lij}`; sectional curvature `K`, with one
factor of `c` upstairs and two in the area form, scales by `1/c`. With `c = 1/u` this gives
`K_{(d−1)} = u · K_d|_{residual}`. **[V]** verified symbolically (`Γ` identical,
`K(cg)·c = K(g)`).

**Lemma A2 (totally geodesic).** *The residual sub-flag `M′` is totally geodesic in `M`,
for any positive weights.*

*Proof.* It suffices that the second fundamental form `II(X,Y) = (∇_X Y)^⊥` vanishes for
`X, Y ∈ m′`. For a `G`-invariant metric on `G/H`, on Killing fields generated by `m`,

```
   ∇_X Y = ½ [X,Y]_m + U(X,Y),     2⟨U(X,Y), Z⟩ = ⟨[Z,X]_m, Y⟩ + ⟨X, [Z,Y]_m⟩  ∀Z.
```

Using matrix units `[E_{ab}, E_{cd}] = δ_{bc} E_{ad} − δ_{da} E_{cb}`:

- For `X,Y ∈ m′` (indices in `{2..d}`), `[X,Y]` has indices in `{2..d}`, so `[X,Y]_m ∈ m′`
  — no `m′^⊥` component; thus `½[X,Y]_m ∈ m′`.
- For `Z ∈ m′^⊥` a `(1,k)` mode and `X ∈ m′` an `(i,j)` mode (`i,j ≥ 2`):
  `[E_{1k}, E_{ij}] = δ_{ki} E_{1j} − δ_{j1} E_{ik} = δ_{ki} E_{1j}` (since `j ≥ 2`), a
  `(1,j)` mode `∈ m′^⊥`. So `[Z,X]_m ∈ m′^⊥`, and by root-space orthogonality
  `⟨[Z,X]_m, Y⟩ = 0` for `Y ∈ m′`; likewise `⟨X, [Z,Y]_m⟩ = 0`. Hence `⟨U(X,Y), Z⟩ = 0`
  for all `Z ∈ m′^⊥`.

Therefore `⟨∇_X Y, Z⟩ = 0` for all `Z ∈ m′^⊥`, i.e. `II(X,Y) = 0`. The argument uses only
the bracket structure of `u(d)` and root-space orthogonality — **independent of the weights
`w_f`**. ∎ **[V]** `II = 0` confirmed at `d = 3, 4, 5` (the relevant pairings vanish to
machine zero).

**Combination.** A totally-geodesic submanifold inherits the ambient connection on its
tangent distribution (the ambient `∇` preserves `m′`), so restricted parallel transport
**is** the intrinsic parallel transport, and the intrinsic curvature equals the ambient
sectional curvature on residual planes (Gauss equation with `II = 0`). Composing with the
constant homothety (Lemma A1), the connection is preserved through both steps; hence the
curvature operator is preserved entrywise and holonomy is preserved for **all** loops (it
is determined by the connection, not sampled), with sectional curvature scaling by `u`.
This is the general statement O-A/O-5 requested, reducing it to the Lemma plus the
elementary bracket structure. **Scope:** fiber-side and generic-stratum (§7). ∎

**Why the sub-flag, and not a submersion (the model is not optional).** The peel could be
modelled two ways on the fiber: as restriction to the sub-flag `M′` (the slice holding the
dominant eigenvector fixed), or as a Riemannian submersion `M → M′` quotienting the shed
directions. The distinction matters, because a submersion carries O'Neill integrability
tensors that can *change* holonomy (`K_base = K_total + ¾|[·,·]^V|²`). The sub-flag model is
the correct one here for a specific reason: the object O-A compares is the *(d−1)-system's
own fiber holonomy*, computed on loops in *its* fiber — which **is** `M′`. For loops lying
in `M′`, the totally-geodesic embedding (Lemma A2) gives intrinsic = ambient-restricted
holonomy with no O'Neill term; the submersion's integrability tensor would contribute only
when comparing holonomy of `M`-loops that *project* to `M′`, which is not the comparison
O-A makes. The ρ-dependence of the projector `Π` (the dominant eigenvector rotates as one
moves in the fiber) is not an obstruction but the same fact from the other side: the
directions that rotate `Π` are exactly the shed modes `m′^⊥`, which the peel annihilates —
they are the orthogonal fiber of the projection, never traversed by an `M′`-loop. So the
sub-flag reading is forced by what is being measured, not chosen for convenience.

---

## 4. Proposition B — shape-side family automorphism (closes O-B)

> **Proposition B.** The peel induces the identity on the operator-monotone label:
> it carries the `f`-metric to the `f`-metric of the renormalized system (up to the scale
> `u`), for **every** `f`. The induced map on the Petz family is therefore a bijection
> onto itself — injective and invertible (the label is recoverable), surjective trivially.

**Lemma B1 (label preservation).** By the Lemma with `σ = 1/u`, the residual block of the
`d`-system's `f`-metric equals `u ·` the `(d−1)`-system's `f`-metric — *same* `f`. So the
peel acts on the family as `f ↦ f`, for every operator-monotone `f`. (The scale-shape
document's extreme-point fact — SLD ↦ SLD, maximal ↦ maximal — is this lemma specialized;
it holds for every member, not only the extremes.) **[V]** symbolic, arbitrary `f`.

**Lemma B2 (recovery).** Evaluating the weight at the eigenvalue pair of ratio `t`
(`a = t, b = 1`): `w_f(t,1) = (t−1)²/f(t)`, so

```
   f(t) = (t − 1)² / w_f(t,1).
```

Across all spectra the residual realizes every ratio `t`, so the **entire** function `f` is
recovered from the `(d−1)`-metric. Hence `f ↦ f` is injective and invertible; surjective is
immediate (any target `(d−1)` `f`-metric is the peel of the `d`-system's `f`-metric). The
induced map is a bijection of the whole family. **[V]** algebraic.

**Why sampling at one spectrum is insufficient (and why B1–B2 are the proof, not the
six-representative check).** A spectrum of size `d−1` samples `f` at only `(d−1 choose 2)`
ratios; finitely many point-values cannot determine an infinite-dimensional family. Two
distinct operator-monotone functions agreeing at exactly those ratios would collapse the
single-spectrum *shape* yet remain separated by `f ↦ f` across spectra (Lemma B2). The
recorded shape-distance check (`≈ 0.72` over six representatives at one spectrum) is thus a
sufficient sanity check that the tested members do not collapse; the bijection over the
**whole** family is secured by the structural label-preservation, which is the completion
O-B named as open.

**The `d = 2` terminus (shape → scale migration).** At the bottom rung the residual is
`d = 2`: the flag is `U(2)/U(1)² = CP¹` with a single root space, so the shape carries
`(2 choose 2) − 1 = 0` degrees of freedom and the normalized shape is `[1]` for every `f`.
The label does not vanish — it sits in the single weight's spectral dependence
`w_f(λ₁,λ₂) = (λ₁−λ₂)²/(λ₂ f(λ₁/λ₂))`, from which `f` is still recovered (Lemma B2). So
`f ↦ f` remains injective at the terminus, but via **scale** rather than shape. This is
exactly the multiplicity-first reading: the `d = 2` fiber has unique *shape* (the Chentsov
terminus of the shape axis), so family-distinctness can only live in scale there. ∎

---

## 5. One mechanism, both halves

Propositions A and B are the same fact read on the two axes. The degree −1 homogeneity of
`w_f` (§2) makes the peel's renormalization act **simultaneously** as:

- a *uniform constant homothety* on the fiber metric (scale side) — which, composed with
  the totally-geodesic restriction, preserves connection / curvature operator / holonomy
  (Prop A); and
- the *identity on the metric label* `f` (shape side) — which, with pointwise recovery,
  is a bijection of the Petz family (Prop B).

The corpus's "one principle, four levels" (homogeneity propagating through metric,
sectional curvature, holonomy, and the non-abelian curvature operator) extends to: **one
principle closes the entire scale/shape well-posedness** — both the scale-side fiber
similarity and the shape-side family automorphism. The orthogonal-and-commuting structure
of the two axes (peel preserves shape; `f` is independent of the depth scalar `u`; the two
moves commute) then has both of its halves established.

---

## 6. Consequence: well-posedness of perspective-agnosticism over scale/shape

*(Framework-level reading. Demarcated as a consequence; not used above.)*

"Perspective-agnosticism" — the claim that the framework's admissible relabelings and
reparametrizations are a gauge group preserving the collinear/orthogonal (scale/shape)
partition — is well-posed precisely to the extent that the gauge moves act by automorphisms
of that partition. The substantive content of that requirement is exactly Propositions A
and B: the scale move (peel) preserves the shape structure (Prop A's geometry **and** Prop
B's label), while a shape move (change of `f`) cannot disturb the scale tower (`u = 1−λ₁` is
`f`-independent), and the two commute. The remaining gauge moves of the framework
(the `x²↔u` binary relabeling, the cascade-family `sl(2,ℝ)` basis change, a global unit
rescaling) are intra-axis by construction. Hence, over the scale/shape partition,
perspective-agnosticism is theorem-grade pending formal write-up, resting on the lone
homogeneity fact.

This is established **for this partition specifically**. The framework groups several
dualities under one heading (scale/shape, series/parallel, derivative/integral,
intrinsic/extrinsic, bulk/boundary); whether these are one nucleating structure or parallel
instances of the *type* (collinear/orthogonal relative to a nucleated axis) is a separate
question (§7). In particular the four-cycle's Wick orthogonality (boost ↔ compact phase)
acts on the `d = 2` budget where the shape axis is empty, so it is a **distinct**
orthogonality from scale/shape; well-posedness is a per-partition obligation, and only
scale/shape is discharged here.

---

## 7. Scope, caveats, and the open frontier

**Scope of the closure.**
- *Fiber-side.* O-A/O-5 and the holonomy content are the non-abelian (Petz) fiber. The
  static tower (Fisher–Rao on the eigenvalue simplex) is the separate abelian/Chentsov
  content and carries no fiber holonomy; the two couple only under the §6 *deformation*
  (frame-dragging), which is not addressed here.
- *Generic stratum.* The arguments assume distinct eigenvalues, where the flag is smooth.
  At spectral coincidences the weights `w_f = (λᵢ−λⱼ)² c_f` vanish and the flag degenerates
  — a measure-zero locus and a known feature (the towers terminate at `d ≤ 2`). The clean
  statement is "on the distinct-spectrum stratum."

**Caveats.**
- *Shared-mechanism fragility.* Both propositions rest on the **same** homogeneity Lemma.
  This is why they are not ad hoc — but also why a single subtle error in that Lemma would
  touch both. A formal write-up should concentrate its rigor there (and on the two standard
  homogeneous-geometry facts invoked: that `g_λ` is `U(d)`-invariant on the flag, and the
  invariant-connection / totally-geodesic criterion).
- *`d = 2` terminus.* Prop B's bijection persists at the terminus only via scale, not shape
  (§4); the shape-based detector is silent there by design.

**What this does not touch (genuinely open).**
- **O-6** — whether the curvature operator's rank-2 signature is *forced*, and whether it is
  the same rank-2 structure as the purity wedge, the saturating bivector, and the DHO
  boost-pair (a possible unification one level up). The totally-geodesic argument is a
  statement about fiber geometry and says nothing about the rank of the curvature operator.
- **O-7** — whether the `1/G²`-per-rung similarity is *physically instantiated* (a conjugate
  pair flow realizing it) versus structurally shared. The recurring instantiation question;
  untouched.
- **The consolidation question** — whether the framework's several dualities are one
  nucleating structure or parallel instances of the collinear/orthogonal type (§6). The
  `d = 2` Wick-orthogonality-vs-scale/shape distinction shows at least two are distinct.

---

## 8. Verification record (reproducible)

All checks this session in `sympy`/`numpy`. Reproducible from the formulas above.

1. **Homogeneity / label preservation [V].** For symbolic `f`, `w_f(a,b) − u·w_f(a/u, b/u)
   = 0` (Lemma; Lemma B1). Confirms `c_f` degree −1 across SLD, Kubo–Mori, maximal,
   Wigner–Yanase explicitly, and for arbitrary `f` symbolically.
2. **Recovery [V].** `w_f(t,1) = (t−1)²/f(t)`, so `f(t) = (t−1)²/w_f(t,1)` (Lemma B2).
3. **Totally geodesic [V].** At `d = 3,4,5`: `max|⟨[res,res]_m, shed⟩| = 0` and
   `max|⟨[shed,res]_m, res⟩| = 0`, so `II = 0` for all weights (Lemma A2).
4. **Homothety curvature [V].** For a generic 2D metric, `g ↦ c·g` leaves the Christoffel
   symbols invariant and gives `K(cg)·c = K(g)` (Lemma A1).
5. **Injectivity sample [V, corpus].** Residual normalized-weight shapes for six
   representatives at `d = 5 → 4` are pairwise separated (`≈ 0.72`) — a finite shadow of
   §4, superseded by the structural bijection.
6. **Post-selection inflation [V].** For a residual mode `X`, `Φ_*X = X/u` and
   `g_f(Φρ)(Φ_*X,Φ_*X)/g_f(ρ)(X,X) = 1/u` exactly (all `f`, all spectra; `d = 3`); shed
   modes are annihilated (`g_after = 0`). Confirms the peel is post-selection (metric
   inflates by `1/u = G²`), not a data-processing contraction (§1).

---

*End of note. Two open completions (O-A/O-5 fiber similarity; O-B family automorphism)
reduced to one elementary fact — the degree −1 homogeneity of the Petz weight — with the
load-bearing steps machine-verified, the scope held to the generic fiber stratum, and the
rank-2 (O-6), instantiation (O-7), and duality-consolidation questions left explicitly
open. Endorsement weighting: the arguments were developed in adversarial review and should
be read as proof sketches at the proposition level awaiting a formally written, fully cited
version; the algebra and the totally-geodesic vanishing are verified, the surrounding
homogeneous-geometry facts are standard but stated here without citation.*
