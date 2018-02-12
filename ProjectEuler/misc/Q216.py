from numpy import *
import time

LIM = 10**6;    Tlim = 10000;               T0 = time.time();
Prime = [2];    IsP = ones(LIM+1, int);     IsP[0] = IsP[1] = 0;
def Gen():
    for i in range(2,LIM/2+1):
        IsP[2*i] = 0;
    p = 3;
    while (p < LIM):
        if IsP[p]:
            Prime.append(p)
            for q in range(2,LIM/p+1):
                IsP[p*q] = 0;
        p += 2;
    print "Generated",len(Prime),"primes up to",Prime[-1];


def Pfactors(num):
    k = 3;      Ret = [];
    while (num%2 == 0):
        num /= 2;
        
    while (num > 1):
        while (num%k == 0):
            Ret.append(k);
            num /= k;
        k += 2;
        if (k*k > num) and (num != 1):
            Ret.append(num);
            num = 1;
    return Ret;
        


#Gen();      Ans = 0;    sp = ' ';   NAns = 0;
GOOD = ones(Tlim+1, int);             GOOD[0] = GOOD[1] = 0;


for n in range(2,Tlim+1):
    if GOOD[n] == 1:
        Val = 2*n*n-1;
        PrimeL = Pfactors(Val);
        if len(PrimeL) > 1:
            GOOD[n] = 0;

        extra = Tlim+1-n;                       # Way to go...
        for p in PrimeL:
            for i in range(1, extra/p):
                GOOD[n+i*p] = 0;                # If p|2t^2-1, p|2(t+p)^2-1
        
print len(GOOD), sum(GOOD), time.time()-T0
