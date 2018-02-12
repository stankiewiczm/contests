from Numeric import *

def Eval(r):
#    mid = (low+high)/2.;
#
    S = 0.;
    for k in range(1,5001):
        S += (900-3.*k)*r**(k-1);

    return S;

def Midpoint(r1, r2):
    L = 600000000000;
    m = (r1+r2)/2;
    if (r1+L)*(Eval(m)+L) > 0:
        return (m, r2);
    else:
        return (r1, m);


Rl = 1.002;     Rh = 1.004;
while (Rh-Rl > 1e-14):
    (Rl, Rh) = Midpoint(Rl, Rh);
    print (Rl, Rh), Eval((Rl+Rh)/2);
