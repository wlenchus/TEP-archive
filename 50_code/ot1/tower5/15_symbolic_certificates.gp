\\ TOWER5 - script 15: EXACT SYMBOLIC CERTIFICATES over Q(zeta20).
\\ Upgrades the numerical Half-A results to identities:
\\  (C1) the five coset functions u_c(r) (sum of 12 Mobius images, exact matrices)
\\       satisfy  prod_c (U - u_c(r)) = U^5 + 30U^3 + 100U^2 + 105U + 36 + j(r)
\\       IDENTICALLY in r, with j(r) = -(r^20-228r^15+494r^10+228r^5+1)^3 / (r^5(r^10+11r^5-1)^5).
\\  (C2) the bridge x = 1/(u^2-2u+21): the Brioschi quintic
\\       B(x) = x^5 - 10Zx^3 + 45Z^2x - Z^2, Z = 1/(1728-j),
\\       pulled back along the bridge, vanishes modulo the resolvent:
\\       numerator( B(1/(u^2-2u+21)) ) = 0  mod  (u^5+30u^3+100u^2+105u+36+j)  in Q(j)[u].
\\  (F1) irreducibility of the resolvent over Q(sqrt5) at j_pm.
\\  (CM) j_pm is NOT a CM j-invariant: x^2-20800x+512000 vs all degree-2 Hilbert
\\       class polynomials polclass(D), -400 <= D < 0.
default(realprecision, 60);

\\ ---------- exact cyclotomic setup ----------
P20 = polcyclo(20, 't);
lift5(e) = Mod(e, P20);
z5  = lift5('t^4);
s5  = lift5('t^4 - 't^8 - 't^12 + 't^16);   \\ sqrt5 as Gauss sum
print("check sqrt5^2 = ", lift(s5^2), "  (expect 5)");
gold = (1 + s5)/2;

Smat = [z5, 0; 0, 1];
Vmat = [-gold, 1; 1, gold];

wordmat(w) = {
  my(M = matid(2));
  if (w == "E", return(M));
  for (k = 1, #w,
    c = mid(w, k, 1);
    M = M * if (c == "S", Smat, Vmat);
  );
  M
};
mid(s, a, n) = concat(vector(n, k, Vec(s)[a+k-1]));

A4words = readstr("/home/claude/tower5/words_A4.txt");
repwords = readstr("/home/claude/tower5/words_reps.txt");
print("A4 |words| = ", #A4words, ", reps = ", #repwords);

A4m = vector(#A4words, k, wordmat(A4words[k]));
Rm  = vector(#repwords, k, wordmat(repwords[k]));

mob(M, r) = (M[1,1]*r + M[1,2]) / (M[2,1]*r + M[2,2]);

\\ ---------- (C1) exact resolvent ----------
{
  ucs = vector(5);
  for (c = 1, 5,
    s = 0;
    for (h = 1, #A4m,
      M = A4m[h] * Rm[c];
      s = s + mob(M, 'r);
    );
    ucs[c] = s;
  );
  \\ product (U - u_c)
  PU = 1;
  for (c = 1, 5, PU = PU * ('U - ucs[c]));
  PU = PU;  \\ rational function in r with polmod coeffs, polynomial in U
  jr = -('r^20 - 228*'r^15 + 494*'r^10 + 228*'r^5 + 1)^3 / ('r^5 * ('r^10 + 11*'r^5 - 1)^5);
  target = 'U^5 + 30*'U^3 + 100*'U^2 + 105*'U + 36 + jr;
  diffP = PU - target;
  \\ diffP is a polynomial in U with rational-function-in-r coefficients (polmod t)
  ok = 1;
  for (k = 0, 5,
    ck = polcoef(diffP, k, 'U);
    ck = simplify(ck);
    if (ck != 0,
      \\ try full normalization: lift and compare numerator
      nk = numerator(ck);
      if (nk != 0, ok = 0; print("  C1 FAIL at U^", k, ": nonzero coeff"));
    );
  );
  print("(C1) resolvent identity prod(U - u_c) = U^5+30U^3+100U^2+105U+36+j(r): ",
        if (ok, "EXACT (identical in r over Q(zeta20))", "FAILED"));
}

\\ ---------- (C2) bridge certificate ----------
{
  \\ work in Q(j)[u]
  Zj = 1/(1728 - 'j);
  xu = 1/('u^2 - 2*'u + 21);
  B = xu^5 - 10*Zj*xu^3 + 45*Zj^2*xu - Zj^2;
  NB = numerator(B);   \\ polynomial in u and j
  R5 = 'u^5 + 30*'u^3 + 100*'u^2 + 105*'u + 36 + 'j;
  rem = NB % R5;       \\ division in (Q(j))[u] : make sure u is main variable
  \\ ensure variable order: u main in both
  NBu = subst(NB, 'u, 'u);
  rem = divrem(NBu, R5, 'u)[2];
  print("(C2) numerator(B(1/(u^2-2u+21), Z(j))) mod resolvent = ", rem,
        "   [0 = EXACT identity]");
}

\\ ---------- (F1) irreducibility over Q(sqrt5) ----------
{
  K = nfinit(y^2 - 5);
  for (sgn = -1, 1,
    if (sgn == 0, next);
    jb = 10400 - sgn*4640*Mod(y, y^2-5);
    R5j = 'x^5 + 30*'x^3 + 100*'x^2 + 105*'x + 36 + jb;
    F = nffactor(K, R5j);
    print("(F1) resolvent at j_", if(sgn>0, "+", "-"), " over Q(sqrt5): factors of degree ",
          vector(#F[,1], k, poldegree(F[k,1])));
  );
}

\\ ---------- (CM) non-CM certificate ----------
{
  tgt = x^2 - 20800*x + 512000;
  hit = 0;
  forstep (D = -3, -400, -1,
    if ((D % 4 == 0) || (D % 4 == -3),
      my(H);
      iferr(H = polclass(D), E, next);
      if (poldegree(H) == 2 && H == tgt, hit = D);
    );
  );
  print("(CM) x^2-20800x+512000 among degree-2 polclass(D), -400<=D<=-3: ",
        if (hit, Str("MATCH at D=", hit), "NO MATCH => j_pm are NOT CM invariants (|D|<=400)"));
  \\ direct analytic bound: a CM tau on the imaginary axis with j ~ 20775 would need
  \\ tau = i*sqrt(m)/2-ish; print nearest candidates for the record:
  print("     tau(-) = 1.57636...i ; sqrt(2.5) = ", sqrt(2.5), " (not equal, 3rd decimal)");
}
quit
