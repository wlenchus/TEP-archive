"""Independent spot-check of MAASS-LIVE at Doud-1951 — fresh code path, fresh group

elements, fresh points. 2026-08-09 (session B), Claude (Fable 5). dps=34, nmax=40000.

&nbsp;

Spec followed (PREREG\_maass\_live\_20260809): F(z) \= sqrt(y) \* sum c\_n K0(2\*pi\*n\*y)

\* (e(nx)-e(-nx)), sin-type, lambda=1/4; c\_n multiplicative, Hecke recursion with

chi(p)=zeta5^j5, a\_1951 \= zeta10^2, chi(1951)=0; automorphy F(gz) \= chi(d) F(z)

for g=\[\[a,b\],\[N,d\]\]; Fricke F(-1/(Nz)) \= \-eps \* G(z), G \= conjugate coefficients.

&nbsp;

INDEPENDENCE: coefficients re-assembled from the exact SYMBOLIC CSV columns (not

the float columns, not their assembler); K0 via own asymptotic split; NEW d values

{11, 23} — d=11 exercises chi \= zeta5^3, a nebentypus value ABSENT from the

certified run (their d in {2,3,7} hit zeta5^{4,1,2}) — and NEW points s,y.

&nbsp;

PREDICTIONS (stated before run):

  V-a  Both fresh pairs pass automorphy under branch chi(d) at residual \<= 1e-20.

  V-b  Corrupting a\_113 (-1 \-\> \+1) breaks pair-1 automorphy by \>= 8 orders.

  V-c  Fricke: |const| \= 1 to \<= 1e-18; const matches \-eps\_committed to \<= 3e-5

       (eps recorded to \~1e-6).

Kill: any failure is reported as-is; if the parse self-test fails, no verdict."""

import csv, time, math

from mpmath import mp, mpf, mpc, besselk, sqrt, sin, cos, exp, pi, conj, fabs, mpmathify

&nbsp;

mp.dps \= 34

CSV \= "/root/.claude/projects/-home-claude/e1c6a220-faa1-5bd1-9d10-c0c3344b96cd/tool-results/project-doc-b99b6076-631d-43e3-92a2-b1e8923dc0c4.txt"

N \= 1951

NMAX \= 40000

&nbsp;

phi \= (1 \+ sqrt(5))/2

def zeta10(k): return exp(mpc(0,1)\*pi\*k/5)

def zeta5(j):  return exp(mpc(0,2)\*pi\*j/5)

&nbsp;

def parse\_apex(s):

    s \= s.strip()

    if s \== "0": return mpc(0)

    sign \= mpf(1)

    if s\[0\] \== '+': s \= s\[1:\]

    elif s\[0\] \== '-': sign \= mpf(-1); s \= s\[1:\]

    fac \= mpf(1)

    if s.endswith("\*1/phi"): fac \= 1/phi; s \= s\[:-6\]

    elif s.endswith("\*phi"): fac \= phi; s \= s\[:-4\]

    elif s.endswith("\*2"): fac \= mpf(2); s \= s\[:-2\]

    assert s.startswith("zeta10^"), s

    k \= int(s\[7:\])

    return sign \* fac \* zeta10(k)

&nbsp;

ap \= {}; chi \= {}; j5tab \= {}

parse\_dev \= mpf(0); nrows \= 0

with open(CSV) as f:

    for row in csv.DictReader(f):

        p \= int(row\['p'\])

        a \= parse\_apex(row\['a\_p\_exact'\])

        c \= mpc(0) if row\['chi\_p\_exact'\].strip() \== '0' else zeta5(int(row\['chi\_p\_exact'\].strip()\[6:\]))

        ap\[p\] \= a; chi\[p\] \= c

        j5tab\[p\] \= row\['j5'\].strip()

        if nrows \< 300:   \# parse self-test vs float columns

            dev \= fabs(a \- mpc(mpmathify(row\['Re\_a\_p'\]), mpmathify(row\['Im\_a\_p'\])))

            parse\_dev \= max(parse\_dev, dev)

        nrows \+= 1

print(f"rows: {nrows}; parse self-test max |symbolic \- float cols| \= {float(parse\_dev):.2e}")

assert parse\_dev \< mpf('2e-15'), "PARSE SELF-TEST FAILED \- no verdict"

&nbsp;

\# smallest-prime-factor sieve and multiplicative assembly

spf \= list(range(NMAX+1))

for i in range(2, int(NMAX\*\*0.5)+1):

    if spf\[i\] \== i:

        for m in range(i\*i, NMAX+1, i):

            if spf\[m\] \== m: spf\[m\] \= i

def assemble(aptab):

    c \= \[None\]\*(NMAX+1); c\[1\] \= mpc(1)

    for n in range(2, NMAX+1):

        p \= spf\[n\]; k \= 1; m \= n

        while m % p \== 0 and spf\[m\] \== p and m \> 1:

            m //= p;

        \# m \= n with all factors p removed? redo cleanly:

        m \= n; k \= 0

        while m % p \== 0: m //= p; k \+= 1

        \# c\[p^k\] via recursion stored on the fly

        pk \= p\*\*k

        if c\[pk\] is None:

            cm1, c0 \= mpc(1), aptab.get(p, None)

            if c0 is None: raise KeyError(f"prime {p} missing")

            prev, cur \= mpc(1), c0

            for \_ in range(k-1):

                prev, cur \= cur, aptab\[p\]\*cur \- chi\[p\]\*prev

            c\[pk\] \= cur if k \>= 1 else mpc(1)

        c\[n\] \= c\[pk\] if m \== 1 else c\[pk\]\*c\[m\]

    return c

&nbsp;

t0 \= time.time()

cn \= assemble(ap)

mx \= max(abs(cn\[n\]) for n in range(1, NMAX+1))

print(f"assembled c\_n to {NMAX} in {time.time()-t0:.1f}s; max|c\_n| \= {float(mx):.4f}")

&nbsp;

\# K0: mpmath below u=32, asymptotic with min-term guard above

def K0(u):

    if u \< 32: return besselk(0, u)

    S \= mpf(1); term \= mpf(1); k \= 0

    while True:

        nxt \= term \* (-(2\*k+1)\*\*2) / (8\*u\*(k+1))

        if abs(nxt) \>= abs(term) or abs(nxt) \< mpf('1e-40'): break

        S \+= nxt; term \= nxt; k \+= 1

    return sqrt(pi/(2\*u)) \* exp(-u) \* S

&nbsp;

def point\_vectors(y):

    twopiy \= 2\*pi\*y

    return \[K0(twopiy\*n) for n in range(1, NMAX+1)\]

&nbsp;

def F\_from(coeffs, Kv, x, y):

    tot \= mpc(0)

    twopix \= 2\*pi\*x

    for n in range(1, NMAX+1):

        tot \+= coeffs\[n\]\*Kv\[n-1\]\*sin(twopix\*n)

    return sqrt(y) \* 2j \* tot

&nbsp;

def tailbound(y):

    \# sum\_{n\>NMAX} d(n)\*phi\*sqrt(y)\*K0(2 pi n y)  with K0(u)\<=sqrt(pi/2u)e^-u, d(n)\<=n

    s \= mpf(0); twopiy \= 2\*pi\*y

    for n in range(NMAX+1, NMAX+3001):

        u \= twopiy\*n

        s \+= n\*phi\*sqrt(y)\*sqrt(pi/(2\*u))\*exp(-u)

    r \= exp(-twopiy)      \# geometric remainder factor

    s \+= (NMAX+3001)\*phi\*sqrt(y)\*sqrt(pi/(2\*twopiy\*(NMAX+3001)))\*exp(-twopiy\*(NMAX+3001))/(1-r)

    return s

&nbsp;

def inverse\_mod(d, n):

    return pow(d, \-1, n)

&nbsp;

results \= {}

Kcache \= {}

def run\_pair(d, s):

    t0 \= time.time()

    a \= inverse\_mod(d, N); b \= (a\*d \- 1)//N

    assert a\*d \- b\*N \== 1

    y \= mpf('1.15')/N

    x \= (mpf(-d) \+ mpf(str(s)))/N

    z \= mpc(x, y)

    den \= N\*z \+ d

    zp \= (a\*z \+ b)/den

    xp, yp \= zp.real, zp.imag

    tb1, tb2 \= tailbound(y), tailbound(yp)

    Kv1 \= Kcache.setdefault(('y', float(y)), point\_vectors(y))

    Kv2 \= point\_vectors(yp)

    F1 \= F\_from(cn, Kv1, x, y); F2 \= F\_from(cn, Kv2, xp, yp)

    chid \= zeta5(int(j5tab\[d\]))

    R  \= abs(F2 \- chid\*F1)/max(abs(F1), abs(F2))

    Rb \= abs(F2 \- conj(chid)\*F1)/max(abs(F1), abs(F2))   \# losing branch

    print(f"pair d={d} (chi=zeta5^{j5tab\[d\]}), s={s}: y'={float(yp):.3e}  "

          f"tails=({float(tb1):.1e},{float(tb2):.1e})  R\[chi\]={float(R):.3e}  "

          f"R\[chibar\]={float(Rb):.3e}   ({time.time()-t0:.0f}s)")

    results\[d\] \= (x, y, Kv1, Kv2, xp, yp, F1, F2, chid, R)

    return R

&nbsp;

R11 \= run\_pair(11, 0.41)

R23 \= run\_pair(23, 0.66)

&nbsp;

\# corruption control: a\_113: \-1 \-\> \+1

apc \= dict(ap); apc\[113\] \= \-ap\[113\]

cc \= assemble(apc)

(x, y, Kv1, Kv2, xp, yp, F1, F2, chid, R) \= results\[11\]

F1c \= F\_from(cc, Kv1, x, y); F2c \= F\_from(cc, Kv2, xp, yp)

Rc \= abs(F2c \- chid\*F1c)/max(abs(F1c), abs(F2c))

print(f"corruption (a\_113 sign flip): R \= {float(Rc):.3e}  vs clean {float(R):.3e}  "

      f"-\> {float(mp.log10(Rc/R)):.1f} orders")

&nbsp;

\# Fricke at one fresh point

t0 \= time.time()

z0 \= mpc(mpf('0.4')/N, mpf('1.15')/N)

w  \= \-1/(N\*z0)

cbar \= \[None\] \+ \[conj(cn\[n\]) for n in range(1, NMAX+1)\]

Kvz \= Kcache\[('y', float(z0.imag))\] if ('y', float(z0.imag)) in Kcache else point\_vectors(z0.imag)

Kvw \= point\_vectors(w.imag)   \# w.imag is O(1): K0 tiny beyond \~20 terms, vector cheap

Fw \= F\_from(cn, Kvw, w.real, w.imag)

Gz \= F\_from(cbar, Kvz, z0.real, z0.imag)

const \= Fw/Gz

eps \= mpc(mpf('0.885096'), mpf('-0.465408'))

print(f"Fricke: |const|-1 \= {float(abs(const)-1):.3e};  const \= {complex(const):.9f}; "

      f"const-(-eps) \= {float(abs(const+eps)):.3e}   ({time.time()-t0:.0f}s)")

print("\\nVERDICTS: V-a", "PASS" if max(float(R11),float(R23))\<1e-20 else "FAIL",

      "| V-b", "PASS" if mp.log10(Rc/R) \>= 8 else "FAIL",

      "| V-c", "PASS" if (abs(abs(const)-1) \< mpf('1e-18') and abs(const+eps) \< mpf('3e-5')) else "FAIL")