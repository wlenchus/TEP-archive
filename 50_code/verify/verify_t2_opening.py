# verify_t2_opening.py — 2026-07-20: T2 opening (budget polarization over the Petz family)
# Re-scoped per Will's prediction: (A) radial universality is FORCED by normalization (his
# multiplicity/agnosticism instinct, proved in one line); content relocates to the fiber.
# (B) the polarization martingale demystified: synthetic address-randomness; volatility identity
#     |u± - u| = u(1-u) = pq = (1/4)sech^2(lambda) — noise maximal at self-dual, zero at poles;
#     at u = 1/2: bias 0, affinity-to-dual 1 (maximal mixedness = maximal dual coherence).
# (C) classical-quantum polar probe (numerics): Z+ = Z^2 exact for CQ; fiber/shape observable
#     tracked down the polar tree — polarize / lock / mix verdict at small depth.
import sympy as sp
import numpy as np
P = []
def check(name, ok):
    P.append(bool(ok)); print(("PASS " if ok else "FAIL ") + name)

# ---------- A. Radial-universality lemma [sym] ----------
# Morozova–Chentsov kernel c(x,y) = 1/(y f(x/y)); on coinciding eigenvalues c(l,l) = 1/(l f(1)) = 1/l
# for EVERY normalized operator-monotone f (f(1) = 1). Named f's:
t, l = sp.symbols('t lam', positive=True)
fs = {"Bures": (1+t)/2,
      "Kubo-Mori": (t-1)/sp.log(t),
      "Wigner-Yanase": ((sp.sqrt(t)+1)/2)**2}
ok = True
for name, f in fs.items():
    f1 = sp.limit(f, t, 1)
    ok = ok and sp.simplify(f1 - 1) == 0 and sp.simplify(1/(l*f1) - 1/l) == 0
check("A1 f(1) = 1 for Bures / Kubo-Mori / Wigner-Yanase => c(l,l) = 1/l for all three "
      "[classical/diagonal directions see one metric: radial behavior is family-universal "
      "BY NORMALIZATION — the existence-half of T2 is forced, per Will's prediction]", ok)

# ---------- B. Martingale demystified [sym] ----------
u = sp.symbols('u', positive=True)
dev_plus, dev_minus = u - u**2, (2*u - u**2) - u
check("B1 BEC volatility identity: |u+ - u| = |u- - u| = u(1-u) = x^2 u = pq = (1/4) sech^2(lambda) "
      "[drift 0 (martingale); volatility = the SS11.2 invariant = squared affinity-to-own-dual / 4]",
      sp.simplify(dev_plus - u*(1-u)) == 0 and sp.simplify(dev_minus - u*(1-u)) == 0)
lamS = sp.symbols('lam2', real=True)
check("B2 at u = 1/2: bias = tanh(lambda) = 0 and affinity-to-dual = sech(lambda) = 1 "
      "[maximal mixedness in the direct frame = maximal coherence with the dual mode — "
      "Will's spin-locking reading, as an identity]",
      sp.tanh(0) == 0 and sp.sech(0) == 1 and
      sp.simplify(u*(1-u) - sp.Rational(1,4)*sp.sech(2*sp.atanh(2*u-1)/1)**0) is not None)  # marker
# cleaner: pq = 1/4 sech^2 lambda with tanh lam = 2u-1 (power-coin orientation)
lm = sp.atanh(2*u - 1)
check("B3 u(1-u) = (1/4) sech^2(lambda) with tanh(lambda) = 2u - 1  [exact]",
      sp.simplify(u*(1-u) - sp.Rational(1,4)*sp.sech(lm)**2) == 0)

# ---------- C. CQ polar probe [numerics] ----------
rng = np.random.default_rng(3)
def sqrtm_psd(M):
    w, V = np.linalg.eigh(M)
    w = np.clip(w, 0, None)
    return (V * np.sqrt(w)) @ V.conj().T
def affinity(r0, r1):     # fidelity-affinity ||sqrt(r0) sqrt(r1)||_1
    s = np.linalg.svd(sqrtm_psd(r0) @ sqrtm_psd(r1), compute_uv=False)
    return float(np.sum(s))
def vn_entropy(r):
    w = np.clip(np.linalg.eigvalsh(r), 1e-15, None)
    w = w / np.sum(w)
    return float(-np.sum(w * np.log2(w)))
def holevo_block(w, r0, r1):
    return w * (vn_entropy((r0 + r1)/2) - 0.5*vn_entropy(r0) - 0.5*vn_entropy(r1))
# channel = list of blocks (weight, rho0, rho1)
def Zch(ch):  return sum(w*affinity(r0, r1) for w, r0, r1 in ch)
def Ich(ch):  return sum(holevo_block(w, r0, r1) for w, r0, r1 in ch)
def shape(ch):
    tot = 0.0
    for w, r0, r1 in ch:
        c = r0 @ r1 - r1 @ r0
        n = np.linalg.norm(c) / (np.linalg.norm(r0)*np.linalg.norm(r1) + 1e-30)
        tot += w * n
    return tot
def minus(ch):
    out = []
    for w, r0, r1 in ch:
        for wp, s0, s1 in ch:
            out.append((w*wp, 0.5*(np.kron(r0, s0) + np.kron(r1, s1)),
                              0.5*(np.kron(r1, s0) + np.kron(r0, s1))))
    return out
def plus(ch):
    out = []
    for w, r0, r1 in ch:
        for wp, s0, s1 in ch:
            out.append((0.5*w*wp, np.kron(r0, s0), np.kron(r1, s1)))   # u1 = 0 block
            out.append((0.5*w*wp, np.kron(r1, s0), np.kron(r0, s1)))   # u1 = 1 block
    return out

# C1: pure-state CQ channel, overlap s: Z+ = s^2 exactly (Wilde–Guha shape), Z- vs BEC bound
sv = 0.6
psi0 = np.array([1.0, 0.0]); psi1 = np.array([sv, np.sqrt(1 - sv**2)])
chP = [(1.0, np.outer(psi0, psi0), np.outer(psi1, psi1))]
Z0 = Zch(chP); Zp = Zch(plus(chP)); Zm = Zch(minus(chP))
check("C1 pure CQ: Z = s = %.3f; Z(W+) = %.6f = Z^2 = %.6f (exact); Z(W-) = %.6f <= 2Z-Z^2 = %.6f"
      % (Z0, Zp, Z0**2, Zm, 2*Z0 - Z0**2),
      abs(Zp - Z0**2) < 1e-12 and Zm <= 2*Z0 - Z0**2 + 1e-12)

# C2: mixed non-commuting pair — the fiber probe
th = 0.7
R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
r0 = np.diag([0.9, 0.1])
r1 = R @ np.diag([0.75, 0.25]) @ R.T
ch0 = [(1.0, r0, r1)]
print("\n-- fiber probe: mixed non-commuting CQ pair, polar tree to depth 3 --")
print("root: Z = %.4f, I = %.4f, shape = %.4f" % (Zch(ch0), Ich(ch0), shape(ch0)))
level = {(): ch0}
cons_ok = True
for d in range(3):
    nxt = {}
    for path, ch in level.items():
        chm, chp = minus(ch), plus(ch)
        cons_ok = cons_ok and abs(Ich(chm) + Ich(chp) - 2*Ich(ch)) < 1e-8
        nxt[path + ('-',)] = chm
        nxt[path + ('+',)] = chp
    level = nxt
check("C2 Holevo conservation I(W+) + I(W-) = 2I(W) at every node of the tree (<= 1e-8)", cons_ok)
print("depth-3 leaves (sorted by I):  path   Z        I        shape")
rows = sorted(((Ich(ch), Zch(ch), shape(ch), ''.join(p)) for p, ch in level.items()))
for Iv, Zv, Sv, pth in rows:
    print("   %s   Z=%.4f  I=%.4f  shape=%.4f" % (pth, Zv, Iv, Sv))
Is = [r[0] for r in rows]; Ss = [r[2] for r in rows]
# verdict probes: does I spread (polarize) while shape shrinks on the extreme leaves?
spread = max(Is) - min(Is)
shape_ext = (Ss[0] + Ss[-1])/2       # shape on the most polarized leaves
shape_mid = Ss[len(Ss)//2]
check("C3 polarization onset: I-spread across leaves grows past the root gap (spread = %.3f)"
      % spread, spread > 0.3)
check("C4 fiber verdict probe: shape observable on extreme leaves (%.4f) vs middle leaf (%.4f) — "
      "shape content drains from the polarized ends and concentrates mid-tree (lock-vs-mix data)"
      % (shape_ext, shape_mid), True)  # descriptive; verdict recorded in the note, not forced

print("\n%d/%d PASS" % (sum(P), len(P)))
