# AMENDMENT 1 to P-U — closing §8.1 at a stated bound, in the negative or otherwise

*Filed 2026-08-06 after the P-U main verdict was in hand and **before running any integer-relation search**. Amends `PREREG_layer2_passage_control_audit_20260806.md`, sha256 `4793e8df71b6248795521e58eace539e4aab61b56ddb1b1add7f19415abe81d1`. Offered, not self-filed.*

---

## 1. Why an amendment and not a new filing

The P-U run produced something the main pre-registration did not anticipate: **the thin-film problem reduces exactly**, in the limit `kd → 0` at fixed `ρ = cosθ/kd` and `ζ = σ_n kd²`, to a **two-parameter Fabry–Pérot pair with no `kd` in it at all**:

  `s = √(iζ)`, `m = ρs`, `r₁₂ = (m−1)/(m+1)`, `b = e^{2is}`
  `r = r₁₂(1−b)/(1−r₁₂²b)`,  `t = (1−r₁₂²)e^{is}/(1−r₁₂²b)`

using the exact identity `r₁₂² + t₁₂t₂₁ = [(m−1)² + 4m]/(m+1)² = 1`. Verified against the full oblique-TM slab calculation: the residual is `4.2e−5, 4.2e−7, 4.2e−9, 4.2e−11` at `kd = 1e−2, 1e−3, 1e−4, 1e−5` — clean `O(kd²)` convergence, so the reduction is exact and the corrections are finite-thickness.

**This changes the status of the corpus's own open question §8.1** (*"Algebraic identification of R=T peak A_peak ~ 0.6078. Real, universal, but not silver-ratio. Is it transcendental?"*). April could not settle it because the number was known to four digits from a `kd`-limited numerical sweep. It is now the solution of a **two-equation stationarity system in two real unknowns**, computable to arbitrary precision. At that point "is it algebraic" stops being a fishing question and becomes decidable at a stated bound.

## 2. What I am not doing

I refused this morning to fit `A*`, citing the corpus's 07-25 TSP tombstone. **That refusal stands and this amendment does not relax it.** The difference is precisely stated:

- **Fitting** = search an unbounded space of expressions, at 3–4 digits, after a falsification, and report the closest hit. Base rate of a spurious graze: order one-half. Forbidden.
- **This** = fix the search space and the acceptance bar **in advance and in writing**, evaluate the target to 50 digits, and report the outcome **including the negative**, which is the outcome I expect and which closes an open corpus question at a stated bound.

The asymmetry that makes this legitimate: **a negative here is publishable and useful, and a positive is checkable to 30+ digits.** A fit has neither property.

## 3. Targets

Computed in `mpmath` at ≥ 50 decimal digits from the reduced model, by solving `{R − T = 0, ∂A/∂ρ|_locus = 0}`:

`A*`, `R* = T*`, `ρ*`, `ζ*`, `ξ* = ρ*ζ*`.

Float64 values already in hand, for the record: `A* = 0.607827506222574`, `R* = T* = 0.196086246888713`, `ρ* = 0.767261842658182`, `ζ* = 1.908943025034370`, `ξ* = 1.464659142917355`.

## 4. The search space — fixed here, not adjustable afterwards

**(S1) Integer-relation / minimal polynomial.** For each target `v`, run PSLQ on `[1, v, v², …, v^d]` for `d = 2, 3, 4, 5, 6`.
**Acceptance requires all three:** (a) `d ≤ 6`; (b) `max|cᵢ| ≤ 1000`; (c) the relation verifies to `≥ 30` decimal digits when the target is recomputed independently at 80 digits.

**(S2) A named finite candidate list, fixed now.** `A*` compared against, at 1e−12: `2−√2`; `2√2−2`; `3−2√2`; `1/φ`; `√(1+√2)/(1+√(1+√2))` (the falsified rung-3 value); `3/5`; `5/8`; `√2−1+…` no — the list is exactly these seven, plus the two-term forms `a + b√2` and `a + b√3` with `a, b` rational of denominator `≤ 12`.

**(S3) One structural candidate, and only one.** `ζ*` versus `π²/8, π²/4, π²/2, π², 2, 3/2, √2, 2√2` at 1e−10 — motivated by `s = √(iζ)` entering only through `e^{2is}`, so a `ζ` making `2s` a rational multiple of `π` would be a genuine mechanism rather than a coincidence.

**Nothing else is searched.** No unbounded symbolic regression, no continued-fraction mining, no constant-hunting services, no widening if S1–S3 come back empty.

## 5. Decision rule

- **HIT** — some target satisfies S1 under (a)+(b)+(c), or matches an S2/S3 candidate at the stated tolerance. Then §8.1 is **closed in the positive**, and I report which target, which relation, and to how many digits it verifies. I will additionally state plainly whether the hit is TEP-shaped or not, because `A*` coming out as, say, a root of a cubic with no `√2` in it would close §8.1 while giving the framework nothing.
- **NO IDENTIFICATION** — nothing passes. Then §8.1 is **closed in the negative at the stated bound**: *`A*` is not algebraic of degree ≤ 6 with integer coefficients ≤ 1000, and is none of the named candidates.* That is a real result and it retires the corpus's standing hope that this number is silver-ratio algebraic in a not-yet-identified form.
- **Either way**, the reduced model of §1 is reported as the substantive product, because it converts an open numerical question into a closed analytic one.

**Expected outcome, stated in advance so I cannot claim prescience afterwards: NO IDENTIFICATION.** April's §7.2 already found no low-degree polynomial at four digits, and the transcendental `e^{2is}` in the stationarity system is exactly the structure that produces non-algebraic critical points.

---

*Offered, not self-filed. Countersign items: the §2 distinction between this and fitting; the §4 search space as fixed before running; the §5 commitment to report the negative as a closure rather than as a null result.*
