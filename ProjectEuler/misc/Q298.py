from numpy import *
from RandomArray import *

def Run(lim):
    Data = map(int, random(lim)*10 + 1)
#    Data = [1,2,4,6,1,8,10,2,4,1]
    Lm = [0]*5;
    Rm = [0]*5;
    Ls = 0;    Rs = 0;
    for e in Data:
        if e in Lm:
            Ls += 1;
            Lm.remove(e);
        else:
            Lm.pop(0);
        Lm.append(e);

        if e in Rm:
            Rs += 1;
        else:
            Rm.pop(0);
            Rm.append(e);
    return [Ls, Rs]
#        print (Ls, Rs), Lm, Rm;


Ans = 0.;
for n in range(1000000):
    [L,R] = Run(50);
    Ans += abs(L-R);
#    Ltot += L;
#    Rtot += R;
    if (n+1)%10000 == 0:
        print n+1, Ans/(n+1)

