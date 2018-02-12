from numpy import *

n = 1;      p = 1;      Prod = 1;   Dec = 10;

while (p < 10**6):
    n += 1;
    if (p + len(str(n)) >= Dec):
        Prod *= (n/(10**(p+len(str(n))-Dec)))%10;
        Dec *= 10;
    p += len(str(n));

print Prod;
