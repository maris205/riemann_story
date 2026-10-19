"""Independent algebra/arithmetic checks for the seven pedagogical figures."""
from pathlib import Path
import json
import numpy as np
import sympy as s

def mu_trial(n):
    parity=0;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;parity+=1
            if n%p==0:return 0
        while n%p==0:n//=p
        p+=1
    if n>1:parity+=1
    return (-1)**parity
rows=np.loadtxt(Path(__file__).parent/'detector_X6.csv',delimiter=',',skiprows=1,dtype=int)
for m,c in rows:
    assert c==sum(mu_trial(d) for d in range(1,7) if m%d==0)
for n,v in [(1,1),(12,0),(30,-1),(210,1)]:assert mu_trial(n)==v==s.mobius(n)
th=s.symbols('theta',real=True)
assert s.trigsimp(3+4*s.cos(th)+s.cos(2*th)-2*(1+s.cos(th))**2)==0
w=s.symbols('w');assert s.expand((1-w)*sum(w**k for k in range(4))-(1-w**4))==0
# Fourier orthogonality supplies mean squared moduli: 1+a² and 1+a⁸.
a=s.Rational(65,100)
assert 1+a*a==s.Rational(14225,10000)
assert round(float(1+a**8),4)==1.0319
x,b=s.symbols('x b');assert s.discriminant(x*x-2*x+b,x)==4*(1-b)
for bv,roots in [(0,[0,2]),(1,[1,1]),(2,[1+s.I,1-s.I])]:
    assert all(s.expand(r*r-2*r+bv)==0 for r in roots)
u=np.linspace(1,10,1000);assert np.all(1-1/(5*u)<1-1/(6*u))
# The Perron integrand has residue x at s=1 because -zeta'/zeta has residue +1.
report={'detector_coefficients':'24 values independently checked by trial factorization','mobius_tree':'1,12,30,210 exact','trigonometric_identity':'symbolically verified','finite_inverse_identity':'symbolically verified','quadratic_roots':'six roots counting multiplicity checked','boundary_order':'checked on grid; exact difference is -1/(30u)<0 for u>0','contour':'residue and sign inspected analytically; conceptual diagram, not numerical quadrature'}
(Path(__file__).parent/'math_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False))
