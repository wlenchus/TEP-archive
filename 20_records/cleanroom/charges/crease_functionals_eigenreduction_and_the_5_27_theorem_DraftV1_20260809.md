# The two crease functionals — eigenreduction, the register-split theorems, and an exact −5/27 for J₂

*DraftV1, 2026-08-09, Claude (Fable 5), on Will's open invitation ("formalization and explicit testing on your most motivated inclination"). Executes D-1/D-2 of the port-wiring queue. Scripts: `register_split.py` (seed 20260809) + two verification blocks, delivered alongside; predictions P-a/P-b/P-c were written into the script header before sections C/D ran (same-session, not hashed — disclosed as such). Training-prior: Schwarz–Pick, numerical-range convexity, and singular-vector basics are weights-knowledge; every theorem below was derived in-session and machine-checked, none recalled. This document contains one retraction of its own first reading (§0), made before filing. Offered, not self-filed.*

---

## 0. Honest bite first: a near-miss erratum, dissolved by own-words reading

My first run found deep creases on J₂ — where Delta 5 §5 records the adversarial infimum as **exactly 0** and P-R4 recorded "no crease," both [T]-adjacent. For about twenty minutes this looked like an erratum against Delta 5. It is not, and the reason is the finding: **the corpus and I were computing two different functionals.** Delta 5 §2/§5 evaluates the interference at the *extremal vector* (x = top right-singular vector of f(A); "an associated extremal unit vector," Bickel-aligned), with level constraints `c ≥ θ·c*`. My computation minimized over *all* unit states. Read against Delta 5's own words, the corpus's claims are correct under its functional — verified again below on the very witness that separates them. The distinction, once drawn, turns out to carry theorems.

Define, for `f` holomorphic on 𝔻̄ with `‖f‖_∞ ≤ 1`, `W(A) ⊆ 𝔻`, `z₀ = 0`, `I(f,x) = Re[conj(f(0))·⟨f(A)x,x⟩]`:

- **I_ext(f) := I(f, x_top(f))** — the **state-extremal** crease functional (the corpus's, throughout Delta 5 / Addenda / P-R);
- **Ĩ(f) := min_{‖x‖=1} I(f,x)** — the **state-worst** crease functional (new here).

Always `Ĩ ≤ I_ext`. The port budget and the law of cosines hold per-state for both. The healing/summit story (Bickel Rmk 4.2's extremality annihilation) is *state-extremal* physics; the state-worst functional probes the port itself, over every read the port could be asked to make.

## 1. T1 [T] — the eigenreduction: the state-worst crease is a support function

**Theorem 1.** `I(f,x) = ⟨H_f x, x⟩` with `H_f := ½(conj(f(0))·f(A) + f(0)·f(A)*)` Hermitian; hence

  **`Ĩ(f) = λ_min(H_f)`**, attained at the ground state of `H_f`.

Equivalently, writing `e := f(0)/|f(0)|` (for `f(0) ≠ 0`; `I ≡ 0` otherwise): `Ĩ(f) = |f(0)| · min Re[ē·W(f(A))]` — **the crease read is the directed support function of the numerical range of `f(A)` in the `−f(0)` direction.** A state-worst crease exists iff `W(f(A))` protrudes past the hyperplane through 0 normal to `f(0)`.

*Proof.* `Re[conj(f0)⟨Fx,x⟩] = ⟨½(conj(f0)F + f0F*)x, x⟩`; Rayleigh–Ritz. The support form is the definition of `W`. ∎ *(Machine check: identity to 6.9e−18 over 200 random `(A,f,x)`; Rayleigh bound never violated.)*

**Instrument consequence.** The x-search in every crease computation is now *exact and free* — one Hermitian eigenproblem per `f`. The near-summit feasibility pathology that made P-H run 1 inconclusive was a property of joint `(f,x)` search; for the state-worst functional it no longer exists, and for the state-extremal functional the x-half is likewise closed-form (top singular vector). Run 2 of anything in this corner should be built on this.

## 2. T2 [T] — the register split is definitional, in both functionals

**Theorem 2 (state-worst form).** Let `x` be any eigenvector of `H_f` (in particular the minimizer). Then `m(x) = |⟨f(A)x,x⟩|/‖f(A)x‖ = 1` **iff** `x` is a *reducing* eigenvector of `f(A)` (a joint eigenvector of `f(A)` and `f(A)*`).

*Proof.* (⇐) immediate. (⇒) `m = 1` gives `f(A)x = μx` (Cauchy–Schwarz equality). Then `f0·f(A)*x = 2H_f x − conj(f0)f(A)x = (2λ − conj(f0)μ)x`, so `x` is also an eigenvector of `f(A)*`. ∎

**Theorem 2′ (state-extremal form).** At `x_top`, `m = 1` iff the norm `‖f(A)‖` is attained on an eigenvector of `f(A)`.

**Corollaries.** (i) `A` normal ⇒ `m = 1` identically at the optimum, both functionals. (ii) `f(A)` with no reducing eigenvector (e.g., the nilpotent Jordan family: `f(A) = f(0)I + N`, whose only eigenvector `e₁` has `‖f(A)e₁‖ = |f(0)| < ‖f(A)‖` and `N*e₁ ≠ 0`) ⇒ `m < 1` **strictly** at every crease optimum, both functionals. (iii) Mixed (block-diagonal normal ⊕ non-normal): the register is decided by **which block carries the ground state** — so the register can *switch* along a parameter family.

The P-R register split is hereby definitional rather than observed, and Addendum 2 §3's "m is the anholonomy deficit" gets its precise statement: `m = 1` exactly on the normal (reducing) directions — the collapsed sub-budget is a direct summand.

## 3. T3 [T] — J₂ separates the functionals, with an exact constant

For `A = J₂` normalized to `W(A) = 𝔻̄` (superdiagonal 2): `f(A) = f(0)I + f'(0)A`, so `W(f(A)) = D(f(0), |f'(0)|)` exactly, and T1 gives the closed form

  **`Ĩ(f) = |f(0)|·(|f(0)| − |f'(0)|)`.**

**(a) State-extremal creases do not exist** — Delta 5 §2's identity (`I_ext = |x₂|²|a₀|²(1+α) ≥ 0`) **stands unchanged**; its infimum-0-on-`f(0)=0` reading is untouched.

**(b) State-worst creases exist iff `|f'(0)| > |f(0)|`.** By Schwarz–Pick, `|f'(0)| ≤ 1 − |f(0)|²`, so a crease is possible exactly when `|f(0)|² + |f(0)| − 1 < 0`, i.e. `|f(0)|` below the positive root of `t² + t − 1` (= 1/φ; stated as the root, nothing more).

**(c) The exact floor.** Over *all* holomorphic self-maps of the disk:

  **`min_f Ĩ(f) = −5/27`, attained by a single Möbius factor with `|a| = 1/3`** (e.g. `f(z) = (z − ⅓)/(1 − z/3)`; then `f(0) = −⅓`, `f'(0) = 8/9`, `Ĩ = ⅑ − 8/27 = −5/27`).

*Proof.* Minimize `t(t − (1−t²)) = t³ + t² − t` over `t = |f(0)| ∈ [0,1]` (Schwarz–Pick saturation is attainable, exactly by Möbius maps): stationarity `3t² + 2t − 1 = 0` gives `t = ⅓`, value `−5/27`; saturation forces `f` Möbius. ∎

*Machine checks:* Möbius `a = ⅓`: direct `I = −0.18518518518518515`, `λ_min(H_f) = −0.18518518518518517`, vs `−5/27 = −0.185185185185185̄` (diff 3e−17); the blind degree-3 optimizer had already landed on −0.1851851 before the closed form was derived; and **on the same `(A, f)` the state-extremal functional reads `I_ext = +0.2151 ≥ 0`** — the two functionals separate on one witness. Three hand-computed zero-triples confirm the closed form independently of the optimizer.

**Reading.** The J₂ "rigidity" is a property of the **extremal read**, not of the port: at non-extremal states the J₂ port interferes destructively down to exactly −5/27. The summit protection of the healing story is extremal-state physics — consonant with the Bickel mechanism, and now with a sharp interior counterpoint.

## 4. Ensemble and switching results (predictions stated before running; script header)

**P-a — `cos Δ = −1` at crease optima.** 0 violations across 30 ensemble creases (random normal / Jordan / upper-triangular) + all 7 anchor matrices; max deviation 1.7e−7. D-1's forcing question is now supported at ~37 optima under the *state-worst* functional, alongside Addendum 2's 6/6 under the state-extremal one. Still unproved; with T1 it is now a crisp geometric statement — at f-optima the support point of `W(f(A))` in the `−f(0)` direction lies on the anti-ray — which is the form a proof attempt should attack.

**P-b — the registers.** `m = 1` to 1e−12 at every normal optimum; `m ≤ 0.695` at every Jordan optimum. Held.

**P-c — register switching, the T2(iii) consequence.** Family `A(s) = diag(diag(0.7, 0.2), s·J₃)`: the global state-worst minimum sits in the normal block (`m = 1.00000`) for `s ≤ 1.10` and in the Jordan block (`m ≈ 0.606`) from `s = 1.25`, with `I_min(s)` continuous through the crossing. **The meter jumps first-order while the depth is continuous** — the register transition's observable signature, predicted in the script header and observed. *(Graded honestly: a verified consequence of T2, not an independent novel prediction.)*

**Optimizer-limit check:** the J₃ state-worst floor is stable under doubling restarts (−0.25000000 at 10, −0.24999989 at 20). The value `−¼` is suspiciously exact; **flagged as a candidate closed form, no derivation attempted, no claim** (the TSP tombstone governs).

## 5. What this changes, and what it does not

- **Unchanged and reconfirmed:** Delta 5 §1–§5 in full under its own functional (including the J₂ identity and P-R4's row — my momentary "optimizer miss" hypothesis is **retracted**; their optimizer missed nothing, because their functional creases nowhere on J₂). Addendum 2's table stands as state-extremal data; its qualitative claims (`cos Δ = −1`; `m` splits the registers) hold under *both* functionals, which is evidence the register structure is functional-robust.
- **New [T]:** T1 (eigenreduction / support-function identity), T2 + T2′ (the register split definitional in both functionals), T3 (the J₂ separation with exact −5/27 and the Möbius extremal).
- **Upgraded:** the P-1 scoped register fork (port-wiring record §7) now has theorem-backed scope in both functionals, and its interesting blind content narrows to the *switching boundary* in mixed matrices and the still-unproved `cos Δ = −1` forcing.
- **Sharpened for the charge:** on disk domains, every crease question now factors cleanly into (state choice) × (an `H_f` or SVD eigenproblem) × (an optimization over `f` alone) — the search space the ellipse campaign will need, one domain over, just got a dimension smaller.

## 6. Boundary

Disk-domain only (`z₀ = 0`); nothing here touches convex Ω, the ellipse frontier, or any thin-film number. The ensemble is degree-≤3 Blaschke with bounded restarts (search yields, stated as such); T3's proof is functional-analytic and does not depend on the optimizer. P-a/P-b/P-c were stated before their runs but within this session, unhashed — one grade below the corpus's prereg bar, disclosed as such. Scripts: `register_split.py` + the two verification blocks accompany this record; suggested archive destination per the 04_scripts pattern.

---

*Offered, not self-filed. Countersign items: the §0 two-functional distinction as the operative finding; T1, T2/T2′, T3 as [T] with their proofs; §4's ensemble results with the P-c consequence graded as verification; §5's explicit retraction of the optimizer-miss hypothesis and reconfirmation of Delta 5/P-R4 under their own functional; the −¼ flag as unclaimed; the §5 upgrade to P-1's scope.*
