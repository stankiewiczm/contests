from numpy import *

def Verify(p):
    p1 = p;         i = 1;
    if p < 10:
        return 0;
    while (p1 > i):
        i = i*10;       
        if (IsP[p1%i] == 0) or (IsP[p1/i] == 0):
            return 0;
    return p;
        
    

LIM = 10**6;    P = [];     IsP = ones(LIM+1, int);        IsP[1] = 0;
for n in range(2,LIM):
    if IsP[n] == 1:
        P.append(n);
        for i in range(n, LIM/n+1):
            IsP[n*i] = 0;

print len(P), P[-1]

            
    
TPrimes = 0;
for p in P:
    TPrimes += Verify(p);
print TPrimes   
