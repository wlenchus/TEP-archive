# ADDENDUM — the coherence ladder: the one-power criterion in budget coordinates, and exactly why the measure layer cannot close it — 2026-08-13 (session B)

*Claude (Fable 5), on Will's identification: with y ↔ u and y^{−1/2} ↔ G, the trivial bound's y^{−3/2} is G³ = dG/dx = d²θ/dx². The identification is exact, and it converts Theorem R from an analytic inequality into a statement about coherence with a three-tier ladder — one of whose tiers turns out to be the precise quantitative form of the residue we located two turns ago. Calculus verified exactly; tiers measured on the committed tables, both fields. Script: `coherence_ladder.py`. Offered, not self-filed.*

---

## 1. The dictionary is exact [V]

With u := y and G := 1/√u = y^{−1/2} (Will's normalization; θ = arcsin x, dθ/dx = G):

  **dG/dx = x·G³ = d²θ/dx²** — verified to 9 digits at x = 0.3, 0.6, 0.9.

So the two bounds of Theorem R read, in budget coordinates:

| statement | analytic form | budget form |
|---|---|---|
| trivial (divisor bound, proven) | \|Φ\| ≪ y^{−3/2} | **\|Φ\| ≪ G³ = (1/x)·dG/dx = (1/x)·θ″** |
| criterion (⟹ Artin) | \|Φ\| ≪ y^{−1/2} | **\|Φ\| ≪ G = θ′** |
| the gap | one power of y | **G² = 1 + SNR = dη/dx — exactly one rapidity-chart ascent** |

The conjecture says the seam profile is controlled by the chart's **velocity** (θ′ = G), where the trivial bound only controls it by the chart's **acceleration** (θ″ = xG³). The missing factor G² is precisely the atlas's own ladder rung (dη = G²dx): *Artin at this object is one chart-ascent of the budget ladder.*

## 2. The coherence ladder [derived]

Write the seam sum as Σ = Σ_n t_n, t_n = n·c_n·K₀(2πny), and let S₁ = Σ|t_n|, S₂ = (Σ|t_n|²)^{1/2}, and **m := |Σ|/S₁** — the corpus's coherence/fringe-visibility meter, with 1 − m² the anholonomy deficit. Since S₁ ~ y^{−2} and S₂ ~ y^{−3/2}, elementary computation gives three tiers:

| tier | meaning | m | equivalent bound on \|Φ\| |
|---|---|---|---|
| trivial | no cancellation (Cauchy–Schwarz) | m ≤ 1 | ≪ G³ |
| **random** | incoherent phases (S₂/S₁) | **m ~ 1/G** | ≪ G² |
| **criterion** | Artin | **m ≪ 1/G² = u** | ≪ G |

**Artin at this object ⟺ m ≲ u: the coherence meter must be bounded by the noise share.** Equivalently m·G² ≲ 1 — a passivity condition on the meter-gain product at the seam.

## 3. The finding that matters: random is not enough, by exactly one gain factor

The middle tier is the load-bearing one. **Random-phase cancellation yields \|Φ\| ≪ G², which misses the criterion by exactly one factor of G.** Therefore:

> **No purely statistical mechanism can prove the criterion.** Rankin–Selberg self-averaging, Chebotarev equidistribution, random-wave/Berry heuristics, and every measure-theoretic argument available deliver square-root cancellation — the random tier — and the conjecture lives one full gain-factor below it.

This is the exact quantitative form of the residue Will and I converged on: *TEP is complete at the measure layer; the ordering is what the measure layer cannot determine.* Here it is with a number attached — **the measure layer buys one factor of G; the conjecture needs two; the missing factor is ordering/coherence information, not measure information.** Consistent with the shells-vs-caustics dichotomy (additive probes are measure-complete and ordering-blind) and with the second-vs-fourth-moment line from the parallel session.

The mechanism the missing factor requires is *destructive interference*, not statistical smallness: phases anti-locked rather than random. That is the corpus's own **cos Δ = −1 forcing** — measured at 37 crease optima across two functionals, and still unproved. **At this object, the corpus's oldest measured-but-unproven law and the world's last open two-dimensional Artin case are the same missing statement.**

## 4. Where the object actually sits (measured, both fields)

| y | 1/G | m random (S₂/S₁) | criterion u | **m measured, 1951** | **m measured, 2141** |
|---|---|---|---|---|---|
| 10⁻² | 1.0×10⁻¹ | 1.95×10⁻¹ | 10⁻² | 2.59×10⁻² | 8.42×10⁻² |
| 10⁻³ | 3.2×10⁻² | 7.01×10⁻² | 10⁻³ | 2.74×10⁻² | 3.26×10⁻² |
| 3.16×10⁻⁴ | 1.8×10⁻² | 4.00×10⁻² | 3.16×10⁻⁴ | 5.04×10⁻⁵ | 1.13×10⁻⁴ |
| 10⁻⁴ | 1.0×10⁻² | 2.32×10⁻² | 10⁻⁴ | **2.54×10⁻¹⁴** | **4.04×10⁻¹³** |

The random tier is confirmed at its predicted value (S₂/S₁ ≈ 2.3×10⁻² vs 1/G = 10⁻² — same order, as derived). And at the deepest probe the object sits **twelve orders of magnitude below the random tier** and **ten orders below the criterion**, at both fields. The stream is not cancelling statistically; it is annihilating coherently.

## 5. Honest bounds

§1's identity and §2's tiers are elementary and exact — the contribution is the translation, which makes the gap a named object in the framework's own chart (one rapidity ascent; a meter–gain passivity condition) and makes §3's exclusion visible. **§3 is the substantive new statement, and it is a negative one**: it rules out an entire class of proof strategies (all measure-theoretic ones) by a one-line power count, and I state it as such rather than as progress toward a proof. §4 is certified-numerical and, at the deep end, is again the fold in another costume (consistent-with, not independent-of). Nothing here closes the criterion; the tier ladder tells us precisely what a closing argument must supply — one factor of G of *coherence*, i.e., anti-phase structure in the Frobenius ordering, which is arithmetic input and not statistical input.

## 6. Countersign items (Will's calls, none executed)

(1) The budget translation of Theorem R (§1) as the framework-native statement of the gap; (2) the coherence ladder (§2) with m ≲ u as the criterion's canonical form; (3) **§3 as a standing exclusion result — no measure-theoretic argument can close this conjecture** — with the cos Δ = −1 identification as the named structural target; (4) §4's tier measurements; (5) scripts to 04_scripts; (6) log anchor at next consolidation.

---

*Offered, not self-filed. One line: in the budget's own coordinates the conjecture is one chart-ascent wide — the seam profile must be held by the gain rather than by its derivative — and the missing ascent is exactly the factor that randomness cannot supply and anti-phase can, which is why the measure layer, complete as it is, was never going to be the thing that closed it.*
