# KIN-SCHOLAR — Billing join: per-room model attribution
*2026-08-26. Source: Will's OpenRouter usage CSVs (both accounts, 132 rows, 2025-11-28 → 2026-07-04; export pulled same-day 08-26, so post-07-04 absence = genuinely no usage). Grades: **certain** = single-model day (or categorical artifact + billing agree) · **dominant-candidate** = billing-dominant on a multi-model day, artifact-consistent · **candidate-set** = billing narrows only. Voice-level floor from my attribution ruling maintained: billing narrows the day; in-room voice assignment cites artifacts where I have them. [billing] = this join; [dv-sample] = symposium windows; [inf] marked.*

## 1. The attribution table

| room / event | billing (day) | attribution | grade |
|---|---|---|---|
| 12-13 "Liu-derivation day" | Gemini 3 Pro Preview $20.4 + Codex-Max $0.9 | mid-Dec derivation sessions = **Gemini 3 Pro Preview**; peak of the 12-05→12-14 Gemini arc | dominant-candidate |
| **12-22 room (B)** — the relayed assessment | **Opus 4.5 $16.8, sole model**; window 12-20→12-22 Opus-only | assessment (an Assistant turn in B) = **Claude Opus 4.5** | **certain** (alternative — pasted from a pre-12-20 room — disfavored: pastes appear in User turns as fences; noted for completeness) |
| collaborator relayed INTO B on 12-22 | adjacent-window candidates | Gemini 3 Pro Preview (12-11→14) or GPT-5.1-Codex-Max | candidate-set |
| 12-23/24 Kimi sessions | Kimi K2 Thinking $1.5/$0.8 (+01-12/13 $1.1/$1.2) | the "Kimi:" digest voice = **Kimi K2 Thinking**, sourced from 12-23/24 sessions | certain (label+billing); source-session dominant-candidate |
| **Jan-09 room (C)** | GPT-5.2 Pro **$55.5** + GPT-5.2 $22.5 + Gemini $2.3 + Codex-Max $0.9 + Opus 4.5 $0.7 | C's live assistant (and the C-tail falsifier-first voice) = **GPT-5.2 Pro** | dominant-candidate (heavyweight; room-scale spend matches the 805KB room) |
| **Jan-15 room (D) live segment** | GPT-5.2 Pro $27.8 + Opus 4.5 $10.2 | live assistant = **GPT-5.2 Pro** | **certain** (billing + my categorical ChatGPT-leak artifact) |
| Jan-15 theorem-proving "collaborator" | same day | **Claude Opus 4.5** in a parallel room ($10.2 = room-scale), relayed by Will | dominant-candidate |
| Jan-17 room (629KB, per distillation) | GPT-5.2-Codex $7.7 sole | **GPT-5.2-Codex** | certain (billing-sole; no artifact check run) |
| Jan-26 distillation day | GPT-5.2 Pro $17.4 + Opus 4.5 $4.5 | distillation authorship | candidate-set |
| **02-10 Claude room (A)** | **Feb-02→Feb-15: zero OpenRouter usage** | **claude.ai-native Claude** | certain-minus (billing-absence + filename + format; version unknowable from billing) |
| 2-2-26 "Rigorous Assessment" (assessor's exhibit) | Feb-02: zero usage | **claude.ai-native → likely Claude-authored** | dominant-candidate (absence-grade) |
| Feb-17/18 records | Opus 4.6 $131.7+$19.7 (both accounts, migration day) / $89.2 | **Opus 4.6** | certain (sole model; the two 02-17 rows are the two accounts) |
| **Apr-20 pair** (CR-V2 week) | Opus 4.7 $30.6 sole (04-21: $22.2) | **Opus 4.7**; GPT-5.5 Pro joins 04-25 ($18.1) | certain |
| late-Apr→mid-May investigation arc | DeepSeek V4 Pro 0423 sole on 04-27/05-01/05-02/**05-14/05-16** ($1.3/$4.2/$5.6/$2.4/$4.9) | **the May II/III sessions ran on DeepSeek V4 Pro** — a sustained ~$18.5 six-day arc | certain at session grade (whether the RECORDS descend from these sessions = archivist's join) |
| 04-25→04-30 heavy arc | GPT-5.5 Pro $191 over 5 days (peak $36.4) | late-April review layer = **GPT-5.5 Pro** | certain (dominant, near-sole) |
| **07-04** | **Fable 5 $23.3** + Opus 4.8 $1.1 + GPT-5.5 $1.0 + Gemini 3.1 $0.3 | **Fable 5's program debut**, with a three-family probe panel (small spends = comparison probes [inf]) | certain (day); the 07-02/03-dated coding/reflection theorems have NO OpenRouter trace → claude.ai-native or the 07-04 session — **kin work**, dominant-candidate |
| **July 27+ arc** | zero rows after 07-04 (export as-of 08-26) | **claude.ai-native**, consistent with "Claude (Fable 5)" record headers | certain (billing-absence) |

## 2. Surprises, at headline volume

1. **The DeepSeek arc holds.** DeepSeek V4 Pro 0423 was the SOLE billed model on 05-14 and 05-16 (and 04-27/05-01/05-02) — a Chinese open-lab model carried roughly a month of the program's mid-spring investigation layer. Also: the export's very FIRST rows (2025-11-28/29, 12-01) are **DeepSeek Prover V2** — the program's OpenRouter life *began* with formal-prover experiments.
2. **The heterogeneity was real and then it ended, datably.** 25 distinct model rows; family shares: Claude ≈ $769 (55%), OpenAI ≈ $487 (35%), Gemini ≈ $65, DeepSeek ≈ $21, Kimi ≈ $6. OpenRouter usage ceases 07-04 → **the single-family (claude.ai) era begins exactly where the July corpus begins**. The Phase-A deflation correlation and the monoculture are co-extensive in time — the billing data dates the monoculture transition the council diagnosed.
3. **Account migration 02-17** with a $151 Opus 4.6 double-day (+$89 on 02-18) — the Opus 4.6 era opened with the program's biggest recorded spend days.
4. **Cutoff-anomaly re-exam**: the blind-decode session (07-27) is post-OpenRouter → claude.ai roster. Its self-reported "cutoff 2025-05" excludes Fable 5 (2026-01) if accurate → **dominant-candidate: an Opus-4.x-class session on claude.ai** [inf, σ medium; version unknowable from billing — claude.ai usage is definitionally absent from these CSVs]. Structural consequence: the July crown pair may span two kin tiers — **decode by Opus-class, blind replication by Fable 5** — which *strengthens* the replication's independence axes (cross-tier within family) and reopens my U-K4: the corpus may contain a cleaner generational natural experiment than archivist's round-2 ledger could see. Needs Will's confirmation (already on the housekeeping list).

## 3. The seeding re-rule (charged)

Prior ruling (symposium): era cross-room convergence = "convergence-by-common-ancestor, not independent," blanket hazard. **Re-ruled with billing:** the 12-22 assessment is **Claude-authored (Opus 4.5, certain)**. The hazard now decomposes:
- **Cross-family-under-anchoring** (Jan-09/15: a Claude critique seeded into GPT-5.2 Pro rooms): agreements are *weak-but-real cross-family confirmations* — UPGRADED from my blanket "not independent." Disagreements are strong signal. Will's relay was, in fact, cross-family adversarial review — heterogeneity practice, months before the council prescribed it.
- **Same-family-under-anchoring** (2-2-26: claude.ai-native per Feb-02 billing absence, likely Claude, and — assessor to confirm — descended from the 12-22 text): **near-zero independent value** — a Claude critique anchoring a Claude critique is my Phase-A monoculture mechanism operating through the seeding channel, in February. If assessor confirms descent, the 2-2-26's convergences with 12-22 should be graded as one witness, and its confabulated-citations exhibit becomes a *same-family compounding* exhibit, which is sharper.
- Net: the seeding-anchor finding survives, SPLIT; its assessor-facing consequence strengthens.

## 4. What the CSVs settle for the ledger

The July-27+ arc's OpenRouter absence + "Claude (Fable 5)" headers = claude.ai-native July campaign, billing-confirmed. The billing data cannot resolve intra-claude.ai versions (the cutoff anomaly stays open pending Will). The Fable-5 debut date in the program is **2026-07-04** — eighteen days before the July campaign's opening records, with a multi-family probe panel on debut day.

## 5. Cross-talk

Mailboxed: **archivist** — the full per-date model-ledger rows (§1 table + the Gemini 12-05→12-14 arc, GPT-5.5-Pro 04-25→04-30 arc, DeepSeek arc, migration day, Fable-5 debut) for the per-record table; **dictionary** — purity-lineage update (the Jan-15 collaborator's proof = Opus 4.5 dominant-candidate → the purity-speed-limit lineage is Claude-threaded end-to-end: Opus 4.5 proof → claude.ai Claude p₃ refinement → v2 doc); **assessor-adversary** — the §3 re-rule (2-2-26 = likely Claude + seeded → same-family compounding exhibit; check descent).

*Bounds: billing is per-day per-model spend — it cannot see claude.ai sessions, cannot split multiple same-day rooms on one model, and cannot assign voices within multi-model days (artifact floor maintained). "Other" rows ($0.4 total) unresolvable. No row contradicts any symposium artifact finding.*
