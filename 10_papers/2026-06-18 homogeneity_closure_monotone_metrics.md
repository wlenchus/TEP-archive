# A homogeneity closure for monotone metrics under the spectral peel

**Abstract.** Let $\rho$ be a faithful density operator with non-degenerate spectrum, and let the *peel* be the operation that deletes the dominant eigenvalue and renormalizes the remainder. Acting on the flag (eigenbasis) fiber, the peel raises two structural questions for the family of monotone (Petz) metrics: does it preserve the fiber geometry, and does it act on the family of metrics? We show both are immediate consequences of a single elementary fact — the degree $-1$ homogeneity of the Morozova–Chentsov weight. The peel is a constant homothety composed with restriction to a totally-geodesic subflag (Proposition A), hence preserves the Levi-Civita connection, the curvature operator, and the holonomy of the residual fiber exactly, scaling sectional curvature by the renormalization scalar; and it induces a bijection of the operator-monotone family onto itself (Proposition B). The load-bearing algebra is machine-verified; the scope is the non-degenerate stratum; the one step requiring a standard external citation (the invariant-connection / totally-geodesic criterion at general dimension) is flagged explicitly.

---

## 1. Setup

Let $\rho$ be a faithful density operator on $\mathbb{C}^d$ with spectrum
$\lambda = (\lambda_1 > \lambda_2 > \cdots > \lambda_d > 0)$, $\sum_i \lambda_i = 1$, and **distinct** eigenvalues — the *generic stratum*, where the eigenbasis flag is smooth (the degenerate locus is treated in §5). The manifold of such states factors locally as

$$
\underbrace{\Delta_{d-1}}_{\text{eigenvalue simplex}} \;\times\; \underbrace{M = U(d)/T}_{\text{flag fiber}}, \qquad T = U(1)^d .
$$

**Monotone metrics.** The Riemannian metrics on density operators contracted under all completely-positive trace-preserving (CPTP) maps are classified by Petz [P96]: they form a family indexed by operator-monotone functions $f:\mathbb{R}_{>0}\to\mathbb{R}_{>0}$ with $f(1)=1$ and the symmetry $f(t)=t\,f(1/t)$. The associated **Morozova–Chentsov weight** [MC, P96] is

$$
c_f(a,b) \;=\; \frac{1}{\,b\,f(a/b)\,}.
$$

In flag coordinates $\theta_{ij}$ (the eigenbasis-rotation angles), the off-diagonal mode $(i,j)$ carries $d\rho_{ij} = (\lambda_i - \lambda_j)\,d\theta_{ij}$, so at fixed spectrum the fiber metric is

$$
g_\lambda \;=\; \sum_{i<j} w_f(\lambda)_{ij}\,\lvert d\theta_{ij}\rvert^2, \qquad w_f(\lambda)_{ij} \;=\; (\lambda_i-\lambda_j)^2\, c_f(\lambda_i,\lambda_j).
$$

$g_\lambda$ is a **$U(d)$-invariant** metric on the flag $M=U(d)/T$: one positive weight $w_f(\lambda)_{ij}$ per complex root space $\mathfrak{m}_{ij}$, with distinct root spaces $g_\lambda$-orthogonal. The reductive complement of $\mathfrak{t}=\mathrm{Lie}(T)$ in $\mathfrak{u}(d)$ is $\mathfrak{m}=\bigoplus_{i<j}\mathfrak{m}_{ij}$, the tangent space at the base point.

**The peel.** Delete the dominant eigenvalue and renormalize:

$$
P(\lambda) = (\lambda_2,\dots,\lambda_d)/u, \qquad u := \sum_{i\ge 2}\lambda_i = 1-\lambda_1 \in (0,1).
$$

On the fiber, $P$ sheds the dominant-attached modes $\mathfrak{m}_{1j}$ and acts on the **residual subflag** $M' = U(d-1)/T'$ ($T'=U(1)^{d-1}$ on indices $2,\dots,d$), embedded in $M$ through the base point with tangent decomposition

$$
\mathfrak{m}' = \bigoplus_{2\le i<j\le d}\mathfrak{m}_{ij} \ \ (\text{residual}), \qquad
\mathfrak{m}'^{\perp} = \bigoplus_{j\ge 2}\mathfrak{m}_{1j} \ \ (\text{shed}).
$$

**The peel is post-selection, not a coarse-graining.** $P$ conditions on *not* being the dominant outcome: $\Phi(\rho) = \Pi\rho\Pi/\operatorname{Tr}(\Pi\rho\Pi)$ with $\Pi$ the residual projector. This map is *not* trace-preserving, so the data-processing inequality (monotone metrics contract under CPTP maps) does **not** apply to it. On tangent vectors, $\Phi$ annihilates the shed modes ($\Pi X \Pi = 0$) and **inflates** each residual mode by $1/u$:

$$
\Phi_* X = X/u, \qquad g_f(\Phi\rho)(\Phi_*X,\Phi_*X) = \tfrac{1}{u}\, g_f(\rho)(X,X),
$$

verified to machine precision for all $f$ and all spectra (§6). The scalar $u=1-\lambda_1$ is exactly the post-selection probability $P(\text{not-dominant})$, so the per-rung inflation $1/u$ is a post-selection weight, **not** a contraction. The statements below are algebraic facts about this restriction–renormalization and must not be read as data-processing statements.

---

## 2. The single mechanism: weight homogeneity

> **Lemma (homogeneity).** For every operator-monotone $f$, the weight $c_f$ is homogeneous of degree $-1$ and $w_f$ of degree $+1$ in the spectrum:
> $$ c_f(\sigma a,\sigma b) = \sigma^{-1} c_f(a,b), \qquad w_f(\sigma\lambda)_{ij} = \sigma\, w_f(\lambda)_{ij}, \qquad \forall\,\sigma>0. $$

*Proof.* Using only $f(\sigma a/\sigma b)=f(a/b)$,
$$
c_f(\sigma a,\sigma b) = \frac{1}{\sigma b\, f(\sigma a/\sigma b)} = \frac{1}{\sigma b\, f(a/b)} = \sigma^{-1} c_f(a,b),
$$
$$
w_f(\sigma\lambda)_{ij} = (\sigma\lambda_i-\sigma\lambda_j)^2 c_f(\sigma\lambda_i,\sigma\lambda_j) = \sigma^2(\lambda_i-\lambda_j)^2\cdot\sigma^{-1}c_f(\lambda_i,\lambda_j) = \sigma\, w_f(\lambda)_{ij}. \qquad\square
$$

This is the only non-trivial input. Both propositions below are corollaries, taken with $\sigma = 1/u$ (the peel's renormalization). Confirmed symbolically for a fully symbolic $f$: $w_f(\lambda)_{ij} - u\,w_f(\lambda/u)_{ij} = 0$, i.e. for the whole family at once (§6).

---

## 3. Proposition A — fiber isometry-up-to-scale

> **Proposition A.** On the generic stratum, the peel $P$, acting on the fiber, equals a constant homothety by $u$ composed with restriction to a totally-geodesic submanifold. Consequently $P$ preserves the Levi-Civita connection, the $(1,3)$ curvature operator entrywise, and the holonomy of the residual fiber exactly (all loops), and scales the sectional curvature by $u$; and this holds for **every** operator-monotone $f$ and every $d$.

The peel on the fiber factors as $P = (\text{homothety by } u) \circ (\text{restriction to } M')$. We treat each factor.

**Lemma A1 (homothety).** By the Lemma with $\sigma = 1/u$,
$$
w_f(\lambda)_{ij} = u\, w_f(\lambda/u)_{ij} \qquad \text{for all residual } (i,j),
$$
so the $d$-flag metric **restricted to the residual modes** equals $u$ times the intrinsic $(d-1)$-flag metric for the *same* $f$ — a constant rescaling, since $u=1-\lambda_1$ depends only on the spectrum, not on the fiber point. A constant homothety $g\mapsto c\,g$ leaves the Christoffel symbols invariant,
$$
\Gamma^k_{ij} = \tfrac12 g^{kl}\!\left(\partial_i g_{jl}+\partial_j g_{il}-\partial_l g_{ij}\right),
$$
because each factor of $g$ carries $c$ and each factor of $g^{-1}$ carries $c^{-1}$. Hence the same connection $\nabla$, the same parallel transport and holonomy, and the same $(1,3)$ curvature operator $R^k{}_{lij}$; the sectional curvature $K$, carrying one factor of $c$ upstairs and two in the area form, scales by $1/c$. With $c=1/u$ this gives the stated $u$-scaling of $K$ and exact invariance of connection, curvature operator, and holonomy. *(Machine-verified: $\Gamma(cg)=\Gamma(g)$ identically; $K(cg)=K(g)/c$, checked non-vacuously on the constant-curvature plane, §6.)*

**Lemma A2 (totally geodesic).** The residual subflag $M'=U(d-1)/T'$, embedded in $M=U(d)/T$ through the base point, is **totally geodesic**: its second fundamental form vanishes, $\mathrm{II}\equiv 0$. For a $U(d)$-invariant metric this is the standard invariant-submanifold criterion — $M'$ is the fixed-point set of an isometric involution of $(M,g_\lambda)$ (conjugation by the diagonal unitary $\operatorname{diag}(-1,1,\dots,1)$, which fixes $\mathfrak{m}'$ and reverses $\mathfrak{m}'^\perp$), and fixed-point sets of isometries are totally geodesic [KN, Ch. XI]. Equivalently, the relevant Lie-bracket projections vanish: $\langle [\mathfrak{m}',\mathfrak{m}']_{\mathfrak m},\,\mathfrak{m}'^\perp\rangle = 0$ and $\langle [\mathfrak{m}'^\perp,\mathfrak{m}']_{\mathfrak m},\,\mathfrak{m}'\rangle = 0$. *(These bracket conditions are verified to machine precision at $d=3,4,5$, §6; the general-$d$ statement is exactly the place a formal write-up invokes the criterion above rather than re-verifying.)*

**Composition.** $P\big|_{\text{fiber}} = (\text{homothety by } u)\circ(\text{totally-geodesic restriction})$. Restriction to a totally-geodesic submanifold preserves the induced Levi-Civita connection and curvature operator (the submanifold's intrinsic and ambient connections agree when $\mathrm{II}=0$); the subsequent constant homothety preserves them too (A1) and scales $K$ by $u$. Hence the connection, $(1,3)$ curvature operator, and holonomy of the residual fiber are preserved exactly, sectional curvature scaled by $u$, for every $f$ and every $d$. $\qquad\square$

---

## 4. Proposition B — family automorphism

> **Proposition B.** On the generic stratum, the peel induces a bijection of the entire operator-monotone family onto itself: the metric label is preserved, $f \mapsto f$.

**Lemma B1 (label preservation).** By A1 the residual fiber metric is, up to the constant scale $u$, the $(d-1)$-flag metric built from the **same** weight $w_f$ — hence the **same** operator-monotone $f$. The peel does not move the label.

**Lemma B2 (recovery).** $f$ is recovered from a single weight. Setting $\lambda_j=1$,
$$
w_f(t,1) = (t-1)^2\, c_f(t,1) = \frac{(t-1)^2}{f(t)} \quad\Longrightarrow\quad f(t) = \frac{(t-1)^2}{w_f(t,1)}.
$$
*(Machine-verified, §6.)* Across all spectra the residual realizes every ratio $t = \lambda_i/\lambda_j$, so the **entire** function $f$ is determined by the $(d-1)$-metric. Hence $f\mapsto f$ is injective and invertible; surjectivity is immediate (any target $(d-1)$ $f$-metric is the peel of the $d$-system's $f$-metric). The induced map is a bijection of the whole family.

**Why finite sampling is insufficient (and why B1–B2, not a finite check, are the proof).** A spectrum of size $d-1$ samples $f$ at only $\binom{d-1}{2}$ ratios; finitely many point-values cannot pin down an infinite-dimensional family. Two distinct operator-monotone functions agreeing at exactly those ratios would coincide on that single spectrum's *shape* yet remain separated by $f\mapsto f$ across spectra (B2). A finite shape-distance check across representatives is therefore a sanity test, not the theorem; the bijection over the whole family is secured by the structural label-preservation B1 together with the pointwise recovery B2.

**The $d=2$ terminus (shape $\to$ scale).** At the bottom rung the residual is $d=2$: the flag is $U(2)/U(1)^2 = \mathbb{CP}^1$ with a single root space, so the shape carries $\binom{2}{2}-1 = 0$ degrees of freedom and the normalized shape is trivial for every $f$. The label does not vanish — it sits in the single weight's spectral dependence
$$
w_f(\lambda_1,\lambda_2) = \frac{(\lambda_1-\lambda_2)^2}{\lambda_2\, f(\lambda_1/\lambda_2)},
$$
from which $f$ is still recovered (B2). So $f\mapsto f$ remains injective at the terminus, but via **scale** rather than shape — the unique-shape ($\check{\mathrm{C}}$encov) terminus of the shape axis. $\qquad\square$

---

## 5. One mechanism, both halves; scope and caveats

Propositions A and B are the same fact read on two axes. The degree $-1$ homogeneity of $w_f$ makes the peel's renormalization act **simultaneously** as a uniform constant homothety on the fiber metric (the scale side — A, preserving connection/curvature/holonomy) and as the identity on the metric label (the shape side — B, a bijection of the family). The two moves commute, and $u=1-\lambda_1$ is independent of $f$ while $f$ is independent of $u$, so the scale and shape data are orthogonal and the peel respects that splitting.

**Scope.**
- *Generic stratum.* The arguments assume distinct eigenvalues, where the flag is smooth. At spectral coincidences the weights $w_f=(\lambda_i-\lambda_j)^2 c_f$ vanish and the flag degenerates — a measure-zero locus; the dimension count terminates at $d\le 2$. The clean statement is "on the distinct-spectrum stratum."
- *Post-selection, not CPTP.* The $1/u$ inflation is the post-selection weight $1/P(\text{not-dominant})$, not a data-processing contraction (§1).

**Caveats for a formal write-up.**
- *Shared mechanism.* Both propositions rest on the **same** homogeneity Lemma; this is why they are not ad hoc, but also why a single error there would touch both. The rigor should concentrate on (i) the Lemma, (ii) the $U(d)$-invariance of $g_\lambda$ on the flag, and (iii) the invariant-connection / totally-geodesic criterion (Lemma A2). Items (ii)–(iii) are standard [KN] but are invoked here rather than re-proved at general $d$.
- *The one $[\text{sketch}\to\text{theorem}]$ item* is Lemma A2 at general dimension: machine-verified at $d=3,4,5$, with the general case resting on the isometry-fixed-point argument above.

**What this does *not* address (genuinely open).**
- Whether the curvature operator carries a forced low-rank signature, and whether any such signature coincides with other rank-$2$ structures in the surrounding theory. The totally-geodesic argument is about the fiber connection and says nothing about the rank of the curvature operator.
- Whether the $1/u$-per-rung similarity is *physically instantiated* by a concrete dynamical flow, versus structurally shared.

---

## 6. Verification record (reproducible)

All checks in `sympy 1.14` (symbolic, exact unless noted).

1. **Homogeneity, symbolic $f$.** $c_f(\sigma a,\sigma b)-\sigma^{-1}c_f(a,b)=0$; $w_f(\sigma\lambda)_{ij}-\sigma\,w_f(\lambda)_{ij}=0$; and the peel form $w_f(\lambda)_{ij}-u\,w_f(\lambda/u)_{ij}=0$ — for a fully symbolic operator-monotone $f$.
2. **Label recovery.** $w_f(t,1)=(t-1)^2/f(t)$, hence $f(t)=(t-1)^2/w_f(t,1)$ (returns $f$ identically).
3. **Homothety preserves the connection.** For $g\mapsto c\,g$, every Christoffel symbol is unchanged: $\max_{k,i,j}\lvert\Gamma^k_{ij}(cg)-\Gamma^k_{ij}(g)\rvert = 0$.
4. **Curvature scaling, non-vacuous.** On the hyperbolic plane ($ds^2=y^{-2}(dx^2+dy^2)$, $K=-1$): $K(cg)=-1/c=K(g)/c$.
5. **Totally geodesic (from the underlying records).** $\max\lvert\langle[\mathrm{res},\mathrm{res}]_{\mathfrak m},\mathrm{shed}\rangle\rvert=0$ and $\max\lvert\langle[\mathrm{shed},\mathrm{res}]_{\mathfrak m},\mathrm{res}\rangle\rvert=0$ for all weights at $d=3,4,5$, so $\mathrm{II}=0$.
6. **Post-selection inflation.** For a residual mode $X$, $\Phi_*X=X/u$ and $g_f(\Phi\rho)(\Phi_*X,\Phi_*X)/g_f(\rho)(X,X)=1/u$ exactly (all $f$, all spectra); shed modes are annihilated.

---

## References

*(To be finalized; the entries below are the standard sources for the cited facts. Bracketed keys are used above.)*

- **[P96]** D. Petz, *Monotone metrics on matrix spaces*, Linear Algebra and its Applications **244** (1996), 81–96.
- D. Petz and C. Sudár, *Geometries of quantum states*, Journal of Mathematical Physics **37** (1996), 2662–2673.
- **[MC]** E. A. Morozova and N. N. Chentsov, *Markov invariant geometry on manifolds of states* (1989); modern formulation in [P96].
- F. Kubo and T. Ando, *Means of positive linear operators*, Mathematische Annalen **246** (1980), 205–224. *(operator-monotone characterization)*
- S. L. Braunstein and C. M. Caves, *Statistical distance and the geometry of quantum states*, Physical Review Letters **72** (1994), 3439–3443. *(the QFI normalization; the symmetric / Bures member)*
- **[KN]** S. Kobayashi and K. Nomizu, *Foundations of Differential Geometry*, Vols. I–II, Wiley (1963/1969). *(totally-geodesic submanifolds as isometry fixed-point sets; invariant connections on homogeneous spaces)*
- N. N. Čencov, *Statistical Decision Rules and Optimal Inference*, AMS Translations of Mathematical Monographs **53** (1982). *(classical uniqueness; the $d\le 2$ terminus)*

---

*Context (demarcated). This note isolates, as a self-contained statement in the geometry of monotone metric spaces, the closure of two questions raised in a larger research program: the fiber isometry-up-to-scale and the metric-family automorphism under the spectral peel. The mathematics above stands independently of any reading from that program.*
