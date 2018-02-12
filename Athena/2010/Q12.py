from numpy import *

#print 10**250-ceil(sqrt(10**499))

L1 = 3162277660*10**240;        L2 = 3162277662*10**240;

while (L2 - L1 > 1):
    Lmid = (L1+L2)/2;
    if Lmid**2 < 10**499:
        L1 = Lmid;
    else:
        L2 = Lmid;

print 10**250 - L2
