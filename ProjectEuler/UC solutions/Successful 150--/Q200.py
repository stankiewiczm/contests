from Numeric import *
from time import *

MAX = 400000;    Prime = [2];    NP = 0;     t0 = time();

def Gen():
    IsP = ones(MAX);    IsP[1] = 0;      

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

    print "Generated",NIsP,"primes up to ",Prime[-1],"in a time of ",time()-t0;
    return NIsP;


def GoodSqb(p,q):
    N0 = p*p*q*q*q;
    
    N = N0;     L = [];
    while (N > 0):
        L.append(N%10);     N /= 10;

    for k in range(len(L)-2):
        if (L[k] == 0) and (L[k+1] == 0) and (L[k+2] == 2):
            return True;
        
def PProof(N):
    N0 = (N/10)*10;
    ToCheck = [N0+1, N0+3, N0+7, N0+9];
    for n in ToCheck:
        Comp = False;
        for p in Prime:
            if (n%p == 0) and (n != p):
                Comp = True;
        if not Comp:
            return False;
    return True;


############################################################

Gen();      L200 = [];

for p in Prime:
    if GoodSqb(2,p):
        L200.append(4*p*p*p);
    if GoodSqb(5,p):
        L200.append(25*p*p*p);

    if GoodSqb(p,2):
        L200.append(8*p*p);
    if GoodSqb(p,5):
        L200.append(125*p*p);

L200.pop(0);            # Element 200 appears twice
S200=sort(L200);

T = 0;      k = -1;
while T != 200:
    k += 1;
    if (PProof(S200[k])):
        T += 1;
            
print "Fin", S200[k], time()-t0
