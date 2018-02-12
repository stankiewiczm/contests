from numpy import *

MAX = 10**7;           Prime = list();     Prime.append(2);    
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


def Inv(p):
    r = p%10;
    if (r == 1):
        return (9*p+1)/10;
    if (r == 3):
        return (3*p+1)/10;
    if (r == 7):
        return (7*p+1)/10;
    return (p+1)/10;

Gen();      S = 0L;
print "Primes generated";
for p in Prime:
    S += Inv(p);
print S
