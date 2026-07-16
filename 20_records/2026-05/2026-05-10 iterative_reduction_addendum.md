# Addendum to `iterative_reduction_and_primes.md`

**Date:** May 10, 2026
**Status:** Literature accounting update; no new mathematical content.

---

## Literature placement

The note's "open directions worth pursuing" — divisor-respecting Schur reduction, with the conjecture that integrating out specific node subsets reveals sub-chain Galois structure — is closed by the existing **isospectral graph reduction** theory of Bunimovich and Webb:

- L. A. Bunimovich and B. Z. Webb, *Isospectral graph reductions*, arXiv:0909.0053 (2009).
- L. A. Bunimovich and B. Z. Webb, *Isospectral graph reductions and improved estimates of matrices' spectra*, Linear Algebra Appl. 437 (2012), 1429–1457.
- L. A. Bunimovich and B. Z. Webb, *Isospectral transformations: A new approach to analyzing multidimensional systems and networks*, Springer Monographs in Mathematics, Springer-Verlag (2014).

Bunimovich-Webb's construction is precisely Schur reduction over the ring of complex rational functions in a spectral parameter $\lambda$, applied to a finite weighted digraph. They prove:

1. The reduction preserves the spectrum of the weighted adjacency matrix up to a known set of eigenvalues determined by the structural-set complement.
2. Sequential reductions commute: $\mathcal R(G; S_1, \ldots, S_m)$ is independent of the order of reductions when the sequences induce valid reductions ending at the same final set.
3. Eigenvectors of the original matrix are recoverable from eigenvectors of the reduction (Duarte-Torres, arXiv:1412.7130, 2015).

Applied to path graphs $P_N$ over a chosen vertex subset, this theory gives the rational eigenvalue tracks I worked out explicitly for $N=5, 7$ as direct corollaries. The cyclotomic-divisor structure of $U_N(y) = \prod_{d | N+1, d > 1} \psi_d(2y)$ is standard algebraic number theory (cyclotomic factorization of Chebyshev polynomials of the second kind), and the framework note already correctly identified this.

For circulant graphs $C_n$, the analogous prime/composite Galois-orbit phenomenon is examined explicitly in:

- arXiv:2505.00730 (April 2025), illustrating the single-orbit prime case ($n=97$) versus multiple-orbital composite case ($n=90$).
- M. Lanzano and G. Russo, *Splitting fields of spectra of circulant graphs*, Journal of Algebra (2021), establishing the inverse Galois problem for circulant graphs.

## What the framework note's "open direction" should now read

The original note ended with: *"If this thread continues, the natural next step is **divisor-respecting Schur reduction**. ... If the framework's claim about 'matching polynomial of the coupling graph' being the canonical structural law is correct, then the divisor-respecting reduction should reproduce the matching polynomial decomposition explicitly..."*

The corrected reading: **divisor-respecting Schur reduction is the Bunimovich-Webb isospectral reduction restricted to vertex subsets that respect the cyclotomic-orbit decomposition of $U_N$**. This is not a conjecture — it follows from the existing theory. What the framework adds is the specific *interpretation* of the rational eigenvalue tracks (each track corresponding to one Galois orbit, with the track's residue structure encoding the cyclotomic factor) as the explicit content of the framework's "metallic-mean spectrum" / "matching polynomial of the coupling graph" claim.

The framework's contribution at this junction is interpretive, not theorematic: it identifies the algebraic-number-theoretic content of path-graph spectra as the substrate of the chain-physics ortholinear hierarchy. This is consistent with — and arguably implied by — the Bunimovich-Webb theory; the framework's job is to articulate why this matters physically and to connect it to the broader corpus.

## Worked-example status

The explicit calculations for $N=5, 7$ in the present session demonstrate the theory's content for the path-graph chain. Specifically:

**$N=5$, Schur on nodes $\{2,4\}$:**
$$M_{\text{eff}}(D) = \begin{pmatrix} D - 1/D & -1/D & 0 \\ -1/D & D - 2/D & -1/D \\ 0 & -1/D & D - 1/D \end{pmatrix}$$

K-eigenvalue tracks: $\{0,\, 1/D,\, 3/D\}$, with resonances at $D=0$, $D^2=1$, $D^2=3$ — corresponding term-by-term to the $\mathbb Q$-irreducible factors of $U_5(y) = 2y(2y-1)(2y+1)(4y^2-3)$.

**$N=7$, Schur on nodes $\{1,3,5,7\}$:**

K-eigenvalue tracks: $\{0,\, (2-\sqrt 2)/D,\, 2/D,\, (2+\sqrt 2)/D\}$, with resonances at $D=0$, $D^2 \in \{2-\sqrt 2,\, 2,\, 2+\sqrt 2\}$ — corresponding to the factors of $U_7(y) = 8y(2y^2-1)(8y^4-8y^2+1)$.

These should be cited in the chain-physics writeup as worked examples illustrating the Bunimovich-Webb framework, not as new theorems.

## Implications for the corpus

The conjectures in the original note's "Conjectural / not yet verified" section are now closed:

- *"The boost law admits partial reductions at composite N+1 corresponding to the divisor structure"* — closed by Bunimovich-Webb commutativity of reductions, refined by the cyclotomic-orbit interpretation.
- *"The iterative Schur reduction 'respects divisor structure' in a precise sense"* — closed in the same way.

The framework's higher-level claim — that "the framework's structural geometry is exactly the algebraic-number-theoretic content of the underlying graph, expressed in the language of canonical hyperbolic budgets" — remains an interpretive claim that goes beyond Bunimovich-Webb. Bunimovich-Webb tells you what the spectrum does under reduction; the framework adds the assertion that this is the *physical content* of chain dynamics in the ortholinear ontology. That assertion is not directly testable by Bunimovich-Webb alone; it requires the framework's own structural identifications (S†S budget, x²+u=1 identity, etc.) to give it content.

So the chain-physics thread of the corpus stands on:
- **Standard:** Bunimovich-Webb isospectral reduction; cyclotomic factorization of $U_N$.
- **Framework's contribution:** identification of the rational eigenvalue tracks as the content of the metallic-mean spectrum and matching-polynomial-of-coupling-graph claim, situated within the broader passive-scattering / Schur / DtN apparatus.

This is honest scoping. The framework's interpretive layer is the contribution; the underlying spectral mathematics is well-developed and should be cited as such.
