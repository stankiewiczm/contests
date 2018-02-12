from numpy import *

F = [1,1];          Phi = (sqrt(5)+1)/2;
while (len(F) < 5000):
    F.append(F[-1]+F[-2]);

def Eval(x):
#    if (x*Phi > 1):
#        return 0;
    E = 0.;     X = 1;
    for k in range(1400):
        X *= x;
        E += X*F[k];
    return E;


def BinSearch(N, low):
    L1 = low;       L2 = 0.618033988#1./Phi-1e-11;
    while (L2-L1 > 1e-11):
        if (Eval((L1+L2)/2) > N):
            L2 = (L1+L2)/2;
        else:
            L1 = (L1+L2)/2;
        
    return (L1+L2)/2;            


def AlmostRat(Bn):
    for q in range(1,10000):
        AR = q*Bn;
        if abs(round(AR)-AR) < 1e-9:
            print Bn, "   ", (int(q*Bn), q);
            return;
    return;


Bn = 0.4;
for n in range(2,1000):
    Bn = BinSearch(n, Bn);
    print n
    AlmostRat(Bn);
