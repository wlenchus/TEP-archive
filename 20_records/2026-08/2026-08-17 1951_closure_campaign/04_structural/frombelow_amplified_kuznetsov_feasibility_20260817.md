> **NOTE (curated pack, 2026-08-17).** Self-consistent as filed. Provenance item only: the second-moment figure supplied in the commissioning charge was wrong and was corrected *inside* this record — (11+6√5)/30 is E[|a_p|]; **E[|a_p|²] = 1 exactly** (Schur orthogonality). The correction is to the charge, not to any prior corpus record.

---

# FROM-BELOW FEASIBILITY — amplified Kuznetsov at (Γ₀(1951), χ): the existence-forcing inequality, its numbers, and where the circle fails to close — 2026-08-17

*Constructive-prover session. Charge: derive the explicit inequality under which a lower-bound instrument at (Γ₀(1951), χ) would force a Maass cusp form, and price it honestly. NOT a proof; deliverable = inequality + input status + gap size. Inputs: `claude/closure_scattering_trace_pincer_cohh_20260816.md` (identity, scattering, packet accounting), `claude/ledger_extension_capladder_20260816.md` (caps 45 at X=8, 26 at X=10). Conventions cross-read against Knightly–Li, "Kuznetsov's trace formula and the Hecke eigenvalues of Maass forms" (Mem. AMS 224, 2013), arXiv:1202.0189, fetched this session: geometric-side constants and the twisted Weil bound verified from the fetched text; the spectral-side global constant is NAMED (𝔠_S) and cancels in every ratio used below (kill-condition discharged by design). All numerics this session, mpmath dps 20–40, scripts `/home/claude/frombelow/step1–6*.py`. Offered under claude/, not self-filed.*

## 0. The formula as used

Spectrum of Δ on L²(Γ₀(1951)\ℍ, χ), χ order-5 primitive even mod N = 1951; λ_j = ¼ + r_j², all u_j newforms (χ primitive ⇒ all-new; ρ_j(1) ≠ 0; residual spectrum empty — parent doc §0/§1). For m, n ≥ 1 and h even, holomorphic on |Im r| ≤ ½ + δ, h ≪ (1+|r|)^{−2−δ}:

**𝔠_S [ Σ_j ω_j h(r_j) λ_j(m) λ̄_j(n) + Σ_{𝔞∈{∞,0}} (1/4π)∫ℝ h(t) φ_{𝔞,t}(m) φ̄_{𝔞,t}(n) dμ_𝔞(t) ] = δ_{m,n}·c_I(h) + Σ_{c≡0(N)} c^{−1} S_χ(m,n;c)·h⁺(4π√(mn)/c)**

- c_I(h) := π^{−2} ∫ℝ h(r) r tanh(πr) dr (the δ-term constant, level-independent; KL/Iwaniec Thm 9.3 both);
- h⁺(x) := (2i/π) ∫ℝ J_{2ir}(x) h(r) r dr/cosh(πr) = −(4/π)∫₀^∞ Im J_{2ir}(x)·r h(r) dr/cosh(πr) (real for real x);
- ω_j := |ρ_j(1)|²/cosh(πr_j) > 0, the harmonic weight; ω_j = 𝔠_ω(r_j)/(N·L(1, Ad u_j)) with 𝔠_ω a named positive convention/Γ-factor constant (Hoffstein–Lockhart flavor). Positivity is the only property used.
- S_χ(m,n;c) = Σ*_{d(c)} χ̄(d) e((md̄+nd)/c); smallest modulus c = N (the structural advantage: every term carries c^{−1/2} ≤ N^{−1/2} = 1/44.2).
- Eisenstein: two χ-singular cusps; coefficients φ_{𝔞,t}(p) = p^{it} + χ(p)p^{−it} up to normalization; density dμ carries the 𝔠_E·N^{−1}|L(1+2it,χ)|^{−2}-suppressed newform-Eisenstein measure (𝔠_E named). The whole bracket is ≥ 0 termwise for amplified inputs.
- Global 𝔠_S: cancels below (only ratios of two instances of the identity are used).

**Twisted Weil.** Knightly–Li (1.10): |S_χ(a,b;𝔫;c)| ≤ τ(𝔫)τ(c)(a𝔫,b𝔫,c)^{1/2} c^{1/2} 𝔠_χ^{1/2} — the general safe bound carries cond(χ)^{1/2} = N^{1/2}. For our special shape (N prime, χ primitive mod N, c = N^α k, (k,N)=1) I derive the sharp bound with NO conductor factor: twisted multiplicativity splits off an untwisted Weil-bounded factor at k; at the N-part, α = 1 is a rank-≤2 Weil/Katz sum (≤ 2√N; Gauss-sum degenerate case √N; doubly degenerate 0), α ≥ 2 is elementary p-adic stationary phase with χ shallow (conductor N ≪ N^α), giving ≤ 2(m,n,N^α)^{1/2}N^{α/2}. Net: **|S_χ(m,n;c)| ≤ τ(c)(m,n,c)^{1/2}c^{1/2}.** Numerical corroboration on order-5 surrogates (χ mod 11 and mod 31; c = p₀k, p₀², 2p₀², p₀³; all m,n ranges incl. degenerate): worst ratio to this bound 0.847 (mod 11), 0.901 (mod 31), attained at c = p₀ where it is exactly Weil. The verdict below uses the sharp bound (the KL factor N^{1/2} = 44 would only worsen it).

## 1. The amplifier

x_p := ā_p for p ≤ P, p ≠ 1951, a_p = tr ρ̃(Frob_p) ∈ ℤ[ζ₅] the exact icosahedral data; A_j := Σ_p ā_p λ_j(p). Expand |A_j|² via the (m,n) = (p,q) instances (equivalently by Hecke relations λ_j(p)λ̄_j(q) = χ̄(q)λ_j(pq) for p ≠ q, |λ_j(p)|² = χ̄(p)λ_j(p²) + 1, using the nebentypus adjoint λ̄_j(n) = χ̄(n)λ_j(n)):

Σ_j ω_j h(r_j)|A_j|² + ℰ(P,h) = c_I(h)·𝒟(P) + K(P,h),  𝒟(P) := Σ_{p≤P}|a_p|², K := Σ_{p,q} ā_p a_q Σ_{c≡0(N)} c^{−1}S_χ(p,q;c) h⁺(4π√(pq)/c).

**Exact moments (Chebotarev densities 1/60, 1/3, 1/4, 1/5, 1/5 on |a_p| = 2, 1, 0, φ, 1/φ):**
- E[|a_p|²] = 4/60 + 1/3 + 0 + (φ²+φ^{−2})/5 = 1/15 + 1/3 + 3/5 = **1 exactly** (φ²+φ^{−2} = (φ+φ^{−1})²−2 = 3). This is ⟨χ_ρ̃, χ_ρ̃⟩ = 1 — Schur orthogonality, i.e. irreducibility; pointwise it is 1 + tr Ad ρ̃(g) = |tr ρ̃(g)|² ≥ 0. So 𝒟(P) = π(P)(1+o(1)) and Σ_p |a_p|²/p = log log P + O(1) with **κ = 1** (the charge's (11+6√5)/30 = 0.813880 is E[|a_p|], the first moment — verified to 25 digits).
- If F exists (r = 0, λ_F(p) = a_p): A_F = 𝒟(P), so its atom contributes ω_F h(0)𝒟² ≈ ω_F π(P)² — the amplifier is perfectly tuned (gain π(P) over the variance level π(P)).

## 2. THE INEQUALITY

Let K_bd(P,h) := Σ_{p,q≤P}|a_p a_q| Σ_{c≡0(N)} τ(c)(p,q,c)^{1/2}c^{−1/2} Ĥ(4π√(pq)/c) with Ĥ ≥ |h⁺| a certified envelope; ℰ_bd an upper bound for the amplified Eisenstein term; κ₁ := Σ_{c≡0(N)}τ(c)c^{−1/2}Ĥ(4π/c) (the (1,1)-instance off-diagonal). Positivity of every spectral term plus the (1,1)-instance bound Σ_j ω_j h(r_j) ≤ c_I + κ₁ give:

**(∗) If Θ < Θ*(P,h) := [𝒟(P) − (K_bd + ℰ_bd)/c_I(h)] / (1 + κ₁/c_I(h)), then some Maass cusp form u_j ∈ S(1951, χ) has |Σ_{p≤P} ā_p λ_j(p)|² > Θ,** and (tail lemma, Kim–Sarnak |λ_j(p)| ≤ 2p^{7/64} + Gaussian decay of h) it can be taken with |r_j| ≤ R = T₀·√(2 log[4𝒟Σ_p p^{7/32}·(c_I(h̃)+κ̃₁)/(Θη)]); at P = 10³, T₀ = 1, Θ = π(P)/2: R = 3.9.

Input status: **proven** — spectral positivity; sharp twisted Weil (derived + corroborated; KL citable fallback); exact a_p (finitely computable from the Doud–Moore quintic, project file 0405534; numerics below use Chebotarev means); Kim–Sarnak; κ₁/c_I = 0.0087. **Proven-structural, not numerically executed** — ℰ_bd: density suppressed by 𝔠_E N^{−1}|L(1+2it,χ)|^{−2}, and its correlation factor |Σ_p ā_p p^{±it}|² is o(π(P)²) by PNT for the nontrivial-irreducible Artin L(s, ρ̃⊗|·|^{it}) on Re s = 1 (Brauer; effective-in-principle at this fixed conductor). **Conditional per its own doc** — cap-ladder rows (standard-ledger-calibrated). **Not assumed anywhere** — bulk square-root cancellation (that is the tie-breaker, §5).

**What the cap ladder does and does not do.** B(X) bounds Σ_j h_Fejér(r_j) with unit weights: it caps COUNTS — m(0) + #exceptional ≤ 45 (X=8), ≤ 26 (X=10); via h_F ≥ ½ on |r| ≤ 0.50, also #{|r_j| ≤ 0.50} ≤ 90. It bounds neither ω_j nor amplifier values. A count-route forcing (replace Θ·(c_I/κ₁) by Θ·ω_max h(0)·B_count) needs ω_max, i.e. Hoffstein–Lockhart L(1,Ad u_j) ≫ log^{−3}N ≈ 1/435: Θ_count/Θ_harm = c_I/(ω_max B_count) ≈ 0.009/𝔠_ω for B_count = 45 — the count route loses by ~10², at any window. The ladder's real role here: it localizes the candidate list for the forced form (≤ 26–90 atoms near the ¼ point), it cannot raise the threshold.

## 3. The numbers (h(r) = e^{−r²}; c_I = 0.094064)

h⁺ computed via complex-order Bessel (mpmath, cross-checked against the power series to 24 digits): slope C₁ = |h⁺|/x → 0.4087 (x→0); max |h⁺| = 0.2167 at x ≈ 3; large-x envelope |h⁺(x)| ≤ 2πc_I√(2/(πx)) exact at phase peaks to 4 digits out to x = 700. Certified envelope Ĥ: 0.410x / 0.230 / 1.02·env(x) on x < 0.562 / ≤ 4.35 / > 4.35. Weights: mean version |a_p a_q| → E[|a|]² = 0.6624 (honest size); safe version ≤ 4 (proven; ×6.04 worse). gcd-diagonal and N|k corrections: ≤ 2π(P)κ₁ and ≤ 8.4x₁/N² — negligible.

| P | π(P) ≈ 𝒟 | K_bd/c_I (mean) | **failure margin M = (K_bd/c_I)/𝒟** | M (safe |a_p|≤2) |
|---|---|---|---|---|
| 10³ | 168 | 4.84·10⁴ | **288** | 1.74·10³ |
| 10⁴ | 1229 | 1.44·10⁷ | **1.17·10⁴** | 7.06·10⁴ |
| 10⁵ | 9592 | 3.99·10⁹ | **4.16·10⁵** | 2.51·10⁶ |

Margin grows ≈ P^{1.6}. Crossover scan: Θ*(P) > 0 only for **P ≤ 40** (mean weights; never, for safe weights): at P = 30, forced Θ = 3.5 against variance level π(30) = 10 — sub-variance, content-free. At the GRH-rigidity radius P = 230 (§6): M = **24** (safe: 145) — the minimal honest statement of the gap: even at the shortest arithmetically meaningful amplifier length, the Weil-bounded off-diagonal exceeds the diagonal by one-and-a-half orders of magnitude.

## 4. The circle, chased and closed on itself

Second application with roles reversed is the SAME identity: the bulk's total amplifier mass Σ_{j≠F} ω_j h|A_j|² = [c_I𝒟 + K − ℰ] − ω_F h(0)𝒟²·𝟙_F. Subtracting the two applications yields 0 = 0: **the relative trace formula fixes the total amplified mass and is permutation-blind to its location** — it cannot distinguish [one atom at r = 0 carrying 𝒟²] from [the same diagonal redistributed as variance ≈ 𝒟 over the bulk]. Sharper, the instrument is structurally self-defeating at long amplifier length: if F exists, then K = ω_F𝒟² + (bulk − c_I𝒟 + ℰ) ≥ ω_Fπ(P)² − c_Iπ(P), so once π(P) > c_I/ω_F ≍ 𝔠_ω^{−1}c_I·N·L(1,Ad ρ̃) = O(10²) the true off-diagonal is FORCED to dominate the diagonal — the atom's entire square sits inside the twisted Kloosterman term. Consequently no upper bound on |K|, however refined (Weil, or even Deshouillers–Iwaniec-average cancellation), can force existence beyond Θ ≈ variance; a from-below proof must EVALUATE the Kloosterman side to relative accuracy o(1) at scale ω_Fπ(P)².

## 5. The tie-breaker, named and classed

Two independent missing inputs:

**(T1) BulkAmp(P, δ)** — the tie-breaker proper: for every u_j ≠ F with |r_j| ≤ R, |Σ_{p≤P} ā_p λ_j(p)| ≤ π(P)^{1−δ}. Equivalently: effective holomorphy + nonvanishing at s = 1 of the Rankin–Selberg-against-Artin Dirichlet series L(s, u_j ⊗ ρ̃^∨), family-wide — precisely what is open for nonsolvable ρ̃ (no base change; continuation across s = 1 is modularity-adjacent). Equivalently a large-sieve/zero-density statement for {u_j × ρ̃^∨} at the ¼ point. **Class: Δ/W — a magnitude/density statement**, same class as the corpus's standing obstruction; proven here to be UNOBTAINABLE from the trace formula itself (§4: the second application is tautological). With (T1) at δ and the off-diagonal controlled, (∗) forces Θ = π(P)^{2−2δ}-level correlation → mean-square matching via the per-form effective RS second moment Σ_p|λ_j(p)|² = π(P)(1+o(1)).

**(T2) Kloosterman-average cancellation** (fixes the off-diagonal only): cancellation in Σ_{c≡0(N)}Σ_{p,q} beyond Weil by ≥ 288 at P = 10³ (≥ 24 at P = 230) — Linnik/Deshouillers–Iwaniec class; the DI Kloosterman large sieve extends to nebentypus in principle, but executing it with explicit constants at fixed N = 1951 is a named project, and even granted, the ceiling Θ ≤ variance (§4) stands without (T1).

**Rigidity radius (correlation → identification).** Effective strong multiplicity one radii for "λ_j(p) = a_p for all p ≤ P₀ determines the form among automorphic objects": on GRH for RS, P₀ ≍ (log Q)² ≈ 230 (Q ≈ N²(1+|r|)⁴ ≈ 4·10⁶); unconditional (Brumley-class effective multiplicity one), P₀ ≪ Q^{2+ε} ≥ 10¹³ — out of reach. And these compare automorphic pairs only: even perfect matching identifies the forced form with another automorphic object, never directly with the Artin data — the final identification IS modularity. Eigenvalue exactly ¼ is likewise not forced by correlation (localization only gives |r_j| ≤ 3.9 at P = 10³).

## 6. Verdict

The inequality (∗) is correct, unconditional, and convention-robust (ratio design). Under proven bounds it closes only for P ≤ 40, where it forces sub-variance correlation — nothing. At P = 10³/10⁴/10⁵ it fails by 288 / 1.2·10⁴ / 4.2·10⁵ (sharp Weil, mean weights; ×6 worse with proven pointwise weights). The failure is not an accounting artifact: if F exists, the off-diagonal genuinely carries ω_Fπ(P)² ≫ diagonal for π(P) ≳ 10², so the from-below instrument at (1951, χ) cannot certify existence by any positivity-plus-upper-bound scheme; its ceiling, with both missing inputs granted, is "a cusp form with |r_j| ≤ R whose Hecke data correlates with ρ̃ at level Θ ≤ π(P)". Existence stays on the Artin side, exactly where the parent docs left it; what this session adds is the priced statement of WHY: the RTF cannot see where the mass sits (§4), and the single statement that would break the tie is (T1), a Δ/W-class bulk-amplifier/density bound at the ¼ point.

**Load-bearing caveats.** (i) The Kuznetsov spectral-side global constant 𝔠_S was not line-by-line re-derived; it cancels in every quantity reported (D, K_bd, κ₁, Θ* are built from two instances of the same identity), and geometric-side constants were verified against the fetched Knightly–Li text — but 𝔠_ω, 𝔠_E remain named, entering only interpretive scales (ω_F, ℰ), not the failure margins. (ii) Numerics use Chebotarev-mean |a_p| (margins are means, not bounds; the proven-|a_p|≤2 column brackets them from above; exact 𝒟, K_bd are finitely computable from the quintic — refinement available). (iii) ℰ_bd is bounded structurally (1/N-suppressed density, PNT-for-ρ̃ correlation), not numerically executed — irrelevant to the failure verdict (ℰ only subtracts), essential to any future success claim; likewise the cap-ladder rows inherit their own doc's standard-ledger conditionality.

*Offered, not self-filed. 2026-08-17.*
