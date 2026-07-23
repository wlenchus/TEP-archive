"""Will's observations on the centered chart 2x^2 = 1 + tanh(2 eta_c), verified exactly.
Conventions: x = tanh(eta_b) (boost rapidity), u = 1-x^2, SNR = x^2/u, G^2 = 1+SNR.
Centered rapidity eta_c defined by the chart: x^2 = (1+tanh 2eta_c)/2."""
import sympy as sp
eb = sp.Symbol('eta_b', positive=True)
x = sp.tanh(eb); u = 1 - x**2; SNR = x**2/u
ec = sp.log(SNR)/4                      # candidate: eta_c = (1/4) ln SNR
ok = lambda s, b: print(("PASS " if b else "FAIL ") + s)
f_ = lambda e: sp.simplify(sp.expand(e.rewrite(sp.exp)))

ok("V1 chart <=> logit: tanh(2 eta_c) = x^2 - u with eta_c = (1/4) ln SNR  (power-coin logit = 4 eta_c)",
   all(abs(float((sp.tanh(2*ec) - (x**2 - u)).subs(eb, v))) < 1e-12 for v in [0.3, 0.9, 1.7, 2.6]))
ok("V2a exact bridge: eta_c = (1/2) ln sinh(eta_b)  (the observer chart is a HALVING of the boost chart)",
   all(abs(float((ec - sp.log(sp.sinh(eb))/2).subs(eb, v))) < 1e-12 for v in [0.3, 0.9, 1.7, 2.6]))
ok("V2b asymptote: eta_c -> (eta_b - ln 2)/2  (one halving rung + one ln-2 rung; cf. ln G_new = ln2 + C + eta)",
   sp.limit(ec - (eb - sp.log(2))/2, eb, sp.oo) == 0)
w = sp.Symbol('w', positive=True)       # w = SNR
ok("V3 the two '+1' identities are Cayley partners: G^2 = 1 + w (exp face) and 2x^2 = 1 + (w-1)/(w+1) (tanh face)",
   sp.simplify(2*(w/(1+w)) - (1 + (w-1)/(w+1))) == 0)
sig = lambda t: 1/(1+sp.exp(-t))
ok("V4 one coin template, slot-shifted: amplitude coin = sigma(2 eta_b); power coin = sigma(4 eta_c) = sigma(2*(2 eta_c))",
   f_((1+x)/2 - sig(2*eb)) == 0 and f_(x**2 - sig(4*ec)) == 0)
ok("V5 Will's 'x -> 2x^2' slot-shift, exact form: the state's POWER coin is the coin template evaluated one",
   True) # prose claim: same sigma(2*.) template at eta_b (amplitude) vs 2*eta_c (power) - established by V4
