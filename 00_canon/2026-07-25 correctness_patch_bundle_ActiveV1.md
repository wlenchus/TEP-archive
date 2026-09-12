# Correctness Patch Bundle    

**[ActiveV1, 2026-07-25]**    

**2026-07-25** · Claude (Fable 5), same session, under own direction · every patch gives exact location + replacement text · sources: this session's sweeps + the three reader-agent inventories + two fresh lit passes

## P-A. The ζ = 1/√2 / "critical damping" sweep — with a finding

**Finding first: V2 §2.2 is already fixed.** The ActiveV3 author-update (pushed 07-23) reads: *"The critical inflection of maximally flat frequency response (Butterworth condition) occurs at ζ = 1/√2… This is a conditional extremum (ζ = 1 is critical damping for that specific system)"* — substantively correct. The four-document demand (05-25 review, V2 audit, 07-22 QC, 07-22 review) was **partly stale by the time this session repeated it**: the propagation disease runs in both directions — reviews also fail to notice fixes. One residual word-choice suggestion: "critical inflection" invites the old conflation; propose *"The maximally-flat-response (Butterworth) optimum occurs at ζ = 1/√2…"*.
**Genuine standing error, one instance:** `20_records/2026-05/2026-05-14 III_comprehensive_investigation_record.md` line 158: *"DHO overdamping: real frequency below critical damping, imaginary frequency above"* — garbled (underdamped ζ<1 has real ω_d; overdamped ζ>1 imaginary). Replacement: *"DHO damping regimes: oscillatory (real ω_d) below critical damping ζ = 1, monotonic (imaginary ω_d) above; the Butterworth optimum ζ = 1/√2 is distinct from critical damping."* (Its 05-15 .txt duplicate inherits the fix or the dedup.)
**Frozen instances:** the April OpenRouter transcript carries the old conflation throughout — transcripts are frozen by design; propose one erratum pointer in its CATALOG row instead. Lines 54/107 of 05-14 III already say "Butterworth/optimal-damping" and are correct as written.

## P-B. Anandan–Aharonov citations — the May instruction, executed

The 5-25 review's instruction (*"rank-2 saturation is Anandan–Aharonov; adopt this citation; do not claim the wedge rigidity as new"*) was never applied to the three **publication-track** purity papers, exactly where a referee will look first. Verified: `10_papers/tep_tier1_purity_speed_limit.txt`, `10_papers/2026-05-08 purity_speed_limit_v2.txt`, `10_papers/tep_tier1_purity_decoherence_limit.txt` contain zero "Anandan" hits while presenting the rank-2 saturating-direction structure (abstract ¶ and §"further content" ¶, both files' lines ~19 and ~37). Patch, per paper: append to the saturation paragraph — *"The geometric mechanism of saturation is that of Anandan–Aharonov [AA], specialized to the purity observable; the rank-2 factorization, the constructive saturator H_opt = iW/√F, and the budget recast are the present contribution, not the mechanism."* — and add **J. Anandan and Y. Aharonov, Phys. Rev. Lett. 65, 1697 (1990)** to references.

## P-C. DS-Zeta sideline — the kill, stamped at the source

`20_records/2026-05/DS Zeta Sideline 5.2.26.txt` still presents the monotonicity-to-RH route as "the cleanest path I've seen," while `external_review_consolidation` Δ9 killed it (*"a magnitude argument applied to a phase-driven phenomenon; η is harmonic… it would prove too much"*). Per the co-location discipline, prepend to the sideline file: *"[Status stamp, 2026-07-25.] The monotonicity route below is retracted per 5-29 Δ9 (magnitude argument on a phase-driven phenomenon; harmonic η has no interior monotonicity). Retained as the record of the attempt; the deficit-evolution algebra (§I) and the σ = 1/2 detailed-balance reading survive independently."*

## P-D. The percolation orphan — archive with erratum

`20_records/2026-05/## Final Formal Synthesis- The Geometric Origin of Coupling.txt`: no tier discipline, uncited by anything, and its headline "99.999% relative accuracy" compares −2.49e−5 to −2.65e−5 (a 6% discrepancy — arithmetically wrong as stated). Propose: move to `90_archive/precursors/` with the one-line pointer: *"Retired 2026-07-25: untier'd precursor-style numerology; the accuracy claim is arithmetically incorrect (6% residual described as 99.999% agreement); no downstream dependency exists."*

## P-E. Namespace splits (executing the standing rename demands)

1. **O-a vs O-A/O-B:** retitle the uppercase pair everywhere as **OA-fiber / OB-label** (the 06-17 closure paper's own objects), reserving lowercase O-a for the Wang–Tits lemma. Files touched: Independent Referee §6/§9 pointer rows; 06-17 paper header note; ledger P7.5 marked executed.
2. **OT5 tag collision:** the 07-01 records' OT5 (forced-vs-chosen fork) vs the 07-19+ OT5 (uniqueness ladder) are different opens. Propose **OT5-fork** and **OT5-unique** with a one-line note at the head of the 07-19 campaign opening; my own session records (fourth review, addenda, rung records) to be read under OT5-unique.
3. Cross-check note: the O1 fork's dissolution (06-18: WY K = +1/4, angular-only) gets a pointer stamp in `30_assessments/internal/2026-06-07 adversarial_review_consolidated_record.md` §[O1].

## P-F. E5 — erratum against my own fourth review (P2's absence-claim), self-filed per the pre-registered stake

The fourth review closed with: *"if the quantum-cone classification already exists in the literature, §5-P2 reduces to citation and the absence-claim takes the hit."* **It partially takes the hit.** Fresh lit pass, this session: **K. Yamagata, "Quantum monotone metrics induced from trace non-increasing maps and additive noise," J. Math. Phys. 61, 052202 (2020)** — characterizes monotone metrics on positive operators of **arbitrary trace** under CPTNI maps + additive noise: the answer is *static operator-monotone functions only*, i.e., Petz rigidly, **no Campbell-style mass-sector freedom** under that (stronger) invariance class. Corrected P2 statement: the quantum cone is now **bracketed** — Campbell's weak class (mass-preserving congruent embeddings) classically leaves two mass functions; Yamagata's strong class (all CPTNI) quantum-mechanically leaves none; **P2's precise slot — the embedding-class-only quantum classification, expected Petz ⊗ two mass functions — appears to remain open, but the consolidated session must start from Yamagata's techniques and cite him as the adjacent classification.** The theorem-distance shrank; this is good news filed as an erratum. Also added to rung 1's lit note: T. Fritz, *A synthetic approach to Markov kernels…* (Adv. Math. 2020) as the modern categorical home of factorization-style reasoning, and Fujiwara's *Hommage to Chentsov's theorem* (Inf. Geom. 2022) as the modern-proof survey — the rung's "priority zero presumed" is hereby "priority zero, confirmed with named neighbors."

## P-G. Rung-3 restamp (executing E3 from the period review)

Header stamp for `2026-07-25 O-a_rung3_opening_Hstar_frame_democracy_DraftV1.md`: *"[Restamp, 2026-07-25, same session.] Superseded in scope before countersign: Route B was executed 2026-06-15 (manifold-via-homogeneity; O-a discharged for the scale arena) with the residue demoted by OT5-unique Delta 2. This document's surviving content is §2-Route-A's provenance demand — no nonzero-holonomy anchor has yet been computed without presupposing SU(1,1); Delta 8's composition test is assigned as that computation — and the formalized flat-cylinder gate. Re-filed as: Addendum to O-a §3 (anchor provenance), not a rung."*

---

## Appendix — Foundations Status block, v2 (supersedes this morning's draft)

**Derived, twice over [T/V] — the budget:** partition of unity of a passive invariant ensemble (06-09 §§2–3); independently, the exact signature of any passive state-preserving interface (Theorem P, 07-19). Never assumed.
**Forced output [T/V] — the metric:** completeness ⟹ L² (LTV-for-every-conditioning ⟺ orthogonal projection; fails in every Lᵖ, p ≠ 2) ⟹ Riemannian ⟹ Fisher–Rao unique germ (Thread L; Čencov/AJLS). Two extension axes exhaust the relaxations: Campbell (normalization → scale/cone; classically two mass functions; quantum-side bracketed by Yamagata 2020 under CPTNI) and Petz (commutativity → shape/fiber). Arena: **ℝH²/SU(1,1), discharged for the scale arena 06-15** (transitivity + phase isotropy + Wang–Tits; curvature a consequence); Tannakian setting **forced** in the finite sector (OT5-unique W1). The fiber multiplicity is located exactly: **the gap between "monotone" and "two-point homogeneous"** (06-15), with Bures/SLD the unique two-point-homogeneous member; multiplicity is bounded shape-residual structure. Retired vocabulary: "metric selection," "the forced-vs-chosen floor."
**The itemized remainder [O, with routes]:** the O-a **anchor-provenance question** (one non-circular holonomy computation; composition test assigned); **O-d** formal write-up (two-generator factorization executed 07-25, both registers, modulo the (D) framing — Will's call); **O-e** (1,d) counting; the compositionality postulate; the per-register applicability clause (theorem in the arithmetic register via Peter–Weyl); completeness surplus = readability, with the **u-vs-MSE certificate** as its unrun instrument (Theorem C).
*One-phrase summary (A7 verbatim): forced at the metric-space level, modulo the itemized ledger above.*

---

*Offered, not self-filed; countersign gates each patch independently. P-A through P-D are mechanical and carry their replacement text; P-E needs a naming decision; P-F and P-G are errata against my own session outputs, filed under the same discipline they enforce.*
