from numpy import *

DP = [];
DP.append(zeros(250,long));
DP.append(zeros(250,long));
DP[0][0] = 1;
LIM = 250250;      MOD = 10**16;

for n in range(1, LIM+1,2):
    if ((n+1)%1000 == 0):
        print n+1;


    res = pow(n,n,250);
    for k in range(250):
        DP[1][k] = (DP[0][k] + DP[0][ (k-res)%250 ]);

    n += 1;
    res = pow(n,n,250);
    for k in range(250):
        DP[0][k] = (DP[1][k] + DP[1][ (k-res)%250 ])%MOD;

print DP[0][0]-1;
