\\ step3_verify.gp -- independent PARI cross-check of LMFDB candidates (COMPUTE phase)
locembed(g, h) = {  \\ 1 if Q2[x]/(g) embeds into Q2[x]/(h); deg g <= deg h
  my(cs, fp, target = poldegree(h));
  if (g == h, return(1));
  cs = polcompositum(g, h);
  for (i = 1, #cs,
    fp = factorpadic(cs[i], 2, 200);
    for (j = 1, #fp[,1],
      if (poldegree(fp[j,1]) == target, return(1))));
  0;
}

K4    = x^4 + 2*x^3 + 2*x^2 + 2;            \\ LMFDB 2.4.6.7
oct1  = x^8 + 2*x^7 + 6;                    \\ LMFDB 2.8.14.1
oct2  = x^8 + 2*x^7 + 2;                    \\ LMFDB 2.8.14.2
m85   = x^16 + 2*x^14 + 4*x^5 + 4*x^3 + 2;  \\ LMFDB 2.16.34.85
m87   = x^16 + 2*x^14 + 4*x^5 + 4*x^3 + 6;  \\ LMFDB 2.16.34.87
q221  = x^2 + 2*x + 2;                      \\ LMFDB 2.2.2.1
q222  = x^2 + 2*x + 6;                      \\ LMFDB 2.2.2.2

chk(pol, name) = {
  my(K = nfinit([pol, [2]]), pr = idealprimedec(K, 2));
  print(name, ": irred/Q2 = ", #factorpadic(pol,2,200)[,1] == 1,
        " ; #primes|2 = ", #pr,
        " ; e = ", pr[1].e, " f = ", pr[1].f,
        " ; v2(disc) = ", valuation(K.disc, 2),
        " ; Eisenstein: ", valuation(polcoef(pol,0),2)==1);
}

{
print("--- identify the ramified quadratics (det-character fields) ---");
print("2.2.2.1 = Q2(sqrt(-1)) ? ", locembed(x^2+1, q221),
      "   2.2.2.1 = Q2(sqrt(-5)) ? ", locembed(x^2+5, q221));
print("2.2.2.2 = Q2(sqrt(-1)) ? ", locembed(x^2+1, q222),
      "   2.2.2.2 = Q2(sqrt(-5)) ? ", locembed(x^2+5, q222));
print();
print("--- octic candidates (claim: e=8, f=1, c=14, Eisenstein) ---");
chk(oct1, "2.8.14.1  x^8+2x^7+6");
chk(oct2, "2.8.14.2  x^8+2x^7+2");
print();
print("--- octics contain K4 = 2.4.6.7 (canonical A4-quartic)? ---");
print("K4 in 2.8.14.1 ? ", locembed(K4, oct1));
print("K4 in 2.8.14.2 ? ", locembed(K4, oct2));
print("   [step1b already proved: P1-factor ~ P2-factor ~ K4-canonical, so this");
print("    containment transfers to BOTH quintics' actual quartic factors]");
print();
print("--- degree-16 minimal candidates (claim: e=16, f=1, c=34) ---");
chk(m85, "2.16.34.85  x^16+2x^14+4x^5+4x^3+2");
chk(m87, "2.16.34.87  x^16+2x^14+4x^5+4x^3+6");
}
quit
