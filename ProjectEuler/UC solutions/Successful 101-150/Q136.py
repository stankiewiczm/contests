from Numeric import *

MAX = 50000000;     Hits = zeros(MAX+1);

for y in arange(2,MAX+1):
    Dmin = y/4+1;
    Dmax = min(y,(MAX/y+y)/4+1);
    for D in arange(Dmin,Dmax):
        N = 4*y*D - y*y;
        Hits[N] += 1;

print max(Hits)

print sum(Hits == 1)
