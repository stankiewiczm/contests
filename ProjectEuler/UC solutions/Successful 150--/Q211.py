from Numeric import *
import time

def T(t):
    Tdiff = time.time()-t;
    return int(1000*(Tdiff))/1000.;

t0 = time.time();       LIM = 64000000;     S2 = [0];
for q in arange(LIM/6+2):
    S2.append(1L);      # Odd numbers
    S2.append(5L);      # Even numbers
    S2.append(10L);
    S2.append(5L);
    S2.append(1L);
    S2.append(14L);

print "starting", T(t0);

N = 3;
while N < LIM:
    N += 1;     N2 = N*N;       k = 1;      Ln = LIM/N;
    while (k <= Ln):
        S2[N*k] += N2;
        k += 1;

print "list filled", T(t0);

Q = 1;      TOT = 0;
while Q < LIM:
    if (int(S2[Q]**0.5))**2 == S2[Q]:
        TOT += Q;
    Q += 1;
print "Total:", TOT,'in total time of ',T(t0);
