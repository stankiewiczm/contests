from Numeric import *

MAX = 1000001;    Prime = list();    Prime.append(2);    NP = 0;  
IsP = ones(MAX);        IsP[1] = 0;      
GOOD = list();      MILL = 1000000;     LIMIT = 1;

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



k = 1;
while (3*k*k+3*k+1 < MILL):
    Alph = k*k;
    N = k*k*k;
    if (IsP[3*k*k+3*k+1]):
        GOOD.append(3*k*k+3*k+1)
        print len(GOOD),k,N,Alph, 3*k*k+3*k+1
    k += 1;


print len(GOOD);
if GOOD[len(GOOD)-1] > MILL:
    print GOOD;
