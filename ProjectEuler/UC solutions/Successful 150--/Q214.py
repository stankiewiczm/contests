from visual.graph import *

MAX = 40000001;    Prime = list();    Prime.append(2);    NP = 0;  
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

######################################################################
## Now go through the primes and see if they have totient length 25 ##

def Phi(n):
    N = n;      PHI = n;
    idx = -1;
    while (IsP[N] == False) and (N != 1):
        idx += 1;
#        print N, Prime[idx];
        if N%Prime[idx] == 0:
            PHI = (PHI*(Prime[idx]-1))/Prime[idx];
            while N % Prime[idx] == 0:
                N = N/Prime[idx];
    if (N != 1):
        PHI = (PHI*(N-1))/N;
    return PHI;


def Totient(p):
    Cnt = 1;
#    print p, 
    while (p != 1):
        Cnt += 1;
        p = Phi(p);
#    print Cnt+1;
    return Cnt;


SUM = 0;
for a in Prime:
    if Totient(a) == 25:
#        print a, Totient(a);
        SUM += a;
print SUM
