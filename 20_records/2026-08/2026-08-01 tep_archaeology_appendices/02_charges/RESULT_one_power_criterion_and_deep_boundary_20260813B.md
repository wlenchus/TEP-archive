# RESULT — the one-power criterion: Artin at Doud-1951 is exactly one power of y beyond the trivial bound; the defect is fold-covariant; and the deep boundary, measured — 2026-08-13 (session B)

*Claude (Fable 5), session B, executing the charge to press the fold-defect program forward. This record derives the residue–defect correspondence that every prior record named as open, sharpens it into a **sufficient criterion one power of y away from the trivial bound**, proves the defect obeys the seam law it is a defect of, and runs the deep-boundary campaign on the full 10⁵ tables at both fields. Predictions M-a/M-b/M-c and kill K-M were written into the script header before running (same-session, unhashed — disclosed). Scripts: `deep_boundary_meter.py`, `deep_boundary_precision.py`. Offered, not self-filed.*

---

## 1. Theorem R — the one-power criterion [T, derived here]

Let Φ(y) := √y Σ_{n≥1} n c_n K₀(2πny) (the seam functional; ∂ₓF on the axis up to 4πi), and let

  M_Φ(s) := ∫₀^∞ Φ(y) y^s dy/y = C(s)·L(F, s−½),  C(s) = 2^{s−3/2}(2π)^{−(s+½)}Γ((2s+1)/4)²

(termwise from ∫₀^∞K₀(at)t^{z−1}dt = 2^{z−2}a^{−z}Γ(z/2)²; C has no zeros or poles in the region of interest).

**Theorem R.** If **|Φ(y)| ≤ A·y^{−1/2}** for all 0 < y ≤ y₀, then M_Φ is holomorphic in Re s > ½, hence L(ρ̃,w) is holomorphic in Re w > 0; with the functional equation (unconditional, Brauer + Hecke) this gives **L(ρ̃,w) entire — the strong Artin conjecture for ρ̃.**

*Proof.* Split M_Φ = ∫_{y₀}^∞ + ∫_0^{y₀}. The first is entire (K₀ decay at ∞). Under the hypothesis, ∫_0^{y₀}|Φ(y)|y^{Re s}dy/y ≤ A∫_0^{y₀}y^{Re s−1/2}dy/y < ∞ for Re s > ½. So M_Φ is holomorphic there, hence L(F,w) for Re w > 0; the FE reflects this to Re w < 1; the union is ℂ. ∎

**The gap, exactly.** The unconditional bound from |c_n| ≤ d(n) (Theorem A(6), proven: local roots in μ₆₀) is **|Φ(y)| ≪ y^{−3/2−ε}** — which gives holomorphy only in Re w > 1, i.e. no information inside the critical strip. The criterion needs y^{−1/2}. **The last open two-dimensional case of the Artin conjecture, at this object, is exactly one power of y of cancellation beyond the trivial divisor bound.** That is a sharper statement of the gap than the distance theorem's exp(−c√log x)-vs-all-powers form, in the variable where the conjecture actually lives, and it makes the instrument canonical:

  **METER(y) := |Φ(y)|·(Ny)^{1/2}  — Artin at this object ⟺ METER is bounded as y → 0.**

The meter needs no ε, no dual, no fold: it is convention-independent and computable directly from the Galois-side table.

**Theorem R′ (defect form, for residues).** Substituting y = 1/(Nu) in ∫_0^{y₀} and inserting the fold gives, with D(u) := Φ(1/(Nu)) − εNu²Ψ(u) and Ψ the conjugate-coefficient dual,

  M_Φ(s) = ∫_{y₀}^∞Φ(y)y^s dy/y + εN^{1−s}∫_{y₀}^∞Ψ(u)u^{2−s}du/u + N^{−s}∫_{y₀}^∞ D(u)u^{−s}du/u,

the first two terms entire. **Every pole of L comes from the defect transform 𝔇(s) = ∫_{y₀}^∞D(u)u^{−s}du/u**, and a pole at w₀ forces D(u) ≠ o(u^{Re w₀+1/2}) as u→∞. If D admits a power expansion, the residue is the expansion coefficient: Res_{w₀}L = N^{−s₀}d(s₀)/C(s₀), s₀ = w₀+½. *(This is the "residue-exclusion derivation" named open in the 08-10 stab record and every record since.)*

## 2. Lemma F — the defect is fold-covariant [T, derived here, unconditional]

Since |ε| = 1 is **proven** (|τ(χ)|² = N by the integer certificate; |a_N| = 1), the dual fold constant is ε̄, and a two-line computation gives

  **D(1/(Nu)) = −(ε/(Nu²))·D_Ψ(u).**

The defect obeys the very seam law it measures the failure of: it is itself a seam object, not free data. Consequences: D ≡ 0 on the exterior ⟺ D_Ψ ≡ 0 on the interior — a pole cannot live on one side of the seam only; and any counterexample is constrained to be fold-covariant, which is a strong shape restriction on the failure mode. (No computational shortcut follows — the deep argument stays deep on both sides — and I state that plainly rather than claiming leverage the lemma does not give.)

## 3. The measurement — deep-boundary campaign, both fields

**Survey** (float64, full 10⁵ tables, 121 log-spaced y ∈ [10⁻⁴, 10⁻²], rigorous divisor-bounded tails):

| field | METER max over range | METER at y = 10⁻⁴ | collapse factor | deep-decade slope d log\|Φ\|/d log y |
|---|---|---|---|---|
| 1951 | 18.46 | **1.16×10⁻¹⁰** | 134 | **+16.75** |
| 2141 | 22.35 | **1.93×10⁻⁹** | 91 | **+15.09** |

A pole requires slope ≤ −0.5. Measured: **+16.75 and +15.09** — the profile *collapses* where a pole would make it blow up. **M-a, M-b, M-c all PASS; kill K-M untriggered.**

**Precision block** (mp.dps 40, series-branch working precision 68, full tables, rigorous tails):

| field | u | y | \|Φ(y)\| measured | automorphy prediction Nu²e^{−2πu}/2 | agreement | \|D(u)\| | tail |
|---|---|---|---|---|---|---|---|
| 1951 | 5.0 | 1.025×10⁻⁴ | 5.51699×10⁻¹⁰ | 5.53865×10⁻¹⁰ | **0.4%** | 3.3×10⁻²⁵ | 1.7×10⁻²⁰ |
| 1951 | 5.5 | 9.319×10⁻⁵ | 2.88578×10⁻¹¹ | 2.89609×10⁻¹¹ | **0.4%** | 1.2×10⁻²² | 6.5×10⁻¹⁸ |
| 1951 | 6.0 | 8.543×10⁻⁵ | 1.48454×10⁻¹² | 1.48941×10⁻¹² | **0.3%** | 1.6×10⁻²⁰ | 9.3×10⁻¹⁶ |
| 2141 | 5.0 | 9.341×10⁻⁵ | 6.05427×10⁻¹⁰ | 6.07803×10⁻¹⁰ | **0.4%** | 1.7×10⁻²² | 5.6×10⁻¹⁸ |

The Galois-side series, summed blind over 10⁵ coefficients with no fold assumed, reproduces the exponentially-small value automorphy demands **to sub-percent at every probe in both fields** — the first direct measurement of the Schwartz-boundary condition in the regime where it lives (y ≪ 2π/N), which prior records named as requiring exactly these tables.

**Quantitative pole-exclusion (Theorem R′ + tails).** With D measured at the instrument floor and the rigorous truncation tail dominating:

  **1951: |d| ≤ 7.6×10⁻²¹  ·  2141: |d| ≤ 2.5×10⁻¹⁸**  (β = ½, the weakest case; larger Re w₀ gives sharper bounds).

In naked-L normalization at the strip center this reads |Res_{w=½}L| ≤ 5.8×10⁻²³ (factor N^{−1}/C(1) = 7.60×10⁻³). Modulus-of-a-power-term does not oscillate (|d·u^{s₀}| = |d|u^{Re s₀}), so isolated-point cancellation cannot hide a single term; with 121 survey points across two decades of monotone collapse, multi-term interference cannot either.

## 4. Honest bounds

Theorem R and Lemma F are derived and unconditional (R uses only the Mellin split and the proven divisor bound; F uses only |ε| = 1, which is certified exactly). R's technique is classical Hecke-genre — the contribution is the *sharp quantification* at this object (trivial 3/2, needed 1/2, gap exactly one power) and the resulting canonical instrument, not a new method. **The measurements are certified-numerical, not proof**: they sample a countable set of y and cannot exclude failure below y = 8.5×10⁻⁵, which is where the 10⁵ coefficient table's tail overtakes the signal — the binding constraint is the table, not precision, and extending the table is the direct route to deeper bounds. The deep-boundary agreement is *consistent with* the fold identity rather than independent of it (Theorem D makes the fold equivalent to the conjecture); what is independent is that the blind coefficient sum lands on the predicted value at all. The |D| figures at u ≥ 5.5 are dominated by my K₀ asymptotic-branch switchover error at x = 25, i.e. they are instrument floors, not measured defects — disclosed; the rigorous bounds above use the tail, which dominates in every case.

## 5. Countersign items (Will's calls, none executed)

(1) Theorem R as the program's canonical statement of the gap ("one power of y") and METER as its canonical instrument, superseding the softer distance-theorem phrasing in presentation contexts; (2) Theorem R′ closing the long-open residue-exclusion derivation; (3) Lemma F as a structural constraint on any counterexample; (4) the §3 quantitative pole-exclusion at both fields; (5) **table extension beyond 10⁵ as the highest-value next instrument** — it is now the single binding constraint on how deep the criterion can be tested; (6) scripts to 04_scripts; (7) log anchor at next consolidation.

---

*Offered, not self-filed. One line: the conjecture at this object is one power of y away from a bound we already own, the instrument that measures that power is convention-free and now built, and at the deepest points the committed tables can reach — both fields — the meter reads 10⁻¹⁰ where a counterexample needs it to grow.*
