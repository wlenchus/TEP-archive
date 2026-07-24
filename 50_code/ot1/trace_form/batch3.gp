hilb_inf(a,b) = if(a<0 && b<0, -1, 1);
profile(f) = {my(S, G, D, a, sg, disc, plist, bad=List(), einf=1); S = polsym(f, 8); G = matrix(5,5,i,j, S[i+j-1]); D = qfgaussred(G); a = vector(5,i, core(numerator(D[i,i])*denominator(D[i,i]))); sg = [sum(i=1,5,a[i]>0), sum(i=1,5,a[i]<0)]; disc = core(prod(i=1,5,a[i])); plist = Set(concat([2,3,5,7], concat(vector(5,i, factor(abs(a[i]))[,1]~)))); for(k=1,#plist, my(p=plist[k], e=1); for(i=1,4, for(j=i+1,5, e *= hilbert(a[i],a[j],p))); if(e==-1, listput(bad,p))); for(i=1,4, for(j=i+1,5, einf *= hilb_inf(a[i],a[j]))); [sg, disc, Vec(bad), einf];}
seen = List(); n=0;
for(A=-40,40, for(Bc=1,40, my(f=x^5+A*x+Bc); if(polisirreducible(f) && polsturm(f)==1 && polgalois(f)[1]==60, my(ps=factor(abs(poldisc(f)))[,1]~); if(!setsearch(Set(seen), Str(ps)), listput(seen, Str(ps)); n++; my(pr=profile(f)); write("batch_results.txt", "ODD ", f, " pdsupp=", ps, " -> ", pr)))));
write("batch_results.txt", "odd distinct-support count: ", n);
m=0;
for(P=-12,-4, for(Q=-5,5, for(R=1,12, for(Sc=-5,5, my(f=x^5+P*x^3+Q*x^2+R*x+Sc); if(Sc!=0 && polsturm(f)==5 && polisirreducible(f) && polgalois(f)[1]==60, m++; my(pr=profile(f), ps=factor(abs(poldisc(f)))[,1]~); write("batch_results.txt", "EVEN ", f, " pdsupp=", ps, " -> ", pr); if(m>=3, break(4)))))));
write("batch_results.txt", "even found: ", m);
write("batch_results.txt", "DONE");
