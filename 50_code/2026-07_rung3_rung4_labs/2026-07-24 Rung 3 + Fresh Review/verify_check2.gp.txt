\\ Trace-form verification for the two A5 quintics
f1 = x^5+20*x+16;          \\ E1
f2 = x^5+10*x^3-10*x^2+35*x-18;  \\ Buhler

hasse(diag, p) = {my(e=1); for(i=1,#diag, for(j=i+1,#diag, e *= hilbert(diag[i],diag[j],p))); e};

tfdata(f) = {
  my(n=poldegree(f), s=vector(2*n-1), G, D, diag, dets);
  \\ Newton power sums s_k = Tr(theta^k), s[k+1] indexes k
  my(ps = polsym(f, 2*n-2));
  G = matrix(n,n,i,j, ps[i+j-1]);
  D = qfgaussred(G);           \\ upper triangular with diagonal = coefficients
  diag = vector(n,i, D[i,i]);
  [G, diag]
};

print("=== E1 = x^5+20x+16 ===");
print("polgalois: ", polgalois(f1), "  (expect [60,1,...] = A5)");
print("disc(f1) = ", poldisc(f1), " = ", factor(poldisc(f1)));
t1 = tfdata(f1); d1 = t1[2];
print("diagonal (Gauss): ", d1);
sig1 = [sum(i=1,#d1, sign(d1[i])>0), sum(i=1,#d1, sign(d1[i])<0)];
print("signature: ", sig1);
det1 = core(numerator(prod(i=1,5,d1[i]))*denominator(prod(i=1,5,d1[i])));
print("det square-class: ", det1);
forprime(p=2, 200, my(e=hasse(d1,p)); if(e==-1, print("  eps_",p," = -1")));
print("  eps_oo = ", hasse(d1, 0));  \\ hilbert with p=0 is the real place in PARI? check below
print("  [real-place check: neg entries pairs] eps_inf = ", (-1)^(binomial(sig1[2],2)));

print("=== E2 = Buhler ===");
print("polgalois: ", polgalois(f2));
print("disc(f2) = ", factor(poldisc(f2)));
t2 = tfdata(f2); d2 = t2[2];
print("diagonal (Gauss): ", d2);
sig2 = [sum(i=1,#d2, sign(d2[i])>0), sum(i=1,#d2, sign(d2[i])<0)];
print("signature: ", sig2);
det2 = core(numerator(prod(i=1,5,d2[i]))*denominator(prod(i=1,5,d2[i])));
print("det square-class: ", det2);
forprime(p=2, 200, my(e=hasse(d2,p)); if(e==-1, print("  eps_",p," = -1")));

print("=== isometry test (rank, det, signature, all Hasse) ===");
same = (sig1==sig2) && (det1==det2);
forprime(p=2,1000, if(hasse(d1,p)!=hasse(d2,p), same=0; print("  MISMATCH at p=",p)));
print("q_E1 ~ q_E2 over Q: ", if(same,"YES (all invariants agree)","NO"));

print("=== reference class (-1,-1): eps_2 ===");
print("hilbert(-1,-1,2) = ", hilbert(-1,-1,2), "  hilbert(-1,-1,5) = ", hilbert(-1,-1,5));

print("=== 2-adic and 5-adic factorization shapes ===");
print("E1 over Q2: ", apply(t->poldegree(t), factorpadic(f1,2,30)[,1]~));
print("E2 over Q2: ", apply(t->poldegree(t), factorpadic(f2,2,30)[,1]~));
print("E1 over Q5: ", apply(t->poldegree(t), factorpadic(f1,5,30)[,1]~));
print("E2 over Q5: ", apply(t->poldegree(t), factorpadic(f2,5,30)[,1]~));

print("=== field discs ===");
print("E1 field disc: ", nfdisc(f1), " = ", factor(nfdisc(f1)));
print("E2 field disc: ", nfdisc(f2), " = ", factor(nfdisc(f2)));

print("=== marking-rule spot data: ramification of E1/E2 at 2,3,5 (e,f per factor) ===");
lf(f,p) = {my(fa=factorpadic(f,p,30)); vector(#fa[,1], i, my(g=fa[i,1]); [poldegree(g), idealstuff(g,p)])};
\\ simpler: e via poldisc valuation per factor is messy; report factor degrees + nfdisc valuations
print("v2(nfdisc E1) = ", valuation(nfdisc(f1),2), "  v5(nfdisc E1) = ", valuation(nfdisc(f1),5));
print("v2(nfdisc E2) = ", valuation(nfdisc(f2),2), "  v5(nfdisc E2) = ", valuation(nfdisc(f2),5));
