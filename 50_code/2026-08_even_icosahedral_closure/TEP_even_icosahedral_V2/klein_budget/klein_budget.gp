\\ (1) Klein's icosahedral syzygy, exact symbolic check: f (deg 12 vertex form),
\\ H = Hessian/121 (deg 20), T = Jacobian(f,H)/20 (deg 30); test sign conventions.
f = x*y*(x^10 + 11*x^5*y^5 - y^10);
fxx = deriv(deriv(f, x), x); fyy = deriv(deriv(f, y), y); fxy = deriv(deriv(f, x), y);
H0 = (fxx*fyy - fxy^2);
fx = deriv(f, x); fy = deriv(f, y);
{
for(sH = -1, 1,
  if(sH == 0, next);
  my(H = sH*H0/121);
  my(Hx = deriv(H, x), Hy = deriv(H, y));
  for(sT = -1, 1,
    if(sT == 0, next);
    my(T = sT*(fx*Hy - fy*Hx)/20);
    if(T^2 + H^3 - 1728*f^5 == 0,
      print("SYZYGY EXACT:  T^2 = 1728 f^5 - H^3   (sH=", sH, ", sT=", sT, ")"));
    if(T^2 - H^3 + 1728*f^5 == 0,
      print("SYZYGY EXACT:  T^2 = H^3 - 1728 f^5   (sH=", sH, ", sT=", sT, ")"))));
}
\\ (2) modular twin, q-series to O(q^12): E4^3 - E6^2 = 1728 Delta
N = 12;
E4 = 1 + 240*sum(n=1, N, sigma(n,3)*q^n) + O(q^(N+1));
E6 = 1 - 504*sum(n=1, N, sigma(n,5)*q^n) + O(q^(N+1));
D  = q*prod(n=1, N, (1-q^n)^24) + O(q^(N+1));
print("modular: E4^3 - E6^2 - 1728*Delta = ", E4^3 - E6^2 - 1728*D);
\\ (3) the budget chart it forces: u = 1728/j on the geodesic z = it (j real >= 1728),
\\ seam x=0 at j = 1728 (z = i, the order-2 CM point / Fricke fixed point); cusp = saturation.
default(realprecision, 30);
{
forstep(t = 1.0, 2.0, 0.25,
  my(j = real(ellj(I*t)), u = 1728/j, x2 = 1 - u);
  if(x2 >= 0,
    my(x = sqrt(x2), G = 1/sqrt(u), A = asin(x), eta = atanh(x));
    print("z=", t, "i:  j=", floor(j), "  x^2=", x2, "  u=", u, "  G=", G, "  G^2-SNR=", G^2 - x2/u)));
}
quit
