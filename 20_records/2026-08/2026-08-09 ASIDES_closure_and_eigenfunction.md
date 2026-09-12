\# Asides consolidation — the closure-and-eigenfunction session — 2026-08-09

&nbsp;

Two campaigns ran end-to-end today, both pre-registered, both fully green; this entry carries the session's unfiled margins. Headline records: \`RESULT\_algebraic\_closure\_1951\_20260809.md\` (8/8; the algebraic side of Doud-1951 complete at every unramified prime, 2141's dyadic obstruction measured in γ itself) and \`RESULT\_maass\_live\_20260809.md\` (4/4; both eigenfunctions exhibited as functions, pointwise Γ₀(N)-automorphic at 10⁻²⁴ out-of-sample, Fricke ratio \= −ε to 10⁻²⁶ constancy).

&nbsp;

\*\*Findings that deserve their own line.\*\* (1) The frame-degeneracy mechanism: a qfsolve orthonormal frame whose element-sum is exactly −1 makes det(I+P\_σU) vanish on ALL orderings — "no rows" meant "all zeros," the reviewer's dichotomy had a third answer. (2) The frame-change law: two honest gauges of the same construction differ by exactly one quadratic character off the involution locus (d₀ \= 78040 \= 8·5·1951; d₀ \= 12), with 2A structurally frame-independent — and 2A therefore MASKS any character in a full-set fit; fit off-involution or fail. (3) The sin-type parity is visible: the rendering's dark seams at x ∈ ½ℤ are the decoded central bit as geometry (\`maass\_forms\_first\_rendering.png\`, \`render\_maass.py\`).

&nbsp;

\*\*Instrument lessons (drift-watch additions).\*\* GP's \`denominator()\` on t\_POL is rational-function semantics — use \`denominator(content(·))\`. GP generic polmod division and Bareiss determinants over ℤ/2^K can throw "impossible inverse" on invertible inputs — go division-free (Newton inverse seeded in 𝔽₂^m; Leibniz det). A tail bound that pairs min(y) with min(n) across two evaluation sides is pessimistically mismatched — bound per side, take the max (caught because the dihedral control's exclusions made no sense; controls catch harness bugs, twelfth instance). A sieve that scans all indices per prime is 168M comparisons of dead weight — iterate multiples only (caught by wall-clock; rewrite verified by output-identity against the slow version). One ordering deviation owned in the MAASS-LIVE record: control C4 ran after certification (passed at the CSV floor).

&nbsp;

\*\*Session-ops.\*\* Certification wall-clock is Bessel-bound (\~700 besselk/s at 28 dps); the asymptotic-K₀-above-u=30 split and per-y caching are what made it land; two-process field split works on 2 cores. mpmath phase iteration costs n\_max·ulp — the 10⁻²⁴ floors are that, documented, not mystery.

&nbsp;

\*\*Queue as it stands tonight:\*\* the four remaining Doud fields via the streamlined recipe (construction \+ FE-character-pin; needs per-conductor emission machinery — a real campaign); Turing-method rigorization (Palojärvi–Zhao 2508.03023) — now with an actual function to rigorize; the Crespo formula citation pin (library access); the countersign ledger session; the rendering as an outreach artifact. Artifacts today: \`TEP\_dyadic\_closure\_20260809.zip\` (3a9cd292…), \`MAASS\_LIVE\_20260809.zip\` (fa8d23a0…), the PNG, Drive folder \`TEP\_dyadic\_closure\_20260809\`, manifest v7 \+ v7b.

&nbsp;

\*Offered, not self-filed.\*