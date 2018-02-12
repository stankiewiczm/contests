from Numeric import *

LIMIT = 100000000;

MAX = int(sqrt(LIMIT))+1;    Prime = list();    Prime.append(2);    NP = 0;  
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

LAST = Prime[NP-1];
Count = NP;
TOT = 0;

def IsPrime(N):
    for p in Prime:
        if N%p == 0:
            return False;
    return True;

for i in arange(NP-1,-1,-1):
    Lim = LIMIT/Prime[i];
    while ((LAST+2)*Prime[i] < LIMIT):
        LAST += 2;
        if IsPrime(LAST):
            Count += 1;

    TOT += Count-i;
    
    if (int(i**0.5)**2 == i):
        print i, Prime[i], Count-i, TOT;
