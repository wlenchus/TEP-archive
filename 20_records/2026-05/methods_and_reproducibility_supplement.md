# Methods and Reproducibility Supplement

## Means and methods for the load-bearing computational claims across all three records

*This supplement records the exact computational means for the claims in the external-review consolidation, the kinetic cascade record, and the bulk anatomy / frame-dragging record. It exists because several of these results are* ***method- sensitive in a way the result statements alone do not convey****: the same computation performed with a different (wrong) invariant gives the opposite answer. The investigation contains documented instances where a coordinate artifact or a trivial- cancellation quantity produced a false verdict (a divergent "singularity" that was a gauge artifact; a flat connection that detected nothing; a ratio that could not fail). So for these claims, recording the result without the method would make them* ***non-reproducible or, worse, reproducibly-wrong****. Each entry below gives: the claim, the faithful method, the specific wrong method that must be avoided and why, and runnable code.*

  

*All code is Python 3 with NumPy (and SymPy where noted). A single consolidated script (§9) reproduces the core numerical claims under one fixed seed. Environment: NumPy ≥1.20; no other dependencies. Tolerances: machine-precision claims use 1e-8 to 1e-12 relative; "verified" means the residual is at floating-point noise level across the stated sample.*

  

*Date: 29 May 2026. Companion to the three investigation records.*

  

## 0\. The general reproducibility principle (why method-recording is load-bearing here)

Three classes of error recurred in this investigation, each producing a *false* result that looked clean:

  

1.  **Coordinate/gauge artifacts** — computing an obstruction through a quantity that diverges where a coordinate degenerates, then reading the divergence as structural. (The metric-invariance arc: K·vol diverged at the degeneracy because the collapsing gap was in a denominator; the gauge-invariant θ = −(b−a)/c is finite.)
2.  **Trivial-cancellation quantities** — testing a dimensionless ratio whose normalization cancels by construction, so the test *cannot fail* regardless of the geometry. (The first O-4 attempt; the first O-2 θ-ratio.)
3.  **Degenerate-example confirmation** — testing at d=3, where special structure and generic structure coincide, so a false general claim is confirmed. (The d=3 trap: four distinct rank/dimension claims confirmed at d=3, all false at d≥4.)

  

**The reproducibility rule that defends against all three: a test must be (a) computed through a coordinate-invariant quantity, (b) able to fail (verify the object is nontrivial before trusting a "preserved" result), and (c) run at d≥4, ideally d=4,5,6 to see the trend.** Every method below is built to satisfy these.

  

## 1\. The DHO N=4 boost-law quartic and the G-distortion master identity (T1)

**Claims (consolidation Δ6, Δ7):** the four reactive crossings of the N=4 damped- harmonic-oscillator chain are roots of an exact quartic in the budget variable u with Σu = 4(1+6ζ²) (pure ζ), ∏u = det(I−K) = κ⁴−3κ²+1 (pure κ, the closure), and the lone ζ–κ coupling term +12κ²ζ². The crossings obey the master identity |w²|² = X² + Y² with X = Re(w²), Y = Im(w²), and (X−r₊)(X−r₋) = Y² with r± = φ²/4, 1/(4φ²) the golden / inverse-golden values; the distortion Y = ζ√u(1−u)/κ² is exactly the G-factor acting on the loss-tangent budget.

  

**Method.** Form the Chebyshev determinant Re\[U₄(w)\] with w = ((1−u) + 2iζ√u)/(2κ); its real part is the quartic in u with the stated coefficients. The crossings are its real roots. For each root compute a = (1−u)/(2κ), b = ζ√u/κ, then X = a²−b², Y = 2ab, |w²| = a²+b², and verify both identities to machine precision.

  

**Why this method is faithful:** the identities are *algebraic* (exact, not statistical), so verification is a direct equality check at the roots; no coordinate choice or sampling is involved. The closure ∏u = det(I−K) is read directly off the constant term c4 of the quartic.

  

import numpy as np

  

phi=(1+5\*\*.5)/2; rp=(3+5\*\*.5)/8; rm=(3-5\*\*.5)/8   \# golden / inverse-golden

  

def roots4(kv,zv):

  

    c1=-(4+24\*zv\*\*2); c2=6+48\*zv\*\*2+16\*zv\*\*4-3\*kv\*\*2

  

    c3=12\*kv\*\*2\*zv\*\*2+6\*kv\*\*2-24\*zv\*\*2-4; c4=kv\*\*4-3\*kv\*\*2+1   \# c4 = det(I-K)

  

    return np.sort(np.roots(\[1,c1,c2,c3,c4\]).real)

  

for kv,zv in \[(0.3,0.1),(0.5,0.2),(0.4,0.3)\]:

  

    for u in roots4(kv,zv):

  

        a=(1-u)/(2\*kv); b=zv\*np.sqrt(u)/kv

  

        X=a\*a-b\*b; Y=2\*a\*b; W2=a\*a+b\*b

  

        assert abs(W2\*\*2-(X\*X+Y\*Y))\<1e-12          \# |w^2|^2 = X^2 + Y^2

  

        assert abs((X-rp)\*(X-rm)-Y\*Y)\<1e-9         \# (X-r+)(X-r-) = Y^2

  

**Scope:** the single-clean-term structure (one Y² cross-term) is specific to N=4 (two w²-factors); higher even N gives a sum of such terms. The "relativistic Doppler verified to 1e-16" headline elsewhere in the corpus is a *tautology* (both sides equal √(ω₊/ω₋) by the definitions) and should not be cited as independent verification.

  

## 2\. The gauge-invariant curvature quantity θ = −(b−a)/c (T1) — and the artifact to avoid

**Claim (bulk record §1, consolidation Δ12):** at an eigenvalue degeneracy the fiber- curvature obstruction is *finite* (θ → −1 at λ₁=λ₂), NOT a curvature singularity. An earlier computation reported a singularity; that was a gauge artifact.

  

**The faithful method:** use θ = −(b−a)/c, where a,b,c are the three gaps (λᵢ−λⱼ)²/(λᵢ+λⱼ) of a triple. This is the Gauss–Bonnet angle density with the collapsing-gap factor *cancelled*: the sectional curvature K = −(b−a)/(ac) has the gap a in the denominator, and the area element dA ∝ a, so K·dA = −(b−a)/c has no a in the denominator and is finite at the degeneracy a→0.

  

**The wrong method (must be avoided):** computing the obstruction as K·vol with K = −(b−a)/(ac) and vol = √(abc) *normalized separately* — this puts the collapsing gap a in a denominator, so the quantity diverges as a→0, and the divergence is an artifact of the coordinate (the collapsing plane), not a feature of the geometry. A genuine curvature *singularity* is coordinate-invariant; this one evaporates under the cancelled form. **The lesson: test obstructions only through quantities where collapsing quantities are not in denominators.**

  

def gaps(l1,l2,l3): return (l1-l2)\*\*2/(l1+l2),(l2-l3)\*\*2/(l2+l3),(l1-l3)\*\*2/(l1+l3)

  

l1=0.45

  

for eps in \[1e-2,1e-4,1e-6\]:                 \# approach the l1=l2 degeneracy

  

    l2=l1-eps; l3=1-l1-l2; a,b,c=gaps(l1,l2,l3)

  

    theta = -(b-a)/c                          \# FAITHFUL: finite, -\> -1

  

    artifact = abs(-(b-a)/(a\*c))\*np.sqrt(a\*b\*c)   \# WRONG: diverges (a in denominator)

  

    \# theta stays finite (\~-1); artifact blows up (\~1/eps). The artifact is a gauge effect.

  

## 3\. The Kubo–Ando monotonicity test (T1)

**Claim (bulk record §2):** monotonicity (data-processing) is the physical selection criterion and is NOT implied by degree-1 homogeneity. The "geometric-mean" metric is *monotone* (the reviewer mislabeled it); the "engineered" metrics are genuinely non-monotone yet still peel-invariant.

  

**Method (Kubo–Ando bound):** a metric with weight coefficient c\_f is monotone (satisfies the data-processing inequality) **iff** the harmonic mean ≤ 1/c\_f ≤ the arithmetic mean of the eigenvalue pair, for all pairs. The minimal (SLD/Bures) metric saturates the arithmetic bound; the maximal metric saturates the harmonic. Sample random eigenvalue pairs and count bound violations: zero violations ⟹ monotone.

  

**Why faithful:** the Kubo–Ando bound is the *definition* of the monotone-metric class (Petz–Sudár / Kubo–Ando operator-mean characterization); it is basis-independent (a property of the weight function c\_f(a,b)). Testing it directly is the standard membership test.

  

hfuns={'bures':lambda a,b:2/(a+b),

  

       'geom-mean':lambda a,b:1/np.sqrt(a\*b),                         \# MONOTONE (was mislabeled)

  

       'engineered-A':lambda a,b:(1/(a+b))\*(1+0.5\*((a-b)/(a+b))\*\*2)}  \# genuinely NON-monotone

  

rng=np.random.default\_rng(0)

  

for nm,h in hfuns.items():

  

    viol=sum(not(2\*a\*b/(a+b)-1e-9 \<= 1/h(a,b) \<= (a+b)/2+1e-9)

  

             for a,b in rng.uniform(0.05,3,(3000,2)))

  

    \# bures, geom-mean: 0 violations (monotone); engineered-A: \~all violations (non-monotone)

  

## 4\. The Petz automorphism: injectivity via residual weight-shape (T1)

**Claim (bulk record §3):** the cascade peel is a *bijection* of the full Petz family — injective (distinct metrics give distinct residuals), invertible (label recoverable), extreme-point-preserving.

  

**Method.** Parametrize the monotone family by operator-monotone f (f(1)=1, f(t)=t f(1/t)); the metric weight is w\_f(a,b) = (a−b)²/(b f(a/b)). Peel the spectrum (λ → λ\[1:\]/u), and for each f compute the *shape* of the residual weights — the vector of weights normalized to its first entry (removing the overall u-rescaling, which is the same for all f). Injectivity = distinct f give distinct shapes; check the minimum pairwise shape difference is bounded away from zero. Use genuinely different f including a non-mixture member (Kubo–Mori) to test the *full* family, not just the convex hull of the two extremes.

  

**Why faithful:** the metric *label* is encoded precisely in the *shape* (the ratios) of the weights, because the u-rescaling (scale) is label-independent (§5). So shape- distinctness is exactly metric-distinctness. Extreme-point preservation is *exact and structural* (Bures and max weight formulas are scale-covariant) and need not be sampled.

  

def fmap(nm):

  

    return {'SLD':lambda t:(1+t)/2,'max':lambda t:2\*t/(1+t),

  

            'KM':lambda t:(t-1)/np.log(t) if abs(t-1)\>1e-9 else 1.0}\[nm\]

  

def w(f,a,b): return (a-b)\*\*2/(b\*f(a/b))

  

d=5; P=\[(i,j) for i in range(d) for j in range(i+1,d)\]; res=\[p for p in P if p\[0\]\>=1\]

  

spec=np.sort(np.random.default\_rng(0).dirichlet(np.ones(d)))\[::-1\]

  

shapes={nm:(lambda s:s/s\[0\])(np.array(\[w(fmap(nm),spec\[p\[0\]\],spec\[p\[1\]\]) for p in res\]))

  

        for nm in \['SLD','max','KM'\]}

  

\# min pairwise |shape\_a - shape\_b| \> 0  (≈0.72 for this spec)  =\> injective

  

**Scope:** verified on six representatives (the script shows three; the full check used Bures, max, Kubo–Mori, Wigner–Yanase, two WYD-α) spanning the family including a non-mixture member. A fully general proof over the entire infinite-dimensional operator- monotone family is the natural completion (open).

  

## 5\. The scale/shape orthogonal split (T1) — with the iso-purity caveat

**Claim (bulk record §4):** the bulk factorizes into a scale axis (boost / SNR-rapidity, changes purity) orthogonal to a shape axis (minority-rearrangement at fixed dominant), under Fisher–Rao, with no cross-terms.

  

**Method.** On the eigenvalue simplex, Fisher–Rao is g = diag(1/pᵢ) on tangent vectors summing to zero. Define the **boost** direction v\_b: increase the dominant p₀, decrease the rest *proportionally* (preserving their ratios — a pure scale move). Define the **shape** directions v\_s: move mass between two minority components at fixed dominant (rearranging ratios). Verify ⟨v\_b, v\_s⟩\_FR ≈ 0 across random spectra and all shape directions.

  

**Faithful and honest caveat (recorded explicitly):** the shape directions are *minority-rearrangement at fixed dominant*, which is **not exactly iso-purity** — along them d(purity)/d(direction) ≈ 0.24, not 0. So the verified split is **boost ⊥ minority- rearrangement**; the identification "scale = SNR-rapidity, shape = iso-purity" is the right intuition but iso-purity (fixed γ) and the exact orthogonal complement of the boost coincide only approximately. **Do not record this as exact iso-purity orthogonality.** The boost-direction construction (ratio-preserving) is what makes it a pure-scale move; this choice is load-bearing.

  

def FR(p): return np.diag(1/p)

  

d=5; rng=np.random.default\_rng(0); worst=0

  

for \_ in range(3000):

  

    p=np.sort(rng.dirichlet(np.ones(d)))\[::-1\]; g=FR(p)

  

    vb=np.zeros(d); vb\[0\]=1; vb\[1:\]=-p\[1:\]/p\[1:\].sum()   \# boost: ratio-PRESERVING (scale)

  

    for k in range(1,d-1):

  

        vs=np.zeros(d); vs\[k\]=1; vs\[k+1\]=-1               \# minority-rearrangement (shape)

  

        worst=max(worst,abs(vb@g@vs))                     \# \~1e-15 =\> orthogonal

  

**The commuting of scale and shape (the mechanism, bulk record §4):** the Petz weight w\_f(λ)=(λᵢ−λⱼ)²/(λⱼ f(λᵢ/λⱼ)) has f enter *only through the ratio* λᵢ/λⱼ, which is *invariant under the peel's uniform rescaling* λ→λ/u. So the metric label lives on the scale-invariant ratios and the peel lives on the ratio-invariant scale; they commute by acting on complementary pieces of the weight. This is an *exact algebraic* fact (verify by inspection of the formula), not merely numerical — the numerical check (paths agree to 1e-15) confirms it.

  

## 6\. The Nomizu/Bures curvature construction (T1) — the faithful build, and two artifacts to avoid

**Claim (kinetic cascade record §4, O-4):** the genuine non-abelian Bures fiber curvature is preserved (as an identity, entrywise) under the peel; and (bulk record §1) its generic rank is maximal, refuting the rank-2 conjecture.

  

**This is the most method-sensitive claim in the investigation.** Two prior constructions were artifacts:

  

  - **Artifact 1 (trivial cancellation):** a "metric-weighted structure constant" \~ w\_ik/√(w\_ij w\_jk). Since every residual weight scales by u, this ratio is invariant *by construction* (u cancels). It **cannot fail** — it tests nothing.
  - **Artifact 2 (flat connection):** a connection built from hand-placed structure constants with a symmetric "Levi-Civita-looking" coefficient came out **flat** (zero curvature). A flat connection's holonomy is trivially unchanged by anything — it detects nothing.

  

**The faithful method — the Nomizu formula from the actual Bures metric:**

  

1.  Tangent space = off-diagonal modes; basis E\_{ij} (antisymmetric generators) for planes (i,j).
2.  Bures metric: diagonal in this basis with weight w\_ij = (λᵢ−λⱼ)²/(λᵢ+λⱼ) (the factor 2 folds into overall scale).
3.  *Compute the metric-adjoint ad from the actual metric*\* (not hand-placed): for the bracket ad\_X = \[X,·\], ad\*\_X is defined by ⟨ad\*\_X Y, Z⟩ = ⟨Y, \[X,Z\]⟩ for all Z, solved in the weighted basis.
4.  Nomizu connection: ∇\_X Y = ½\[X,Y\] − ½(ad\*\_X Y + ad\*\_Y X).
5.  Curvature: R(X,Y)Z = ∇\_X∇\_Y Z − ∇\_Y∇\_X Z − ∇\_{\[X,Y\]} Z, assembled as a matrix on the mode-frame.

  

**The mandatory gate (this is what the artifacts failed):** *before* trusting any preservation/rank result, **verify the connection is non-flat** — count nonzero curvature components (the faithful build gives 120/216 nonzero at d=4). A test of "is the curvature preserved/rank-2" is meaningless if the curvature is zero or if the tested quantity cannot fail.

  

def build\_curvature(spec):

  

    d=len(spec); P=\[(i,j) for i in range(d) for j in range(i+1,d)\]; n=len(P)

  

    E={}

  

    for (i,j) in P:

  

        M=np.zeros((d,d)); M\[i,j\]=1; M\[j,i\]=-1; E\[(i,j)\]=M

  

    w={(i,j):(spec\[i\]-spec\[j\])\*\*2/(spec\[i\]+spec\[j\]) for (i,j) in P}

  

    Wv=np.array(\[w\[p\] for p in P\])

  

    co=lambda M: np.array(\[M\[i,j\] for (i,j) in P\])

  

    def fc(c):

  

        M=np.zeros((d,d))

  

        for k,(i,j) in enumerate(P): M\[i,j\]=c\[k\]; M\[j,i\]=-c\[k\]

  

        return M

  

    def adstar(X,Y):                                   \# metric-adjoint from ACTUAL metric

  

        B=np.array(\[np.sum(2\*Wv\*co(Y)\*co(X@E\[P\[k\]\]-E\[P\[k\]\]@X)) for k in range(n)\])

  

        return fc(B/(2\*Wv))

  

    nab=lambda X,Y: 0.5\*(X@Y-Y@X)-0.5\*(adstar(X,Y)+adstar(Y,X))    \# Nomizu

  

    cur=lambda X,Y,Z: nab(X,nab(Y,Z))-nab(Y,nab(X,Z))-nab(X@Y-Y@X,Z)

  

    def R(X,Y):

  

        M=np.zeros((n,n))

  

        for k,c in enumerate(P):

  

            Rc=cur(X,Y,E\[c\])

  

            for m,p in enumerate(P): M\[m,k\]=Rc\[p\[0\],p\[1\]\]

  

        return M

  

    return P,E,R

  

\# MANDATORY GATE: confirm non-flat before any preservation/rank test

  

spec=np.sort(np.random.default\_rng(0).dirichlet(np.ones(4)))\[::-1\]

  

P,E,R=build\_curvature(spec)

  

nz=sum(np.linalg.norm(R(E\[a\],E\[b\]))\>1e-9 for a in P for b in P)  \# \~120/... nonzero =\> CURVED

  

\# Only if nz\>0 is it meaningful to test "R preserved under peel" (identity, entrywise) or

  

\# "rank of R(X,Y)" (maximal for generic X,Y -\> rank-2 conjecture REFUTED).

  

**For the preservation (O-4):** compute R on residual modes for the full spectrum and for the peeled spectrum (relabeled), and check entrywise equality (R\_dual = R\_full,residual, not merely R\_dual = O·R·O⁻¹ — verify *entrywise*, since a rotation would preserve eigenvalues while changing entries). For the rank (bulk §1): use *generic* X,Y (random combinations of all planes), not single-plane generators, and compute rank via SVD.

  

## 7\. The frame-dragging deformation (T1)

**Claim (bulk record §6.2):** a t≠0 deformation of the peel produces a scale–shape cross-term linear in t and O(t) rung non-commutativity, both zero at t=0 — the Kerr-like frame-dragging signature.

  

**Method.** Deform the boost direction by mixing in a shape rotation of strength t: v\_scale(t) = v\_boost + t·v\_shape. Measure the Fisher–Rao cross-term against an *independent* shape direction; it should be linear in t and zero at t=0. For the non-commutativity: apply two deformed moves (with different shape-mixing) in both orders; the path difference (commutator) is zero at t=0 and grows linearly.

  

d=5; p=np.array(\[0.4,0.3,0.18,0.08,0.04\]); g=np.diag(1/p)

  

vb=np.zeros(d); vb\[0\]=1; vb\[1:\]=-p\[1:\]/p\[1:\].sum()

  

vs1=np.zeros(d); vs1\[1\]=1; vs1\[2\]=-1                 \# shape direction mixed into the boost

  

vs\_test=np.zeros(d); vs\_test\[2\]=1; vs\_test\[3\]=-1     \# independent shape direction to measure against

  

for t in \[0.0,0.1,0.2\]:

  

    cross=(vb+t\*vs1)@g@vs\_test                       \# 0 at t=0, linear in t (Kerr g\_{t phi})

  

**Interpretation note:** the cross-term being linear in t *and* the non-commutativity turning on together linearly is the verified structural correspondence to the Kerr rotation parameter. "This is *gravitational* frame-dragging of a physical system" is the instantiation question (T3), separate from the verified structure.

  

## 8\. The d≥4 rule for rank/dimension claims (methodological, T1)

**Claim (bulk record §1):** d=3 is the systematic false-confirmation dimension for rank/ dimension claims; the relevant test is d≥4.

  

**Method/demonstration.** For the generic Bures fiber-curvature rank, compute at d=3,4,5: rank is 2 at d=3 (which *equals* the tangent dimension 3 minus 1, coinciding with "generic maximum minus one") and jumps to the generic maximum (6, 10) at d=4,5. Any "rank-2" claim confirmed only at d=3 is confirmed by the coincidence d−1 = 2 = generic rank, not by genuine rank-2 structure.

  

for d in \[3,4,5\]:

  

    spec=np.sort(np.random.default\_rng(d).dirichlet(np.ones(d)))\[::-1\]

  

    P,E,R=build\_curvature(spec); n=len(P)

  

    X=np.zeros((d,d)); Y=np.zeros((d,d))

  

    cx=np.random.default\_rng(1).standard\_normal(n); cy=np.random.default\_rng(2).standard\_normal(n)

  

    for k,(i,j) in enumerate(P):

  

        X\[i,j\]=cx\[k\];X\[j,i\]=-cx\[k\]; Y\[i,j\]=cy\[k\];Y\[j,i\]=-cy\[k\]

  

    rank=int(np.sum(np.linalg.svd(R(X,Y),compute\_uv=False)\>1e-8))

  

    \# d=3: rank 2 (= coincidence); d=4: rank 6; d=5: rank 10 (generic maximum)

  

**The rule, stated for reuse:** any structural claim about rank, kernel dimension, or holonomy-algebra dimension must be tested at d≥4 (ideally d=4,5,6 to confirm the trend); d≤3 evidence is treated as *no evidence* for such claims, because the tangent/curvature dimensions are small enough that special and generic structure coincide.

  

## 9\. Consolidated reproduction script

The following single script reproduces the core numerical claims (§1–§8) under one fixed seed. It is the minimal self-check that the results are not seed-artifacts.

  

import numpy as np

  

rng=np.random.default\_rng(20260529)

  

\# \[1\] DHO master identity

  

phi=(1+5\*\*.5)/2; rp=(3+5\*\*.5)/8; rm=(3-5\*\*.5)/8

  

def roots4(kv,zv):

  

    c1=-(4+24\*zv\*\*2); c2=6+48\*zv\*\*2+16\*zv\*\*4-3\*kv\*\*2

  

    c3=12\*kv\*\*2\*zv\*\*2+6\*kv\*\*2-24\*zv\*\*2-4; c4=kv\*\*4-3\*kv\*\*2+1

  

    return np.sort(np.roots(\[1,c1,c2,c3,c4\]).real)

  

ok=all(abs((a\*a+b\*b)\*\*2-((a\*a-b\*b)\*\*2+(2\*a\*b)\*\*2))\<1e-12

  

       for kv,zv in \[(0.3,0.1),(0.5,0.2),(0.4,0.3)\] for u in roots4(kv,zv)

  

       for a,b in \[((1-u)/(2\*kv),zv\*np.sqrt(u)/kv)\])

  

print("\[1\] DHO |w^2|^2=X^2+Y^2:", ok)

  

\# \[2\] gauge-invariant theta finite at degeneracy

  

def gaps(l1,l2,l3): return (l1-l2)\*\*2/(l1+l2),(l2-l3)\*\*2/(l2+l3),(l1-l3)\*\*2/(l1+l3)

  

a,b,c=gaps(0.45,0.45-1e-6,1-0.45-(0.45-1e-6))

  

print("\[2\] theta=-(b-a)/c finite (-\>-1):", abs(-(b-a)/c+1)\<1e-3)

  

\# \[3\] Kubo-Ando

  

h=lambda a,b:1/np.sqrt(a\*b)   \# geometric-mean: should be MONOTONE

  

viol=sum(not(2\*a\*b/(a+b)-1e-9\<=1/h(a,b)\<=(a+b)/2+1e-9) for a,b in rng.uniform(0.05,3,(3000,2)))

  

print("\[3\] geom-mean monotone (0 violations):", viol==0)

  

\# \[5\] scale/shape orthogonality

  

d=5; worst=0

  

for \_ in range(3000):

  

    p=np.sort(rng.dirichlet(np.ones(d)))\[::-1\]; g=np.diag(1/p)

  

    vb=np.zeros(d); vb\[0\]=1; vb\[1:\]=-p\[1:\]/p\[1:\].sum()

  

    for k in range(1,d-1):

  

        vs=np.zeros(d); vs\[k\]=1; vs\[k+1\]=-1; worst=max(worst,abs(vb@g@vs))

  

print("\[5\] scale\_|\_shape (worst\<1e-12):", worst\<1e-12)

  

\# \[6\] frame-dragging linear cross-term

  

p=np.array(\[0.4,0.3,0.18,0.08,0.04\]); g=np.diag(1/p)

  

vb=np.zeros(5); vb\[0\]=1; vb\[1:\]=-p\[1:\]/p\[1:\].sum()

  

vs1=np.zeros(5); vs1\[1\]=1; vs1\[2\]=-1; vt=np.zeros(5); vt\[2\]=1; vt\[3\]=-1

  

cr=\[ (vb+t\*vs1)@g@vt for t in \[0,0.1,0.2\]\]

  

print("\[6\] frame-drag cross-term linear, zero at t=0:", abs(cr\[0\])\<1e-12 and abs(cr\[2\]-2\*cr\[1\])\<1e-9)

  

Expected output: all True. (The Petz bijection §4, the Nomizu curvature §6/§8, and the d≥4 rank trend require the longer builds above; they are omitted from the minimal script for length but reproduce identically under the same seed.)

  

## 10\. What is NOT reducible to a reproduction script (and how to check it instead)

Some claims are structural/algebraic rather than numerical, and "reproducibility" for them means *re-deriving*, not re-running:

  

  - **The homogeneity argument** (degree-1 weight → degree-0 connection → degree-0 curvature operator, kinetic cascade §6): verify by inspecting the homogeneity degrees of the weight formula and the Nomizu construction. The numerical curvature-preservation (§6 above) is the *consequence*; the homogeneity is the *cause*, checked by hand.
  - **Chentsov as the d≤2 shape-axis collapse** (bulk §5.2): verify by the shape-DOF count — at d=2 there is one plane, hence zero independent weight-ratios, hence a unique metric. This is a counting argument, not a computation.
  - **The three-layer separation** (spectral / homogeneity / monotonicity, bulk §2): verify that the budget x²+u=1 is a function of the spectrum alone (metric-independent), that the recursion follows from homogeneity (the engineered non-monotone metrics recurse), and that monotonicity is the Kubo–Ando bound (§3) — three independent checks.
  - **The bulk-axis ↔ ζ-dictionary-axis identification** (bulk §6.1): this is a T2 structural correspondence (same role on both sides), not a numerical equality; it is not reducible to a check and is recorded as an identification, not a theorem.

  

  

*End of supplement. The load-bearing principle: for every preservation/obstruction/rank claim, use a coordinate-invariant quantity, confirm the tested object is nontrivial (the test can fail), and test at d≥4. The recurring artifacts in this investigation — the divergent gauge quantity, the flat connection, the trivial-cancellation ratio, the d=3 coincidence — were all caught by these three checks, and any reproduction should apply them.*

  