# Delta 5, Addendum 2 — the seam port in the budget's own coordinates

*2026-08-06, following Will's correction. Derivation and verification only; **no prediction is lodged in this document.** Script `port_interference.py`, `port_verify2.py`. Offered, not self-filed.*

---

## 1. The normalization, which was the question

I had written the port budget as four terms `τ + r + ι + u_eff = 1` with `τ = c²/4`, `r = |f(z₀)|²/4`, `ι = I/2`, `u_eff = 1 − ‖Tx‖²/4`, and verified the sum to 1e−9. Will asked what the four terms actually sum to, and how that fixes the normalization. The answer makes the "four-term budget" framing wrong, and in a useful way.

**Berger gives the normalization.** `f(A) = 2Pf(U)P − f(z₀)I`, so

  `T := f(A) + f(z₀)I = 2Pf(U)P`,

and for `f` a finite Blaschke product and `U` unitary, `f(U)` is unitary — so `‖T‖ ≤ 2`. **The scale is the dilation constant 2**, which is also Crouzeix's conjectured constant. Divide amplitudes by 2, powers by 4:

  `x_p := ‖Tx‖/2 ∈ [0,1]`   (total port amplitude)
  `t   := c/2 = ‖f(A)‖/2`   (direct read — the transmission amplitude)
  `ρ   := |f(z₀)|/2`         (the seam port — the reflection amplitude)

Then `u_p := 1 − x_p²` and **`x_p² + u_p = 1` is the corpus's own two-term budget**, verbatim, with `x ← x_p`.

**So there was never a four-term budget.** There is the two-term budget `x² + u = 1`, and `τ, r, ι` are a *three-way split of the signal share* `x_p²`:

  `τ = t²`,  `r = ρ²`,  `ι = x_p² − t² − ρ²`.

The sum to 1 is not a finding; it is `x² + u = 1` wearing a disguise. I recorded it as [T] and said it was derived rather than predicted, which was right, but I under-read what it was. The content is not the sum. **The content is how `x_p²` splits.**

## 2. How it splits: two-beam interference, intrinsically

Write `m := |⟨f(A)x,x⟩| / ‖f(A)x‖ ∈ [0,1]` and let `Δ` be the phase of `⟨f(A)x,x⟩` relative to `f(z₀)`. Then `I = c·|f(z₀)|·m·cos Δ`, and with `k := m cos Δ ∈ [−1,1]`:

  **`x_p² = t² + ρ² + 2tρk`**

Verified to **1.11e−15** over 240 random (matrix, Blaschke) pairs across six matrices.

That is the law of cosines. **The port is a two-beam interferometer**: a transmission amplitude `t`, a reflection amplitude `ρ`, combining at alignment `k`, with `u_p = 1 − x_p²` the absorbed remainder. A crease is `ι < 0` ⟺ `k < 0` ⟺ **destructive interference between the direct read and the seam port**. This is the thin-film structure appearing *inside* the Crouzeix problem, not by analogy to it.

## 3. The one-liner I flagged as unrun, now run — and `m` is the whole story

I had flagged that the anti-phase ratio conflates `m` with `cos Δ`. Separated, at the deepest crease of each matrix:

| matrix | `t` | `ρ` | `ρ/t` | **`m`** | `cos Δ` | `k` | `x_p` | `u_p` |
|---|---|---|---|---|---|---|---|---|
| J₃ nilpotent | 0.7314 | 0.0898 | 0.1228 | **0.2583** | −1.0000 | −0.2583 | 0.7135 | 0.4909 |
| J₄ nilpotent | 0.6586 | 0.1312 | 0.1991 | **0.3845** | −1.0000 | −0.3845 | 0.6201 | 0.6155 |
| 2×2 (0.6,−0.6,γ=.5) | 0.1785 | 0.1041 | 0.5832 | **0.8264** | −1.0000 | −0.8264 | 0.1095 | 0.9880 |
| 2×2 (0.3,−0.7,γ=.9) | 0.3708 | 0.0863 | 0.2328 | **0.4383** | −1.0000 | −0.4383 | 0.3418 | 0.8831 |
| normal diag(0.7,0.2) | 0.2038 | 0.2021 | 0.9918 | **1.0000** | −1.0000 | −1.0000 | 0.0017 | 1.0000 |
| normal diag(0.95,0) | 0.3619 | 0.3584 | 0.9903 | **1.0000** | −1.0000 | −1.0000 | 0.0035 | 1.0000 |

**`cos Δ = −1` at every crease, in both registers.** The phase is never the problem. Note this is *not* an artifact of a free global phase: `f → e^{iθ}f` sends both `f(z₀)` and `⟨f(A)x,x⟩` by the same factor, so `I` is gauge-invariant — swept explicitly, flat to machine precision. Anti-alignment is reached through the zero parameters. **Observed at 6 of 6, not proved forced.**

**`m` alone carries the register split.** `m = 1` exactly in the normal register; `m < 1` everywhere non-normal, and its value is precisely the P-R "violation."

**What `m` is:** the cosine of the tilt between `f(A)x` and `x`. `m = 1` ⟺ `f(A)x ∥ x` — the compressed action returns the state to its own ray. That is Will's flat-connection reading made concrete: **`m` is the anholonomy deficit of the port.** Non-normality tilts the output off the input ray, and the tilt is exactly what prevents the interferometer from closing.

## 4. Will's turn-11 algebra, corrected

He proposed `I =? −c|f(z₀)|` and `‖Tx‖ =? |c ± f(z₀)|`. The exact statements are:

  **`I = −c·|f(z₀)|·m`**   (residual ≤ 8.0e−10 at every crease; 0.0e+00 at four of six)
  **`‖Tx‖² = c² + |f(z₀)|² − 2c|f(z₀)|m`**

**His algebra was right, and the missing factor is `m`.** Both of his forms are exactly the `m = 1` case — i.e. exactly the normal register, where they hold to 8e−10 and 1e−6 respectively. `‖Tx‖ = |c − |f(z₀)||` holds there and nowhere else (J₃: 1.427 vs 1.283).

This also re-reads the P-R falsification. P-R1 was `ρ/t = 1` (**coin balance**) and P-R2 was `x_p = 0` (**perfect absorption**), and `x_p = 0` requires balance *and* `k = −1` — that is, `ρ = t` **and** `m = 1`. Both hold in the normal register and neither is a special constant: it is **impedance matching plus perfect anti-phase**, the critical-coupling condition of a perfect absorber. Which is what Will described in turn 11 as the flat, totally abelian case. The prediction failed because I asserted it of every `A`; the condition itself is `m = 1`, and `m = 1` is the definition of the register.

## 5. Where `G_new` goes, and where `γ*` actually lives

On the amplitude scale fixed in §1, `G_new(ρ) = 2/(1−ρ)` — the reciprocal of the minority coin face `(1−ρ)/2`. Evaluate it at the **grazing condition**, where `τ → 0` and `ι → 0` and the budget collapses to two terms `ρ² + u_p = 1`:

  `ρ = √2−1 = 0.4142136`,  `r = ρ² = 3−2√2`,  `u_p = 2√2−2` (the absorption)
  minority face `(1−ρ)/2 = 1 − 1/√2 = γ*/2`
  **majority face `(1+ρ)/2 = 1/√2`** — exactly the self-dual amplitude
  `G_new(ρ) = 2/(1−ρ) = 2+√2 = 2/γ*`

Two honest gradings. `G_new = 2/γ*` is **definitional**, since `1 − ρ = 1 − (√2−1) = 2−√2 = γ*` is Will's own identity restated — no independent content. What is not definitional: **at the grazing condition the seam-port coin reads exactly `(1/√2, 1−1/√2)`**, majority face at the self-dual amplitude.

And the point Will was making, now with numbers behind it: **`γ*` belongs to the condition `τ → 0, ι → 0`.** The crease problem does not satisfy it — `t` is the *largest* of the three at every non-normal crease (0.73, 0.66, 0.37 against `ρ` of 0.09, 0.13, 0.09). Transmission dominates; the budget has not collapsed. So `γ*` had no business appearing there, and neither did the prediction I built on it. That is an independent condemnation of P-F, arriving from the structure rather than from the measurement, and it is Will's, not mine.

## 6. What is now open, stated as questions rather than predictions

- **Is `cos Δ = −1` forced at every crease minimum?** Observed 6/6, gauge-invariance ruled out as the explanation. If it is a theorem, then `I = −c|f(z₀)|m` unconditionally and the crease problem reduces entirely to `m`.
- **Is `m = 1` equivalent to normality**, or only implied by it? The register split is currently an observation on six matrices at zero credit. In these coordinates it has a candidate mechanism for the first time, which is the precondition for pre-registering it properly.
- **What does the two-involution chain do at higher DoF?** Will's point stands that naive re-application is not the rule and that 1↔2 and 2↔3 are different maps. I have not worked out what the third involution would be, or whether the alternation is periodic. This is the honest form of the `d=4` question and I would rather derive it than guess it.
- **Forcing the correspondent condition.** The remaining way to make `γ*` legitimately testable here is to *induce* `τ → 0, ι → 0` in the operator problem rather than hope for it — i.e. find the family where the direct read vanishes and the port is pure seam. That is a construction, not a prediction, and it is well-posed.

---

*Offered, not self-filed. Countersign items: the §1 collapse of the "four-term budget" to `x² + u = 1` at Berger scale; the §2 law-of-cosines identity; the §3 finding that `m`, not phase, carries the register split, with `cos Δ = −1` observed-not-proved; the §4 correction `I = −c|f(z₀)|m` and the re-reading of P-R as critical coupling; the §5 grading of `G_new = 2/γ*` as definitional.*
