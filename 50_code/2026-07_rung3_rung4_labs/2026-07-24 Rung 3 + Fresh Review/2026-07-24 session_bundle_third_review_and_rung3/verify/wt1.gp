default(parisize, 2000000000);
t0 = getabstime();
d4 = mfdim([4000,1,-4], 0);
print("dim S_1^new(4000, chi_-4) = ", d4, "   [", (getabstime()-t0)/1000., " s]");
t0 = getabstime();
d20 = mfdim([4000,1,-20], 0);
print("dim S_1^new(4000, chi_-20) = ", d20, "   [", (getabstime()-t0)/1000., " s]");
