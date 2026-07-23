"""Reconstruction of the inline twist-orbit analysis (recorded result: the 8 gauge
solutions of each branch form the exact orbit under the 7 nontrivial quadratic
characters of conductor | 40; chi_-4[0] vs chi_-20 related by no single quadratic
character, as required). Run against sweep_p2_results.json."""
import json
from sympy import jacobi_symbol, factorint
def kron(D,n):
    v=1
    for p,e in factorint(n).items():
        if p==2:
            if D%2==0: return 0
            s=1 if D%8 in (1,7) else -1
        else:
            if D%p==0: return 0
            s=int(jacobi_symbol(D,p))
        if e%2==1: v*=s
    return v
res=json.load(open('sweep_p2_results.json'))
for branch in ('-4_0','-20_0'):
    pats=res[branch]['patterns']; base=pats[0]
    core=[q for q in sorted(int(x) for x in base) if q<4700]
    print(f"branch {branch}:")
    for j in range(1,len(pats)):
        flips={q for q in core if pats[j][str(q)]!=base[str(q)]}
        hit=next((D for D in (5,8,40,-4,-8,-20,-40)
                  if not flips^{q for q in core if kron(D,q)==-1}), None)
        print(f"  sol{j}: {'chi_'+str(hit) if hit else 'no single-character match'}")
