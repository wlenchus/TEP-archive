\\ step1_shape.gp -- local 2-adic shape of both quintics (COMPUTE phase, no grading)
\\ P1 = ours (field 5.1.1000000.2), P2 = Buhler control
P1 = x^5 + 20*x + 16;
P2 = x^5 + 10*x^3 - 10*x^2 + 35*x - 18;
prec = 100;

\\ resolvent cubic of quartic x^4+a*x^3+b*x^2+c*x+d
rescubic(g) = {
  my(a = polcoef(g,3), b = polcoef(g,2), c = polcoef(g,1), d = polcoef(g,0));
  x^3 - b*x^2 + (a*c - 4*d)*x - (a^2*d - 4*b*d + c^2);
}

process(P, name) = {
  print("========== ", name, " : ", P, " ==========");
  my(D = nfdisc(P));
  print("global quintic field disc = ", D, " = ", factor(D)~);
  print("v2(field disc) = ", valuation(D,2), ",  v5 = ", valuation(D,5));
  my(fp = factorpadic(P, 2, prec));
  print("factorpadic over Q2, degrees of factors: ", apply(poldegree, fp[,1]~));
  my(g4 = 0);
  for (i = 1, #fp[,1], if (poldegree(fp[i,1]) == 4, g4 = liftall(fp[i,1])));
  \\ reduce lifted coefficients mod 2^40 (centered) -- Krasner-equivalent model
  my(gl = Pol(centerlift(Mod(Vec(g4), 2^40)), x));
  print("quartic factor, integer model (coeffs mod 2^40): ", gl);
  \\ number field maximal at 2 only (avoid factoring huge disc)
  my(K = nfinit([gl, [2]]));
  my(pr = idealprimedec(K, 2));
  print("primes above 2 in Q(x)/(g4~): ", #pr);
  for (j = 1, #pr, print("   e = ", pr[j].e, "  f = ", pr[j].f));
  print("v2(disc of quartic 2-adic field K4) = ", valuation(K.disc, 2));
  \\ is disc a square in Q2 (A4/V4 vs others)?
  my(dpol = poldisc(gl));
  print("v2(poldisc of model) = ", valuation(dpol,2),
        " ; poldisc is a square in Q2: ", issquare(dpol + O(2^(2*valuation(dpol,2)+20))));
  \\ resolvent cubic over Q2
  my(rc = rescubic(gl));
  my(fr = factorpadic(rc, 2, prec));
  print("resolvent cubic 2-adic factor degrees: ", apply(poldegree, fr[,1]~));
  if (#fr[,1] == 1 && poldegree(fr[1,1]) == 3,
    my(c3 = liftall(fr[1,1]));
    my(c3l = Pol(centerlift(Mod(Vec(c3), 2^30)), x));
    my(Kc = nfinit([c3l, [2]]));
    my(prc = idealprimedec(Kc, 2));
    print("resolvent cubic field at 2: e = ", prc[1].e, " f = ", prc[1].f,
          "  v2(disc) = ", valuation(Kc.disc,2), "  (f=3,v2=0 <=> unramified cubic)"));
  gl;
}
g1 = process(P1, "P1 ours x^5+20x+16");
g2 = process(P2, "P2 Buhler x^5+10x^3-10x^2+35x-18");

\\ save integer models of quartic factors for later steps
write("/home/claude/p2_break/quartic_models.gp", "g1q = ", g1, "; g2q = ", g2, ";");
print("saved quartic models.");
quit
