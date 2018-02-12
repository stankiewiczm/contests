from Numeric import *

ALL = list();                   DIG = 12;
NMin = int(10**((DIG-1)/3.));   NMax = int(10**(DIG/3.));


def Sort(N):
    Dl = list();
    for d in str(N):
        Dl.append(int(d));
    D = sort(Dl);
    SN = long(0);
    for b in arange(len(D)):
        SN = SN*10+D[b];
    return SN;


Occ = zeros(10000);
for i in arange(NMin,NMax):
    ALL.append(Sort(i**3));
for a in arange(len(ALL)):
    for b in arange(a):
        if ALL[b] == ALL[a]:
            Occ[b+NMin] = Occ[b+NMin]+1;
            Occ[a+NMin] = Occ[a+NMin]+1;
#            print "Hallelujah",(b+NMin),(a+NMin),(b+NMin)**3,(a+NMin)**3,ALL[a];
for C in arange(len(Occ)):
    if (Occ[C] >= 4):
        print Occ[C],C,C**3, Sort(C**3);

