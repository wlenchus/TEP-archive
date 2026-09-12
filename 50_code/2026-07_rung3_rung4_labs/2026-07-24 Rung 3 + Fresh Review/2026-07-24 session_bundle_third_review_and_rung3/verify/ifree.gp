default(parisize, 800000000);
RS6 = X^6-100*X^4+6000*X^2+32000*X+40000;
print("RS6 irreducible: ", polisirreducible(RS6));
print("RS6 galois group (deg 6): ", polgalois(RS6));
\\ compositum K12 = RS6 . Q(sqrt5)
comp = polcompositum(RS6, X^2-5);
K12 = comp[#comp];
print("K12 degree: ", poldegree(K12));
\\ does K12 contain i?  (x^2+1 has a root in K12?)
print("i in K12: ", #nfisincl(x^2+1, K12) > 0);
print("sqrt5 in K12 (control, must be 1): ", #nfisincl(x^2-5, K12) > 0);
\\ and the quintic's own splitting-relevant fields: does the degree-5 field contain i? (sanity)
print("i in E1 (control, must be 0): ", #nfisincl(x^2+1, x^5+20*x+16) > 0);
