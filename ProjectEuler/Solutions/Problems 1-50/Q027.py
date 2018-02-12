from numpy import *

Prime = [];     IsP = ones(50001,int);      IsP[1] = 0;
for k in range(1,50000):
    if IsP[k]:
        Prime.append(k);
        for l in range(k, 50000/k+1):
            IsP[k*l] = 0;

print len(Prime), Prime[-1]

MAX = 0;        Best = [0,0];
for b in range(2,1000):
    if IsP[b]:
        for a in range(-999,1000):
            n = 0;
            while IsP[n*n+a*n+b]:
                n += 1;
                if n*n+a*n+b < 0:
                    break;
            if n > MAX:
                Best = [a,b];
                MAX = n;

print MAX, Best
