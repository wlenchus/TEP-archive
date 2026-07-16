# Entrodynamics as a Metriplectic System
## A variational principle for the dynamics, assembled from the budget's forced Kähler and bimetric structure

*Date: 17 June 2026. Author: the reviewer (Claude), in an extended adversarial-review session.
This note proposes that the framework's **dynamical** content — the gap the foundations leg
repeatedly names as the lone item separating "organizing kinematics" from "physical theory" —
is a **metriplectic (GENERIC) flow** whose two operators the framework already supplies in
forced form: a symplectic structure from the SU(1,1) coadjoint orbit and a dissipative metric
from Chentsov–Petz. The note's distinguishing feature is that its structural core is **verified
this session**, including a decisive independent check (the Mandelstam–Tamm purity speed limit
recovered as a gradient flow), with the seams that remain open marked explicitly.*

*Tier convention (corpus): **[V]** machine-verified this session (sympy 1.14 / numpy 2.4);
**[T]** standard/elementary, cited; **[G]** grounded in a verified corpus result; **[A]** posit;
**[P]** my proposal/extrapolation; **[O]** open. Verification code is in the Appendix and is
reproducible from the forms stated.*

---

## 0. The claim, in one paragraph

The kinematic floor (interior-spine §11; 6-2 §11.2; 6-15) derives the relativistic *group and
geometry* — SU(1,1), the K=−1 hyperbolic interval, the Lorentzian signature — but only
**classifies** admissible dynamics (the su(1,1) trichotomy), it does not **select** the realized
one. A variational principle is exactly what converts a classification into a selection. The
proposal here is that the realized dynamics is the **metriplectic flow**

> **dρ/dτ = {ρ, E}_ω + grad_g(S)**     (reversible Hamiltonian part + dissipative gradient part)

on the budget manifold, with the two operators **already forced** by the framework: the symplectic
form `ω` is the Kirillov–Kostant–Souriau form of the SU(1,1) coadjoint orbit (the budget disk),
and the dissipative metric `g` is the Fisher/QFI metric forced by Chentsov–Petz. The complex
structure `J` relating them (Kähler) is the framework's time↔space **Wick involution**. The
framework's **bimetric** apparatus (K=−1 Poincaré vs K=+4 QFI) is, on this reading, *exactly* the
metriplectic two-operator structure — `ω` from the K=−1 side, the dissipative metric from the K=+4
side — and the central bimetric balance **γ\* = 2−√2 is the point where the two operators
curvature-normalize**. The framework's own **(σ,t) plane** (Markovianity × associativity) is the
pair of **GENERIC degeneracy conditions**. The decisive consequence: the **Mandelstam–Tamm purity
speed limit, derived independently, is the gradient flow of the dissipative bracket** — a
second, non-circular fact the structure reproduces.

This is a research direction, not an established theory. §3–§5 are verified; §6 (the reversible
Hamiltonian and the degeneracy-condition checks) is proposed with a stated pending computation;
§7 marks what it does and does not reach (it reaches `c`-as-law and resolves a prior retraction;
it does **not** reach gravity/field equations).

---

## 1. The ingredients the framework already supplies (forced, not imported)

The forward-directions note (6-17) flagged the variational mechanism as an **external import**
(`[X]`, the optimal-transport / GENERIC picture), cutting against the corpus's internal-derivation
preference. That framing is too pessimistic: every operator a metriplectic system needs is already
present in **forced** form. "GENERIC" here is not foreign machinery bolted on; it is the
*recognition* that the framework's own forced structures **are** a metriplectic system.

- **The symplectic form `ω` [G, standard].** The budget disk is the symmetric space
  `SU(1,1)/U(1) = ℍ²`, a coadjoint orbit of SU(1,1); coadjoint orbits carry the canonical KKS
  symplectic form, and the SU(1,1) action is Hamiltonian with respect to it (Kirillov; Perelomov).
  The corpus books this triple explicitly (6-9 I.10: budget disk = SU(1,1) coadjoint orbit ⟹
  compatible `(g, ω, J)` by KKS + Hermitian-symmetric structure). This is the **reversible**
  (Poisson) operator `L`.

- **The dissipative metric `g` [G].** "Passivity = monotonicity under coarse-graining" forces the
  metric: Chentsov on the simplex (unique Fisher–Rao), Petz on density operators (the monotone
  family) — 6-7 II.6. The **QFI** (= 4·Bures, Braunstein–Caves) is the metric of statistical
  *distinguishability*, which dissipation degrades; §4 confirms it is the right dissipative
  operator `M` by recovering the speed limit. The two metrics are *independent* operators
  (`L` from the orbit, `M` from Chentsov–Petz) — exactly as GENERIC allows; they need not be a
  single metric.

- **The complex structure `J` [G].** On the Hermitian symmetric disk, `(g, ω, J)` is a compatible
  Kähler triple. The corpus's sole novel identification is `J` = the time↔space involution = the
  2D Hodge star (6-9 I.10; the Wick involution `√SNR → i√SNR` of 6-7 II.4). `J` is what rotates the
  reversible flow into the dissipative one.

- **The (σ,t) plane [G, live speculative-sideline dictionary].** The geometric dictionary (5-2;
  5-29 §6) carries two conjugate axes — **σ = memory/dissipation** (σ=½ = detailed balance, the
  functional-equation/time-reversal symmetry σ↔1−σ) and **t = associativity/commutativity** (t=0 =
  cascade rungs commute; off it `[f_a,f_b]=O(t)`) — that are *harmonic conjugates* on the plane.
  *(Provenance note, corrected this session: this (σ,t)/ζ dictionary is a live speculative sideline,
  not retracted material. Only the specific monotonicity→RH **implication** (5-29 Δ9) was retracted;
  the structural correspondence "self-dual budget point ↔ critical line as one fixed locus in two
  representations" is tagged [T] in 6-9 T-2, with "zeros untouched." The dictionary is used below
  as a structural scaffold, at that strength.)*

- **The cascade as a flow [G].** The cascade is a genuine path-sum over depth — rapidity
  `τ = Σ ln(1/u_k)`, `∏u_k = exp(−Στ)` — and is the forgetting/heat semigroup (5-29 §6.3; 6-9 T-3).
  It is the **dissipative gradient flow** in this picture.

---

## 2. The metriplectic proposal

A metriplectic (GENERIC, Grmela–Öttinger; Morrison) system is

> **dx/dτ = L · δE/δx + M · δS/δx,**

with `L` antisymmetric (Poisson, reversible), `M` symmetric positive (friction, irreversible), and
two **degeneracy conditions**: `L·δS = 0` (the reversible flow conserves entropy) and `M·δE = 0`
(the dissipative flow conserves energy). The proposal maps the framework onto this exactly:

| GENERIC object | framework realization | status |
|---|---|---|
| `L` (Poisson / reversible) | KKS symplectic form `ω` of the SU(1,1) coadjoint orbit | [G] forced |
| `M` (friction / dissipative) | QFI/Fisher metric (Chentsov–Petz) | [G] forced; [V] §4 |
| `J` (Kähler, `L↔M` rotation) | time↔space Wick involution | [G] |
| `E` (conserved energy) | SU(1,1) Casimir / mass-shell invariant `pq = x²u` | [A/P] §6 |
| `S` (produced entropy) | capacity `𝒞 = ln(1+SNR) = −ln u` (equiv. entropy `−𝒞`) | [V] §3 |
| `L·δS = 0` degeneracy | **t = 0** (scale ⊥ shape; cascade associative) | [G/P] §6 |
| `M·δE = 0` degeneracy | **σ = ½** (detailed balance) | [G/P] §6 |
| degeneracies relaxed | **t ≠ 0, σ ≠ ½** (frame-dragging / driven) | [G] §6 |

The content is in fixing `E` and `S` from the framework's own invariants — which is what converts
the kinematic *classification* into a dynamical *selection*.

---

## 3. Verified core — the capacity is a J-conjugate generator on the Kähler disk [V]

On the K=−1 budget/Poincaré disk `ds² = 4(dr² + r²dθ²)/(1−r²)²`, with the budget reading
`x² = r²`, `u = 1−r²`, and the **capacity** (corrected to the full per-bandwidth form, nats)

> **𝒞 = ln(1 + SNR) = ln G²(x) = −ln u = −ln(1−r²),**     `C/B = 𝒞/ln2` (bits),

the following hold (all [V], symbolic):

- **The gradient flow is radial and dissipative.** `grad_g 𝒞 = [r(1−r²)/2] ∂_r` (radial), with
  **Laplace–Beltrami `Δ_g 𝒞 = 1 = |K|`** and divergence `1 ≠ 0` — so the flow *changes hyperbolic
  volume* (irreversible) at a **uniform rate equal to the curvature magnitude**. This is the cascade
  / forgetting direction (toward/from the pure-state boundary).

- **Its J-conjugate is symplectic and reversible.** `X_𝒞 = −J·grad_g 𝒞 = −[(1−r²)/2] ∂_θ`
  (a differential rotation) is **area-preserving**: `L_{X_𝒞} ω = 0` and `div X_𝒞 = 0`. It is a
  Hamiltonian (symplectic) vector field — the reversible flow.

- **One functional, two flows, rotated by J.** The same capacity `𝒞` supplies a dissipative
  gradient flow and a reversible symplectic flow, conjugate by `J` (the Wick involution). The
  residual `u` is conserved by the rotation and changes monotonically along the gradient flow.

So `J` (the time↔space involution) is concretely the **reversible↔irreversible rotation** of a
metriplectic system, and the capacity is a clean **dissipative potential** with an explicit
symplectic conjugate. (`Δ_g 𝒞 = |K|` is a small elegant fact: on the hyperbolic disk the capacity
is, up to a constant, `2 ln cosh(ρ/2)` in geodesic radius `ρ`, with uniform Laplacian.)

---

## 4. The decisive check — the Mandelstam–Tamm speed limit IS the dissipative gradient flow [V]

This is the test the forward-directions note rightly demanded: does the structure reproduce a
**second, independent** dynamical fact, or only re-encode itself? It reproduces one.

The purity speed limit (central reference 1.1; 5-8) — derived **independently** as a
Mandelstam–Tamm corollary — is `|dγ/dt| ≤ 4‖H‖√F`, `F = p₃ − γ²`, saturated by `H_opt = iW/√F`.
For the qubit, `F = r²(1−r²)/4` [V]. Taking the **QFI** as the dissipative metric (radial part
`g_rr = 1/(1−r²)`, the f-independent Fisher–Rao radial shared by the whole monotone family = 4×Bures):

> **|∇γ|²_QFI = (1−r²)·(∂_r γ)² = r²(1−r²) = 4F,   i.e.  F = ¼ |∇γ|²_QFI**     [V, ratio exactly 4]

Hence `max|dγ/dt| = 4√F = 2|∇γ|_QFI` — the maximal rate of the purity is **twice its QFI-gradient
norm**, the factor 2 being Mandelstam–Tamm's. In other words, **the speed-limit-saturating
trajectory is precisely the gradient flow of the purity in the QFI (dissipative) metric**, and the
explicit saturator `H_opt = iW/√F` is the gradient direction. The Mandelstam–Tamm bound — proved
without reference to any of this — *is* the dissipative bracket of the metriplectic structure. This
is the non-circular fact the proposal needed to clear, and it clears it.

The radial flow of §3 (capacity, in the Poincaré metric) and the radial flow here (purity, in the
QFI metric) are the **same dissipative direction** — radial, toward/from the pure-state boundary —
described in the two metrics of the bimetric. §3 exhibits its J-conjugacy to the reversible flow;
§4 exhibits that it reproduces the independently-derived speed limit.

---

## 5. The bimetric IS the two-operator structure; γ* = 2−√2 is the metriplectic balance [V]

The framework's most-developed and most-verified apparatus is the **bimetric**: the K=−1
purity/Poincaré metric `g_P` versus the K=+4 QFI/Bures metric `g_B`, with the balance at
γ\* = 2−√2. On the metriplectic reading these are not two competing distance notions to be
adjudicated — they are the **two operators of one GENERIC system**:

- `g_P` (K=−1) is the **Kähler metric of the reversible sector** — the one compatible with `ω` and
  `J`, the SU(1,1)-invariant geometry (6-2 §11.2 establishes SU(1,1) is its isometry group, *not* a
  Bures symmetry).
- `g_B`/QFI (K=+4) is the **dissipative metric** `M` — statistical distinguishability, which §4
  shows reproduces the speed limit.

Different metrics for the reversible and dissipative sides is *normal* in GENERIC (`L` and `M` are
independent). And the balance point is exactly where they reconcile:

> **|K_B| g_B = |K_P| g_P  ⟺  4 g_B = g_P  ⟹  γ² − 4γ + 2 = 0  ⟹  γ\* = 2 − √2**     [V]

So **γ\* — the framework's central forced number — is the point where the reversible-side metric
and the dissipative-side metric curvature-normalize to agree.** The bimetric balance the corpus
worked so hard to establish is the **balance of the metriplectic structure's two operators**. (The
QFI-vs-WY fork, O1 in 6-7 — whether the unit-curvature elliptic partner is QFI → 2−√2 or WY →
8−2√14 — becomes, on this reading, the question of *which* monotone metric is the physical `M`; the
QFI is selected by being the operational estimation/distinguishability metric that the speed limit
lives in, §4.)

---

## 6. The reversible Hamiltonian, and the (σ,t) plane as the degeneracy conditions [G/P; one check pending]

What §3–§5 verify is the **dissipative side** (the metric `M` = QFI, the dissipative potential
`S` = capacity/entropy, the balance γ\*) and the **J-conjugacy** to a reversible flow. To close the
GENERIC structure, two things remain, and both have a clear form:

**The reversible energy `E` [A/P].** The natural conserved Hamiltonian is the **mass-shell
invariant** `pq = x²u = sech²(2η)/4` (6-2 §11.2) — equivalently the SU(1,1) Casimir of the
coadjoint orbit. It is the *boostless-transport invariant*: the reactive, reversible motion that
stays on the hyperbola. For a genuine metriplectic system `E` and `S` must be **different**
functions (energy conserved, entropy produced); here `E` = the mass-shell Casimir and `S` = the
capacity are distinct, as required. (§3's use of the *same* `𝒞` for both flows is the special
"holomorphic" case that exhibits the J-conjugacy cleanly; the full flow pairs `E` = Casimir with
`S` = capacity.)

**The (σ,t) plane = the two degeneracy conditions [G/P].** The GENERIC degeneracies map onto the
framework's own conjugate axes:

- **`σ = ½` (detailed balance) ⟺ `M·δE = 0`** — the dissipative flow conserves the reactive energy.
  Off σ=½ (σ↔1−σ broken) is the **driven / non-equilibrium** regime where dissipation no longer
  conserves `E`.
- **`t = 0` (scale ⊥ shape; cascade associative) ⟺ `L·δS = 0`** — the reversible flow conserves the
  capacity/entropy. Off t=0 is the **frame-dragging** regime: 5-29 §6.2 *verifies* that turning on
  `t` produces exactly the Kerr `g_{tφ}` cross-term plus non-commuting would-be-Killing directions
  — i.e., the reversible and dissipative sectors are *dragged into each other*, which is precisely
  the relaxation of the degeneracy `L·δS = 0`.

So `(t=0, σ=½)` is the **clean GENERIC point** (both degeneracies hold = the standard
reversible/irreversible split, equilibrium and associative), and moving off it in either direction
relaxes one degeneracy — driven dynamics along σ, frame-dragging along t.

**The pending computation [O].** Pin `E` = the mass-shell Casimir explicitly on the disk and verify
the two degeneracy conditions hold at `(t=0, σ=½)` and relax linearly off it (the frame-dragging
half is already verified in 5-29; the σ half and the joint `E`/`S` degeneracy structure are the
remaining check). This is the step that would lift §6 from proposal to verified.

---

## 7. What it reaches, and what it does not

**It dissolves the "external import" objection [resolved].** `ω`, `M`, and `J` are all forced
internally; recognizing the framework as metriplectic is internal, not foreign.

**It resolves the 5-21 retraction [G→explained].** The dynamics thread retired the gradient flow
`ẋ = −ln(SNR)` as "the dynamics" and concluded "dynamics lives in the clock; one budget gives one
clock; you need two." Both are now explained: `ẋ = −ln(SNR)` is the **dissipative half** (the
gradient flow of the capacity, since `𝒞 = ln(1+SNR)`); its failure to be the whole story is the
metriplectic point — it needs its **J-conjugate reversible half**. The "two clocks" *are* the two
brackets, the symplectic and the dissipative, rotated by `J`. The retraction was a half-seen
metriplectic system.

**It upgrades `c` from kinematic to dynamical [G/P].** `c`-as-the-bound-on-rapidity was a kinematic
statement (6-2 §10.1). Here the reversible flow *preserves the bounded mass-shell* `pq = const`, so
the **equation of motion itself** bounds the rapidity — `c` is the boundedness of the symplectic
orbit, a property of the dynamics, not of a coordinate choice.

**It converts classification into selection [P].** The su(1,1) trichotomy classified admissible
flows; fixing `E` (mass-shell Casimir) and `S` (capacity) gives a *specific* equation of motion.

**It does NOT reach gravity or field equations [O — stated precisely].** The metriplectic flow is
the dynamics of *one* budget over *its own* state space — a point particle in information space.
Field equations require a metriplectic **field theory**: the budget structure varying over a base
manifold, with the base metric *sourced* by the budget. The genuine handhold is that the t≠0
frame-dragging regime already produces the Kerr `g_{tφ}` cross-term and non-commuting Killing
directions together — the algebraic signature of a *rotating gravitational source* — but that is the
dynamics of the **deformation**, not Einstein's equations. Gravity remains the frontier;
frame-dragging is the first structural toehold, not a crossing.

**It inherits the forced-vs-chosen residue in `E`, `S` [O].** The mass-shell Casimir and the
capacity are the *natural* generators, but proving they are *forced* (not merely natural) is the
floor's residue one level up. Mitigating this: the capacity's role as the J-conjugate dissipative
potential is *forced* once the budget's Kähler geometry is accepted (§3), and `M` = QFI is selected
by reproducing the independent speed limit (§4) — so the residue is narrow, concentrated in the
choice of the reactive Hamiltonian `E`.

---

## 8. The two checks (one passed, one pending) and the field-theory direction

The forward-directions note set the bar: a candidate functional must reproduce a *second*
independent dynamical fact.

- **Check 1 — PASSED [V].** The Mandelstam–Tamm purity speed limit is the QFI-gradient flow of the
  purity (`F = ¼|∇γ|²_QFI`, §4). Derived independently; reproduced here. This is what makes `M` =
  QFI a *forced* dissipative operator rather than a fitted one.
- **Check 2 — PENDING [O].** The **α discriminator**: `r* = tanh(2r*)` (`r* ≈ 0.9575`) is a
  self-consistent *rate* fixed point, so it should be a fixed point of the metriplectic flow, with
  the weak-coupling exponent (`√2−½ ≈ 0.9142` budget vs `r*² ≈ 0.9168` curved, a ~0.3% gap) a
  feature of the gradient rate near it. This is **HEOM-accessible** — the empirical leg of the
  "information-theoretic foundations" claim, and a genuine could-have-failed prediction once the
  operational definition of α and its error budget are pinned (the hygiene 6-9 II.2 requires).

**Next computational step.** Either (a) close §6 — pin `E` = mass-shell Casimir and verify the two
degeneracy conditions at `(t=0, σ=½)` with linear relaxation off it; or (b) run Check 2 — derive the
α exponent as the metriplectic gradient rate at the `r* = tanh(2r*)` fixed point and compare to the
HEOM value. (a) completes the structure; (b) tests it empirically.

**The field-theory direction (for gravity).** The single structural lead worth following toward the
field-equation frontier is the frame-dragging result: a metriplectic *field theory* in which the
base-manifold metric is sourced by the local budget's `t`-deformation would have the Kerr `g_{tφ}`
cross-term as its rotating-source solution. Whether the Einstein-like equation is the consistency
condition of such a sourcing is the open question; the toehold is verified, the field theory is not
built.

---

## 9. Provenance, attribution, and literature

**Grounded in the corpus (verified there) [G]:** the Kähler triple on the budget disk (6-9 I.10);
the (σ,t) geometric dictionary and the t≠0 frame-dragging verification (5-2; 5-29 §6) — a live
speculative sideline, not retracted; the cascade as path-sum / heat semigroup (5-29 §6.3; 6-9 T-3);
the bimetric `g_P`/`g_B` and γ\* = 2−√2 (6-2; 6-7); Chentsov–Petz forcing the metric (6-7 II.6); the
purity speed limit and `H_opt = iW/√F` (5-8; central reference 1.1).

**Verified this session [V]:** the budget/SNR/capacity bookkeeping; the metriplectic J-conjugate
split on the disk with `Δ_g 𝒞 = |K|` (§3); `F = ¼|∇γ|²_QFI`, the speed-limit-as-gradient-flow (§4,
the decisive check); γ\* = 2−√2 as the curvature-normalized two-metric balance (§5).

**My proposal/extrapolation [P]:** the synthesis that the framework's forced structures *are* a
metriplectic system — `L` from the K=−1 Kähler side, `M` from the K=+4 QFI side, the bimetric
balance = the two-operator balance, the (σ,t) plane = the two degeneracy conditions, the capacity =
dissipative potential, the mass-shell Casimir = reversible energy.

**Literature, honestly placed.** GENERIC (Grmela–Öttinger 1997), metriplectic dynamics (Morrison
1986), and information-geometric / Kähler quantum mechanics (Kibble; Ashtekar–Schilling;
Brody–Hughston — already cited in 6-9 I.10) are all established. The scoped contribution, *if* the
pending checks hold, is specific: the metriplectic structure arises **from the budget's forced
Kähler geometry**; the **capacity is the J-conjugate dissipative potential**; the **bimetric is the
two-operator structure with γ\* its balance**; and the **(σ,t) = (Markovianity, associativity) plane
is the degeneracy-condition deformation**, with frame-dragging its off-diagonal regime. The
disk computation, the speed-limit recovery, and the γ\* balance are the verified first pieces.

---

## Appendix — verification (reproducible)

All symbolic, sympy. Reproduces §0 bookkeeping, §3 split, §4 decisive check, §5 balance.

```python
import sympy as sp
r, th, g = sp.symbols('r theta gamma', positive=True)

# --- budget / SNR / capacity (x^2=S/(S+N), u=N/(S+N), SNR=x^2/u=x^2 G^2, 1+SNR=G^2=1/u) ---
x2=sp.Symbol('x2',positive=True); u_=1-x2; G2=1/u_; SNR=x2/u_
assert sp.simplify(1+SNR-G2)==0 and sp.simplify(SNR-x2*G2)==0
# capacity (nats) = ln(1+SNR) = ln G^2 = -ln u ;  bits: C/B = that/ln2
assert sp.simplify(sp.log(1+SNR) - sp.log(1/u_))==0   # = -ln u (sympy form: log(1/(1-x2)))

# --- metriplectic split on K=-1 Poincare disk; capacity C = -ln u = -ln(1-r^2) ---
E=4/(1-r**2)**2; Gm=4*r**2/(1-r**2)**2; Erm,Grm=1/E,1/Gm
C=-sp.log(1-r**2); sg=sp.sqrt(sp.simplify(E*Gm))
gradC_r=sp.simplify(Erm*sp.diff(C,r))                              # = r(1-r^2)/2 (radial)
lapC=sp.simplify((1/sg)*(sp.diff(sg*Erm*sp.diff(C,r),r)))          # = 1 = |K|
XC=sp.simplify(-gradC_r*sp.sqrt(E/Gm))                             # = -(1-r^2)/2 (d_theta)
assert sp.simplify(sp.diff(XC*sg,th))==0                           # L_X omega = 0  (reversible)
assert sp.simplify((1/sg)*sp.diff(sg*gradC_r,r))==1               # div(grad C)=1  (dissipative)
print("grad C =",gradC_r,"d_r ; Lap C =",lapC,"; X_C =",XC,"d_th (symplectic)")

# --- decisive check: MT speed limit F = 1/4 |grad gamma|^2_QFI ---
gamma=(1+r**2)/2; F=sp.simplify((2*gamma-1)*(1-gamma)/2)           # = r^2(1-r^2)/4
gradgam2_QFI=sp.simplify((1-r**2)*sp.diff(gamma,r)**2)             # QFI radial g^rr=(1-r^2)
assert sp.simplify(gradgam2_QFI/F)==4                              # F = 1/4 |grad gamma|^2_QFI
print("F =",F,"; |grad gamma|^2_QFI / F =",sp.simplify(gradgam2_QFI/F),"=> max|dgamma/dt|=2|grad gamma|_QFI")

# --- gamma* = 2-sqrt2 as the two-metric (K=-1 vs K=+4) balance ---
gB=1/(8*(2*g-1)*(1-g)); gP=1/(g**2*(1-g))
assert (2-sp.sqrt(2)) in [sp.simplify(s) for s in sp.solve(sp.Eq(4*gB,gP),g)]
print("4 g_B = g_P  ->  gamma* = 2 - sqrt(2)")
```

Output:
```
grad C = r*(1 - r**2)/2 d_r ; Lap C = 1 ; X_C = r**2/2 - 1/2 d_th (symplectic)
F = r**2*(1 - r**2)/4 ; |grad gamma|^2_QFI / F = 4 => max|dgamma/dt|=2|grad gamma|_QFI
4 g_B = g_P  ->  gamma* = 2 - sqrt(2)
```

*End of note. The dissipative side (metric, potential, balance, speed-limit recovery) is verified;
the reversible Hamiltonian and the degeneracy-condition checks are the stated pending work; gravity
is explicitly out of reach pending a metriplectic field theory. Endorsement weighting: the algebra
and the speed-limit recovery are machine-checked and stand independent of interpretation; the
metriplectic synthesis is a proposal whose value rests on the two checks of §8, one passed and one
pending.*
