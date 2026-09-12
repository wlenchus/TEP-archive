RS6 = X^6-100*X^4+6000*X^2+32000*X+40000;
print("RS6 irreducible over Q: ", polisirreducible(RS6));
print("RS6 number of real roots (Sturm): ", polsturm(RS6));
print("RS6 galois group: ", polgalois(RS6));
K = nfinit(y^2-5);
fa = nffactor(K, RS6);
print("RS6 factor degrees over Q(sqrt5): ", apply(poldegree, fa[,1]~));
