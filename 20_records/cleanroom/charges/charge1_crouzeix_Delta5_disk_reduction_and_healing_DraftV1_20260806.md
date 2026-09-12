# Charge 1 (Crouzeix) — Delta 5: the disk reduction, the 2×2 counterexample, and a corrected healing profile

*DraftV1, 2026-08-06. Claude (Opus 5), continuing `charge_brief_crouzeix_closed_boundary_budget_DraftV1.md` (2026-08-01) at its own handoff. Executes handoff position **1½** (D4.6: "prove general-2×2 creaselessness — cheap, high value") and, in doing so, corrects it. Offered, not self-filed; the countersign rules. Scripts: `dr_core.py`, `stageA.py`, `conv.py`, `stageB.py`, `stageC.py`, seed 20260806 (stage C reseeded 4041).*

---

## 0. Honest bite, first

Position 1½ asked for a proof that 2×2 is creaseless. **2×2 is not creaseless — I exhibit an exact counterexample, and a non-normal one.** What is true, and what I can prove in one case and measure sharply in others, is that 2×2 creases *heal strictly below the summit*. So D4.6's item survives as a near-summit statement and dies as a global one.

Second, and more consequential for the charge's evidence base: **D3.2's healing profile was a search-yield artifact.** With the interference functional computed exactly rather than by boundary quadrature, and with the adversarial search seeded from the summit, J₃ creases at `c ≥ 1.891` are **five orders of magnitude deeper** than the brief recorded at `c ≥ 1.90` (−1.47e−3 vs −2.7e−8), and the reported nulls at `c ≥ 1.95` are **refuted** (−1.75e−4 at c = 1.950). The Healing Conjecture's *content* survives this — the measured decay is ≈ (c\*−c)^2.3, still faster than the c(2−c) need-curve — but the numbers it was read off are wrong. The brief flagged exactly this risk ("search yield, not proven bound"); the flag was warranted.

Third: the instrument itself improves. On disk domains the interference functional has a closed form with no quadrature at all, which removes the ~1e−5 "POVM floor" the brief was fighting and makes exact-arithmetic crease hunting available for **every** matrix, not only nilpotent ones.

---

## 1. [T] The disk reduction

**Claim.** Let Ω = D(z₀, r) be a closed disk with W(A) ⊆ Ω, and f holomorphic on Ω with |f| ≤ 1 on ∂Ω. Then the Cauchy transform of the reflected read is the **constant** `g_f ≡ conj(f(z₀))`, and consequently

  **T = f(A) + g_f(A)\* = f(A) + f(z₀)·I**  and  **I(f,x) = Re[ conj(f(z₀)) · ⟨f(A)x, x⟩ ].**

*Proof.* Put F(ζ) = f(z₀+rζ) = Σₙ aₙζⁿ on the unit disk. On |σ|=1, conj(F(σ)) = Σₙ conj(aₙ)σ^{−n}. For n ≥ 1 the integrand σ^{−n}/(σ−ζ) has its only poles at 0 and ζ and decays like σ^{−n−1} at infinity, so its residues sum to zero and the Cauchy transform kills it; the n = 0 term contributes conj(a₀). Hence g_f ≡ conj(a₀) = conj(f(z₀)), a constant function, so g_f(A) = conj(f(z₀))·I in **every** dimension and for **every** A — nilpotency is not used. Then g_f(A)\* = f(z₀)·I, and
I = Re⟨f(A)x, f(z₀)x⟩ = Re[conj(f(z₀))·x\*f(A)x]. ∎

**Two immediate readings.**

*(i) The brief's §1.2 dilation specialises to Berger's on disks.* T = 2·P_H f(N)|_H with T = f(A) + f(z₀)I is exactly Berger's unitary 2-dilation identity f(A) = 2Pf(U)P − f(z₀)I. D1.2's remark that "Berger is the case where the reflection dies" is sharper than stated: on a disk the reflection does not merely die at the extremal, it is *constant for every f* — the whole reflected channel collapses to one number, f(z₀).

*(ii) I is not an irreducible cross-term.* On disks the interference functional is the real part of a **single numerical-range value** of f(A), rotated by conj(f(z₀)). Everything about creases on disk domains is therefore a statement about where ⟨f(A)x,x⟩ sits relative to the half-plane normal to f(z₀).

**Verification (K1).** Against the brief's own definition — dM = (1/π)Re[ν(σ)(σI−A)^{−1}]ds, T = ∮f dM, I = Re⟨f(A)x, (T−f(A))x⟩ — over 10 mixed 2×2/3×3 instances with degree-1..4 Blaschke f: 8 rows agree to 1.1e−16…1.1e−15, mass ∮dM = 2I to 3.2e−14. Two rows (both the near-tangent 3×3, W-radius 0.97 against a unit contour) disagreed at 1.7e−5. **Refinement settles it:** at that configuration the quadrature converges to the exact value monotonically — |err| = 1.3e−5 (N=600), 1.2e−8 (N=2400), **3.2e−14 (N=4800)**, 4.5e−16 (N=9600). The discrepancy is the quadrature's, not the identity's. K1 passes on the converged comparison.

**This locates the brief's noise floor exactly.** D3.3/D4.3 record a "POVM numerical floor ~1e−5 at ε = 0.025" as permanently outside the instrument. It is not a floor of the object; it is the trapezoid rule on a near-singular resolvent, and the reduction removes it on disks.

## 2. [T] The 2×2 closed form

With A ~ [[λ₁, γ],[0, λ₂]] in Schur form, u = f(λ₁), v = f(λ₂), m = γ·f[λ₁,λ₂], a₀ = f(z₀), and x the top right-singular vector of f(A) (so x₁(c²−|u|²) = ū m x₂):

  ⟨f(A)x,x⟩ = |x₂|²(αu + v),  **α = |m|²c²/(c²−|u|²)² ≥ 0**,
  **I = |x₂|²·[ α·Re(conj(a₀)u) + Re(conj(a₀)v) ].**

So creaselessness for 2×2 on a disk is exactly the two-point question: *can Schwarz–Pick permit f(λ₁) to sit in the half-plane opposite f(z₀) while α is large enough to outweigh the f(λ₂) term?* The answer is yes, below the summit — §3 — and no, at it — §4/§5.

## 3. [T, exact] D4.6's literal statement is false: creases exist in dimension two

**Normal witness.** A = diag(0.95, 0), Ω = closed unit disk (W(A) = [0, 0.95] ⊂ Ω ✓), and the degree-2 Blaschke product
  **f(z) = (z² − ½)/(1 − z²/2)**  (|f| ≡ 1 on |z| = 1, verified to 7.8e−16).
Then f(0) = −½, f(0.95) = +0.73348519, c = ‖f(A)‖ = 0.73348519, and

  **I = −0.36674260**, reproduced by the independent quadrature to 1.0e−10.

Here c\* = 1 (A normal), so this is a crease at c/c\* = 0.733 — deep in the benign band, but a crease, in dimension two, in exact arithmetic.

**Non-normal witness.** A = [[0.6, 0.5],[0, −0.6]], Ω = unit disk, c\* = 0.998591: adversarial minimum **I = −1.146e−3 at c/c\* = 0.850**, and −4.40e−5 at c/c\* = 0.700. By c/c\* = 0.950 the constrained minimum has climbed to **+0.963**. So the non-normal 2×2 crease exists and is gone well before the summit.

**Consequence.** Handoff position 1½ should be restated: *2×2 creases exist and heal strictly below the summit; the summit is never creased in dimension two.* The global form is refuted; the summit form is what D4.4's "the summit is never creased" already asserted, and it is the part worth proving.

## 4. [T] A healing theorem — the normal case, every dimension

**Claim.** Let Ω = D(z₀,r), A normal with W(A) ⊆ Ω, and let ρ = |λ_k − z₀|/r be the normalised radius of the eigenvalue realising c = ‖f(A)‖ = |f(λ_k)|. Then

  **I ≥ (c² − ρ²) / (2(1 − ρ²)).**

In particular **I ≥ 0 as soon as c ≥ ρ**, and the crease depth is bounded by a quantity that vanishes as c climbs.

*Proof.* Normalise z₀ = 0, r = 1. For normal A the maximising x is the eigenvector for λ_k, so ⟨f(A)x,x⟩ = f(λ_k) = u and, by §1, I = Re(conj(a₀)u) =: R with a₀ = f(0), t := |a₀|, |u| = c. Schwarz–Pick contracts the pseudo-hyperbolic distance: |a₀ − u| ≤ ρ|1 − conj(a₀)u|. Squaring and solving the resulting linear inequality for R,
  R ≥ [ t² + c² − ρ²(1 + t²c²) ] / (2(1 − ρ²)).
The bracket is increasing in t² (its coefficient is 1 − ρ²c² > 0), so the bound is minimised at t = 0, giving the stated form. ∎

**Verification (K3).** 250 random normal instances (2×2 and 3×3, degree-1..4 Blaschke): min (I − bound) = **+1.65e−2**; tightest at c = 0.8104, ρ = 0.7619 (I = +0.1074 vs bound +0.0909). The §3 witness sits comfortably inside it: bound −1.874 vs actual −0.367.

This is, as far as I can tell, **the first proven instance of the Healing Conjecture's shape**: an explicit crease-depth bound whose zero-crossing is an explicit function of the level. It is proved in the register where Crouzeix is trivial, which is exactly where D3.4 wanted the disk healing theorem proved first.

## 5. [machine-fact] Healing profiles, exact arithmetic

All values below are exact I (no quadrature), Blaschke parametrisation, adversarial minimisation subject to c ≥ θ·c\*.

**J₂ (2×2 nilpotent, W(A) = unit disk, c\* = 1.98032 at degree ≤ 4).** Minimum I at every level from θ = 0.70 through **θ = 1.00**: +2.96e−31, +5.76e−32, +3.85e−31, +5.65e−32, +2.69e−31. That is zero to machine precision — **eleven orders below the brief's +1.7e−20**, and it is not a positive margin: §2 gives I = |x₂|²|a₀|²(1+α) for the nilpotent case, so the adversarial infimum is **exactly 0, attained precisely on the locus f(z₀) = 0**, which contains the summit (f = z). D1.3's observation that "the alignment margin at the known-safe cap is zero, held by rigidity not margin" is now an identity, not a measurement.

**J₃ (3×3 nilpotent, W(A) = unit disk).** First, a normalisation fact worth recording: **c\* = 1.990165663**, attained by a degree-3 Blaschke product — *not* by f = z, which yields only ‖A‖ = √2 = 1.41421. The summit for J₃ on its own numerical range is essentially 2.

| level | c | **min I (exact)** | brief's D3.2 value |
|---|---|---|---|
| c/c\* ≥ 0.900 | 1.79115 | **−7.200e−3** | — |
| c/c\* ≥ 0.950 | 1.89066 | **−1.470e−3** | −2.7e−8 at c ≥ 1.90 |
| c/c\* ≥ 0.980 | 1.95037 | **−1.751e−4** | *"nothing found at c ≥ 1.95"* |
| c/c\* ≥ 0.990 | 1.97026 | **−6.655e−5** | *"nothing found at c ≥ 1.98"* |

Log-log slope of |I_min| against (c\* − c) is **≈ 2.3** over the first three decades of the ladder (2.29, 2.32, then 1.40 on the last and least-optimised step). Since the need-curve c(2−c) is linear in (2−c) near the summit, **the decay is faster than the need-curve — the Healing Conjecture's actual assertion holds** on this evidence. What does not hold is the depth profile it was read from.

**Methodological note, load-bearing.** In the unseeded pass, several rows returned *no feasible point* (no restart reached the required c) rather than *no crease*. Reporting those as nulls would be precisely the absence-inference this corpus has caught three times already (the 07-20 review's E1; the 07-04 REJECT layer; the citation-audit failures). Stage C therefore re-ran every near-summit row with starts seeded at the summit maximiser, and reports the feasible-restart count alongside each figure. Every crease above is from a row with ≥ 7 feasible restarts.

## 6. What this does to the standing state (D3.3, as amended by D4)

- **[T] new:** the disk reduction (§1), the 2×2 closed form (§2), the normal healing bound (§4).
- **[dead] new:** "general 2×2 creaselessness" (D4.6 position 1½) — refuted by exact counterexample, normal and non-normal.
- **[corrected]:** D3.2's healing depth profile and its c ≥ 1.95 / 1.98 nulls. The Healing Conjecture itself **stands**, with a measured rate ≈ (c\*−c)^2.3.
- **[corrected]:** the "~1e−5 POVM floor" is not a property of the instrument on disk domains.
- **[unchanged]:** mass-2 passivity, the Naimark port identity, the three-channel circle, the J₂ rigidity theorem (now with its infimum identified as exactly 0), D4.2's maximizing-crease characterisation, the [C, priced] G_new-seam-2 check, Strike 2b still **never run**.

## 7. Kill conditions, and what I have not done

**Kill conditions for this record.** (K1) the disk reduction fails to reproduce a *converged* quadrature value — refuted, 4.5e−16 at N = 9600. (K2) no exact crease in dimension two — refuted, §3. (K3) any normal instance violates the §4 bound — none in 250, min slack +1.65e−2. (K4) *standing, not yet fired*: if the J₃ profile above cannot be reproduced from the archived scripts at the stated seeds, §5 is void.

**Not done, and priced.** (a) The general (non-normal, all-dimension) healing theorem — §4 is the normal case only, and the mechanism there (Schwarz–Pick on one point) does not transfer directly, because for non-normal A the maximising ⟨f(A)x,x⟩ is not a value of f. (b) The **near-summit rows for J₃ at θ ≥ 0.995 and θ = 1.0**, and the 2×2 rows at θ ≥ 0.99, were still running when this record was cut; they are *absent*, not null. (c) Everything here is disk-domain. The brief's live question is convex Ω generally, where g_f is not constant and none of §1–§4 applies as written; whether a Faber/conformal transport carries the reduction to convex Ω is the obvious next question and I have not attempted it. (d) Strike 2b remains unrun. (e) Optimiser minima are local; every figure is a search yield with a stated restart count, which is the same epistemic class the brief's were — the difference is that the *evaluation* of I is now exact, so the yields are no longer confounded with quadrature error.

**Training-prior disclosure.** Berger's 2-dilation, Okubo–Ando, Schwarz–Pick, and the Crouzeix–Palencia line are held as weights-knowledge; the disk residue computation, the 2×2 closed form, the counterexample and the §4 bound were derived in-session and machine-checked, not recalled. I have not re-read Crouzeix–Palencia verbatim, so F1 (the brief's own literature debt) is untouched and §1's "this is Berger" identification is mine, offered for checking.

---

*Offered, not self-filed. Suggested countersign items: §1 as [T]; §2 as [T]; §3 as the refutation of D4.6 position 1½ with the restatement in §3's Consequence; §4 as [T]; §5 as the correction to D3.2's profile — with the Healing Conjecture itself explicitly retained.*
