\\ Crespo-genre construction for Doud-1951: rational orthonormalization of the trace form,
\\ U = V.B (V = root Vandermonde, B^t G B = I), gamma = det(I + U); per-prime square test in F_{p^m}.
P = x^5 - x^4 - 780*x^3 - 1795*x^2 + 3106*x + 344;
ps = polsym(P, 8);
G = matrix(5, 5, i, j, ps[i+j-1]);
print("trace-form Gram (power basis), det = ", matdet(G), " = disc? ", matdet(G) == poldisc(P));
orth(GG) = {
  my(n = matsize(GG)[1]);
  if(n == 0, return(matrix(0, 0)));
  if(n == 1,
    my(c = GG[1,1], s);
    if(!issquare(c, &s), error(Str("1-dim residual not a square: w2 obstruction? c=", c)));
    return(Mat(1/s)));
  my(H = matconcat([GG, matrix(n, 1); matrix(1, n), Mat(-1)]));
  my(v = qfsolve(H));
  my(w = v[1..n], t = v[n+1]);
  if(t == 0, error("isotropic t=0"));
  my(v1 = w / t);
  my(K = matker(Mat((GG*v1)~)));
  my(B2 = orth(K~*GG*K));
  matconcat([Mat(v1), K*B2]);
}
B = orth(G);
print("B^t G B = I exactly: ", B~*G*B == matid(5));
den = lcm(apply(denominator, Vec(matconcat(Vec(B)))));
print("lcm of B denominators: ", factor(den));
\\ numeric validation: U orthogonal, gamma != 0
default(realprecision, 120);
rts = polroots(P);
V = matrix(5, 5, i, j, real(rts[i])^(j-1));
U = V*B;
print("||U^t U - I|| ~ ", vecmax(abs(Vec(matconcat(Vec(U~*U - matid(5)))))));
gam0 = matdet(matid(5) + U);
print("gamma (embedding 1-ordering) = ", gam0);
\\ conjugates under a few orderings: symmetric functions should be rational
{
my(pr = [[1,2,3,4,5],[2,1,3,4,5],[1,3,2,4,5],[2,3,4,5,1]]);
for(k = 1, #pr,
  my(Vp = matrix(5,5,i,j, real(rts[pr[k][i]])^(j-1)));
  print("  gamma[", pr[k], "] = ", matdet(matid(5) + Vp*B)));
}
\\ per-prime: m = Frobenius order in A5 from factormod degrees; square test of gamma in F_{p^m}
sgn(p) = {
  my(F = factormod(P, p));
  my(degs = vecsort([poldegree(F[i,1]) | i <- [1..matsize(F)[1]]]));
  my(m = if(degs == [1,1,1,1,1], 1, degs == [1,2,2], 2, degs == [1,1,3], 3, degs == [5], 5, 0));
  if(m == 0 || den % p == 0, return([-99, 0]));
  my(g = ffgen([p, m], 'w));
  my(rr = polrootsmod(P*g^0, g));
  if(#rr != 5, return([-98, 0]));
  my(Vp = matrix(5, 5, i, j, rr[i]^(j-1)));
  my(Up = Vp * (B*Mod(1, p)));
  my(gm = matdet(matid(5)*g^0 + Up));
  if(gm == 0,
    \\ odd root-ordering: one transposition makes it even (det(I+improper-orth) = 0 identically)
    my(t = rr[1]); rr[1] = rr[2]; rr[2] = t;
    Vp = matrix(5, 5, i, j, rr[i]^(j-1));
    Up = Vp * (B*Mod(1, p));
    gm = matdet(matid(5)*g^0 + Up);
    if(gm == 0, return([-97, 0])));
  my(sq = gm^((p^m - 1)/2));
  [m, if(sq == g^0, 1, -1)];
}
{
system("rm -f crespo_signs.txt");
forprime(p = 3, 7000,
  if(p == 1951 || p == 7 || p == 71 || p == 137, next);   \\ ramified + index primes (2 skipped by loop start)
  my(r = sgn(p));
  if(r[1] > 0, write("crespo_signs.txt", Str(p, ":", r[1], ":", r[2]))));
print("sign emission done");
}
quit
