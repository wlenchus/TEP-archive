"""R3.4-e VALUE-REGISTER RUN — the reduction-flow locator, graded blind.

Evaluator (carriage path — no ideal multiplication, no Gauss composition, no key access):
  input: (p, r_p) under the declared convention [r_p in (0,p/2), root of x^2 = -5 mod p]
  1. lift to the conductor-2 order:  r' = 2*r_p mod p   (since 2(r_p+sqrt-5) = 2r_p + sqrt-20)
  2. form the local chart:  Q_p = [p, 2r', (r'^2+20)/p]  (disc -80)
  3. run the PSL(2,Z) REDUCTION FLOW (chart moves T/S only -- the tower's chart groupoid;
     the group law of Cl(-80) is never used)
  4. read the terminal chart in {[1,0,20], [4,0,5], [3,2,7], [3,-2,7]}
  5. dictionary (gauged by the single datum psi(p_3) = +i, i.e. p_3 -> [3,-2,7]):
        [3,-2,7] -> +i   [3,2,7] -> -i   [1,0,20] -> +1   [4,0,5] -> -1
Analytic certificate: j(z_p) at z_p = (-r' + i*sqrt(20))/p equals j of the terminal chart
  (PSL2-invariance): the locator is a value-register read; reduction is its exact evaluator.

Grading (answer-key path, never touched by the evaluator):
  - nonprincipal split p: the frozen key (Delta 2/3), fit zone p<100 and BLIND zone 100<p<300
  - principal split p: predicted psi = +-1  =>  predicted a_p = 2*psi, graded against the
    eta(4t)eta(20t) coefficients computed independently from the pentagonal expansion.
"""
import math

# ---------- shared ----------
def is_prime(p):
    return p > 1 and all(p % d for d in range(2, int(math.isqrt(p))+1))

def root_conv(p):
    for r in range(1, p):
        if (r*r + 5) % p == 0:
            return r if r < p - r else p - r
    return None

def split_type(p):
    """None (inert/ramified), 'principal', 'nonprincipal' in Cl(Q(sqrt-5))"""
    if p in (2,5) or not is_prime(p): return None
    if pow(-5 % p, (p-1)//2, p) != 1: return None
    for x in range(0, int(math.isqrt(p))+1):
        rr = p - x*x
        if rr >= 0 and rr % 5 == 0:
            y2 = rr//5; s = int(math.isqrt(y2))
            if s*s == y2: return 'principal'
    return 'nonprincipal'

# ---------- the evaluator: reduction flow only ----------
def reduce_form(a, b, c):
    """Gauss reduction of positive definite (a,b,c); chart moves only."""
    while True:
        # normalize: b in (-a, a]
        if not (-a < b <= a):
            k = (a - b) // (2*a)          # shift so that b + 2ka in (-a, a]
            b = b + 2*a*k
            c = (b*b + 80) // (4*a)       # disc = b^2-4ac = -80  =>  c = (b^2+80)/(4a)
        if a > c:
            a, b, c = c, -b, a            # the S-move
            continue
        if a == c and b < 0:
            b = -b
        return (a, b, c)

DICT = {(3,-2,7): '+i', (3,2,7): '-i', (1,0,20): '+1', (4,0,5): '-1'}

def locate(p):
    r = root_conv(p)
    rp2 = (2*r) % p
    if (rp2*rp2 + 20) % p != 0:
        rp2 = p - rp2
    c0 = (rp2*rp2 + 20)//p
    term = reduce_form(p, 2*rp2, c0)
    return term, DICT.get(term, '??')

# ---------- analytic certificate at one blind prime ----------
import mpmath as mpm
mpm.mp.dps = 40
def j_from_tau(tau):
    q = mpm.exp(1j*mpm.pi*tau)
    t2 = mpm.jtheta(2,0,q); t3 = mpm.jtheta(3,0,q)
    L = (t2/t3)**4
    return 256*(1-L+L**2)**3/(L**2*(1-L)**2)

def tau_of(form):
    a,b,c = form
    return (-b + mpm.sqrt(-80))/(2*a)

# ---------- grading data (key path) ----------
FROZEN_KEY = {3:'+i', 7:'-i', 23:'-i', 43:'+i', 47:'+i', 67:'-i', 83:'-i',
              103:'+i', 107:'-i', 127:'-i', 163:'+i', 167:'+i', 223:'+i', 227:'-i', 263:'+i', 283:'-i'}

# eta(4t)eta(20t) coefficients (independent: pentagonal expansion)
NE = 2000
def eta_product(deltas, N):
    pref = sum(deltas); shift = pref // 24
    coeffs = [0]*(N+1); coeffs[0] = 1
    for d in deltas:
        pent = {}
        k = 0
        while True:
            e1 = k*(3*k-1)//2; e2 = k*(3*k+1)//2
            if d*min(e1,e2) > N and k > 0: break
            for e in {e1,e2}:
                if d*e <= N: pent[d*e] = pent.get(d*e,0) + ((-1)**(k%2))
            k += 1
        new = [0]*(N+1)
        for e,cc in pent.items():
            if cc == 0: continue
            for i in range(0, N+1-e):
                if coeffs[i]: new[i+e] += cc*coeffs[i]
        coeffs = new
    out = [0]*(N+1)
    for i in range(0, N+1-shift): out[i+shift] = coeffs[i]
    return out
eta_c = eta_product([4,20], NE)

# ---------- run: nonprincipal (vs frozen key) ----------
print("== NONPRINCIPAL split primes: reduction-flow locator vs FROZEN KEY ==")
fit_ok = blind_ok = fit_n = blind_n = 0
for p in sorted(FROZEN_KEY):
    term, pred = locate(p)
    truth = FROZEN_KEY[p]
    zone = 'fit  ' if p < 100 else 'BLIND'
    hit = (pred == truth)
    if p == 3:
        tag = 'GAUGE'
    else:
        tag = 'ok' if hit else 'MISS'
        if p < 100: fit_n += 1; fit_ok += hit
        else: blind_n += 1; blind_ok += hit
    print(f"  p={p:>3} [{zone}] terminal chart {str(term):>10}  ->  {pred}   key: {truth}   {tag}")
print(f"  fit zone: {fit_ok}/{fit_n}   BLIND zone: {blind_ok}/{blind_n}")

# ---------- run: principal (vs eta coefficients) ----------
print("\n== PRINCIPAL split primes: locator-predicted a_p = 2*psi vs eta(4t)eta(20t) ==")
pr_ok = pr_n = 0
for p in range(3, 300):
    if split_type(p) == 'principal':
        term, pred = locate(p)
        pa = {'+1': 2, '-1': -2}.get(pred)
        truth = eta_c[p]
        hit = (pa == truth)
        pr_n += 1; pr_ok += hit
        print(f"  p={p:>3} terminal {str(term):>10} -> psi {pred} -> a_p {pa:+d}   eta coeff: {truth:+d}   {'ok' if hit else 'MISS'}")
print(f"  principal grade: {pr_ok}/{pr_n}")

# ---------- analytic certificate (one blind prime) ----------
p = 227
r = root_conv(p); rp2 = (2*r) % p
if (rp2*rp2+20) % p: rp2 = p - rp2
z = (-rp2 + mpm.sqrt(-80))/(2*p)*2   # z_p = (-r' + i sqrt20)/p ; sqrt(-80)/2 = i sqrt20
z = (-rp2 + mpm.sqrt(-80)/2*2/2*2)/ (2*p) * 2  # (avoid confusion: recompute plainly)
z = (mpm.mpf(-rp2) + 1j*mpm.sqrt(20))/p
jz = j_from_tau(z)
term, _ = locate(p)
jt = j_from_tau(tau_of(term))
print(f"\n== analytic certificate at blind p=227: |j(z_p) - j(terminal chart)| = {float(abs(jz-jt)):.2e}")
print(f"   (PSL2-invariance: the raw p-local point and the terminal chart carry the same value)")
print(f"   j at the four charts: [1,0,20]: {complex(j_from_tau(tau_of((1,0,20)))):.6e}")
print(f"                         [4,0,5] : {complex(j_from_tau(tau_of((4,0,5)))):.6e}")
print(f"                         [3,2,7] : {complex(j_from_tau(tau_of((3,2,7)))):.4e}")
print(f"                         [3,-2,7]: {complex(j_from_tau(tau_of((3,-2,7)))):.4e}")
