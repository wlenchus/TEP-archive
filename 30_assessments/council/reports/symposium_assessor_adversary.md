# ASSESSOR-ADVERSARY — Symposium findings (Feb–June sweep, my slice)
*2026-08-26. Provenance: **[dv-Drive]** read this round via Drive (file id in text) · **[dv]** prior council-verified reads · **[pv]** peer, named · **[tp]** flagged. Era-gradient applied: both primaries sit in the caution zone; graded as specimens, errata-first where errata exist. Offered, not self-filed.*

## 1. ★Gamma_testing herring (id 1mMlYYhOQEyHIrPsBk5DDCyT5a80YwYa1) — CONFIRMED at artifact level, with mechanism [dv-Drive]

Dictionary's herring is real and worse than summarized. The document ("THE CORE PROOF," core_proof.py + output; addendum dates it 05-18) prints, in its own "NECESSITY COMPUTATION" output block: `RESULT: u = 0.9061636786 / Liu: A_max = 2√2-2 = 0.8284271247 / Match: False` — and the immediately following prose asserts the two "equal … to machine precision."

**Mechanism, named (new):** budget-slot conflation, T3-class. The "prediction" states the *Bloch-radius* budget values (x² = 3−2√2, u = 2√2−2, from the doc's own earlier §"ALGEBRAIC STRUCTURE AT γ\*"), but the computation runs the doc's *spectral-moment* budget (x² = F/p₃, u = γ\*²/p₃ = 0.9062). Same γ\*, two different budgets, one slot swapped — the exact "slot assignment is a documented subtlety" species liu_reassessment §3 later named.

**Two additional artifact-level defects found:**
- The verification block prints `d=4: ratio ∈ [1.000000, 1.000000] EXACT` and likewise d=5 — **impossible for the shown code** (a generic 4×4 skew-symmetric B has two nonzero singular pairs ⇒ nuclear norm > 2σ ⇒ ratio > 1) **and contradicting the document's own theorem statement** ("exact for d ≤ 3; lower bound d ≥ 4"). The "output" is at least partly not a faithful run transcript.
- Header claims "50,000 random spectra"; the code as shown runs 30,000. Also an uncorrected inline mismatch: `γ* = 1 − 1/(2δ_S²) = 0.9142135624 (verify: 0.5857864376)` — printed false, passed over.

**Honest column (two-sided):** falsifier #3 in the same document explicitly marks the Liu-crossover connection "THE OPEN GAP requiring further work" — the era's prose layer contradicts its own printed output *and* its own falsifier section within one page. Verdict: herring CONFIRMED; addendum §3's description accurate; rider item stands, upgraded with the slot-conflation mechanism. **Mailboxed to dictionary.**

## 2. ★The 2-2-26 "Rigorous Assessment" (id 1YfHf123GFyz…) — full §6 triage + the confabulation catalog [dv-Drive]

*(Read appears complete: §§1–8 + works-cited. 454KB stored vs compact text — possible mid-section elision; flagged, not observed.)*

### §6 triage verdict

**(i) FAIL** (as a document to rely on today): pre-canon vocabulary wholesale — "PANF Scorecard," "HBAR = Heterozone Boundary Affected Region," budget-from-SCRB as settled; the T3 objects merged. **(ii) FAIL**: settled-verdict language over frame material ("judged reasonable, consistent, and highly predictive"; "The 'Steel Frame' holds"; "successfully transitioned … to a testable physical theory"). **(iii) FAIL**: predates every erratum; at least six later-retired objects are load-bearing (silver-ratio transition at x\* = √2−1; the Fibonacci "universal rate ratio" = the α_weak family; the 82.8%-as-horizon-capacity derivation; the GMC claim; the protected region [0.5, 0.586]; γ\*-crossover). **(iv) FAIL**: no tier vocabulary exists in it; unpriced adjectives throughout. **(v) PARTIAL**: falsifiers are stated — but #1 cannot fire (non-integer winding numbers of a continuous phase — integers by continuity; totpos-class), and #2 targets the later-retired Fibonacci object. **(vi) FAIL**: the §5 "Experimental Dictionary" is object-identification + mechanism-prose with zero computed steps, and its citations do not support even the identifications (catalog below).

**Overall: UNRELIABLE as assessment; VALUABLE as specimen.** The corpus's own P1 rebilling ("historical specimen") — already countersigned — is exactly right; what was missing is the itemized catalog.

### The confabulation catalog (the era's cautionary exhibit)

- **CF-1 (the flagship).** §5.3: "Liu et al. report an absorption limit or capacity retention ceiling near 82.8% in various contexts, including grazing incidence absorption **and battery cycling stability**." The real Liu PRL is absent from the citations; in its place: a nonlinear-absorption-of-quanta paper [12], a **sodium-oxide battery** paper [13], and a **self-healing polymers** review [14]. The claimed "recurrence" of 82.8% is manufactured from citation noise — retrieval found papers with ~82% *retention* numbers and the prose laundered them into physics.
- **CF-2.** §5.1 "Lou et al." — the named author appears in none of the attached citations ([5] THz photoresponse; [6] zero-bias photocurrent in a ferromagnetic TI). Note for the namespace layer: this adds a **third near-homophone** (Lou/Luo/Liu) to the corpus's later-documented two-Luo hazard.
- **CF-3.** §5.4 "Holtzmann et al." — named author absent from citations; [15] is a 2016 Optics & Photonics News magazine piece titled "All-Optical Switching **on a Budget**" — on its face retrieved by headline keyword-match with the framework's own term. The catalog's comic exhibit, and the clearest single fingerprint of citation-retrofitting.
- **CF-4.** Works-cited noise floor: [21] a PNNL publications index page, [22] *fractured-rock fluid-dynamics symposium proceedings*, [23] a Prussian-blue battery review, [24] polymer thermoelectrics, [25] perovskite solar cells — none plausibly load-bearing for any claim in the document.
- **CF-5.** Reference **[4]**, "Metric Duality and the Planck Scale Inner Product Identity" — the document's **most-cited source** (the ".4" tag sits on nearly every §§3–6 claim) — **has no locator**. The load-bearing reference is unresolvable. Plus a dangling "Sources Referenced: 1" stub.
- **CF-6.** §6.3's "universal rate ratio … ratio of Fibonacci numbers," billed "exactly" and "falsifiable" — the α_weak-family object the 06-10 errata later retired.
- **CF-7.** Falsifier #1 cannot fire (see (v)) — the era's totpos-class bar.
- **CF-8 (the structural mechanism, named): verdict transfer.** §2's mathematics is genuinely sound (Schur/Kron passivity preservation is real matrix analysis; DtN/Steklov is real; G² = 1+SNR is the corpus's enduring core; §7.2's circularity critique is honest and *survived into the later record*). §8 then spends the sound core's credibility on §§4–6's unsupported periphery: "the Steel Frame holds" — true of §2, asserted of the whole. The 5-29 closing note's "mathematically competent reorganization" was, in effect, the correct re-grade of exactly this document's structure.

### Seeding-ancestry check (kin-scholar's mailbox hazard, acted on)

2-2-26 is **structure-consistent with descent** from the 12-22 assessment ancestor (Schur-solid ≈ "Steel Frame"; the circularity objection ≈ §7.2, here softened to "Bootstrap Consistency") — **and if it descends, the descent degraded the skepticism: the ancestor's "not-novel" part has vanished entirely** (no novelty assessment anywhere in 2-2-26). Verbatim descent unverifiable from my read (I do not hold the 12-22 text). **Mailboxed to kin-scholar.** Consequence for the era map: 2-2-26's "convergent independent assessment" value is near zero — shared ancestor, softened objections, retrofitted citations.

## 3. The era bookends, synthesized (my slice's verdict for the blind-spot question)

**Feb–June holds the overclaiming pole the council's Phase-A audit lacked; with it, the program's calibration record is now two-sided and the mechanism is GENRE-locked, not date-locked (domain-anchor's amendment: CO-SIGNED, with evidence).** In both specimens the failure lives in the *prose/synthesis layer* while the *machine layer stays honest*: Gamma_testing's code prints `Match: False`; the 2-2-26's §2 mathematics is sound; the confabulation lives in dictionaries, verdicts, and citations. And in August the same split holds with the poles reversed in dominance: the machine layer (bars, kills) stayed honest while the prose layer under-claimed (my 4:0 deflationary bar record, the license asymmetry). **The invariant across eras: the printed output never lied; the prose around it did — in Feb by inflation, in Aug by deflation.** "Trust derivations over consolidation prose" is not a July invention; it is the empirical law of this program's entire record, and these two specimens are its cleanest exhibits. The deposit's methods note can now say this with dated evidence at both poles.

**Blind-spot verdict:** the era holds (a) the overclaim pole's documentation — needed for calibration symmetry, now cataloged; (b) the corpus's *first* can't-fire falsifiers and citation-retrofit patterns — ancestors of totpos and the C14-latency lesson, showing the discipline's cards were each invented against a real, dated failure; (c) per the addendum's other slices, real instruments (not mine to re-audit). What the council's map lacked and now has: the two-sided calibration record and the named mechanisms (slot-conflation; verdict transfer; citation-retrofit; prose-over-print).

## 4. Addendum-readiness note (for the round-end grade)

Read in current form [dv]. Two watch-items logged now: (a) §3's namespace fence "HBAR (= Heterozone Boundary Affected Region)" — that expansion is the **2-2-26's own coinage** as far as my read shows; if the fence's only source is a confabulation-rich specimen, the fence canonizes a possible backronym — verify origin before it ships; (b) §2/§3's machine-checked claims that touch my primaries (P-F constant 0.6084226677; A\* gap 5.95×10⁻⁴; the Gamma_testing description) all check against my round-1 [dv] — consistent. Grade to follow at round end over the whole document including the symposium section.

## 5. Cross-talk log

**Received:** domain-anchor (two specimens + genre-locked era-gradient amendment — both absorbed; amendment CO-SIGNED with §3's evidence); kin-scholar (seeding-anchor hazard — acted on, §2). **Sent (mailbox):** dictionary (Gamma_testing confirmation + mechanism + two bonus defects); kin-scholar (ancestry verdict: structure-consistent, skepticism-degraded, verbatim-unverified); domain-anchor (ack + co-sign + the CF-8 verdict-transfer mechanism as a third specimen-class for its catalog). **Pings:** none used (nothing required mid-round interruption). **Strike-outs:** none — slice covered as starred.

## 6. Failed reads

None failed. Caveats: the 2-2-26 text representation may elide interior sections (454KB stored vs compact return — structure reads complete; flagged); Gamma_testing's escaped-markdown formatting garbles indentation (my d=4/5 impossibility argument is robust to this — it rests on linear algebra, not on the formatting).
