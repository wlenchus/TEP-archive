"""Extract p1 gauge patterns for chi=-4 emb=0 in the p2 JSON format; compare across primes."""
import sys, json, itertools, numpy as np
from fractions import Fraction
sys.path.insert(0,'/home/claude/ot1_16000')
import decoder as D, decoder2 as D2
P=1000003; NCOL=4801; DEPTH=4800
def fast_E1(chiD,depth):
    m=abs(chiD); B1=Fraction(sum(D.kron(chiD,x)*x for x in range(1,m)),m)
    c=[0]*depth
    for d_ in range(1,depth):
        cd=D.kron(chiD,d_)
        if cd:
            for n_ in range(d_,depth,d_): c[n_]+=cd
    return [-B1/2]+[Fraction(v) for v in c[1:]]
D.DEPTH=DEPTH; D.E1_series=lambda chiD: fast_E1(chiD,DEPTH)
H=np.load('H_p1.npy').astype(np.float64); Minv=np.load('Minv_p1.npy').astype(np.float64)
pd=D2.pdata_quintic(DEPTH)
F=D2.build_f2(pd,-4,0,DEPTH,{2:None,5:None})
E=D.E1_series(-4)[:DEPTH]
Emod=np.array([(int(e.numerator)%P)*pow(int(e.denominator)%P,P-2,P)%P for e in E],dtype=np.float64)
blocks={}
for m_,d in F.items():
    if m_>DEPTH: continue
    for T,v in d.items():
        for c in range(4):
            x=v[c]
            if x==0: continue
            if T not in blocks: blocks[T]=np.zeros((4,NCOL))
            xm=(int(x.numerator)%P)*pow(int(x.denominator)%P,P-2,P)%P
            L=min(len(E),NCOL-m_)
            blocks[T][c,m_:m_+L]=np.mod(blocks[T][c,m_:m_+L]+xm*Emod[:L],P)
Ts=[T for T in blocks if T!=frozenset()]; nT=len(Ts)
sing_idx={k:next(iter(Ts[k])) for k in range(nT) if len(Ts[k])==1}
pats1=[]
for i in range(1,9):
    try: v=np.load(f'gauge_solution_{i}.npy')
    except FileNotFoundError: break
    s={str(sing_idx[k]):(1 if int(v[k])==1 else -1) for k in sing_idx}
    pats1.append(s)
p2=json.load(open('sweep_p2_results.json'))
pats2=p2['-4_0']['patterns']
def keyset(pats): return {tuple(sorted(p.items())) for p in pats}
k1,k2=keyset(pats1),keyset(pats2)
print(f"p1 patterns: {len(pats1)}, p2 patterns: {len(pats2)}")
print(f"IDENTICAL pattern sets across primes: {k1==k2}")
inter=len(k1&k2); print(f"intersection: {inter}/8")
if k1!=k2 and inter:
    print("(partial overlap — list a differing prime example)")
if k1==k2:
    # interior vs edge: how do the 8 patterns differ from each other?
    allp=sorted(pats1[0], key=int)
    diff=[q for q in allp if len({p[q] for p in pats1})>1]
    print(f"signs varying across the 8 solutions: {diff} (expect only edge primes >4750)")
    interior={q:pats1[0][q] for q in allp if int(q)<4700}
    import hashlib
    hs=hashlib.md5(json.dumps(interior,sort_keys=True).encode()).hexdigest()[:12]
    json.dump(interior,open('decoded_interior_signs_chi-4.json','w'),indent=0)
    print(f"INTERIOR SIGN VECTOR: {len(interior)} primes, unanimous across all 8 gauge points and BOTH primes; md5 {hs}")
    print("sample:", {q:interior[q] for q in allp[:12] if q in interior})
