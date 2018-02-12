from Numeric import *
import time

LIM = 10000;      LIM2 = 20000;     C = zeros(LIM2);        t = time.time();

for a in arange(1,LIM+1):
    for b in arange(1,min(a,LIM2/a)+1):
        for c in arange(1,b+1):
            N = 2*(a*b+b*c+c*a);    DEL = 4*(a+b+c)
            if N < LIM2:
                C[N] += 1;              L = 0;
                while (N + DEL + 8*L < LIM2):
                    N += DEL+8*L;
                    C[N] += 1;
                    L += 1;

for a in arange(len(C)):
    if C[a] == 1000:
        print a, time.time()-t
        
    
