# Investigation Record Addendum: The Dynamics Thread

## Derivatives as Connections on Budget Manifolds, and the Scope of "Generic Dynamics" in TEP

*A working record of one extended investigation into whether the TEP/Entrodynamics
framework can accommodate a dimension-agnostic, generic dynamical theory. The
investigation produced one positive structural result (the paired-budget
scalar-potential construction), one secondary structural result (the associated
1+1 Lorentzian arena and its fibre-bundle organization), and a set of explicitly
scoped or retired branches. As with the prior comprehensive records, this
document distinguishes carefully between what is forced by the framework's
algebra, what is a motivated construction, and what was pursued and found
wanting. Several methodological corrections are recorded openly, including
instances where the assisting model over-generalized a result or pursued a
tangent before being corrected.*

*Date of record: 21 May 2026. Companion to Comprehensive Investigation Records
I–III and the cited derivation addenda.*

---

## Preface: Scope and Epistemic Standards

The previous comprehensive records documented the framework's technical content
for thermal-statistical physics (the cascade-family stratification, the BE/MB/FD
Riccati orbits, the NSR-composition derivation of Haldane statistics), for
passive scattering (the layered budget architecture of coupled DHO systems), and
for the foundational reckoning grounded in Chentsov's theorem.

This addendum covers a different question, raised after that foundational work:
**can the framework accommodate a generic, dimensionless, dimension-agnostic
notion of dynamics** — not the family-specific Riccati flows already in the
corpus, but a structural account of what a *derivative* is, framework-internally,
and therefore of what *dynamics* is at the framework's level of generality.

The motivating observation, due to the framework's author, is sharp and worth
stating precisely because it organizes everything that follows:

> A derivative is a subclass of composites — it is two metrics in ratio. But it
> is not a *generic* ratio. A generic ratio Y/X is perspectivally privileged
> toward the denominator: X is the independent variable, the state parameter,
> the thing whose change drives the change in Y. A genuine derivative requires
> *dependence* between numerator and denominator, but the framework should be
> able to describe that dependence in generic terms — without privileging either
> slot, and without assuming the two metrics are budget duals.

The investigation's task was to find the framework-internal object that meets
this specification: derivative-specific (not applying trivially to all ratios),
dimension-agnostic, instantiation-independent, and carrying genuine dynamical
content rather than a locked or trivial constraint.

The standards used throughout are those of the prior records:

1. **Derivational / forced** — a consequence of the framework's stated algebra
   (the budget identity, the construction formula, the SU(1,1) structure) with
   no external physical input.
2. **Constructed / motivated** — a definition introduced for good structural
   reasons but representing a choice, not a forced consequence.
3. **Scoped** — valid only under stated conditions, with the conditions made
   explicit.
4. **Retired** — pursued and found not to deliver what was hoped, recorded so it
   is not re-explored.

The Central Reference's tier vocabulary is used in the closing summary.

---

## Part 1: The Single Two-Term Budget — Where Its Derivative Content Lives

Before the positive result, a clarifying obstruction — but one that must be
stated narrowly, because a first phrasing of it in this investigation was too
strong and was corrected against an explicit instantiation (the damped harmonic
oscillator). The corrected statement is more useful than the overclaim it
replaces.

The framework's primary object is the two-term budget identity

$$x^2 + u = 1.$$

A natural first attempt at a framework-internal derivative is to identify the
numerator with one budget sector and the denominator with the other — Y with
x², X with u — and ask for the rate of one with respect to the other, or the
rate of each with respect to the budget's own intrinsic rapidity η.

### 1.1 What is genuinely forced

The budget identity is a *single rigid constraint* on *two* quantities, so it
leaves exactly one degree of freedom. Differentiating,

$$\frac{dx^2}{d\eta} = -\frac{du}{d\eta},$$

so the response of the signal sector to any change *in the budget's own
coordinate* is exactly minus the response of the noise sector. The ratio of
sector responses is locked at −1. Equivalently, the sector-versus-intrinsic-
rapidity derivative is a fixed function with no independent freedom: with
x² = ½(1 + tanh 2η_s) by construction, d(x²)/dη_s = sech²(2η_s) is determined
entirely by η_s.

This much is forced and verified. The narrow, correct statement is:

> **A single two-term budget cannot host a nontrivial derivative *between its
> own two sectors expressed in its own intrinsic rapidity coordinate*.** In that
> coordinate the sector relationship is kinematically frozen — the response
> ratio is locked at −1.

### 1.2 The overclaim, and its correction against the damped oscillator

A stronger phrasing — "a two-term budget cannot host a nontrivial derivative at
all, full stop" — was initially adopted in this investigation and is **wrong**.
It was corrected by testing against a concrete instantiation, the underdamped
harmonic oscillator, whose kinetic and potential energy fractions form a genuine
two-term budget KE/E + PE/E = 1 (verified to machine precision in numerical
integration).

In that system the two sectors are emphatically *not* dynamically dead. The ratio
PE/KE sweeps its full range as energy sloshes between the sectors; the signed
rapidity η_s = ½ ln(PE/KE) oscillates; its rate dη_s/dt changes sign dozens of
times over a multi-period run. A two-term budget can carry thoroughly nontrivial
dynamics.

The reconciliation is the substantive point. The response ratio is locked at −1
*in the budget's intrinsic rapidity coordinate*, but the oscillator's energy does
not evolve along that coordinate — it evolves along *physical time*, and the map
from physical time to budget rapidity is itself time-dependent and oscillatory.
The locked −1 is a statement about the intrinsic coordinate; the rich PE/KE
dynamics is a statement about physical time; the two are reconciled entirely by
the nontrivial reparametrization t ↦ η_s.

### 1.3 The corrected lesson: the dynamics is in the clock

The corrected and more useful statement:

> **A two-term budget's dynamical content lives in its *clock function*
> dη/dt — the map from physical time to budget rapidity — not in the ratio of
> its two sectors.** The sector ratio is kinematically determined relative to
> the budget's own coordinate; all genuine dynamics is the non-constancy of the
> clock.

This reframes the obstruction productively rather than negatively. It is not
that two-term budgets are dynamically inert — they are not. It is that their
dynamics is *located* in dη/dt, and a single budget has no second clock to
compare its clock against. A derivative is fundamentally a *comparison of
clocks*; one budget supplies one clock; you need a second clock for the
comparison to be nontrivial.

This is exactly why the positive result (Part 3) is a *two-budget* construction:
the connection compares the clock of budget a against the clock of budget b, and
its content — d log Φ/ds = x_a − x_b — is precisely a statement about two
clocks in relation. The single-budget "obstruction" and the two-budget
connection are therefore two faces of one fact: dynamical content is relational
between clocks, not internal to a sector ratio.

Three attempts in the investigation that produced *locked* results — the
sector-response ratio (−1), an imposed reciprocal constraint (ratio constant),
and the equal-increment constraint imposed *within a single budget* (increment
ratio ±1) — were all instances of trying to extract a derivative from a single
clock. They fail for that reason, not because two-term budgets lack dynamics.

The two routes to a nontrivial framework-internal derivative are therefore:
(i) a structure *between two budgets* — two clocks — which is the connection of
Part 3; or (ii) the three-term budget x² + w + u = 1, where the third sector
supplies a second independent degree of freedom within one object (noted in
Part 6 as viable but undeveloped).

---

## Part 2: The Construction Formula Reading, and Why It Was Insufficient

The construction formula

$$x^2 = e^{-2|\eta|}, \qquad \eta = \ln(X / X_{\text{inv}})$$

maps any bounded measure X (with operationally identified extremum X_inv) to a
budget variable. A natural reading of a derivative within this apparatus: the
rapidity of a ratio Y/X is the *difference of constituent rapidities*,

$$\eta_{Y/X} = \eta_Y - \eta_X = \ln\!\left(\frac{Y/X}{Y_{\text{inv}}/X_{\text{inv}}}\right),$$

and the ratio's budget variable follows from the construction formula applied to
this difference.

This reading is correct as far as it goes, and it has one genuine virtue: it
explains the appearance of the c/√2 self-dual point in relativistic kinematics.
With X = v, X_inv = c, the ratio v/c has its self-dual point at v/c = 1/√2,
which is where the framework's signed log-SNR changes sign (Part 5) and where
several physical observables exhibit algebraic transitions. The Chicone–Mashhoon
result is, on this reading, not an external confirmation but a consequence of the
framework already treating velocity as a ratio-budget.

**However, this reading was correctly judged insufficient by the framework's
author**, for a decisive reason: it is not derivative-specific. The construction
η_Y − η_X applies to *any* ratio of two bounded measures, the overwhelming
majority of which have nothing to do with dynamics. A generic ratio of two
unrelated quantities is not a derivative. The rapidity-difference reading
produces a budget for every ratio indiscriminately; it does not capture the
*dependence* between numerator and denominator that distinguishes a derivative
from an arbitrary quotient.

The defect is precise: in η_Y − η_X, the two rapidities η_Y and η_X are
*independent*. A derivative requires them to be *coupled* — both driven by a
common underlying change. The rapidity-difference reading is retired as a
candidate for the generic derivative, retained only as the correct description
of generic ratios (a strictly weaker object).

---

## Part 3: The Positive Result — Derivatives as a Scalar Potential on Paired Budgets

The construction that does meet the specification treats the derivative not as a
conversion (a scalar relating numerator to denominator) but as a *comparison
between two budget manifolds*. The comparison object is the ratio of G-factors,
Φ = G(x_a)/G(x_b); Part 4 establishes that this object is a globally-defined
scalar potential on the two-budget space (the term "connection," used in earlier
drafts of this investigation, is corrected there). The construction is presented
here; its properties — flatness identity, gradient quantity — follow.

### 3.1 The construction

Take two budgets, each on its own Poincaré disk, in rapidity coordinates:

$$x_a = \tanh(\eta_a), \quad x_b = \tanh(\eta_b), \qquad G(x) = \frac{1}{\sqrt{1-x^2}} = \cosh(\eta).$$

The author's specification — eliminate the perspectival privilege of the
denominator by constraining numerator and denominator to co-evolve with equal
increments — is imposed as

$$|\Delta\eta_a| = |\Delta\eta_b|.$$

In the same-sign (diagonal) branch this is the one-parameter joint boost

$$\eta_a(s) = \eta_{a0} + s, \qquad \eta_b(s) = \eta_{b0} + s,$$

where s is the joint-boost rapidity — the evolution parameter, and the answer to
the author's question "what does the coupled change evolve with respect to." It
is neither a's rapidity nor b's, but the rapidity of the diagonal SU(1,1)
one-parameter subgroup that boosts both symmetrically.

Under this constraint the *increment ratio* Δη_a/Δη_b is locked at +1. This is
the author's observation that what standard mechanics calls an acceleration (a
second-order rate) is here re-expressed as a boost (a first-order transformation),
with the locked ratio being the "Δ²" signature of the change. The locked
increment ratio carries the *fact* of change but not its variation; the genuine
dynamical content must therefore live elsewhere.

### 3.2 The connection coefficient

The nontrivial content is the **capacity ratio** — the ratio of the two budgets'
remaining boost capacities before budget-boundary saturation:

$$\Phi(s) = \frac{G(x_a)}{G(x_b)} = \frac{\cosh(\eta_{a0}+s)}{\cosh(\eta_{b0}+s)}.$$

This is the connection coefficient: the rule for transporting a unit of change
from a's manifold to b's. It is dimensionless, it is not locked (it varies as the
pair evolves), and it is exactly the f(G(x)) form the author's intuition
anticipated. Crucially, Φ is **not a constraint between x_a and x_b** — it is a
third object living between them. That is why it does not collapse the way every
scalar-tie attempt of Part 1 did.

### 3.3 The flatness ⟺ alignment identity (verified)

Differentiating along the joint boost (verified symbolically, sympy 1.14):

$$\frac{d\Phi}{ds} = \frac{\sinh(\eta_{a0} - \eta_{b0})}{\cosh(\eta_{b0}+s)^2}.$$

The numerator depends **only** on the rapidity gap δ = η_{a0} − η_{b0}, and is
constant along the joint boost (s does not appear in it). This yields the
investigation's central identity:

> **δ = 0** (the two budgets share a rapidity — aligned)
> ⟹ dΦ/ds = 0 ⟹ Φ ≡ 1 ⟹ **the connection is flat**.
>
> **δ ≠ 0** (the budgets are misaligned)
> ⟹ Φ varies along the boost ⟹ **the connection is curved**.

This is the identity the author conjectured before the calculation: the degree of
eigenbasis alignment *is* the flatness of the connection. It is not an analogy —
it is an equality. A flat connection is exactly one where the two budgets share a
rapidity. The framework's word "flat" thereby becomes literally correct: a flat
connection is one in which the equal-increment constraint is globally integrable
and the budgets' rapidities stay aligned under transport.

### 3.4 The logarithmic rate (verified)

The connection coefficient's logarithmic rate of change is a clean,
framework-native quantity (verified numerically to 1e−11 over 2000 random
points; sympy's `simplify` does not auto-close the arctanh/log form, but the
identity holds exactly):

$$\frac{d\log\Phi}{ds} = x_a - x_b.$$

The rate of the connection coefficient is simply the **difference of budget
variables** — not a ratio, not an exotic combination. This is the genuine
dynamical content the author was after: the increment ratio is locked (the
constraint, the "Δ"), but d log Φ/ds = x_a − x_b is what varies and carries the
real information.

### 3.5 The gradient quantity, and a correction: Φ is a scalar potential, not a curved connection

The gap quantity sinh(δ) controls all variation factors, at any point along the
boost, as

$$\sinh(\delta) = G(x_a)\,G(x_b)\,(x_a - x_b)$$

(verified symbolically; uses sinh η = xG, cosh η = G). It is nonzero precisely
when x_a ≠ x_b, i.e. when the budgets are misaligned, weighted by both G-factors.
The second-order behaviour is

$$\frac{d^2\Phi}{ds^2} = \frac{-2\sinh(\delta)\,\sinh(\eta_{b0}+s)}{\cosh(\eta_{b0}+s)^3}.$$

**A correction is required here, and it is recorded openly.** An earlier phrasing
of this investigation called sinh(δ) = G_a G_b (x_a − x_b) "the curvature of the
connection" and described Φ as an affine connection with curvature and holonomy.
That language is too strong, and the closure check that exposed it is documented
in Part 4.3. The corrected statement:

Φ = G(x_a)/G(x_b) = cosh(η_a)/cosh(η_b) is *globally a function of position* on
the two-budget space. Its logarithm, log Φ = log cosh η_a − log cosh η_b, is a
**separable scalar** — a function of a minus a function of b. The 1-form
d(log Φ) is therefore *exact*; its exterior derivative (the curvature 2-form) is
identically zero; and the holonomy of Φ around any closed loop in the two-budget
space is trivial. Φ is **not a connection with curvature in the gauge-theoretic
sense** — it is a *scalar potential* on the two-budget space. (This concerns Φ
specifically; it is not a statement about the framework's boundary-transport
holonomy, which is separate and nontrivial — see §4.2.)

What sinh(δ) = G_a G_b (x_a − x_b) actually measures is therefore not a curvature
but the *gradient of that scalar potential along the diagonal branch*. The
"flat versus curved" language of §3.3 should accordingly be read as "the scalar
potential is constant versus varying along a chosen branch." The flatness ⟺
alignment identity itself survives intact under this rewording — Φ is constant
along the diagonal branch iff δ = 0 — but it is a statement about a scalar's
stationarity, not about a connection's curvature. This correction does not weaken
the result; §4.4 and the separate flatness/collapse treatment argue that the
universal exactness of these forms is itself a substantive structural finding.

### 3.6 Why this is derivative-specific and not generic-ratio

This resolves the defect of Part 2. A generic ratio Y/X has no connection
structure — nothing transports, nothing is constrained, the two quantities are
independent. The object constructed here is the *data of how a unit of change
transports between two budgets under a co-evolution constraint*. A connection is,
by definition, "a derivative that does not privilege a coordinate" — which is
exactly the author's specification. Generic ratios are not connections;
derivatives are. The construction is therefore genuinely derivative-specific.

It is also dimension-agnostic and instantiation-independent: the connection is
defined purely by the two budget rapidities, with no reference to what a and b
physically are, no dimensional content, and no choice of cascade family or
SU(1,1) generator. This is the property the K-A-N classification (Part 6) lacks.

### 3.7 Status

**Constructed / forced hybrid.** The construction (the equal-increment constraint,
the same-sign branch) is a motivated choice. Given that choice, the
flatness ⟺ alignment identity, the logarithmic rate x_a − x_b, and the gradient
quantity G_a G_b (x_a − x_b) are all forced consequences, verified symbolically
and numerically. The identification of Φ as a *scalar potential* (not a curved
connection) is forced by the closure check of §4.3. What is **not** established
is that any particular physical system's dynamics *is* this structure; that is
the open empirical step (Part 7).

---

## Part 4: The Two Branches, the Lorentzian Arena, and the Dual-Pair Reading

The Part 3 construction used only one of the two branches the equal-increment
constraint admits. Completing it — computing the second branch, the joint metric,
and the closure of the resulting forms — both corrects the "curvature" language
of Part 3 and yields the secondary structural result: the pair of budgets joined
by a derivative constraint is a 1+1 Lorentzian arena, with the two budgets
entering as a dual pair.

### 4.1 The decomposition and the two branches

For two coupled budgets in rapidity coordinates, write

$$\Sigma = \eta_a + \eta_b, \qquad \Delta = \eta_a - \eta_b,$$

so dη_a = ½(dΣ + dΔ) and dη_b = ½(dΣ − dΔ). The equal-increment constraint
|Δη_a| = |Δη_b| admits two branches, and they are exactly the two coordinate
axes of the (Σ, Δ) plane:

- **Same-sign (diagonal) branch:** η_a = η_{a0}+s, η_b = η_{b0}+s. Moves along
  Σ at fixed Δ. This is the branch of Part 3.
- **Opposite-sign (anti-diagonal) branch:** η_a = η_{a0}+s, η_b = η_{b0}−s.
  Moves along Δ at fixed Σ.

The opposite-sign branch was computed (verified symbolically and numerically)
and is the clean mirror of the same-sign branch, with the rapidity *gap* δ
replaced throughout by the rapidity *sum* Σ_0 = η_{a0}+η_{b0}:

| Quantity | Same-sign branch | Opposite-sign branch |
|---|---|---|
| dΦ/ds | sinh(δ)/cosh²(η_{b0}+s) | sinh(Σ_0)/cosh²(η_{b0}−s) |
| stationary (flat) ⟺ | δ = 0 (budgets aligned) | Σ_0 = 0 (budgets antisymmetric) |
| d log Φ/ds | x_a − x_b | x_a + x_b |
| gradient quantity | sinh δ = G_a G_b (x_a − x_b) | sinh Σ_0 = G_a G_b (x_a + x_b) |

The two branches are therefore a matched pair: one governed by Δ, one by Σ; they
are the two natural axes of the (Σ, Δ) plane.

### 4.2 The closure check — Φ is a scalar potential

With both branches in hand, the question of §3.5 can be settled. Is d(log Φ) a
connection 1-form with curvature, or an exact form?

log Φ = log cosh η_a − log cosh η_b is separable — a function of a minus a
function of b. Its mixed partials on the (Σ, Δ) plane agree exactly (verified):

$$\partial_\Delta\partial_\Sigma \log\Phi = \partial_\Sigma\partial_\Delta \log\Phi = \frac{\cosh\Delta\,\cosh\Sigma + 1}{(\cosh\Delta + \cosh\Sigma)^2}.$$

So d(log Φ) is **closed**, hence exact (the (Σ,Δ) plane is simply connected),
hence its curvature 2-form is identically zero and the holonomy of *this object*
around any closed loop in the (Σ,Δ) plane is trivial. **Φ is a globally-defined
scalar potential, not a connection with curvature.** This is the correction
flagged in §3.5. The "flat ⟺ aligned" identity survives as a statement about a
scalar's stationarity along a branch; the gauge-theoretic language of curvature
and holonomy is withdrawn *for Φ*.

This must be scoped precisely, to avoid a second overclaim in the opposite
direction. The triviality established here is the triviality of *one specific
object* — the scalar potential Φ = G(x_a)/G(x_b) on the (Σ,Δ) plane of a paired
two-budget construction. It is **not** a claim that the framework has no
holonomy. The framework's boundary-transport machinery — the SU(1,1) gluing
operations, the conserved boundary-phase-current, Schur reduction across
composite boundaries — carries genuine, nontrivial holonomy, and nothing here
bears on that. What collapses is the *inter-manifold topology* of independently
constructed budget manifolds (the multiplicity-collapse / single-manifold
observation); what remains nontrivial is *transport along framework boundaries*.
These are different objects and the present result speaks only to the first.

The exactness is not specific to this Φ. It follows from log Φ being separable,
which in turn follows from the construction formula building each budget
independently. That every framework connection between two budget manifolds is
correspondingly flat — and what that implies — is a substantive structural claim
treated separately (see the companion note on connection-flatness and
multiplicity collapse); it is too consequential to fold into this working record.

### 4.3 The joint metric — a 1+1 Lorentzian arena

The naive joint metric dη_a² + dη_b² is Pythagorean (signature ++), and an
earlier step of this investigation wrongly concluded from it that the (Σ,Δ)
plane is Euclidean. That was the wrong metric: summing the two rapidity line
elements in quadrature treats *both* budgets as numerator and discards the
numerator/denominator asymmetry that defines a derivative.

The corrected joint metric carries that asymmetry as a relative sign:

$$ds^2 = d\eta_a^2 - d\eta_b^2 = d\Sigma\,d\Delta.$$

This is the null (light-cone) form of the 1+1 Minkowski metric. Σ and Δ are its
two null coordinates; the two equal-increment branches are its two null
directions. The pair of budgets joined by the derivative constraint is therefore
a genuine 1+1 Lorentzian arena.

### 4.4 The dual-pair reading — and why no slot is privileged

The relative sign in ds² = dη_a² − dη_b² requires interpretation, and the
interpretation must be stated with care, because a careless phrasing would assert
the opposite of what the construction achieves.

It is tempting to call one rapidity "timelike" and the other "spacelike." This
language is **deliberately not used here.** It is a confusing vestige: it imports
the connotation that the timelike slot is a distinguished evolution parameter —
which would reinstate exactly the perspectival privilege of the denominator that
the whole construction was built to eliminate. It also misleadingly suggests the
generic budget terms are dimension-flavoured archetypes (space, time), which the
framework does not claim.

The correct reading: the two budgets enter the derivative as a **dual pair**.
One slot transforms covariantly, the other contravariantly, with respect to a
shared metric space. Their increments therefore contribute with opposite sign to
the joint quadratic form. The indefinite signature is nothing more than the
index-raising/lowering asymmetry of a dual pairing — and a dual pairing is the
canonical example of two objects that are operationally distinct yet *neither
privileged*: a vector and a covector pair to a scalar, transform by inverse
matrices, and neither is "the" distinguished one.

**The shared metric space must be named explicitly.** The two budgets are not
co-/contravariant with respect to each other (circular) but with respect to the
**budget rapidity axis**: the single real line ℝ, carrying the Poincaré metric
ds_P² = dη², into which the construction formula x = tanh(η), η = ln(X/X_inv)
maps *every* budget. That line is shared because the construction formula is the
same map for every budget; a and b are two embeddings into that one line. (This
is the same "one shared line" that the connection-flatness/collapse result
identifies from the differential-geometric side.)

What is **forced** and what is **convention** must be distinguished:

- *Forced:* the two slots enter with opposite signature — as a dual pair. If they
  entered symmetrically (both covariant, ++), the metric would be Euclidean and
  there would be no derivative structure, only an arc length. The derivative
  *requires* the dual pairing.
- *Convention (flagged):* which specific slot is labelled covariant and which
  contravariant. The construction formula yields two budget rapidities; it does
  not assign the upper and lower index.

That the labelling is genuine convention is established by the swap-symmetry
test (§4.5), not merely asserted.

### 4.5 Swap symmetry — the formal statement that no slot is privileged

Under the exchange a ↔ b, the coordinates transform as

$$\Sigma \to \Sigma, \qquad \Delta \to -\Delta,$$

a reflection of the light-cone about the Σ axis — an involution (applying it
twice is the identity). Every quantity derived in this investigation is then
either invariant or simply reflected (verified):

- **Σ-sector quantities are invariant:** the joint boost Σ, the sum x_a + x_b,
  the opposite-branch gradient sinh Σ_0.
- **Δ-sector quantities reflect (acquire a sign):** the gap Δ, the difference
  x_a − x_b, the same-branch gradient sinh δ, and Φ → 1/Φ (so log Φ → −log Φ).

Nothing acquires new content under the swap; nothing is destroyed. The swap is a
discrete symmetry of the entire structure. Therefore the covariant/contravariant
labelling of the two slots is a convention: exchanging the labels reflects Δ and
inverts Φ — a relabelling, not a physical change.

This is the formal statement that the construction has eliminated the
perspectival privilege of the denominator. The only asymmetry that remains is the
index duality itself — and even that is convention up to the reflection
Δ → −Δ. Neither slot is, or is implied to be, a distinguished state parameter.

### 4.6 The fibre-bundle organization

The same (Σ, Δ) structure organizes as a fibre bundle, which clarifies
constrained versus generic evolution:

| Bundle element | Identification |
|---|---|
| Base coordinate | Δ = η_a − η_b (the misalignment) |
| Fibre coordinate | Σ = η_a + η_b (the joint boost) |
| Total space | the (η_a, η_b) plane = product of the two budgets' disks |
| Projection | π(η_a, η_b) = η_a − η_b |
| Scalar potential | Φ = G(x_a)/G(x_b), separable, exact |

The same-sign branch is motion along a fibre (fixed Δ); the opposite-sign branch
is motion along the base (fixed Σ). A fully generic dependent evolution is a path
with both components. This corrects a hope raised mid-investigation that *any*
changing ratio could be rearticulated to abide the equal-increment constraint:
it cannot. What is true is that any changing ratio *decomposes* into a
constraint-abiding part (Σ motion) and a constraint-violating part (Δ motion);
the equal-increment constraint defines the distinguished subclass of fibre-only
evolutions, not a universal property of ratios.

### 4.7 Status

**Constructed, with forced sub-results.** The two-branch structure, the closure
of d(log Φ) (hence Φ as scalar potential), and the swap symmetry are forced and
verified. The Lorentzian metric ds² = dΣ dΔ is forced *given* that the
derivative's numerator/denominator asymmetry is read as a dual pairing — a
well-motivated reading, and the only one consistent with there being a derivative
structure at all, but an interpretive identification rather than a theorem. The
fibre-bundle organization is a motivated framing, internally consistent, not
independently verified against a physical system.

---

## Part 5: A Universal Algebraic Feature — The Sign Change of ln(SNR)

One algebraic fact, family-independent, deserves recording because it organizes
the geometry of the self-dual point.

The signal-to-noise ratio SNR = x²/u satisfies, universally,

$$\ln(\text{SNR}) = \ln(x^2/u), \qquad \ln(\text{SNR}) = 0 \iff x^2 = u = \tfrac{1}{2}.$$

The natural **signed rapidity** is η_s = ½ ln(SNR), with the clean identity

$$\tanh(\eta_s) = 2x^2 - 1.$$

In this coordinate the full manifold runs η_s ∈ (−∞, +∞), the self-dual point is
the *regular interior point* η_s = 0, and the two budget extrema are at η_s = ±∞.
The corpus's standard rapidities — η_C = ln(1 + SNR) and η_M = SNR — are
positive-definite and do not cross zero; the signed rapidity η_s is the natural
coordinate in which the self-dual point is a sign change rather than a boundary.

This clarified a scope point for the self-dual threshold (see Part 6, hemi-fold):
a physical observable will exhibit qualitative transition at the self-dual point
**only if** it carries a tanh(η_s) = (2x² − 1) algebraic factor. Observables
without that factor pass through the self-dual point smoothly. The framework's
identification of the self-dual point as algebraically special is universal; its
manifestation as a *physical* transition is conditional on the observable's
algebraic form.

---

## Part 6: Scoped and Retired Branches

The investigation pursued several other constructions. Each is recorded here with
its honest status, so they are not re-explored without new reason.

### 6.1 The hemi-fold construction — SCOPED

A Campbell-style decomposition splitting the budget manifold at the self-dual
point into two conditional sub-manifolds ("hemi-folds"), each carrying its own
G-factor with divergence at the shared self-dual boundary. The hemi-fold G-factor
satisfies the elegant identity

$$G_{\text{hemi}}(\zeta) = \frac{G(\zeta)}{G(i\zeta)}, \qquad G(i\zeta) = (1+\zeta^2)^{-1/2},$$

i.e. the standard G-factor divided by its Wick-rotated form — the framework's
T-cycle structure appearing in the hemi-fold pairing.

**What holds.** Where the underlying physics provides an observable with the
(1 − 2p²) algebraic form, the hemi-fold construction correctly predicts both the
location of a transition (at p² = 1/2) and the divergent scaling of dynamical
timescales near it. Two confirmations: the Chicone–Mashhoon generalized Jacobi
equation, whose tidal coefficient is κ(1 − 2V²) with sign change at V = c/√2;
and the driven single DHO, whose resonance frequency is ω_r = ω_n√(1 − 2ζ²),
vanishing at ζ = 1/√2 (the resonance-existence threshold, distinct from critical
damping at ζ = 1).

**What fails.** The construction does not apply at framework self-dual points
where the physics lacks a (1 − 2p²)-form observable. This was tested thoroughly
on the Layer-2 coupled-DHO self-dual point (ζ₁ζ₂ = 1). Across fifteen
Layer-2-natural observables (reactive crossing frequencies, Doppler ratio,
splitting, rapidity, |H₁₂| at crossings, group delays, Q-factors), scanned on
both the minority and majority sides of the self-dual point, **every observable
is a smooth analytic function through the self-dual point** — no divergence, no
hemi-fold scaling. The Layer-2 self-dual point is a regular interior point of the
coupled-DHO parameter space; the framework identifies it as algebraically
self-dual (it is where x_z² = 1/2), but no physical observable is sensitive to
that algebraic fact.

**Status: scoped.** The hemi-fold construction is valid only where the underlying
physics supplies a (1 − 2p²)-form observable. It is not a generic feature of
framework self-dual points. The two confirmations stand within that scope; the
construction is not a general-purpose predictive tool. It is also tangential to
the generic-dynamics question — it was a construction about self-dual thresholds,
not about derivatives, and is retired from the dynamics thread proper.

### 6.2 The gradient flow ẋ = −ln(SNR) — RETIRED as "the" dynamics

Integrating the signed quantity of Part 5 gives a potential

$$F(x) = \int \ln(\text{SNR})\,dx = 2x\ln x + (1-x)\ln(1-x) - (1+x)\ln(1+x),$$

with the compact closed form (verified numerically on (0,1))

$$F(x) = x\,\ln(\text{SNR}) - 2\,\mathrm{arctanh}(x).$$

F(x) is convex on (0,1) with a unique minimum at the self-dual point x = 1/√2,
suggesting a gradient flow ẋ = −F'(x) = −ln(SNR(x)) that drives any state toward
the self-dual point as attractor. The cascade and MRC versions of this flow are
related by the bridge Jacobian dη_C/dη_M = 2x — so the flow *is* family-universal
when expressed in budget coordinates.

**Why it is retired as the framework's generic dynamics.** The corpus's existing
family-specific Riccati flows (BE: dn/ds = −n(1+n); the Family II, III, IV flows)
are qualitatively distinct: they are polynomial in occupation, and their
attractors are at the *manifold boundaries* (x → 0 for depletion-type, x → 1 for
saturation-type). The gradient flow ẋ = −ln(SNR) is logarithmic and its attractor
is the *self-dual point*. Direct comparison confirmed these are different
dynamical objects with different fixed points and different sign structure.

The gradient flow is therefore a legitimate mathematical construction but **not
"the" framework dynamics**, and not consistent with the corpus's established
Riccati flows as a replacement for them. It is a separate construct whose
physical realization (if any) is unestablished. Most standard physical relaxation
laws (T₁ relaxation, logistic growth, exponential decay) are polynomial, not
logarithmic; the gradient flow's natural home, if it has one, would be
information-theoretic settings (Bayesian updating, maximum-entropy relaxation),
which were not investigated. **Status: retired** from the claim of being the
generic framework dynamics; retained only as a noted construction.

### 6.3 The K-A-N classification — VALID BUT NOT GENERIC

The Iwasawa K-A-N decomposition of SU(1,1) gives a clean classification of flow
generators: K (compact rotation) ↔ reactive/phase dynamics; A (non-compact boost)
↔ dissipative/accumulating dynamics (the corpus's Riccati flows are A-generated);
N (parabolic shear) ↔ active/gain dynamics (Family II, capacity-additive). This
is valid and a useful organizational statement.

**It is not, however, generic.** The K-A-N classification presupposes a chosen
SU(1,1) action — it classifies generators *within* an already-fixed instantiation
(a chosen state space, state parameter, and family). It answers an operational
question ("what kinds of flow can a given instantiation support") but not the
structural question the investigation was after ("what is a derivative,
framework-internally, independent of instantiation"). Its deployment is
instantiation-dependent. **Status: valid, recorded, but set aside** as not
answering the generic-dynamics question. The connection of Part 3 is the
instantiation-independent object; K-A-N is its instantiation-specific
specialization.

### 6.4 The scalar-conversion hope — RETIRED with a lesson

A recurring hope through the investigation was that the relationship between
numerator and denominator of a derivative could be a single scalar — identical,
reciprocal, or otherwise simply tied. Every such attempt produced a trivial
(locked or constant) result.

The lesson, now stated as a structural principle: **any single scalar tie between
numerator and denominator removes one of the two degrees of freedom a derivative
requires, rendering it trivial.** A nontrivial derivative cannot reduce to a
scalar conversion. The connection of Part 3 is precisely the object that relates
two quantities *without* a scalar tie — it is a transport rule, a comparison at a
distance, and its non-reducibility to a scalar is its content, not a defect.
**Status: retired**, with the obstruction recorded as a principle.

---

## Part 7: A Noted Structural Parallel (Not an Identification)

The gradient quantity of Part 3,

$$\sinh(\delta) = G(x_a)\,G(x_b)\,(x_a - x_b) = \sqrt{\tfrac{1}{u_a}\tfrac{1}{u_b}}\;(x_a - x_b),$$

has the same algebraic *form* as the purity-transport bivector of the corpus's
Tier-1 speed-limit result,

$$W_{ac} = \sqrt{\lambda_a \lambda_c}\,(\lambda_a - \lambda_c).$$

Both have the structure (symmetric pairing) × (antisymmetric difference) — the
signature of a rank-2 wedge, an oriented area element on a two-state space.

**This is a structural parallel, not an identification.** The weights differ in a
way that matters: W is weighted by √(λ_a λ_c), a geometric mean of the *state
occupations* (it vanishes when either state is unoccupied); the gradient quantity
is weighted by G_a G_b, a geometric mean of the *boundary-divergence rates* (it
diverges as either budget approaches its boundary). They are the same algebraic
type — rank-2 wedge on a two-state space — with dual weighting behaviour at the
extremes: W-type dynamics freezes exactly where the scalar potential's gradient
grows without bound. The parallel is recorded as suggestive structure; it is
explicitly *not* claimed that the gradient quantity "is" a W. They are wedges on
different manifolds (budget manifold versus state-eigenvalue manifold), with the
weighting each manifold's geometry forces.

---

## Part 8: Methodological Corrections

In the discipline of the prior records, the corrections made during this
investigation are documented openly.

**Over-generalization of the hemi-fold.** The hemi-fold construction was
initially presented as a generic feature of framework self-dual points,
predicting divergent scaling everywhere. This was corrected after the Layer-2
coupled-DHO test: the construction is scoped to systems with a (1 − 2p²)-form
observable. The two confirmations (Chicone–Mashhoon, single DHO) are real within
that scope; the general claim was withdrawn.

**The gradient-flow tangent.** The gradient flow ẋ = −ln(SNR) was pursued as a
candidate for "the" generic framework dynamics. Comparison with the corpus's
Riccati flows showed it to be a distinct construct, not the framework's
established dynamics. It was retired from that claim. The tangent was, in
retrospect, not well-motivated by the original question — it was a construction
about the self-dual point as attractor, not about derivatives.

**Over-retreat, then correction, on Layer-2.** At one point the assisting model
concluded too quickly that the Layer-2 coupled-DHO showed no structure, on the
basis of a small number of observables. The framework's author correctly pushed
back that the prior corpus "falsification" of Layer-2 Lorentz-subtraction claims
was about a different object, and that the right observables had not been tested.
A thorough re-test (fifteen Layer-2-natural observables, both hemi-fold sides)
was then run; it confirmed the smooth-through-self-dual finding properly. The
correction improved the result's reliability; the initial retreat had been
under-evidenced.

**The scalar-conversion hope, recurring.** The hope that numerator and
denominator could be tied by a single scalar recurred several times in different
forms. Each instance was a different face of the same obstruction (Part 1). The
obstruction is now stated as a principle so the hope is not revived without new
reason.

**The two-term-budget overclaim.** An initial version of this addendum stated, in
Part 1, that "a two-term budget cannot host a nontrivial derivative" without
qualification. The author flagged this as untested against instantiation and
noted that budget duals are often closely, even dynamically, related. A direct
test against the damped harmonic oscillator confirmed the concern: a two-term
budget *does* carry rich dynamics. Part 1 was rewritten. The corrected claim is
narrow — the *sector-response ratio in the budget's intrinsic coordinate* is
locked — and the corrected lesson is more useful: the dynamical content of a
two-term budget is its clock function dη/dt, and a derivative is a comparison of
two clocks. This correction strengthened the result rather than competing with
it, by showing the single-budget "obstruction" and the two-budget construction
to be two faces of one fact. The episode is a reminder that even a clean,
well-verified algebraic identity (the locked −1) can be over-read into a broader
claim than it supports, and that testing against a concrete instantiation is the
corrective.

**The curvature overclaim.** An initial version of this addendum described
Φ = G(x_a)/G(x_b) as an affine connection with curvature and nontrivial
holonomy, and called sinh(δ) = G_a G_b (x_a − x_b) its "curvature source."
Completing the construction — computing the opposite-sign branch and then the
closure of d(log Φ) — showed this to be wrong (§4.2). log Φ is separable
(a function of a minus a function of b), so d(log Φ) is exact, the curvature
2-form vanishes identically, and the holonomy *of Φ* is trivial. Φ is a
globally-defined *scalar potential*, not a connection with curvature. The
gauge-theoretic language was withdrawn for Φ throughout and replaced with
"scalar potential / gradient / stationarity." A second scoping correction was
then required in the opposite direction: "trivial holonomy" must not be read as
a claim about the *framework*, which retains genuine boundary-transport holonomy
(the SU(1,1) gluing machinery, the conserved boundary-phase-current); the
triviality is a property of the specific object Φ, not of the framework. The
flatness ⟺ alignment identity survives the rewording. This is an instance where
finishing a half-built calculation (the opposite-sign branch, pursued precisely
because it would either enlarge the result or expose it) exposed an overclaim —
the calibration working as intended. Notably, the *exactness itself* — every
such form being closed because the construction formula admits no cross-terms —
is a substantive finding, treated in the
companion note on connection-flatness and multiplicity collapse.

**The Pythagorean-metric error, and its correction.** An intermediate step
computed the joint metric on the (Σ, Δ) plane as dη_a² + dη_b² and concluded,
wrongly, that the plane is Euclidean — apparently falsifying a conjectured
Lorentzian structure. The author identified the error: summing the two rapidity
line elements in quadrature is additive-in-x budget thinking and discards the
numerator/denominator asymmetry that defines a derivative. The corrected metric
carries that asymmetry as a relative sign, ds² = dη_a² − dη_b² = dΣ dΔ, which is
the 1+1 Minkowski light-cone form (§4.3). The conjectured Lorentzian structure
was therefore not falsified — it had been tested against the wrong metric. The
relative sign is now read not as a spacelike/timelike split (a vestige that would
wrongly imply a privileged state parameter) but as the dual-pairing of two
budgets with respect to the shared budget rapidity axis (§4.4–4.5).

**Distinguishing the author's specification from the model's elaboration.** The
core specification — derivatives as constrained co-evolution with no perspectival
privilege — is the author's, as is the diagnosis of both the Pythagorean-metric
error and the dual-pair (rather than spacelike/timelike) reading. The
construction's elaboration — the two-branch table, the closure check, the
swap-symmetry test, the fibre-bundle organization — is the investigation's. The
author's guard against assuming a and b are budget duals was correct and was
respected: the construction does *not* assume a and b are budget duals in the
x² + u = 1 sense; it assumes only that each carries a budget rapidity, and the
dependence between them is the scalar potential, not an intrinsic duality. The
covariant/contravariant pairing of §4.4 is duality of a different kind — index
duality with respect to a shared metric space — and §4.5 proves it carries no
privileged slot.

---

## Summary of Findings

**Tier 1 — forced, verified.**

1. *The single-budget clock principle.* A single two-term budget x² + u = 1
   cannot host a nontrivial derivative *between its own two sectors in its own
   intrinsic rapidity coordinate* — the budget identity forces the sector-response
   ratio to −1. But a two-term budget is *not* dynamically inert: tested against
   the damped harmonic oscillator, its sectors carry rich dynamics, located
   entirely in the clock function dη/dt (the map from physical time to budget
   rapidity). The corrected principle: a two-term budget's dynamical content lives
   in its clock, not its sector ratio; a nontrivial derivative is a comparison of
   *two* clocks, requiring either a second budget (the connection, Part 3) or a
   third budget term. (Part 1.)

2. *The flatness ⟺ alignment identity.* For Φ = G(x_a)/G(x_b) along the joint
   boost, dΦ/ds = sinh(δ)/cosh(η_{b0}+s)² with δ the rapidity gap. δ = 0
   (aligned) ⟺ Φ stationary along the diagonal branch; δ ≠ 0 ⟺ Φ varies.
   Verified symbolically. (Part 3.3, reworded per Part 4.2.)

3. *The logarithmic rate.* d log Φ/ds = x_a − x_b on the same-sign branch,
   x_a + x_b on the opposite-sign branch — the difference and sum of budget
   variables. Verified numerically. (Parts 3.4, 4.1.)

4. *Φ is an exact form (a scalar potential).* d(log Φ) is closed — its mixed
   partials on the (Σ, Δ) plane agree identically — hence exact, with zero
   curvature 2-form and trivial holonomy *for Φ*. Φ = G(x_a)/G(x_b) is a
   globally-defined scalar potential, not a connection with curvature. (This is
   scoped to Φ; the framework's boundary-transport holonomy is separate and
   nontrivial.) Verified symbolically. (Part 4.2.)

5. *The Lorentzian joint metric.* With the derivative's numerator/denominator
   asymmetry carried as a relative sign, ds² = dη_a² − dη_b² = dΣ dΔ — the 1+1
   Minkowski light-cone form; Σ, Δ are its null coordinates and the two branches
   its null directions. (Part 4.3.)

6. *Swap symmetry.* The exchange a ↔ b acts as Σ → Σ, Δ → −Δ, an involution;
   every derived quantity is invariant (Σ-sector) or reflected (Δ-sector). The
   covariant/contravariant labelling of the two slots is therefore a convention;
   no slot is privileged. Verified symbolically. (Part 4.5.)

7. *The signed-rapidity identity.* tanh(η_s) = 2x² − 1 for η_s = ½ ln(SNR); the
   self-dual point is the regular interior point η_s = 0. (Part 5.)

**Tier 2 — constructed, internally consistent, motivated.**

8. *Derivatives as a scalar potential on paired budgets.* The framework's
   generic, dimension-agnostic, instantiation-independent notion of a derivative
   is the scalar potential Φ = G(x_a)/G(x_b) on the two-budget space, with
   rapidity alignment as stationarity. It is derivative-specific — a comparison
   between two budget manifolds, not a generic ratio — and answers the motivating
   question. (Part 3.)

9. *The Lorentzian arena and the dual-pair reading.* The pair of budgets joined
   by a derivative constraint is a 1+1 Lorentzian arena (ds² = dΣ dΔ). The two
   budgets enter as a dual pair — covariant and contravariant with respect to the
   shared budget rapidity axis — which supplies the indefinite signature without
   privileging either slot. Reading the relative sign as a spacelike/timelike
   split is explicitly rejected as a misleading vestige. (Part 4.3–4.5.)

10. *The fibre-bundle organization.* Coupled budget evolution organizes as a
    fibre bundle: base Δ (misalignment), fibre Σ (joint boost), scalar potential
    Φ = G_a/G_b. The same-sign branch is fibre motion, the opposite-sign branch
    base motion; generic dependent evolution has both. (Part 4.6.)

**Tier 3 — suggestive, recorded without claim.**

11. The gradient quantity G_a G_b (x_a − x_b) shares the rank-2 wedge form of the
    purity bivector W, with dual (capacity- versus state-) weighting. A structural
    parallel, explicitly not an identification. (Part 7.)

**Scoped.**

9. The hemi-fold construction (G_hemi = G(ζ)/G(iζ)) predicts transitions and
   divergent scaling only where the physics supplies a (1 − 2p²)-form observable.
   Confirmed for Chicone–Mashhoon and the single driven DHO; shown not to apply
   at the Layer-2 coupled-DHO self-dual point. Not a generic feature of framework
   self-dual points. (Part 6.1.)

**Retired.**

- The rapidity-difference reading of a derivative (η_Y − η_X): correct for generic
  ratios, but not derivative-specific; the constituents are independent rather
  than coupled. (Part 2.)
- The gradient flow ẋ = −ln(SNR): a legitimate construction with the self-dual
  point as attractor, but distinct from the corpus's Riccati flows and not "the"
  generic framework dynamics. (Part 6.2.)
- The K-A-N classification as a candidate for *generic* dynamics: valid but
  instantiation-dependent; it is the connection's instantiation-specific
  specialization, not the generic object. (Part 6.3.)
- The scalar-conversion hope: any single scalar tie between numerator and
  denominator trivializes the derivative. Recorded as a structural principle.
  (Part 6.4.)

---

## What the Framework Can and Cannot Claim About Generic Dynamics

Stated with the calibration the Central Reference requires:

**The framework can claim** that it possesses a generic, dimension-agnostic
notion of a derivative: the scalar potential Φ = G(x_a)/G(x_b) on the two-budget
space, with rapidity alignment as stationarity, and — when the two budgets are
read as a dual pair — a 1+1 Lorentzian arena (ds² = dΣ dΔ) whose two null
directions are the two equal-increment branches. This is genuinely
instantiation-independent (unlike K-A-N), genuinely derivative-specific (unlike
the rapidity-difference reading of a generic ratio), and it answers the
motivating question: derivatives are a subclass of composites, and the subclass
is characterized by being a comparison between two budget manifolds — a dual
pairing — rather than a mere quotient. The construction is forced once the
equal-increment co-evolution constraint is adopted; its key identities (the
flatness ⟺ alignment identity, the branch rates x_a ∓ x_b, the exactness of
d log Φ, the swap symmetry) are verified.

**The framework cannot yet claim** that this structure *is* the dynamics of any
specific physical system. What has been established is a structural object and
its internal properties. The empirical step — exhibiting a physical system whose
dependent state evolution is a section of the bundle, and verifying that its
observed rate matches d log Φ/ds = x_a ∓ x_b — is not done. Until it is, the
result is "the framework's generic notion of a derivative is a scalar potential
on a dual pair of budgets," not "the framework predicts the dynamics of system X."

**Two interpretive load-bearing points are flagged, not hidden.** First, that the
two budgets enter as a dual pair (opposite signature) is forced — symmetric entry
would give a Euclidean metric and no derivative structure — but *which* slot is
covariant and which contravariant is a convention, shown to be such by the swap
symmetry. Second, the Lorentzian reading depends on accepting the
numerator/denominator asymmetry as that dual pairing; this is the only reading
consistent with a derivative structure existing at all, but it is an interpretive
identification, not a theorem.

This is a smaller claim than "TEP is a generic dynamical theory," and a much more
secure one. It is of the same character as the framework's other Tier-1/Tier-2
results: a structural identification, grounded in the framework's algebra,
honestly scoped.

---

## Open Questions

**Q1 — The empirical step.** Find a physical system whose dependent state
evolution is a section of the connection bundle. Verify d log Φ/ds = x_a − x_b
against an observed rate. The cleanest candidate is a system with two genuinely
co-evolving budgets driven by a shared parameter; relativistic kinematics
(velocity/time) is the natural first test, since v/c is already a clean
ratio-budget.

**Q2 — The opposite-sign branch. [RESOLVED, Part 4.1.]** The anti-diagonal branch
η_a + s, η_b − s was computed: it is the mirror of the same-sign branch with the
rapidity gap δ replaced by the rapidity sum Σ_0 throughout. The two branches are
the two null directions of the 1+1 Lorentzian metric ds² = dΣ dΔ (Part 4.3),
making the pair of budgets a genuine 1+1 arena — as the question anticipated.

**Q3 — The curvature 2-form and holonomy. [RESOLVED, Part 4.2.]** d(log Φ) is
closed, hence exact; the curvature 2-form of *this object* is identically zero
and its holonomy around any closed loop in the (Σ,Δ) plane is trivial. Φ is a
scalar potential, not a connection with curvature. This is scoped to Φ
specifically: it is not a claim about the framework's boundary-transport
holonomy (the SU(1,1) gluing machinery and conserved boundary-phase-current),
which is a separate and nontrivial matter untouched by this result. The
non-obvious consequence — that *every* construction-formula scalar potential
between independently built budget manifolds is similarly exact, and that this
is the differential-geometric face of inter-manifold multiplicity collapse — is
substantive enough to be treated in a separate companion note rather than here.

**Q4 — The three-term budget route.** Part 1 noted that the other route around
the single-budget obstruction is the three-term budget x² + w + u = 1 from the
passivity decomposition. A derivative hosted in the three-term budget — with the
reflection/harmonic sector w providing the second degree of freedom — was not
developed. If dynamics "lives in the third sector," that would give the harmonic
Hodge sector a dynamical role the corpus has not assigned it. Worth investigating
as an alternative or complement to the paired-budget construction.

**Q5 — Relation to the corpus's Riccati flows.** The paired-budget construction
(Part 3) and the family-specific Riccati flows (corpus) are different objects.
The construction is a comparison between budgets; the Riccati flows are evolution
within a budget under a chosen family. Their precise relationship — whether the
Riccati flows are the construction's restriction to specific sections, or
genuinely independent structure — was not worked out.

**Q6 — The clock function as a dynamical object.** Part 1's corrected lesson —
that a two-term budget's dynamical content lives in its clock dη/dt rather than
in its sector ratio — was established for the damped oscillator but not developed
generally. If the clock function is where single-budget dynamics resides, it
deserves its own treatment: what determines a budget's clock, whether the clock
is itself a framework-native object (a rate of rapidity accumulation), and how
the evolution parameter s of the paired construction relates to the individual
clocks of its two constituent budgets. This is the natural bridge between the
single-budget picture and the two-budget construction, and it was only sketched.

---

*End of addendum. The paired-budget result (Parts 3–4) is the substantive
positive finding; the scoped and retired branches (Part 6) are recorded so the
dynamics thread can be resumed without re-traversing them. The empirical step
(Q1) is the natural next work. The flatness/collapse result flagged in Part 4.2
is developed in a separate companion note.*
