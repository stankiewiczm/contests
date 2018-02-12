from Numeric import *

N = 10**25;
DIG = [];
while N != 0:
    if N%2 == 0:
        DIG.append(0);
    else:
        DIG.append(1);
    N = N/2;
