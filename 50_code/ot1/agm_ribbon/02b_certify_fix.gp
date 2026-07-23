\\ AGM ribbon - LINK 1->2 certification, repaired:
\\ (B2) skip primes dividing the model conductor (bad-reduction artifact at p=3);
\\ (C2) widened quadratic-twist probe incl. fundamental unit eps=(1+sqrt5)/2 and
\\      3/89-supported twists, to find the twist-minimal conductor support.
default(parisize, 512*1024*1024);

projord(a, q) = {
  my(M = Mod([0, -q; 1, a], 5), P = M);
  for(n = 1, 6,
    if(P[1,2] == 0 && P[2,1] == 0 && P[1,1] == P[2,2], return(n));
    P = P*M);
  return(0);
};
quintord2(f, p) = {
  my(fa = factormod(f, p), degs = vector(#fa[,1], i, poldegree(fa[i,1])));
  lcm(degs);
};

K = nfinit(t^2 - 5);
F5q = x^5 + 20*x + 16;

print("== (B2) Certification with bad-model primes excluded ==");
{
  my(jvals = [Mod(10400 - 4640*t, t^2-5), Mod(10400 + 4640*t, t^2-5),
              Mod(10400 - 4639*t, t^2-5)]);
  my(names = ["j_+ (Z_+ branch)", "j_- (Z_- branch)", "PERTURBED control"]);
  for(iv = 1, 3,
    my(j = jvals[iv], E, ok = 0, bad = 0, amb = 0, tot = 0, badp = List());
    E = ellinit(ellfromj(j), K);
    my(gr = ellglobalred(E), Nc = gr[1], badnorm = idealnorm(K, Nc));
    forprime(p = 3, 1000,
      if(p == 2 || p == 5 || badnorm % p == 0, next);
      my(oQ = quintord2(F5q, p));
      my(dec = idealprimedec(K, p), pr = dec[1], f = pr.f);
      my(ap = ellap(E, pr));
      my(oE = projord(lift(Mod(ap,5)), lift(Mod(p,5)^f)));
      my(oQeff = if(f == 1, oQ, if(oQ == 2, 1, oQ)));
      tot++;
      if(oE == oQeff, ok++,
        if(oE == 5 && oQeff == 1 && (ap^2 - 4*p^f) % 5 == 0, amb++,
           bad++; if(#badp < 8, listput(badp, [p, f, oE, oQeff]))));
    );
    print("  ", names[iv], ": matched ", ok, "/", tot,
          " | scalar-vs-unipotent ambiguous (consistent) ", amb, " | CLEAN MISMATCHES ", bad);
    if(bad > 0, print("    mismatches [p,f,ordE,ordQ_eff]: ", Vec(badp)));
  );
}

print("");
print("== (C2) Twist-minimal conductor probe (wider) ==");
{
  my(eps = Mod((1+t)/2, t^2-5));  \\ fundamental unit phi
  my(base = [1, -1, 2, -2, 3, -3, 5, -5, 6, -6, 10, -10, 15, -15, 30, -30,
             89, -89, 267, -267, 445, -445, 534, -534]);
  my(jv = [Mod(10400 - 4640*t, t^2-5), Mod(10400 + 4640*t, t^2-5)]);
  for(i = 1, 2,
    my(E = ellinit(ellfromj(jv[i]), K));
    my(best = idealnorm(K, ellglobalred(E)[1]), bestd = 1, bestfa = 0);
    for(u = 0, 2,  \\ unit part: 1, eps, eps^2? (eps^2 same square class as 1? eps^2=eps*eps -- eps mod squares: {1,eps} x {+-1})
      for(k = 1, #base,
        my(d = base[k] * if(u == 0, 1, if(u == 1, eps, -eps)));
        my(Et, nt);
        iferr(
          Et = ellinit(elltwist(E, d), K);
          nt = idealnorm(K, ellglobalred(Et)[1]);
          if(nt < best, best = nt; bestd = d),
          err, );
      ));
    my(Ebest = if(bestd == 1, E, ellinit(elltwist(E, bestd), K)));
    my(grb = ellglobalred(Ebest), fac = idealfactor(K, grb[1]));
    print("  branch ", i, ": twist-minimal conductor norm = ", best, " = ", factor(best),
          "  via twist d = ", bestd);
    for(r = 1, #fac[,1],
      my(pr = fac[r,1]);
      print("     prime over p=", pr.p, " (f=", pr.f, ", e=", pr.e, "): exponent ", fac[r,2]));
    \\ also print local data at 2 and 5 for the best model
    print("     [note] j-invariant valuations: v(j) at primes over 2,5 and v(j-1728):");
    my(j = jv[i]);
    forprime(pp = 2, 5,
      my(dc = idealprimedec(K, pp));
      for(m = 1, #dc,
        print("       v_(", pp, ",", m, ")(j) = ", idealval(K, j, dc[m]),
              " ; v(j-1728) = ", idealval(K, j - 1728, dc[m]))));
  );
}
quit;
