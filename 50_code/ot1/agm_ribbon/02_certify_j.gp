\\ AGM ribbon - LINK 1->2 certification (formula-independent, per the corpus's
\\ "certificate sovereignty" discipline in the 07-01 transcript):
\\ (A) certify the Brioschi normalization Z_B = 1/(1728-j) on a random rational Z_B
\\     (positive control) and a wrong normalization (negative control), via:
\\     factorization type of B_Z mod p  ==  projective order of Frob_p on E_j[5].
\\ (B) certify the two computed j_± = 10400 -/+ 4640*sqrt(5) over K = Q(sqrt5)
\\     against the quintic x^5+20x+16's cascade-Frobenius (factor mod p), plus a
\\     perturbed-j negative control.
\\ (C) emit conductor data of E_(j±) over K (compute-then-grade; grading separate).
default(parisize, 256*1024*1024);

\\ projective order of the companion matrix [0,-q;1,a] in PGL_2(F_5); returns n<=6
projord(a, q) = {
  my(M = Mod([0, -q; 1, a], 5), P = M);
  for(n = 1, 6,
    if(P[1,2] == 0 && P[2,1] == 0 && P[1,1] == P[2,2], return(n));
    P = P*M);
  return(0);
};

\\ order of Frobenius class from degree-5 factorization: lcm of factor degrees
quintord(f, p) = {
  my(fa = factormod(f, p, 1)[,1]);  \\ degrees only? factormod(...,1) gives matrix [deg? ]
  \\ factormod(f,p,1) returns factorization with only degrees in col 1? Use full:
  0;
};
quintord2(f, p) = {
  my(fa = factormod(f, p), degs = vector(#fa[,1], i, poldegree(fa[i,1])));
  lcm(degs);
};

\\ ---------- (A) normalization controls over Q ----------
print("== (A) Normalization control over Q: Z0 = 1/100, j0 = 1728 - 1/Z0 = 1628 ==");
{
  my(Z0 = 1/100, j0 = 1728 - 1/Z0,
     B = x^5 - 10*Z0*x^3 + 45*Z0^2*x - Z0^2,
     Bn , E, ok = 0, bad = 0, amb = 0, tot = 0);
  Bn = subst(B, x, x/10)*10^5;  \\ clear denominators: integral model of same field? careful
  \\ safer: scale roots: x -> x/c with c chosen so poly integral: B has denoms 100^2=10^4 etc.
  \\ Use B directly with rational coefficients: factormod needs integral; multiply by 10^4:
  my(Bi = 10^4 * (x^5 - 10*(1/100)*x^3 + 45*(1/100)^2*x - (1/100)^2));
  \\ Bi = 10^4 x^5 - 10^3 x^3 + 45 x - 1  (integral, same splitting field)
  E = ellinit(ellfromj(j0));
  forprime(p = 7, 3000,
    if(p == 2 || p == 5, next);
    if(Mod(poldisc(Bi), p) == 0, next);
    my(ap, gd = 1);
    iferr(ap = ellap(E, p), err, gd = 0);
    if(!gd || Mod(ellminimaldisc(E)*0 + E.disc, p) == 0, next);
    my(oE = projord(ap, p), oQ = quintord2(Bi, p));
    tot++;
    if(oE == oQ, ok++,
       if(oE == 5 && oQ == 1, amb++, bad++; if(bad <= 5, print("  MISMATCH p=",p," E:",oE," B:",oQ))));
  );
  print("  matched ", ok, "/", tot, "  (charpoly {1,5}-ambiguous: ", amb, ", clean mismatches: ", bad, ")");
}
print("== (A') WRONG normalization control: j0' = 1/Z0 + 1728 (deliberately wrong) ==");
{
  my(Z0 = 1/100, j0 = 1/Z0 + 1728, ok = 0, bad = 0, amb = 0, tot = 0);
  my(Bi = 10^4 * (x^5 - 10*(1/100)*x^3 + 45*(1/100)^2*x - (1/100)^2));
  my(E = ellinit(ellfromj(j0)));
  forprime(p = 7, 500,
    if(p == 2 || p == 5, next);
    if(Mod(poldisc(Bi), p) == 0, next);
    my(ap, gd = 1);
    iferr(ap = ellap(E, p), err, gd = 0);
    if(!gd, next);
    my(oE = projord(ap, p), oQ = quintord2(Bi, p));
    tot++;
    if(oE == oQ, ok++, if(oE == 5 && oQ == 1, amb++, bad++));
  );
  print("  matched ", ok, "/", tot, " (ambig ", amb, ", mismatch ", bad, ") -- expect heavy failure");
}

\\ ---------- (B) the two computed j's over K = Q(sqrt5) ----------
print("");
print("== (B) Certify j_+ = 10400 - 4640*sqrt5 and j_- = 10400 + 4640*sqrt5 over K ==");
K = nfinit(t^2 - 5);
F5q = x^5 + 20*x + 16;  \\ the corpus quintic
{
  my(jvals = [Mod(10400 - 4640*t, t^2-5), Mod(10400 + 4640*t, t^2-5),
              Mod(10400 - 4639*t, t^2-5)]);  \\ third = perturbed negative control
  my(names = ["j_plusbranch(Z_+)", "j_minusbranch(Z_-)", "j_PERTURBED_control"]);
  for(iv = 1, 3,
    my(j = jvals[iv], E, ok = 0, bad = 0, amb = 0, tot = 0, badp = List());
    E = ellinit(ellfromj(j), K);
    forprime(p = 3, 700,
      if(p == 2 || p == 5, next);
      my(oQ = quintord2(F5q, p));
      my(dec = idealprimedec(K, p), pr = dec[1], f = pr.f);
      my(ap, gd = 1);
      iferr(ap = ellap(E, pr), err, gd = 0);
      if(!gd, next);
      my(q5 = Mod(p, 5)^f, a5 = Mod(ap, 5) * Mod(1,5));
      my(oE = projord(lift(a5), lift(q5)));
      \\ expected: split (f=1): oE == oQ ; inert (f=2): oE == order of sigma^2
      my(oQeff = if(f == 1, oQ, if(oQ == 2, 1, oQ)));
      tot++;
      if(oE == oQeff, ok++,
        if(oE == 5 && oQeff == 1, amb++,
           bad++; if(#badp < 6, listput(badp, [p, f, oE, oQeff]))));
    );
    print("  ", names[iv], ": matched ", ok, "/", tot,
          " (ambig ", amb, ", clean mismatches ", bad, ")");
    if(bad > 0, print("    first mismatches [p, f, ordE, ordQ_eff]: ", Vec(badp)));
  );
}

\\ ---------- (C) conductor data of E_(j±) over K (COMPUTED; grading deferred) ----------
print("");
print("== (C) Conductor of E_j over K = Q(sqrt5)  [ellfromj model, then minimal twists probe] ==");
{
  my(jv = [Mod(10400 - 4640*t, t^2-5), Mod(10400 + 4640*t, t^2-5)]);
  for(i = 1, 2,
    my(E = ellinit(ellfromj(jv[i]), K), gr = ellglobalred(E));
    my(Ncond = gr[1], nrm = idealnorm(K, Ncond));
    print("  branch ", i, ": conductor ideal norm = ", nrm, " = ", factor(nrm));
    print("     conductor factorization (prime ideals over): ");
    my(fa = idealfactor(K, Ncond));
    for(r = 1, #fa[,1],
      my(pr = fa[r,1]);
      print("       over p=", pr.p, " (f=", pr.f, ", e_ram=", pr.e, "), exponent ", fa[r,2]));
    \\ probe quadratic twists by small S-units to find twist-minimal conductor support
    my(tw = [-1, 2, -2, 5, -5, 10, -10, Mod(t,t^2-5), Mod(-t,t^2-5), Mod(2+t,t^2-5), Mod(2-t,t^2-5)]);
    my(best = nrm, bestd = 1);
    for(k = 1, #tw,
      my(Et, grt, nt);
      iferr(
        Et = ellinit(elltwist(E, tw[k]), K);
        grt = ellglobalred(Et); nt = idealnorm(K, grt[1]);
        if(nt < best, best = nt; bestd = tw[k]),
        err, );
    );
    print("     twist-minimal norm found in probe: ", best, " = ", factor(best), "  (twist by ", bestd, ")");
  );
}
quit;
