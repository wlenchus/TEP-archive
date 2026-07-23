# 2026-07-19 (night) — The completeness reduction, adjudicated: passivity is generic, completeness is the readable surplus [DraftV1 — offered]

*Opens campaign item 1 (concerted assessment §5.1). The recorded question (6-20 delta, item b; interior spine §11.1; transmission functor IV.1): does measure-completeness alone force linearity, passivity, reciprocity, and information-monotonicity? Adjudicated here in the classical case with explicit hypotheses per the III.5 discipline ("a chain of conditionals reading as unconditional" is the documented hazard; every hypothesis is therefore surfaced). Script: `verify_completeness_reduction.py` — 9/9 [V], finite-space exact at 1e-12. Quantum case fenced with citations, not proven.*

---

## 1. Setup

Probability space (Ω, F, P), observable Y ∈ L²(P), WLOG Var(Y) = 1 after centering/scaling. An **interface** is a linear map T on observables. Two nested classes:

- **Passive interface:** T positive, unital (T1 = 1), and state-preserving (E[Tf] = E[f]). Operational reading: the interface neither manufactures signal nor moves the state. (Finite model: row-stochastic M with stationary p.)
- **Complete interface:** a passive interface whose record is statistically sufficient for Y's statistics.

Budget entries: x²_T = Var(TY), u_T = E[T(Y²) − (TY)²].

## 2. Theorem P (genericity: passivity alone) [V + three-line proofs]

For **every** passive interface T:

**(P1) Budget, exact.** Var(TY) + u_T = Var(Y).
*Proof.* Var(TY) + u_T = E[(TY)²] − E[TY]² + E[T(Y²)] − E[(TY)²] = E[T(Y²)] − E[TY]² = E[Y²] − E[Y]² (state-preservation, twice). ∎

**(P2) u_T ≥ 0.** Jensen pointwise: (TY)² ≤ T(Y²) for positive unital T (Kadison–Schwarz in the quantum lift). ∎

**(P3) Monotonicity.** Passive maps are L²-contractions (E[(TY)²] ≤ E[T(Y²)] = E[Y²]), so along any composition x²_{Ψ∘Φ} ≤ x²_Φ ≤ 1. ∎

**(P4) Ledger chain rule, exact.** u_{Ψ∘Φ}(Y) = u_Φ(Y) + u_Ψ(ΦY).
*Proof.* Insert-and-cancel: E[ΨΦ(Y²) − (ΨΦY)²] = E[Ψ(Φ(Y²)) − Ψ((ΦY)²)] + E[Ψ((ΦY)²) − (ΨΦY)²]; the first bracket = E[Φ(Y²) − (ΦY)²] by state-preservation of Ψ. ∎

**Consequence (the deflationary half, stated plainly):** the budget identity, its non-negativity, its monotonicity, and its telescoping ledger are **signatures of passivity, not of completeness**. This is the two-line theorem behind "identity, not discovery" and behind the budget's ubiquity: *any* passive interface budgets. The load-bearing hypothesis is state-preservation — the [V] counterexample T-F (an idempotent, positive, unital averaging with the wrong weights) breaks the budget outright.

## 3. Theorem C (the completeness surplus) [V for the separations; MRD/HS cited]

For a passive interface T, the following are equivalent (finite case; general σ-finite case with standard care):

(a) **Repeatable and reciprocal:** T² = T and T is self-adjoint in L²(P);
(b) **Conditional expectation:** T = E[·|B] for a sub-σ-algebra B — the Moy–Rota–Douglas characterization of positive unital contractive projections;
(c) **Pythagorean/readable form:** Y = TY ⊕ (Y − TY), record orthogonal to residual;
(d) **u is the honest error:** u_T = E[(Y − TY)²] — the budget's noise entry equals the mean-square error of the record;
(e) **Sufficiency:** the record is sufficient (Halmos–Savage factorization face; Petz-recoverability / saturated DPI in the quantum lift).

Verified separations [V]: for the CE, u = MSE exactly (T-D1); for a generic passive T the budget holds while u ≠ MSE (T-D2) — the interface still *budgets* but its noise entry is no longer the error of any readable record.

For chains of complete interfaces (filtrations) [V]: refinement monotonicity; the waste identity u(B₁) − u(B₂) = ‖R₂Y − R₁Y‖²; spend telescoping with orthogonal increments (T-E) — U1's "per-rung ledger is chart, the total is invariant" is Doob's martingale-increment orthogonality, and asymptotic sufficiency is Lévy upward convergence. (Variance-currency spend is bounded by 1; the corpus's unbounded capacity is the log-currency lift — Gaussian face, capacity-audit record.)

## 4. Verdict on the recorded claim

**The reduction is TRUE, with a refinement that sharpens it.** "Completeness forces linearity, passivity, reciprocity, monotonicity" — yes, via (e) ⟹ (b) ⟹ everything, and with hypotheses now explicit (L² finiteness; state-preservation; measurement-as-conditioning enters only in *naming* the complete class). But three of the four properties were already forced by passivity alone (Theorem P); the surplus that completeness uniquely adds is **repeatability + reciprocity ⟺ readability (u = MSE)**. One axiom buys the budget world; the *second* axiom — sufficiency — characterizes the readable subclass of it. The framework's two-tier structure (generic budget everywhere; readable records only at complete interfaces) is thereby a theorem pair rather than a posit.

**A new operational handle falls out:** (d) is a *checkable certificate of completeness*. For any real interface, compare the budgeted noise entry u against the measured record error E[(Y − TY)²]; equality certifies sufficiency, and the gap u − MSE... (sign and magnitude) quantifies the interface's incompleteness in budget currency. This is a could-have-failed instrument, cheap, and to my knowledge not previously stated in the corpus as a test.

## 5. Quantum fences (stated, not proven here)

Conditional expectations onto a von Neumann subalgebra exist iff the subalgebra is modular-invariant (Takesaki); where they exist, §§2–3 lift in the Hilbert–Schmidt/linear-entropy metric with Kadison–Schwarz replacing Jensen — exactly the corpus's recorded fence (06-28 §L: ρ = u exact for linear entropy, false for von Neumann). Sufficiency ⟺ Petz recoverability ⟺ saturated DPI (Petz). The classical adjudication above is complete; the quantum statement inherits the Takesaki gate and nothing worse.

## 6. Queue

(1) Write the HS-metric quantum case in full (the chain rule should be the same three-liner under Kadison–Schwarz). (2) Develop §4's completeness certificate (u vs MSE) into an audit-protocol item — it is a new falsifiable instrument. (3) Log-currency lift of P4 (KL-waste vs variance-waste; join to the two-ledgers trichotomy). (4) Canonicity of the variance currency itself — why *this* metric — is the Chentsov leg, which is the companion OT5 note's territory: the two campaign items meet exactly there. Scripts: `verify_completeness_reduction.py`.

*Not self-filed; countersign gates tier marks. Proposed status if countersigned: §2–§3 classical, theorem-grade [V+T]; §5 [T, cited]; §4's certificate [new instrument, unrun].*
