import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(20260807)
CIRC = np.exp(2j*np.pi*np.arange(1024)/1024)
A = np.zeros((3,3), complex); A[0,1]=A[1,2]=1.0; r3 = np.cos(np.pi/4); deg = 8
def Ld(v):
    coef = v[:deg+1] + 1j*v[deg+1:]
    fb = np.polyval(coef, r3*CIRC); sup = np.abs(fb).max()
    if sup < 1e-13: return (0.0, 0.0)
    coef = coef/sup
    fA = np.zeros((3,3), complex)
    for cc in coef: fA = fA @ A + cc*np.eye(3)
    c = np.linalg.norm(fA, 2)
    x = np.linalg.svd(fA)[2].conj().T[:, 0]
    return c, np.real(coef[-1]*np.conj(x.conj() @ fA @ x))
starts = []
for _ in range(18):
    rr = minimize(lambda v: (lambda q: q[1] + 100*max(0, 1.83 - q[0])**2)(Ld(v)),
                  rng.standard_normal(2*(deg+1)), method='Nelder-Mead',
                  options={'maxiter': 2500, 'fatol': 1e-13})
    c, Iv = Ld(rr.x)
    if c >= 1.82 and Iv < -1e-5: starts.append((Iv, c, rr.x.copy()))
starts.sort(); starts = starts[:3]
print(f"crease starts found: {len(starts)}")
for k, (I0, c0, v0) in enumerate(starts):
    traj = []
    minimize(lambda v: -Ld(v)[0], v0, method='Nelder-Mead',
             callback=lambda vk: traj.append(Ld(vk)),
             options={'maxiter': 5000, 'fatol': 1e-14})
    cs = np.array([t[0] for t in traj]); Is = np.array([t[1] for t in traj])
    pos = np.nonzero(Is >= 0)[0]
    if len(pos) and (Is[pos[0]:] >= -1e-9).all():
        print(f"  start {k}: (c={c0:.4f}, I={I0:+.2e}) -> heals at c={cs[pos[0]]:.4f}, stays healed -> ends (c={cs[-1]:.4f}, I={Is[-1]:+.2e})")
    elif len(pos):
        print(f"  start {k}: (c={c0:.4f}, I={I0:+.2e}) -> crosses at c={cs[pos[0]]:.4f} but re-creases -> ends (c={cs[-1]:.4f}, I={Is[-1]:+.2e})")
    else:
        print(f"  start {k}: (c={c0:.4f}, I={I0:+.2e}) -> NEVER heals; ends (c={cs[-1]:.4f}, I={Is[-1]:+.2e})  [CREASE CARRIED]")
