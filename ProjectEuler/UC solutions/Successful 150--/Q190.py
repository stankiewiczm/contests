from Numeric import *

def WProd(m):
    P = 1.;
    xs = zeros(m+1, Float);     x1 = 2./(m+1);
    for i in arange(1,m+1):
        xs[i] = x1*i;
        P = P*(xs[i])**i;
    return int(P);


SUM = 0;
for q in arange(2,16):
    SUM += WProd(q);
print SUM;
