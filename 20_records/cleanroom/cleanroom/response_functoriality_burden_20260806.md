# Response to the five-deliverable functoriality challenge

*Drafted 2026-08-06. Answers only from work already completed and recorded; no new claims.*

Your five deliverables are well-posed, and I want to start by agreeing with the load-bearing one rather than negotiating around it.

**Step 3 is conceded, without qualification.** We claim no functorial transfer, we have no candidate ladder, and we agree with your table: base change and automorphic induction need solvability, symmetric powers run the wrong way, Jacquet–Langlands preserves Galois type, and icosahedral parameters are not endoscopic. There is no theorem of the form you specify, we do not possess one, and nothing in our work supplies one. If the question is "has someone proved automorphy for an even icosahedral representation by functoriality," the answer is no.

What follows is therefore not a rebuttal. It is a clarification of what kind of object we are claiming, because your list — correctly, for its target — collapses two claims that are separable, and only one of them is conditional.

## The two claims, separated

**Claim A (Galois side): the Frobenius traces of ρ are explicitly computable, and we have computed them.** For a fixed even icosahedral ρ, the quantities a_p = tr ρ(Frob_p) are determined by ρ alone. Their existence and computability do not depend on automorphy, on functoriality, or on Artin's conjecture. This is an algebraic claim about a group representation attached to an explicit number field.

**Claim B (analytic side): L(s, ρ) appears to be entire and to satisfy its functional equation.** This we support with numerical evidence only, and we price it as such.

Artin's conjecture asserts, among other things, that Claim A's list coincides with the Hecke eigenvalue list of an automorphic form. That coincidence is exactly what remains unproven, and we do not assert it. What we assert is that one of the two lists now exists explicitly, and the other's existence has strong numerical evidence — with the two claims kept apart in every record.

## The deliverables, answered as they apply

**1 (source must exist unconditionally).** We have no automorphic source and claim none. Our source is a Galois representation, exhibited unconditionally by an explicit polynomial: Doud's x⁵ − x⁴ − 780x³ − 1795x² + 3106x + 344 (conductor 1951, the proven minimum) and x⁵ − x⁴ − 856x³ + 4025x² + 28501x − 40877 (conductor 2141). Both are totally real quintics with Galois group A₅ and discriminant p⁴, verified directly. Nothing hypothetical enters at this step, precisely because nothing automorphic does.

**2 (explicit L-homomorphism, correct conjugacy class, conductor).** No L-homomorphism is claimed, and I want to be unambiguous about that: our framework supplies a method for reading an L-function's boundary constraints, not a map of L-groups and not a transfer. Calling it a functor in your sense would be precisely the overclaim your list is designed to catch. But your parenthetical here contains an error that matters, and it is the one place where our completed work has something concrete to offer your list.

You write that for an even representation, complex conjugation must have eigenvalues (+1, +1), not (+1, −1). The exclusion of (+1, −1) is right — that is exactly what "even" means, det ρ(c) = +1. But it does not follow that ρ(c) = +I. An involution in GL₂(ℂ) with determinant +1 is **±I**, and both signs are even. The two cases give genuinely different archimedean parameters: Γ_ℝ(s)² for +I (cos-type Maass form) versus Γ_ℝ(s+1)² for −I (sin-type), both at λ = 1/4. So an even icosahedral representation may perfectly well have ρ(c) = −I, and any transfer specification that hard-codes (+1, +1) will impose the wrong parameter at infinity in that case.

This is not a hypothetical concern. It is a bit that the symmetric square cannot see — Sym²(±I) = I identically — and so it is invisible to every certificate that works through the 3-dimensional shadow. We treated it as an unknown, ran both archimedean hypotheses as competing cells, and measured it: for both fields the sin-type cell (ρ(c) = −I) satisfies the functional equation at the instrument's floor while the cos-type cell fails by eleven orders. Independently, on the algebraic side, the trace-form construction produces a cos-type lift by identity, and the character connecting it to the minimal-conductor object is odd in both cases — the same conclusion by a different route. Conductor was not assumed either: a blind scan over conductors selects exactly 1951 and exactly 2141, with ±5% neighbours failing by thirteen orders.

**3 (transfer as theorem).** Conceded above. Our route never transfers anything. We work with the Galois object's L-function directly and test its analytic properties; there is no automorphic representation in the pipeline to transfer from.

**4 (local–global compatibility).** At unramified p, the Satake parameters of the object we test are by construction the eigenvalues of ρ(Frob_p) — that is input, not output, so it is not evidence of compatibility; it is the definition of what was tested. At ramified p, the local conductor exponent is derived (tame, e = 5, minimal lift with a fixed line, exponent 1) and cross-checked by the blind conductor scan, which lands on exactly 1951 and exactly 2141. On the ε-factor: it was measured as a free unimodular phase and then checked against exact Gauss-sum arithmetic that never entered the computation — ε·√p/τ(χ) lands on μ₁₀ to 2.6×10⁻¹⁰ (1951) and 7.2×10⁻¹⁶ (2141), with the rival convention off by many orders. That is a local ε-factor test passed against exact algebra external to the pipeline.

At infinity, your challenge is the sharpest one on the list, and it deserves a direct answer rather than a concession. **λ = 1/4 is measured, not assumed.** For a Maass form of spectral parameter r (λ = 1/4 + r²) the archimedean factor is Γ_ℝ(s+1+ir)Γ_ℝ(s+1−ir), whose inverse Mellin kernel is 4y·K_{ir}(2y). We scanned r with everything else held at values that are not ours to tune: the coefficients are fixed by the Galois representation and independently confirmed by the trace-form construction, and N is the Artin conductor derived from the field rather than a fitted parameter. r is therefore the sole free quantity in the test. The residual is exactly linear in r over five decades — slope 8.5×10⁻⁵ (1951), 6.7×10⁻⁵ (2141) — and reaches the instrument's floor only at r = 0:

    r = 0      λ = 0.250000000    residual 7.4e-15  |  3.5e-15
    r = 1e-4   λ = 0.250000010    residual 8.5e-09  |  6.7e-09
    r = 1e-2   λ = 0.250100000    residual 8.5e-05  |  6.7e-05
    r = 1e-1   λ = 0.260000000    residual 8.5e-03  |  6.7e-03

Resolution is floor divided by slope: |r| < 8.7×10⁻¹¹, hence **|λ − 1/4| < 7.6×10⁻²¹** at 1951 and < 2.7×10⁻²¹ at 2141. Your stated bar — error bounds tight enough to exclude 0.2501 — is cleared by ten orders. Weight zero is likewise not tuned: even representations correspond to Maass forms and odd ones to holomorphic weight-1 forms, so weight 0 follows from the measured parity rather than being selected.

Two honest limits on this. The scan varies r with the decoded bits fixed; a joint (r, bits) scan was not run, though bit-flips are discrete and cost ≳10⁻² at the visible set while the r-response is smooth at 10⁻⁵·r, so the scales cannot compensate in the small-r regime. And your deeper point stands as stated: no numerical measurement can exclude λ = 1/4 + 10⁻¹⁰⁰. The exclusion is a quantitative bound, not a proof of exactness.

**5 (exact extraction of Hecke eigenvalues).** This one we have, though by algebraic rather than automorphic means, so I will state exactly what it is and let you judge whether it meets the spirit of your requirement.

There is a finite, exact, numerics-free algorithm for a_p, valid for every unramified p: factor the defining quintic modulo p to obtain the projective class of Frob_p; determine the spin lift class by testing whether the trace-form solution element γ = det(I + U) — where U is the orthogonal Galois trivializer built from a rational isometry of the trace form, computed once per field — is a square in 𝔽_{p^m}; combine the two to get tr ρ(Frob_p) exactly, in ℚ(ζ₅, √5). No L-function, no automorphic input, no numerical approximation. This is a classical construction in the Serre/Crespo embedding-problem tradition, not an invention of ours.

We ran it, and it agrees with our independently decoded values at 65 of 65 comparable primes per field, modulo exactly one global quadratic character each — which is the expected twist-family freedom of the construction, and each character is uniquely determined among roughly 24,000 fundamental discriminant candidates. Two internal validations worth stating because they are answer-free: γ is a non-square at every one of 221 (respectively 231) involution-class primes, which is the unique-involution signature of SL₂(𝔽₅) and could not survive a wrong γ; and feeding the constructed values through the functional-equation instrument reproduces the decoded residuals to the last digit while resolving the handful of primes outside the construction's reach to the decoded values.

One honest caveat on this step: our implementation of γ was written from the recalled structure of the classical construction rather than from a fetched statement of the theorem, so its correctness in our hands is established by the measurements just described rather than by a citation. Pinning the reference is an open item on our list.

## What we are actually claiming, priced

Two even icosahedral representations now have explicit Frobenius-trace data, produced by two independent methods that agree, one of them a finite exact algorithm requiring no automorphy. That is a statement about Galois representations. Separately, the associated L-functions satisfy their conjectured functional equations and show no poles across the tested region at 10⁻¹⁵ precision, with blind conductor selection and every corruption failing by nine to thirteen orders — evidence for automorphy, not proof of it. Artin's conjecture for these representations remains exactly as open as it was.

Where this bears on your challenge: if someone eventually proves the transfer theorem in your step 3, its output is not free. It must reproduce these numbers. A published, checksummed list of exact traces is a falsifiable target for any future proof, and it is also a target for anyone who prefers to refute us — the construction is elementary enough to be rerun independently in an afternoon.

The one thing I would press back on in the framing: "decisive identification of the Hecke eigenvalues" is only unmeetable-by-construction if the eigenvalues are defined as belonging to an automorphic form whose existence is the open question. Defined on the Galois side, they are computable today, and the interesting question becomes what evidence exists that the two definitions agree. On that question we offer measurements rather than a theorem, and we label them as such throughout.

## On whether invoking the conductor presupposes the conjecture

One anticipated objection deserves answering directly, because it sounds decisive and is not: that testing at the Artin conductor smuggles in Artin's conjecture.

It does not, and the reason is a matter of what each object is. The Artin conductor is a **local algebraic invariant**, defined in 1930 from the higher ramification filtration acting on V — a finite computation from the number field, requiring no L-function and no automorphy. Separately, the **functional equation itself is a theorem, not a conjecture**: by Brauer induction every character is a ℤ-combination of characters induced from one-dimensional characters of subgroups, so L(s, ρ) is a ratio of products of Hecke L-functions, and therefore has meromorphic continuation and satisfies Λ(s, ρ) = ε(ρ)·Λ(1−s, ρ̄) with the Artin conductor in the completed factor and the Artin root number as ε. What Artin conjectured, and what remains open, is a **third and separate statement: that L(s, ρ) is entire** — no poles.

So the structure of our test is: conductor from ramification theory (theorem), functional equation with that conductor (theorem, Brauer 1947), and then a numerical probe of the one thing that is actually open — whether poles are present. A pole would have shown up: our keyed pole controls deflect the same instrument by thirteen orders. Nothing conjectural is assumed; the conjectural part is what is being measured.

And the conductor is doubly determined in any case. It is derived — Tate's lifting theorem for existence, local tame arithmetic for the exponent — and then **blind-scanned**, with the residual minimum landing at exactly 1951 and exactly 2141 while ±5% neighbours fail by thirteen orders. Had we fitted the conductor to make the equation work, the objection would have teeth. We computed it from the field, then measured it independently, and the two agree.

## Summary against your list

Step 1: satisfied trivially, because our source is a polynomial rather than an automorphic object — nothing conditional enters. Step 2: no L-homomorphism claimed; the conductor is selected blind at the proven minimum, and your (+1, +1) specification needs the correction above. **Step 3: conceded outright — no transfer theorem, none claimed, and we agree none exists.** Step 4: unramified compatibility is definitional rather than evidential; ramified structure is derived and its ε-factor checked against exact Gauss sums; the archimedean parameter is measured to |λ − 1/4| < 10⁻²⁰, and weight zero follows from parity theory. Step 5: satisfied in substance by a finite exact algorithm, though by algebraic rather than automorphic means, with the citation pin open.

Four of your five are met or not-applicable-by-design. The fifth is the one that matters most, and it is missing, and we say so first rather than last. What we would ask a skeptical reader to take from that is not that automorphy has been established, but that a specific, checkable, previously-empty list of numbers now exists for the objects in question — produced by two independent routes that agree, one of them rerunnable in an afternoon by anyone who would like to prove us wrong.
