from numpy import *

ANS = [zeros(101, int), ones(101, int)];
for n in range(2,101):
    ANS.append(zeros(101,int));
    for k in range(101):
        ANS[n][k] = ANS[n-1][k];
        prv = n;
        while (k >= prv):
            ANS[n][k] += ANS[n-1][k-prv];
            prv += n;
        

print ANS[100][100]-1
