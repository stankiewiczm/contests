from numpy import *

D = zeros(40000,int);       AB = [];        BAD = ones(30000, int);

for k in range(1,30001):
    for l in range(2, 30000/k+1):
        D[k*l] += k;

for k in range(1,28200):
    if D[k] > k:
        AB.append(k);

print len(AB)

for k in range(len(AB)):
    for l in range(k+1):
        if (AB[k]+AB[l] < 30000):
            BAD[AB[k]+AB[l]] = 0;

print sum(BAD);

SUM = 0;
for k in range(len(BAD)):
    if BAD[k] == 1:
        SUM += k;
print SUM;
