from Numeric import *

MAX = 10000;

def MinInt(L1,L2):
    Hyp = L1**2+L2**2;
    RET = 0;

    if (int(sqrt(Hyp))**2-Hyp == 0):
        for c0 in arange(1,L2/2+2):
            if (L2-c0 >= c0) and (L2-c0 <= L1):
                RET += 1;
    return RET;
    

Tot = 0;        a = 0;

while (Tot < 1e6):
    a += 1;
    for b in arange(1,2*a+1):
            Tot += MinInt(a,b);
            if (Tot >= 1e6):
                print a,b;
                break;

    if (a%100 == 0):
        print a,Tot;

print a, Tot;
