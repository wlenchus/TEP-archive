# V2 Q1 Execution — Spectral Moments of Bekenstein–Hawking Thermal States (DraftV1, offered)
**2026-08-01 · Claude (Fable 5) · Countersign gates everything below.**

## 0. Provenance and commissioning
V2 Central Reference (2026-04-19, ActiveV3), Open Questions: "**Q1: Spectral Moments of Bekenstein–Hawking Thermal States.** The Fubini–Study identification (Tier 3.4 [sic; the entry is §3.5]) uses √p₃ = m_P/M and γ = l_P/r as definitional assignments. Whether the actual spectral moments p₃ and γ of a Bekenstein–Hawking thermal state (computed via standard QFT-in-curved-spacetime methods) match these assignments is an open computation. A match would significantly strengthen the bridge between the purity transport formalism and gravitational physics. **A mismatch would establish that the identification is formal only.**"

Tier 3.5 (verbatim): "Under the assignments √p₃ = m_P/M and γ = l_P/r, the Fubini–Study cosine between the purified bulk state and the boundary-projected state satisfies cos θ = γ/√p₃ = r_s/(2r) exactly. … **What's missing:** The identification … is a definitional choice, not derived from any specific density matrix for a gravitational thermal state. The computation of actual spectral moments p₃ and γ for the Bekenstein–Hawking thermal state has not been performed in the corpus. Until it is, the identification is a formal analogy rather than a derived correspondence."

Definitions pinned by V2 §1.1: γ = Tr(ρ²), p₃ = Tr(ρ³). Both the February referee and V2 ranked this computation decisive; the 2026-08-01 archaeology found it swept out of every queue by the Tier 5.5 gravity retirement (correctly aimed, over-broad in scope). Commissioned here under Will's 08-01 "push on a present thread" invitation.

**Preregistration status, stated honestly:** this note executes a test whose adjudicating criterion was preregistered *by V2 itself* 3.5 months ago (mismatch ⇒ "formal only"). The structural results below were derived this session and then machine-verified; no blind protocol applies because the verdict rule predates the computation and belongs to the corpus, not to me.

**Training-prior disclosure:** the thermal-spectrum moment algebra, Schatten-norm monotonicity (‖ρ‖₃ ≤ ‖ρ‖₂ for density matrices), and log-convexity of power sums are standard results I hold as weights-priors. Each is machine-verified below (sympy symbolic identities + a 200,000-spectrum numeric sweep, d = 2–11, seed 20260801, zero violations).

## 1. The question, typed precisely
The "match" arm of Q1 requires that some density matrix licensed by "standard QFT-in-curved-spacetime methods" *realizes* the assignment pair (γ = l_P/r, √p₃ = m_P/M) — with γ varying over the observation radius r while p₃ stays pinned to the mass. Four readings exhaust the natural realizations. All four are adjudicated; all four mismatch.

## 2. Readings and results

**R-A. Single effective thermal mode** (the minimal "thermal state" reading). For a bosonic thermal mode with spectrum λ_n = (1−x)xⁿ: γ = (1−x)/(1+x) and p₃ = (1−x)³/(1−x³), which eliminate to the one-parameter **thermal moment curve p₃(γ) = 4γ²/(3 + γ²)** [verified symbolically]. Imposing both assignments forces 4γ²/(3+γ²) = (m_P/M)² with γ = l_P/r, which has exactly one solution: with ε = m_P/M, **r*/r_s = √(12 − 3ε²)/6 → 1/√3 ≈ 0.577** as ε → 0 [verified]. The unique radius at which a thermal state satisfies both assignments lies *strictly inside the horizon* for every M. Everywhere outside the horizon — the entire domain where cos θ = r_s/2r is advertised as the Newtonian potential — the pair is thermally unsatisfiable.

**R-B. Any quantum state whatsoever** (dimension-free; drops thermality entirely). Schatten monotonicity gives p₃ ≤ γ^{3/2} for every density matrix [0 violations / 200,000 random spectra]. The assignments then require (m_P/M)² ≤ (l_P/r)^{3/2}, i.e.
  **r ≤ l_P·(M/m_P)^{4/3},  equivalently  r_max/r_s = (M/m_P)^{1/3}/2.**
Beyond r_max, *no density matrix in any Hilbert-space dimension* realizes the pair — a three-line theorem [T]. For M = M_⊙: r_max ≈ 2.25 × 10¹² r_s. Large, but finite: the weak-field regime that gives the Fubini–Study reading its appeal extends past a radius where the identification is state-theoretically empty.

**R-C. The d = 2 budget register.** Qubit purity is floored: γ ∈ [1/2, 1] (with p₃ = (3γ−1)/2 exactly) [verified]. The assignment γ = l_P/r is unrealizable at d = 2 for any r > 2l_P. Stated because the budget formalism's home register is d = 2.

**R-D. The literal multimode Bekenstein–Hawking state** (Q1's own "standard QFT-in-curved-spacetime" clause: greybody-filtered thermal radiation / thermal atmosphere). Moments are multiplicative across modes, so −ln γ is *extensive*, of order S_BH ~ 4π(M/m_P)² ≈ 10⁷⁷ for M_⊙ — against the assignment's −ln γ = ln(r/l_P) ≈ 89 nats at r_s. A log-space mismatch of ~75 orders of magnitude; ensemble choice and O(1) greybody coefficients are irrelevant at this separation.

## 3. Verdict (offered)
Mismatch on every constructed reading. Per Q1's own preregistered consequence: **"the identification is formal only."**

Status vocabulary, applied with the discipline this corpus (and this week's correction record) demands: nothing here *falsifies an instantiated claim* — V2 explicitly declined to instantiate ("a definitional choice, not derived"). What this note does is execute the pending computation, converting Tier 3.5 from *formal-analogy-pending-computation* to **formal-only, computed**. The Fubini–Study algebra itself is untouched — cos θ = γ/√p₃ = r_s/2r remains exact under the stated assignments, exactly as V2 graded it. The same-family neighbors (Tier 3.4 mass budget, Tier 1.2 Kerr–Newman identity) are independent algebra and unaffected. Proposed disposition: Q1 → resolved-negative; Tier 3.5 status line gains "identification adjudicated formal-only (08-01)."

## 4. Escape hatches, priced
(i) *Reinterpret the assignments as definitions* of effective functionals M(ρ), r(ρ) — concedes "formal only" by construction. (ii) *Alternative moment definitions* (normalized moments; per-mode moments at the Hawking peak) — abandons V2 §1.1's pinned definitions; would need a fresh pin and a fresh Q1. (iii) *Engineered non-thermal ρ(r) families* — permitted by R-B only inside r_max, and excluded by Q1's own "standard methods" clause. **Same-family caveat:** all four readings adjudicate through one toolbox (power-sum/Schatten algebra); the priced exits above are the only ways out of that toolbox I can construct, and each forfeits Q1's terms.

## 5. Positive residue [T, offered]
The R-B bound is a small new structural fact in its own right: **any state-realization of the FS–Schwarzschild assignments is confined to r ≤ l_P(M/m_P)^{4/3}**, with the clean M^{1/3} scaling of the validity horizon in Schwarzschild radii. If a state-realized version of the analogy is ever wanted, this is its outer wall — and a falsifiable signature of any candidate construction.

## 6. Kill conditions for this note
(a) V2's γ, p₃ mean anything other than Tr ρ², Tr ρ³ (foreclosed by §1.1, quoted); (b) machine checks fail replication (script below; seed pinned); (c) a state class licensed by "standard QFT-in-curved-spacetime methods" is produced that realizes the pair outside the excluded regimes. Any of these voids the verdict and returns Q1 to open.

## 7. Reproduction script
```python
import sympy as sp, numpy as np
x, g, eps = sp.symbols('x g epsilon', positive=True)
# R-A: thermal curve and unique joint radius
gam, p3 = (1-x)/(1+x), (1-x)**3/(1-x**3)
p3_of_g = sp.simplify(p3.subs(x, sp.solve(sp.Eq(gam, g), x)[0]))   # -> 4g^2/(g^2+3)
gstar = sp.sqrt(3)*eps/sp.sqrt(4-eps**2)                            # solves p3(g)=eps^2
assert sp.simplify(p3_of_g.subs(g, gstar) - eps**2) == 0
print("r*/r_s =", sp.simplify(eps/(2*gstar)), "->", sp.limit(eps/(2*gstar), eps, 0))  # 1/sqrt(3)
# R-B: Schatten sweep
rng = np.random.default_rng(20260801); viol = 0
for _ in range(200000):
    lam = rng.dirichlet(np.ones(rng.integers(2,12))*rng.uniform(0.05,3.0))
    viol += (lam**3).sum() > (lam**2).sum()**1.5 + 1e-12
print("violations:", viol)                                          # 0
Mr = sp.symbols('Mr', positive=True)
print("r_max/r_s =", sp.simplify(Mr**sp.Rational(4,3)/(2*Mr)))      # Mr^(1/3)/2
# R-C: qubit floor
l_ = sp.symbols('l', nonnegative=True); gq = l_**2 + (1-l_)**2
assert sp.minimum(gq, l_, sp.Interval(0,1)) == sp.Rational(1,2)
assert sp.simplify((l_**3+(1-l_)**3) - (3*gq-1)/2) == 0
# R-D: magnitudes (M_sun)
R = 1.98892e30/2.176434e-8
print(f"S_BH~4pi(M/mP)^2={4*np.pi*R**2:.3e}; assigned gamma(r_s)={1/(2*R):.3e}; r_max/r_s={R**(1/3)/2:.3e}")
```

*Offered, not filed. This discharges the archaeology's R4 and closes the reviewer-side maintained judgment of the 08-01 correction record — from "it is open" to "here is the execution." The countersign rules on: the verdict framing (§3), the Tier 3.5 status line, and whether the validity-horizon residue (§5) is worth a one-line home in the canon.*
