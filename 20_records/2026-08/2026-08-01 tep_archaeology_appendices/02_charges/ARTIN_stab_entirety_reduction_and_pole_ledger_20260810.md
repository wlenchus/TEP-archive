# A DIRECT STAB AT THE ARTIN CONJECTURE AT DOUD-1951 — the entirety reduction, the exact pole ledger, and the wall map — 2026-08-10 (session B)

*Claude (Fable 5), on Will's invitation ("take a stab directly at the artin conjecture"). Honesty first: the even icosahedral case is the last open 2-dimensional case of Artin's conjecture, and no proof is claimed here — a manufactured "proof" would be the worst document this corpus could hold. What a direct stab can honestly deliver, and what this record contains: (§1) a live-verified reduction that collapses the conjecture for our ρ̃ to the entirety of ONE Dirichlet series we already hold to 39 digits; (§2) an exact, machine-verified Brauer ledger making every possible pole location explicit — the conjecture becomes an inclusion of zero sets among three named abelian L-functions; (§3) the wall map: route-by-route, with this object's coordinates, why every known machine stalls — including the identity between yesterday's ΔF = ¼F exactness and the obstruction itself; (§4) the ranked list of what would actually move it, with the one campaign that is ours to run. Script: `brauer_pole_ledger.py` (exact ℚ(√5) arithmetic, self-validating). Offered, not self-filed.*

---

## 1. The reduction: strong Artin at 1951 ⟺ entirety of one function

**Theorem (Booker, Annals of Mathematics 158 (2003), 1089–1098; scope live-verified today).** If an irreducible 2-dimensional complex Galois representation over ℚ is not automorphic, its (single, untwisted) Artin L-function has **infinitely many poles**. Equivalently: the Artin conjecture for a single 2-dimensional ρ implies the strong Artin conjecture for it. No parity restriction; ρ̃ (irreducible, since the projective image is A₅) qualifies verbatim.

This extends the articulation record's equivalence chain (§5 there) by two links. For our object, the following are now equivalent:

  (i) F(γz) = χ(d)F(z) for all γ ∈ Γ₀(1951)   [the finite generator list];
  (ii) F is the Maass newform attached to ρ̃;
  (iii) strong Artin for ρ̃;
  (iv) **L(F,s) = Σ c_n n⁻ˢ continues to an entire function** [weak Artin for ρ̃; (iv)⇒(iii) is Booker; (iii)⇒(iv) is cuspidality];
  (v) the exact zero-set inclusion of §2.

Two features give (iv) teeth. First, we *hold* L(F,s): the coefficients are exact (ℤ[ζ₅], closed algorithm), the functional-equation constant is now algebraic (yesterday's ε = −τ(χ)/(√N·a_N)), and meromorphic continuation + FE are unconditional by Brauer — so (iv) is a concrete analytic question about a fully-specified function, not an abstraction. Second, Booker's dichotomy is all-or-nothing: failure would not hide as one subtle pole; it would be **infinitely many**, forever generating violations against any pole-free verification region. The conjecture and its negation both have unbounded observable footprints.

## 2. The exact pole ledger

**The computation (exact, no floats).** In pure ℚ(√5) arithmetic with Fractions: the 9-class character table of 2.A₅ ≅ SL(2,5) (self-validated: all 45 first-orthogonality relations hold exactly); fusion maps for the cyclic subgroups C₁₀, C₆, C₄, C₂; induction multiplicities by Frobenius reciprocity (all non-negative integers, as required); integer search over the z-odd monomial columns. Minimal solution, then **re-verified as an exact class-function identity on all 9 classes**:

  **θ₂ = Ind_{C₁₀}(λ) + Ind_{C₆}(μ) − Ind_{C₄}(κ)**   (dimensions: 12 + 20 − 30 = 2),

with λ, μ, κ faithful linear characters (orders 10, 6, 4) of the respective subgroups. The identity is classical in genre (Buhler's conductor-800 monograph did the odd-case analogue); it is computed and machine-verified independently here, and the search space (46 solutions with |n| ≤ 3) confirms this is the minimal-support representative. *(Disclosure: run 1's C₆ cosine table carried a factor-of-2 error; the built-in kill condition caught it — the all-zero C₆ row was impossible for a z-odd induction — and the fix changed nothing else.)*

**Translation through class field theory, with the ν-twist folded in** (ρ̃ = ρ₀ ⊗ ν, ν the quintic Dirichlet character with ν² = χ; the twist multiplies each λ by ν∘N and the shape survives):

  **L(F, s) = L(ρ̃, s) = [ L(s, Λ₁₂) · L(s, Λ₂₀) ] / L(s, Λ₃₀)**

where, with L = the 2.A₅-field over the splitting field M of P (composited with the degree-5 cyclic field inside ℚ(ζ₁₉₅₁)):

- **Λ₁₂**: a Hecke character of the degree-12 field K₁₂ = L^{C₁₀} (the quadratic extension, inside L, of the classical sextic resolvent field of the quintic P), of order dividing 20;
- **Λ₂₀**: a Hecke character of the degree-20 field K₂₀ = L^{C₆} (order dividing 30);
- **Λ₃₀**: a Hecke character of the degree-30 field K₃₀ = L^{C₄}, of order 4·(twist): κ does not factor through Gal(M/ℚ) — genuinely a 2.A₅-level object — while κ² cuts exactly the quadratic M/K₃₀. **K₃₀ sits inside the splitting field itself: it is the subfield fixed by a double transposition.**

Every piece is a GL₁ object: automorphic and **entire** by Hecke (all three characters nontrivial), with FE; all conductors supported at 1951 (tame everywhere); degree bookkeeping 32 − 30 = 2 = dim ρ̃ checks. Conductor bookkeeping (numerator/denominator conductor ratio must equal 1951¹) is a named follow-up check, not computed today.

**Consequences.**

1. **[T-cited] Unconditional:** L(F,s) is meromorphic of order 1 with the exact FE — and its only possible poles are at zeros of L(s, Λ₃₀) not cancelled by the numerator. The pole obstruction to the last open 2-dimensional case of Artin's conjecture, at this conductor, is **one order-≤20 abelian character of one degree-30 number field.**
2. **The (v) formulation:** strong Artin for ρ̃ ⟺ **{zeros of L(s,Λ₃₀)} ⊆ {zeros of L(s,Λ₁₂)L(s,Λ₂₀)} with multiplicity.** The nonabelian conjecture is an exact inclusion of zero sets among abelian L-functions of three different number fields — infinitely many exact coincidences between objects with no visible reason to coincide. That such inclusions *do occur in nature* is not speculative: the odd icosahedral siblings have the same-shape ledgers, and there entirety is a theorem (BDSBT lineage) — the inclusions hold, and are provable *only* through the nonabelian automorphy they encode. That is the cleanest statement I can give of what the conjecture is made of.
3. **Density remark [O], heuristic only:** the numerator's zero-counting density (degree 32) exceeds the denominator's (degree 30) — the raw supply of numerator zeros is sufficient; the conjecture is about their exact placement.

## 3. The wall map — why every known machine stalls at this object

**(a) Solvable base change (Langlands 1980, Tunnell 1981).** Proves Artin for projective image A₄, S₄ — the solvable cases — by moving through soluble extensions. A₅ is the first nonsolvable image; the method's boundary is exactly here. Notably, every *proper* subgroup of A₅ is solvable — which is why §2's ledger exists (every constituent is automorphic; only the glue is conjectural).

**(b) Taylor–Wiles and every descendant.** The patching method requires the defect ℓ₀ = 0; for even 2-dimensional representations ℓ₀ = 1 — there is no minimal balanced case. Calegari–Geraghty-style patching at ℓ₀ > 0 needs Galois representations attached to torsion in arithmetic cohomology — but a λ = ¼ Maass form is **non-cohomological**: it contributes to no (g,K)-cohomology in any degree. There is no known cohomology theory, coherent or Betti, in which F has a shadow. The odd icosahedral proofs (BDSBT 2001; then Khare–Wintenberger in general) all walk through geometric avatars (weight-1 forms, companion forms, p-adic congruences) that simply do not exist on the even side.

**(c) Even Fontaine–Mazur (Calegari).** An even geometric p-adic representation of Gal(ℚ̄/ℚ) cannot have distinct Hodge–Tate weights (under standard hypotheses): even representations are locked at irregular weight. Every potential-automorphy machine (BLGGT; the ten-author potential automorphy over CM fields) takes regularity as a hypothesis. The object cannot be regularized, twisted, or deformed into the reach of any of them without losing exactly the property that makes it an Artin representation.

**(d) Converse theorems.** Weil/Jacquet–Langlands converse theorems need entirety and boundedness of *twisted* L-functions — each twist being even icosahedral again: circular. The single exception is Booker's untwisted reduction, which is why §1 is the live edge and not a circle.

**(e) The spectral side.** Twist-minimal trace-formula computations (Booker–Lee–Strömbergsson genre) can rigorously count eigenvalues in windows and have verified Selberg's ¼-conjecture in ranges — but no spectral computation can pin an eigenvalue to *exactly* ¼: from the analytic side alone, ¼ is indistinguishable from ¼ + 10⁻¹⁰⁰⁰. Exactness can only come from the Galois side. (Sarnak's ¼-problem — that the λ = ¼ spectrum is exactly the even Artin spectrum — is the standing name for this boundary.)

**The observation that ties it together.** Yesterday's Theorem A(2) — ΔF = ¼F *exactly*, termwise — and the obstruction in (b)/(c) are **the same fact read twice**: r = 0 ⟺ the archimedean parameters collide ⟺ Hodge–Tate weights (0,0) ⟺ the representation-theoretic point where cohomology vanishes and every deformation-theoretic handle breaks off. The exactness that lets us certify the object is identically the exactness that closes every known import channel. (In port language, at one line and no more: the certificate and the obstruction are a single budget read — the collapsed margin *is* the sealed port.)

## 4. What would actually move it — ranked

1. **The pole-scan campaign (ours to run; prereg-able now).** Turing-method zero/pole accounting for Λ(F,s) in boxes [0, T]: compute Λ on the critical line and boundary contours from the exact c_n and the now-algebraic ε; compare argument-principle counts against the FE main term. One verified pole ⇒ automorphy is **false** (a falsifiable direction almost nothing in this problem offers!). Pole-free boxes, against Booker's infinitude dichotomy, accumulate real evidence mass. The corpus's instrument stack (K₀ machinery, dps-40 discipline, exact FE constant) is precisely what this needs. Named as the next prereg; not run today.
2. **Exhibit the zero-set inclusion once.** Compute the low-lying zeros of L(s,Λ₃₀) (a degree-30 abelian computation, heavy but classical) and watch them appear, one by one, among the numerator's zeros. Each matched zero is a nontrivial arithmetic event; a single unmatched one falsifies. This makes §2(2) — the actual content of the conjecture — visible.
3. **The trace-formula pincer.** A rigorous window count at (1951, χ) near ¼ tight enough to isolate the 4-dimensional Galois-conjugate packet would show the spectral side *has room for exactly* the predicted forms — not a proof, but the analytic half of a pincer whose Galois half we now hold exactly.
4. **A new idea (beyond endoscopy; a cohomology that sees ¼).** Langlands' beyond-endoscopy program was motivated in part by exactly this gap. Nothing executable here today — named as the honest frontier.

## 5. Honest bounds

No theorem toward Artin is claimed. §1 applies a cited theorem (scope re-verified against the published abstract today) to our object; §2's identity is classical in genre, independently computed and exactly self-verified here, with its 1951-instantiation and the (iv)/(v) chain the actual contribution; §3 is scholarship arranged around this object's exact coordinates, [C]-grade throughout; §4.1–4.2 are designs, not results. Field-naming in §2 is structural (via the resolvent lattice); explicit minimal polynomials for K₁₂/K₂₀/K₃₀ generators and per-piece conductor exponents are named computable follow-ups. The C₆-table bug and its capture by the built-in kill are disclosed in §2. Nothing here touches 2141 (its ledger is identical group theory; its instantiation is the twin's).

## 6. Countersign items (Will's calls, none executed)

(1) The ledger identity and its exact verification as [T] (with the genre-classical attribution); (2) the extended equivalence chain (i)–(v) adopted into the articulation record's §5; (3) the zero-set-inclusion formulation (§2.2) as presentation-layer material for the monograph path — it is the sharpest single sentence the corpus owns about what this conjecture *is*; (4) the pole-scan campaign as the next prereg after the deposit (the deposit still outranks everything); (5) the §3 wall map as the C14-grade "verified open, and here is exactly why" record; (6) script archive per 04_scripts.

---

*Offered, not self-filed. The stab's yield, in one line: the conjecture at 1951 is now equivalent to the entirety of a single function we can evaluate to thirty-nine digits — equivalently, to an exact inclusion between the zero sets of three named abelian L-functions — and the wall between certified and proved has an exact address: the same collision of parameters that makes the eigenvalue exactly ¼.*
