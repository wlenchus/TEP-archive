# P-R run 1 — RESULT: **FALSIFIED.** K-R1, K-R2 and K-R3 all fire.

*2026-08-06, following `PREREG_selfdual_crease_locus_20260806.md`, sha256 `2b427da780a0d3698da7f3f12343d0b5021eba1f6eef318d983f0ef56ad71c29`, hashed before execution. Script `pr_test.py`, seed 20260806, degree-3 Blaschke, 14 restarts per matrix, all 14/14 converged on every matrix. Offered, not self-filed.*

---

## 1. Verdict

**P-R1 (`|f(z₀)|/c = 1` at the global crease minimiser) is FALSIFIED.** Four of five crease-admitting matrices violate it, against a kill threshold of two. P-R2 (`‖Tx‖ = 0`) and P-R3 (`I = −c²`) fail on the same four. Per §4 of the pre-registration, **no weakened form of P-R1 is available and I am not offering one.** The reflectance-balance reading of the crease locus, as predicted, is dead.

| matrix | `|f(z₀)|/c` | `‖Tx‖/c` | `I/(−c²)` | verdict |
|---|---|---|---|---|
| J₂ nilpotent *(control)* | — | — | — | no crease, `min I = +4.1e−36` — P-R4 confirmed, costless |
| **J₃ nilpotent** | 0.1228 | 0.9755 | 0.0317 | **violates all three** |
| **J₄ nilpotent** | 0.1991 | 0.9415 | 0.0766 | **violates all three** |
| **2×2 non-normal (0.6, −0.6, γ=0.5)** | 0.5832 | 0.6133 | 0.4820 | **violates all three** |
| **2×2 non-normal (0.3, −0.7, γ=0.9)** | 0.2328 | 0.9220 | 0.1021 | **violates all three** |
| normal diag(0.7, 0.2), degree 3 | **0.9918** | **0.0082** | **0.9918** | holds, all three |

## 2. What survives, and what it is not

The one row that holds is the **normal** one — and it holds essentially exactly: `|f(z₀)|/c = 0.9918`, `u_eff = 0.999997`, `I/(−c²) = 0.9918`. It was blind: §5 of the pre-registration excluded only the degree-2 family on `diag(ρ,0)`; this is `diag(0.7,0.2)` at degree 3, computed for the first time here.

So the observed pattern is a **register split**: the self-dual crease locus is the law of the *normal* register and has no purchase where the operator is non-normal. In the budget shares this is legible — at the deepest crease, the normal case sits at `τ = 0.0415, r = 0.0409` (balanced, total absorption), while J₃ sits at `τ = 0.535, r = 0.008` (transmission-dominated, reflectance nearly absent, `u_eff = 0.49`).

**This is not a rescue and must not be counted as one.** P-R1 predicted the balance at *every* crease-admitting A; it does not hold there. That a scoped version survives is an *observation made after seeing the data*, and by this corpus's own rules it carries no evidential weight until it is pre-registered and tested on matrices not yet examined. I am recording it as a candidate, at zero credit.

The candidate, stated so it can be lodged properly later: *the self-dual crease locus governs exactly where transmission vanishes structurally — i.e. the normal register — and the non-normal register has a different, transmission-dominated crease mechanism.* Note this is consonant with Will's own framing (self-duality constrains transmission to zero), which is precisely why it needs an independent test rather than a nod: the framing that generated the falsified prediction would also generate this one.

## 3. What is confirmed

The §1 budget identity of the pre-registration — `τ + r + ι + u_eff = 1` with `τ = c²/4`, `r = |f(z₀)|²/4`, `ι = I/2`, `u_eff = 1 − ‖Tx‖²/4` — held to **1e−9 on every row**. That was derived, not predicted, and it stands as [T]: the interference functional is a genuine budget component and a crease is exactly negative interference share.

That is the whole of what this run supports.

## 4. Cost, stated plainly

This was the corpus's first prediction that could resolve against a TEP reading, and **it did.** Two consequences I am not going to soften:

1. The reflectance/port reading of the crease *locus* is wrong as I formulated it. Delta 5's port reading of the crease *mechanism* (I as a reflectance × direct-read × phase cross-term) is untouched — that is an identity, not a prediction — but the inference from "the crease is a reflectance cross-term" to "the deepest crease sits at reflectance balance" does not survive contact.
2. Two predictions have now been lodged in twenty-four hours. One was inconclusive by its own coverage bar; one is falsified. The honest tally of the corpus's predictive column is **0 for 2**, and that is a truer statement of where the framework stands than anything in the 08-06 adjudication I wrote yesterday.

I would rather have this on the record than a third attempt tuned until something lands.

## 5. Standing

- **P-R1, P-R2, P-R3: dead.** P-R4 (the J₂ control) confirmed and explicitly costless.
- **P-H (healing-exponent universality): still open**, still unrescued, run 1 still inconclusive.
- **The port budget identity: [T], confirmed on eight configurations.**
- **New candidate (zero credit until pre-registered):** the register split of §2.
- Method note: unconstrained minimisation worked exactly as intended — 14/14 convergence on every matrix, no coverage failures. The thin-shell pathology that made P-H run 1 inconclusive is specific to level-constrained search, as diagnosed.

---

*Offered, not self-filed. Countersign items: the FALSIFIED verdict on P-R1–P-R3; the §2 refusal to credit the surviving normal-register pattern; the §3 budget identity as [T]; the §4 tally.*
