from Numeric import *

def Check(N):
    while (N > 0):
        k = N%2;
        if (k == 0):
            return 0
            return False;
        N = N/10;
    return 1;
    return True;


def Rev(N):
    SN = str(N);        LSN = len(SN);
    RN = 0;
    for i in arange(LSN):
        RN = 10*RN+int(SN[LSN-1-i]);
    return RN;


TOT = 0;    i = 1;
while (i < 1e7):        # No solutions above 10^8;
    for j in arange(1,10):
        k = 10*i+j;
        TOT += Check(k+Rev(k));

    i += 1;
    if (i%25000 == 0):
        print 10*i, TOT

print TOT;
