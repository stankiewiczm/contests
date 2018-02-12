from numpy import *

def SD(n):
    R = 0;
    while (n > 0):
        R += n%10;
        n /= 10;
    return R;

L = [];
for a in range(2,100):
    for b in range(2,101):
        L.append(SD(a**b));
print max(L);
