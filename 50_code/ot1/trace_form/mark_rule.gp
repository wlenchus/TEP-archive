tab(f, mark) = {my(nf=nfinit(f), d=abs(nf.disc), ps=factor(d)[,1]~); for(k=1,#ps, my(p=ps[k], v=valuation(d,p), dec=idealprimedec(nf,p), ef=vector(#dec,i,[dec[i].e,dec[i].f]), wild=0); for(i=1,#dec, if(dec[i].e % p == 0, wild=1)); print(f, " | p=", p, " v_p(d)=", v, " ef=", ef, " wild=", wild, " p%4=", p%4, " p%8=", p%8, " MARKED=", if(p==mark,"YES","no")));}
tab(x^5+20*x+16, 2);
tab(x^5+10*x^3-10*x^2+35*x-18, 2);
tab(x^5-8*x^3+11*x^2+6*x+4, 53);
tab(x^5-6*x^3+11*x^2-8*x+3, 5);
tab(x^5-6*x^3+11*x^2-6*x+3, 3);
tab(x^5-6*x^3+12*x^2-10*x+4, 2);
tab(x^5-5*x^3-x^2+9*x+7, 73);
tab(x^5-4*x^3+x^2-2*x+9, 17);
tab(x^5-3*x^3-4*x^2+6*x+3, 3);
tab(x^5-10*x^3-5*x^2+10*x+3, 0);
tab(x^5-10*x^3+5*x^2+10*x-3, 0);
