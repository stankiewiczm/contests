from Numeric import *

def IsTri(T):
    Ntr = sqrt(2.*T+0.25)-0.5;
    if (abs(Ntr-round(Ntr)) < 1e-6):
        return int(Ntr);
    else:
        return 0;


def IsPen(P):
    Npe = sqrt(2.*P/3. + 1./36)+1./6;
    if (abs(Npe-round(Npe)) < 1e-6):
        return int(Npe);
    else:
        return 0;


for i in arange(100000):
    Hex = 2*i**2 - i;
    if (IsPen(Hex) and IsTri(Hex)):
        print Hex, "Tri,Pen,Hex #'s:", IsTri(Hex), IsPen(Hex), i;

