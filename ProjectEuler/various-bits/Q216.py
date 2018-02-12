from Numeric import *

LIM = 10000;

MAX = 3*LIM/2;    Prime = list();    Prime.append(2);    NP = 0;  
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

##################################################################
def IsPrime(q):
    if q < MAX:
        if IsP[q] == 0:
            return False;
        else:
            return True;
    for p in Prime:
        if (q%p == 0):
            if (q == p):
                return True;
            if p not in BADS:
                print int(sqrt(q/2.+1)),'failed as ',q,' divisible by ',p;
                BADS.append(p);
            return False;
    return True;


N = 0;      a = 1;      BADS = [];
while (a <= LIM):
    t =  2*a*a-1;
    if IsPrime(t):
        N += 1;
#        print a, N;
    a += 1;

print LIM, N
