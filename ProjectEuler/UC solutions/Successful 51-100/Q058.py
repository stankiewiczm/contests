from Numeric import *;

MAX = 30001;     NP = 0;             Prime = list();     
Prime.append(2);    IsP = ones(MAX);    IsP[1] = 0;      

def Gen():
    for i in arange(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    NIsP = 1;
    while (n < MAX):
        if (IsP[n] == 1):
            Prime.append(n);
            NIsP += 1;
            for i in arange(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n = n+2;
    return NIsP;


#############################################3
#############################################3

NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];


def PCheck(n):
    for i in arange(NP):
        if n%Prime[i] == 0:
            if (n == Prime[i]):
                return 1;
            return 0;
    return 1;


#N = 7;      D = 13;     Ps = 8;
N = 3;      D = 5;     Ps = 3;

while (D / Ps < 10):
    N = N+2;
    D = D+4;
    for i in arange(1,4):
        Ps += PCheck(N*N-i*(N-1));

print N,D,Ps;
