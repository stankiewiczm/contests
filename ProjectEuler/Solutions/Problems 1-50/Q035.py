from numpy import *

LIM = 10**6;    P = [];     IsP = ones(LIM+1, int);        IsP[1] = 0;
for n in range(2,LIM):
    if IsP[n] == 1:
        P.append(n);
        for i in range(n, LIM/n+1):
            IsP[n*i] = 0;

print "Generated",len(P),"primes";

NCirc = 0;
for p in P:
    Dig = len(str(p));      OK = 0;     p0 = p;
    for k in range(5):
        p0 = (p0/10) + (p0%10)*10**(Dig-1);
        OK += IsP[p0];
    if (OK == 5):
        NCirc += 1;
#        print p

print NCirc

