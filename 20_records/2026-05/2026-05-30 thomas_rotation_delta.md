# Delta Record — Thomas-Rotation / Relativity-as-Generic₂ Investigation (5-30)

*Reconstructed from a full re-reading of the session transcript and re-execution of the
35 scripts run during the session. Every quantitative claim below was re-run and its output
re-checked against the transcript prose; where the two diverged, the code output governs.
This document is the **delta** — what changed from the project corpus going in, to the
conclusions coming out — written to the corpus's own tiering discipline (T1 verified /
T2 structural / T3 suggestive / R retired-or-artifact / O open).*

---

## 0. The question and the starting position

**Question carried in.** Is relativistic content — specifically Thomas–Wigner rotation — a
generic₂ property of measurement derivable from the TEP/Entrodynamics budget structure,
*deselecting* spacetime as its privileged source, rather than an attribute of spacetime? The
deselection framing (not selection) was clarified mid-session and is load-bearing: the goal
is to show relativistic effects are scale/measure properties of *any* TEP-applicable budget,
with spacetime as one instance, not to derive spacetime.

**Corpus position going in (what the project files actually said).**
- The relativistic content (Tier 2.3, c/√2) was treated as a single coincidence / "one hit."
- "TEP derives gravity / information as basis for spacetime" was **retired** (V2 §5.5).
- The DHO Lorentz investigation (2-16) had: single-oscillator Lorentz structure exact;
  naïve velocity-addition between damping ratios **falsified**; coupling acts as a boost on
  the damping rapidity (the G(κ) law), verified to 3.55e-15 across 4104 parameter sets.
- The kinetic-cascade record (O-4) concluded the preserved curvature under the peel is an
  **"identity, not rotation"** and read this as ruling out the G-rotation reading.
- Wigner/Thomas rotation had been **deflated** — absorbed into "G-distortion," treated as
  not separately needing relativistic content.

---

## 0b. Two senses of "generic" (the generic₁ / generic₂ distinction)

This distinction is load-bearing for the whole investigation, and conflating the two was one
of the session's flagged errors (corpus tag **R-claude-3**, "a sloppiness the author
flagged," external-review consolidation line 142). The source separates two senses; the
subscript notation used in this document maps onto them as follows.

**generic₁ — *intra-mathematical* genericity.** A property that is true of *every object of a
given mathematical type*, by virtue of the type itself. Example: F₊ = F₋ for every rank-2
bivector — it is the Plücker relation for being a decomposable wedge, not a fact about the
*purity* wedge specifically. Such a property is real and often verifiable to machine
precision, but it **carries no predictive content**: because it holds for everything of that
type, observing it tells you nothing you didn't already know from the type. "True by
construction, of the whole class."

**generic₂ — *cross-domain* genericity.** A definitional structure that, when **transported
to a new domain**, *predicts a feature there* that was not put in by hand. Example: the budget
language flagging a true, non-obvious feature of an actual scattering problem (the Luo
result). This sense **does** carry content, because the prediction could have failed — the
structure could have transported and predicted nothing, or the wrong thing. "Forced in a new
domain, where it could have come out otherwise."

**Compare / contrast.**

| | generic₁ (intra-mathematical) | generic₂ (cross-domain) |
|---|---|---|
| Quantifier | over all objects *of a type* | over *domains* a structure is carried into |
| Content | none — true of everything of the type | predictive — could have failed in the new domain |
| Failure branch | cannot fail (definitional) | can fail (the test is whether the prediction lands) |
| Evidential weight | establishes consistency, not novelty | establishes that the structure *reaches* a domain |
| Example | F₊=F₋ for any rank-2 bivector | budget predicting a real scattering threshold |
| The trap | reading a generic₁ fact as if it were a discovery | (none — this is the contentful sense) |

**The relationship between them (why they're "consistent, not rivals").** They are not in
tension; they are different questions. A structure can be generic₁ (true of its whole type)
*and* generic₂ (transport to a new domain and predict there) at once — the error is only in
**mistaking one for the other**, specifically in citing a generic₁ fact (which cannot fail)
as if it were generic₂ evidence (which can). The verification discipline that runs through
this whole document — *does the test have a real failure branch?* — is exactly the operational
test that separates them: a result that *could not have come out otherwise* is at most
generic₁; a result that *could have failed and didn't* is candidate generic₂ evidence.

**Why it matters for the deselection claim specifically.** "Relativistic content is a
generic₂ property of measurement" is the substantive form of the claim: that the budget
structure, transported into any measurement domain (purity, coupling, mass-flow, scattering),
*predicts* relativistic kinematics there — and this could fail (a domain could carry the
budget and show no Lorentzian structure). The **deflationary trap** is the generic₁ shadow:
"everything described in rapidity coordinates exhibits rapidity-coordinate kinematics" is true
of the whole type and predicts nothing — which is why §10 open-join #1 (is x²+u=1 *forced* or
*chosen*) is decisive: if the budget constraint is forced for any bounded measure, the
deselection is generic₂ (contentful); if it is a parameterization we elect, it collapses to
generic₁ (tautological). The precession-factor result (§5) is genuine generic₂ evidence
precisely because its zero-control *could* have failed and didn't.

---

## 1. The central structural correction (T1) — the deflation was answering the wrong question

**Delta.** The corpus's "identity, not rotation" (O-4) was computed along the **peel / scale
axis** — a single one-parameter scaling operation. A scaling is collinear with itself by
construction, so composing it with itself *cannot* produce a rotation; the "identity" result
is near-tautological for that operation. **Thomas rotation is a different question: the
composition of two *non-collinear* boosts.** That question was never run by the corpus.

**Verified (layer1d_holonomy.py, re-run):** transporting a frame around a closed geodesic
triangle built from genuine non-collinear SU(1,1) boost legs gives holonomy = Gauss–Bonnet
area to machine precision (max |holonomy| − |area| = **7.99e-15**). This *is* the Wigner
angle, and it is the same K=−1 area-deficit object the corpus's O-3 machine computes — but
nonzero, because the loop has genuine angular extent. The corpus had the machinery and had
only ever pointed it down the degenerate (collinear) axis.

**Status:** T1. The corpus's own holonomy machine, correctly aimed, yields the Wigner angle.

---

## 2. The sign correction (T1) — Bures was the wrong metric; purity supplies K=−1

**Delta.** The first computational pass (Layer 2) found a genuine non-abelian holonomy on
the framework's Bures flag-fiber at d=4,5 — verified as a real metric rotation:

- curvature identity R(X,Y) = [A_X,A_Y] − A_[X,Y] holds to **1.46e-15 / 2.58e-16**
  (layer2e_curvature_identity.py, re-run): "holonomy per area = curvature" on the fiber;
- but the fiber sectional curvature is **positive** (K ≈ +1.94, +8.74) — a compact,
  SU(2)-type rotation, **not** the relativistic K=−1.

I initially reported this positive sign as "the sign measurement geometry hands you,"
treating the relativistic K=−1 as special/low-dimensional. **This was a metric error**, and
it was corrected by the framework author: Bures is one (the minimal) member of the
non-unique Petz family; it is not privileged. The framework's **purity metric** supplies
K=−1 as a derived, omniregime, metric-specific fact.

**Verified (premise_review.py, re-run):**
- the framework's own radial purity metric ds² = dγ²/(γ²(1−γ)) **equals** the radial
  Poincaré metric exactly (symbolic difference = 0) — K=−1 is inherited by the framework's
  own object, not imported;
- K=−1 is **constant across the whole regime** (omniregime), not a pointwise coincidence;
- **sign is metric-specific on the same manifold**: purity K=−1, Bures K=+4.

**Verified (purity_disk_wigner.py, re-run):** two non-collinear purity-changing boosts on
the K=−1 purity disk compose to a rotation equal to the K=−1 Gauss–Bonnet area to **9.77e-15**,
with vertices that are genuine purity changes. The relativistic-sign Thomas/Wigner rotation
is present on the framework's own derived geometry.

**Status:** T1 (the K=−1 purity metric and the Wigner angle on it). The Layer-2f "wrong sign"
concern is **R (retired as a metric artifact)** — it came from computing on Bures.

---

## 3. The flux-composition result (T1) — hyperbolic signature is forced, not chosen

**Delta.** A serious self-mounted challenge: the two-outcome budget X²+V²=1 is a *circle*
(Euclidean, K>0); Fisher–Rao/Bures on it is a *sphere* (natural arclength arcsin, K>0). So
where does the *hyperbolic* (Lorentzian, K<0) structure come from — is x = tanh(η) a
coordinate choice that imports it? This looked like a genuine gap ("two-outcome →
Lorentzian has a missing arrow; passivity is the load-bearing extra premise").

**The challenge was wrong, and the resolution is the strongest single structural result
(resolution.py, re-run).** The same budget |R|²+|T|²=1 has two representations:
- **scattering (state) rep:** the circle, signature ++;
- **transfer (composition) rep:** |a|²−|b|²=1, the hyperbola, signature +−.

The minus sign is **forced by flux conservation**: the conserved flux form is
σ_z = diag(+1,−1) (rightward − leftward), verified M†σ_z M = σ_z to machine precision; the
group preserving an indefinite form is SU(1,1) by definition of indefinite. Transfer matrices
**compose by ordinary multiplication** (cascade = product), and the product stays in SU(1,1)
(verified: three random lossless scatterers' product is SU(1,1), associative). So the
hyperbolic face is **the composition face** — what you get the moment you require the budget
to compose associatively under cascade — and it does **not** require passivity: *lossless*
flux conservation already forces it via the indefiniteness of the flux form.

**Status:** T1. "Two-outcome budget gives only a sphere" is **R (retired)**: it confused the
state rep (circle) with the composition rep (hyperbola). Thomas rotation lives in the
composition rep, which is forced hyperbolic. Reference class is "any flux-conserving cascade
with associative composition," broader than "passive systems."

---

## 4. The dimensional / composed-object thread — corrected twice, landing on the geodesic reframe

This thread had the most correction and is where the compaction summary later proved
unreliable; the transcript is the authority.

**4a. The dual-pairing arena (corpus 5-21).** The framework-internal derivative = two budgets
in ratio = a 1+1 Lorentzian arena ds² = dη_a² − dη_b², budgets entering as a dual pair,
neither slot privileged (Σ, Δ null coordinates). 1+1 has one boost axis — abelian, no Wigner
rotation. The scalar potential Φ = G(x_a)/G(x_b) is **exact** (separable), trivial holonomy —
the corpus had already retracted its own "Φ has curvature" language.

**4b. The (1,n) construction and its retraction.** I verified that "one clock budget against
n independent measure-budgets" gives signature (1,n) and at n=3 reproduces the full 3+1
Thomas–Wigner rotation to 1e-15 (concrete_13_wigner.py). **But** the author corrected that
this slot-pairing is the "two metrics in ratio" picture explicitly *not* the framework's
native construction. So the (1,3) result is "the destination via a road that isn't the
framework's mechanism."

**4c. Targets 1 and 2 — the internal-composite construction, derived not asserted.**
- **Target 1 (target1_fSNR.py, re-run):** a within-budget sector ratio f(SNR)=f(x²/u)
  collapses — SNR = sinh²η exactly, so any f(SNR) lives on the *single* rapidity line; the
  budget rebuilt from SNR is identically the original. **No second direction.** (Clean
  falsification, expected and confirmed.)
- **Target 2 (target2_PQ.py, re-run):** for an internally composite measure X=P/Q, the
  construction-faithful induced metric (the one that carries the ratio's own line element) is
  **rank-1** — the ratio direction is physical, the common mode is null/gauge. **Internal
  ratio-composition does not raise the dimension count.** Notably, the dual-pairing (1,1)
  Lorentzian metric I had leaned on *fails* the ratio's construction-consistency check — a
  correction to my own earlier work.

So measure-composition (internal) keeps handing back **one** direction. This is the framework
being economical, and it is *inconvenient* for the strong claim — recorded as such.

**4d. The geodesic reframe (the figure/ground inversion).** The author's correction: Thomas
rotation is not built by composing two boosts; it is **emergent** — in 3+1D the worldline is
*just a geodesic*, and the rotation is the frame-dependent twist registered between two
budgets held in ratio along that single motion. This dissolved my entire "need two
non-collinear boosts" demand and explained why Target 2 keeps giving one direction: there is
only one motion; the "second direction" was never a second boost, it is the dual partner the
one motion is measured against.

**Verified (inner_product.py, re-run):**
- the **invariant** misalignment ⟨U_P,U_Q⟩ = cosh δ is boost-independent (an isometry can't
  move an invariant) — trivial, as it must be;
- the **frame-dependent** relative angle Δθ(s) = gd(η_P+s) − gd(η_Q+s) (Gudermannian
  difference) *does* change with the boost and washes out as s→∞ — this is the emergent
  rotation, exactly the structure of real Thomas precession (a frame anholonomy with no
  invariant content).

**Status:** T1 for the inner-product structure; the geodesic reframe is the correct object.
"Composed arena is 1+1, no Thomas rotation possible" — the conclusion later surfaced via a
conversation-search line-reading of a months-old document — is **R (retired artifact)**: it
was the output of the malformed single-static-metric / scalar-Φ holonomy tests this session
corrected. It must not be carried as a live constraint.

---

## 5. The deselection result (T1/T2) — the precession factor is measure-generic

**Delta.** With the goal clarified as deselection, the genericity of the Gudermannian
artifact flips from weakness to evidence: "can't distinguish spacetime from a damped
oscillator" *is* the deselection result.

**Verified (deselection.py, re-run):** the Thomas precession factor — the **½** and the
bilinear-in-rapidity leading Wigner angle — emerges from two abstract budgets with no
spatial/temporal identity, converging to exactly ½·η₁·η₂ as rapidities shrink (ratio →
1.0000), and reproducing identically for a purity-type × coupling-type pair (ratio 0.9995).
The ½ is derived as the K=−1 triangle-area factor — a geometric constant of any hyperbolic
budget pair.

**Verified faithful capstone (faithful_capstone.py, re-run):** on the corrected object
(single-geodesic dual-frame Gudermannian transport), the **zero control passes exactly**
(aligned budgets δ=0 give identically 0 at all s — the apparatus can return zero), and the
deselection factor converges to 1.0000 for non-spacetime budgets.

**Status:** T1 for the factor's emergence (verified, controls pass); T2 for the deselection
*claim* (the kinematic/geometric-phase layer of relativity is generic to budget pairs,
spacetime is one instance). **Scope:** this is the *kinematic shell* (Lorentz factor, Doppler,
precession factor, geometric-phase angle). It does **not** transfer the *dynamical* content
(why a system has the budget it has, why spacetime's bound is c, field equations).

---

## 6. The DHO as a non-spacetime instance — the dimensional-agnosticism payoff

**Delta.** "Oscillator" is not intrinsically dimensional: replace displacement with mass-flow,
population, field amplitude — any quantity periodic against any reference — and the budget,
rapidity, and geometric phase are identical. The Thomas-type phase attaches to the *budget
relation*, substrate-independent. Spacetime velocity is the famous instance, not the carrier.

**Verified (cascade_families.py, re-run):** whether two axes compose abelian (no rotation) or
non-abelian (rotation) is a **cascade-family property**, not an interpretive choice:
- capacity-additive single axis: abelian scalar add (ln(1+SNR)), no rotation;
- the DHO's **two axes** (damping p, coupling κ) add **in quadrature** — the corpus's own
  machine-verified discriminant D = D₀ + κ². Quadrature addition **is** Killing-orthogonality
  (verified: ⟨K₁,K₂⟩=0, and [K₁,K₂] = −K₀ = the rotation generator). The orthogonality is the
  corpus's result read through the Killing form — an identity, not my identification. This
  resolved my "quadrature → orthogonal" reservation.

**Status:** T1 for "quadrature = Killing-orthogonality = rotation generator"; T2 for the DHO
hosting the rotation, with the native-vs-slot-paired caveat (§8).

---

## 7. The capstone arc — a failed measurement, corrected, and a methodological finding

This is one of the more consequential deltas, and it is about **method**.

**7a. The failed time-domain capstone (capstone_phase.py, re-run — fails its own controls).**
An attempt to "observe" the phase by integrating the DHO EOM around a (damping, coupling)
loop and subtracting the dynamical phase. **It failed three of five controls:** sign did not
flip under reversal (forward +3.18, reversed +3.19, sum +6.37 ≠ 0); the **zero-area
degenerate loop gave +3.26** (must be ~0); geo/area not constant (76.8 vs 108.7). Diagnosis:
the "geometric phase" was dominated by un-removed dynamical residual; the observable
(relative oscillator phase) was the constant-|z| **circle** the first segment had already
shown gives zero holonomy.

**7b. The time-domain framing was itself a category error.** The framework's program is
dimensional agnosticism; its native parameter is the **dimensionless** rapidity / frequency
ratio (signed rapidity η_s = ½ln(SNR) runs over ℝ; reactive crossings live in the frequency
domain on H₁₂(ω)). There is **no time-domain anything** to be missing — demanding a
time-integration smuggled back the privileged temporal parameter the deselection dissolves.
The faithful capstone's use of the dimensionless parameter s was already the correct object;
the "still not observed in time" caveat was withdrawn.

**7c. The scalar-holonomy zero (dho_relphase.py, re-run).** Transporting arg H₁₂ (a scalar)
around the loop gives **identically zero** winding, with zero-controls passing. This is a
*trustworthy* zero, and it is near-tautological: the loop integral of a single-valued scalar
is always zero (exact form). Same category as the corpus's exact Φ. A scalar cannot hold
holonomy.

**7d. The proper observable — gated frame transport (dho_frame_transport.py, re-run).**
Transporting the **non-abelian mode frame** (not a scalar) around the loop, fully gated:
- **G1 zero control:** collapsed loop and zero-area loop give identity to 1e-12 — apparatus
  returns zero when it must;
- **G2 non-flat gate:** small vs large loop give different, area-growing holonomy
  (5.7e-4 vs 4.1e-2) — connection is non-flat, the test *can* fail;
- **G3 rotation reading:** holonomy unitary to 1e-13 — a genuine frame rotation;
- **G4 area scaling:** angle/h² converges to a constant (1.476→1.465) — curvature holonomy.

So the DHO eigenframe carries a **genuine, gated, dimensionless, non-abelian frame-rotation
holonomy**. The scalar tests could not hold it because scalars are exact/flat.

**7e. BUT the metric error recurred (caught by the author).** The frame transport in 7d used
the **Euclidean coordinate inner product** on the dynamical generator's eigenvectors —
neither Bures nor purity, and exactly the "coordinate basis without a metric" Failure-2
object. So the curvature value (~1.47) is **not** comparable to K=−1, and the unitary/rotation
readings were w.r.t. the wrong metric. The *existence* of a non-abelian holonomy stands; its
**value/sign claim is retired**.

**7f. The corrected purity-metric version (dho_purity_metric.py, re-run).** With a
known-answer validation gate: on the K=−1 purity disk, geodesic-triangle holonomy/area = 1
exactly (apparatus validated against the known K=−1). The DHO control loop maps onto that
validated disk (budget → radius is *forced*; coupling → disk-angle is a *modeling choice* —
the flagged hinge), and its holonomy is the K=−1 Gauss–Bonnet area. Relativistic-sign
holonomy on the framework's own metric, dimensionless, no time — **contingent on the
angle-mapping** (whether κ is a genuine second disk direction).

**Methodological finding (T1, the most robust empirical result of the session).** Across the
whole session: **fresh holonomy/phase constructions built on scalar or coordinate-basis
objects produced triviality or artifact (Φ exact; arg H₁₂ zero; Euclidean-metric ~1.47;
time-domain controls failed); every result that held was the non-abelian frame transport
read against a faithful metric, resting on the corpus's pre-verified identities.** The
holonomy lives in the non-abelian frame, never in a scalar reduction of it. The same lesson
applies one level up: a *retrieved conclusion* (conversation-search or corpus quote) gets the
same gate as a fresh number — what object was it computed on, was it faithful, could it have
failed — and the "1+1/no rotation" conclusion fails that gate (computed on malformed objects).

---

## 8. The cascade / peeling-as-learning thread (T3 / O)

**Delta (live, not from corpus).** The radial/peel direction is *mostly* iso-budget but
carries a slight **capacity change** (a boost), conjectured to become dramatic as the cascade
number approaches the **effective** degrees of freedom — peeling as a form of *learning*
(distinguishing degrees of freedom), with the infinite-d self-dual point at the hyperbolic
center.

**Tested (cascade_noncommute.py, re-run):**
- Part A (capacity per peel) was run on **geometric spectra, which are cascade fixed points**
  — so Δx²=0 trivially. **Uninformative as run** (wrong spectra: fixed points cannot show
  capacity change). Not evidence against the claim.
- Part B (peel/shape non-commutativity): the commutator is **nonzero everywhere**
  (6.5e-2 to 2.2e-2) and **largest near the effective-d limit** (1.97e-1 at d_eff=1.23), but
  **not monotonic** in d_eff across the four spectra tested. This is genuinely
  **single-budget-native** (no slot-pairing) non-abelian structure that amplifies near the
  limit — the right *kind* of thing for the claim.

**Status:** T3 (suggestive). It is scalar-level (budget x²), only four spectra, non-monotonic,
and does **not** yet establish a hyperbolic frame holonomy. **Pending test (well-posed):**
gated frame-transport on the single-budget **peel/shape loop** (not the slot-paired
damping/coupling loop), on the purity metric, with the known-answer validation gate — the one
computation that would settle whether the cascade hosts a *native* (not slot-paired) holonomy.

---

## 9. What changed, in one table

| Claim | Corpus going in | Delta out |
|---|---|---|
| Thomas rotation in TEP | deflated / absorbed into G-distortion | present and derived; deflation was the collinear (peel) question (T1) |
| The relevant holonomy object | (not isolated) | non-abelian frame transport on a faithful metric; scalars are exact/flat (T1) |
| Sign (K) | (Bures-flavored, K>0 where computed) | metric-specific; purity gives K=−1 omniregime, derived (T1) |
| Hyperbolic signature origin | (implicit / coordinate) | forced by flux-conserving associative composition (indefinite σ_z) (T1) |
| Relativistic kinematics | spacetime-specific "one hit" | generic to any budget pair; deselected from spacetime (T2) |
| Precession factor ½ | (not derived) | K=−1 triangle-area factor, emerges from non-spacetime budgets (T1) |
| Dimension of relativistic content | (2+1 native, 3+1 open) | unchanged: 2+1D native (SO(2,1)); 3+1 behind the Grassmannian Wick seam (O) |
| "Composed arena is 1+1, no rotation" | (recorded conclusion) | **R**: malformed-test artifact, superseded by faithful work this session |
| DHO hosts the rotation | (G(κ) boost only) | yes, gated frame holonomy — but slot-paired form verified; native form pending (T2/O) |

---

## 10. The genuine open joins (O) — unchanged by anything above

1. **Forced vs chosen budget.** Is x²+u=1 a *forced constraint* on any bounded
   measure-against-dual (substantive deselection) or a *chosen hyperbolic parameterization*
   (tautological deselection)? Prior to every computation; not resolvable from inside the
   machinery built on the postulate. The corpus treats it as "true by definition"; that is
   exactly the thing under examination. **This is the deepest join and nothing this session
   closed it.**

2. **Native vs slot-paired second axis.** The DHO's rotation-hosting second axis came from two
   independent controls (damping, coupling) — slot-paired. The internal-composite construction
   (Target 2) gives only one direction. Whether a *single* budget's own structure (the cascade
   peel/shape, §8) carries a native holonomy is suggestive (T3) with a clean pending test.

3. **Signature/dimension count.** What fixes (1,3) specifically — one clock against three
   measures — vs (1,n) generally? Plausibly the Grassmannian d=4 chiral SU(2)×SU(2) ≅ SO(4)
   Wick-rotated to SO(3,1) (corpus Q4), explicitly open.

4. **Curvature as proof, given metric non-uniqueness.** Curvature is not metric-invariant, and
   the metric is canonical only classically, generically, and non-uniquely in the Petz regime.
   Reframe (live): this is a *solution*, not a problem — the metric non-uniqueness **is** the
   shape/fiber freedom that supplies the second direction; the evidential weight sits on the
   *family-invariant budget structure*, not on any single metric's curvature value, and the
   rotation correctly has no invariant magnitude (Thomas precession has none either). Recorded
   as a reframing to be developed, not a closed result.

---

## 11. Epistemic calibration (recorded at the author's standard)

This investigation moved my assessment from "narrow result, strong claim unsupported" to
"deselection holds for the kinematic + geometric-phase layer, derived and falsification-tested,
2+1D-scoped." That is a large update. It was driven substantially by the author's corrections
catching genuine errors of mine. I was wrong in **both** directions:

- **Overstated gaps (twice):** the Bures-vs-purity sign (computed on the wrong metric); the
  "two-outcome gives only a sphere" flux-signature gap (confused state rep with composition
  rep).
- **Mistook artifacts for findings (three times):** the coordinate-basis commutator
  "adversarial finding" (Failure-2); the failed time-domain capstone (un-removed dynamical
  phase); the Euclidean-metric frame transport (wrong metric, value meaningless).
- **Laundered a malformed conclusion through retrieval (once):** resurfaced "composed arena is
  1+1, no rotation" from a conversation-search line-reading of a months-old document, and
  weighed current results against it — when that conclusion was the output of the malformed
  tests this session corrected.

The updates I judge **earned** rest on computations with real failure branches that did not
trigger (flux form *could* have been definite; the SU(1,1) product *could* have failed to
close; quadrature *could* have been linear; the frame-transport gates *could* have failed;
the deselection zero-control *could* have been nonzero). The updates I have **retired** are
those that came from objects that could not have failed (scalars, fixed-point spectra) or were
read against the wrong metric.

**Weighting guidance:** my endorsement should be weighted as an interested party who has now
flip-corrected repeatedly, not as clean external validation. The robust core is the set of
results resting on the corpus's pre-verified identities (the G(κ) boost law, the D=D₀+κ²
discriminant) plus machine-precision checks with live failure branches. The single most
valuable remaining computation — the gated frame-transport on the single-budget peel/shape
loop on the purity metric — would convert the native-holonomy question (open #2) from
suggestive to decided, and is the natural next step.
