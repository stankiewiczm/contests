from numpy import *

MOD = 10**16;
LIM = 1600000;          P = [2];        P5k = [2];      
IsP = [0,1]*(LIM+1);    IsP[1] = 0;     IsP[2] = 1;
def Gen():
    k = 3;
    while (k < LIM):
        if IsP[k]:
            for l in range(2,LIM/k+1):
                IsP[k*l] = 0;
            P.append(k);
            if (k < 5000):
                P5k.append(k)
        k += 2;
    print "Primes generated"


Gen()
ANS = [0]*LIM;      ANS[0] = 1;     Sum = 0;
for p in P5k:
    print p
    Sum += p;
    for k in range(Sum, p-1, -1):
        ANS[k] = (ANS[k]+ANS[k-p])%MOD;
        
Solve = 0;
for p in P:
    Solve += ANS[p];
print "Answer is",Solve%MOD

# Answer is 9275262564250418
