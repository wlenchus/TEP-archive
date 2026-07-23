\\ TOWER5 - script 11a: exact level-5 algebra in PARI.
\\ (1) Phi_5 = polmodular(5): symmetry check, export coefficients.
\\ (2) Factor Phi_5(X, j_pm) over K = Q(sqrt5)  [j_pm = 10400 -/+ 4640 sqrt5].
\\ (3) R12(X) = Res_Y(Y^2 - 20800 Y + 512000, Phi_5(X,Y)) in Z[X]; factor over Q.
\\ (4) Pentagon (D5-invariant) sextic resolvent of x^5+20x+16 built numerically
\\     from the roots, rounded to Z[X], re-verified; field comparisons via nfisincl:
\\     does the resolvent-sextic field embed in the degree-12 field of the isogenous j's?
\\     does Q(sqrt5)?
\\ Compute-then-grade: values printed before verdict lines.
default(realprecision, 120);

P5 = polmodular(5);
print("Phi_5 degrees: deg_x = ", poldegree(P5, x), ", deg_y = ", poldegree(P5, y));
sym = P5 - subst(subst(subst(P5, x, 'z), y, x), 'z, y);
print("Phi_5(X,Y) - Phi_5(Y,X) = ", sym, "   [0 = symmetric]");

\\ export coefficients for python (list of [i, j, c] with c coeff of x^i y^j)
{
  cf = List();
  for (i = 0, poldegree(P5, x),
    ci = polcoef(P5, i, x);
    for (jd = 0, poldegree(ci, y),
      c = polcoef(ci, jd, y);
      if (c != 0, listput(cf, [i, jd, c]));
    );
  );
  f = fileopen("/home/claude/tower5/phi5_coeffs.txt", "w");
  for (k = 1, #cf, filewrite(f, Str(cf[k][1], " ", cf[k][2], " ", cf[k][3])));
  fileclose(f);
  print("phi5_coeffs.txt written, ", #cf, " monomials");
}

\\ (2) factorization over Q(sqrt5)
K = nfinit(t^2 - 5);
jp = 10400 - 4640*t;   \\ branch (+), j ~ 24.64
jm = 10400 + 4640*t;   \\ branch (-), j ~ 20775.36
Fp = nffactor(K, subst(P5, y, Mod(jp, t^2-5)));
Fm = nffactor(K, subst(P5, y, Mod(jm, t^2-5)));
print("\nfactor of Phi_5(X, j_+) over Q(sqrt5): #factors = ", #Fp[,1]);
for (k = 1, #Fp[,1], print("   degree ", poldegree(Fp[k,1]), " ^", Fp[k,2]));
print("factor of Phi_5(X, j_-) over Q(sqrt5): #factors = ", #Fm[,1]);
for (k = 1, #Fm[,1], print("   degree ", poldegree(Fm[k,1]), " ^", Fm[k,2]));

\\ (3) R12 over Q
R12 = polresultant(y^2 - 20800*y + 512000, P5, y);
R12 = R12 / content(R12);
print("\nR12 = Res_Y(minpoly(j), Phi_5) : degree ", poldegree(R12));
FR = factor(R12);
print("factorization of R12 over Q:");
for (k = 1, #FR[,1], print("   degree ", poldegree(FR[k,1]), " ^", FR[k,2]));
R12a = FR[1,1];
print("leading/first factor written below (for the record):");
print(R12a);

\\ (4) pentagon resolvent sextic of x^5+20x+16
quintic = x^5 + 20*x + 16;
ro = polroots(quintic);
\\ 12 pentagon structures: cyclic orders of (1..5) up to rotation+reflection.
\\ enumerate permutations fixing first element = 1: (1, p2, p3, p4, p5), 4! = 24,
\\ each cycle counted twice (reflection) -> 12 distinct theta values.
{
  perms = List();
  v = [2,3,4,5];
  \\ all permutations of v
  pp = numtoperm(4, 0); \\ dummy
  for (n = 0, 4! - 1,
    pm = numtoperm(4, n);
    listput(perms, concat([1], vector(4, k, v[pm[k]])));
  );
  thetas = List();
  for (k = 1, #perms,
    s = perms[k];
    th = sum(i = 1, 5, ro[s[i]] * ro[s[(i % 5) + 1]]);
    listput(thetas, th);
  );
  \\ dedupe numerically (each theta appears twice: reflection)
  uniq = List();
  for (k = 1, #thetas,
    isnew = 1;
    for (m = 1, #uniq, if (abs(thetas[k] - uniq[m]) < 1e-80, isnew = 0; break));
    if (isnew, listput(uniq, thetas[k]));
  );
  print("\ndistinct pentagon-sum theta values: ", #uniq, " (expect 12)");
  \\ split into two A5-orbits of 6: sextic with rational coefficients.
  \\ brute force: try all C(12,6)/2 splits is 462 -- but the two orbits are
  \\ determined by: product over orbit of (X - theta) has (near-)integer coeffs.
  \\ Efficient: for each subset of size 6 containing uniq[1], test integrality.
  found = 0;
  su = [0,0];
  forsubset([11, 5], ss,
    idx = concat([1], vector(5, k, ss[k] + 1));
    pol = prod(k = 1, 6, ('X - uniq[idx[k]]));
    co = Vec(pol);
    ok = 1;
    for (m = 1, #co, if (abs(co[m] - round(real(co[m]))) > 1e-60 || abs(imag(co[m])) > 1e-60, ok = 0; break));
    if (ok,
      found++;
      su = idx;
      sext = sum(m = 1, #co, round(real(co[m])) * 'X^(#co - m));
      print("integer-coefficient sextic found (orbit ", found, "): ", sext);
    );
  );
}

\\ verify the sextic is irreducible, then field inclusions
sext6 = 0;
{
  \\ recompute the found sextic cleanly: redo the search, keep the first
  perms = List();
  v = [2,3,4,5];
  for (n = 0, 4! - 1,
    pm = numtoperm(4, n);
    listput(perms, concat([1], vector(4, k, v[pm[k]])));
  );
  thetas = List();
  for (k = 1, #perms,
    s = perms[k];
    th = sum(i = 1, 5, ro[s[i]] * ro[s[(i % 5) + 1]]);
    listput(thetas, th);
  );
  uniq = List();
  for (k = 1, #thetas,
    isnew = 1;
    for (m = 1, #uniq, if (abs(thetas[k] - uniq[m]) < 1e-80, isnew = 0; break));
    if (isnew, listput(uniq, thetas[k]));
  );
  forsubset([11, 5], ss,
    idx = concat([1], vector(5, k, ss[k] + 1));
    pol = prod(k = 1, 6, ('X - uniq[idx[k]]));
    co = Vec(pol);
    ok = 1;
    for (m = 1, #co, if (abs(co[m] - round(real(co[m]))) > 1e-60 || abs(imag(co[m])) > 1e-60, ok = 0; break));
    if (ok,
      sext6 = sum(m = 1, #co, round(real(co[m])) * 'X^(#co - m));
      break;
    );
  );
}
print("\npentagon resolvent sextic RS6(X) = ", sext6);
print("RS6 irreducible over Q: ", #factor(sext6)[,1] == 1);
print("galois group of RS6 (polgalois): ", polgalois(subst(sext6, 'X, x)));

\\ inclusions: K12 = Q[X]/(R12a).  Check sqrt5 in K12, RS6-field in K12.
print("\n[grade] R12 irreducible over Q: ", #FR[,1] == 1 && FR[1,2] == 1);
inc5 = nfisincl(x^2 - 5, R12a);
print("[grade] Q(sqrt5) embeds in K12 = Q[X]/R12factor: ", inc5 != 0);
sx = subst(sext6, 'X, x);
inc6 = nfisincl(sx, R12a);
print("[grade] resolvent-sextic field embeds in K12: ", inc6 != 0);
print("        => K12 = RS6-field * Q(sqrt5) iff both yes and 12 = 6*2 (degrees): deg R12a = ", poldegree(R12a));
