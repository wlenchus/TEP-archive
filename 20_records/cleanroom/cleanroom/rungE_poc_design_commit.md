# Rung E — PROOF-OF-CONCEPT RUN, design commit (lodged before any target computation)

**2026-07-27** · at Will's direction ("rip the band-aid... treat this problem as though you're confident you can solve it") · This deviates from the staged brief by compressing E0–E3 into one encapsulated run at PoC fidelity — deviation directed and cosigned by Will; the staged brief remains the posterity path. Framework-native design per Will's correction: the seam-port and down-flow recovery are the *engine*, not garnish.

## The move

The 2-dim even lift ρ̃ needs the central sign-bits (the K̃/Crespo layer — expensive). **Sym² kills the center**: ρ₃ = Sym²ρ̃ is the 3-dimensional representation of A₅ itself, so its Frobenius traces are computable from the quintic's emission data alone — factorization mod p (A₅ class) + face-sign (5A/5B, Vandermonde vs √disc) — with **no lift data, no K̃, no tables**. Trace values: 1A→3, 2A→−1, 3A→0, 5A/5B→(1±√5)/2 (assignment = the global face-convention; both gauge choices run). For a totally real field, ρ₃(c) = I: **gamma factor Γ_ℝ(s)³, the even seam, archimedean parameter pinned** — the search-collapse, degree 3.

**Openness of the target [T-checked]:** ρ₃ is even (trivial at c) and nonsolvable; it is inside no classical automorphy cone — not solvable (no Langlands–Tunnell), not odd 2-dim (no Deligne–Serre/K–W), and its automorphy via Gelbart–Jacquet would *require* the open 2-dim even case. Entirety of L(s, ρ₃) at these fields is, to the best of current knowledge, unproven and (pending the E0(ii) sweep) numerically untested. Both outcomes bear on Artin at the corner.

## The instrument

Smoothed functional-equation/theta-relation test at the seam (the corpus's FE instrument family, degree-3 build, fresh implementation, mpmath high precision): Λ(s) = N^{s/2}Γ_ℝ(s)³L(s, ρ₃) = ε·Λ(1−s), ε = ±1 (self-dual, real traces). Certificates, pre-declared:
1. **Synthetic keyed control:** product of three even Dirichlet L-functions (entire, exact gamma Γ_ℝ(s)³, known N and ε) — the instrument must pass at high precision and fail violently at wrong N. Builds and validates the kernel/identity.
2. **Theorem-grade seam control:** Sym² of the even dihedral λ = ¼ Maass object at 229 (automorphic by Hecke–Maass; Sym² automorphic by Gelbart–Jacquet) — coefficients re-derived fresh from ℚ(√229) class-field arithmetic (h = 3; principality via qfbsolve).
3. **Negative controls:** scrambled face-signs; random class reassignments; wrong gamma (odd-shifted); wrong N — all must fail by orders of magnitude.
4. **The runs:** (a) Doud's 1951 quintic (x⁵−x⁴−780x³−1795x²+3106x+344; tame, minimal even prime conductor — disclosed import: the polynomial and its conductor-minimality from Doud's public tables; no spectral/automorphic data exists anywhere to import); (b) the corpus's parked {2,7,331} quintic (x⁵−11x³−7x²+14x+7). Per run: theta-relation residual at the predicted conductor; **blind conductor scan** (the instrument selects N — for (b) this *measures* the wild dyadic exponent of ρ₃, a number no table holds); ε measured and checked against the trace-form/tame-marking prediction where applicable.

## Kill conditions

**KP-1** instrument fails control 1 → build error; stop, report. **KP-2** fails control 2 → seam-instrument flaw at λ = ¼; stop, report (itself informative). **KP-3** controls pass, icosahedral residual large/unstable → report as-is with the t-profile (a pole signature is Artin-relevant data, distinguished from noise by shape); no tuning toward success. **KP-4** conductor scan ambiguous → claim downgraded to residual-only, stated. Scope line, pre-committed: a PASS is a **numerical entirety/automorphy-consistency certificate at PoC fidelity** — evidence, not theorem; fidelity upgrades (rigorous tail bounds, Booker-style zero counting, referee) are the posterity path per the staged brief.

## Framework stake (pre-registered reading)

This is the down-flow read at the seam: emission data (the quintic's Frobenius/anholonomy shadow) in, Γ_ℝ(s)³-pinned FE observer at the parabolic port out. A clean PASS with blind conductor selection on objects **outside both classical cones** is the proof-of-concept that the corner is readable — the Conservation clause operating where no classical instrument reaches. A principled FAIL is a pole-shaped finding at the corner. Enthusiasm-bias control: the controls run first, the target last, and the record reports whatever the residuals say.

*Committed before any target computation. SHA-256 of artifacts at close.*
