# Charge 1 — REASSESSMENT: the Crouzeix work is set on settled ground, and the Healing Conjecture is a 2020 theorem

*2026-08-06. Supersedes the standing framing of `charge_brief_crouzeix_closed_boundary_budget` and of `charge1_crouzeix_Delta5` §§1–4. Literature verified against primary sources this session. Offered, not self-filed.*

**This is the most consequential thing I have found in two days, and it goes against the corpus.**

---

## 1. The finding, in three sentences

The Crouzeix charge is set in the **disk** (`W(A) ⊆ 𝔻`, `‖f‖_∞ ≤ 1` on the disk). In that setting the constant **2 is a theorem — Berger (1965) plus Okubo–Ando (1975)** — and has been for sixty years; Crouzeix's conjecture has content only when the supremum is taken over `W(A)` itself and `W(A)` is *not* a disk. And the **Healing Conjecture** — the load-bearing conjecture of the charge — is a corollary of a published theorem: **Bickel, Gorkin, Greenbaum, Ransford, Schwenninger, Wegert, CMFT 20 (2020), Theorem 4.1 / Remark 4.2.**

## 2. Why the disk is not the conjecture

| statement | status |
|---|---|
| `w(A) ≤ 1 ⟹ ‖p(A)‖ ≤ 2·sup_𝔻\|p\|` | **Theorem.** Berger 1965 (unitary 2-dilation) + Okubo–Ando, *Manuscripta Math.* **16** (1975) 385–394 (complete 2-spectral set). |
| `W(A) = a disk ⟹ ‖p(A)‖ ≤ 2·sup_{W(A)}\|p\|` | **Theorem** — same result. |
| `W(A) ⊊ 𝔻 ⟹ ‖p(A)‖ ≤ 2·sup_{W(A)}\|p\|` | **Open** — the Okubo–Ando sup is over the larger set. |

Every computation in Delta 5 uses `nilpotent_W_unit(n)` — a Jordan block scaled so `W(A)` *is* the closed unit disk — and measures `f` on that disk. That is row one. It is also recovered twice inside the modern framework: Caldwell–Greenbaum–Li (arXiv:1707.08603, §6), and Malman–Mashreghi–O'Loughlin–Ransford (IMRN 2025) as the case `a(𝔻) = 0` of their `K ≤ 1 + √(1+a(Ω))`, where they explicitly note it "recovers the Okubo–Ando result."

**The disk reduction I derived yesterday** — `g_f ≡ conj(f(z₀))`, the Cauchy transform of `f̄` being constant on a disk — **is also already published**, in Caldwell–Greenbaum–Li §6. I derived it independently and did not know it. That is a competence signal and nothing more; it has zero priority.

## 3. The Healing Conjecture is Remark 4.2

**Bickel et al. 2020, Theorem 4.1.** If `f` is extremal for `(A,Ω)`, `x` an associated extremal unit vector, and `f = f₁f₂` with `f₁,f₂ ∈ H^∞₁(Ω)`, then `⟨f₁(A)x, (‖f(A)‖²I − f₂(A)*f₂(A))x⟩ = 0`.

**Remark 4.2** (`f₁ = f`, `f₂ = 1`): `(‖f(A)‖² − 1)⟨f(A)x,x⟩ = 0`, hence

  **`‖f(A)‖ > 1 ⟹ ⟨f(A)x,x⟩ = 0`.**

In the disk `g_f` is the constant `conj(f(z₀))`, so the corpus's interference functional is `I = Re[conj(f(z₀))·⟨f(A)x,x⟩]`, and Remark 4.2 gives **`I = 0` at the summit, as a theorem**, whenever `c* > 1`. Creases heal because extremality annihilates the numerical-range term. That is the whole mechanism.

Verified numerically against my own machinery:

| A | `c* = max‖f(A)‖` | `\|⟨f(A)x,x⟩\|` at summit | `I` at summit |
|---|---|---|---|
| J₃ nilpotent | 1.99016566 | 1.31e−2 | 8.6e−5 |
| J₄ nilpotent | 1.88854382 | **1.51e−11** | **1.14e−22** |
| J₅ nilpotent | 1.77777778 | **3.01e−10** | **4.54e−20** |

and the approach, which is what I measured yesterday as an exponent:

| `c/c*` | `\|⟨f(A)x,x⟩\|` | `min I` |
|---|---|---|
| 0.900 | 1.17e−1 | −7.41e−3 |
| 0.950 | 5.61e−2 | −1.65e−3 |
| 0.990 | 1.15e−2 | −6.73e−5 |
| 0.999 | 1.45e−3 | −1.07e−6 |

`|⟨f(A)x,x⟩|` is **linear** in the gap `(1 − c/c*)`; `I` is **quadratic**. My measured healing exponent of 2.3 was that quadratic, read coarsely off a sparser grid. The exponent is real; it is the rate at which a first-order extremality condition is approached, not a new law.

## 4. What this does to the charge, item by item

| item | standing before | standing now |
|---|---|---|
| Crouzeix constant 2 in this setting | open conjecture under attack | **Berger 1965 / Okubo–Ando 1975** |
| Disk reduction `g_f ≡ conj(f(z₀))` | my derivation | correct, independently derived, **published — Caldwell–Greenbaum–Li 2017** |
| **Healing Conjecture** | the charge's load-bearing conjecture | **Bickel et al. 2020, Rmk 4.2** |
| Healing exponent ≈ 2.3 | measured law | correct measurement of the approach to a known first-order condition |
| Normal-register healing bound `I ≥ (c²−ρ²)/(2(1−ρ²))` | my theorem | true, and about **normal** matrices — where Crouzeix is trivial with constant **1**, not 2 |
| Refutation of D4.6 position 1½ | internal correction | **stands** — still a valid internal correction |
| Correction of D3.2's crease numbers | internal correction | **stands** |
| Port budget / law-of-cosines coordinates | new framing | **correct and elementary**; the same expansion appears in Schwenninger–de Vries (arXiv:2302.05389, Thm 5). Zero credit as mathematics; some value as exposition. |

**Net contribution of the Crouzeix charge to the literature: zero.** Net contribution to the corpus: a set of valid internal corrections, and a research programme pointed at ground that was settled before it started.

I want to be plain that this includes my own work of the last two days. I proved a theorem about the trivial case, re-derived a 2017 lemma, and numerically confirmed a 2020 theorem while calling it a conjecture. The protocol caught none of it, because the protocol checks whether I moved the bar after the run — not whether the problem was open before it.

## 5. Where the frontier actually is

Three targets, all verified open as of 2026, in order of how well the corpus's existing machinery fits them.

**(i) Ransford's Question 4.1 — the unitality gap.** *(Ransford–Schwenninger, SIMAX 39 (2018) 342–345; formalized as Ostermann–Ransford, arXiv:2011.10422, Conjecture 1.2. An affirmative answer proves Crouzeix's conjecture.)*

Ransford–Schwenninger showed the Crouzeix–Palencia framework is **sharp**: from the two hypotheses `‖g‖_Ω ≤ ‖f‖_Ω` and `‖f(T)+g(T)*‖ ≤ 2‖f‖_Ω` alone, no constant below `1+√2` is obtainable. Their witness is `T = [[1,1],[0,0]]`, `Ω` two small disks about `0` and `1`, `α(f) = −conj(f(0))` on `Ω₀` and `−conj(f(1))` on `Ω₁`. The only property their `α` lacks that the true Cauchy transform has is **unitality**: theirs sends `1 ↦ −1`.

In the port coordinates this is unusually legible. Writing `t = ‖f(A)x‖/2`, `ρ = ‖g(A)*x‖/2`, `x_p = ‖(f(A)+g(A)*)x‖/2 ≤ 1`, and `k` the alignment, **Crouzeix's conjecture is exactly `t ≤ 1`**, and `x_p² = t² + ρ² + 2tρk`. At the RS extremal, computed:

  `t = (1+√2)/2 = 1.20710678`,  `ρ = (√2−1)/2 = 0.20710678`,  **`k = −1` exactly**,  **`x_p = 1` exactly**, `u_p = 0`

so `x_p² = (t−ρ)² = 1` and **`t = 1 + ρ`**. That is the sharpness in one line: *at perfect anti-phase with the port fully open, the signal exceeds 1 by exactly the reflection amplitude*, and `2t = 2 + 2ρ = 1+√2`.

And at the unit function, the two regimes are the two ends of the interference axis:

| | `t` | `ρ` | `k` | `x_p` | `u_p` |
|---|---|---|---|---|---|
| unital, `α(1) = +1` | 0.5 | 0.5 | **+1** | 1 | 0 |
| RS, `α(1) = −1` | 0.5 | 0.5 | **−1** | 0 | 1 |

Same amplitudes, opposite alignment: fully open port versus total absorption. **Question 4.1 is the question of whether pinning the interferometer to fully constructive at `f ≡ 1` forces `t ≤ 1` everywhere.** That is the entire gap between `1+√2` and `2`.

I claim **no novelty** for any of this. The expansion is elementary and the people who posed the question certainly see it. What the coordinates buy is that the obstruction and the crack become a single picture, which is worth something for orientation and nothing as mathematics.

**(ii) The ellipse.** Malman–Mashreghi–O'Loughlin–Ransford, IMRN 2025, give `K(a,b) = 1 + √(1 + (2/π)arctan(½|b/a − a/b|))` — strictly between `2` and `1+√2` for every non-circular ellipse, `→ 2` as the ellipse rounds, `→ 1+√2` as it degenerates. **The conjecture is open for every non-circular ellipse.** This is the natural next domain after the disk: `g_f` is genuinely non-constant, so the interference functional has real content instead of collapsing to a scalar; there is a published constant to beat; and the machinery already written transfers with the harmonic-measure kernel `μ(σ,z) = (1/π)Re[ν(σ)/(σ−z)]` swapped in. **This is where I would take the charge.**

**(iii) General 3×3.** Open. `3×3` nilpotent (`A³ = 0`) is settled (Crouzeix, SIMAX 2016); `3×3` non-cyclic is settled (O'Loughlin–Virtanen, LAA 2024); the general case is not.

Also worth recording as adjacent open problems the corpus is well-placed for: **Greenbaum's AIM Problem 1.7** — *when does `‖f(A)+g(A)*‖ ≥ ‖f(A)‖` hold, particularly for `f = B∘φ` with `B` a Blaschke product?* — which is `t ≤ x_p`, and which the corpus has been computing without knowing it was a problem of record.

## 6. What I recommend

**Move the charge to the ellipse.** It is one domain over, it is open, the machinery transfers, and there is a published constant to measure against. The first honest deliverable there is not a prediction: it is *does the interference functional go negative at extremal pairs when `g` is non-constant* — the exact question Bickel et al.'s Theorem 4.1 leaves open outside the disk, and the exact question the corpus's numerics are built to answer.

**And add a stamp.** The protocol failed here in a way pre-registration cannot catch. Proposed for the Spine V3 kit, alongside C13:

  **C14 — "before attacking an open problem, verify it is open."** Cite the primary source establishing the *current* status of the exact statement, in the exact setting, at the top of the charge brief. A conjecture in one domain may be a theorem in the domain you are actually computing in.

---

## Sources

Crouzeix & Palencia, *The numerical range is a (1+√2)-spectral set*, SIAM J. Matrix Anal. Appl. **38** (2017) 649–655 · [arXiv:1702.00668](https://arxiv.org/abs/1702.00668)
Ransford & Schwenninger, *Remarks on the Crouzeix–Palencia proof…*, SIMAX **39** (2018) 342–345 · [arXiv:1708.08633](https://arxiv.org/abs/1708.08633)
Ostermann & Ransford, *An abstract approach to the Crouzeix conjecture* · [arXiv:2011.10422](https://arxiv.org/abs/2011.10422)
Bickel, Gorkin, Greenbaum, Ransford, Schwenninger, Wegert, *Crouzeix's Conjecture and Related Problems*, Comput. Methods Funct. Theory **20** (2020) 701–728 · [arXiv:2006.04901](https://arxiv.org/abs/2006.04901)
Caldwell, Greenbaum, Li, *Some Extensions of the Crouzeix–Palencia Result* · [arXiv:1707.08603](https://arxiv.org/abs/1707.08603)
Malman, Mashreghi, O'Loughlin, Ransford, *Double-layer potentials, configuration constants…*, IMRN **2025** no. 8, rnaf084
Malman, Mashreghi, O'Loughlin, Ransford, *On the Crouzeix ratio for N×N matrices* · [arXiv:2409.14127](https://arxiv.org/abs/2409.14127)
Schwenninger & de Vries, *On abstract spectral constants* · [arXiv:2302.05389](https://arxiv.org/abs/2302.05389)
Okubo & Ando, *Constants related to operators of class C_ρ*, Manuscripta Math. **16** (1975) 385–394
O'Loughlin & Virtanen, *Crouzeix's conjecture for classes of matrices*, Linear Algebra Appl. (2024) · [arXiv:2306.12183](https://arxiv.org/abs/2306.12183)
[AIM problem list on Crouzeix's conjecture](http://aimpl.org/crouzeix/1/) — Problems 1.2 (Ransford) and 1.7 (Greenbaum)

---

*Offered, not self-filed. Countersign items: §2, that the charge's setting is the settled case; §3, that the Healing Conjecture is Bickel et al. 2020 Rmk 4.2; §4's line-by-line regrade including of my own two days; §5(i)'s port reading of the RS obstruction, claimed at zero novelty; the §6 recommendation to move to the ellipse; stamp C14.*
