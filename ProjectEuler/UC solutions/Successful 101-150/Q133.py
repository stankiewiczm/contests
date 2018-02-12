from Numeric import *

MAX = 100000;    Prime = list();    Prime.append(2);    NP = 0;  
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

#####################################################

def Check(p):
#    if (p == 3):
#        return False;
    L = [];     Len = 0;    Next = (10)%p;
    while ((Next not in L) and (len(L) <= 20)):
        L.append(Next);
        Len += 1;
        Next = (Next**10)%p;
    if (1 in L) and (p != 3):
        print p, len(L);
        return True;
    return False;


TOT = 0;
for p in Prime:
    if not Check(p):
        TOT += p;
print "Total is ",TOT;
