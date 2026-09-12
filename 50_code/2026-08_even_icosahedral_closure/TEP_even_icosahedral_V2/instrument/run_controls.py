#!/usr/bin/env python3
"""KD-1 controls, resumption 2026-08-03: kernel triple-validation; alpha; beta1-even; beta1-odd; meter floors."""
import numpy as np, mpmath as mp, json, sys
sys.path.insert(0, '.')
from instr2 import ker, Arm, sieve, Xof, TGRID, UGRID
mp.mp.dps = 30

out = {}

# ---- 1. kernel triple validation: scipy-k0 leg vs mpmath-besselk leg vs meijerg leg vs subdivided MB ----
ys = [0.05, 0.3, 1.0, 3.0, 8.0, 15.0]
worst_even = 0.0; worst_odd = 0.0
for y in ys:
    kv  = float(ker(0, np.array([y]))[0])
    kvo = float(ker(1, np.array([y]))[0])
    bk  = 4*mp.besselk(0, 2*mp.mpf(y))              # closed form: 4K0(2y)
    bko = 4*mp.mpf(y)*mp.besselk(0, 2*mp.mpf(y))    # 4yK0(2y)
    mg  = 2*mp.meijerg([[], []], [[0, 0], []], mp.mpf(y)**2)
    mgo = 2*mp.meijerg([[], []], [[mp.mpf(1)/2, mp.mpf(1)/2], []], mp.mpf(y)**2)
    worst_even = max(worst_even, abs(kv - float(bk))/float(bk), abs(float(mg) - float(bk))/float(bk))
    worst_odd  = max(worst_odd,  abs(kvo - float(bko))/float(bko), abs(float(mgo) - float(bko))/float(bko))
# Mellin-Barnes third leg, subdivided contour (quadrature-limited; bar 1e-9, disclosed)
worst_mb = 0.0
for y in [0.3, 3.0]:
    c = mp.mpf('1.7'); seg = [-80, -40, -15, -5, 0, 5, 15, 40, 80]
    f  = lambda tau: mp.re((mp.gamma((c + 1j*tau)/2))**2 * mp.mpf(y)**(-(c + 1j*tau)))
    v  = mp.quad(f, seg, maxdegree=10) / (2*mp.pi)
    fo = lambda tau: mp.re((mp.gamma((c + 1 + 1j*tau)/2))**2 * mp.mpf(y)**(-(c + 1j*tau)))
    vo = mp.quad(fo, seg, maxdegree=10) / (2*mp.pi)
    worst_mb = max(worst_mb, abs(float(ker(0, np.array([y]))[0]) - float(v))/abs(float(v)),
                            abs(float(ker(1, np.array([y]))[0]) - float(vo))/abs(float(vo)))
print(f"KERNEL validation: even worst rel {worst_even:.3e}  odd worst rel {worst_odd:.3e} (bar 1e-13); MB leg {worst_mb:.3e} (bar 1e-9)")
out['kernel'] = {'even': worst_even, 'odd': worst_odd, 'mb': worst_mb,
                 'pass': worst_even < 1e-13 and worst_odd < 1e-13 and worst_mb < 1e-9}

# ---- 2. alpha control: L(chi5)L(chi8), N=40, even port ----
k58 = {}
for line in open('alpha_chars.txt'):
    p, k5, k8 = line.strip().split(':')
    k58[int(p)] = (int(k5), int(k8))
def loc_alpha(p):
    if p not in k58:
        return None
    k5, k8 = k58[p]
    return np.convolve([1.0, -k5], [1.0, -k8])
N = 40.0
arm = Arm(N, 0)
arm.set_a(sieve(arm.X, loc_alpha))
r, eps = arm.residual()
x, eta, gnew = arm.meter(eps)
gdev = float(np.max(np.abs(gnew - 2)))
selfgate = float(np.max(np.abs(gnew[:15][::-1]*gnew[15:] - 4.0/(1.0 - x[15:]*x[:15][::-1]))))
# negatives
armw = Arm(N*1.05, 0, X=arm.X); armw.set_a(arm.a); rw, _ = armw.residual()
armw2 = Arm(N/4, 0, X=arm.X); armw2.set_a(arm.a); rw2, _ = armw2.residual()
de = arm.Fi - (-1.0) * arm.t * np.conj(arm.F); rwe = float(np.max(np.abs(de))/np.max(np.abs(arm.F)))
print(f"ALPHA (N=40): residual {r:.3e}  eps {eps:.6f}  meter dev {gdev:.3e}  selfgate {selfgate:.3e}")
print(f"  NEG wrong-N*1.05: {rw:.3e}   wrong-N/4: {rw2:.3e}   wrong-eps(-1): {rwe:.3e}")
out['alpha'] = {'residual': r, 'eps': [eps.real, eps.imag], 'meter': gdev,
                'neg': [rw, rw2, rwe], 'pass': r <= 5e-12}

# ---- 3. beta1-even: Ind psi_229, N=229, even port ----
dih = {}
for line in open('../gp/classes_dih229.txt'):
    p, c = line.strip().split(':')
    dih[int(p)] = c
FAC2 = {'P': [1.0, -2.0, 1.0], 'N': [1.0, 1.0, 1.0], 'I': [1.0, 0.0, -1.0], 'R': [1.0, -1.0]}
def loc_dih(scramble=0.0, rng=None):
    def f(p):
        c = dih.get(p)
        if c is None:
            return None
        if rng is not None and c in 'PN' and rng.random() < scramble:
            c = 'N' if c == 'P' else 'P'
        return FAC2[c]
    return f
arm229 = Arm(229.0, 0)
arm229.set_a(sieve(arm229.X, loc_dih()))
r229, eps229 = arm229.residual()
x2, eta2, gnew2 = arm229.meter(eps229)
g2dev = float(np.max(np.abs(gnew2 - 2)))
rng = np.random.default_rng(20260803)
arm229s = Arm(229.0, 0); arm229s.set_a(sieve(arm229s.X, loc_dih(0.3, rng))); rs, _ = arm229s.residual()
armw = Arm(229.0/4, 0, X=arm229.X); armw.set_a(arm229.a); rwn, _ = armw.residual()
armo = Arm(229.0, 1, X=arm229.X); armo.set_a(arm229.a); ro, _ = armo.residual()
print(f"BETA1-EVEN (Ind psi_229, N=229): residual {r229:.3e}  eps {eps229:.6f}  meter dev {g2dev:.3e}")
print(f"  NEG scramble30%: {rs:.3e}   wrong-N/4: {rwn:.3e}   odd-port: {ro:.3e}")
out['beta1even'] = {'residual': r229, 'eps': [eps229.real, eps229.imag], 'meter': g2dev,
                    'neg': [rs, rwn, ro], 'pass': r229 <= 5e-12}

# ---- 4. beta1-odd: Ind psi_229 (x) chi_-4, N=3664, odd port ----
def chi4(p):
    return 0 if p == 2 else (1 if p % 4 == 1 else -1)
def loc_dih_odd(p):
    c = dih.get(p)
    if c is None or p == 2:
        return None if p == 2 else None
    if c == 'R':
        return [1.0, -chi4(p)]
    if c == 'P':
        return [1.0, -2.0*chi4(p), 1.0]
    if c == 'N':
        return [1.0, 1.0*chi4(p), 1.0]
    if c == 'I':
        return [1.0, 0.0, -1.0]
    return None
armodd = Arm(3664.0, 1)
armodd.set_a(sieve(armodd.X, loc_dih_odd))
rodd, epsodd = armodd.residual()
xo, etao, gnewo = armodd.meter(epsodd)
godev = float(np.max(np.abs(gnewo - 2)))
armoe = Arm(3664.0, 0, X=armodd.X); armoe.set_a(armodd.a); roe, _ = armoe.residual()
armon = Arm(3664.0*1.05, 1, X=armodd.X); armon.set_a(armodd.a); ron, _ = armon.residual()
print(f"BETA1-ODD (Ind psi_229 x chi_-4, N=3664): residual {rodd:.3e}  eps {epsodd:.6f}  meter dev {godev:.3e}")
print(f"  NEG even-port: {roe:.3e}   wrong-N*1.05: {ron:.3e}")
out['beta1odd'] = {'residual': rodd, 'eps': [epsodd.real, epsodd.imag], 'meter': godev,
                   'neg': [roe, ron], 'pass': rodd <= 5e-12}

out['floors'] = {'theta': max(out['alpha']['residual'], out['beta1even']['residual'], out['beta1odd']['residual']),
                 'meter': max(out['alpha']['meter'], out['beta1even']['meter'], out['beta1odd']['meter'])}
json.dump(out, open('controls2.json', 'w'), indent=1)
allpass = out['kernel']['pass'] and out['alpha']['pass'] and out['beta1even']['pass'] and out['beta1odd']['pass']
print("KD-1 GATE:", "ALL CONTROLS PASS" if allpass else "*** CONTROL FAILURE — STOP ***")
