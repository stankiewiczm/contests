from numpy import *

LIM = 10**6;        SD = ones(LIM+1, int);      Best = 0;


def Solve(n0):
    n = SD[n0];         L = [n0];
    if SD[n0] <= n0:
        return 0;

    while n not in L:
        L.append(n);
        if (n < n0) or (n > 1e6):
            return;
        n = SD[n];
    if n == n0 and len(L) > 2:
        print len(L), L;
        return len(L);
    return 0;
        

for i in range(2,LIM+1):
    for j in range(2, LIM/i+1):
        SD[i*j] += i;
print "Populated"

for k in range(1,LIM):
    Best = max(Best, Solve(k));
