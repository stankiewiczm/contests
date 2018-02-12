from Numeric import *

def Pow2(m):
    t = m;
    while (t%2 == 0):
        t = t/2;
    if (t == 1):
        return 1;
    else:
        return 0;

PRF = 0;
TOT = 0;

m = 1;
while (PRF*12345 >= TOT):
    m += 1;
    k = m*(m-1);

    TOT += 1;
    PRF += Pow2(m);

print k, PRF, TOT;
