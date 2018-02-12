from numpy import *

LIM = 10**6;    P = [];     IsP = ones(LIM+1, int);        IsP[1] = 0;
for n in range(2,LIM):
    if IsP[n] == 1:
        P.append(n);
        for i in range(n, LIM/n+1):
            IsP[n*i] = 0;

print "Generated",len(P),"primes";


NFact = zeros(LIM);
for p in P:
    for k in range(1, LIM/p):
        NFact[k*p] += 1;
print "Populated"

for i in range(2*LIM):
    if NFact[i] == NFact[i+1] == NFact[i+2] == NFact[i+3] == 4:
        print i, i+1, i+2, i+3;
        break;
