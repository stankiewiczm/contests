from numpy import *

LIM = 7654325;    P = [];     IsP = ones(LIM+1, int);        IsP[1] = 0;
for n in range(2,LIM):
    if IsP[n] == 1:
        P.append(n);
        for i in range(n, LIM/n+1):
            IsP[n*i] = 0;

print "Generated",len(P),"primes";


for k in range(len(P)-1, -1, -1):
    DIG = zeros(10, int);
    DIG[0] = 1;     DIG[8] = 1;     DIG[9] = 1;
    for l in range(7):
        DIG[(P[k]/10**l)%10] += 1;
    if max(DIG) == 1:
        print P[k];
        break;
