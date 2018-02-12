from Numeric import *

# MUST BE ALL DIFFERENT;

def Choose(n,k):
    R = long(1);
    for i in arange(k):
        R = (R*(n-i))/(i+1);
    return R


TOT = [];
for q in arange(26):    TOT.append(long(0));

for N in arange(1,26):
    for i in arange(1,N):
        for j in arange(0,i):
            TOT[N] += Choose(26,N) * Choose(i,j);
    print N, TOT[N]

