from Numeric import *


def Bn(n):
    Dell = 1;
    N0 = long(sqrt(n)*(10**99));   V0 = n*10**(198);
    while (Dell != 0):
        Dell = (N0**2-V0)/(2*N0);
#        print Dell;
        N0 = N0 - Dell;
    return N0-1;
    


def Sn(W):
    S = 0;
 #   print W,W*W
    while W > 0:
        S += W%10;
        W = W/10;
    return S;


TOT = 0;
for i in arange(2,100):
    if int(sqrt(i))**2 != i:
        TOT += Sn(Bn(i));
        print i, TOT;

