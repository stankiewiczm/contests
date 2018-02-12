from numpy import *

LIM = 10**4;    P = [];     IsP = ones(LIM+1, int);        IsP[1] = 0;
for n in range(2,LIM):
    if IsP[n] == 1:
        P.append(n);
        for i in range(n, LIM/n+1):
            IsP[n*i] = 0;

print "Generated",len(P),"primes";


def CheckDig(n1, n2, n3):
    Diff12 = zeros(10, int);        Diff13 = zeros(10,int);
    for k in range(4):
        Diff12[ (n1/10**k)%10 ] += 1;
        Diff12[ (n2/10**k)%10 ] -= 1;
        Diff13[ (n1/10**k)%10 ] += 1;
        Diff13[ (n3/10**k)%10 ] -= 1;
    return (max(Diff12)+max(Diff13) == 0)

for k1 in range(len(P)):
   if P[k1] > 1000:
      for k2 in range(k1+1, len(P)):
         if IsP[(P[k1]+P[k2])/2]:
            if CheckDig(P[k1], (P[k1]+P[k2])/2, P[k2]):
               print P[k1], (P[k1]+P[k2])/2, P[k2]
