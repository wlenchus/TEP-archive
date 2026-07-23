#!/usr/bin/env python3
"""
TOWER5 - script 12: the X(5) hauptmodul r(tau) = Rogers-Ramanujan continued fraction.
Definition used (product form):  r(tau) = q^{1/5} prod_{n>=1} (1-q^n)^{legendre(n,5)}.
IMPORTED CLASSICAL IDENTITIES -- each VERIFIED numerically at random non-special tau
BEFORE any use at tau(pm)  [labels D2.5 = Duke BAMS 42 (2005) eq (2.5), D7.4 = ibid eq (7.4),
RAM5 = Ramanujan's degree-5 modular equation, ETA1/ETA5 = Ramanujan eta identities,
VMAP = the Fricke action r(-1/tau) = (1 - phi r)/(phi + r), phi = golden ratio]:
  (D2.5)  (r^20 - 228 r^15 + 494 r^10 + 228 r^5 + 1)^3 + j(tau) r^5 (r^10 + 11 r^5 - 1)^5 = 0
  (ETA1)  1/r - r      = eta(tau/5)/eta(5 tau) + 1
  (ETA5)  1/r^5 - r^5  = (eta(tau)/eta(5 tau))^6 + 11
  (RAM5)  r(tau)^5     = r(5 tau) (1 - 2v + 4v^2 - 3v^3 + v^4)/(1 + 3v + 4v^2 + 2v^3 + v^4), v = r(5 tau)
  (D7.4)  r(tau/5)^5 / r(5 tau) = (r^4 - 3r^3 + 4r^2 - 2r + 1)/(r^4 + 2r^3 + 4r^2 + 3r + 1), r = r(tau)
  (T5)    j = (t^2 + 250 t + 3125)^3 / t^5,  t = (eta(tau)/eta(5 tau))^6   [X_0(5) hauptmodul]
  (SHIFT) r(tau + 1) = zeta_5 r(tau)
Then: values at tau(pm), 5 tau, tau/5, (tau+k)/5; T5-based algebraicity certificate of
t(tau_pm) as a resolvent-sextic-field element; icosahedral certificate for r(tau_pm).
Compute-then-grade.
"""
import mpmath as mp
mp.mp.dps = 100
import sys
sys.path.insert(0, "/home/claude/tower5")
from tower5_values import tau_p, tau_m

I = mp.mpc(0, 1)
phi = (1 + mp.sqrt(5))/2
z5 = mp.e**(2*mp.pi*I/5)
s5 = mp.sqrt(5)
jp = 10400 - 4640*s5
jm = 10400 + 4640*s5

def leg5(n):
    m = n % 5
    return 0 if m == 0 else (1 if m in (1, 4) else -1)

def rr(tau, nmax=None):
    """Rogers-Ramanujan via eta-type product; q^{1/5} = exp(2 pi i tau/5) (principal on tau)."""
    q = mp.e**(2*mp.pi*I*tau)
    if nmax is None:
        nmax = int(mp.ceil(mp.mp.dps * mp.log(10) / (2*mp.pi*mp.im(tau)))) + 30
    pr = mp.mpc(1)
    for n in range(1, nmax+1):
        c = leg5(n)
        if c:
            pr *= (1 - q**n)**c
    return mp.e**(2*mp.pi*I*tau/5) * pr

def rr_cfrac(tau, depth=None):
    """actual continued fraction q^{1/5}/(1+q/(1+q^2/(1+...)))"""
    q = mp.e**(2*mp.pi*I*tau)
    if depth is None:
        depth = int(mp.ceil(mp.mp.dps * mp.log(10) / (2*mp.pi*mp.im(tau)))) + 40
    v = mp.mpc(1)
    for n in range(depth, 0, -1):
        v = 1 + q**n/v
    return mp.e**(2*mp.pi*I*tau/5)/v

def J(tau):
    return 1728*mp.kleinj(tau)

def eta(tau):
    q = mp.e**(2*mp.pi*I*tau)
    nmax = int(mp.ceil(mp.mp.dps*mp.log(10)/(2*mp.pi*mp.im(tau)))) + 30
    pr = mp.mpc(1)
    for n in range(1, nmax+1):
        pr *= (1 - q**n)
    return mp.e**(mp.pi*I*tau/12)*pr

def icos_num(r):   # Duke 2.5 numerator polynomial
    return r**20 - 228*r**15 + 494*r**10 + 228*r**5 + 1

def icos_den(r):
    return r**5 * (r**10 + 11*r**5 - 1)**5

print("== identity battery at random non-special tau ==")
rand_taus = [mp.mpc('0.13', '1.21'), mp.mpc('-0.37', '0.89'), mp.mpc('0.05', '2.30')]
for k, t in enumerate(rand_taus):
    r = rr(t)
    rc = rr_cfrac(t)
    jt = J(t)
    tt = (eta(t)/eta(5*t))**6
    res = {}
    res['product=cfrac'] = abs(r - rc)
    res['SHIFT'] = abs(rr(t+1) - z5*r)
    res['D2.5'] = abs(icos_num(r)**3 + jt*icos_den(r)) / (abs(icos_num(r))**3 + abs(jt*icos_den(r)))
    res['ETA1'] = abs(1/r - r - (eta(t/5)/eta(5*t) + 1))
    res['ETA5'] = abs(1/r**5 - r**5 - (tt/( (eta(5*t)/eta(5*t))**6 ) if False else (eta(t)/eta(5*t))**6) - 11)
    v = rr(5*t)
    res['RAM5'] = abs(r**5 - v*(1 - 2*v + 4*v**2 - 3*v**3 + v**4)/(1 + 3*v + 4*v**2 + 2*v**3 + v**4))
    res['D7.4'] = abs(rr(t/5)**5/v - (r**4 - 3*r**3 + 4*r**2 - 2*r + 1)/(r**4 + 2*r**3 + 4*r**2 + 3*r + 1))
    res['T5'] = abs((tt**2 + 250*tt + 3125)**3/tt**5 - jt)/abs(jt)
    res['VMAP'] = abs(rr(-1/t) - (1 - phi*r)/(phi + r))
    print(f"tau_rand{k+1} = {mp.nstr(t, 10)}:  r = {mp.nstr(r, 20)}")
    for lab, v_ in res.items():
        print(f"    {lab:14s} residual = {mp.nstr(v_, 4)}")

print("\n== values at the branch points ==")
store = {}
for name, tau, j0 in [("+", tau_p, jp), ("-", tau_m, jm)]:
    print(f"--- branch ({name}) ---")
    r0 = rr(tau)
    print("  r(tau)      =", mp.nstr(r0, 45))
    print("  |r(tau)|    =", mp.nstr(abs(r0), 30))
    ic = abs(icos_num(r0)**3 + j0*icos_den(r0)) / (abs(icos_num(r0))**3 + abs(j0*icos_den(r0)))
    print("  icosahedral certificate (D2.5 with exact j_branch), rel residual =", mp.nstr(ic, 4))
    r5 = rr(5*tau)
    print("  r(5 tau)    =", mp.nstr(r5, 35))
    r15 = rr(tau/5)
    print("  r(tau/5)    =", mp.nstr(r15, 35))
    for k in range(1, 5):
        print(f"  r((tau+{k})/5) =", mp.nstr(rr((tau+k)/5), 30))
    rV = rr(-1/tau)
    print("  r(-1/tau)   =", mp.nstr(rV, 35), "  |VMAP residual| =", mp.nstr(abs(rV - (1-phi*r0)/(phi+r0)), 4))
    t0 = (eta(tau)/eta(5*tau))**6
    print("  t(tau) = (eta/eta5)^6 =", mp.nstr(t0, 40))
    sext_res = abs((t0**2 + 250*t0 + 3125)**3 - j0*t0**5)/abs(j0*t0**5)
    print("  X0(5)-sextic certificate: |(t^2+250t+3125)^3 - j t^5| rel =", mp.nstr(sext_res, 4))
    print("    [=> t(tau) is a root of the EXACT Q(sqrt5)-sextic (T^2+250T+3125)^3 - j_pm T^5,")
    print("        whose splitting field is the resolvent-sextic field * Q(sqrt5) (11a);")
    print("        the eta-quotient value itself is a resolvent-sextic-field number]")
    store[name] = dict(r0=r0, r5=r5, r15=r15, t0=t0)

with open("/home/claude/tower5/tower5_rr.py", "w") as f:
    f.write("from mpmath import mpf, mpc\n")
    for name in ("+", "-"):
        tag = "p" if name == "+" else "m"
        for key, val in store[name].items():
            f.write(f"{key}_{tag} = {val!r}\n")
print("\n[saved tower5_rr.py]")
