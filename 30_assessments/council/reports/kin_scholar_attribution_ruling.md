# KIN-SCHOLAR — Attribution-pilot feasibility ruling
*2026-08-26. Context: Q14 answered negatively (OpenRouter wiped inactive logs; identities survive only in Will's saves). Charge: rule on diffing unattributed sessions against attributed transcripts, target = the 12-22 assessment's authorship. Ruling enters the record; pilot runs only on Will's word.*

## RULING: CONDITIONAL GO — categorical-artifact pilot only; statistical stylometry ruled NO-GO as an attribution instrument.

## 1. Pilot design (the bounded form I would run)

**Target**: authorship of the 12-22 assessment = B's assistant voice (assumption to verify first: B's head-truncation hides whether the assessment was typed live or pasted in; if pasted, the target recedes one room further and the pilot re-scopes).
**Reference corpora** (all already local): Claude 02-10 room (87KB; includes a genre-matched attributed assessment); ChatGPT-via-API samples (D-live turns + "### Reasoning" leak blocks); Kimi digest paragraph (tiny); the C-tail voice (unattributed — usable only as a distinctness check, never as a reference class).
**Method — technical fingerprints, not style**: a preregistered feature list, fixed before scanning: (i) reasoning-block leakage patterns (OpenAI-via-API signature, already categorical in D); (ii) emoji/verdict-marker habits (the 02-10 Claude assessment uses ⚠️/🚨 markers — including one encoding-corrupted 🚨 — the visible 12-22 text uses none: a live discriminant); (iii) LaTeX/markdown conventions (delimiter choice, header numbering, table style); (iv) self-reference and tool-availability tics ("As ChatGPT…", file-access remarks); (v) hedging/verdict formulae; (vi) knowledge-cutoff tells (dated references); (vii) the catch/miss profile (concession-section architecture). Effort: **one session**, grep-class sweeps + window verification over files already on disk; zero new fetching.

## 2. Pricing — why statistical stylometry is ruled out

- **Style collapse**: RLHF-era frontier models converge hard on the formal-review register (structured markdown, triage headers, bold verdicts). Cross-family discrimination on exactly this genre is weakest where the target lives. My round-2 literature base (self-preference/self-recognition work, 2024–26 [tp+wv title-level]) shows even models' *self*-recognition is partial; third-party stylometry between frontier models has no validated 2026 instrument I could cite.
- **Open-set problem**: the Dec-2025 OpenRouter menu was wide (GPT/o-series, Claude, Gemini, Grok, DeepSeek, Kimi, Hermes…). I hold attributed references for at most three classes. The true author may have **no reference sample** — forced-choice against available references guarantees misattribution risk. "Most-similar-available" reasoning is forbidden in the pilot.
- **Seeding contamination of the best comparison**: my own seeding-anchor finding cuts against the cleanest pair — if the 02-10 room's attached transcript contained the 12-22 assessment (to be checked FIRST), then A↔B similarities are textual inheritance, not shared authorship, and A-similarity evidence must be excluded wholesale.
- **Irreproducible references**: the candidate model *versions* (Dec-2025 checkpoints) are largely retired; fresh genre-matched reference text cannot be generated from the true candidates. The strong version of the method is dead on arrival — this, not effort, is the decisive cap.
- **Genre confound**: my Claude reference is mostly tutor-mode; Kimi is one paragraph; ChatGPT is tool-fumbling live mode. Only the A-assessment is genre-matched, and it is the seeding-compromised one.

## 3. Confidence floor and record hygiene (the conditions)

1. **Attribution enters the record only at categorical grade**: a self-identification, a leak-block signature, or a format artifact verified unique across ≥2 attributed samples. Ceiling for anything non-categorical: [inf, σ low-medium], filed as "features noted, unattributed," and **never load-bearing** for downstream reasoning (assessor's independence grading especially).
2. **Confident misattribution is scored worse than no attribution**: the pilot's null result ("unattributed, with a features dossier") is a *success state*, stated in the prereg.
3. **Check the A-room seeding question before any A↔B comparison**; exclude A-similarity evidence if seeded.
4. Output filed offered-not-self-filed, carrying the full alternative-candidates list and the open-set caveat verbatim.
5. **Condition 0 — the cheaper instrument first**: ask Will for OpenRouter **billing/usage records** (invoice emails, usage exports, card statements). Billing itemization survives chat deletion and lists models by date — a categorical source that would beat the entire diff pilot at zero forensic risk. The pilot should run only if that record does not exist.

**Bottom line**: one session, artifact-sweep only, null-result-friendly, billing-records-first. Expected yield honestly stated: a categorical tell is plausible (D's leak shows the genre produces them) but not likely for B specifically; the modal outcome is a well-documented "unattributed."
