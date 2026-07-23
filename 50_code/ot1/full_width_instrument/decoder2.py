"""Decoder v2 — generic weight-lifting membership decoder.

Adds: ramified unknowns (a_2, a_5 as sign-bit monomials with unit u in {1,i}),

parametrized depth/host, gauge resolution of nullspace, decoded-a_p reporting.

"""

import numpy as np

from fractions import Fraction

from functools import lru_cache

from sympy import primerange, factorint

import decoder as D  # reuse qmul/qadd/qscale, kron, cycle_type, parity5, E1_series pieces



Z4=(Fraction(0),)*4; ONE=D.ONE; IU=D.IU; PHI=D.PHI; IPHI=D.IPHI



@lru_cache(maxsize=None)

def fac(m): return tuple(sorted(factorint(m).items()))



_pdata_cache={}

def pdata_quintic(depth):

    if depth in _pdata_cache: return _pdata_cache[depth]

    pd={}

    for p in primerange(3, depth+1):

        if p==5: continue

        ct=D.cycle_type(p)

        if ct==(1,1,1,1,1): pd[p]=('1',None)

        elif ct==(2,2,1):   pd[p]=('2',None)

        elif ct==(3,1,1):   pd[p]=('3',None)

        else:               pd[p]=('5',D.parity5(p))

    _pdata_cache[depth]=pd

    return pd



def pdata_cm20(depth):

    pd={}

    for p in primerange(3, depth+1):

        if p==5: continue

        pd[p]=('1',None) if D.kron(-20,p)==1 else ('2',None)

    return pd



def ppow_table(p, cls, par, chiD, emb, kmax):

    chi=D.kron(chiD,p)

    u=ONE if chi==1 else IU

    mag={'1':D.qscale(Fraction(2),ONE),'2':Z4,'3':ONE}.get(cls)

    if cls=='5':

        mag = PHI if ((par==+1) ^ (emb==1)) else IPHI

    tau=D.qmul(mag,u)

    A=[ONE,Z4]; B=[Z4,tau]

    for k in range(1,kmax):

        A.append(D.qadd(D.qmul(tau,B[k]),D.qscale(Fraction(-chi),A[k-1])))

        B.append(D.qadd(D.qmul(tau,A[k]),D.qscale(Fraction(-chi),B[k-1])))

    return A,B



def ram_table(u, kmax):

    """a_{p^k} = (u s)^k: A_k = u^k [k even], B_k = u^k [k odd]."""

    A=[ONE]; B=[Z4]; cur=ONE

    for k in range(1,kmax+1):

        cur=D.qmul(cur,u)

        A.append(cur if k%2==0 else Z4)

        B.append(cur if k%2==1 else Z4)

    return A,B



def build_f2(pdata, chiD, emb, depth, ram):

    tables={}

    for p,(cls,par) in pdata.items():

        kmax=1

        while p**(kmax+1)<=depth: kmax+=1

        tables[p]=ppow_table(p,cls,par,chiD,emb,kmax)

    for p,u in ram.items():

        if u is None: continue

        kmax=1

        while p**(kmax+1)<=depth: kmax+=1

        tables[p]=ram_table(u,kmax)

    F={1:{frozenset():ONE}}

    for m in range(2, depth+1):

        fs=fac(m); d={frozenset():ONE}; dead=False

        for p,e in fs:

            if p in (2,5) and ram.get(p) is None: dead=True; break

            A,B=tables[p]

            term={}

            if any(A[e]): term[frozenset()]=A[e]

            if any(B[e]): term[frozenset([p])]=B[e]

            if not term: dead=True; break

            nd={}

            for T1,v1 in d.items():

                for T2,v2 in term.items():

                    T=T1|T2; v=D.qmul(v1,v2)

                    nd[T]=D.qadd(nd[T],v) if T in nd else v

            d=nd

        if not dead: F[m]=d

    return F



def rref_modp(M,p):

    M=M%p; rows,cols=M.shape; piv=[]; r=0

    for c in range(cols):

        nz=np.nonzero(M[r:,c])[0]

        if nz.size==0: continue

        i=r+int(nz[0]); M[[r,i]]=M[[i,r]]

        M[r]=(M[r]*pow(int(M[r,c]),p-2,p))%p

        col=M[:,c].copy(); col[r]=0

        M=(M-np.outer(col,M[r]))%p

        piv.append(c); r+=1

        if r==rows: break

    return M[:r],piv



def make_reducer(host,p):

    R,piv=rref_modp(host.copy(),p)

    pivset=set(piv); nonpiv=[c for c in range(host.shape[1]) if c not in pivset]

    def residual(v):

        w=v%p

        for i,c in enumerate(piv):

            if w[c]: w=(w-w[c]*R[i])%p

        return w[nonpiv]

    return residual,len(piv)



def run(host, pdata, chiD, emb, depth, ram, p, gauge=True, report=False):

    ncol=depth+1

    F=build_f2(pdata,chiD,emb,depth,ram)

    E=D.E1_series(chiD)[:depth]

    Emod=np.array([(int(e.numerator)%p)*pow(int(e.denominator)%p,p-2,p)%p for e in E],dtype=np.int64)

    blocks={}

    for m,d in F.items():

        if m>depth: continue

        for T,v in d.items():

            for c in range(4):

                x=v[c]

                if x==0: continue

                if T not in blocks: blocks[T]=np.zeros((4,ncol),dtype=np.int64)

                xm=(int(x.numerator)%p)*pow(int(x.denominator)%p,p-2,p)%p

                L=min(len(E),ncol-m)

                blocks[T][c,m:m+L]=(blocks[T][c,m:m+L]+xm*Emod[:L])%p

    reducer,hrank=make_reducer(host,p)

    Ts=[]; cols=[]; b=None

    for T,arr in blocks.items():

        flat=np.concatenate([reducer(arr[c]) for c in range(4)])

        if T==frozenset(): b=(-flat)%p

        else: Ts.append(T); cols.append(flat)

    A=np.stack(cols,axis=1)%p

    Aug=np.concatenate([A,b.reshape(-1,1)],axis=1)

    R,piv=rref_modp(Aug,p)

    nT=len(Ts)

    if nT in piv: return dict(status='REJECT', rank=len(piv))

    sol=np.zeros(nT,dtype=np.int64)

    for i,c in enumerate(piv): sol[c]=R[i,nT]

    free=[c for c in range(nT) if c not in piv]

    # nullspace basis

    null=[]

    for fcol in free:

        v=np.zeros(nT,dtype=np.int64); v[fcol]=1

        for i,c in enumerate(piv): v[c]=(-R[i,fcol])%p

        null.append(v)

    def pm(x): return x==1 or x==p-1

    def as_sign(x): return 1 if x==1 else (-1 if x==p-1 else None)

    cands=[sol]

    if gauge and len(free)>0 and len(free)<=2:

        import itertools

        cands=[]

        for coeffs in itertools.product(range(-1,2),repeat=len(free)):

            v=sol.copy()

            for cf,nv in zip(coeffs,null): v=(v+cf*nv)%p

            cands.append(v)

        # also solve free coeff to force a chosen singleton to +-1

        extra=[]

        for nv in null:

            supp=[k for k in range(nT) if nv[k] and len(Ts[k])==1]

            if supp:

                k=supp[0]; inv=pow(int(nv[k]),p-2,p)

                for tgt in (1,p-1):

                    c=((tgt-sol[k])*inv)%p

                    extra.append((sol+c*nv)%p)

        cands+=extra

    best=None

    for v in cands:

        sing={next(iter(Ts[k])):v[k] for k in range(nT) if len(Ts[k])==1}

        if not all(pm(x) for x in sing.values()): continue

        ok=True

        for k in range(nT):

            if len(Ts[k])>1:

                prod=1

                for q in Ts[k]: prod=(prod*sing[q])%p

                if v[k]!=prod: ok=False; break

        if ok: best=({q:as_sign(x) for q,x in sing.items()},v); break

    if best is None:

        return dict(status='SOLVED-NO-GAUGE', free=len(free), rank=len(piv))

    signs,_=best

    out=dict(status='PASS', free=len(free), signs=signs)

    return out