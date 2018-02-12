from numpy import *

# m^2+n^2, 2mn, m^2-n^2

LIM = 1500000;      Count = zeros(LIM+1, int);

def GCD(a,b):
    while (b > 0):
        c = a-(a/b)*b;
        a = b;
        b = c;
    return a;


m = 1;      M2 = 1;     
while (2*M2 < LIM):
    n = m%2+1;
    while (2*M2+2*m*n < LIM) and (n < m):
        if GCD(m,n) == 1:
            p = 2*M2+2*m*n;
            for k in range(1, LIM/p+1):
                Count[p*k] += 1;
        n += 2;
    m += 1;            
    M2 = m*m;

print sum(Count==1)
