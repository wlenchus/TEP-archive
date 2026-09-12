"""

Full port ledger at maximizers (Will's rotation/absorption question, 08-01).

For each c-maximizer measure: I \= Re\<fAx, g\*x\> (interference), J \= Im\<...\> (rotated/

reactive), u\_eff \= 1 \- ||Tx||^2/4 (total deficit: dilation leak \+ spectral detuning).

EXACT constraint to verify: (c^2+I)^2 \+ J^2 \<= 4 c^2 (1 \- u\_eff)   \[circle ledger\]

Prediction: at extremals (c-\>2): I,J,u\_eff all \-\> 0 (total channel collapse into

pure aligned transmission \= seam/jet configuration); rotation and absorption both

TAX a would-be violator (they shrink the room, never open it).

"""

import numpy as np

from scipy.optimize import minimize

rng \= np.random.default\_rng(20260803)

&nbsp;

def povm(A, eps=0.05, m=512):

    th \= np.linspace(0, 2\*np.pi, m, endpoint=False)

    pts, nrm \= \[\], \[\]

    for t in th:

        H \= (np.exp(-1j\*t)\*A \+ np.exp(1j\*t)\*A.conj().T)/2

        w, V \= np.linalg.eigh(H); v \= V\[:, \-1\]

        pts.append(v.conj() @ A @ v); nrm.append(np.exp(1j\*t))

    z, nu \= np.array(pts), np.array(nrm)

    sig \= z \+ eps\*nu

    dsig \= (np.roll(sig, \-1) \- np.roll(sig, 1))/2

    n \= A.shape\[0\]; I\_ \= np.eye(n); Ms \= \[\]

    for s, ds in zip(sig, dsig):

        C \= np.linalg.inv(s\*I\_ \- A)\*ds/(2j\*np.pi)

        Ms.append(C \+ C.conj().T)

    return sig, np.array(Ms)

&nbsp;

def ledger(A, coef, sig, Ms):

    f\_b \= np.polyval(coef, sig); sup \= np.abs(f\_b).max()

    if sup \< 1e-13: return None

    coef \= coef/sup; f\_b \= f\_b/sup           \# normalize sup|f|=1

    n \= A.shape\[0\]; fA \= np.zeros((n,n), complex)

    for cc in coef: fA \= fA @ A \+ cc\*np.eye(n)

    c \= np.linalg.norm(fA, 2\)

    T \= np.tensordot(f\_b, Ms, axes=(0,0))

    x \= np.linalg.svd(fA)\[2\].conj().T\[:, 0\]

    W \= np.vdot(fA @ x, (T \- fA) @ x)        \# complex cross term

    Iv, Jv \= np.real(W), np.imag(W)

    Tx \= np.linalg.norm(T @ x)

    ueff \= 1 \- Tx\*\*2/4

    lhs \= (c\*\*2 \+ Iv)\*\*2 \+ Jv\*\*2

    rhs \= 4\*c\*\*2\*(1 \- ueff)

    return c, Iv, Jv, ueff, lhs, rhs

&nbsp;

def run(name, A, deg=5, restarts=15):

    sig, Ms \= povm(A)

    def negc(v):

        L \= ledger(A, v\[:deg+1\] \+ 1j\*v\[deg+1:\], sig, Ms)

        return \-(L\[0\] if L else 0\)

    best, bv \= 0, None

    for \_ in range(restarts):

        r \= minimize(negc, rng.standard\_normal(2\*(deg+1)), method='Nelder-Mead',

                     options={'maxiter': 3000, 'fatol': 1e-11})

        if \-r.fun \> best: best, bv \= \-r.fun, r.x.copy()

    c, Iv, Jv, ueff, lhs, rhs \= ledger(A, bv\[:deg+1\] \+ 1j\*bv\[deg+1:\], sig, Ms)

    ok \= "OK " if lhs \<= rhs \+ 1e-9 else "VIOLATED"

    print(f"{name:26s} c={c:7.4f}  I={Iv:+9.5f}  J(rot)={Jv:+9.5f}  u\_eff(abs)={ueff:+8.5f}  circle:{ok} (lhs={lhs:8.4f} rhs={rhs:8.4f})")

&nbsp;

run("J2=\[\[0,2\],\[0,0\]\] extremal", np.array(\[\[0,2\],\[0,0\]\], complex))

run("J3 nilpotent extremal",     np.array(\[\[0,1,0\],\[0,0,1\],\[0,0,0\]\], complex))

A \= rng.standard\_normal((3,3)) \+ 1j\*rng.standard\_normal((3,3)); run("random 3x3", A)

run("ellipse 2x2 b=0.4", np.array(\[\[-1, .4\],\[0, 1\]\], complex))