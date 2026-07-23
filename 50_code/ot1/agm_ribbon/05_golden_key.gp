\\ AGM ribbon - the "golden cascade-Frobenius sequence" (the comparison target of
\\ Link 5), computed from the Galois side alone (cascade-Frobenius = factor mod p,
\\ per 06-29 Thread C/D).  2.A5 trace dictionary: order 1 -> |a|=2; order 2 -> 0;
\\ order 3 -> 1; order 5 -> {phi, 1/phi} (golden magnitudes; the phi-vs-1/phi split
\\ is the 5A/5B face-sign, NOT readable from the cycle type = the recorded bulk mode).
F = x^5 + 20*x + 16;
print("p | factorization degrees mod p | Frobenius order | predicted |a_p| class");
{
forprime(p = 3, 100,
  if(p == 2 || p == 5, next);
  my(fa = factormod(F, p), degs = vector(#fa[,1], i, poldegree(fa[i,1])));
  my(o = lcm(degs));
  my(pred = if(o == 1, "2", if(o == 2, "0", if(o == 3, "1", "golden {phi or 1/phi}"))));
  print(p, " | ", degs, " | ", o, " | ", pred);
);
}
print("");
print("LMFDB/07-22 ground truth magnitudes (4000.1.b.a, nu=i*phi embedding):");
print("  |a_3|=1/phi |a_7|=1 |a_11|=1 |a_13|=1/phi |a_17|=1 |a_19|=1/phi |a_23|=0 |a_29|=1 |a_31|=phi");
quit;
