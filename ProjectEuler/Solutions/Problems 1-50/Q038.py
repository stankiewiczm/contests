from numpy import *

def Check(k, n):
    Dig = zeros(10, int);
    for i in range(1,n+1):
        l = k*i;
        while l > 0:
            Dig[l%10] += 1;
            l /= 10;
    if max(Dig) == 1 and Dig[0] == 0:
        print k, n;

for k in range(9000,10000):
    Check(k, 2);
