from numpy import *

DP = [ones(201,int)];        COIN = [1,2,5,10,20,50,100,200];
for k in range(1,8):
    DP.append(zeros(201, int));
    for l in range(201):
        DP[k][l] = DP[k-1][l];      # not adding new coin;
        m = l;
        while (m >= COIN[k]):
            m -= COIN[k];
            DP[k][l] += DP[k-1][m]

print DP[7][200]    
    
