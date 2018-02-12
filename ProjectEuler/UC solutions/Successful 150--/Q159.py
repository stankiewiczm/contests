from Numeric import *

MAX = 1000001;   Prime = list();    Prime.append(2);    IsP = ones(MAX);     IsP[1] = 0;
LIM = 1000000;   DS = zeros(LIM);        Gen();     BEST = zeros(LIM);

def Gen():
    for i in arange(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    NIsP = 1;
    while (n < MAX):
        if (IsP[n] == 1) and (n < int(sqrt(MAX))+1):
            Prime.append(n);
            NIsP += 1;
            for i in arange(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n = n+2;
    print "Generated all the primes needed",len(Prime)


def Recurse(N0):
    if IsP[N0]:                         # Prime
        return DS[N0];
    for p in Prime:                     # Product of two primes
        if (N0%p == 0):
            if (IsP[N0/p]):
                return max(DS[N0], DS[p]+DS[N0/p]);

    B0 = DS[N0];
    for q in arange(2,int(sqrt(N0))+2):
        if N0%q == 0:
            if (B0 < BEST[q]+BEST[N0/q]):
                B0 = BEST[q]+BEST[N0/q];
    return B0;


######################################################

for n in arange(0,LIM/10):
    for m in arange(10):
        DS[10*n+m] = DS[n]+m;
        while (DS[10*n+m] >= 10):
            DS[10*n+m] = DS[DS[10*n+m]]

for n in arange(2,10):
    BEST[n] = n;

for n in arange(10,LIM):
    BEST[n] = Recurse(n);
print len(BEST), sum(BEST)
