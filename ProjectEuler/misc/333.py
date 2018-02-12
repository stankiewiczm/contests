from numpy import *

LIM = 100;
P = [2];    IsP = [0,1]*(LIM/2)+[0];        IsP[1] = 0;     IsP[2] = 1;

def Gen():
    k = 3;
    while (k < LIM):
        if IsP[k]:
            for l in range(2,LIM/k+1):
                IsP[k*l] = 0;
            P.append(k);
        k += 2;
    print len(P),"primes generated"


def CanPart(n):
    return True;

def UnqPart(p):
    if p <= 5:
        return True;

    


Gen();      Ans = 0;
for prime in P:
    if UnqPart(prime):
        Ans += prime;
