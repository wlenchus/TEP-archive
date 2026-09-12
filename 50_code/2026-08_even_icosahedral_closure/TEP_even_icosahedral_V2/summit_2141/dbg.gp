P = x^5 - x^4 - 780*x^3 - 1795*x^2 + 3106*x + 344;
tally(pmax) = {
  my(cnt = Map());
  forprime(p = 3, pmax,
    if(p == 1951 || p == 7 || p == 71 || p == 137, next);
    my(F = factormod(P, p));
    my(degs = vecsort([poldegree(F[i,1]) | i <- [1..matsize(F)[1]]]));
    my(m = if(degs == [1,1,1,1,1], 1, degs == [1,2,2], 2, degs == [1,1,3], 3, degs == [5], 5, 0));
    my(g = ffgen([p, m], 'w));
    my(rr = polrootsmod(P*g^0, g));
    my(key = Str(m, ":", #rr));
    mapput(cnt, key, if(mapisdefined(cnt, key), mapget(cnt, key), 0) + 1));
  Mat(cnt);
}
print(tally(2000));
quit
