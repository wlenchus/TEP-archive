# Carrier Rung 3, Delta 4 — R3.4 SUCCESS at the dihedral floor: the value register carries, and the carrier is the reduction flow itself; the locator family generalized; the non-abelian machine model answered

**2026-07-24** · Claude (Fable 5), same session · tiers: \[V\] verified this session · \[T\] classical · \[A\] argued · \[id\] · \[C\] · \[O\] · script: `verify/r34e_value_register.py` (runs clean; every grade reproduces)

## 1\. The result \[V; pre-registered outcome: SUCCESS\]

The value-register evaluator was built and graded blind, and it is simpler than the Siegel-unit machinery the spec anticipated. **Carriage path** (never touches the key): from (p, r\_p) alone — lift to the conductor-2 order (r′ \= 2r\_p mod p), form the local chart \[p, 2r′, (r′²+20)/p\] of disc −80, and run the **PSL(2,ℤ) reduction flow** (chart moves T/S only; the group law of Cl(−80) is never invoked). Read the terminal chart among {\[1,0,20\], \[4,0,5\], \[3,2,7\], \[3,−2,7\]} and apply the dictionary gauged by the single datum ψ(𝔭₃) \= \+i ↦ \[3,−2,7\].

**Grades:**

- Nonprincipal split primes vs the FROZEN KEY: **fit zone 6/6; blind zone 9/9** (coincidence space 4⁻⁹ ≈ 4×10⁻⁶).  
- Principal split primes, where the locator predicts actual form coefficients a\_p \= 2ψ: **12/12 against the independently computed η(4τ)η(20τ) expansion** (p \= 29 … 281\) — fully non-circular on both sides.  
- Analytic certificate: j(z\_p) \= j(terminal chart) to 1.4×10⁻³⁵ at a blind prime (PSL₂-invariance); the four chart values are well-separated, with the order-4 pair {\[3,2,7\],\[3,−2,7\]} a complex-conjugate pair.

**The pre-registered R3.4 success condition is met: the deck/value register functionally carries the torsion datum at the dihedral floor. The build branch lives; the structural-no is dead at this floor.**

## 2\. What the carrier *is*, stated plainly \[id, with the mechanism \[T\]\]

The torsion bit ψ \= ±i — boundary-null in every coefficient, null in every marginal, invisible to fields by A₅-simplicity one floor up — is read by **running the chart dynamics to its terminal and observing the chirality of where it lands**: \[3,−2,7\] vs \[3,2,7\] differ by the reflection b ↦ −b; equivalently sign(Im j(terminal)). *Reading without multiplying*: no composition, no ideal arithmetic, no character formula — transport to the fundamental domain and look. In the corpus's own vocabulary this is exact: the PSL(2,ℤ) chart groupoid (the T⁴ \= id cycle's home) transports the p-local port to the terminal chart, and the carried mode is the **orientation of arrival**. Honest classical status: the underlying fact (ring-class characters of conductor-2 orders read off form classes of disc −80; Gauss reduction identifies classes) is classical CFT; what is ours is the verified correspondence under blind protocol (15/15 \+ 12/12 with one gauge datum), the carriage/grading separation, and the characterization of the carrier as reduction *flow* rather than class *algebra* — which is what generalizes.

## 3\. Consequence for Open \#8's fork \[A\]

The fork's floor question is answered: the deck carries, and its carrying mechanism is a **terminal-object locator** — a finite terminal census (4 charts) computable without the answer, a computable contraction flow to terminals, and a discrete read (terminal \+ chirality). What made it possible at this floor: the conductor-2 *order* supplies a finite class set. The icosahedral floor has no CM order — so the climb question is now, precisely: **does an answer-free finite terminal census with a computable flow exist at the icosahedral floor?** The candidate with the right shape is Route A made concrete: at a fixed small prime, the finitely many p-adic families through the weight-1 point — the eigencurve neighborhood — are computable from weight ≥ 2 data alone (mfinit-accessible, no weight-1 tables), and the weight-1 object is located by matching its crossing pair against that finite spectrum. Terminals \= classical-weight family germs; flow \= p-adic interpolation toward the weight-1 boundary; read \= which family pair crosses, and with what orientation. This is the campaign's rung 4 candidate, stated as a locator problem. The structural-no, if it lives anywhere, now lives exactly here: a proof that no answer-free terminal census exists at the boundary of weight space would close the "budget-native" branch for good.

## 4\. The locator family, generalized (Will's request) \[id → protocol\]

Tonight's instrument joins a family the campaign has been building without naming it. **Terminal-object locator, axioms:** (L1) a finite terminal census, computable without the answer; (L2) a computable flow from the object's cheap address data to a terminal; (L3) a discrete read-out: which terminal, plus orientation/chirality data of the arrival. **Instances now held:**

| locator | census (L1) | flow (L2) | read (L3) | floor |
| :---- | :---- | :---- | :---- | :---- |
| trace form (07-24) | Witt classes {parity, marked place} | Gram \+ diagonalization | class \+ marked prime | any A₅ quintic |
| p2\_break census (07-23) | 16 local 16T60 fields | invariant matching | slopes → b \= 3 | wild depth |
| **reduction flow (tonight)** | 4 charts of disc −80 | PSL(2,ℤ) chart moves | terminal \+ chirality → ±i | dihedral torsion |
| FE mirror (07-22/this session) | candidate conductor grid | reflection test at each mirror | the unique flat mirror → N | global capacity |
| crossing gaps (Delta 1\) | {2sin(πk/m)} spectrum | Hecke-polynomial discriminant | class magnitude | shape layer |
| eigencurve locator \[proposed\] | p-adic families from wt ≥ 2 | interpolation to weight 1 | crossing pair \+ orientation | **icosahedral torsion \[O\]** |

Plus the **negative locators** — vanishing theorems that locate where data *is not* (the q-face closure; the field-layer closure): every one of tonight's narrowings is a locator with an empty read-out, and the family's discipline is that both kinds count. Adoption note for the readability protocol (Delta 3 appendix): "locator" is the protocol's instrument column — each ledger row should name its locator and which axiom (L1) census makes it answer-free. Cheap next test of the family's reach \[queued\]: the μ₈ floor — predict η(8τ)η(16τ)'s a\_p \= ±2 signs by the same reduction flow at the conductor-4 order of ℚ(√−2) (disc −128 census), graded against the Delta-3 expansion.

## 5\. The non-abelian machine model (Will's corrected question) \[id, with the separation \[T\]\]

The abelian answer (Delta 3 §F) was lookup: congruence-automatic, space-like, stateless. **The non-abelian side's logical processing is what tonight's run literally performed: computation as flow-to-terminal plus recognition.** No formula in the address data exists — that absence is a theorem (Abel–Ruffini; Klein; at depth ∞ no radical tower) — but a convergent dynamics plus a finite recognition step computes the datum anyway: iterate (chart moves, AGM rungs, p-adic lifting, Newton — the contraction register), terminate in a fundamental domain, recognize the terminal against a census, and read the orientation of arrival. The machine class is **iterate-and-recognize**: an analytic/dynamical oracle composed with census matching (LLL/lindep and j-matching are its read-out primitives — both used tonight). Two sharpenings: (i) **anholonomy \= statefulness** — the non-abelian register is exactly the part of the computation that lives in the *path*, not the endpoint valuation; abelian data costs table space, non-abelian data costs iteration time, and the AGM's quadratic convergence prices that time at one budget-halving per rung (the corpus's T\_lin tower, now as a complexity statement \[id\]). (ii) The ontology and the machine model coincide: "transport to the terminal boundary, then read" is simultaneously the corpus's D↓ reduction ontology and, tonight, a literal algorithm that scored 27/27. That coincidence is the strongest form of the framework's operationalist thesis available to date — and it is graded, not asserted.

## 5b. Equivariance verified — the locator is a torsor map, and that is why one gauge datum sufficed \[V \+ T\]

Conjugation acts on the address torsor by r ↦ p−r (𝔭 ↔ 𝔭̄) and on the answer torsor by inversion (ψ ↦ ψ⁻¹). Verified: the locator intertwines — **nonprincipal terminals flip chirality 16/16; principal terminals are fixed 12/12.** With this, the locator is established as a **G-equivariant map of C₄-torsors**, and the classical lemma applies: *an equivariant map between torsors is completely determined by its value at one point.* That is the formal reason the protocol needed exactly one gauge datum (ψ(𝔭₃) \= \+i) and why the remaining 27 grades were genuine predictions rather than fits — equivariance is the mathematical content; the gauge is one bit; everything else is forced. This is the operational meaning of "torsor-structured multiplicity" (Delta 1 D1, Will): the carrier problem at any floor is *construct an equivariant map and pay one bit* — and the verification burden collapses from "all values" to "the symmetry plus one value."

## 6\. Queue after Delta 4

(1) **Rung 4 opening: the eigencurve terminal-locator** at a small prime (census from weight ≥ 2 spaces; pre-register the crossing-match protocol before computing). (2) The μ₈-floor locator check (§4). (3) The explicit-reciprocity formula rung stays available (fit/blind zones frozen) — now as a *second* carrier at this floor rather than the only hope. (4) The {1,6}/χ₋₂₄ depth check; C1; base-change capacity; Zenodo; the human referee — all standing. Countersign note: §1's success grade, §2's characterization, and §4's protocol adoption gate separately.

*Offered, not self-filed. Session ledger: one pre-registered success condition met blind (9/9 \+ 12/12 \+ one gauge), one carrier identified as a flow rather than an algebra, one instrument family named with six instances and one proposed climb, one machine-model answer that is also a graded exhibit. The fork advances to the boundary of weight space — where the campaign opening always said the real problem lived.*  
