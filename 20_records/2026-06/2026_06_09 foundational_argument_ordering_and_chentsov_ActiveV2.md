# The Foundational Argument: Ordering, Object, and the Role of Chentsov

## Why the axioms are applied to the metric space (not a metric or a system), in what order, what is actually assumed, and what Chentsov is actually for

*A companion to the focused core (`scale_shape_decomposition_focused_core.md`). Where the
core states the verified structural result, this note reconstructs the **foundational
argument** beneath it: the logical chain by which a passive space acquires a uniquely-forced
metric, with attention to two things that are easy to state loosely — the **object** the
axioms act on, and the **order** in which they apply. It marks each step as theorem or
assumption, isolates the single load-bearing posit, and resolves the apparent tension
between "Chentsov is the anchor" (it appears early and pins everything) and "Chentsov is the
terminus" (the Petz-first reorientation). Those are two different jobs, and seeing both is
what makes the foundation coherent.*

*This is a foundations note, not a comprehensive reference. Tier marks: **[T]** theorem /
standard result, **[A]** assumption / posit, **[V]** verified in this work, **[O]** open.*

*Date: 29 May 2026.*

---

## 1. The object: the axioms are applied to the *space*, so the metric is an output

The first and most consequential choice is *what the axioms are about*. Three candidates,
and only one makes the structure non-arbitrary:

- **A system** — a specific physical object with specific dynamics. Too narrow; not
  invariant; the conclusions would be facts about that system, not about structure.
- **A metric** — a specific distance function on the states. This *presupposes* the metric
  and begs the question: the framework's content is supposed to be that the metric is
  *forced*, which one cannot show by assuming it.
- **A metric space** — the ensemble of accessible measures / microstates, equipped with
  *whatever* metric structure is compatible with the axioms. **This is the right object**,
  because the axioms then *determine* the metric (via the uniqueness theorem of §3) rather
  than presupposing it.

So the object is the **space of accessible measures**, and the metric is an **output, not an
input**. This is the whole reason the argument routes through Chentsov: you axiomatize the
space (a passive, hence bounded, hence invariant ensemble), and uniqueness *hands you* the
metric. Calling the object a "metric space" rather than "a metric" or "a system" is not
stylistic — it is what lets the metric be a consequence. The framework characterizes the
*space of microstates*; the geometry falls out forced.

---

## 2. The order: a logical dependency, with one assumed link

The axioms apply in a specific order because **each step is a precondition for the next** —
the ordering is a genuine logical dependency, not a presentational choice. The chain:

**(1) Passivity** *(the operational axiom on the space).* The space is passive: no energy
generation, contractive or lossless, never active.

**(2) Passivity ⟺ boundedness** *([T], the passivity–positive-real–Herglotz correspondence).*
A passive space is exactly a bounded (contractive) one. This is the rigorous content of
"passive," standard in network/scattering theory — a theorem, not an assumption. *Passivity
of a space is tantamount to boundedness.*

**(3) Boundedness → invariance of the ensemble** *([T], with a precise reading).* A
bounded/contractive space maps its ensemble of accessible measures into itself: nothing
escapes, nothing is created or destroyed. The microstate ensemble is therefore **closed and
conserved — a genuine probability simplex.** This is exactly where the budget enters: the
identity **x² + u = 1 is the boundedness/normalization condition written as a partition of
unity** (signal-fraction + noise-fraction, conserved). Steps (1)→(2)→(3) are the chain that
turns "the space of microstates" into a *well-defined statistical manifold* — an invariant
distribution space.

**(4) The invariant ensemble admits a sufficient statistic** *([A] — the single load-bearing
assumption).* Chentsov's theorem requires the Markov-morphism / congruent-embedding
structure — the sufficient-statistic structure — on the manifold. The framework **posits**
that the invariant ensemble carries it; this is *not* derived from (1)–(3). This is the V2
"Q3: axioms assumed, not derived" concern, located precisely. And it is where the *genericity
is purchased*: in the strict Chentsov sense, the sufficient-statistic structure delimits to
the one-parameter/binary case on the commutative base (the MSS ⟺ one-parameter scope result).
Everything downstream is rigorous *given* (4); **(4) itself is the open posit.**

**(5) Chentsov uniqueness** *([T], given (4)).* Now the rigidity fires: a Riemannian metric
on a statistical manifold invariant under sufficient statistics is **uniquely Fisher–Rao**
(up to scale). This is the identification step — and *why* it is invoked is the subtle point
of §3.

**(6) Extensions: Petz and Campbell** *([T], extending Chentsov in two directions).* Anchored
to Fisher–Rao on the commutative, normalized base, the structure extends:
- **Petz** relaxes *commutativity* (the quantum / density-matrix case) → the one-parameter
  monotone family.
- **Campbell** relaxes *normalization* (the positive cone over the simplex) → a two-parameter
  family (Fisher–Rao plus a radial/total-mass term).

**The ordering is necessary, not decorative:** one cannot invoke Chentsov (5) before the
space qualifies as a statistical manifold (1)–(4); one cannot extend (6) before anchoring
(5). The dependency `passivity → bounded → invariant → [sufficient-statistic] → Chentsov →
extensions` is forced. And exactly one link in it — (4) — is an assumption rather than a
theorem. The argument is rigorous *given* (4); (4) is where the foundation rests on a posit.

---

## 3. The primitive conditions and their dependencies (what is actually assumed)

A natural audit: do we need to separately assert **linearity, reciprocity, or
positive-realness** — and are any of these (passivity included) *derived* or *presupposed*
by a finite-dimensional monotone metric space? The answer collapses most of the list, and
the surviving distinctions are the substance. Each condition is marked **constitutive**
(built into the object), **derived** (a theorem from other conditions), **assumed** (a
posit), or **optional** (neither presupposed nor derived).

**Positivity — constitutive.** The measures are non-negative; this is what it means to be a
measure / density operator. Not asserted; definitional.

**Passivity ≡ boundedness ≡ positive-realness ≡ normalization — one equivalence class,
*derived*, not four independent axioms.** Given positivity, these are the same statement in
different languages: *normalization* (the budget x²+u=1, trace 1) is conservation of total
probability; *passivity* (energy non-generation) is contractivity; *boundedness* is the
analytic form of contractivity; *positive-realness* is the immittance-function encoding for
the LTI representation. The bridge is a theorem: **a positive, trace-preserving map is a
contraction** (stochastic maps contract the total-variation / trace norm; the simplex is
invariant). So passivity and normalization are *equivalent given positivity* — each derives
the other. §2 took passivity as axiom and derived normalization; one could equally take
normalization as primitive and derive passivity. **You assert one member of the class (or
read it off the object being a space of density measures); the rest follow.**
**Positive-realness is never asserted separately — it is the LTI-analytic name for
passivity, which is already derived.**

**Linearity — three distinct senses, three different answers.**
- *Linearity of an underlying physical system* (the scattering operator is a matrix):
  **not needed and not the subject.** The axioms act on the *measure space*, not a system.
  Never asserted.
- *Morphism-linearity* (the relevant transformations respect convex mixtures — they are
  stochastic maps / Markov morphisms): **constitutive of "monotone metric space," and the
  content of step (4).** "Monotone" *means* "contracts under stochastic maps," so positing a
  monotone metric space *is* positing the convex-linear stochastic-map structure. It is not
  a separate axiom; it is built into the object. Its *applicability to a given situation* —
  whether a real ensemble carries this structure rather than nonlinear / mean-field measure
  dynamics — is exactly the step-(4) posit.
- *Temporal Markovianity* (memorylessness of the multi-step process): **not loaded** (the
  Markovianity axis of the appendix; orthogonal to the cascade's associativity axis).

The crucial non-collision: morphism-linearity (one stochastic map respecting mixtures) is
**not** temporal Markovianity (a memoryless multi-step process). The framework presupposes
the first constitutively and bears no load on the second.

**Reciprocity — optional; neither presupposed nor derived.** A monotone metric is monotone
under *all* stochastic maps, reciprocal or not, so reciprocity (S = Sᵀ, the
time-reversal/reversibility symmetry) is a constraint on the *dynamics*, not on the *metric
space* — **orthogonal to the metric structure.** Imposing it lands one at a reversibility
locus (aligned with the Markovianity/detailed-balance axis of the appendix; the *exact*
identification with the detailed-balance point is flagged **[O]**, not asserted — what is
solid is the orthogonality to the metric, not a precise locus). The framework is strictly
*more general* without it. (Direct evidence it is not load-bearing and is even a trap: the
addendum's Hodge-under-reciprocity claim invoked S = Sᵀ to zero a signed flow, which proved
vacuous-by-zero.) Reciprocity is the one item on the audit list that is genuinely
independent of the foundation.

**Finite-discontinuity — definitional.** "Finitely discontinuous" = finite dimension ⟹ a
finite cascade tower (height d−1) and finitely many degeneracy / dimensional-transition
loci. This is what makes the tower *terminate* (at d≤2) and the discontinuities finite.

**The dependency picture, and why the list splits the way it does.** Notice that *passivity/
normalization* and *commutativity* are exactly the two **base-defining constraints whose
relaxations are the two axes** (§6): relax normalization → Campbell → scale axis; relax
commutativity → Petz → shape axis; Chentsov is the doubly-constrained (passive *and*
commutative) base. So passivity is not merely presupposed — it *defines the base, and its
relaxation is the scale axis.* Morphism-linearity is the constitutive structure one cannot
relax without leaving the statistical-manifold setting entirely (into nonlinear / mean-field
territory). And reciprocity is a *different kind of object* — not a base-defining constraint
at all, but an optional symmetry locus. That is the clean statement of the audit:
**positive-realness is passivity (derived); system-linearity is unneeded while
morphism-linearity is constitutive (and is step 4); reciprocity is an optional symmetry
orthogonal to the structure; and passivity/normalization and commutativity are the two
constraints whose relaxations generate the two axes.**

---

## 4. What Chentsov is *for*: rigidity, not the statistical toolbox

This is the heart of the matter, and it is easy to misstate. The **standard** use of
Chentsov in information geometry is *instrumental*: Fisher–Rao is canonical, therefore one
may deploy Cramér–Rao, estimation theory, the statistical apparatus. **The framework does
not use Chentsov this way.** It invokes Chentsov for **rigidity / uniqueness** — to make the
metric *forced rather than chosen*.

The logical role of (5) is: *once the space qualifies as a statistical manifold (steps
1–4), you do not get to pick the metric; it is uniquely Fisher–Rao.* That rigidity is what
makes the entire structure **non-arbitrary**. The framework is not *doing statistics* with
Fisher–Rao; it is using Fisher–Rao's *uniqueness* as the constraint that forbids
arbitrariness on the base. In a phrase: **the use of Chentsov is defensive, not productive** —
it does not extract machinery from Fisher–Rao; it uses Fisher–Rao's uniqueness to *forbid
the metric from being a free choice.*

Stated as the identification it performs: *identifying a generic metric on a Riemannian
manifold of measures — given (assumed) a valid sufficient statistic — uniquely with
Fisher–Rao, and thereby qualifying the base for the Petz and Campbell extensions.* The
sufficient-statistic premise (step 4) is the door; Chentsov's uniqueness is what is behind
it; and the extensions are what the uniquely-anchored base supports.

---

## 5. Anchor vs. terminus: reconciling the ordering with the Petz-first reorientation

There is an apparent tension. The ordering of §2 makes Chentsov appear **early and
load-bearing** — the rigidity that pins everything. But the foundational reorientation (bulk
record §5.2) calls Chentsov the **terminus** — the d≤2 collapse of the shape axis, *not* the
cornerstone. Both are correct; they are **two different jobs**, and seeing both is what makes
the foundation coherent:

- **Logically (the ordering), Chentsov is the ANCHOR.** It is the rigidity that pins the
  base so that the Petz/Campbell extensions extend from a *uniquely-determined* metric rather
  than a free-floating one. Without the anchor, the extensions would have nothing definite to
  be extensions *of*.
- **Geometrically (the decomposition), Chentsov is the TERMINUS.** It is the d≤2 collapse of
  the shape axis, where the metric multiplicity vanishes (shape degrees of freedom: 0 at d=2,
  2 at d=3, 5 at d=4) and uniqueness reappears.

These cohere because **the ordering earns uniqueness *only at the base / d≤2*, and the
extension to d≥3 is exactly where uniqueness fails and multiplicity enters.** The argument's
own structure therefore tells you: uniqueness is a base/terminus phenomenon; multiplicity
(the Petz extension) is the content; and the **metric-selection question** (the focused
core's O-C) is precisely the statement that *the anchor pins the base but does not pin the
fiber* — Chentsov's uniqueness at d≤2 does not propagate to a unique choice at d≥3. So the
Petz-first reorientation is not in tension with Chentsov-as-anchor; it *falls out of* the
foundational argument: Chentsov anchors the base and is the terminus of the tower, while the
shape axis (the extension) carries the content and the open selection question.

---

## 6. The two extensions are the two axes [V — structural]

Organizing the argument exposes a clean alignment that was implicit. Chentsov's two classical
extensions map **exactly onto the two axes** of the decomposition (focused core §4–5):

- **Campbell** (relax normalization; the positive cone) ↔ the **scale axis** (the peel's
  u-rescaling, the depth/radial direction).
- **Petz** (relax commutativity; density matrices) ↔ the **shape axis** (the fiber, the
  metric label).
- **Chentsov** (normalized *and* commutative; the fixed-mass simplex base) ↔ their
  **common intersection** — the unique-Fisher–Rao base from which both axes extend.

This is structural, not analogical, and is verified: **[V]** Campbell's *extra* parameter
beyond Chentsov is the radial / total-mass direction, which is orthogonal to the simplex
(shape) directions under the Fisher-type cone metric (to 1e-16, by construction — the radial
$p_i$ contracted with $1/(m\,p_i)$ against any sum-zero vector vanishes). And the peel's scale
move *is* that radial direction: multiplying the residual block by $1/u$ is a pure total-mass
rescaling that fixes the residual's simplex shape — Campbell's radial direction exactly. So:

> The two directions in which Chentsov can be extended — relaxing normalization (Campbell,
> radial) and relaxing commutativity (Petz, fiber) — **are** the scale and shape axes of the
> decomposition, and Chentsov sits at their intersection as the uniquely-forced common base.

The scale ⊥ shape orthogonality of the focused core (§5) is then the *same* orthogonality as
Campbell's radial ⊥ simplex split — the decomposition's two axes are the two independent ways
the base extends, and they are orthogonal because relaxing normalization and relaxing
commutativity are independent relaxations. This is the cleanest available statement of why
the decomposition has exactly two axes: **there are exactly two independent constraints to
relax (normalization, commutativity), Chentsov is the doubly-constrained base, and the two
relaxations are the two orthogonal axes.**

---

## 7. Summary, and the honest status

**The foundational argument, in one chain:**

> A *passive* space is *bounded* [T]; a bounded space has an *invariant, conserved
> ensemble* of accessible measures — a probability simplex, the budget x²+u=1 as its
> normalization [T]; this invariant ensemble is *assumed* to carry a sufficient-statistic
> structure [A — the one load-bearing posit, Q3, which delimits the strict case to binary on
> the base]; given which, Chentsov forces the metric *uniquely* to Fisher–Rao [T] — invoked
> for **rigidity** (to forbid arbitrariness), not for the statistical toolbox; and the
> uniquely-anchored base extends in exactly two independent directions — Campbell (radial /
> normalization → the scale axis) and Petz (fiber / commutativity → the shape axis) [T, V] —
> which are the two orthogonal axes of the decomposition, with Chentsov at their intersection.

**The object** is the *space of measures* (so the metric is forced, not posited). **The
order** is a necessary logical dependency. **Chentsov's role** is rigidity/anchoring. **The
one assumption** is the sufficient-statistic qualification (step 4). And the **anchor/terminus
reconciliation** shows the Petz-first reorientation is a consequence of the argument: Chentsov
pins and terminates the base; the shape axis (the Petz extension) carries the content and the
open selection question.

**Honest status:**
- Steps (2), (3), (5), (6) are theorems / standard results. **[T]**
- Step (4) — the sufficient-statistic qualification — is the **single load-bearing
  assumption [A/O]**. It is where the genericity is purchased, and it delimits the strict
  Chentsov case to the binary/one-parameter base. A new conversation auditing the foundations
  should focus its skepticism here; everything else is rigorous given it.
- The two-extensions-are-two-axes alignment is **verified structurally [V]** (Campbell radial
  ⊥ simplex; the peel's scale move *is* the radial direction).
- **[O]** Whether step (4) can be *derived* (rather than posited) from passivity/boundedness
  plus a natural additional condition — i.e., whether a passive bounded ensemble *must* carry
  the sufficient-statistic structure — is the deepest open foundational question, and closing
  it would convert the foundation from "rigorous given a posit" to "rigorous." This is
  distinct from, and prior to, the metric-selection question (O-C): (4) is whether the base is
  *forced to qualify*; O-C is which metric is selected on the *fiber* once it does.

---

*End of foundations note. The object is the space (metric as output); the order is a
necessary dependency with one assumed link (the sufficient-statistic qualification, step 4);
Chentsov is invoked for rigidity, not the toolbox; and the anchor/terminus reconciliation
shows the Petz-first reorientation and the two-axis decomposition fall out of the foundational
argument itself — Campbell and Petz are the two orthogonal axes, Chentsov their uniquely-forced
common base. The load-bearing posit (step 4) and its possible derivation (O) are flagged as
the deepest foundational frontier, prior to the metric-selection question. Companion to the
focused core; a candidate foundations section for the eventual comprehensive reference.*

---

## Appendix — The commutativity/associativity axis and the Markovianity axis (self-contained)

*This note refers above to two axes — "commutativity/associativity" and "Markovianity" —
and to a "detailed-balance" locus. This appendix states what those mean so the document is
self-contained. The two axes originate in a parametrized family of compositions studied in
the broader program (the "ζ-sideline"); only the structural content needed here is given.*

**The setting.** Consider composing the framework's transformations in sequence — rung after
rung of the cascade, or more generally a chain of the projective (Möbius/SL(2,R)) maps that
act on the budget/SNR observable. Such a family of compositions carries two independent
parameters that are conjugate to each other (they behave as a harmonic-conjugate pair —
roughly, real and imaginary parts of one analytic structure). Call them t and σ.

**The commutativity/associativity axis (t).** This parameter controls whether the composed
maps **commute / associate**. At **t = 0** the rungs commute: the order of composition does
not matter, and the composition is associative. Off zero, the commutator of two rungs is
**[f_a, f_b] = O(t)** — the maps fail to commute in proportion to t. So t measures departure
from the commutative/associative limit.

- **The cascade lives at t = 0.** Its composition is carried by the scalar residual masses
  uₙ, whose cumulative product ∏uₙ is order-independent (scalar multiplication commutes). So
  the cascade *is* the associative/commutative limit; this is why peeling is order-independent
  and history-free *as a composition*.
- **t ≠ 0 is the frame-dragging regime.** Deforming the peel so that a shape-rotation of
  strength t mixes into the scale move produces, simultaneously and both linear in t, a
  scale–shape cross-term and O(t) rung non-commutativity — the structural signature of a
  rotating (Kerr-like) metric, where one rotation parameter sources both the off-diagonal
  term and the non-commutativity. (Verified as structure; the gravitational reading is the
  open instantiation question.)
- **Identification with the geometry.** The t-axis is the **scale axis** of the decomposition
  (the cascade/depth direction). Its orthogonal partner is the shape axis.

**The Markovianity axis (σ).** This parameter controls **memorylessness of the multi-step
process** — whether the dynamics the cascade composes is Markovian. It carries a symmetry
σ ↔ 1−σ; the symmetric point **σ = 1/2 is detailed balance / reversibility** (the
Fokker–Planck-style symmetry of forward and backward transition structure). So σ measures
where the underlying process sits between irreversible and reversible, with σ = 1/2 the
reversible (detailed-balance) locus.

- **No load is borne on σ.** The cascade lives on the t-axis (associativity); σ is the
  *orthogonal* axis. Showing the cascade is associative (t = 0) says **nothing** about
  whether the underlying process is Markovian (σ) — the two are conjugate/independent. So the
  framework neither assumes nor determines Markovianity: the cascade is compatible with any σ.
  (The metric weights used in this work happen to be local in the spectrum, which places the
  *specific* realization at the memoryless point, but that is a choice of example, not a
  requirement of the structure.)
- **Why this matters for §3's reciprocity discussion.** Reciprocity (S = Sᵀ, reversibility)
  is a *reversibility/symmetry* condition and therefore aligns with the σ-axis (the
  detailed-balance direction at σ = 1/2), **not** with the metric structure. This is why
  reciprocity is optional and orthogonal to the foundation: it is a locus on the σ-axis, and
  the monotone metric is σ-blind (monotone under all stochastic maps, reversible or not). The
  precise identification reciprocity ⟺ σ = 1/2 is flagged **[O]**; what is firm is that
  reciprocity sits on the reversibility axis, orthogonal to the metric.

**The conjugacy, and why it forbids one tempting argument.** t and σ are conjugate (a
harmonic-conjugate pair). Conjugacy means a property on one axis does not transfer to the
other — which is exactly why associativity (t) carries no information about Markovianity (σ),
and why an argument that tried to derive a σ-property (e.g. a monotonicity/reversibility
conclusion) from a t-property (the cascade's associativity) would be unsound. The two axes
must be treated independently; the foundation uses only the t = 0 (associative) structure and
leaves σ free.

**Summary of the appendix.** Two conjugate, independent axes govern composition: **t**
(commutativity/associativity; t = 0 is the commuting/associative limit where the cascade
lives; t ≠ 0 is frame-dragging; t is the scale axis) and **σ** (Markovianity; σ = 1/2 is
detailed balance/reversibility; the cascade bears no load on σ; reciprocity aligns with this
axis, orthogonal to the metric). The decomposition's scale ⊥ shape orthogonality is the t-axis
and its conjugate partner; Markovianity (σ) and reciprocity live on a separate, optional axis
that the foundation does not require.
