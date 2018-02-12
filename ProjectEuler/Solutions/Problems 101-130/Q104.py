from numpy import *

def PanCheck(n):
    N = [1,0,0,0,0,0,0,0,0,0];
    S = str(n);
    for c in S:
        N[int(c)] += 1;
    return (max(N) == min(N));


def F9Gen(i):
    Lphi = log10((1+sqrt(5))/2);        L5 = log10(5)/2;
    N = i*Lphi-L5;
    N = (N-int(N-8));
    return int(10**N);
    

F1 = 1;     F2 = 1;     n = 2;      MOD = 10**9;    Found = False
while ( n < 1000000 ) and (not Found):
    F1 = (F1+F2)%MOD;       
    F2 = (F2+F1)%MOD;
    n += 2;
    if PanCheck(F1):
        if PanCheck(F9Gen(n-1)):
            print n-1, F1, F9Gen(n-1);
            Found = True;
    if PanCheck(F2):
        if PanCheck(F9Gen(n)):
            print n, F2, F9Gen(n);
            Found = True;
        
