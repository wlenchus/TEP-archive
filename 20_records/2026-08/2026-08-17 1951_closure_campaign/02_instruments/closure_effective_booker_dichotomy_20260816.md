> **STATUS HEADER (curated pack, 2026-08-17).** This record's route (FV(T₀) with Lemmas M and CT_fin) is **superseded as the campaign's frontier** by the winding reduction in `closure_integer_read_localization_20260816.md`: M(M1) is eliminated outright, CT_fin is absorbed into the one-witness statement (W), and M(M2) shrinks to the localized repulsion Δ(T₀). Retained as the effective route's ledger and for **COH**, which remains an equivalent form of strong Artin at 1951. Its citation layer inherits the same Weil → Jacquet–Langlands repair noted on the winding record.

---

# CLOSURE attempt — effective Booker dichotomy for the even icosahedral ρ̃ of conductor 1951 — 2026-08-16

*Session external to both August lineages. Charge: prove an effective version of Booker's pole dichotomy for the two-tile class, extract T₀, or locate the missing lemma exactly. All cited statements re-verified against sources this session (Annals PDF, Booker's Bristol page, ar5iv, Compositio/IMRN/BLMS pages). Offered under claude/; not self-promoted to charges/.*

## 0. Verified inputs (exact statements)

**Booker 2003** (Ann. of Math. 158, 1089–1098), verbatim: *Theorem.* "If some twist L(s, ρ⊗χ) of L(s,ρ) by a Dirichlet character χ has a pole then L(s,ρ) has infinitely many poles." *Corollary.* "If L(s,ρ) is not automorphic then it has infinitely many poles. In particular, the Artin conjecture for ρ implies the strong Artin conjecture for ρ." Even case gamma factor γ(s) = π^{−s}Γ((s+a)/2)², a ∈ {0,1}; FE γ(s)L(s,ρ) = εN^{1/2−s}γ(1−s)L(1−s,ρ̄). Machine: additive twists L(s,ρ,α) = Σ aₙe(−nα)n^{−s}; Lemma 1: for α ∈ ℚ these are meromorphic, poles only in 0 < Re s < 1, and are ratios of entire functions of order 1 (via Brauer). The finitely-many-poles hypothesis enters as convergence of the residue sum (his eq. (2)) feeding the bounded side; the rotation parameter δ "controls poles with imaginary part between 0 and about 1/δ"; a hypothetical pole of the additive twist at β+iτ gives divergence Ω_ε((1/δ)^{β+m−n−1/2−ε}) against remainder O_ε((1/δ)^{m−n−1/2+ε}) — the polar signal beats the regular side by exactly δ^{−β}, β ≤ 1. *Remark 2* (verbatim): "…the result is ineffective as it depends on the location of a hypothetical pole of L(s,ρ,α) (which probably does not exist!)."

**Booker 2006** (Turing paper, math/0507502): A₅ is "almost monomial" (his Prop. 2.3), so pole-freeness in a box is verifiable by an integer-valued zero census (Heilbronn characters + Turing's method) — no residue magnitudes needed. His p. 15 names the missing effective statement: an effective converse theorem "requiring, say, meromorphy of all twists and holomorphy of a finite number in a bounded region."

**Booker–Krishnamurthy**: Compositio 2011 (relaxed ramified twists), BLMS 2013 (restricted pole sets among unramified twists; Eisenstein cases), IMRN 2014 ("allowing the twists by non-trivial Dirichlet characters to have arbitrary poles"). None reduces the twist set to finitely many moduli.

## 1. Theorem R (unconditional, effective; proved)

Let Ξ_ψ := λ·(ψ∘N_{K₁₀}) for ψ primitive mod q, (q,1951)=1; Q_λ = 1951⁸, Q_μ = 1951⁹.

**R1 (polar rigidity).** Poles of L(ρ̃⊗ψ) lie in Z(L(Ξ_ψ)); poles of every additive twist L(s,ρ̃,t/q) lie in ⋃_{ψ mod q} Z(L(Ξ_ψ)) ∪ (finitely many explicit local-factor zeros on Re s ∈ {0} ∪ [−½,½]·(log-scale), from imprimitive ψ). Candidate polar sites are effectively enumerable: the charge's "unknown polynomial P" of Booker's genre has degree ≤ N_λ(T), explicitly bounded (R4).

**R2 (uniform no-Siegel; new, clean).** For every ψ with (q,1951)=1, Ξ_ψ is non-real. Proof: (Ξ_ψ)² = λ²·(ψ²∘N). If trivial, then λ² = ψ̄²∘N; K₁₀ is ramified only at 1951, so every p|q is unramified in K₁₀ and the local norm N(O_v^×) = ℤ_p^×, whence ψ²∘N is ramified at p exactly when ψ² is; comparing conductors (1951-power vs coprime-to-1951) forces ψ² unramified everywhere, so ψ² = 1 and λ² = 1 — contradicting ord(λ) = 4. ∎ Hence **no exceptional (Siegel) zero occurs anywhere in the entire twisted family**: one uniform effective constant c₀ serves all q.

**R3 (funnel).** Every pole s₀ = β+iτ of every L(ρ̃⊗ψ) satisfies β ≤ 1 − c₀/log(1951⁸ q^{10}(|τ|+3)^{10}), with c₀ computable (explicit zero-free regions for Hecke L-functions: Kadiri/Zaman/Ahn–Kwon genre, c₀ ≈ 0.078-class). By the FE (unconditional via Brauer) applied within the Galois family {ρ̃⊗χ^j}₀≤j≤4 (ρ̃* = ρ̃⊗χ⁻¹), poles pair under s ↦ 1−s̄; so if any pole exists in the family, one exists with β ≥ 1/2.

**R4 (census bound, with the conductor 1951⁸).** |N_λ(T) − (T/π)(log 1951⁸ + 10·log(T/2πe))| ≤ C₁ log(1951⁸(T+3)^{10}) + C₂, with C₁, C₂ absolute and computable (Landau/Rademacher; explicit-constant versions: Trudgian, Hasanalizade–Shen–Wong genre, adapted to Hecke L-functions). Same shape for Ξ_ψ with 1951⁸q^{10}. So: #{poles of L(ρ̃⊗ψ) to height T} ≤ (T/π)log(1951⁸q^{10}(T/2πe)^{10}) + O_eff(log).

**R5 (dodged control; effective).** For every T there is t* ∈ [T,T+1] with |L(σ+it*,Ξ_ψ)|⁻¹ ≤ exp(C₃ log²(1951⁸q^{10}(T+3)^{10})) uniformly in −1 ≤ σ ≤ 2 (zero-density in unit boxes ≪ log Q(T) + Borel–Carathéodory). Consequences: rigorous argument-principle censuses at any finite height (this is what makes the |t| ≤ 12 scans and any future FV(T₀) *certifiable*), and residue upper bounds |Res| ≤ exp(C₄ log²(1951q(|τ|+3))) at every pole.

## 2. The effectivization run, and where it breaks

Re-running Booker's machine for our class in contrapositive form — assume the census verifies no poles of L(ρ̃) (family) to height T, suppose some L(ρ̃⊗ψ) has a pole, seek contradiction with explicit T₀(q):

(a) The bounded side no longer needs the finiteness hypothesis: the polar tail above T is routed through dodged contours (R5), giving bounds exp(C log²(Q·(1/δ)^{10})) uniformly as δ → 0. **This removes Booker's "finitely many poles" assumption — but at superpolynomial cost.** The divergence from the hypothetical pole beats the regular side by only δ^{−β}, β ≤ 1, while the dodging loss exp(C log²(1/δ)) exceeds every power of 1/δ. The m, n tuning cannot help: both sides carry the same δ^{−(m−n−1/2)}.

(b) The divergence side's Ω-constant is proportional to the pole's leading Laurent coefficient. In the two-tile class that residue equals a jet of L(μ·ψ∘N) at the λψ-zero divided by a derivative of L(Ξ_ψ) there; **no effective lower bound exists** — μ may have a zero arbitrarily near an unmatched λ-zero, making a genuine pole invisibly small. Integer censuses (R5) are immune to this; Booker's analytic machine is not.

(c) Twist aggregation: the per-twist contradiction yields a q-dependent threshold T₀(q) ≍ (1951⁸q^{10})^{B}; Weil's converse theorem (in all four Booker/BK forms verified above) quantifies over infinitely many moduli, so sup_q T₀(q) = ∞.

**Kill condition K1 — hit, and localized to two named lemmas** (the charge's guidance (i) is *achieved* — pole sets and P-degrees are effectively enumerable (R1, R4) — and is *insufficient*; what fails is magnitude control and twist-finiteness, not pole bookkeeping):

**Lemma M (polynomial-loss minimum modulus / pair non-degeneracy).** There is a computable A with: (M1) for each needed Ξ ∈ {λ, μ, Ξ_ψ: q ≤ Q*} and every T, some t* ∈ [T,T+1] has |L(σ+it*,Ξ)|⁻¹ ≤ (Q_Ξ(T+3))^{A} on −1 ≤ σ ≤ 2; and (M2) at every actual pole of L(ρ̃⊗ψ), the leading Laurent coefficient is ≥ (Q(|τ|+3))^{−A}. Status: strictly beyond current technology; not delivered by GRH where it matters — under GRH the losses at σ ≥ 1/2+ε are subpolynomial (Littlewood type), but GRH also pins all candidate poles to σ = 1/2, exactly where even GRH yields only exp((log T)^{1−o(1)}) control. (M2) is a zero-repulsion statement between the two fixed abelian tiles μ and λ — weaker than universal zero-spacing, but of that family.

**Lemma CT_fin(Q*) (finite-twist converse theorem at level 1951).** For π-data of level 1951, nebentypus χ, gamma factor Γ_ℝ(s+a)², with (i) Euler product, (ii) FE of *every* twist (both unconditionally true for ρ̃ via Brauer — our class supplies for free the "meromorphy of all twists" half of Booker's p. 15 wish), automorphy follows from *pole-freeness of the twists with q ≤ Q** alone, Q* computable. Status: open; this is precisely Booker's stated wish instantiated where its cheap half is already a theorem. The BK 2014 "arbitrary poles" theorem is the closest existing statement and does not yet bound the twist set.

## 3. Theorem S (conditional effective dichotomy — full skeleton)

Assume Lemma M (with 10A < 1/2 − ϑ for some ϑ > 0) and CT_fin(Q*). Then: **if ρ̃ is not automorphic, some L(ρ̃⊗χ^j), 0 ≤ j ≤ 4, has a pole s₁ with |Im s₁| ≤ T₀**, where
  T₀ = (1951⁹ · Q*^{12})^{B(A)},  B(A) ≤ C₆(1+A)/(1/2 − ϑ − 10A),
C₆ absolute and computable from three displayed inequalities of the machine (skeleton-grade; to be pinned in a full write-up). Proof skeleton: contrapositive; census-verified pole-freeness to T₀ + (M1) makes the bounded side ≤ C(q)δ^{−(m−n−1/2)−10A−ε}; (M2) + R3 (some pole in the family has β ≥ 1/2) makes a hypothetical twisted pole diverge at rate δ^{−(1/2+m−n−1/2−ε)}; contradiction once δ < δ*(q), forcing pole-freeness of all twists q ≤ Q*; CT_fin closes to automorphy; automorphy kills all poles (Hecke). Each lemma's status: R1–R5 proved; M open; CT_fin open; assembly routine-but-long. **K2 check: T₀ is a single polynomial in 1951⁹Q*^{12} — no tower.**

## 4. The finite verification (exact statement)

FV(T₀): for each j ∈ {0,…,4}, by interval-certified argument principle on dodged rectangles/circles (R5) tiling 0 ≤ Im s ≤ T₀: certify that every zero of Λ(λ·χ^j∘N) is matched, with multiplicity, by a zero of Λ(μ·χ^j∘N) — equivalently every local winding number ∮ d log Λ(ρ̃⊗χ^j) ≥ 0. Integer-valued, robust to invisible-residue poles, and exactly the |t| ≤ 12 scans' primitive extended to T₀. Under M + CT_fin: FV(T₀) ⟹ strong Artin for ρ̃ (an even Maass form, eigenvalue 1/4, level 1951, nebentypus χ, with matching L-function) — the last open genus of 2-dimensional Artin.

## 5. Distance to closure (honest)

Unconditional gains this session: the entire polar bookkeeping of Booker's machine is now effective for this class (R1–R5), the Siegel obstruction is dead across all twists by a conductor-coprimality argument (R2), the finiteness hypothesis is eliminable in principle (dodged contours), and T₀ is tower-free once the two lemmas exist. What resists is sharply localized and provably not cosmetic: (M) — polynomial magnitude control of abelian L-functions at/near the critical line, sitting between GRH and zero-spacing; and (CT_fin) — finite-twist converse with all-twist FE granted, which is Booker's own named wish with half its hypotheses now free. The dichotomy's ineffectivity for our class is thus *entirely* a magnitude problem (residues/minimum modulus) plus a twist-count problem — the location/degree problems the charge targeted are closed. Distance: two lemmas, both named exactly, neither reachable by refinement of the present method; (CT_fin) looks the softer target (BK 2014 is adjacent), and any CT_fin proof immediately converts the existing census technology into a terminating algorithm for strong Artin at conductor 1951, modulo (M) only through heights polynomial in 1951⁹Q*^{12}.
