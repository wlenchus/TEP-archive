\\ deeper planted tables + kronecker twist tables + summit quintic-character logs
TW = [5, 8, 12, 13, -3, -4, -7, -8];
emitD2(D, XX) = {
  my(Q = Qfb(1,1,(1-D)/4), fn = Str("classes_planted_", D, ".txt"), kf = Str("kron_", D, ".txt"), n=0);
  system(Str("rm -f ", fn, " ", kf));
  forprime(p = 2, XX,
    my(k = kronecker(D,p), c);
    if(k == 0, c = "R", k == 1, c = if(qfbsolve(Q,p) != 0, "P", "N"), c = "I");
    write(fn, Str(p, ":", c));
    write(kf, Str(p, concat(vector(#TW, i, Str(":", kronecker(TW[i], p))))));
    n++);
  print("D=", D, " deepened to ", XX, "  primes=", n);
}
{
emitD2(2089, 7200);
emitD2(40093, 30900);
\\ summit: kron table + quintic character discrete-log table mod 1951 (g0 = 3)
my(kf = "kron_1951.txt", cf = "chilog_1951.txt", g0 = Mod(3, 1951));
system(Str("rm -f ", kf, " ", cf));
forprime(p = 2, 7000,
  write(kf, Str(p, concat(vector(#TW, i, Str(":", kronecker(TW[i], p)))))));
forprime(p = 2, 7000,
  if(p != 1951,
    my(j = lift(znlog(Mod(p, 1951), g0)) % 5);
    write(cf, Str(p, ":", j))));
print("summit tables done (kron to 7000; chilog j(p)=ind_3(p) mod 5)");
print("sanity: j(3)=", lift(znlog(Mod(3,1951), g0))%5, "  chi(3)=zeta5^1 expected");
print("znorder(g0)=", znorder(g0));
}
quit
