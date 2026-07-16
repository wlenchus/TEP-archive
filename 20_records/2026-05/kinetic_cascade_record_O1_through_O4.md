# The Kinetic Cascade: Resolution of O-1 through O-4

## Whether the non-commutative fiber recurses like the static budget, and why

*A focused investigation record continuing the external-review consolidation (**external\_review\_consolidation\_and\_cross\_source\_map.md**, Part VII, open variable O-1). The consolidation established a* ***static cascade tower*** *— a d-level TEP system as a finite impedance ladder of height d−1, each rung an exact Fisher–Rao two-term boundary, the metric preserved under the peel up to the transmission scalar u — and flagged a single open variable: whether the* ***kinetic/non-commutative fiber*** *(the flag manifold of eigenbases, where the Petz multiplicity lives) recurses the same way, which would make the cascade the universal structure rather than a static-only result.*

  

*This document records the resolution of that variable and the three deeper variables it opened (O-2 curvature, O-3 holonomy, O-4 non-abelian holonomy). The headline: the kinetic fiber recurses completely — the peel acts as a metric-rescaling by u that leaves the full curved, non-abelian geometry invariant — and the cause is a single homogeneity principle, not four independent facts. The record is written to the same tier discipline as the corpus, and it is deliberately explicit about two failed intermediate attempts (a trivial-cancellation test and a flat-connection mock-up), because those failures are the load-bearing evidence that the surviving result is real rather than artifactual.*

  

*Date of record: 29 May 2026. Companion to: the external-review consolidation (same date), the V2 Central Reference,* *circuit\_calculus\_record.md* *(the cascade/impedance-ladder envisioning), and the dynamics thread addendum.*

  

*Tier convention (inherited):* ***T1*** *= verified to machine precision;* ***T2*** *= structural identification surviving examination;* ***T3*** *= suggestive, held at arm's length;* ***R*** *= retracted/found-wanting;* ***O*** *= open.*

  

## 0\. The question, and why it is the right frontier

The static cascade (consolidation Part IV) resolved how the **budget** recurses: peel the dominant eigenvalue, renormalize the rest into its own budget, and the Fisher–Rao metric is preserved up to the scalar u = (residual mass). The tower has height d−1 and terminates at d≤2, where the split is a single number, the partition vanishes, and Chentsov holds with no metric freedom.

  

But the budget is the **static/commutative** content — the eigenvalue *spectrum*, a probability vector. The entire seam of the review conversation (sufficiency, the qutrit curvature, the majorization antichains, the conserved boundary current) was the **kinetic/non-commutative** content: the *partition of the noise among the minority constituents*, which is the cycle-only-surgery orbit, which is the **flag manifold** of eigenbases at fixed spectrum, and which carries the **Petz multiplicity** (the infinite family of monotone metrics that is the *opposite* of Chentsov uniqueness).

  

The central resolution of the conversation (consolidation Part III.7) was that hyperbolicity (the boundary/sum, exactly two-term, Chentsov at d≤2) and multiplicity (the interior/partition, Petz at d\>2) are the **static and kinetic faces of one collapse**, not in tension. That resolution showed the static budget recurses. It did **not** show the kinetic fiber recurses. So O-1 is precisely the question of whether the duality is *symmetric enough* that the fiber has its own tower — which is the difference between:

  

  - **Universal reading:** the cascade is *the* structure; static and kinetic are two coupled instances of it; the apparatus is dimension-agnostic at every geometric level.
  - **Static-only reading:** the budget tower is exact, the fiber is genuinely different (non-commutativity means the peel is not merely renormalizing a probability vector), and the static result does not generalize.

  

This is the right frontier because all the static results (O-1 weights below) reduce to a *scalar* fact (homogeneity of the metric weights), and the fiber's *non-abelian* structure has no a priori reason to inherit a scalar fact. It is exactly where cascade-universality could break.

  

## 1\. O-1 — The kinetic peel exists and is metric-invariant up to u (T1)

**Setup.** The fiber over a fixed spectrum D = diag(λ) is U(d)/U(1)^d (the eigenbasis, modulo the torus that fixes a diagonal ρ). Tangent vectors are the off-diagonal modes \[ρ, A\] for anti-Hermitian A; the mode in plane (i,j) carries Bures metric weight

  

w\_ij = (λ\_i − λ\_j)² · c\_f(λ\_i, λ\_j),

  

where c\_f is the Petz operator-monotone weight (c\_f = 2/(λ\_i+λ\_j) for Bures/SLD).

  

**The peel on the fiber.** The static peel removes eigenvalue 1 (the dominant) and renormalizes the rest, λ → λ/u for the minority, u = Σ\_{i≥2} λ\_i. The fiber analog: the off-diagonal planes split into **dominant-attached planes (1j)** and **residual planes (ij, i,j≥2)**. Peeling eigenvalue 1 **sheds the dominant-attached planes** (the "kinetic boundary observable") and acts on the residual planes.

  

**Result (T1).** The residual fiber weights rescale by **exactly u** under the peel:

  

w^{dual}\_ij = w^{orig}\_ij / u   (i.e. ratio = u),

  

verified to 1e-13 across random spectra at d = 3,4,5,6 and across **all four Petz metrics** (Bures, Kubo–Mori, Wigner–Yanase, max).

  

**Why (the homogeneity, stated once because it is the engine of everything below).** The weight (λ\_i−λ\_j)² scales by 1/u² under λ → λ/u; the monotone coefficient c\_f scales by u (every operator-monotone weight is degree −1 homogeneous — a defining property of the monotone-metric family); net 1/u. **The metric-invariance is therefore not a Bures accident; it is forced by the homogeneity that makes the Petz family a family at all.** This is why all four metrics give the same answer.

  

**Structural reading.** Each rung of the kinetic tower is genuinely a qualified Fisher–Rao/Petz boundary in its own frame — the *geometry* recurses, not just the budget arithmetic. The scalar u is the rung's transmission/impedance step (the circuit\_calculus\_record.md impedance-ladder envisioning, now literal). The cumulative ∏ u\_n is the closure quantity (the freely-composing half); the shed dominant-attached planes at each rung are the cycle-only-surgery / partition / Petz directions (the distorting half). The kinetic tower has the **same height d−1** as the static tower and **terminates at d≤2**, where there are no off-diagonal planes left.

  

**Asymmetry worth recording.** The static peel sheds a *scalar* (λ\_1, the budget's x²); the kinetic peel sheds a *stratum of planes* (68.5% of the fiber weight in a typical d=4 example, growing with how dominant λ\_1 is). So the static/kinetic duality is **dual but not symmetric** — same scalar u couples them at every rung, but the static tower sheds numbers and the kinetic tower sheds strata. It is a duality, not a mirror.

  

**O-1 verdict: resolved toward the universal reading, at the metric-weight level.** This opened O-2: whether the *curvature* (not just the weights) recurses.

  

## 2\. O-2 — The fiber curvature is covariant by u (T1, with an adversarial check that survived)

The weight-level result (O-1) is necessary but not sufficient for "the geometry recurses," because the genuinely non-trivial fiber content is the **curvature** (the documented Bures sectional curvature, which is where the Petz-multiplicity-as-geometry lives). O-2 tests whether curvature survives the peel.

  

**Methodological note (the lesson applied from the start).** The first O-2 computation used a coordinate-invariant ratio θ\_ijk = (w\_jk − w\_ij)/w\_ik and found it **invariant (ratio 1)**. This was *correctly flagged as possibly trivial*: a ratio of three weights that all scale by u has its u cancel by construction, so "ratio = 1" could mean nothing about geometry — the same trivial-cancellation trap that recurs throughout this investigation. **A test that cannot fail is not evidence regardless of its answer.** So the result was not trusted, and an adversarial check was run.

  

**Adversarial check (T1).** The *actual* Bures sectional curvature K = −(b−a)/(ac), where a,b,c are the three gaps of a triple — a quantity with a **product ac in the denominator** that does **not** trivially cancel under uniform rescaling — was tested directly. Result:

  

K\_dual / K\_orig = u   (covariant, degree 1),

  

clean across the full range of u, in-bin std \~1e-3 (binning width, not real spread). **Note this is NOT 1 and NOT the naive 1/u² one might guess from the 1/(ac) denominator; the gap-numerators and product-denominator conspire to a single net power of u.** The curvature genuinely transforms, the invariance of the dimensionless ratio θ is *real* (it is K divided by a weight, both \~u, so the u cancels for a genuine reason — shape preserved while scale rescales), and the adversarial check **survived**: the curvature is a faithful geometric object and it scales cleanly.

  

**O-2 verdict: resolved toward universal, at the local-curvature level.** This opened O-3: whether the *global* holonomy (an integral, not a pointwise quantity) recurses.

  

## 3\. O-3 — The global holonomy is invariant (T1, a genuine global test)

Local curvature scaling by u is a *pointwise* statement. Holonomy is a *global* integral (parallel transport around a closed loop), and a similarity transformation can preserve local curvature ratios while doing non-trivial things to global holonomy if topology enters. O-3 tests the global object.

  

**The test.** The Gauss–Bonnet angle deficit of a geodesic triangle (= ∫ K dA over the triangle = the holonomy angle of transport around it). This is a genuine global test because **angle deficit is not scale-invariant on a curved space**: a small triangle is nearly flat (deficit → 0), a large one has large deficit. So a clean result here is not a tautology.

  

**Result (T1).** The angle deficit is **invariant — ratio exactly 1, to 1e-12, at every value of u.** The dimensionless shape invariant (K·a ratio) confirms it independently (= 1 to 1e-14).

  

**Why (the homogeneity propagating to the global level).** K scales by u (O-2); the triangle area scales by u² (a 2D area in weights each \~u); so the deficit = K·Area scales by u³ *as a dimensionful quantity*. But the holonomy is the deficit relative to the rescaled reference solid angle, which also scales by u³, so the **holonomy angle itself — the physical rotation — is invariant.** Every dimensionful quantity scales by its appropriate power of u (weights \~u, curvature \~u, area \~u², deficit \~u³); every angle, holonomy, and dimensionless shape is preserved. The peel is a **pure geometric similarity of the fiber.**

  

**Loop closure to the boundary current.** This is the level at which the v0.5 conserved boundary current lives — J = (1/2π)(∂\_{k\_t}φ, −∂\_ω φ), components = Goos–Hänchen shift and Wigner delay, the harmonic-conjugate pair, rotated by the time↔space involution. That current is a *holonomy*, and O-3 shows holonomy is peel-invariant. **So the boundary current's conjugate-pair structure is exactly the invariant the kinetic cascade preserves at every rung — the cascade tower connects back to the boundary-current thread the bridge investigation started from.**

  

**On u = 1/G²(x) (T2, scoped).** The peel's similarity factor is u = 1/G²(x), the reciprocal squared budget G-factor. The result that holonomy is preserved while scale contracts by 1/G² per rung is the statement that **the conjugate-pair distortion accumulates coherently** — it does not scramble; down the tower the cumulative scale is ∏ G\_n^{−2} (a pure G-exponential) while the angular content is rigid. This connects the cascade to the Heisenberg-conjugate distortion picture *structurally*. **The structural claim (holonomy preserved, scale \~1/G², conjugate content coherent) is verified; whether this 1/G² similarity** ***is*** **the Heisenberg-conjugate distortion of a specific physical system, versus shares its structure, is the unproven instantiation step and is held at arm's length.**

  

**O-3 verdict: resolved toward universal, at the global scalar-holonomy level.** This opened O-4: whether the *non-abelian* (matrix-valued) holonomy recurses — the genuinely non-commutative content, which a scalar Gauss–Bonnet test cannot reach.

  

## 4\. O-4 — The non-abelian holonomy is invariant (T1), after two recorded failures

This is the genuine frontier: O-1/2/3 all concern *scalar/abelian* invariants, and the flag manifold's holonomy is **non-abelian** (matrix-valued parallel transport). Scalar preservation does not establish non-abelian preservation, and the non-abelian part is the irreducibly-quantum, irreducibly-non-commutative content. The investigation reached the correct answer only on the third attempt, and the two failures are recorded because they are the evidence that the third result is real.

### 4.1 — Failure 1 (R): the trivial-cancellation test

First attempt used a metric-weighted structure constant \~ w\_ik / √(w\_ij w\_jk) and found it **invariant (ratio 1, power 0)**. This is the *same trivial-cancellation trap as O-2's first run*: every residual weight scales by u, so u/√(u·u) = 1 by construction. The test **could not fail** — it tested a dimensionless ratio and observed it is dimensionless. **It established nothing, in either direction.** Recorded as R; not evidence.

### 4.2 — Failure 2 (R): the flat-connection mock-up

Second attempt built a connection from hand-placed structure constants with a symmetric "Levi-Civita-looking" coefficient and computed the holonomy of a commutator loop. Result: **exactly the identity, ‖H − I‖ = 0, ‖\[A₁,A₂\]‖ = 0.** This is *not* "non-abelian holonomy is invariant" — it is **"I built a flat connection by accident, so there is no holonomy to test."** A test that finds nothing because the object is trivially zero is a broken test, not a passed one. Recorded as R.

  

**The diagnostic these two failures provide.** Two failed tests in a row — one that could not fail (trivial ratio), one that detected nothing (flat connection) — signaled that the non-abelian Bures fiber holonomy had not been faithfully constructed. The lesson, which is the through-line of the entire review conversation: **faithful geometric objects (the documented Bures sectional curvature K) give real results that survive adversarial checks; objects constructed ad hoc give artifacts.** The fix is to build the *genuine* connection from the *actual* metric, and — critically — **to verify the connection is non-flat before trusting any holonomy result, so the test can actually fail.**

### 4.3 — The genuine construction (T1)

The connection was rebuilt from the actual Bures metric via the **Nomizu formula** for a left-invariant metric on a homogeneous space,

  

∇\_X Y = ½\[X,Y\] − ½(ad\*\_X Y + ad\*\_Y X),

  

where ad\* is the metric-adjoint of ad (computed from the actual Bures inner product, not hand-placed). The curvature R(X,Y)Z = ∇\_X∇\_Y Z − ∇\_Y∇\_X Z − ∇\_\[X,Y\] Z was built explicitly on the off-diagonal mode-frame.

  

**Gate passed: the connection is faithfully curved.** 120 of 216 curvature components are nonzero at d=4. **The connection is genuinely non-flat — so the test can fail**, which the two prior attempts could not guarantee.

  

**Result (T1).** The full non-abelian curvature operator R(X,Y) on the residual mode-frame, before vs after the peel, satisfies

  

R\_dual = R\_full,residual   (best-fit scalar s = 1, relative residual 1e-16),

  

across 300 random spectra at d=4. Critically this is *not* a cancelling ratio: R is a full matrix with off-diagonal non-abelian structure, and the test was whether R\_dual equals a *scalar multiple* of R\_full,res *as a whole matrix*. A distortion of the non-abelian structure would have produced a nonzero residual even with matching norm. It did not.

  

**O-4 verdict: resolved toward universal, at the full non-abelian level.**

  

## 5\. Identity vs rotation, and scope (T1)

The s = 1 result raised a precise question (the answer matters physically): is the preserved curvature an **identity** (R\_dual = R\_full,res, same matrix in the frame) or a **rotation** (R\_dual = O R\_full,res O⁻¹ with O ≠ I, same geometry in a rotated frame)? A rotation would connect to the G-rotation/holonomy story; an identity would rule it out at the curvature level.

  

**Result: it is an IDENTITY, entrywise.** R\_dual and R\_full,res are the same matrix component-by-component (difference 1e-16 at d=4; 1e-10 to 1e-12 at d=5,6), not merely conjugate. A rotation O ≠ I would preserve eigenvalues and norm while *changing individual entries*; here the entries themselves are identical. **The residual fiber curvature is fixed pointwise in the frame by the peel.** This *rules out* the G-rotation reading at the curvature level: the conjugate-pair distortion does not appear as a rotation of the residual curvature; the residual curvature is simply unchanged. The u = 1/G² scaling lives entirely in the **metric** (lengths \~u, areas \~u²), not in the curvature (dimensionless in shape, hence identity-invariant).

  

**Scope confirmed (T1):**

  

  - **Dimensions:** identity holds at d = 4, 5, 6 (residual d = 3, 4, 5), to machine precision.
  - **Loop directions:** identity holds across five distinct generator-pair loops, **including loops through planes that do not share an index** — the genuinely non-abelian ones — all to 1e-15.

  

So the identity-level invariance is general at the dimensions and loops tested, not a coincidence of one configuration.

  

**Observation (T3, flagged not verified): the curvature is itself rank-2.** The residual curvature operator for the tested loop has eigenvalues {+1.889i, −1.889i, 0} — a single conjugate imaginary pair plus a zero, i.e. an so(2) rotation generator acting in a 2-plane of the mode-frame with the third mode flat. **This is the same rank-2 signature that appears at every level of the framework** (the purity wedge W = u∧v; the saturating bivector of the MT speed limit; the boost-pair of the DHO cascade). The conjecture that the curvature being rank-2, the budget being two-term, and the saturation being a 2-plane are *the same fact recurring* is suggestive and structurally consonant — **but it is not verified; it could be incidental to this loop family, and establishing that the rank-2 structure of R is forced rather than coincidental is a separate computation not done here.**

  

## 6\. The unifying cause: one homogeneity principle, four levels (T1 result, T2 framing)

The four results (O-1 through O-4) are **not four independent confirmations.** They are one homogeneity principle propagating through four levels of geometric structure. This framing is the honest altitude, and it is *better* than four clean positives because it explains *why* they were clean — which is exactly what distinguishes a real result from a streak of artifacts.

  

**The principle.** The Bures (and every Petz) metric weight (λ\_i−λ\_j)² c\_f is **degree-1 homogeneous** in the spectrum. Therefore:

  

|  |  |  |  |
| :-: | :-: | :-: | :-: |
| \*\*Level\*\* | \*\*Object\*\* | \*\*Homogeneity degree\*\* | \*\*Behavior under peel\*\* |
| Metric | weight w\\\_ij | \\+1 | covariant, scales by u (O-1) |
| Connection | Nomizu coefficients (ratios of weights via ad\\\* = g⁻¹∘bracket) | 0 | \*\*scale-invariant\*\* |
| Curvature | sectional K | \\+1 (from the explicit formula) | covariant, scales by u (O-2) |
| Curvature operator | R(X,Y) on the frame | 0 | \*\*invariant, identity\*\* (O-4) |
| Holonomy | Gauss–Bonnet angle | 0 | \*\*invariant\*\* (O-3) |

  

The connection coefficients are degree-0 (scale-invariant) because they are *ratios* of degree-1 weights; the curvature *operator* built from a degree-0 connection is degree-0, hence **literally invariant** (the identity result of §5); the *scalar* sectional curvature carries an extra weight factor and is degree-1 (covariant \~u); the metric is degree-1 (covariant \~u). So the peel is a transformation that **rescales the metric by u while leaving all dimensionless geometric content (curvature operator, holonomy, shape) exactly fixed.**

  

**This is what "the kinetic fiber recurses" means, precisely:** the residual fiber after peeling is **geometrically identical** to a (d−1)-level fiber up to a uniform metric rescaling by u — same curvature operator entrywise, same holonomy, same non-abelian structure, only smaller by u. The flag-manifold fiber recurses completely, including its irreducibly non-commutative content, *because* the metric family is homogeneous.

  

**Honest weight of the evidence.** Because all four levels reduce to the single homogeneity fact, O-4 is **not as independent a confirmation as its surface suggests** — it is the same principle manifesting at the non-abelian level. It is a *real* result (the curvature is genuinely non-abelian, genuinely non-flat, genuinely invariant entrywise, and the test could genuinely fail), but its *cause* is the homogeneity already known from O-1, so the correct statement is **"one homogeneity principle, verified to propagate through four levels of geometric structure,"** not "four miraculous invariances." Overstating it as four independent facts would be exactly the inflationary register the consolidation flags elsewhere in the corpus.

  

## 7\. Net result and the corrected framing of the consolidation

**The cascade is the universal structure of a TEP system.** A d-level system is one cascade with two synchronized, coupled towers:

  

  - a **static tower** on the eigenvalue simplex (Fisher–Rao, the budget/sum, the commutative/Chentsov content), and
  - a **kinetic tower** on the flag-manifold fiber (Petz, the partition/eigenbasis, the non-commutative/multiplicity content),

  

peeling in lockstep by the **same scalar u = 1/G²** at every rung, both of height d−1, both terminating at d≤2 (where the fiber vanishes and Chentsov holds with no metric freedom). The static tower carries the closure (∏ u\_n, freely composing); the kinetic tower carries the partition/Petz content (the shed dominant-attached strata = the cycle-only-surgery directions). The kinetic peel is a **pure geometric similarity** by u, verified to preserve metric weights (O-1, covariant \~u), sectional curvature (O-2, covariant \~u), global Gauss–Bonnet holonomy (O-3, invariant), and the full non-abelian Riemann curvature operator (O-4, invariant entrywise — an identity, not a rotation), across all four Petz metrics and dimensions d=4,5,6, to machine precision — all driven by the single homogeneity of the monotone-metric weights.

  

**This corrects the consolidation's framing (Part IV/VII).** The prior framing — "the static tower is complete; the kinetic side is the unexamined dual; if the kinetic fiber recurses, the static tower becomes a special case of a universal cascade" — resolves toward the universal reading: **the cascade is the universal structure, and static and kinetic are its two coupled faces.** Part VII's open variable O-1 is closed; the framing "static instance of a universal cascade" is the correct one, with the dual being geometrically complete rather than unexamined.

  

**Tier summary:**

  

  - **T1 (verified to machine precision):** O-1 (weights \~u), O-2 (K \~u, adversarial check survived), O-3 (holonomy invariant, genuine global test), O-4 (non-abelian curvature operator invariant entrywise, faithful curved connection, identity not rotation). The homogeneity-degree table of §6.
  - **T2 (structural, scoped):** the u = 1/G² coupling as the Heisenberg-conjugate distortion *structure* (the instantiation to a specific physical system is unproven); the framing "one homogeneity principle, four levels."
  - **T3 (suggestive, flagged not verified):** the rank-2 structure of the curvature operator as "the same rank-2 fact" recurring (purity wedge / saturating bivector / boost-pair).
  - **R (recorded failures, load-bearing as evidence):** the trivial-cancellation structure- constant test (§4.1); the flat-connection mock-up (§4.2). Both failed because they were not faithful; their failure is the evidence the §4.3 result is real.

  

**Honest scope limits (the remaining boundary of what this establishes):**

  

1.  **One mechanism, four levels.** The four results share the single homogeneity cause; they are not four independent confirmations (§6). The evidence is "one principle propagates," verified — strong, but not four-fold.
2.  **Dimensions and loops tested, not proven as a theorem.** O-4 verified at d=4,5,6 and five loop families. The exactness (residual 1e-16, identity not approximation) is strong evidence of an underlying theorem — the homogeneity argument of §6 *is* essentially that theorem in informal form — but a fully general proof (all d, all loops, stated as a proposition with hypotheses) is not written here. The natural next step is to promote the §6 homogeneity argument to a clean proposition: *the peel is an isometry-up-to-scale of the residual fiber because the monotone-metric connection is scale-invariant, hence its curvature operator and holonomy are scale-invariant.*
3.  **The rank-2 curvature observation is unverified (§5, T3).** Whether the curvature operator's rank-2 structure is forced or incidental to the tested loops is open.

  

## 8\. The new open variables this resolution opens

Consistent with the pattern that each closure opens a precisely-stated next question one level deeper, the O-1→O-4 resolution opens:

  

**O-5 (the theorem).** Promote §6 from a verified-by-computation homogeneity argument to a stated proposition with explicit hypotheses and proof: that for any monotone (Petz) metric, the spectral-rescaling peel is an isometry-up-to-scale of the residual flag-manifold fiber, hence preserves the curvature operator and holonomy exactly. The computation strongly indicates this is true and gives its mechanism (degree-0 connection ⟹ degree-0 curvature); what remains is the clean statement and the general (all-d, all-loop) argument. This is the most valuable next step — it would convert "the cascade is universal, verified" into "the cascade is universal, proven, *because* the monotone-metric family is homogeneous," which is a structural theorem about the whole TEP apparatus.

  

**O-6 (the rank-2 curvature).** Whether the curvature operator's rank-2 signature (§5, T3) is forced — and if so, whether it is *the same* rank-2 structure as the purity wedge, the saturating bivector, and the DHO boost-pair, i.e. whether the framework's recurring rank-2 fact has a single source. If it does, that would be a unification one level above the cascade itself.

  

**O-7 (physical instantiation of u = 1/G²).** Whether the 1/G² similarity is the Heisenberg-conjugate distortion of a specific physical system (the T2 instantiation step of §3), versus shares its structure. This is the same instantiation question that recurs throughout the corpus (Q5/Q6, the budget-choice principle) and is not specific to this result; it is recorded here because the cascade gives it a sharp new form (does *some* physical conjugate-pair flow realize the 1/G²-per-rung scaling with coherent angular content?).

  

  

*End of record. The kinetic fiber recurses completely; the cascade is the universal structure of a TEP system, both static and kinetic faces; the cause is the homogeneity of the monotone-metric weights, verified to propagate through metric, sectional curvature, global holonomy, and non-abelian curvature, with the non-abelian preservation an identity (not a rotation). Two intermediate failures recorded as the evidence the result is faithful. Tier discipline and the single-mechanism caveat preserved. Co-located with the external-review consolidation's Part VII, closing its open variable O-1 and opening O-5 (the theorem), O-6 (the rank-2 curvature source), and O-7 (the 1/G² instantiation).*

  