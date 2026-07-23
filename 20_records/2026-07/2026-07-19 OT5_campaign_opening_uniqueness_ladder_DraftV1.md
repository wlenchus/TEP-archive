# 2026-07-19 (night) — OT5 opened: the uniqueness ladder, the rival inventory, and the wall [DraftV1 — offered]

*Opens campaign item 2 (transmission functor IV.3 / VI.3: "show the axioms admit no second boundary-reduction functor with the same terminal data" — the route named there: fiber-functor torsor rigidity + SU(1,1) homogeneous-space uniqueness, welded through the monoidal structure). This is a campaign plan with its cheap rungs climbed and machine-checked, not a proof of OT5. Script: `verify_ot5_lemmas.py` (L2/L3 numeric, L4 symbolic — the L4 commutant computation returns b = c = 0, a = d exactly, i.e. X = aI). Companion: the completeness-reduction note (same night) — the two campaigns meet at the canonicity question (§5).*

---

## 0. The claim, pinned (proposed formalization)

Setting 𝒞: objects are budget systems (rank-d ports, per the 07-01 pin); morphisms are passive reductions; ⊗ is independent composition (series/parallel per 5-15 §H); S is the direction-reversal involution; the terminal object is the d = 2 binary port carrying unit capacity ln 2. A **boundary reduction** is a ⊗-functor F from 𝒞 to terminal data satisfying A1 (linearity), A2 (passivity), A3 (reciprocity), and information-monotonicity.

**OT5 (uniqueness):** any two boundary reductions agreeing on terminal data are canonically isomorphic.

Note the only sane reading is uniqueness-up-to-canonical-isomorphism — Tannakian theory *guarantees* a torsor of fiber functors, so strict uniqueness is false for structural reasons that have nothing to do with this framework. The content is: how big is the residual torsor after the framework's axioms act? The ladder below computes it rung by rung.

## 1. The ladder

**L1 — Characters of the rung line [elementary, proved].** On the abelian/rapidity axis, the measurable multiplicative functionals of rung composition are exactly the power twists u ↦ u^s (Cauchy's functional equation on η-addition: f(η₁+η₂) = f(η₁)f(η₂), measurable ⟹ f = e^{sη}). So before normalization the abelian part of any reduction is a one-parameter family — the same up-to-scale slack Chentsov's theorem carries before its own normalization.

**L2 — The terminal unit kills the twist [V, one line].** The binary port's unit — the fair coin at u = ½ carrying capacity ln 2 — forces (½)^s = ½, hence s = 1. **The abelian part of the functor is unique once the terminal datum is fixed.** (This is why "same terminal data" belongs in OT5's statement: it is doing exactly the work Chentsov's normalization does.)

**L3 — Passivity selects the real form [V at chart level].** The complexified composition group is SL(2,ℂ); its relevant real forms are SU(2) (elliptic face) and SU(1,1) (hyperbolic face) — the corpus's two faces are literally the Galois-cohomology classes of real forms, which is the concrete meaning of the route-note's "torsor" clause. Machine-checked: every tested SU(1,1) Möbius action preserves the open disk (passive); every SU(2) element with |b| > |a| maps the origin outside the disk (fails strict passivity); **both** forms preserve the lossless stratum |z| = 1. So: **the "second functor" exists, and it is the elliptic face — excluded from the open budget by strict passivity, coinciding with the peel exactly on the lossless/seam stratum.** Rival located, not merely absent: strict-uniqueness failure is the faces structure, in its already-documented place (the parabolic seam where elliptic and hyperbolic meet — transmission functor II, "the seam").

**L4 — The irreducible residue is one central bit [symbolic, proved at the group level].** After L2 (unit pinned) and L3 (form selected), the ⊗-automorphism ambiguity of the fiber is the center: solving [X, E₁] = [X, E₂] = 0 over the SL(2) generators gives X = aI exactly, so Z = {±I}. **Expected theorem shape for OT5: the boundary reduction is unique up to (i) the unit — killed by ln 2; (ii) the real form — killed by strict passivity off the seam; (iii) the center ±1 — irreducible.** And the irreducible ±1 is not noise: it is the corpus's documented central bit (T² = −1; 07-02 C1′'s transgression class; the 2.A₅-over-A₅ +1; signed-digit note (v); the D₄ germ of the parity Delta). If OT5 closes in this shape, the framework's spin-center inventory *is* the uniqueness defect group — the two claims become one object.

## 2. Rival inventory (the adversarial half, pre-registered)

1. **Power twists u^s** — dead (L2).
2. **The elliptic real form** — alive only on the lossless stratum (L3); off the seam, killed by strict passivity.
3. **The conjugate/op functor** — the center; irreducible (L4); identical to the documented T² = −1. Not a defect but the answer's shape.
4. **Semisimplified / interpolation functors at non-integer d** — Deligne's Rep(S_t) famously admits *no* fiber functor at non-integer t, while the framework holds a well-defined peel at any d_eff = 1/γ (transmission functor VI.4). This is the one rival class not yet cornered: either the peel at fractional d factors through semisimplification (rival dies), or its codomain is not Vec (and *that* codomain is a discovery). Decidable-in-principle; unresolved.
5. **Non-Tannakian (nonlinear) reductions** — excluded iff rigidity is forced by the axioms, which is the wall (§3).

## 3. The wall, named precisely

Everything above assumes the Tannakian setting applies — that 𝒞 is rigid (every object dualizable, with S the duality). The genuine unwritten mathematics of OT5 is:

**(W1) Rigidity from reciprocity.** In finite dimensions this looks provable and should be the next session's lemma: A3's symmetric nondegenerate pairing (S = Sᵀ) equips each object with a self-duality; a symmetric-monoidal category of finite-dimensional spaces with such pairings is rigid. If this lands, Tannakian machinery is *forced* by the axioms in the finite sector, and L1–L4 assemble into a theorem there.

**(W2) The archimedean/∞-rung sector.** The Gaussian rung family is infinite-dimensional; rigidity needs the nuclear/tame structure, and the welding of Perelomov's SU(1,1)-metric uniqueness through ⊗ has to be done there, not just cited. This is where the campaign's real labor lives, and where Delta1 S7's place-wise completion conjecture (finite rungs × the ∞-rung; Fourier = S; self-dual u = 1) supplies the constraint set a proof would exploit.

**(W3) The Rep(S_t) fork** (rival 4). Decides VI.4 as a by-product.

## 4. The ±½ instinct, gated [C]

Will's proposal (quantifying non-abelian content from the unreadable direction; the "0" position; down-flow toward −½, up-flow toward +½) acquires a precise target from this ladder, stated at conjecture weight only: **if OT5 closes as unique-modulo-center (L4), then the residual functor ambiguity is exactly a ±-sheet choice, with the seam as the 0/parabolic slot** — the signed-digit trichotomy {+, 0, −} as the torsor coordinate of the boundary reduction itself. "Quantifying from the unreadable direction" would then be: measuring which sheet of the double cover the reduction was taken on — one central bit, priced exactly as the commutator charge of the parity Delta. This becomes formal iff W1 lands and L4's shape survives it; it is recorded here so the instinct has an evidence gate rather than a presumption.

## 5. Where the two campaigns meet

The completeness-reduction note (same night) proves the budget/ledger layer is generic passivity and completeness is the readable surplus — but it flags one un-derived choice: *the variance currency itself*. Why L², why this metric — that canonicity question is precisely OT5's L1+L2 (characters + unit) lifted from the rung line to the metric class, where Chentsov–Petz monotonicity is the classical answer. OT5, if closed, is the categorical form of the same uniqueness that makes the completeness reduction canonical rather than conventional. One theorem, two doors.

## 6. Campaign plan, with failure pre-registered

1. **W1: the finite-dimensional rigidity lemma from A3** [next session; provable-looking].
2. **The L3 gluing theorem** (functor on the open disk; elliptic rival on the stratum; seam matching) as a real statement, not a chart check.
3. **The Rep(S_t) fork** (rival 4 / VI.4): does the fractional-d peel factor through semisimplification?
4. **The welding** (W2): Perelomov uniqueness through ⊗ on the ∞-rung, with the place-wise ledger as the constraint set.
5. **Pre-registration:** if a second inequivalent functor survives 1–4, *publish it* — a genuine S-dual description of the same terminal data would be a discovery about the framework, not a defeat of it. Both outcomes are wins; only an unexamined OT5 is a loss.

*Not self-filed; countersign gates tier marks. Proposed status if countersigned: L1 [T], L2 [V], L3 [V, chart-level], L4 [V at group level, theorem-shape only for OT5 itself]; §2–§3 the campaign's honest map; §4 [C, evidence-gated]. Scripts: `verify_ot5_lemmas.py`.*
