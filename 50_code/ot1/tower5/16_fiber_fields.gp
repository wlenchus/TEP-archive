\\ TOWER5 - script 16: field structure of the level-5 fiber values over Q(sqrt5).
\\ (a) X0(5) side: factor (T^2+250T+3125)^3 - j_pm T^5 over K=Q(sqrt5)  [t(tau_pm) lives here]
\\ (b) X(5) side: factor the degree-60 icosahedral polynomial
\\     (r^20-228r^15+494r^10+228r^5+1)^3 + j_pm r^5 (r^10+11r^5-1)^5 over K  [r(tau_pm) lives here]
\\ (c) SL2-lift constant observation: -det[[-phi,1],[1,phi]] = phi+2 = (5+sqrt5)/2;
\\     sqrt(phi+2) = 2 sin(2pi/5); the det-1 lift needs i*sqrt(phi+2) in Q(zeta20)\Q(zeta5).
default(realprecision, 60);
K = nfinit(y^2 - 5);
{
for (sgn = -1, 1,
  if (sgn == 0, next);
  jb = 10400 - sgn*4640*Mod(y, y^2 - 5);
  lab = if (sgn > 0, "+", "-");
  S6 = ('x^2 + 250*'x + 3125)^3 - jb*'x^5;
  F6 = nffactor(K, S6);
  print("(a) X0(5) sextic at j_", lab, " over Q(sqrt5): degrees ",
        vector(#F6[,1], k, poldegree(F6[k,1])));
);
}
{
for (sgn = -1, 1,
  if (sgn == 0, next);
  jb = 10400 - sgn*4640*Mod(y, y^2 - 5);
  lab = if (sgn > 0, "+", "-");
  P60 = ('x^20 - 228*'x^15 + 494*'x^10 + 228*'x^5 + 1)^3 + jb*'x^5*('x^10 + 11*'x^5 - 1)^5;
  gettime();
  F60 = nffactor(K, P60);
  print("(b) X(5) degree-60 fiber at j_", lab, " over Q(sqrt5): degrees ",
        vector(#F60[,1], k, poldegree(F60[k,1])), "   [", gettime()/1000., "s]");
);
}
{
  print("(c) phi+2 = (5+sqrt5)/2 ; sqrt(phi+2) = ", sqrt((5+sqrt(5))/2),
        " ; 2 sin(2pi/5) = ", 2*sin(2*Pi/5));
  print("    [the projective icosahedral machine has constants in Q(zeta5);");
  print("     the det-1 (binary 2.A5 = SL(2,5)) lift of V requires i*sqrt(phi+2),");
  print("     which lies in Q(zeta20) = Q(i, zeta5) but NOT in Q(zeta5):");
  print("     the i enters the tower exactly at the projective->binary lift]");
}
quit
