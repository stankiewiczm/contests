from Numeric import *
import time;

D = [];         HSH = 11;       t0 = time.time();       ANS = 0L;       MOD = 10**9;

for t in range(20+1):
    D.append([]);
    for l in range(2000):
        D[t].append(0L);
D[0][0] = 1;

for t in range(1,20+1):
    for k in range(0,82*t):
        for d in range(0,10):
            D[t][k+d*d] += D[t-1][k];

######### The frequency of the sum of 11 first digits is preserved.            

SumL2 = [];
for l in range(20-HSH):
    SumL2.append(zeros(1000));
for d in range(10):
    SumL2[0][d*d] = d;

for l in range(1,20-HSH):
    for d in range(0,10):             # Add d * 10^l
        for i in range(82*l):
            SumL2[l][i+d*d] = (SumL2[l][i+d*d]+ SumL2[l-1][i] + d*10**l*D[l][i])%MOD;

######## SUM of last digits 9 is now hashed 


for i in range(1,1000):
    k = 40;        Bit = 0L;
    while (k*k >= i):
        Bit += D[HSH][k*k-i];
        k -= 1;
    ANS += Bit*SumL2[19-HSH][i];

######## Answers are 

print HSH, ANS%MOD, time.time()-t0;

