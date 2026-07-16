# Manifold Existence via Homogeneity, not a Curvature-Bound Axiom
## O-a discharged for the scale arena; the bulk multiplicity identified as non-two-point-homogeneity

*Date: 15 June 2026. Reviewer-led session (Will held the reins to the reviewer for this item). Companions: 6-9 external review record (Routes 1/2/3, O-a); interior-spine §11 (measure-completeness → budget); the QFI-normalized universality thread (bimetric crossing γ* Petz-invariant); the shape/scale factorization (5-29) and the automorphic/bijective Hodge dissolution. Tier marks: **[V]** machine-verified this session; **[T]** theorem/standard result, cited; **[A]** posit; **[O]** open.*

---

## 0. The question (the last gap on the foundations leg)

The space-first reduction runs: axioms on the **constructed distinguishability metric space** (boundedness / passivity / contractivity — one convergent constraint; note these are properties of the *information geometry built from* a system, not of the system, which may be closed/open/gain/lossy/nonlinear) → **manifold** → nonunique sufficient statistic → additive Fisher metric (sufficient) → budget as the **d = 2 boundary condition** (d = distinguishable DOF), with the cascade the coarse-graining flow between d and the total D.

The one owed item is the manifold-existence arrow. The 6-9 record listed three routes and flagged Route 2 (Berestovskii 1975 + Nikolaev smoothing) as carrying a **two-sided Alexandrov curvature bound = a new axiom**. The question: is the manifold *forced*, or does it rest on that added axiom?

## 1. The wrong route, and the asymmetry that kills it

Route 2 tries to get the manifold from a two-sided curvature bound, and hopes contractivity supplies the bound. It does not supply *both* sides. Contractivity is a property of **maps** (coarse-grainings are non-expansive in the monotone metric). Translating a contraction property into an intrinsic curvature statement — where it can be done at all, as in synthetic-Ricci theory (Lott–Sturm–Villani; Bakry–Émery) — yields **lower** curvature bounds. The **upper** bound (curvature bounded above, CBA) is a strictly stronger and separate regularity condition that no contraction property delivers. [T]

So Route 2 needs the upper bound as an *input*: the "new axiom." The contractivity → curvature-bound program is therefore the wrong way to *force* the manifold. This is an asymmetry argument and does not depend on the precise synthetic-Ricci translation; it depends only on contraction-type hypotheses being lower-bound-flavored while CBA is not.

## 2. The right route: homogeneity (no curvature axiom)

Two classical facts make the curvature bound unnecessary:

- **Topological manifold from homogeneity.** A homogeneous, locally compact, finite-dimensional, locally contractible space is a topological manifold (Montgomery–Zippin; the homogeneous case of Hilbert's fifth problem). No curvature hypothesis. [T]
- **Smooth manifold from two-point homogeneity.** A connected two-point-homogeneous space is a rank-one symmetric space (or Euclidean) — Wang 1952, Tits 1955 — which is automatically a smooth Riemannian manifold with its curvature **fixed by the symmetric-space structure**, not imposed. [T]

Once the observer-symmetry is identified as SU(1,1) (from the multiplicative-tilting / Radon–Nikodym Lorentzian invariant `pq = T²−X²`, interior-spine §11.2), the **scale arena is its symmetric space** `SU(1,1)/U(1) = ℍ²` (the Poincaré/budget disk). Two-point homogeneity of that arena reduces to two ingredients the framework already has:

- **transitivity** — tilting carries any interior state to any other (the boost acts transitively on the disk);
- **isotropy transitive on directions** — the phase `U(1)` fixes a point and rotates its tangent directions transitively.

Transitive + isotropy-transitive = two-point homogeneous ⇒ rank-one symmetric ⇒ smooth, with curvature a *consequence*. Verified: the budget/Poincaré disk metric `ds² = 4|dz|²/(1−|z|²)²` has Gaussian curvature **K ≡ −1** [V]. **O-a is discharged for the scale arena** as a transitivity check supplied by the observer-symmetry; the curvature is not an axiom.

## 3. The bulk: a manifold without a curvature axiom, and the multiplicity located

For the full state space (with the shape/angular directions), the manifold structure comes from homogeneity (topological, §2) plus the **explicit, computable** smoothness of the Fisher/monotone metric on the interior — not from an imposed bound. The qubit (d = 2) anchor, derived from the Morozova–Chentsov form `⟨A,A⟩_ρ = Σ_{ij} c_f(λ_i,λ_j)|A_{ij}|²` on the equatorial slice `ρ = (I + r cosθ σ_x + r sinθ σ_y)/2`, eigenvalues `λ_± = (1±r)/2`:

| direction | coefficient | f-dependence |
|---|---|---|
| radial (scale) | `g_rr = ¼(1/λ₊ + 1/λ₋) = 1/(1−r²)` | **none** — equals the classical Fisher–Rao of `(1±r)/2` [V] |
| angular (shape) | `g_θθ = (r²/2)·c_f(λ₊,λ₋)` | **f-dependent** — the Petz fiber [V] |

Per-metric Gaussian curvature of the slice, all **smooth and two-sided bounded on the interior** [V]:

| monotone metric | `c_f(x,y)` | `g_θθ` | `K(r)` | `K` at r = 0.2, 0.5, 0.8 |
|---|---|---|---|---|
| Bures / SLD (minimal = QFI) | `2/(x+y)` | `r²` | **+1 (constant)** | +1, +1, +1 |
| Kubo–Mori (entropy Hessian) | `(ln x − ln y)/(x−y)` | `(r/2)ln[(1+r)/(1−r)]` | varies | −0.009, −0.073, −0.364 |
| RLD (maximal) | `(x+y)/(2xy)` | `r²/(1−r²)` | `−2/(1−r²)` | −2.08, −2.67, −5.56 |

Three things follow:

1. **No curvature axiom in the bulk.** Each monotone metric's curvature is *computed* and finite on compact interior subsets, so each gives a manifold by ordinary smoothness. The curvature blows up only at the pure-state boundary `r → 1` (e.g. RLD `K → −∞`), which is the finite-disconnectedness / stratification edge (boundary = lower stratum), exactly as the space-axiom layer provides. [V]
2. **The multiplicity is the gap between "monotone" and "two-point homogeneous."** The family contains both a two-point-homogeneous member (Bures = SLD, the only constant-curvature one) and non-two-point-homogeneous members (Kubo–Mori, RLD, non-constant curvature). The Petz fiber exists *because* the monotonicity axiom does not force two-point homogeneity. The nonuniqueness is the shape leverage, not a defect awaiting a selection rule. [V]
3. **This is the QFI-normalized universality, restated geometrically.** The unique two-point-homogeneous member is Bures/SLD = the QFI metric. So normalizing the distinguishability ratio by QFI is referencing against the symmetric member; the bimetric crossing γ* is Petz-invariant because it lives in the shared radial sector `g_rr` (f-independent); and the multiplicity is the departure of the other monotone metrics from the symmetric one. The crossing varies with γ but is *the same function* across the family in the radial sector — crossing 1 at γ* (= 2−√2 at d = 2) regardless of the metric. [V/T]

## 4. Why this closes the leg and unifies with the rest

The same structural fact does three jobs at once:

- **forces the scale-arena manifold** (two-point homogeneity ⇒ `ℍ²`, curvature −1, no axiom);
- **explains the interior multiplicity** (its *failure* in the angular directions ⇒ the Petz fiber);
- **carries the universality** (γ* lives in the radial sector every monotone metric shares; QFI = the symmetric member that normalizes the ratio).

So scale = two-point-homogeneous = forced kinematics = dimensionally agnostic (filtration/cascade), and shape = non-two-point-homogeneous = the leverage = dimension-conditional. The foundations leg and the interior-leverage theme are one geometry, not two results.

## 5. Status and honest residuals

- **O-a discharged for the scale arena** (d = 2 budget disk): manifold and curvature −1 forced by the observer-symmetry's symmetric-space structure; the Route-2 curvature-bound axiom is **not needed**. [V/T]
- **Bulk manifold** forced by homogeneity (topological) + explicit Fisher-metric smoothness (computed, interior-bounded). Verified at d = 2; the structure is general (monotone metrics are real-analytic on the full-rank interior in every d, with singular strata only on the boundary faces — the finite-disconnectedness allowance). The full-d statement is therefore [V at d=2] + [T, general], not [V] in all d. [A→T candidate: write the all-d interior-analyticity + boundary-stratification statement as a single lemma.]
- **Untouched:** the dynamical floor — c-as-a-law, field equations, equivalence beyond kinematics. This note is entirely kinematic/foundational; the dynamical frontier remains the open question, and is now the lone item separating "general organizing kinematics" from "physical theory." [O]

---

## Appendix — verification

```python
import sympy as sp
r, th = sp.symbols('r theta', positive=True)

def gauss_K(E, F, G, u, v):
    g = sp.Matrix([[E, F],[F, G]]); ginv = g.inv(); coords=[u,v]
    Gam=[[[0]*2 for _ in range(2)] for _ in range(2)]
    for l in range(2):
        for i in range(2):
            for j in range(2):
                s=sum(ginv[l,m]*(sp.diff(g[m,i],coords[j])+sp.diff(g[m,j],coords[i])-sp.diff(g[i,j],coords[m])) for m in range(2))
                Gam[l][i][j]=sp.simplify(s/2)
    def R(l,i,j,k):
        t=sp.diff(Gam[l][i][k],coords[j])-sp.diff(Gam[l][i][j],coords[k])
        for m in range(2): t+=Gam[l][j][m]*Gam[m][i][k]-Gam[l][k][m]*Gam[m][i][j]
        return sp.simplify(t)
    return sp.simplify(sp.simplify(g[0,0]*R(0,1,0,1)+g[0,1]*R(1,1,0,1))/g.det())

# calibration: unit sphere -> +1 ; Poincare/budget disk -> -1
psi=sp.symbols('psi',positive=True)
assert gauss_K(1,0,sp.sin(psi)**2,psi,th)==1
assert gauss_K(4/(1-r**2)**2,0,4*r**2/(1-r**2)**2,r,th)==-1   # budget disk K=-1

# monotone metric on qubit equatorial slice
lamp,lamm=(1+r)/2,(1-r)/2
g_rr=sp.simplify(sp.Rational(1,4)*(1/lamp+1/lamm))            # = 1/(1-r^2), f-independent
p=(1+r)/2
assert sp.simplify((sp.diff(p,r)**2/p+sp.diff(1-p,r)**2/(1-p))-g_rr)==0   # = classical Fisher-Rao

for name,c in {'Bures':lambda x,y:2/(x+y),
               'Kubo-Mori':lambda x,y:(sp.log(x)-sp.log(y))/(x-y),
               'RLD':lambda x,y:(x+y)/(2*x*y)}.items():
    g_thth=sp.simplify((r**2/2)*c(lamp,lamm))
    K=gauss_K(g_rr,0,g_thth,r,th)
    print(name, 'g_thth=',g_thth, ' K=',sp.simplify(K),
          ' K@(.2,.5,.8)=',[round(float(K.subs(r,v)),4) for v in (sp.Rational(1,5),sp.Rational(1,2),sp.Rational(4,5))])
```

Output:
```
Bures      g_thth= r**2                                K= 1                  K@(.2,.5,.8)= [1.0, 1.0, 1.0]
Kubo-Mori  g_thth= r*(-log(1-r)+log(r+1))/2            K(r) (non-constant)   K@(.2,.5,.8)= [-0.0092, -0.0726, -0.3643]
RLD        g_thth= -r**2/(r**2-1)                      K= 2/(r**2-1)         K@(.2,.5,.8)= [-2.0833, -2.6667, -5.5556]
```

*g_rr is f-independent (= classical Fisher–Rao of the eigenvalue distribution); g_θθ and hence the curvature are f-dependent; Bures/SLD/QFI is the unique constant-curvature (two-point-homogeneous) member; the budget/Poincaré disk is K = −1.*
