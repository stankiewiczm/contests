from Numeric import *

MAX = 330000;    Fs = list();    Fs.append(long(1));     Fs.append(long(1));

phi = (1. + sqrt(5))/2;     P0  = log10(1./sqrt(5));    Pp  = log10(phi);


def Check(Pan):
    Arr = zeros(10);
    for a in str(Pan):
        Arr[int(a)] = 1;
    if (sum(Arr) == 9) and (Arr[0] == 0):
        return 1;
    return 0;


P0 = P0+2*Pp;
for i in arange(2,MAX):
    Fs.append((Fs[i-1]+Fs[i-2])%1000000000);
    P0 = P0+Pp;
    if (P0 > 9):
        P0 = P0-1;
    TS = int(floor(10**P0))
    if (Check(Fs[i]) == 1):
        if (Check(TS) == 1):
            print i+1, Fs[i],TS;
        else:
            print i+1;


print "All done"
