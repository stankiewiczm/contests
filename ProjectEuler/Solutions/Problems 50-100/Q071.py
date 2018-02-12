from numpy import *

def Solve(maxD):
    Best = 0.;      Bn = 0;     Bd = 0;
    for D in range(3,maxD+1):
        N = (3*D)/7;
        if ((N+0.)/D > Best) and (D%7 != 0):
            Best = (N+0.)/D;
            Bn = N;     Bd = D;

    print (Bn,Bd), Best;

Solve(1e6)
