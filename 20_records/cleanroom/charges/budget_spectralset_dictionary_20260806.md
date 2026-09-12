# The budget ↔ spectral-set dictionary — Will's `G²` guess, checked

*2026-08-06. Derivation and grading; no prediction lodged. Script `budget_spectral.py`. Offered, not self-filed.*

---

## 1. The guess was right

Will asked: *"Spectral Set characteristic correspondent with `G²(x_{d−1})`?"*

Malman–Mashreghi–O'Loughlin–Ransford (IMRN 2025) give the best current per-domain spectral-set constant as `C(Ω) = 1 + √(1 + a(Ω))`, `a(Ω) ∈ [0,1)` the analytic configuration constant, `sup_Ω a = 1`. Equivalently `C² − 2C − a = 0`.

**Substitute the budget's `G² = 1/u` for `C`:**

  `C² − 2C − a = 0`  ⟹  **`a·u² + 2u − 1 = 0`**,  `u(a) = (√(1+a) − 1)/a`

| domain | `a(Ω)` | `C = G²` | `u` | `x² = 1−u` | chain position |
|---|---|---|---|---|---|
| **disk** (Berger / Okubo–Ando) | 0 | **2** | **½** | **½** | **rung 1 — the self-dual seed** |
| sup over convex Ω | 1 | **1+√2** | **√2−1** | **2−√2 = γ\*** | **rung 2 exactly** |

**The Crouzeix spectral-set constant, as `Ω` ranges over convex sets, traces the budget's `u` from the self-dual seed down to rung 2 — and no further.** Both endpoints are the corpus's own chain values, not arbitrary numbers. The conjecture is the claim that the seed value holds everywhere; the theorem is that you never get past rung 2.

The ellipse family, from MMOR's `a = (2/π)arctan(½|b/a − a/b|)`:

| `b/a` | `a(Ω)` | `C = G²` | `u` | `x²` | `η = artanh x` |
|---|---|---|---|---|---|
| 1.00 | 0 | 2.0000000 | 0.5000000 | 0.5000000 | 0.8813736 |
| 0.70 | 0.222400 | 2.1056218 | 0.4749191 | 0.5250809 | 0.9173148 |
| 0.50 | 0.409666 | 2.1872934 | 0.4571860 | 0.5428140 | 0.9433532 |
| 0.10 | 0.873098 | 2.3686117 | 0.4221882 | 0.5778118 | 0.9965450 |
| 0.02 | 0.974539 | 2.4051828 | 0.4157688 | 0.5842312 | 1.0065954 |

## 2. Grading, before anyone asks

**`C ↦ u = 1/C` is a change of variable.** Under it the budget's central identity `G² − SNR = 1` becomes `C − (C−1) = 1` — a tautology. **The budget adds no constraint here; it relabels.** Anyone who says "the budget explains the Crouzeix constant" is wrong, and I want that in writing before the correspondence gets quoted.

**What is not trivial:** `a(Ω)` lands as the coefficient of `u²`, and its two endpoints are rung 1 and rung 2 rather than arbitrary numbers. That is a one-parameter family with both ends on the chain, which is a much stronger match than a single constant hitting a single constant, and it is not disposed of by the corpus's own TSP base-rate tombstone.

**An apparent second hit, which collapses.** At the self-dual point the corpus's transfer matrix `T = G[[1,x],[x,1]] = exp(ησ₁)` has `det T = 1`, `tr T/2 = G = √2`, and eigenvalues `e^{±η} = 1+√2` and `√2−1` — i.e. *both* Crouzeix constants and the rung-2 `u` on one matrix. **This is not two facts.** `e^{−η} = 1/e^{+η}` and `u = 1/C` are the same reciprocal relation, so seeing `1+√2` and `√2−1` together is one statement counted twice. Recorded so it does not get quoted as corroboration.

**One real chain fact it does expose:** `e^{η_n} = G²(x_{n+1})` holds **iff `x²_n = ½`** — since `e^η = G(1+x)` and `G²(x_{n+1}) = 1 + G(x_n)`, equality forces `Gx = 1`, i.e. `x² = ½`. So the rapidity–gain coincidence is a property of the self-dual seed alone and does not propagate. Consistent with Will's own point that the chain is two involutions, not one rule.

## 3. `λ_min` — the junior partner

Will asked what happens to the smallest eigenvalue at extremality, a question the corpus has never posed. For nilpotent `A` (the Delta 5 test family), `f(A) = f(0)I + N` with `N` nilpotent, so

  **`det f(A) = f(0)^n`**  — an exact ledger, verified to six decimals at every summit.

| A | `σ_max = c*` | `σ_min` | `\|f(0)\|` | `\|det f(A)\|^{1/n}` |
|---|---|---|---|---|
| J₃ | 1.99016566 | 2.16e−5 | 6.600e−3 | 6.600e−3 |
| J₄ | 1.88854382 | 5.91e−23 | 7.421e−9 | 7.421e−9 |
| J₅ | 1.77777778 | 6.77e−19 | 4.809e−10 | 4.809e−10 |

**The junior partner is spent to buy the senior one.** Driving `‖f(A)‖` toward 2 requires `f(0) → 0`, which drives `σ_min → 0` at rate `f(0)`, with the determinant as the conservation law.

**In port coordinates this is the sharp statement.** `ρ = |f(z₀)|/2 = |f(0)|/2 → 0` at the summit: **the seam port closes.** So the disk summit reaches `x_p = 1` by *pure transmission* — `ρ = 0`, `t → 1`, `k` irrelevant.

Compare the Ransford–Schwenninger counterexample, which also reaches `x_p = 1`, but by `k = −1` with `ρ = (√2−1)/2 > 0`, giving `t = 1 + ρ = (1+√2)/2`.

> **The gap between the conjectured 2 and the proven 1+√2 is exactly the difference between closing the seam port and anti-phasing it.**
>
> Closing it (`ρ → 0`) caps `t` at 1. Anti-phasing it (`k = −1`, `ρ > 0`) buys `t = 1 + ρ`. Ransford's Question 4.1 — does unitality force the constant to 2? — is the question of whether an admissible `α` can ever anti-phase a port it cannot close.

I claim no novelty for this; it is the RS example in different letters. It is offered as orientation, and it is the clearest statement of the frontier I have.

---

*Offered, not self-filed. Countersign items: §1's dictionary and its two endpoints; §2's insistence that the correspondence is a relabeling and that the transfer-matrix "double hit" is one fact; §3's determinant ledger and the close-vs-anti-phase reading of the 2 / 1+√2 gap, claimed at zero novelty.*
