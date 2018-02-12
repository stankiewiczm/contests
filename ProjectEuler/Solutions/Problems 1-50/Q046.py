from numpy import *

LIM = 10**4;    P = [];     IsP = ones(LIM+1, bool);        IsP[1] = 0;
for n in range(2,LIM):
    if IsP[n]:
        P.append(n);
        for i in range(n, LIM/n+1):
            IsP[n*i] = False;

print "Generated",len(P),"primes";


CanDo = zeros(3*LIM, bool);        k = 3;
for p in P:
    for n in range(100):
        CanDo[p+2*n*n] = True;


while True:
    k += 2;
    if not (IsP[k] or CanDo[k]):
        print k;
        break;
        
