P = x^5 - x^4 - 856*x^3 + 4025*x^2 + 28501*x - 40877;
dP = deriv(P);
sd = sqrtint(poldisc(P));
K = 9;
\\ element arithmetic in (Z/p^K)[y]/(G), G monic irreducible mod p
emul(a, b) = my(c = (a*b) % G); Pol(apply(t -> t % M, Vec(c)), 'y);
epol(a) = Pol(apply(t -> t % M, Vec(a)), 'y);
pev(f, r) = my(v = Vec(f), acc = Pol(v[1] % M, 'y)); for(i = 2, #v, acc = emul(acc, r); acc = epol(acc + (v[i] % M))); acc;
einv(e) = {
  my(ep = subst(Pol(apply(c -> c % p, Vec(e)), 'y), 'y, T));
  my(w = ep^(-1)); my(i0 = w.pol);
  if(type(i0) != "t_POL", i0 = Pol(i0, 'y));
  my(iv = epol(i0));
  for(k = 1, 5, iv = emul(iv, epol(2 - emul(e, iv))));
  iv;
}
hensel(r) = {
  my(rr = epol(r));
  for(k = 1, 7,
    my(fv = pev(P, rr), dv = pev(dP, rr));
    rr = epol(rr - emul(fv, einv(dv))));
  rr;
}
decide(pp) = {
  p = pp; M = p^K;
  my(F = factormod(P, p));
  if(vecsort([poldegree(F[i,1]) | i <- [1..matsize(F)[1]]]) != [5], return(-1));
  G = liftall(ffinit(p, 5, 'y));
  T = ffgen(G*Mod(1,p));
  my(r0 = polrootsmod(P*T^0, T));
  if(#r0 != 5, return(-2));
  \\ Frobenius-ordered ff-orbit, then lift each
  my(orbff = vector(5)); orbff[1] = r0[1];
  for(i = 2, 5, orbff[i] = orbff[i-1]^p);
  my(orb = vector(5));
  for(i = 1, 5,
    my(rp = liftall(orbff[i].pol));
    if(type(rp) != "t_POL", rp = Pol(rp, 'y));
    orb[i] = hensel(rp));
  my(V = Pol(1, 'y));
  for(i = 1, 5, for(j = i+1, 5, V = emul(V, epol(orb[i] - orb[j]))));
  if(poldegree(V) > 0, return(-3));
  my(v0 = polcoef(V, 0) % M, s = sd % M);
  if(v0 == s, return(3), v0 == (M - s) % M, return(4), return(-4));
}
\\ ffgen-Vandermonde reference (for odd-prime validators)
faceref(p) = {
  my(g = ffgen([p, 5], 'w));
  my(rts = polrootsmod(P*g^0, g), r = rts[1]);
  my(orb = vector(5)); orb[1] = r;
  for(i = 2, 5, orb[i] = orb[i-1]^p);
  my(V = g^0);
  for(i = 1, 5, for(j = i+1, 5, V = V*(orb[i] - orb[j])));
  my(c = lift(polcoef(V.pol, 0)));
  if(Mod(c, p) == Mod(sd, p), 3, Mod(c, p) == -Mod(sd, p), 4, -9);
}
{
my(n = 0);
forprime(q = 3, 600,
  if(n >= 4, break);
  my(F = factormod(P, q));
  if(vecsort([poldegree(F[i,1]) | i <- [1..matsize(F)[1]]]) == [5],
    my(a = faceref(q), b = decide(q));
    print("validator p=", q, ": ffgen-face ", a, "  p-adic decider ", b, "  ", if(a == b, "MATCH", "*** MISMATCH ***"));
    n++));
print("p=2 decision (3 = face-a, 4 = face-b): ", decide(2));
}
quit
