from Numeric import *

def SortN(N):
    Dl = list();
    for d in str(N):
        Dl.append(int(d));
    D = sort(Dl);
    SN = 0;
    for b in arange(len(D)):
        SN = SN*10+D[b];
    return SN;

for i in arange(123456,170000):
    if SortN(i) == SortN(2*i):
        if (SortN(i) == SortN(3*i)) and (SortN(i) == SortN(4*i)) and (SortN(i) == SortN(5*i))and (SortN(i) == SortN(6*i)):
            print i, 2*i,3*i,4*i,5*i,6*i;
