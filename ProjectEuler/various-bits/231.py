from visual.graph import *

MAX = 20000000;           Prime = list();     Prime.append(2);    
IsP = ones(MAX);        IsP[1] = 0;         NP = 0;  

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
        
NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];


SUM = 0;        N = 20000000;     C = 15000000;
for p in Prime:
    f = 0;      pk = 1;
    while (pk * p < N):
        pk *= p;
        f += N/pk - C/pk - (N-C)/pk;
    SUM += f*p;        
print SUM;
