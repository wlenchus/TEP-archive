#!/usr/bin/env python3
"""
AGM ribbon - LINKS 2-3 (PINNED): Z -> j -> AGM-invert -> tau.
Record basis:
  06-29 Thread D: "Z=H^3/1728f^5 playing j/1728" => j = 1728*Z_record.
  06-29 Open #2: "AGM-invert j -> tau".
  07-01 SIV.3: "the same nome-squaring computing period and Frobenius
  orbit-products: K = (pi/2)e^{2C_tot}"  [verified below as the Landen cascade].
Procedure (classical, as licensed): j -> lambda via the modular sextic
  256(1-l+l^2)^3 = j * l^2(1-l)^2 ;  K = K(m=l), K' = K(1-l);  tau = i K'/K;
round-trip check via Klein j.  60-digit working precision.
Compute-then-grade: everything printed; no ground-truth comparison in this script.
"""
import mpmath as mp
mp.mp.dps = 60

s5 = mp.sqrt(5)
j_plus  = 10400 - 4640*s5   # Z_+ branch  (Brioschi Z_B+ = (271+145*sqrt5)/1013888)
j_minus = 10400 + 4640*s5   # Z_- branch
print("record-Z (= j/1728 = H^3/1728f^5) values:")
print("  Z_record(+) =", mp.nstr(j_plus/1728, 40))
print("  Z_record(-) =", mp.nstr(j_minus/1728, 40))
print("  (Brioschi parameter Z_B = 1/(1728-j), certified in 02/02b)")
print()

def lambda_roots(j):
    # 256(1-l+l^2)^3 - j l^2 (1-l)^2 = 0, expanded to polynomial coefficients
    l = mp.mpf(1)  # placeholder
    # expand symbolically-lite: coefficients of 256(1-l+l^2)^3
    # (1-l+l^2)^3 = sum: use polynomial multiplication
    import itertools
    def pmul(a, b):
        c = [mp.mpf(0)]*(len(a)+len(b)-1)
        for i, ai in enumerate(a):
            for k, bk in enumerate(b):
                c[i+k] += ai*bk
        return c
    p1 = [mp.mpf(1), mp.mpf(-1), mp.mpf(1)]        # 1 - l + l^2 (ascending powers)
    p3 = pmul(pmul(p1, p1), p1)
    p3 = [256*c for c in p3]                        # 256(1-l+l^2)^3
    q1 = pmul([mp.mpf(0), mp.mpf(0), mp.mpf(1)], pmul([mp.mpf(1), mp.mpf(-1)], [mp.mpf(1), mp.mpf(-1)]))  # l^2(1-l)^2
    q1 = [j*c for c in q1]
    n = max(len(p3), len(q1))
    poly = [(p3[i] if i < len(p3) else 0) - (q1[i] if i < len(q1) else 0) for i in range(n)]
    poly_desc = list(reversed(poly))
    return mp.polyroots(poly_desc, maxsteps=300, extraprec=300)

def invert_j(j, name):
    print(f"--- AGM inversion for {name}: j = {mp.nstr(j, 40)} ---")
    roots = lambda_roots(j)
    print("  lambda sextet:")
    for r in roots:
        print("    ", mp.nstr(r, 30))
    # choose principal lambda: prefer real in (0,1) else smallest |.| with Im tau > 0
    lam = None
    for r in roots:
        if abs(mp.im(r)) < mp.mpf(10)**(-40) and 0 < mp.re(r) < 1:
            if lam is None or abs(mp.re(r) - 0) < abs(mp.re(lam)):
                lam = mp.re(r) if mp.re(r) < 0.5 else lam
    if lam is None:
        # complex j<1728 case: take root with positive imag part, |lam| smallest
        cands = sorted(roots, key=lambda r: abs(r))
        lam = cands[0]
    Kv  = mp.ellipk(lam)
    Kpv = mp.ellipk(1-lam)
    tau = mp.mpc(0,1)*Kpv/Kv
    if mp.im(tau) < 0:
        tau = -tau
    print("  chosen lambda =", mp.nstr(lam, 40))
    print("  K  =", mp.nstr(Kv, 40))
    print("  K' =", mp.nstr(Kpv, 40))
    print("  tau = iK'/K =", mp.nstr(tau, 40))
    # Landen / nome-squaring cascade verification of K = (pi/2) e^{2 C_tot}
    k = mp.sqrt(lam)
    rungs = []
    kk = k
    for n in range(80):
        kp = mp.sqrt(1 - kk**2)
        knext = (1 - kp)/(1 + kp)
        rungs.append(knext)
        kk = knext
        if abs(knext) < mp.mpf(10)**-58:
            break
    Ctot = mp.mpf(0) if all(abs(mp.im(r)) == 0 for r in rungs) else mp.mpc(0)
    Ctot = sum(mp.log(1 + r) for r in rungs)/2
    K_cascade = (mp.pi/2)*mp.e**(2*Ctot)
    print("  Landen cascade rungs used:", len(rungs))
    print("  C_tot = (1/2) sum ln(1+k_n) =", mp.nstr(Ctot, 40))
    print("  (pi/2) e^{2C_tot}          =", mp.nstr(K_cascade, 40))
    print("  |K - (pi/2)e^{2C_tot}|     =", mp.nstr(abs(Kv - K_cascade), 8))
    agm = mp.agm(1, mp.sqrt(1-lam))
    print("  AGM(1,k') = ", mp.nstr(agm, 40))
    print("  |K - pi/(2 AGM)| =", mp.nstr(abs(Kv - mp.pi/(2*agm)), 8))
    # round-trip: Klein j
    Jrt = mp.kleinj(tau)          # mpmath kleinj: J = j/1728 normalization check below
    print("  kleinj(tau)      =", mp.nstr(Jrt, 40))
    print("  1728*kleinj(tau) =", mp.nstr(1728*Jrt, 40))
    print("  round-trip error |1728*kleinj(tau) - j| =", mp.nstr(abs(1728*Jrt - j), 8))
    q2 = mp.e**(2*mp.pi*mp.mpc(0,1)*tau)
    print("  q = e^{2 pi i tau} =", mp.nstr(q2, 35), "  |q| =", mp.nstr(abs(q2), 30))
    print()
    return tau, lam

# sanity of kleinj normalization
print("kleinj normalization check: kleinj(i) =", mp.nstr(mp.kleinj(mp.mpc(0,1)), 20), " (expect 1 if J = j/1728)")
print()
tau_p, lam_p = invert_j(j_plus,  "j_+ (= 10400 - 4640*sqrt5, Z_+ branch)")
tau_m, lam_m = invert_j(j_minus, "j_- (= 10400 + 4640*sqrt5, Z_- branch)")

print("=== Summary of emitted tau (principal representatives, mod PSL(2,Z) only) ===")
print("  tau(+) =", mp.nstr(tau_p, 45), "   |tau| =", mp.nstr(abs(tau_p), 30))
print("  tau(-) =", mp.nstr(tau_m, 45), "   |tau| =", mp.nstr(abs(tau_m), 30))
with open("tau_values.txt", "w") as f:
    f.write(repr(tau_p) + "\n" + repr(tau_m) + "\n" + repr(lam_p) + "\n" + repr(lam_m) + "\n")
print("  [saved to tau_values.txt]")
