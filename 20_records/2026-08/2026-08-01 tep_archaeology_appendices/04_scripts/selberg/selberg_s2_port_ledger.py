#!/usr/bin/env python3
"""
selberg_s2_port_ledger.py -- Strike S2: the cusp-port ledger of the modular surface.

X = SL(2,Z)\\H as a one-port resonant cavity; the Eisenstein constant term
y^s + phi(s) y^{1-s} is incident + reflected wave at the cusp port.

TWO reflection-coefficient conventions (they differ by the Mobius factor s/(s-1)):

  xi(s)   = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)   (ENTIRE; xi(s)=xi(1-s); xi(0)=xi(1)=1/2)
  Lam(s)  = pi^{-s/2} Gamma(s/2) zeta(s)                (completed zeta with poles at s=0,1)

  phi_xi(s) = xi(2s-1)/xi(2s)      -- the charge's definition (pole-stripped / regularized port)
  phi_cl(s) = Lam(2s-1)/Lam(2s)
            = sqrt(pi) Gamma(s-1/2) zeta(2s-1) / (Gamma(s) zeta(2s))
            = phi_xi(s) * s/(s-1)  -- the ACTUAL Eisenstein constant-term coefficient
                                      (pole at s=1, residue 3/pi = 1/Vol(X); phi_cl(1/2) = -1)

On Re s = 1/2 the factor s/(s-1) is unimodular, so P-S2a is identical for both.
Elsewhere the two ledgers differ and the script reports both, honestly.

Sources used:
  * Maass cusp form spectral parameters R (lambda = 1/4 + R^2), level 1, all simple:
      LMFDB (lmfdb.org/ModularForm/GL2/Q/Maass/, labels 1.1 - 1.10):
      9.53369526 (odd), 12.1730083 (odd), 13.7797513 (even), 14.3585095 (odd),
      16.1380731 (odd), 16.6442592 (odd), 17.7385633 (even), 18.1809178 (odd),
      19.4234814 (even), 19.4847138 (odd).
      Consistent with Hejhal (1992), Steil (DESY 94-028), and the certified values of
      Booker-Strombergsson-Venkatesh (2006). "even/odd" = symmetry under z -> -conj(z);
      both parities count in the Weyl law of the full surface.
  * Refined Weyl law shape: W. Mueller, "Weyl's law in the theory of automorphic forms",
      Thm 4.1: N(T) + M(T) = (Area/4pi) T^2 - (m/pi) T log T + c T + O(T/log T),
      m = #cusps = 1, Area = pi/3, with M(T) = -(1/4pi) int_{-T}^{T} (phi'/phi)(1/2+ir) dr
      and phi = phi_cl (the scattering determinant).

Env knobs: S2_FAST=1 for a smoke test; S2_SECTIONS=a,b,c,d to select sections.
"""

import os, sys, time, json
import mpmath
from mpmath import (mp, mpf, mpc, mpmathify, pi, sqrt, log, exp, gamma, zeta,
                    digamma, arg, atan, euler, coth, zetazero, linspace, quad, diff)

FAST = bool(os.environ.get('S2_FAST'))
SECTIONS = os.environ.get('S2_SECTIONS', 'a,b,c,d').split(',')
TAG = ('FAST_' if FAST else '') + '_'.join(SECTIONS)
LOGPATH = '/home/claude/tep-review-out/selberg_s2_port_ledger_output_%s.txt' % TAG
_logf = open(LOGPATH, 'w')

def say(*a):
    line = ' '.join(str(x) for x in a)
    print(line, flush=True)
    _logf.write(line + '\n'); _logf.flush()

def d(x, n=20):
    return mp.nstr(x, n)

RES = {}
T0 = time.time()
say('mpmath version:', mpmath.__version__, '| FAST =', FAST, '| sections =', SECTIONS)

# ----------------------------------------------------------------------------------
# The port functions
# ----------------------------------------------------------------------------------
def xi_raw(s):
    """Entire completed zeta, written pole-safely: (1/2) s Gamma(s/2) = Gamma(s/2+1)."""
    s = mpmathify(s)
    return (s - 1) * pi**(-s/2) * gamma(s/2 + 1) * zeta(s)

def xi(s):
    s = mpmathify(s)
    if s == 1 or s == 0:
        return mpf(1)/2          # exact limit values xi(0) = xi(1) = 1/2
    return xi_raw(s)

def phi_xi(s):
    s = mpmathify(s)
    return xi(2*s - 1) / xi(2*s)

def phi_cl(s):
    s = mpmathify(s)
    return phi_xi(s) * s / (s - 1)

def phi_cl_direct(s):
    """Independent implementation from the Gamma/zeta formula (implementation cross-check)."""
    s = mpmathify(s)
    return sqrt(pi) * gamma(s - mpf(1)/2) * zeta(2*s - 1) / (gamma(s) * zeta(2*s))

# ==================================================================================
# P-S2a  --  seam unitarity |phi(1/2+it)| = 1
# ==================================================================================
if 'a' in SECTIONS:
    say('\n================ P-S2a: seam unitarity =================')
    mp.dps = 30
    t_bench0 = time.time()
    _ = phi_xi(mpf('0.5') + mpc(0, 60))
    bench = time.time() - t_bench0
    say('single phi_xi eval at t=60, dps=30: %.3f s' % bench)
    npts = 12 if FAST else 200
    ts = linspace(mpf('0.05'), mpf(60), npts)
    maxdev = mpf(-1); tmax = None
    for t in ts:
        s = mpf('0.5') + mpc(0, t)
        dev = abs(abs(phi_xi(s)) - 1)
        if dev > maxdev:
            maxdev, tmax = dev, t
    say('points: %d on t in [0.05, 60], dps = 30' % npts)
    say('max | |phi_xi(1/2+it)| - 1 |  =', d(maxdev, 6), ' attained at t =', d(tmax, 8))
    say('prediction: <= 1e-20  ->', 'PASS' if maxdev <= mpf('1e-20') else 'FAIL')
    # independent-implementation cross-check at 10 points
    maxrel = mpf(0)
    for t in ts[::max(1, npts//10)]:
        s = mpf('0.5') + mpc(0, t)
        a1 = phi_cl_direct(s); a2 = phi_cl(s)
        maxrel = max(maxrel, abs(a1 - a2)/abs(a1))
    say('cross-check phi_cl_direct (Gamma/zeta form) vs phi_xi*s/(s-1): max rel diff =', d(maxrel, 4))
    RES['S2a'] = dict(maxdev=d(maxdev, 8), t_at=d(tmax, 8), npts=npts, dps=30,
                      crosscheck=d(maxrel, 4), passed=bool(maxdev <= mpf('1e-20')))
    say('[t = %.1f s]' % (time.time() - T0))

# ==================================================================================
# P-S2b  --  passivity map on the physical half Re s in (1/2, 1]
# ==================================================================================
if 'b' in SECTIONS:
    say('\n================ P-S2b: passivity map ==================')
    mp.dps = 20
    say('map computed at dps = 20 (anomalies rechecked at dps = 40); grid 49 x 61')
    nsig, nt = (8, 10) if FAST else (49, 61)
    sigmas = linspace(mpf('0.51'), mpf('0.99'), nsig)
    tvals  = linspace(mpf(0), mpf(30), nt)
    grid_max_xi = mpf(-1); grid_max_xi_loc = None
    off_max_xi  = mpf(-1); off_max_xi_loc = None
    n_gain_xi = 0
    gain_cl = []          # (sigma, t, |phi_cl|) with |phi_cl| > 1
    tgb0 = time.time()
    for sg in sigmas:
        for t in tvals:
            s = mpc(sg, t)
            axi = abs(phi_xi(s))
            mob = abs(s/(s-1))
            acl = axi * mob
            if axi > grid_max_xi:
                grid_max_xi, grid_max_xi_loc = axi, (sg, t)
            if t > 0 and axi > off_max_xi:
                off_max_xi, off_max_xi_loc = axi, (sg, t)
            if axi > 1:
                n_gain_xi += 1
            if acl > 1:
                gain_cl.append((sg, t, acl))
    say('grid time: %.1f s' % (time.time() - tgb0))
    say('--- phi_xi (entire-xi ratio, the charge\'s definition) ---')
    say('max |phi_xi| over grid       =', d(grid_max_xi, 12), 'at (sigma,t) = (%s, %s)'
        % (d(grid_max_xi_loc[0], 6), d(grid_max_xi_loc[1], 6)))
    say('max |phi_xi| off axis (t>0)  =', d(off_max_xi, 12), 'at (%s, %s)'
        % (d(off_max_xi_loc[0], 6), d(off_max_xi_loc[1], 6)))
    say('grid points with |phi_xi| > 1:', n_gain_xi, ' (prediction |phi|<=1: %s)'
        % ('HOLDS EVERYWHERE' if n_gain_xi == 0 else 'VIOLATED'))
    say('--- phi_cl (Lambda ratio = actual constant-term coefficient) ---')
    say('grid points with |phi_cl| > 1:', len(gain_cl), 'of', nsig*nt)
    if gain_cl:
        tmaxg = max(p[1] for p in gain_cl); smin = min(p[0] for p in gain_cl); smax = max(p[0] for p in gain_cl)
        say('gain points: sigma in [%s, %s], t up to %s' % (d(smin, 4), d(smax, 4), d(tmaxg, 4)))
        rows = sorted(set(float(p[1]) for p in gain_cl))
        say('gain rows (t values): %s' % rows)
        biggest = max(gain_cl, key=lambda p: p[2])
        say('largest |phi_cl| on grid =', d(biggest[2], 10), 'at (%s, %s)' % (d(biggest[0], 4), d(biggest[1], 4)))
        anomalies = [p for p in gain_cl if p[1] >= 5]
        if anomalies:
            say('ANOMALY CANDIDATES at t >= 5 -- rechecking at dps = 40:')
            mp.dps = 40
            confirmed = []
            for (sg, t, val) in anomalies:
                v40 = abs(phi_cl(mpc(sg, t)))
                say('  (%s, %s): dps20 %s -> dps40 %s' % (d(sg,4), d(t,4), d(val,10), d(v40,10)))
                if v40 > 1: confirmed.append((sg, t, v40))
            mp.dps = 20
            say('confirmed high-t gain points:', len(confirmed))
        else:
            say('no gain points with t >= 5: gain confined to the low-t lens over the real segment')
    # real segment, fine
    say('--- real segment s = sigma in (0.5, 1), step 0.002 ---')
    nseg = 20 if FAST else 250
    seg = linspace(mpf('0.501'), mpf('0.999'), nseg)
    seg_max_xi = mpf(-1); seg_max_xi_at = None; seg_all_below = True
    seg_min_cl = mpf('1e100'); seg_min_cl_at = None; onset_ok = True
    for sg in seg:
        axi = abs(phi_xi(sg))
        acl = axi * abs(sg/(sg-1))
        if axi > seg_max_xi: seg_max_xi, seg_max_xi_at = axi, sg
        if axi >= 1: seg_all_below = False
        if acl < seg_min_cl: seg_min_cl, seg_min_cl_at = acl, sg
        if acl <= 1: onset_ok = False
    say('phi_xi: max on segment =', d(seg_max_xi, 15), 'at sigma =', d(seg_max_xi_at, 6),
        '| all < 1:', seg_all_below, '(sup -> 1 as sigma -> 1/2+)')
    say('phi_cl: min |phi_cl| on segment =', d(seg_min_cl, 12), 'at sigma =', d(seg_min_cl_at, 6),
        '| |phi_cl| > 1 on ALL of (0.5,1):', onset_ok)
    say('phi_cl gain onset: |phi_cl(0.501)| - 1 =', d(abs(phi_cl(mpf('0.501'))) - 1, 8),
        '  (slope prediction (2log4pi-2gamma)*delta =', d((2*log(4*pi)-2*euler)*mpf('0.001'), 8), ')')
    say('samples: |phi_cl(0.75)| =', d(abs(phi_cl(mpf('0.75'))), 10),
        ' |phi_cl(0.99)| =', d(abs(phi_cl(mpf('0.99'))), 10),
        ' |phi_cl(0.999)| =', d(abs(phi_cl(mpf('0.999'))), 10))
    say('sign on segment: phi_cl(0.75) =', d(phi_cl(mpf('0.75')), 10), '(negative: pi phase)')
    # lens ceiling: solve |phi_cl(sigma + i t)| = 1 in t
    def lens_ceiling(sg):
        f = lambda t: abs(phi_cl(mpc(sg, t))) - 1
        lo, hi = mpf('0.05'), None
        tprev, fprev = lo, f(lo)
        t = lo
        while t < 8:
            t += mpf('0.25')
            ft = f(t)
            if fprev > 0 and ft <= 0:
                lo, hi = tprev, t
                break
            tprev, fprev = t, ft
        if hi is None: return None
        for _ in range(60):
            mid = (lo + hi)/2
            if f(mid) > 0: lo = mid
            else: hi = mid
        return (lo + hi)/2
    if not FAST:
        for sg in (mpf('0.51'), mpf('0.75'), mpf('0.99')):
            tc = lens_ceiling(sg)
            say('gain-lens ceiling at sigma = %s :  |phi_cl| = 1 at t = %s' % (d(sg,4), d(tc, 10) if tc else 'none<8'))
    # transmission null tied to the first zeta zero: s* = (1+rho_1)/2
    mp.dps = 25
    rho1 = zetazero(1)
    sstar = (1 + rho1)/2
    say('port null at s* = (1+rho_1)/2 =', d(sstar, 15))
    say('  |phi_cl(s*)| =', d(abs(phi_cl(sstar)), 4), '  |phi_xi(s*)| =', d(abs(phi_xi(sstar)), 4),
        '(zeros of zeta(2s-1) are total-absorption points of the port)')
    mp.dps = 20
    RES['S2b'] = dict(grid_max_xi=d(grid_max_xi, 12), n_gain_xi=n_gain_xi,
                      n_gain_cl=len(gain_cl),
                      gain_tmax=d(max((p[1] for p in gain_cl), default=mpf(0)), 6),
                      seg_max_xi=d(seg_max_xi, 12), onset_all=onset_ok)
    say('[t = %.1f s]' % (time.time() - T0))

# ==================================================================================
# P-S2c  --  the Weyl budget identity
# ==================================================================================
if 'c' in SECTIONS:
    say('\n================ P-S2c: Weyl budget =====================')
    mp.dps = 20
    say('winding integral at dps = 20; phase-unwrap cross-check at dps = 15 (disclosed)')

    def lnphi_cl_deriv(t):
        """(phi_cl'/phi_cl)(1/2+it), d/ds. Uses the functional equation of zeta to keep
        all zeta evaluations on Re = 1: zeta'/zeta(2it) = chi'/chi(2it) - conj(zeta'/zeta(1+2it)),
        chi'/chi(s) = log(2pi) + (pi/2)cot(pi s/2) - psi(1-s), cot(pi i t) = -i coth(pi t)."""
        t = mpmathify(t)
        it = mpc(0, t)
        z  = zeta(1 + 2*it)
        zp = zeta(1 + 2*it, derivative=1)
        L1 = zp/z
        ps1 = digamma(1 + 2*it)
        chi_ld = log(2*pi) + (pi/2)*(-mpc(0,1)*coth(pi*t)) - mpmathify(ps1).conjugate()
        L0 = chi_ld - L1.conjugate()
        return digamma(it) - digamma(mpf('0.5') + it) + 2*L0 - 2*L1

    def lnphi_cl_deriv_direct(t):
        t = mpmathify(t); it = mpc(0, t)
        return (digamma(it) - digamma(mpf('0.5') + it)
                + 2*zeta(2*it, derivative=1)/zeta(2*it)
                - 2*zeta(1 + 2*it, derivative=1)/zeta(1 + 2*it))

    vmax = mpf(0)
    for tv in (mpf('0.7'), mpf('3.3'), mpf('9.9')):
        a1 = lnphi_cl_deriv(tv); a2 = lnphi_cl_deriv_direct(tv)
        vmax = max(vmax, abs(a1 - a2)/abs(a2))
    say('functional-equation acceleration validated: max rel dev vs direct =', d(vmax, 4))

    Ttop = 3 if FAST else 20
    edges = [mpf(k)/2 for k in range(0, 2*Ttop + 1)]
    integ = lambda t: lnphi_cl_deriv(t).real
    Mcum = {mpf(0): mpf(0)}
    acc = mpf(0)
    tq0 = time.time()
    for i in range(len(edges) - 1):
        acc += quad(integ, [edges[i], edges[i+1]], method='gauss-legendre')
        Mcum[edges[i+1]] = -acc/(2*pi)      # M(T) = -(1/4pi) int_{-T}^{T} = -(1/2pi) int_0^T Re
    say('quadrature time: %.1f s (%d panels to T = %d)' % (time.time() - tq0, len(edges)-1, Ttop))

    if not FAST:
        M15 = Mcum[mpf(15)]
        M15_xi = M15 + atan(mpf(30))/pi
        say('M_cl(15) = -(1/4pi) int_{-15}^{15} (phi_cl\'/phi_cl) dt =', d(M15, 15))
        say('M_xi(15) = M_cl(15) + arctan(30)/pi              =', d(M15_xi, 15),
            '  [Delta = arctan(2T)/pi =', d(atan(mpf(30))/pi, 10), '-> 1/2 as T -> oo]')

        # phase-unwrap cross-check
        mp.dps = 15
        tu0 = time.time()
        prev = mpc(-1)          # phi_cl(1/2) = -1 exactly
        th = pi                  # theta(0) = pi
        Munwrap = {}
        kmax = 2000
        for k in range(1, kmax + 1):
            t = mpf(k)/100
            cur = phi_cl(mpf('0.5') + mpc(0, t))
            th += arg(cur/prev)
            prev = cur
            if k in (1500, 2000):
                Munwrap[k/100] = -(th - pi)/(2*pi)
        say('unwrap time: %.1f s (step 0.01, dps 15)' % (time.time() - tu0))
        mp.dps = 20
        say('M_cl(15) via phase unwrap =', d(Munwrap[15.0], 12),
            '| quad - unwrap =', d(M15 - Munwrap[15.0], 4))
        say('M_cl(20) via quad =', d(Mcum[mpf(20)], 12), '| via unwrap =', d(Munwrap[20.0], 12))

        # sign change of Re phi'/phi on the line (ceiling of the gain lens AT the line)
        lo, hi = mpf(2), mpf(5)
        flo = integ(lo)
        for _ in range(50):
            mid = (lo + hi)/2
            if integ(mid)*flo > 0: lo = mid
            else: hi = mid
        say('Re (phi_cl\'/phi_cl)(1/2+it) changes sign at t* =', d((lo+hi)/2, 8),
            '(passivity-gain boundary touches the seam at this height)')

        # eigenvalues (LMFDB level-1 Maass forms; lambda = 1/4 + R^2; all simple)
        RJ = [mpf('9.53369526'), mpf('12.1730083'), mpf('13.7797513'), mpf('14.3585095'),
              mpf('16.1380731'), mpf('16.6442592'), mpf('17.7385633'), mpf('18.1809178'),
              mpf('19.4234814'), mpf('19.4847138')]
        PAR = ['odd','odd','even','odd','odd','odd','even','odd','even','odd']
        Ncusp = lambda T: sum(1 for r in RJ if r <= T)
        say('N_cusp(15) = %d  from R = 9.53369526 (odd), 12.1730083 (odd), 13.7797513 (even), 14.3585095 (odd)'
            % Ncusp(15))
        say('   [source: LMFDB level-1 Maass forms, labels 1.1-1.4; consistent with Hejhal/Steil/BSV certified values; all multiplicity one]')

        S15 = Ncusp(15) + M15
        lead = mpf(225)/12
        say('--- headline balance at T = 15 ---')
        say('N_cusp(15) + M_cl(15) =', d(S15, 12))
        say('leading Weyl term T^2/12 =', d(lead, 12))
        say('residual (sum - T^2/12) =', d(S15 - lead, 8))
        S15xi = Ncusp(15) + M15_xi
        say('with the charge\'s phi_xi instead: N + M_xi =', d(S15xi, 12),
            ' residual =', d(S15xi - lead, 8))

        # refined law (Mueller Thm 4.1, m = 1): N+M = T^2/12 - (1/pi) T log T + c T + O(T/log T)
        say('--- refined-law comparison over T in [4, 20] (Mueller Thm 4.1 shape) ---')
        Ts = [float(e) for e in edges if 4 <= e <= 20]
        Rvals = [float(Ncusp(mpf(T)) + Mcum[mpf(T)] - mpf(T)**2/12) for T in Ts]
        import math
        # Fit A: R = a T log T + b T + c
        def fit3(Ts, Rv):
            X = [[T*math.log(T), T, 1.0] for T in Ts]
            # normal equations 3x3
            A = [[sum(X[i][p]*X[i][q] for i in range(len(Ts))) for q in range(3)] for p in range(3)]
            Bv = [sum(X[i][p]*Rv[i] for i in range(len(Ts))) for p in range(3)]
            det = (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
                   - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
                   + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
            def rep(col):
                M2 = [row[:] for row in A]
                for r in range(3): M2[r][col] = Bv[r]
                return (M2[0][0]*(M2[1][1]*M2[2][2]-M2[1][2]*M2[2][1])
                        - M2[0][1]*(M2[1][0]*M2[2][2]-M2[1][2]*M2[2][0])
                        + M2[0][2]*(M2[1][0]*M2[2][1]-M2[1][1]*M2[2][0]))
            a, b, c = rep(0)/det, rep(1)/det, rep(2)/det
            rms = math.sqrt(sum((Rv[i] - (a*Ts[i]*math.log(Ts[i]) + b*Ts[i] + c))**2
                                for i in range(len(Ts)))/len(Ts))
            return a, b, c, rms
        a, b, c, rms = fit3(Ts, Rvals)
        say('Fit A: N+M-T^2/12 = a T log T + b T + c :')
        say('   a = %.6f  (Mueller predicts -1/pi = %.6f; ratio %.4f)' % (a, -1/math.pi, a/(-1/math.pi)))
        say('   b = %.6f, c = %.6f, fit RMS = %.4f' % (b, c, rms))
        # Fit B: a fixed at -1/pi
        a0 = -1/math.pi
        Y = [Rvals[i] - a0*Ts[i]*math.log(Ts[i]) for i in range(len(Ts))]
        n = len(Ts); Sx = sum(Ts); Sxx = sum(T*T for T in Ts); Sy = sum(Y); Sxy = sum(Ts[i]*Y[i] for i in range(n))
        bb = (n*Sxy - Sx*Sy)/(n*Sxx - Sx*Sx); cc = (Sy - bb*Sx)/n
        rms2 = math.sqrt(sum((Y[i] - (bb*Ts[i] + cc))**2 for i in range(n))/n)
        say('Fit B (a := -1/pi fixed): b = %.6f, c = %.6f, RMS = %.4f' % (bb, cc, rms2))
        say('   (RMS is the O(1) eigenvalue-staircase fluctuation; hyperbolic/elliptic terms not modeled)')
        say('included: leading T^2/12; sub-leading -(1/pi)T log T (Mueller); empirical T-linear + const')
        say('NOT included: oscillatory hyperbolic remainder, explicit elliptic constants')
        # small table
        say('--- table: T | N | M_cl | N+M | T^2/12 | (N+M)-T^2/12 ---')
        for T in (5, 10, 12, 14, 15, 16, 18, 20):
            Tm = mpf(T)
            say('  %4.1f | %2d | %s | %s | %s | %s'
                % (T, Ncusp(Tm), d(Mcum[Tm], 8), d(Ncusp(Tm)+Mcum[Tm], 8), d(Tm**2/12, 8),
                   d(Ncusp(Tm)+Mcum[Tm]-Tm**2/12, 6)))
        RES['S2c'] = dict(M15=d(M15, 15), M15_xi=d(M15_xi, 15),
                          quad_minus_unwrap=d(M15 - Munwrap[15.0], 4),
                          N15=Ncusp(15), sum15=d(S15, 12), lead=d(lead, 8),
                          residual15=d(S15 - lead, 8),
                          fitA=dict(a=a, b=b, c=c, rms=rms),
                          fitB=dict(a=a0, b=bb, c=cc, rms=rms2))
    say('[t = %.1f s]' % (time.time() - T0))

# ==================================================================================
# P-S2d  --  the jet at the seam
# ==================================================================================
if 'd' in SECTIONS:
    say('\n================ P-S2d: seam jet ========================')
    mp.dps = 30
    # xi(0) and xi(1) as numerical limits through the raw formula (no special-casing)
    eps = mpf('1e-25')
    x0p, x0m = xi_raw(eps), xi_raw(-eps)
    x1p, x1m = xi_raw(1 + eps), xi_raw(1 - eps)
    say('xi(0) limits:  xi(+1e-25) - 1/2 =', d(x0p - mpf(1)/2, 4),
        ' xi(-1e-25) - 1/2 =', d(x0m - mpf(1)/2, 4))
    say('xi(1) limits:  xi(1+1e-25) - 1/2 =', d(x1p - mpf(1)/2, 4),
        ' xi(1-1e-25) - 1/2 =', d(x1m - mpf(1)/2, 4))
    say('phi_xi(1/2) = xi(0)/xi(1) = 1 exactly (both equal 1/2 by xi(s)=xi(1-s));')
    say('   numerically: |phi_xi(1/2 + 1e-20) - 1| =', d(abs(phi_xi(mpf('0.5') + mpf('1e-20')) - 1), 4))
    say('   NOTE: the CLASSICAL coefficient phi_cl(1/2) = -1 (Lam-poles flip the sign);')
    say('   numerically: phi_cl(1/2 + 1e-20) + 1 =', d(phi_cl(mpf('0.5') + mpf('1e-20')) + 1, 4))

    # c1 three ways
    c1_closed = 2*log(4*pi) - 2*euler - 4
    ratio0 = diff(xi, mpf(0)) / xi(mpf(0))
    ratio1 = diff(xi, mpf(1)) / xi(mpf(1))
    closed_ratio0 = -(euler/2 + 1 - log(4*pi)/2)
    say('xi\'(0)/xi(0) numeric =', d(ratio0, 20))
    say('closed form -(gamma/2 + 1 - log(4pi)/2) =', d(closed_ratio0, 20),
        '| dev =', d(abs(ratio0 - closed_ratio0), 4))
    say('functional-equation check xi\'(1)/xi(1) = -xi\'(0)/xi(0): dev =', d(abs(ratio1 + ratio0), 4))
    c1_b = 2*(ratio0 - ratio1)
    half = mpf('0.5')
    def Dc(dl):
        return (phi_xi(half + dl) - phi_xi(half - dl)) / (2*dl)
    d1, d2, d3 = Dc(mpf('1e-6')), Dc(mpf('5e-7')), Dc(mpf('2.5e-7'))
    r1 = (4*d2 - d1)/3; r2 = (4*d3 - d2)/3
    c1_c = (16*r2 - r1)/15
    say('c1 = d/d(delta) phi_xi(1/2+delta) at 0:')
    say('   closed form  2 log(4 pi) - 2 gamma - 4 =', d(c1_closed, 22))
    say('   via 2(xi\'/xi(0) - xi\'/xi(1))          =', d(c1_b, 22), '| dev =', d(abs(c1_b - c1_closed), 4))
    say('   via Richardson finite differences      =', d(c1_c, 22), '| dev =', d(abs(c1_c - c1_closed), 4))
    say('   c1 to 15 digits: %s' % d(c1_closed, 15))
    say('   (= 4 xi\'(0)/xi(0); reflection dips BELOW 1 into the physical side: passive seam)')
    # classical jet
    c1cl_closed = 2*log(4*pi) - 2*euler
    dcl = (phi_cl(half + mpf('1e-6')) - phi_cl(half - mpf('1e-6'))) / mpf('2e-6')
    say('classical jet: phi_cl(1/2+delta) = -(1 + (2log4pi - 2gamma) delta + O(delta^2))')
    say('   slope 2log(4pi) - 2gamma =', d(c1cl_closed, 22))
    say('   phi_cl\'(1/2) numeric =', d(dcl, 15), ' vs -(2log4pi-2gamma) =', d(-c1cl_closed, 15))
    say('   |phi_cl| GROWS off the seam on the real ray: gain onset at the seam itself')
    RES['S2d'] = dict(c1=d(c1_closed, 17), c1_richardson=d(c1_c, 17),
                      xi_ratio0=d(ratio0, 17), c1_classical_slope=d(c1cl_closed, 17))
    say('[t = %.1f s]' % (time.time() - T0))

say('\nTOTAL TIME: %.1f s' % (time.time() - T0))
say('JSON_SUMMARY ' + json.dumps(RES))
_logf.close()
