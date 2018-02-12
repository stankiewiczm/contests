from numpy import *

for k in range(999,1,-2):
    if k%10 in [1,3,7,9]:
        n = 10;      d = 1;
        while (n != 1):
            n = (n*10)%k;
            d += 1;
        if k-d == 1:
            break;
print k, d;
        
