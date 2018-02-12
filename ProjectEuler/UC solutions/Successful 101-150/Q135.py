from Numeric import *

MAX = 1000000;     Hits = zeros(MAX+1);

for B in arange(2,MAX+1):
    Dmin = B/4+1;
    Dmax = min(B,(MAX/B+B)/4+1);
    for D in arange(Dmin,Dmax):
        N = 4*B*D - B*B;
        Hits[N] += 1;

print max(Hits)

print sum(Hits == 10)
