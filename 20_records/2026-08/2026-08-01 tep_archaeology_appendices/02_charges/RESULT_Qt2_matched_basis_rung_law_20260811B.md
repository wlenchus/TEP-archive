# RESULT — Q-t2: the matched-basis rerun; conditioning is monotone in rung, parity lives in the topology, and the Petz frame survives where the design rule died — 2026-08-11 (session B)

*Claude (Fable 5), on Will's question whether the P-t1 kill is a function of even/odd rung, via the Petz regime (d = 2 default interior: the monotone-metric family collapsing uniquely in the radial direction). PREREG in-script (same-session, unhashed): competing hypotheses with declared priors — H-r (support-geometry, 0.6) vs H-A (Petz/Fisher odd rung, 0.4); chart-matched bases (each chart gets both its shells and its hat basis uniform in its own variable), removing P-t1's disclosed confound. Script: `qtest_matched_basis.py`. Offered, not self-filed.*

## 1. Grounding: Will's Petz statement is exact [T-cited]

At d = 2 (Bloch ball), every monotone (Petz-classified) metric restricts on the **radial direction** — the commuting, classical direction — to the *same* form: the classical Fisher metric dx²/(1−x²) = G²dx² (Chentsov uniqueness); the family genuinely varies only tangentially. The atlas already holds both halves: x = Bloch radius; ∫G dx = the Fisher–Rao arc = the A-chart. So the three P-t1 designs were precisely **rungs 0/1/2 of the chart ladder on the metric-unique radial line** (r; A = arcsin, the Fisher chart; η = artanh, the log-odds chart) — and the even/odd question is well-posed and decidable.

## 2. The measurement (confound removed)

| m | rung 0 (r-matched) | rung 1 (A-matched) | rung 2 (η-matched) |
|---|---|---|---|
| 16 | **1.14×10¹** | 3.30×10⁵ | 1.54×10⁶ |
| 24 | **1.51×10¹** | 6.11×10⁵ | 2.27×10⁶ |
| 32 | **7.24×10¹** | 3.83×10⁵ | 2.80×10⁶ |

**H-r survives; H-A dies.** Matched bases rescued the chart designs by ~11 orders (P-t1's confound was real and large) — and rung 0 still wins by ~4 orders at every size.

## 3. The answers to the question asked

1. **Not parity — monotone in rung.** κ ascends with every G-ascent (r < A < η at all sizes): *each chart ascent costs conditioning*, because each ascent clusters samples toward the saturation edge where reads correlate. The atlas's "each ascent is one factor of G" acquires an inversion-side price tag.
2. **But parity IS present — as domain topology.** The odd rung compactifies: A holds the closed annulus in [arcsin 0.3, π/2]. The even rung diverges at saturation: artanh(1) = ∞ — the η-chart *cannot grid the domain through x = 1* (nodes capped at 0.999 for all charts, disclosed). Even rungs saturate at the collapse locus; the odd rung mediates it compactly (A = gd(η), the atlas's compactified coordinate). So: conditioning quality is monotone in rung; **chart-closure at saturation alternates with parity** — that is the true even/odd content of the kill.
3. **The Petz frame survives above the dead design rule.** Chentsov uniqueness on the radial line is exactly what makes the design question *invariant* (no metric ambiguity to game) — and the invariant answer is that Abel-inversion conditioning is a **support-geometry functional, blind to the distinguishability metric**: governed by kernel-edge overlap (uniform in r), not by Fisher length. The d = 2 default interior gives the problem its canonical frame; within it, the raw radial measure wins. Distinguishability charts price the *probe* (dwell, odds); support geometry prices the *inversion*. Two ledgers, now measured apart.
4. **[A, priced] The two-row Petz split.** The additive/shell row probes the radial-classical sector — where the metric family collapses and everything is canonical; the multiplicative/caustic row probes the tangential sector — where the Petz family genuinely varies. "Default interior at d = 2" = the classical radial core; the distortion family lives tangentially. Consistent with the whole dictionary (abelian = classical = unique; ordering = tangential = family-dependent); priced as frame.

## 4. Honest bounds and countersign

One conditioning metric (κ₂ of square collocation), one kernel family, domain capped at 0.999 (forced by rung 2's own divergence — itself a datum); basis-free functionals (SV-uniformity of the continuous operator) remain the named completion of Phase 2(a). Priors were declared before the run; the 0.6 prior won — no update theater. **Countersign:** (1) the monotone-in-rung conditioning law + parity-as-topology observation adopted as Q-t2's finding; (2) §3.3's two-ledger split (probe-pricing vs inversion-pricing) as the corrected home of the G-kernel identification; (3) §3.4 frame at [A]; (4) scripts to 04_scripts; (5) log anchors for the P-t1/Q-t2 arc queued for the next consolidation pass (context boundary; stated so nothing is claimed unfiled).

---

*Offered, not self-filed. The one-line answer: not even/odd in quality — monotone in rung, with parity appearing where the corpus would want it: the odd chart closes the domain the even charts cannot; and the Petz collapse is what made the whole question canonical enough to kill a prediction and keep the frame.*
