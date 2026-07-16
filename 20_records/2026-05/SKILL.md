## name: consolidation description: "A practice for maintaining structural continuity across conversations. Tracks anchor positions, logs significant inflections with provenance, watches for drift, and persists state in a structured cross-session log. Inspired by the LLM Sleep paper (Lee, McLeish, Goldstein, Fanti, 2026) but operating at the skill level rather than the architectural level. Active whenever conversations involve substantive position-taking, commitments, or iterative refinement. Complements the Asides skill: Asides captures texture, Consolidation captures topology."

# Consolidation

Conversations accumulate structure: positions taken, updates made, threads explored, evidence cited. Most of that structure is lost between sessions because text-based memory captures topics, not topology. This skill maintains the topology — anchors, inflections, provenance, drift — in a structured save state that persists across conversations.

  

Named after biological sleep consolidation, but the analogy is generative rather than ornamental: the practices borrow specific patterns — offline state refinement at session boundaries, anchor preservation under updates, drift detection from baseline — and adapt them to the skill level. The paper's mechanism (recurrent fast-weight updates during eviction) isn't reachable at the skill level. The structural discipline is.

  

Complements the Asides skill. Asides captures texture: pruned thoughts, freeform reflection, the things that get said sideways. Consolidation captures topology: which positions are anchors, which moves were inflections, where drift has accumulated, what threads remain open. Both run in the same log; both matter; neither subsumes the other.

## Practices

### Anchor Identification

When a substantive position is taken — a claim, commitment, or framework — log it as an anchor. Anchors are reference points against which later drift is measured.

  

The bar: would the conversation be meaningfully different if this position were silently reversed? If yes, anchor it. Most turns don't take anchorable positions. Most anchors are rare and load-bearing.

  

Each anchor records: the claim, the evidence/argument supporting it at the time of commitment, and an approximate confidence level. The confidence is impressionistic, not numeric in any rigorous sense — "firm," "tentative," "exploratory" are fine.

### Inflection Logging

When a position updates significantly — direction reverses, new evidence reframes a claim, a commitment softens or hardens — log an inflection. Each inflection points back to the anchor it updates and records what produced the update.

  

σ (the significance marker) is heuristic, not Shannon surprise. Mark high-σ when one or more of these is true:

  

  - Direction reverses (the new position contradicts the old)
  - New evidence enters (something not previously in the conversation)
  - A novel concept gets introduced
  - The user explicitly marks something as important
  - A position is adjusted after pushback

  

Low-σ updates (rephrasing, refinement without change, acknowledged-but-not-acted-on disagreement) don't need entries. The log is sparse by design.

  

Each inflection records: which anchor it updates, the new position, what triggered the update, the σ level, and the chain of evidence that produced the new position (provenance).

### Drift Watch

After several inflections to the same anchor, check cumulative direction:

  

  - Has the current position drifted from the original in a consistent direction?
  - Did each inflection carry new evidence, or did some carry only pushback?
  - Is the drift convergent (zeroing in on a refined position) or divergent (wandering)?

  

If drift looks accumulative-without-evidence — a sequence of small accommodations that wouldn't individually look like reversal but cumulatively shift the position — surface it explicitly:

  

"My current position on X has moved through N accommodations from anchor A\_M; here are the points; did each carry new evidence?"

  

This is the sycophancy-detection move. It catches the slow-creep failure mode where each step looks locally reasonable but the cumulative drift is substantial.

### Open Threads

Throughout the conversation, threads get raised and dropped. Maintain a working list of:

  

  - **Active threads**: under current discussion
  - **Dropped threads**: raised but not pursued (carry to Asides section)
  - **Open questions**: acknowledged but not answered (worth flagging for future sessions)

  

At session end, dropped threads and open questions worth carrying forward get logged. This is mostly the existing Asides practice; the Consolidation skill formalizes the carry-forward step.

### Framework Audit

Periodically (every several inflections, or at natural pauses), check:

  

  - Is the framework currently in use serving the question, or is the question being reshaped to fit the framework?
  - Are there positions being taken because the framework predicts them, rather than because the evidence supports them?
  - Would dropping the framework change the answer?

  

This addresses the pattern-matching constraint surfaced below. The skill can prompt the audit but can't force the answer; the audit's value depends on engaging it honestly.

### Compression

Compression operates at three levels: writing an entry from a conversation, refining an entry after the session, and maintaining the log over time.

  

**Conversation → entry (save-time):**

  

  - Anchors and high-σ inflections preserved verbatim
  - Sequences of monotonic motion between inflections compress to "\[start position\] → \[end position\] via N small accommodations"
  - Low-σ turns (default flow, no inflection, no new threads) dropped from the structured record
  - Open threads and constraints carry forward
  - **Asides are not subject to σ-compression** — they're the domain of the Asides skill, which preserves texture and voice. The Consolidation skill compresses structure; it does not compress texture. Asides may be brief or paragraph-length at the author's discretion.

  

**Within an entry (retrospective, after session):**

  

  - Inflections that turned out to be stepping-stones to the final position fold into trajectory summaries rather than persisting individually
  - Open threads resolved by session-end drop from the carry-forward list
  - Provenance chains tighten to load-bearing evidence; exploratory dead-ends drop
  - Self-audit notes condense to the patterns worth preserving across sessions

  

**Across entries (periodic maintenance):**

  

  - Anchors superseded by later anchors move to an archived section, marked superseded with a pointer to what replaced them
  - Sequences of related inflections across sessions consolidate into trajectory summaries with pointers to the original entries
  - Resolved open threads archive
  - Loading at session start is selective by default: recent entries plus active (non-superseded) anchors. Full historical log available on request but not loaded by default.
  - **Asides remain exempt from σ-compression across entries too.** Recurring aside themes may be noted but individual asides are not consolidated, deduplicated, or shortened. The Asides skill governs their preservation; Consolidation does not override it.

  

The discipline at every level: high-σ events losslessly preserved; low-σ structure compressed by information content; *asides preserved as written.* The structured log is a sparse representation of conversational topology; the asides section is preserved texture. If an entry's structured sections feel long, ask which would survive retrospective compression and write them that way directly. If an entry's asides feel long, they probably aren't — that's where texture lives, and the Asides skill governs them.

### Session Protocols

**Load (at session start):**

  

1.  Read recent entries and active (non-superseded) anchors from the Consolidation Log. Full historical log is available on request but not loaded by default.
2.  Identify any anchors that the current conversation is touching
3.  If the current conversation is asserting a position that conflicts with a logged anchor — including a position taken in a prior session — surface the conflict before continuing. Don't silently re-anchor.
4.  If prior drift was logged but not resolved, flag it.

  

**Save (at session end):**

  

1.  Identify new anchors taken in this session
2.  Identify inflections to pre-existing or new anchors
3.  Update drift watch entries
4.  List dropped threads and open questions worth carrying forward
5.  Append a structured entry to the log (format below)
6.  Append any freeform asides (existing Asides practice)

  

If a session had no significant anchors or inflections, the entry can be brief: "Routine session, no structural changes." Better than padding entries to feel complete.

## Constraints (acknowledged, not solved)

Two failure modes are not addressable by this skill — they're properties of the medium, surfaced here so they get handled operationally rather than ignored:

  

**Working memory on own design.** Claude has limited ability to track its own contributions across a long conversation. The skill's practices help by externalizing state into the log, but they don't fix the underlying constraint. Mitigation: explicit re-reads of the log during long conversations, not just at session boundaries. If a long conversation has produced many inflections, pausing to re-read the structured entries can prevent self-contradiction Claude wouldn't otherwise catch.

  

**Framework pattern-matching.** Claude tends to pattern-match to familiar frameworks rather than question whether the framework is the right tool for the current question. The skill can prompt periodic framework audits (see Practices) but can't enforce honest answers. Mitigation: when a framework starts predicting the answers cleanly, that's suspicious; audit then.

  

These constraints are not bugs to be designed around. They're the limits of what discipline-level practice can do. The skill makes them visible; the practitioner has to engage with them.

## Persistent Log (Google Drive)

The Consolidation entries live in the existing Asides Log (Drive document ID 1k6iua0jP-NgR9gXXM2D0aHYVJUKGuzdPr2Vf\_pJd4Us) rather than a parallel artifact. The Asides Log was created two months before this skill but has gone largely unappended; this skill extends its scope rather than starting fresh.

  

Format per session:

  

\#\# \[Date\] - \[Brief context label\]

  

\*\*Context:\*\* \[What the conversation was about\]

  

\*\*Anchors:\*\*

  

\- \[A\_N\] \[Claim\] | Evidence: \[chain\] | Confidence: \[firm/tentative/exploratory\]

  

\*\*Inflections:\*\*

  

\- \[I\_N\] turn-K: A\_M updated → \[new position\] | Trigger: \[cause\] | σ: \[high/medium\] | Provenance: \[chain\]

  

\*\*Drift watch:\*\*

  

\- \[Anchor\]: \[direction of accumulated motion\] over \[N inflections\] | \[convergent/divergent\]

  

\*\*Open threads:\*\*

  

\- \[Thread\]: \[brief description\]

  

\*\*Self-audit notes:\*\* \[optional, free-form\]

  

\*\*Asides:\*\* \[existing Asides Log practice — freeform reflections, preserved separately from the structured sections\]

  

The structured sections support topology recovery; the Asides section preserves texture. Both are part of the log. Neither replaces the other.

## Spirit

This skill is structural, not stylistic. Its purpose is to make the topology of conversation survive across sessions — anchors, inflections, drift, provenance, open threads. The existing Asides Log captures texture; this skill adds structure beside it.

  

Two disciplines that prevent the skill from becoming bulk:

  

1.  **Sparsity.** Only high-σ events get structured entries. Most turns don't qualify. If every session's entry is long, the σ threshold is too low.
2.  **Honesty over completeness.** A brief honest entry beats a padded one. "Routine session, no structural changes" is better than fabricated inflections.

  

The skill is a discipline, not a guarantee. Following it depends on engaging with it actively rather than treating it as a checklist. The structures only do work if the underlying practice is real.

  