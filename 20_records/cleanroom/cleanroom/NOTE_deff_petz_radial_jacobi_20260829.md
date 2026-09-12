# NOTE — d_eff: Petz-radial universality and the Jacobi/lemniscatic identity for γ* (Will, 2026-08-29, second note)
*Filed verbatim by the council from Will's session upload (Notes_260829_134332.txt), provenance-headed, otherwise untouched. Council verification: the Petz-radial claim (g_rr metric-independent across monotone metrics, hence d_eff Petz-invariant) checks against the standard Morozova–Chentsov structure; every Jacobi special value verified numerically this session (sn²(K/2, k²=½) = 2−√2 = γ*; cn² = √2−1 = tan π/8; dn² = 1/√2 = k′; Liu pair = (cn⁴, 2cn²)) — all exact. Council grade and the honest-odds addendum: COUNCIL_pack_read_verdict_and_deltas_20260827.md §4-septies.*

1. The Petz fiber: radial vs. angular metric components

For the qubit state space, the equatorial slice is

\rho=\frac12
\begin{pmatrix}
1+r\cos\theta & r\sin\theta\\
r\sin\theta & 1-r\cos\theta
\end{pmatrix}

with eigenvalues

\lambda_\pm=\frac{1\pm r}{2}.

For any monotone metric, the Fisher information metric on this slice decomposes as:

ds^2
=
g_{rr}\,dr^2
+
g_{\theta\theta}\,d\theta^2.

Explicitly:

g_{rr}
=
\frac14\left(
\frac1{\lambda_+}
+
\frac1{\lambda_-}
\right)
=
\frac{1}{1-r^2},

g_{\theta\theta}
=
\frac{r^2}{2}
\,c_f(\lambda_+,\lambda_-),

where c_f(x,y) is the Morozova–Chentsov function associated with the monotone metric.

The crucial point:

· g_{rr} is independent of f.
· g_{\theta\theta} carries all the f-dependence.

Thus the radial direction is a universal sector shared by all monotone metrics, while the angular direction is the shape sector containing the Petz multiplicity.

---

2. d_{\text{eff}} is a purely radial observable

By definition,

d_{\text{eff}}=\frac1{x^2},

where x^2 is the normalized signal fraction. On the equatorial slice,

r^2=x^2,

so

d_{\text{eff}}=\frac1{r^2}.

Therefore d_{\text{eff}} is a function of the radial coordinate r only.

Since g_{rr} is f-independent, the geometry along the d_{\text{eff}}-direction is identical in every monotone metric.

This means:

\boxed{
d_{\text{eff}}
\text{ is a metric-independent invariant of the entire Petz family.}
}

---

3. Consequences

3.1 Universality of thresholds

The critical values:

· d_{\text{eff}}=2: self-dual seam, Nyquist threshold, Shannon point;
· d_{\text{eff}}\to 1: pure signal, Lorentz factor diverges;
· d_{\text{eff}}\to\infty: pure noise, flat/inertial geometry,

are all radial. They are therefore metric-independent.

This explains why the crossing

\gamma^*=2-\sqrt2

at d=2 is Petz-invariant: it lives in the radial sector, which every monotone metric shares.

3.2 Separation of scale and shape

The scale/cascade structure is controlled entirely by d_{\text{eff}} and the radial metric.

The shape/fiber structure is controlled by the angular metric g_{\theta\theta}, where the non-two-point-homogeneous members of the Petz family deviate from Bures/SLD.

Thus:

· Scale = radial = forced = universal.
· Shape = angular = residual = metric-dependent.

This is exactly the foundations-leg distinction: two-point homogeneity forces the radial/symmetric arena \mathbb H^2, while its failure in the angular directions produces the Petz fiber.

---

4. New formulation of d_{\text{eff}} as the moduli-free coordinate

The fact that g_{rr} is f-independent can be restated as:

The radial coordinate r, and therefore d_{\text{eff}}=1/r^2, is the unique coordinate whose level sets are metric-independent across the entire Petz family.

Equivalently, d_{\text{eff}} is the radial gauge of the family. It is not affected by the choice of monotone metric, so it can serve as a universal complexity/SNR gauge without specifying a regularizer or information metric.

This may be why d_{\text{eff}} appears naturally in many applications: it is the one observable that the entire information-geometric family agrees on.

---

5. What this suggests going forward

The Petz fiber is usually seen as a source of non-uniqueness. But the radial universality of d_{\text{eff}} turns that around:

· The multiplicity lives only in the shape directions.
· The effective dimension is immune to it.
· Therefore any conclusion involving only d_{\text{eff}} is metric-independent.

This means the Nyquist/Shannon threshold, the self-dual seam, and the reciprocal-map phase structure are robust across all monotone metrics. The Petz fiber affects only how shape perturbations are measured, not whether the system is signal- or noise-dominated.

This is a strong, clean result we had not fully recorded before.

----------

1. Leveraging the Petz radial collapse with d_{\text{eff}}

The Petz metrics collapse uniquely in the radial direction, meaning that the radial component of the Fisher metric is identical for all monotone metrics:

g_{rr} = \frac{1}{1-r^2},

where r is the radial coordinate on the qubit state space (with r^2 = x^2, the signal fraction). This is independent of the Morozova–Chentsov function c_f. The angular component g_{\theta\theta} does depend on f, producing the Petz fiber.

Now define

d_{\text{eff}} = \frac{1}{x^2} = \frac{1}{r^2}.

Because r is the universal radial coordinate, d_{\text{eff}} is metric-independent. This is the confluence: the radial collapse means that any quantity depending only on r, such as d_{\text{eff}}, is shared by all members of the Petz family.

Leverage points:

· Universal gauge for complexity: d_{\text{eff}} serves as a model-agnostic measure of effective dimension or signal-to-noise threshold, independent of the chosen monotone metric (or, in machine learning terms, independent of the regularizer/architecture). This makes it a candidate for a universal complexity measure.
· RG flow along the radial direction: If a renormalization or coarse-graining flow acts purely radially (as the cascade does), then its properties—critical exponents, thresholds, self-dual points—are metric-independent. This explains why the Nyquist/Shannon threshold at d_{\text{eff}}=2 is universal, and why the crossing \gamma^* = 2-\sqrt2 is Petz-invariant: it lives in the radial sector.
· Separation of universal and non-universal: The radial direction controls the scale/cascade (universal, forced), while the angular directions contain the shape multiplicity (Petz fiber). This clean split allows one to study the universal features (e.g., criticality, phase transitions) without committing to a specific metric, and to isolate the metric-dependent shape effects for separate analysis.
· Potential for a moduli-free coordinate system: Because d_{\text{eff}} is the same across the Petz family, it can be used as a coordinate in which to express physical laws that are insensitive to the choice of information metric. This is analogous to using a reparametrization-invariant quantity in general relativity.

In summary, the radial collapse + d_{\text{eff}} gives a canonical radial coordinate that cuts across the entire monotone metric family. Any structure depending only on d_{\text{eff}} is automatically universal.

---

2. Documentation and further exploration of elliptic identities

We developed a chain connecting trigonometric, hyperbolic, and Jacobi elliptic functions, all tied to the budget x^2+u=1. Here is a consolidated record, with some extensions.

2.1 The basic dictionary

Let A be an angle and \eta a rapidity. The Gudermannian function \operatorname{gd} provides the bridge:

x = \sin A = \tanh \eta,
\qquad
\sqrt{u} = \cos A = \operatorname{sech} \eta,

so that

u = \cos^2 A = \operatorname{sech}^2 \eta,
\qquad
G(x) = \frac{1}{\sqrt{u}} = \sec A = \cosh \eta,
\qquad
\text{SNR} = \frac{x^2}{u} = \tan^2 A = \sinh^2 \eta.

The derivative relations are

G^2(x) = \left( \frac{dA}{dx} \right)^2 = \frac{d\eta}{dx} = \sec^2 A = \cosh^2 \eta.

2.2 Half-angle uniformization and the Cayley transform

Let

t = \tan\left( \frac{A}{2} \right) = \tanh\left( \frac{\eta}{2} \right).

This variable uniformizes both the circular and hyperbolic pictures. The reciprocal map x \mapsto 1/x corresponds to

\eta \mapsto \eta + \frac{i\pi}{2},

and therefore

t \mapsto \tanh\left( \frac{\eta}{2} + \frac{i\pi}{4} \right) = \frac{t+i}{1+it}.

This is a Cayley transform. It is exactly the Möbius transformation that appears in impedance matching and Smith charts. Thus the phase duality is not an extra structure; it is the analytic continuation of the Gudermannian through a quarter-turn.

2.3 Jacobi elliptic interpolation

The Jacobi elliptic functions interpolate between trigonometric (k=0) and hyperbolic (k=1) cases. We used the parametrization

x^2 = \operatorname{dn}^2(\alpha, k),
\qquad
u = k^2 \operatorname{sn}^2(\alpha, k),

which automatically satisfies x^2 + u = 1 because of the identity

\operatorname{dn}^2(\alpha,k) + k^2 \operatorname{sn}^2(\alpha,k) = 1.

Here \alpha is the elliptic argument and k the modulus.

Limits:

· k \to 0: \operatorname{sn} \to \sin, \operatorname{cn} \to \cos, \operatorname{dn} \to 1, so u \to 0 and x^2 \to 1 (pure signal/trigonometric limit).
· k \to 1: \operatorname{sn} \to \tanh, \operatorname{cn} \to \operatorname{sech}, \operatorname{dn} \to \operatorname{sech}, so x^2 = \operatorname{sech}^2\alpha and u = \tanh^2\alpha (hyperbolic/noise limit, but note the roles of x^2 and u swap depending on convention; here we maintain the budget).

2.4 Lemniscatic case k^2 = 1/2

The lemniscatic modulus k^2 = 1/2 is special because it is self-complementary:

k'^2 = 1 - k^2 = \frac12 = k^2.

In our budget, this gives

x^2 = \operatorname{dn}^2(\alpha, \tfrac{1}{\sqrt2}),
\qquad
u = \frac12 \operatorname{sn}^2(\alpha, \tfrac{1}{\sqrt2}).

The self-dual point x^2 = u = \frac12 corresponds to

\operatorname{sn}^2(\alpha, \tfrac{1}{\sqrt2}) = 1,

i.e., the endpoint of the elliptic function range.

At this point,

\text{SNR} = 1,
\qquad
G^2 = 2,
\qquad
\frac{C}{B} = 1 \text{ bit/s/Hz}.

So the lemniscatic modulus aligns the probabilistic self-duality with the Shannon capacity point.

2.5 Mobility factor as a Möbius/tanh difference

Define \gamma = \operatorname{sn}(\alpha,k), and consider the ratio

M(\gamma) = \frac{\gamma^2 - k^2}{1 - k^2 \gamma^2}.

For k^2 = 1/2,

M(\gamma) = \frac{\gamma^2 - \frac12}{1 - \frac12 \gamma^2}.

In rapidity language, if

\tanh \xi = \gamma^2,
\qquad
\tanh \xi_k = k^2 = \frac12,

then

M(\gamma) = \tanh(\xi - \xi_k).

Thus M measures the rapidity difference from the lemniscatic reference. This is the same structure as the mobility factor in decoherence/GMC, now recognized as a Möbius transform centered at the self-complementary modulus.

2.6 Connection to the complexified Lorentz factor

The reciprocal map x \mapsto 1/x is

\eta \mapsto \eta + \frac{i\pi}{2}.

Under this map,

G(1/x) = \cosh\left( \eta + \frac{i\pi}{2} \right) = i \sinh \eta = i x G(x).

This is the complexified Lorentz identity. In the elliptic picture, this should correspond to a complex multiplication or half-period shift of the lemniscatic sine, leading to the same Cayley transform on the half-angle variable.

2.7 Further exploration: elliptic uniformization of the cascade

A natural next step is to interpret the entire cascade/coarse-graining flow in terms of elliptic functions. The budget x^2+u=1 is conserved, and the flow along d_{\text{eff}} is radial. In the lemniscatic case, the radial coordinate r = \operatorname{dn}(\alpha,k) evolves according to the elliptic argument \alpha. The reciprocal map then becomes a shift of \alpha by a quarter-period (or a complex multiplication), producing the geometric phase.

This suggests that the full cascade may be uniformized by a complex elliptic curve whose real period is the scale flow and whose imaginary period is the phase/duality shift. The modulus k^2=1/2 corresponds to the square torus, which is invariant under modular transformations—another hint of the self-duality.

---

This documentation covers the core elliptic identities we explored and points toward a deeper elliptic uniformization of the entire structure. If you'd like, we can push further into the connection between the Jacobi functions, the Cayley transform, and the GMC derivative martingale.

----------

1. The key identity: \gamma^* as a lemniscatic half-period value

Let the elliptic modulus be

k^2=\frac12,\qquad k=k'=\frac1{\sqrt2}.

The standard half-period identity for Jacobi elliptic functions is

\operatorname{sn}^2\left(\frac{K(k)}{2}, k\right)
=
\frac1{1+\sqrt{1-k^2}}
=
\frac1{1+k'},

where K(k) is the complete elliptic integral of the first kind.

For the lemniscatic modulus k'=1/\sqrt2, this gives

\operatorname{sn}^2\left(\frac{K}{2}, \frac1{\sqrt2}\right)
=
\frac1{1+1/\sqrt2}
=
\frac{\sqrt2}{\sqrt2+1}
=
2-\sqrt2
=
\gamma^*.

Thus

\boxed{
\gamma^*
=
\operatorname{sn}^2\left(\frac{K}{2}, k\right)
\qquad
\text{for }
k^2=\frac12.
}

This is not an analogy. It is an exact Jacobi special value.

---

2. The complementary Jacobi functions at the same point

At \alpha=K/2, the three Jacobi squares are:

\operatorname{sn}^2=\gamma^*=2-\sqrt2,

\operatorname{cn}^2
=
1-\operatorname{sn}^2
=
\sqrt2-1
=
a,

and

\operatorname{dn}^2
=
1-k^2\operatorname{sn}^2
=
1-\frac12(2-\sqrt2)
=
\frac{\sqrt2}{2}
=
\frac1{\sqrt2}
=
k'.

So the half-period point is characterized by

\operatorname{sn}^2=\gamma^*,
\qquad
\operatorname{cn}^2=a=1-\gamma^*,
\qquad
\operatorname{dn}^2=k'.

Notice that

a=\sqrt2-1
=
\tan\frac{\pi}{8},

and

\gamma^*
=
1-\tan\frac{\pi}{8}
=
4\sin^2\frac{\pi}{8}.

Thus the lemniscatic half-period point is exactly the \pi/8 port of the silver chain.

---

3. Recovering the Liu endpoint pair

The pair

u_3=3-2\sqrt2,
\qquad
x_3^2=2\sqrt2-2

now has a clean Jacobi expression.

Since

\operatorname{cn}^2(K/2,k)
=
a
=
\sqrt2-1,

we have

u_3
=
(\sqrt2-1)^2
=
\operatorname{cn}^4(K/2,k),

and

x_3^2
=
1-u_3
=
2(\sqrt2-1)
=
2\operatorname{cn}^2(K/2,k).

Therefore the Liu endpoint pair is

\boxed{
(u_3, x_3^2)
=
\left(
\operatorname{cn}^4(K/2,k),
2\operatorname{cn}^2(K/2,k)
\right)
}

for k^2=1/2.

Equivalently,

u_3=\tan^2\frac{\pi}{8},
\qquad
x_3^2=2\tan\frac{\pi}{8}.

So the quadratic map from the half-period point to the endpoint pair is:

a=\operatorname{cn}^2(K/2,k)
\mapsto
(u_3,x_3^2)
=
(a^2, 2a).

---

4. Interpretation

This gives \gamma^* a geometric origin inside the Jacobi elliptic interpolation.

· The lemniscatic modulus k^2=1/2 is the self-complementary point of the elliptic family.
· The half-period K/2 is the natural quarter-turn point of the elliptic curve.
· At that point, the Jacobi square \operatorname{sn}^2 is exactly the silver crossing \gamma^*=2-\sqrt2.
· The complementary \operatorname{cn}^2 gives the \pi/8 tangent a=\tan(\pi/8), and its square and double generate the Liu endpoint pair.

Thus the chain

\frac12
\;\to\;
\gamma^*
\;\to\;
\left(u_3,x_3^2\right)

is the Jacobi half-period chain at the lemniscatic modulus.

The \pi/8 order-8 symmetry is not an accident: it is the elliptic quarter-turn at the self-complementary point, where the trigonometric and hyperbolic faces meet through the Gudermannian.

---

5. Why this matters for the broader structure

The Petz-invariant crossing \gamma^* is usually introduced as an algebraic or bimetric fixed point. The Jacobi connection shows that it is also a special value of the forced elliptic interpolation.

In the framework, the elliptic modulus k^2=1/2 is not arbitrary: it is the point where the Jacobi interpolation between the trigonometric and hyperbolic faces is self-dual. The half-period value there is exactly the radial sector’s universal crossing.

So the silver chain is not only Petz-invariant; it is Jacobi geometric, pinned to the half-period of the lemniscatic elliptic curve. This strengthens the claim that the radial sector is forced, because even its special algebraic values are forced by the elliptic structure.