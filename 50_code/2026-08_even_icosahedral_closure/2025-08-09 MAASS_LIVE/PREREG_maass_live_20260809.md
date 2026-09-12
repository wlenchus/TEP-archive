# PRE-REGISTRATION — MAASS-LIVE: the eigenfunction itself, tested pointwise — 2026-08-09

**Pivot (Will):** to the analytic side — exhibit the Maass partner as a *function* and test what no FE certificate touches. **The out-of-sample claim:** the committed coefficients were selected by FE/twist optimization (finitely many reflection identities); genuine Γ₀(N)-automorphy at points is an infinite family of independent constraints never used in selection. If the committed object were an FE-impostor, pointwise automorphy would shred it. This is a real kill-risk test.

## Objects

F_N(z) = √y Σ_{n≥1} c_n K₀(2πny)·(e(nx) − e(−nx)) for N ∈ {1951, 2141} — **sin-type (ω = −1) per the measured parity**, λ = 1/4 (r = 0) per the measured spectral parameter, coefficients c_n assembled multiplicatively to n_max = 25,000 from the committed CSVs (exact symbolic columns at 30 dps; Hecke recursion a_{p^{k+1}} = a_p a_{p^k} − χ(p) a_{p^{k−1}}; χ(p) = ζ₅^{j₅(p)}; a_N = ζ₁₀² at 1951, ζ₁₀⁸ at 2141 with χ(N) = 0). Dual G_N = same with c̄_n.

## Predictions

1. **[control] Dihedral-229** (Ind ψ₂₂₉, even/cos, χ = kron(229,·), a_p from the certified session-A table): passes pointwise automorphy and Fricke-constancy at the working floor.
2. **[control] Corruption sensitivity:** flipping a single coefficient sign (c₂ at 229; b₁₀₁ at 1951) breaks automorphy by ≥ 8 orders — each bit is pointwise-visible (leverage graded by e^{−2πpy}).
3. **[novel, the claim] Both icosahedral objects pass pointwise Γ₀(N)-automorphy:** F(γz) = χ^{(±)}(d)·F(z) at every test pair, at the truncation-plus-precision floor (~10⁻²⁰ or better), for all γ = [[a,b],[N,d]], d ∈ {2,3,7}, and all test points. The nebentypus convention (χ(d) vs χ̄(d)) is a priori two-valued; the SAME branch must hold across all pairs, both objects — the branch itself is measured and reported.
4. **[novel] Fricke covariance:** F(−1/(Nz))/G(z) is CONSTANT over test points to the floor with |const| = 1. (Identification of arg(const) against the committed ε is exploratory — conventions documented after constancy is established, before any comparison is graded.)
5. **[forced, stated for completeness]** Δ-eigenvalue 1/4 and T-periodicity are built into the expansion — carry no test content; listed so nobody mistakes them for evidence.

## Procedure (fixed before running)

Test points at the level waist: x = −d/N + s/N (s ∈ {0.37, 0.71, 1.23}), y ∈ {1, 1.3}/N; γz computed in mpmath; every pair requires min(y, y′) ≥ y_min with tail bound Σ_{n>n_max} τ(n)·φ·√y·K₀(2πny) < 10⁻²⁵ (computed and reported per pair; pairs failing the bound are dropped, not stretched). Residual R = |F(γz) − χ(d)F(z)| / max(|F|, |F(γz)|). Two phases: float64/scipy prescreen (bug-catching calibration, threshold 10⁻¹⁰, explicitly not the grade), then the mpmath 30-dps certification pass (the grade). Coefficient assembler is cross-checked against the deep_twist assembly on overlap before anything else runs.

**Kill conditions.** (i) Control 1 fails → instrument invalid, nothing counts. (ii) Control 2 fails to fail → functional has no leverage, nothing counts. (iii) Any icosahedral pair fails at floor while controls pass → **the analytic-partner claim is REFUTED at that object** — recorded loudly, no post-hoc parity/convention scans beyond the two pre-declared branches (χ vs χ̄; and if the primary ω = −1 fails, ω = +1 is run once as a labelled diagnostic of the parity measurement, not as a rescue).

*Offered, not self-filed. Scripts: maass_live.py. Committed inputs only; no re-fitting of any kind.*
