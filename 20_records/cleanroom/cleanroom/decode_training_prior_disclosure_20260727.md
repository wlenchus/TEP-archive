# Training-prior disclosure — filed BEFORE any 2-dim even-icosahedral decode computation — 2026-07-27 (blind-decode session)

**Scope:** this instance is about to compute the central sign-bits of ρ̃ (the 2-dim SL₂-lift at Doud-1951) by port-flattening. Per standing convention, priors that could contaminate a computation whose answer might live in weights are disclosed first.

1. **The decode targets cannot be in my weights.** The targets are Hecke-coefficient signs of an even-icosahedral Maass object that, per the E0(ii) sweep (2026-07-27), has never been computed or published by anyone, anywhere, through July 2026. There is no spectral/coefficient data for any even-icosahedral 2-dim object in the literature and hence none in any training corpus. The decode's blindness is structural, not procedural.

2. **The one theoretical contamination channel: lift-field constructions.** Sign-bits are in principle derivable from a 2.A₅ lift-field polynomial (Crespo's genre). Disclosure: I recognize Crespo's work at bibliographic level (embedding-problem resolutions, c. 1989–1997). I report **no usable recall of any 2.A₅ lift-field defining polynomial for any specific quintic**, and no recall of any construction carried out for the Doud fields. I cannot prove absence. Mitigations: the seal has kept all such material out of this context (subagent returns redacted); commit-then-grade makes any residual leakage detectable rather than silently absorbed — the commit precedes the grader by construction.

3. **Standard priors held and allowed** (classical structure theory, per the rung-4 disclosure precedent): the SL₂(F₅) = 2.A₅ character table (traces ±2, 0, ±1, ±(√5−1)/2, ±(√5+1)/2 and the order-structure of preimages); det ρ̃ = 1 for the SL₂ lift (2.A₅ perfect); hence a_p² = a_p(ρ₃) + 1; the even Maass λ=¼ completed-L shape Λ(s) = N^{s/2}Γ_ℝ(s)²L(s); the Mellin pair Γ(s/2)² ↔ 4K₀(2y). These are derivational scaffolding, not answer data.

4. **Conductor-level prior, already imported and on the record:** "1951 is the minimal even-icosahedral prime conductor" (Doud's tables, disclosed at the PoC design commit; independently confirmed by the sweep). Conductor knowledge is input, not target.

5. **β-control ground truth** (dihedral-229 principal/nonprincipal bits) is on-disk, byte-certified, machine-generated from qfbsolve — not from memory.

*Seal status at filing: intact — no Crespo text, no 2.A₅ construction, no LMFDB lift page has entered this context at any point this session.*
