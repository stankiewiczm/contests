from numpy import *

def GCD(n,m):       # Requires n >= m
    while (m > 0):
        a = n-(n/m)*m;
        n = m;
        m = a;
    return n;
    
ANS = 0;
for D in range(3,12000+1):
    l = D/3+1;
    h = D/2+1;
    for N in range(l,h):
        if GCD(N,D) == 1:
            ANS += 1;

print ANS;
