from numpy import *

LIM = 10**5;        P = [];
ARR = ones(LIM);        ARR[0] = 0;     ARR[1] = 0;

for k in range(LIM):
    if ARR[k] == 1:
        P.append(k);
        l = k*k;
        while (l < LIM):
            ARR[l] = 0;
            l += k;

print len(P);

def Check(n):
    for p in P:
        if n%p == 0:
            return 0;
    return 1;


N = 10**8+7;        Sum = 0;
while (N < 10**8+10**8):
    Sum += Check(N);
    N += 18;



                   
