# Charge 1 — Delta 5, Addendum 1: the healing bound in budget form, and which ½ is real

*2026-08-06, same session. Filed on Will's reading of the Delta 5 bound. Two results and one retraction. Script: `budget_form.py`, alongside the Delta 5 bundle. Offered, not self-filed.*

---

## A1.1 [T, verified] The bound is a budget statement, exactly

Will's rearrangement is exact. With the corpus gauge `G²(ρ) = 1/(1−ρ²)` and `SNR(ρ) = ρ²/(1−ρ²)`, the Delta 5 healing bound

  I ≥ (c² − ρ²) / (2(1 − ρ²))

is identically

  **I ≥ ½ [ c²·G²(ρ) − SNR(ρ) ]**   (max residual 2.8e−14 over 20,000 random (c,ρ))

and equivalently, in the two-gauge form he wrote,

  **I ≥ (c²/2) · G²(ρ) / G²(ρ/c)**   (max residual 5.0e−16).

So the floor is *half the extremal capacity read in the observable's own gauge, less the observable's own SNR* — or, in the ratio form, half the extremum times the gauge measured absolutely against the gauge measured in units of the extremum. Both are the corpus's vocabulary applied to a bound derived from Schwarz–Pick, and they are the same object.

## A1.2 [T, verified] The ½ that is real: extremality collapses the bound onto the self-dual value

Set c = 1 (extremality for normal A). Then

  bound = ½[G²(ρ) − SNR(ρ)] = ½ · 1 = **½, exactly, for every ρ**,

because `G² − SNR = 1` is the corpus's own budget identity. Verified to fifteen decimals across ρ ∈ {0, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99, 0.9999}: the ρ-dependence cancels identically.

This is the substantive half of Will's reading, and it is not decoration. The healing floor at extremality is the self-dual constant, and the *mechanism of the cancellation is the two-budgets-one-identity relation* — the same identity the atlas verifies at 30–40 dps. Reading it forward: the bound says the interference floor is a capacity difference, and at extremality every observable-dependence in that difference is eaten by the budget identity, leaving the self-dual value alone. That is an instance of the "emergent transition at self-duality rather than extremality" pattern Will named — here the transition value *is* ½ and it appears precisely because extremality is imposed.

**Honest scoping.** The mechanism underneath is Schwarz–Pick, i.e. contraction of the Poincaré metric on the disk, whose density is `2/(1−|z|²) = 2G²`. The corpus already names ℝH²/SU(1,1) as its arena (Foundations Status v2), so this is a **confirmation of the dictionary, not an independent derivation from it**: TEP predicts that a hyperbolic-contraction bound should read as a budget statement, and it does, with the identity doing visible work. That is worth something and it is less than a theorem produced by the framework. I would not claim more in a referee's hearing.

## A1.3 [retraction] The ½ that is *not* real: my witness function's constant is arbitrary

The Delta 5 counterexample used `f(z) = (z² − ½)/(1 − z²/2)`, whose zeros sit at ±1/√2 — on the self-dual circle |z|² = ½. That looked structural. **It is not.** I chose t = ½ for clean arithmetic.

Minimising I over the family `f_t(z) = (z² − t)/(1 − t z²)` on `A = diag(ρ, 0)`, Ω = unit disk, the stationarity condition is

  **ρ² t² − 2t + ρ² = 0,  t\* = (1 − √(1 − ρ⁴)) / ρ²,**

so t\* = 0.630815 at ρ = 0.95 — not ½, and not 1/√2 = 0.707107. Across ρ ∈ {0.95, 0.90, 0.80, 0.60, 0.40} the optimum runs 0.6308, 0.5106, 0.3619, 0.1862, 0.0805: no fixed constant at all, self-dual or otherwise. The delivered witness is genuinely suboptimal — I = −0.36674 at c = 0.73349, against I = −0.39793 at c = 0.63081 for t\*.

**What the optimum does have** is a clean characterisation, which is the thing worth keeping from this line:

  at t\*, **f(ρ) = −f(0) exactly**, and consequently **I = −c²**.

Verified to eight decimals at all five ρ. So within this family the deepest crease is *exact anti-phase between the direct read and the reflected read*, and its depth is minus the squared gain — full destructive interference, priced. That is a structural fact about creases; the ½ was mine.

## A1.4 What this changes

- Delta 5 §4's bound gains the budget statement of A1.1 and the extremality collapse of A1.2 as [T] readings.
- Delta 5 §3's witness gains a footnote: it is a valid counterexample and a suboptimal one; the family optimum is t\* above, with the anti-phase characterisation.
- Nothing else in Delta 5 moves. The refutation of D4.6 position 1½ stands, the corrected J₃ profile stands, and the Healing Conjecture still stands with its measured rate.

*Offered, not self-filed. Countersign items: A1.1 and A1.2 as [T] readings of the Delta 5 bound; A1.3 as a self-erratum against Delta 5 §3's implicit suggestion that the constant was chosen; the anti-phase characterisation `f(λ) = −f(0) ⟹ I = −c²` as [T] within the stated family.*
