from numpy import *

MAX = 100;    Prime = [2];     NP = 0;  
IsP = ones(MAX);                IsP[1] = 0;

def Gen():
    for i in range(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    while (n < MAX):
        if (IsP[n] == 1):
            Prime.append(n);
            for i in arange(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n += 2;
    return len(Prime);

NP = Gen();

ANS = [zeros(101, int)];        ANS[0][0] = 1;
for n in range(1,25):
    ANS.append(zeros(101,int));
    for k in range(101):
        ANS[n][k] = ANS[n-1][k];
        prv = Prime[n-1];
        while (k >= prv):
            ANS[n][k] += ANS[n-1][k-prv];
            prv += Prime[n-1];

for k in range(len(ANS[-1])):
    if ANS[-1][k] > 5000:
        print k, ANS[-1][k];
        break;
