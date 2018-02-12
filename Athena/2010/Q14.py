from numpy import *

LIM = 10**6;    P = [];     IsP = ones(LIM+1, int);        IsP[1] = 0;
for n in range(2,LIM):
    if IsP[n] == 1:
        P.append(n);
        for i in range(n, LIM/n+1):
            IsP[n*i] = 0;

print "Generated",len(P),"primes";
SP = [];        BIGS = [];
for k in range(700):
    SP.append(P[P[k]-1]);


def IsOk(n):
    DIG = zeros(10,int);
    while n > 0:
        DIG[n%10] += 1;
        n /= 10;
    return max(DIG) == 1;


for sp in SP:
    print sp,
    k = 9876543210/sp;
    while k > 0:
        if IsOk(sp*k):
            print sp*k;
            BIGS.append(sp*k);
            break;
        k -= 1;

print "\n ", sum(BIGS);
