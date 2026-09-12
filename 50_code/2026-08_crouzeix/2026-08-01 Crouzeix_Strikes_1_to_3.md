"""

STRIKE 1 — Crouzeix as a boundary-budget problem. 2026-08-01, seed 20260801\.

PREREGISTERED PREDICTIONS (written before first run):

  P1: the boundary POVM M (harmonic-measure operator density on an inflated

      contour around W(A)) is pointwise PSD with total mass 2I, for every test matrix.

  P2: at known extremals (scaled Jordan J2 with f=z; J3 with f=z^2), c \-\> 2/(1+eps)

      and the interference I(f,x\*) \-\> 0 (reflected channel silenced).

  P3: at optimizer-found maximizers on random 2x2/3x3/4x4, c \< 2 and I \>= 0 (alignment).

  P4: no maximizer found with I \< 0\.  \[Any P4 failure \= the discovery, not the failure.\]

LEMMA (exact, 3 lines): c^2 \+ I \= Re\<f(A)x, Tx\> \<= ||T|| c \<= 2c (sup|f|=1 on contour)

  \=\> I \<= c(2-c). Hence any Crouzeix violation (c\>2) REQUIRES destructive

  interference I \< 0 between the transmitted read f(A) and reflected read g(A)\*.

"""

import numpy as np

from scipy.optimize import minimize

rng \= np.random.default\_rng(20260801)

&nbsp;

def wboundary(A, m=720):

    th \= np.linspace(0, 2\*np.pi, m, endpoint=False)

    pts, nrm \= \[\], \[\]

    for t in th:

        H \= (np.exp(-1j\*t)\*A \+ np.exp(1j\*t)\*A.conj().T)/2

        w, V \= np.linalg.eigh(H)

        v \= V\[:, \-1\]

        pts.append(v.conj() @ A @ v)

        nrm.append(np.exp(1j\*t))

    return np.array(pts), np.array(nrm)

&nbsp;

def povm(A, eps=0.05, m=720):

    z, nu \= wboundary(A, m)

    sig \= z \+ eps\*nu                      \# inflated contour, ccw

    dsig \= (np.roll(sig, \-1) \- np.roll(sig, 1))/2

    n \= A.shape\[0\]

    Ms, cauchy \= \[\], np.zeros((n, n), complex)

    I\_ \= np.eye(n)

    for s, ds in zip(sig, dsig):

        R \= np.linalg.inv(s\*I\_ \- A)

        C \= R\*ds/(2j\*np.pi)

        cauchy \+= C

        Ms.append(C \+ C.conj().T)         \# dM \= 2 Re\[.\]

    Ms \= np.array(Ms)

    mass \= Ms.sum(axis=0)

    minev \= min(np.linalg.eigvalsh((M+M.conj().T)/2).min() for M in Ms)

    return sig, Ms, mass, cauchy, minev

&nbsp;

def cval\_and\_I(A, coef, sig, Ms):

    f\_b \= np.polyval(coef, sig)           \# f on contour

    sup \= np.abs(f\_b).max()

    if sup \< 1e-14: return 0.0, 0.0, None

    fA \= np.polyval(coef, A\[np.newaxis\]\[0\]) if False else None

    \# matrix polynomial:

    n \= A.shape\[0\]; fA \= np.zeros((n,n), complex)

    for c in coef: fA \= fA @ A \+ c\*np.eye(n)

    c \= np.linalg.norm(fA, 2)/sup

    T \= np.tensordot(f\_b, Ms, axes=(0,0))

    G \= T \- fA                            \# \= g(A)^\*

    U, S, Vh \= np.linalg.svd(fA)

    x \= Vh.conj().T\[:, 0\]                 \# maximizing unit vector

    Ival \= np.real(np.vdot(fA @ x, G @ x))/sup\*\*2

    Tnorm \= np.linalg.norm(T, 2)/sup

    return c, Ival, Tnorm

&nbsp;

def maximize\_c(A, deg=5, restarts=40, eps=0.05, m=720):

    sig, Ms, mass, cauchy, minev \= povm(A, eps, m)

    massdev \= np.linalg.norm(mass \- 2\*np.eye(A.shape\[0\]), 2\)

    cauchydev \= np.linalg.norm(cauchy \- np.eye(A.shape\[0\]), 2\)

    best \= (0, 0, None)

    def obj(v):

        coef \= v\[:deg+1\] \+ 1j\*v\[deg+1:\]

        c, \_, \_ \= cval\_and\_I(A, coef, sig, Ms)

        return \-c

    for k in range(restarts):

        v0 \= rng.standard\_normal(2\*(deg+1))

        r \= minimize(obj, v0, method='Nelder-Mead',

                     options={'maxiter': 4000, 'fatol': 1e-12, 'xatol': 1e-10})

        if \-r.fun \> best\[0\]:

            coef \= r.x\[:deg+1\] \+ 1j\*r.x\[deg+1:\]

            c, Ival, Tn \= cval\_and\_I(A, coef, sig, Ms)

            best \= (c, Ival, Tn)

    return best, minev, massdev, cauchydev

&nbsp;

def report(name, A, deg=5, restarts=40, eps=0.05):

    (c, Ival, Tn), minev, md, cd \= maximize\_c(A, deg, restarts, eps)

    ceil \= c\*(2-c)

    print(f"{name:28s} c={c:8.5f}  I={Ival:+10.6f}  ceiling c(2-c)={ceil:+9.6f}  "

          f"||T||/sup={Tn:7.5f}  minEig(M)={minev:+.2e}  |mass-2I|={md:.2e}  |Cauchy-I|={cd:.2e}")

    return c, Ival

&nbsp;

print("== P1/P2 exact-extremal validations \==")

J2 \= np.array(\[\[0,2\],\[0,0\]\], complex)

report("J2=\[\[0,2\],\[0,0\]\] (disk)", J2)

J3 \= np.array(\[\[0,1,0\],\[0,0,1\],\[0,0,0\]\], complex)

report("J3 nilpotent (disk r=cos45)", J3)

&nbsp;

print("\\n== P3/P4 random sweeps \==")

for i in range(4):

    A \= rng.standard\_normal((2,2)) \+ 1j\*rng.standard\_normal((2,2))

    report(f"random 2x2 \#{i+1}", A, restarts=30)

for i in range(4):

    A \= rng.standard\_normal((3,3)) \+ 1j\*rng.standard\_normal((3,3))

    report(f"random 3x3 \#{i+1}", A, restarts=30)

for i in range(2):

    A \= rng.standard\_normal((4,4)) \+ 1j\*rng.standard\_normal((4,4))

    report(f"random 4x4 \#{i+1}", A, restarts=25)

&nbsp;

print("\\n== near-extremal 3x3 family (Crabb-type, scaled) \==")

for a in \[0.8, 1.0, 1.2\]:

    C3 \= np.array(\[\[0,a,0\],\[0,0,a\],\[0,0,0\]\], complex)

    report(f"J3 scaled a={a}", C3, restarts=30)

&nbsp;

—-----------------

&nbsp;

"""

STRIKE 2a — the fold hunt (Will's Jacobian objection, 2026-08-01). Seed 20260802\.

PREREGISTERED: on thin ellipses (spectrum at the pointy foci \= tight corners of the

fitted sheet) with high-degree f (Chebyshev folds), Alignment predicts I \>= 0 at all

c-maximizers, with I shrinking as eccentricity grows. KILL: any I \< 0 at a maximizer.

Also: adversarial minimization of I among near-maximal-c polynomials.

"""

import numpy as np

from scipy.optimize import minimize

from numpy.polynomial import chebyshev as Ch

rng \= np.random.default\_rng(20260802)

&nbsp;

def wboundary(A, m=512):

    th \= np.linspace(0, 2\*np.pi, m, endpoint=False)

    pts, nrm \= \[\], \[\]

    for t in th:

        H \= (np.exp(-1j\*t)\*A \+ np.exp(1j\*t)\*A.conj().T)/2

        w, V \= np.linalg.eigh(H); v \= V\[:, \-1\]

        pts.append(v.conj() @ A @ v); nrm.append(np.exp(1j\*t))

    return np.array(pts), np.array(nrm)

&nbsp;

def povm(A, eps=0.05, m=512):

    z, nu \= wboundary(A, m)

    sig \= z \+ eps\*nu

    dsig \= (np.roll(sig, \-1) \- np.roll(sig, 1))/2

    n \= A.shape\[0\]; I\_ \= np.eye(n)

    Ms \= \[\]

    for s, ds in zip(sig, dsig):

        C \= np.linalg.inv(s\*I\_ \- A)\*ds/(2j\*np.pi)

        Ms.append(C \+ C.conj().T)

    Ms \= np.array(Ms)

    return sig, Ms

&nbsp;

def evalf(A, coef, sig, Ms):

    f\_b \= np.polyval(coef, sig); sup \= np.abs(f\_b).max()

    if sup \< 1e-13: return 0.0, 0.0

    n \= A.shape\[0\]; fA \= np.zeros((n,n), complex)

    for c in coef: fA \= fA @ A \+ c\*np.eye(n)

    c \= np.linalg.norm(fA, 2)/sup

    T \= np.tensordot(f\_b, Ms, axes=(0,0))

    x \= np.linalg.svd(fA)\[2\].conj().T\[:, 0\]

    Ival \= np.real(np.vdot(fA @ x, (T \- fA) @ x))/sup\*\*2

    return c, Ival

&nbsp;

def cheb\_seed(k, deg):

    ck \= np.zeros(k+1); ck\[k\] \= 1.0

    p \= Ch.cheb2poly(ck)

    coef \= np.zeros(deg+1, complex); coef\[-(len(p)):\] \= p\[::-1\]

    return coef

&nbsp;

def hunt(name, A, deg=12, restarts=30, eps=0.05):

    sig, Ms \= povm(A, eps)

    def cI(v):

        return evalf(A, v\[:deg+1\] \+ 1j\*v\[deg+1:\], sig, Ms)

    \# stage 1: maximize c (random \+ Chebyshev-fold seeds)

    best \= (0, 0, None)

    seeds \= \[np.concatenate(\[np.real(cheb\_seed(k, deg)), np.imag(cheb\_seed(k, deg))\])

             for k in range(2, deg+1, 2)\]

    seeds \+= \[rng.standard\_normal(2\*(deg+1)) for \_ in range(restarts)\]

    for v0 in seeds:

        r \= minimize(lambda v: \-cI(v)\[0\], v0, method='Nelder-Mead',

                     options={'maxiter': 3500, 'fatol': 1e-12})

        c, Iv \= cI(r.x)

        if c \> best\[0\]: best \= (c, Iv, r.x.copy())

    cmax, Imax, vbest \= best

    \# stage 2: adversarial — minimize I subject to c \>= 0.9 cmax

    worstI \= Imax

    for v0 in \[vbest \+ 0.15\*rng.standard\_normal(vbest.shape) for \_ in range(12)\] \+ \\

              \[rng.standard\_normal(2\*(deg+1)) for \_ in range(8)\]:

        r \= minimize(lambda v: cI(v)\[1\] \+ 60\*max(0, 0.9\*cmax \- cI(v)\[0\])\*\*2, v0,

                     method='Nelder-Mead', options={'maxiter': 3500, 'fatol': 1e-12})

        c, Iv \= cI(r.x)

        if c \>= 0.9\*cmax and Iv \< worstI: worstI \= Iv

    print(f"{name:34s} c\_max={cmax:7.4f}  I@max={Imax:+9.5f}  worst I (c\>=0.9c\_max)={worstI:+9.5f}  ceil={cmax\*(2-cmax):+8.5f}")

    return cmax, Imax, worstI

&nbsp;

print("== control \==")

hunt("J2 disk (control)", np.array(\[\[0,2\],\[0,0\]\], complex), deg=8, restarts=20)

print("== thin ellipses: foci \+-1, minor axis b (fitted-sheet corners) \==")

for b in \[1.0, 0.4, 0.15\]:

    A \= np.array(\[\[-1, b\],\[0, 1\]\], complex)

    hunt(f"ellipse 2x2 b={b}", A, deg=12, restarts=25)

print("== thin 3x3 / 4x4 (three/four eigenvalues under a thin sheet) \==")

for b in \[0.3, 0.12\]:

    A \= np.diag(\[-1, 0, 1\]).astype(complex); A\[0,1\] \= A\[1,2\] \= b

    hunt(f"thin 3x3 b={b}", A, deg=12, restarts=25)

A4 \= np.diag(\[-1, \-0.33, 0.33, 1\]).astype(complex)

for i in range(3): A4\[i, i+1\] \= 0.2

hunt("thin 4x4 b=0.2", A4, deg=12, restarts=20)

print("== raw Chebyshev fold-scaling on thinnest ellipse (no optimization) \==")

A \= np.array(\[\[-1, 0.15\],\[0, 1\]\], complex)

sig, Ms \= povm(A, 0.05)

for k in \[2, 4, 6, 8, 10, 12\]:

    c, Iv \= evalf(A, cheb\_seed(k, 12), sig, Ms)

    print(f"  T\_{k:2d}: c={c:7.4f}  I={Iv:+9.5f}")

&nbsp;

—-----------------

"""

STRIKE 2b' — off-disk healing \+ the climbing test. Seed 20260806\.

PREREGISTERED:

  P7 (off-disk): creases (I\<0 at near-maximizers) exist below the local summit on

     non-circular domains too; depth pinches toward the local summit, resolvable only

     down to the POVM noise floor (\~1e-5 at eps=0.025, m=768 — floor stated honestly).

  P8 (climbing heals): c-ascent started FROM a crease configuration raises I to \>= 0

     before reaching the summit; no path carries a crease to the top. This is the

     checkable face of the Maximizing-Crease Characterization (violation \<=\> a crease

     AT a maximizer above 2; see Delta 4).

"""

import numpy as np

from scipy.optimize import minimize

rng \= np.random.default\_rng(20260806)

&nbsp;

\# \---------- exact-disk machinery (nilpotent A) \----------

CIRC \= np.exp(2j\*np.pi\*np.arange(2048)/2048)

def ledger\_disk(A, r, coef):

    fb \= np.polyval(coef, r\*CIRC); sup \= np.abs(fb).max()

    if sup \< 1e-13: return None

    coef \= coef/sup

    n \= A.shape\[0\]; fA \= np.zeros((n,n), complex)

    for cc in coef: fA \= fA @ A \+ cc\*np.eye(n)

    c \= np.linalg.norm(fA, 2\)

    x \= np.linalg.svd(fA)\[2\].conj().T\[:, 0\]

    W \= coef\[-1\]\*np.conj(x.conj() @ fA @ x)

    return c, np.real(W)

&nbsp;

\# \---------- POVM machinery (general A) \----------

def povm(A, eps=0.025, m=768):

    th \= np.linspace(0, 2\*np.pi, m, endpoint=False)

    pts, nrm \= \[\], \[\]

    for t in th:

        H \= (np.exp(-1j\*t)\*A \+ np.exp(1j\*t)\*A.conj().T)/2

        w, V \= np.linalg.eigh(H); v \= V\[:, \-1\]

        pts.append(v.conj() @ A @ v); nrm.append(np.exp(1j\*t))

    sig \= np.array(pts) \+ eps\*np.array(nrm)

    dsig \= (np.roll(sig, \-1) \- np.roll(sig, 1))/2

    n \= A.shape\[0\]; Ms \= \[\]

    for s, ds in zip(sig, dsig):

        C \= np.linalg.inv(s\*np.eye(n) \- A)\*ds/(2j\*np.pi)

        Ms.append(C \+ C.conj().T)

    return sig, np.array(Ms)

def ledger\_povm(A, coef, sig, Ms):

    fb \= np.polyval(coef, sig); sup \= np.abs(fb).max()

    if sup \< 1e-13: return None

    coef \= coef/sup; fb \= fb/sup

    n \= A.shape\[0\]; fA \= np.zeros((n,n), complex)

    for cc in coef: fA \= fA @ A \+ cc\*np.eye(n)

    c \= np.linalg.norm(fA, 2\)

    T \= np.tensordot(fb, Ms, axes=(0,0))

    x \= np.linalg.svd(fA)\[2\].conj().T\[:, 0\]

    return c, np.real(np.vdot(fA @ x, (T \- fA) @ x))

&nbsp;

\# \---------- Part 1: off-disk creases \+ healing \----------

print("== P7: off-disk families (POVM, eps=0.025, m=768; noise floor \~1e-5) \==")

fams \= \[\]

A1 \= np.zeros((3,3), complex); A1\[0,1\]=A1\[1,2\]=1.0; A1 \+= 0.05\*np.diag(\[1,-0.5,-0.5\]); fams.append(("J3+0.05\*asym", A1, 8))

A2 \= np.zeros((3,3), complex); A2\[0,1\]=A2\[1,2\]=1.0; A2 \+= 0.15\*np.diag(\[1,-0.5,-0.5\]); fams.append(("J3+0.15\*asym", A2, 8))

A3 \= np.array(\[\[0,2\],\[0.5\*np.exp(1j\*np.pi/3),0\]\], complex); fams.append(("P(0.5,pi/3) 2x2", A3, 6))

for name, A, deg in fams:

    sig, Ms \= povm(A)

    def L(v): return ledger\_povm(A, v\[:deg+1\] \+ 1j\*v\[deg+1:\], sig, Ms)

    \# find local summit

    best \= 0; bv \= None

    for \_ in range(18):

        r \= minimize(lambda v: \-(L(v)\[0\] if L(v) else 0), rng.standard\_normal(2\*(deg+1)),

                     method='Nelder-Mead', options={'maxiter': 3000, 'fatol': 1e-12})

        if \-r.fun \> best: best, bv \= \-r.fun, r.x.copy()

    cmax \= best

    out \= \[f"{name}: c\_max\~{cmax:.4f} |"\]

    for frac in \[0.90, 0.95, 0.975\]:

        thr \= frac\*cmax; worst \= 1e9

        for \_ in range(16):

            r \= minimize(lambda v: (lambda q: (q\[1\] \+ 100\*max(0, thr \- q\[0\])\*\*2) if q else 1e6)(L(v)),

                         bv \+ 0.3\*rng.standard\_normal(bv.shape), method='Nelder-Mead',

                         options={'maxiter': 3000, 'fatol': 1e-13})

            q \= L(r.x)

            if q and q\[0\] \>= thr and q\[1\] \< worst: worst \= q\[1\]

        out.append(f"I\_min(c\>={frac:.3f}c\_max)={worst:+.2e}")

    print("  " \+ "  ".join(out))

&nbsp;

\# \---------- Part 2: climbing heals (exact disk, J3) \----------

print("== P8: climbing test (exact disk J3): ascend c from crease starts, track I \==")

A \= np.zeros((3,3), complex); A\[0,1\]=A\[1,2\]=1.0; r3 \= np.cos(np.pi/4); deg \= 8

def Ld(v):

    q \= ledger\_disk(A, r3, v\[:deg+1\] \+ 1j\*v\[deg+1:\])

    return q if q else (0, 0\)

\# find crease starts (c\>=1.85, I\<0)

starts \= \[\]

for \_ in range(40):

    rr \= minimize(lambda v: (lambda q: q\[1\] \+ 100\*max(0, 1.85 \- q\[0\])\*\*2)(Ld(v)),

                  rng.standard\_normal(2\*(deg+1)), method='Nelder-Mead',

                  options={'maxiter': 4000, 'fatol': 1e-14})

    c, Iv \= Ld(rr.x)

    if c \>= 1.85 and Iv \< \-1e-5: starts.append((Iv, c, rr.x.copy()))

starts.sort(); starts \= starts\[:3\]

for k, (I0, c0, v0) in enumerate(starts):

    traj \= \[\]

    def cb(vk): traj.append(Ld(vk))

    minimize(lambda v: \-Ld(v)\[0\], v0, method='Nelder-Mead', callback=cb,

             options={'maxiter': 6000, 'fatol': 1e-14})

    cs \= np.array(\[t\[0\] for t in traj\]); Is \= np.array(\[t\[1\] for t in traj\])

    crossed \= np.argmax(Is \>= 0\) if (Is \>= 0).any() else \-1

    cfin, Ifin \= cs\[-1\], Is\[-1\]

    if crossed \>= 0:

        print(f"  start {k}: (c={c0:.4f}, I={I0:+.2e}) \-\> I crosses \>=0 at c={cs\[crossed\]:.4f} \-\> ends (c={cfin:.4f}, I={Ifin:+.2e})")

    else:

        print(f"  start {k}: (c={c0:.4f}, I={I0:+.2e}) \-\> I NEVER crosses; ends (c={cfin:.4f}, I={Ifin:+.2e})  \[CREASE CARRIED\]")

&nbsp;

—-------

&nbsp;

"""

STRIKE 2c — exact-disk adversarial test of Alignment. Seed 20260804\.

On centered disks with nilpotent A, the reflection has CLOSED FORM: g(A)\* \= f(0)·I

(residue computation; no POVM, no quadrature error). So

    I(f,x) \= Re\[ f(0) \* conj( x\* f(A) x ) \],   x \= top right-singular vector of f(A).

PREREGISTERED:

  P6a (J2): I \>= 0 at EVERY (f, maximizer) — claimed as a two-line theorem found in

      design: x1 \= conj(a0) b / (lam \- |a0|^2) x2 forces the cross term positive:

      I \= |a0|^2 (1 \+ |b|^2 |x2|^2/(lam \- |a0|^2)) \>= 0, zero iff a0 \= 0 (Berger sector).

      Numerics must find min I \= 0 (at a0 \-\> 0), never negative.

  P6b (J3, J4): OPEN — conjectured I \>= 0 at near-maximizers (confidence \~0.6).

      A finding of I \< 0 with c \>= threshold \= THE CREASE: Alignment's clean form dies

      on the very domain where Crouzeix is a theorem, forcing the corridor restatement.

"""

import numpy as np

from scipy.optimize import minimize

rng \= np.random.default\_rng(20260804)

&nbsp;

def make(n):

    A \= np.zeros((n, n), complex)

    for i in range(n-1): A\[i, i+1\] \= 1.0

    r \= np.cos(np.pi/(n+1))     \# numerical radius of J\_n

    return A, r

&nbsp;

CIRC \= np.exp(2j\*np.pi\*np.arange(2048)/2048)

&nbsp;

def ledger\_disk(A, r, coef):

    zb \= r\*CIRC

    fb \= np.polyval(coef, zb); sup \= np.abs(fb).max()

    if sup \< 1e-13: return None

    coef \= coef/sup

    n \= A.shape\[0\]; fA \= np.zeros((n, n), complex)

    for cc in coef: fA \= fA @ A \+ cc\*np.eye(n)

    c \= np.linalg.norm(fA, 2\)

    x \= np.linalg.svd(fA)\[2\].conj().T\[:, 0\]

    a0 \= coef\[-1\]                       \# f(0), post-normalization

    W \= a0\*np.conj(x.conj() @ fA @ x)   \# f(0)\*conj(\<f(A)\>\_x): exact cross term

    return c, np.real(W), np.imag(W), abs(a0)

&nbsp;

def strike(n, deg, cthr, label, restarts=60):

    A, r \= make(n)

    def L(v): return ledger\_disk(A, r, v\[:deg+1\] \+ 1j\*v\[deg+1:\])

    \# sanity: c\_max via direct extremal f \= z^{n-1}

    ext \= np.zeros(deg+1); ext\[deg+1-n\] \= 1.0

    cext \= ledger\_disk(A, r, ext \+ 0j)\[0\]

    \# adversarial: minimize I subject to c \>= cthr

    worst \= (1e9, None)

    for k in range(restarts):

        v0 \= rng.standard\_normal(2\*(deg+1))

        rr \= minimize(lambda v: (lambda q: q\[1\] \+ 80\*max(0, cthr \- q\[0\])\*\*2)(L(v)),

                      v0, method='Nelder-Mead', options={'maxiter': 4000, 'fatol': 1e-13})

        q \= L(rr.x)

        if q\[0\] \>= cthr and q\[1\] \< worst\[0\]: worst \= (q\[1\], q)

    \# dense random scan at maximizer-agnostic points (for the J2 theorem check)

    scanmin \= 1e9

    for \_ in range(4000):

        v \= rng.standard\_normal(2\*(deg+1))

        q \= L(v)

        if q and q\[1\] \< scanmin: scanmin \= q\[1\]

    wI, q \= worst

    print(f"{label}: c\_extremal={cext:.5f} | adversarial (c\>={cthr}): "

          f"min I \= {wI:+.2e} (c={q\[0\]:.4f}, J={q\[2\]:+.2e}, |a0|={q\[3\]:.4f}) | "

          f"random-scan min I \= {scanmin:+.2e}")

&nbsp;

print("== P6a: J2 (theorem check: min I must be \>= 0, \-\>0 only via a0-\>0) \==")

strike(2, 6, 1.85, "J2 deg6")

print("== P6b: J3, J4 (open) \==")

strike(3, 8, 1.85, "J3 deg8")

strike(4, 8, 1.72, "J4 deg8")

&nbsp;

—-----------------

&nbsp;

"""

STRIKE 2c-2 — crease-depth profile. Seed 20260805\.

QUESTION: does the J3 crease heal as c \-\> 2 (I\_min(c) \-\> 0^-: benign, summit rigidity)

or stay open (bounded-negative corridor all the way up)?

PREREGISTERED: healing predicted (the cap on the disk is a theorem; the circle ledger

forces I \>= c(2-c)+... at the limit: at c \= 2 exactly, I \<= c(2-c) \= 0 AND the

saturated-circle/total-collapse structure should pinch I \-\> 0 from below too).

Depth profile: min I at c \>= {1.85, 1.90, 1.95, 1.98} for J3; J4 fixed with seeds.

"""

import numpy as np

from scipy.optimize import minimize

rng \= np.random.default\_rng(20260805)

CIRC \= np.exp(2j\*np.pi\*np.arange(2048)/2048)

&nbsp;

def make(n):

    A \= np.zeros((n, n), complex)

    for i in range(n-1): A\[i, i+1\] \= 1.0

    return A, np.cos(np.pi/(n+1))

&nbsp;

def ledger(A, r, coef):

    fb \= np.polyval(coef, r\*CIRC); sup \= np.abs(fb).max()

    if sup \< 1e-13: return None

    coef \= coef/sup

    n \= A.shape\[0\]; fA \= np.zeros((n, n), complex)

    for cc in coef: fA \= fA @ A \+ cc\*np.eye(n)

    c \= np.linalg.norm(fA, 2\)

    x \= np.linalg.svd(fA)\[2\].conj().T\[:, 0\]

    W \= coef\[-1\]\*np.conj(x.conj() @ fA @ x)

    return c, np.real(W), np.imag(W), abs(coef\[-1\])

&nbsp;

def probe(n, deg, cthr, restarts=50):

    A, r \= make(n)

    ext \= np.zeros(2\*(deg+1)); ext\[deg+1-n\] \= 1.0     \# f \= z^{n-1} seed (real part slot)

    def L(v): return ledger(A, r, v\[:deg+1\] \+ 1j\*v\[deg+1:\])

    def obj(v):

        q \= L(v)

        if q is None: return 1e6

        return q\[1\] \+ 120\*max(0, cthr \- q\[0\])\*\*2

    worst \= (1e9, None)

    seeds \= \[ext \+ 0.25\*rng.standard\_normal(ext.shape) for \_ in range(restarts//2)\] \+ \\

            \[rng.standard\_normal(2\*(deg+1)) for \_ in range(restarts//2)\]

    for v0 in seeds:

        rr \= minimize(obj, v0, method='Nelder-Mead',

                      options={'maxiter': 4500, 'fatol': 1e-14})

        q \= L(rr.x)

        if q and q\[0\] \>= cthr and q\[1\] \< worst\[0\]: worst \= (q\[1\], q)

    if worst\[1\] is None:

        print(f"  J{n} c\>={cthr}: no config found above threshold"); return

    wI, q \= worst

    print(f"  J{n} c\>={cthr:.2f}: min I \= {wI:+.3e}  (c={q\[0\]:.4f}, J={q\[2\]:+.1e}, |a0|={q\[3\]:.4f})")

&nbsp;

print("== J3 crease-depth profile \==")

for cthr in \[1.85, 1.90, 1.95, 1.98\]:

    probe(3, 8, cthr)

print("== J4 (fixed, seeded) \==")

for cthr in \[1.75, 1.85\]:

    probe(4, 8, cthr, restarts=40)

&nbsp;