from numpy import *

def DS(n0):
    R = 0;
    while (n0 > 0):
        R += n0%10;
        n0/= 10;
    return R;

def LongSqrt(n):
    N2 = n*10**198
    n0 = int(sqrt(n))*10**99;
    n1 = n0+10**99;
    while (n1 - n0) > 1:
        m = (n1+n0)/2;
        if (m**2 < N2):
            n0 = m;
        else:
            n1 = m;
    return n0;


ANS = 0;
for n in range(2,100):
    if int(sqrt(n))**2 != n:
        ANS += DS(LongSqrt(n));
print ANS;
