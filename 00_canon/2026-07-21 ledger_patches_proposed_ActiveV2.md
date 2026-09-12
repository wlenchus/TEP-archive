# 2026-07-21 — Proposed ledger patches [ActiveV1]

*Prior draft offered & countersigned following a majority pass.*    
***Still outstanding:** P4, P5, parts of P6, and P7.6's 30-40% vs p≈0.1 point, pending further review of the challenge*

*Companion to the 2026-07-20 external review and its 07-21 erratum. Answers Will's question about revising the archive's approach to honest representation: the recommendation is to change nothing about the append-only, date-forward architecture — it is the right architecture, and it is what made the review possible — and to add pointer discipline at exactly the spots where a frozen celebration or a stale billing can mislead a reader who trusts the map. Every patch below is paste-ready or skeleton-ready; none deletes anything.*

---

## P1 — README priority-spine rebilling for 2-2-26 (replaces the "Definitive Feb 2026 audit" line)

> ④ *2-2-26 Rigorous Assessment* — **historical specimen, read with care.** The most confident synthesis of the February era, and the document the V2 Central Reference exists to walk back (see the 6-20 delta: "the over-claiming pole"). On the spine because the Operationalist Pivot narrative and the era's ambitions are best seen here in original strength — not because its claims survive. Its "Budget is a Theorem" framing, PANF scorecard, experimental dictionary, and §5.3 numerical matches should be checked against V2 Tiers 4–5 before citing.

## P2 — Supersession stamp for the 00_canon spine trace (paste at the head of the 6-1 / Liu section)

> **[Status stamp, added YYYY-MM-DD]** The priority framing below ("made a structural prediction that came true") is superseded by the 2026-06-10 consolidated errata, Set A: the temporal-antecedence leg fails (Liu et al. PRL accepted 3 Dec 2025; abstract public before the timestamped records); route-independence survives; priority credit zero; the calibration reading is A8's ("strong private evidence of generative capacity, weak public evidence"). The text below is retained unmodified as the record of what was believed on 06-07.

This is the template for the general fix: wherever the errata demote a claim that a *map-level* document still celebrates, the demotion gets stamped at the point of reading, and the original text stays. The corpus's co-location discipline (6-10 header) already mandates this; it has just not been executed against 00_canon's own maps.

## P3 — Source-material naming convention (one paragraph for the repo README and the Drive workflow)

> Files prefixed `TRANSCRIPT_` are session transcripts: verbatim exports of Will+model working sessions. Ingested third-party source material (video transcripts, paper texts, datasets pasted from elsewhere) uses the prefix `SOURCE_` instead, e.g. `2026-07-18 SOURCE_3B1B_Compression_is_Intelligence_Part_2.txt`. Rationale: filename-based sampling and future-instance corpus reads must be able to distinguish "what we said" from "what we read" without opening the file. Existing misfiled items (the three 3B1B copies) should be renamed, deduplicated to one copy, and — if a session discussing the video exists — that session's export filed beside it under `TRANSCRIPT_`.

## P4 — OT1 N=16000 delta record, skeleton (to be filled from the actual run outputs and countersigned)

```markdown
# Session Delta — OT1: N=16000 [REJECT / PASS — fill], ladder [advanced to 32000 / closed]
**2026-07-[DD]** · tiers: [V]erified · [T]classical · [A]rgued · [O]pen

## Headline
[One line: host regenerated (flag 1, no header, row count 2321 = dim S2(G0(16000)) — verified
independently 2026-07-21), CM control at level 20 | 16000 → residual 0 [Y/N], sweep outcome
across chi in {-4,-8,-20,-40} x both embeddings (+ order-4 branches if run).]

## Instrument state
[Which decoder versions ran; DEPTH used vs rank; primes; runtime; machine.]

## Outcome and ladder consequence
[If REJECT everywhere: b >= 9, a2 >= 8, next rung N=32000 = 2^8*5^3. Note: dim S2(G0(32000))
cuspidal = 4681, Sturm = 9600 (computed 2026-07-21, PARI 2.15.4). If PASS: prediction JSON
committed before grading, per protocol — attach hash + grading result.]

## The story (per Will, 07-21: "the story is interesting")
[Whatever complications occurred — host regeneration issues, memory, partial sweeps —
recorded here, since the 07-05 addendum's last word on 16000 was the voided upload.]

## Files
[Names + storage location — state explicitly that outputs live in Drive "Code, Tests, &
Datasets" (or wherever they land), so no future auditor repeats the 07-20 reviewer's
absence-inference.]
```

## P5 — Records name their script locations (one-line convention)

> Every record whose [V] tags reference session scripts ends with: *"Scripts archived at: [Drive folder / repo path]."* The recent layer's scripts are in Drive "Code, Tests, & Datasets"; the records that cite them do not say so, which is what misled the external review (Erratum E2). One line prevents the next false absence-claim.

## P6 — Cleanup list (mechanical, no judgment calls)

1. 00_canon: remove one of the two identical 6-10 errata files (keep the date-prefixed one).
2. 07-03 ActiveV5: fix internal header "Status: ActiveV1" → ActiveV5.
3. Drive: dedupe verify_conversion_ledger.py, verify_t2_opening.py, verify_dihedral_shadow.py, verify_polar_identification.py, verify_sigma_completion.py, verify_activation_checks.py, verify_parity_quadrature.py, verify_cross_budget_gnew.py, verify_tduality_pnt.py (each uploaded twice); locate or reconstruct audit5.py; dedupe the two completeness_reduction_theorem_note copies and the two 07-01 transmission-functor copies.
4. 3B1B triplicate: dedupe + rename per P3; fix or annotate the ASR garbles if the file is kept as source ("Kolbach-Leibler" et al.).
5. May-14/15 duplicate investigation-record series: collapse to one canonical set with a pointer (already flagged in the catalog's known-gaps; still pending).
6. 90_archive/transcripts: add the missing 07-01 Langlands source transcript (2026-07-01-08-24-54-tep-langlands-tannakian-thread.txt) if it exists anywhere; if it does not, stamp the 07-01 record with that fact.
7. v0.5 date: pin one authoritative date (title says 2025-08-23; the early-corpus synthesis implies Nov 2025 context) with a one-line note reconciling them.
8. Repo: next push should include 50_code/ mirrors of the Drive verify_*.py series and the OT1 16000 artifacts, so the public archive's [V] tags are runnable again.

## P7 — Foundational-cluster errata (from the 07-21 addendum; each is one edit)

1. scale_shape_decomposition_focused_core.md §1: the "Markov morphism… Petz–Sudár" sentence contradicts the later, correct treatment (peel = post-selection, not trace-preserving; DPI does not apply; metric inflates by 1/u). Stamp with a pointer to the 06-17/06-18 correction.
2. Both closure papers + downstream: prefer "equivariance / no-collapse of the Petz family" over "automorphism of the family" (the induced label map is the identity — which is the stronger and more honest statement).
3. manifold_existence note: qualify the Montgomery–Zippin sentence (group-action sense only; under bare topological homogeneity it is the open Bing–Borsuk conjecture, dim ≥ 3). Not load-bearing; still worth the two words.
4. 2026-05-15 supplement_cited_derivation_bures_fisher.md: remove the raw LLM artifact ("Wait, let me redo this carefully:") or stamp it; repair L.6's uniqueness sentence (unitary invariance holds for the whole monotone family and selects nothing).
5. Rename one of the O-a/O-b vs O-A/O-B tracks before the collision bites an auditor.
6. The V2 Central Reference's §2.2 critical-damping/Butterworth sentence (self-refuting as written), §2.1's residual derivation-language ("emerges… not as an external input," contradicted four lines later), and Tier 4.2's 30–40% vs ~10%/p≈0.1 discrepancy — none tracked in any patch list to date.

---

*Nothing above alters the archive's philosophy. The date-forward, append-only, keep-the-mistakes architecture is correct and is the program's most defensible property. These patches only make the maps tell the reader where the ledger has since moved — which is the difference between preserving history and re-serving it.*
