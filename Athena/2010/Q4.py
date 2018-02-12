from numpy import *

LIM = 6*10**5;        P = [];
ARR = ones(LIM);        ARR[0] = 0;     ARR[1] = 0;

def Check(P):
    if (P < 6):
        return 0;
    k = 1;
    N = 10;
    while (N != 1):
        N = (N*10)%P;
        k += 1;
#    print N, k, P;
    if (k+1 == P):
        return 1;
    return 0;


for k in range(LIM):
    if ARR[k] == 1:
        P.append(k);
        l = k*k;
        while (l < LIM):
            ARR[l] = 0;
            l += k;

print len(P);       Sum = 0;
for p in range(len(P)):
    Sum += Check(P[p]);
    if (p % 1000 == 0):
        print Sum, p, P[p];

print Sum

# 18439
