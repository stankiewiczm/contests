from Numeric import *

MAX = 175001;    Prime = list();    Prime.append(2);    NP = 0;  
IsP = ones(MAX);        IsP[1] = 0;      

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


K = 10**9;     TOT = 0;        Cnt = 0;     i = 3;
while (Cnt < 40):
    F = (10**10)%Prime[i];
    for j in arange(8):
#        print Prime[i], j, F
        F = (F**10)%Prime[i];

    if (F == 1):
        Cnt += 1;
        TOT += Prime[i];
        print Cnt, [i, Prime[i]], TOT;
    i += 1;

print "Sum of ",Cnt,"prime factors is ",TOT;
