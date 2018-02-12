from numpy import *
from time import *

Lim = 10000;     Hit = [];      T0 = time();

for q in range(Lim):
    Hit.append([]);

#def E(m,n):
#    return m**2+m*n+n**2

for p in range(1,Lim):
    P2 = p**2;
    Qlim = min(p, Lim-p)+1;
    for q in range(1,Qlim):
        A = P2+(p+q)*q
        if int(A**0.5)**2 == A:
            Hit[p].append(q);
            Hit[q].append(p);

print time()-T0
