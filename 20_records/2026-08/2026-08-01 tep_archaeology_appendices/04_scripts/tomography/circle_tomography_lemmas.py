"""Exact lemmas for the modular-circle tomography groundwork. 2026-08-11, session B.
L-A: sum-k chord family envelope = circle of radius cos(pi k/n)  [exact]
L-B: ink density of the sum-k picture at radius r  ~  r/sqrt(r^2-p^2), r>p
     (uniform sampling along chords) — the single-shell backprojection kernel
     [= G(p/r), the corpus gain function — see the G-kernel ADDENDUM]
L-C: multiple-k envelope = epicycloid E(t) = (k e^{it} + e^{ikt})/(k+1):
     tangency check, k-1 cusps (at the map's fixed points), inner reach (k-1)/(k+1)
L-D: the dilation family contains exact diameters (reaches the center) for all k>=2
"""
import numpy as np

# L-A
n, out = 120, []
for k in (15, 20, 25):
    th = 2*np.pi*np.arange(n)/n
    a, b = th, th + 2*np.pi*k/n
    # distance of chord(a,b) from center = |cos((b-a)/2)|
    d = np.abs(np.cos((b-a)/2))
    out.append((k, d.min(), d.max(), np.cos(np.pi*k/n)))
print("L-A shell radii (min=max=cos(pi k/n)):")
for k, dmin, dmax, pred in out:
    print(f"  k={k}: {dmin:.12f} = {dmax:.12f} = {pred:.12f}  OK={abs(dmin-pred)<1e-12 and abs(dmax-pred)<1e-12}")

# L-B: histogram of r for points uniform on chords vs r/sqrt(r^2-p^2)
k, n2 = 20, 240
p = np.cos(np.pi*k/n2)
th = 2*np.pi*np.arange(n2)/n2
S = 4000
ts = np.random.rand(n2, S)
za = np.exp(1j*th)[:, None]; zb = np.exp(1j*(th + 2*np.pi*k/n2))[:, None]
pts = za + (zb - za)*ts
r = np.abs(pts).ravel()
hist, edges = np.histogram(r, bins=40, range=(p+0.002, 0.999))
mid = (edges[:-1] + edges[1:])/2
pred = mid/np.sqrt(mid**2 - p**2)
ratio = hist/pred
ratio /= ratio.mean()
print(f"\nL-B backprojection kernel: histogram/(r/sqrt(r^2-p^2)) flat to "
      f"rel std {ratio.std():.3f} over 40 bins (MC, {n2*S} samples)")

# L-C: epicycloid envelope
for k in (2, 3, 4):
    t = np.linspace(0, 2*np.pi, 200001)
    E = (k*np.exp(1j*t) + np.exp(1j*k*t))/(k+1)
    za, zb = np.exp(1j*t), np.exp(1j*k*t)
    m = np.abs(zb - za) > 1e-6
    u = (zb[m] - za[m])/np.abs(zb[m] - za[m])
    dist = np.abs(np.imag(np.conj(u)*(E[m] - za[m])))
    Ep = np.gradient(E, t)
    speed = np.abs(Ep)
    thr = speed.max()*1e-3
    below = speed < thr
    cusps = int(np.sum(np.diff(below.astype(int)) == 1))
    print(f"L-C k={k}: max tangency defect {dist.max():.2e}; cusps={cusps} (pred {k-1}); "
          f"inner reach min|E|={np.abs(E).min():.6f} (pred {(k-1)/(k+1):.6f})")

# L-D: diameters in the dilation family: chord(theta, k theta) through center
for k in (2, 3, 4):
    # need k*theta = theta + pi (mod 2pi): theta = pi/(k-1) — exact diameter
    th0 = np.pi/(k-1)
    d = abs(np.cos((k*th0 - th0)/2))
    print(f"L-D k={k}: chord at theta=pi/{k-1} has center-distance {d:.2e} (exact diameter)")
