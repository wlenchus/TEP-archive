\\ planted ladder generator — answer-free (qfbsolve ground truth), resumption 2026-08-03
emitD(D) = {
  my(X = ceil(13.0*sqrt(D)), Q = Qfb(1,1,(1-D)/4), fn = Str("classes_planted_", D, ".txt"), n=0);
  forprime(p = 2, X,
    my(k = kronecker(D,p), c);
    if(k == 0, c = "R",
      k == 1, c = if(qfbsolve(Q,p) != 0, "P", "N"),
      c = "I");
    write(fn, Str(p, ":", c)); n++);
  print("D=", D, "  X=", X, "  primes=", n, "  h=", quadclassunit(D).no);
}
{
emitD(2089);
emitD(40093);
emitD(3806549);
\\ alpha-control character tables
my(fn = "alpha_chars.txt");
forprime(p = 2, 120, write(fn, Str(p, ":", kronecker(5,p), ":", kronecker(8,p))));
print("alpha chars done");
}
quit
