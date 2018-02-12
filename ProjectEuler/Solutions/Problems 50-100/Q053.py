from numpy import *

def C(n,r):
    R = 1;
    for k in range(r):
        R = (R*(n-k))/(k+1);
    return R;

LIM = 10**6;        SUM = 0;
for n in range(1,101):
    for r in range(n):
        if C(n,r) > LIM:
            SUM += 1;
print SUM
