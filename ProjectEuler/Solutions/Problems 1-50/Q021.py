from numpy import *

D = zeros(30000,int);

for k in range(1,10001):
    for l in range(2, 10000/k+1):
        D[k*l] += k;

SUM = 0;
for k in range(1,10000):
    if D[D[k]] == k:
        if D[k] != k:
            SUM += k;

print SUM
