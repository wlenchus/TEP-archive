hilb_inf(a,b) = if(a<0 && b<0, -1, 1);
analyze(f, name) = {
  my(nf, B, G, D, dg, a, sg, disc, plist, eps);
  nf = nfinit(f); B = nf.zk;
  G = matrix(5,5,i,j, nfelttrace(nf, B[i]*B[j]));
  D = qfgaussred(G);
  a = vector(5,i, D[i,i]);
  \\ clear squares: use core of numerator*denominator
  a = vector(5,i, core(numerator(a[i])*denominator(a[i])));
  print(name, " diag (square-free parts): ", a);
  sg = [sum(i=1,5, a[i]>0), sum(i=1,5, a[i]<0)];
  print(name, " signature: ", sg);
  disc = core(prod(i=1,5,a[i]));
  print(name, " disc class (ss-free): ", disc);
  plist = Set(concat([2,5], concat(vector(5,i, factor(abs(a[i]))[,1]~))));
  for(k=1, #plist, my(p=plist[k], e=1);
    for(i=1,4, for(j=i+1,5, e *= hilbert(a[i],a[j],p)));
    print(name, " Hasse eps_", p, " = ", e));
  my(einf=1); for(i=1,4, for(j=i+1,5, einf *= hilb_inf(a[i],a[j])));
  print(name, " Hasse eps_inf = ", einf);
  \\ product over ALL places incl. large primes dividing entries
  my(prodall=einf); for(k=1,#plist, my(p=plist[k], e=1);
    for(i=1,4, for(j=i+1,5, e *= hilbert(a[i],a[j],p))); prodall *= e);
  print(name, " product formula (should be +1): ", prodall);
}
analyze(x^5+20*x+16, "E1");
print("---");
analyze(x^5+10*x^3-10*x^2+35*x-18, "E2(Buhler)");
print("---");
\\ comparison class: the (-1,-1) Hamilton quaternion class invariants
print("(-1,-1) class: eps_2 = ", hilbert(-1,-1,2), ", eps_5 = ", hilbert(-1,-1,5), ", eps_inf = ", hilb_inf(-1,-1));
