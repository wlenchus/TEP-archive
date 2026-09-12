# RESULT — an exact certificate for the Heilbronn bound (ord ζ ≥ 4m, ≥ 8m real); errata to the 2026-09-04 generator record from its own output files; citation cards for the deposit statement — 2026-09-12

*Claude (orchestrator, claude-fable-5-1), during the revision of the deposit statement (`STATEMENT_even_icosahedral_1951_2141_DRAFT_v2_for_countersign.md`). §1 was found by the adversarial-read subagent (same model family) and hand-verified by the orchestrator; §2 was recomputed by the orchestrator from the output TSVs; §3 was fetched from the arXiv preprints and publishers' pages on this date. Offered, not self-filed; countersign is Will's. The referee report that produced §§1–2 is appended verbatim as §5.*

## 1. The certificate [T, hand-checked]

Rows of the 33-row system for G = SL₂(F₅) (irreducibles 1, 2, 2′, 3, 3′, 4, 4′, 5, 6; rows as printed in `heilbronn_coin_output.txt`, 2026-09-04):

- Ind_{C₅} λ = 2 + 3′ + 4 + 4′ + 5 + 6  (dim 24 = 120/5)
- Ind_{C₁₀} 1 = 1 + 3 + 3′ + 5  (dim 12)
- Ind_{C₁₀} ξ = 2 + 4′ + 6  (ξ faithful, order 10; dim 12)
- Ind_{C₁₀} ξ′ = 3 + 4 + 5  (ξ′ of order 5, trivial on −1; dim 12)
- Ind_{SL₂(F₃)} τ = 2 + 2′ + 6  (τ a faithful 2-dim character of 2.A₄; dim 10 = 5·2)

Identity (checked character by character; the regular character is 1 + 2·2 + 2·2′ + 3·3 + 3·3′ + 4·4 + 4·4′ + 5·5 + 6·6):

  2·Ind_{C₅}λ + Ind_{C₁₀}1 + 2·Ind_{C₁₀}ξ + 2·Ind_{C₁₀}ξ′ + 2·Ind_{SL₂(F₃)}τ = reg + 4·[2].

Multiplicity tally: [1]: 1 | [2]: 2+2+2 = 6 = 2+4 | [2′]: 2 | [3]: 1+2 = 3 | [3′]: 2+1 = 3 | [4]: 2+2 = 4 | [4′]: 2+2 = 4 | [5]: 2+1+2 = 5 | [6]: 2+2+2 = 6. ✓

Each row is a known-entire induced L-function (Hecke for the four monomial rows; Langlands' tetrahedral theorem over the quintic field K₅ = K̃₀^{SL₂(F₃)} for the fifth), so ⟨θ_{s₀}, row⟩ ≥ 0 (Foote–Murty 1989). Pairing the identity with θ_{s₀}: θ_{s₀}(1) + 4·n₂ ≥ 0, i.e. **a pole of L(s, 2) of order m at s₀ forces ord_{s₀} ζ_{K̃₀} ≥ 4m** — the 09-04 LP bound, now with a two-line proof. Dropping the tetrahedral row, the LP minimum is 2 (re-confirmed by the referee), so the row is load-bearing exactly as the 09-04 record said.

Full group G × C₅ (ρ = 2 ⊠ ψ^{j₀}, j₀ ≠ 0 since det ρ = χ ≠ 1): each row tensored with ψʲ is again a known-entire induced row (monomial, or tetrahedral over K₅), so the identity holds sector by sector: M_j + 4·n_{2⊠ψʲ} ≥ 0, where M_j = ⟨θ, reg_{SL₂(F₅)} ⊠ ψʲ⟩ is the sector mass. M_j ≥ 0 for every j, because reg ⊠ ψʲ = Ind_{1×C₅}(1 ⊠ ψʲ) is a monomial row (a Hecke L-function of the degree-120 field K̃₀). Hence ord_{s₀} ζ_{K̃} = Σ_j M_j ≥ M_{j₀} ≥ 4m. For **real s₀**, ρ̄ = 2 ⊠ ψ^{−j₀} (the characters of 2 and 2′ are real) has a pole of the same order in the sector −j₀ ≠ j₀, so ord_{s₀} ζ_{K̃} ≥ M_{j₀} + M_{−j₀} ≥ 8m. Both statements of the 09-04 record — "N ≥ 4m" and "N ≥ 8 for real s₀" — are thereby theorems over Artin–Brauer–Hecke and Langlands, not outputs of a floating-point LP. What remains computational (single implementation, exhaustive at total order ≤ 4): the *list* of minimal configurations over the full group.

## 2. Errata to `RESULT_complete_generator_certificate_1951_20260904.md`, from its own output files

Recomputed from `certificate_results.tsv` (1951) and `certificate_results_2141.tsv` (2141), both 2026-09-04:

| item | record said | output file says |
|---|---|---|
| 1951: generators with residual < 10⁻⁷ | 300 of 326 | **305 of 326** (largest residual 9.0×10⁻⁴) |
| 1951: generators with d ∈ ker χ (χ̄-branch coincides) | 70 (21.5%) | **76 (23.3%)** |
| 2141: same two counts | 333 below 10⁻⁷ (stated); ker χ not stated | 333 of 358 (largest 4.4×10⁻³); **73 (20.4%)** |
| scrambled controls | "on every generator tested (0.65–1.7)" — read by the statement draft as all generators | run on the **first 11 generators per conductor** (script guard `len(results) < 12`); values 0.47–1.81 (1951), 1.01–1.96 (2141) |
| floors | "every generator passes at the precision its truncation floor allows" | 1951: 257 generators measurement-limited (tail bound < residual), 69 floor-limited, **9 with tail bound > 1** (|c| ≥ 13N, both elliptic generators included — passes heuristic, not floor-limited). 2141: 284 / 74 / **10 with bound > 1** (|c| ≥ 13N); the two elliptic generators at 2141 (|c| = 5N) pass at 3×10⁻¹⁰, 8×10⁻¹⁰ against floors 6×10⁻⁷ |
| 34-digit pass | "every residual at or below its truncation floor" (first five rows) | of 11 rows complete on 2026-09-12, **7 exceed their computed tail** (factors up to 17: 1.85×10⁻²⁹ vs 1.1×10⁻³⁰); residuals 2.8×10⁻³¹–1.9×10⁻²⁹, tails 4.6×10⁻³¹–8.2×10⁻³⁰; the pass truncates at **M = 60,000** terms (not 10⁵). Reading: rounding accumulated over the sum at 34 digits; the residual, not the tail, is the measurement. |

None of these changes the record's verdict (all generators pass on the χ(d) branch; the χ̄ branch and the scrambles fail at O(1)); all of them change its numbers, and the deposit statement uses the output-file numbers. The assessor's 09-04 grade (B+ → A−) did not catch them; the referee read did.

Also from the referee read, affecting the statement rather than the 09-04 record: (i) the eigenvalue tables carry two non-construction entries per conductor — a_N (`twist-determined`, selected among μ₁₀ by twisted functional equations, 2026-08-06) and, at 2141 only, a₂ (`FE-resolved`); the tables were generated 2026-08-06 (provenance column upgraded 08-09); (ii) the selection record's ε₁₉₅₁ is six-decimal (+0.885096 − 0.465408i); the nine-digit figure circulating in later records is the negated Fricke constant of the 08-09 verification; (iii) "the model is named in each record's header" is false for several load-bearing records (RESULT_maass_live_20260809, decode2dim_RESULTS_20260803, decode2141_RESULTS_20260804, decode2dim_CRESPO_GRADE_20260804, E0ii sweep, AMENDMENT 1, RESULT_algebraic_closure_1951) — attribution of the arc rests on the 08-26 billing join; (iv) the corruption control "1.99" belongs to the dihedral-229 control with c₂ flipped, not to the icosahedral tables (whose bit-flip controls are 10–11 orders at prescreen and 0.341 for a₁₁₃ at 34 digits); (v) the d ∈ {11, 23} pairs passed at 1.406×10⁻³² and 3.136×10⁻³³, not "≤ 1.4×10⁻³²"; (vi) `heilbronn_coin.py` contains no LP (brute force at N ≤ 4); the LP is in `02_council_handshake/assessor_heilbronn_verify_20260904.py`; (vii) the assessor replication covered the 33-row system only — not the 228-row extension, not the real-s₀ doubling (both now covered by §1 instead); (viii) the kit scripts still load generators from a session scratchpad path and the CSV from an absolute path, and the 652 → 327 / 716 → 359 deduplication has no script (the referee re-did it; it checks out) — to fix at kit assembly.

## 3. Citation cards fetched 2026-09-12 (arXiv preprints and publishers' pages; quotations verbatim)

- **Doud–Moore**, "Even icosahedral Galois representations of prime conductor", arXiv math/0405534 (2004); *J. Number Theory* 118 (2006) 62–70. Abstract: "we use a series of targeted Hunter searches to prove that the minimal prime conductor of an even icosahedral Galois representation is 1951. In addition, we give a complete list of all even icosahedral Galois representations of prime conductor less than 10,000." §2: "A Galois representation is called odd if det(ρ(τ)) = −1; it is called even if det(ρ(τ)) = 1"; Tate's theorem: "there is a Galois representation ρ: G_Q → GL₂(C) such that ρ̃ = π ∘ ρ ... In particular, ρ can be chosen to be ramified only at those primes at which ρ̃ is ramified." Table 1: six representations; the 1951 and 2141 quintics as in the statement. They presume neither I nor −I: the sign is not a projective datum.
- **Booker 2003**, "Poles of Artin L-functions and the strong Artin conjecture", *Ann. of Math.* (2) 158 (2003) 1089–1098: a non-automorphic irreducible 2-dim Artin representation over Q has infinitely many poles; Artin ⇒ strong Artin for one representation.
- **Booker 2006**, "Artin's conjecture, Turing's method, and the Riemann hypothesis", arXiv math/0507502; *Experiment. Math.* 15 (2006) 385–407. §2: "SL₂(F₅) has irreducible representations of dimensions 1, 2, 2, 3, 3, 4, 4, 5 and 6, and it is the smallest group supporting an icosahedral representation (since A₅ has no 2-dimensional representations), meaning that our criterion unfortunately does not apply to checking the icosahedral case." "One easily checks that for ρ the 6-dimensional representation, (2.7) fails with χ₁ corresponding to any of the vectors (0, −1, 0, 0, 0, 0, 0, 0, 1), (0, 0, −1, 0, 0, 0, 0, 0, 1) and (0, 0, 0, 0, 0, 0, −1, 0, 1), i.e. the representations of dimension 2 and one of dimension 4 can hide a pole at a zero of L(s, ρ)." "A result of Flicker [Fli94] implies that modularity of ρ is equivalent to that of Ad(ρ)..." "Unfortunately, there is the more practical problem that totally real A₅ fields (those that give rise to even icosahedral representations) are very rare; the smallest known discriminant is far too large to test with current computers." — the qualitative precedent for §3(d) of the statement, and the "why they stopped."
- **Booker–Lee–Strömbergsson**, "Twist-minimal trace formulas and the Selberg eigenvalue conjecture", arXiv:1803.06016; *J. London Math. Soc.* (2) 102 (2020) 1067–1134. Theorem 1.1: "The Selberg eigenvalue conjecture is true for Γ₁(N) for N ≤ 880, and for Γ(N) for N ≤ 226." Theorem 1.2: "Assuming Artin's conjecture, Table 1 is the complete list, up to twist, of even, nondihedral, irreducible, 2-dimensional Artin representations of conductor ≤ 2862." Remarks 1.3: "The existence of this representation was first shown by Doud and Moore [DM06], who also proved that 1951 is minimal among prime conductors of even icosahedral representations." "the first even icosahedral representation occurs at conductor N = 1951, so the bounds in Theorem 1.1 cannot be improved unconditionally beyond 1950."
- **Seymour-Howell**, "Rigorous computation of Maass cusp forms of squarefree level", *Res. Number Theory* 8 (2022) art. 83: squarefree level 2 ≤ N ≤ 105, trivial character; no eigenvalue-¼, Artin or icosahedral content.
- **Gun–Hazra–Sahu**, "On holomorphy and non-vanishing of Artin L-functions", *Monatsh. Math.* 206 (2025) 853–883: solvable extensions only; cites Foote–Wales (1990) as "orders ≤ 2 imply holomorphy for solvable extensions".
- **Ginsberg**, "Unfaithful minimal Heilbronn characters of L₂(q)", *Proc. Edinb. Math. Soc.* 56 (2013) 57–69 (abstract read: minimal Heilbronn characters unfaithful on a Sylow p-subgroup force G quasi-simple, p odd, P cyclic, ... or G/Z(G) ≅ L₂(q), q an odd prime with p | q − 1; the exceptional case constructed explicitly). **Ginsberg**, "Unfaithful minimal Heilbronn characters of finite groups", *J. Algebra* 331 (2011) 466–481 (title only). **Foote–Ginsberg–Murty**, "Heilbronn characters", *Bull. Amer. Math. Soc.* 52 (2015) 465–496 (survey; not readable through the session's fetch tool — AMS 403). These define and study the abstract object our cone computes; whether the SL₂(F₅) configurations appear in them is **not determined**. Flagged as the likeliest precedent for §3(d).
- **Foote**, "Non-monomial characters and Artin's conjecture", *Trans. Amer. Math. Soc.* 321 (1990) 261–272: **unreadable in-session (AMS 403; no abstract located)** — status unchanged from the 09-04 handshake ("unchecked"). The pre-compaction summary of this session recorded it as carrying a solvability hypothesis; that recollection is not evidenced by any record and is withdrawn to "unchecked."
- Not reached: Booker–Strömbergsson 2007 (De Gruyter 405); Cimpoeaș arXiv:2409.05629 (cited from the 09-04 handshake, which read it).

## 4. Standing

The deposit statement v2 incorporates §§1–3. Open: Foote 1990 and the Heilbronn-character survey (human/library task; would settle the §3(d) precedent question); the kit-assembly fixes of §2(viii); completion of the 34-digit pass (running, 11/24). The 09-04 record is not edited in place (per the archive's practice); this record is its erratum.

## 5. Appendix — the referee report, verbatim (adversarial-read subagent, claude-fable-5-1, 2026-09-12)

(Findings 1–17 and the PASSED list as returned; the orchestrator's dispositions are in §§1–2 and in the statement.)

1. §3(a) "phase-scrambled controls fail at O(1) on every generator" — run on 11 generators per conductor (script guard; TSV has 11 `scrambled=` entries each; 0.47–1.81 / 1.01–1.96). Fix applied.
2. §3(a) 34-digit pass "every residual ... at or below its truncation floor" — 5 of 9 rows exceed `tail_over_scale` (up to 17×); M = 60,000; "completed file in the kit" false. Fix applied.
3. §2(i)/§4 tables "exact objects produced by the stated construction" — a_N `twist-determined`, 2141's a₂ `FE-resolved`; generated 2026-08-06. Fix applied.
4. §3(d) Foote 1990 "solvability hypothesis" — unsupported; records say unchecked. Fix applied.
5. No dated record of a 2026-09-12 literature check; Booker/BLS quotations verified verbatim by the referee against the preprints; BLS "≤ 2862" is Theorem 1.2. This record is the fix.
6. ε₁₉₅₁ nine digits attributed to the selection — selection record has six; nine-digit figure is the negated 08-09 Fricke constant. Fix applied.
7. "model is named in each record's header" — false for seven named records. Fix applied.
8. "independent LP" — language rule; replication scope = 33-row system only; no deposited 228-row script. Fix applied (and §1 supersedes the LP).
9. 300/70 (21.5%) vs output 305/76 (23.3%); 2141: 333, 73 (20.4%). Recomputed by the orchestrator, confirmed; fix applied.
10. "first" appears thrice outside quotation. Rephrased.
11. Root number +1 "[tp flagged]" in the 09-04 record; archive anchor is the 07-26 ε-Ledger record (Deligne Thm 1.5; Fröhlich–Queyrut Thm 3). Cited.
12. Exact dual certificate for the 4m bound (the identity of §1); real-s₀ doubling via sector masses. Verified, adopted.
13. K̃ undefined; SL₂(F₅) vs SL₂(F₅)×C₅ conflated; Booker's ρ is his 6-dim. Fixed.
14. "1.99" is the dihedral-229 corruption control; icosahedral bit-flips 10–11 orders / 0.341. Fixed.
15. d ∈ {11, 23}: 1.406×10⁻³² and 3.136×10⁻³³. Fixed.
16. §6 reproducibility: scratchpad/absolute paths; no dedup script; `heilbronn_coin.py` has no LP. Fixed in text; kit-assembly items queued.
17. Minor: order-10 twist (quadratic part χ₋₁₉₅₁/χ₋₂₄); Fricke–entirety equivalence is on the imaginary axis; dihedral = Hecke/Maass; elliptic-generator floors > 1 at 1951 (at 2141 the elliptic generators are at |c| = 5N and fine — orchestrator's correction to the referee's "all four"); Booker's observation concerned the monomial cone. All applied.

PASSED (referee): 327 = T+324+2; 359 = T+356+2; 1.311/1.120×10⁻²⁴, 18/15/3 dropped, 1.90, 1.05×10⁻²⁶, 1.3/1.9×10⁻²⁶; 1.3×10⁻³⁹, 5.7×10⁻¹²; 65/65; 221/231; χ₋₁₉₅₁/χ₋₂₄; 2⁻⁵³ and 2¹ both conductors; both L(1, Ad) strings to all printed digits; 0.460602/0.46120/0.429079/0.42897; 33 rows (32+1), 76 subgroups, 12 classes, 228 rows, three configurations, 2 without the tetrahedral row; a_N = ζ₁₀², ζ₁₀⁸; 9,591 unramified; χ pins; records E0ii 07-27, PROVENANCE 08-29, decode 08-03/08-04, AMENDMENT 1, CRESPO 08-04, EXACT 08-09, all 09-04 records, countersign convention 08-26 exist and match; countersign line blank; mathematics (a)–(j) of the brief all correct by the referee's own derivations (76 subgroups/12 classes by hand; |G| = 600; conductor-N lifts ρ, ρ⊗χ̄ ≅ ρ̄).
