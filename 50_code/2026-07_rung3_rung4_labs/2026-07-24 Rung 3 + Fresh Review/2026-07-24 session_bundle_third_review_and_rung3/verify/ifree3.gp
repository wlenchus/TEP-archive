RS6 = X^6-100*X^4+6000*X^2+32000*X+40000;
print("irreducible/Q: ", polisirreducible(RS6));
print("real roots (Sturm): ", polsturm(RS6));
r = polroots(RS6);
for(i=1,6, print("  root ",i,": ", precision(r[i], 10)));
