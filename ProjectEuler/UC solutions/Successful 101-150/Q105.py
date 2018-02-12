from Numeric import *

SS = [20,31,38,39,40,42,45];        CURR = sum(SS);


def Check(Seq):
    TST = zeros(14000);
    OTH = zeros(14000);

    for i in arange(2**len(Seq)):
        Bits = zeros(len(Seq));
        I = i;
        for j in arange(len(Seq)):
            Bits[j] = I%2;
            I = I/2;

        S = 0;
        for k in arange(len(Seq)):
            S += Bits[k]*Seq[k];

        TST[S] += 1;
        OTH[S] = sum(Bits);
    
    if (max(TST) >= 2):

        return False;

    Mx = 0;
#    print "trying",Seq;
    for i in arange(len(OTH)):
        if (OTH[i] >= 1) and (OTH[i] < Mx):
            return False;
        if OTH[i] > Mx:
            Mx = OTH[i];
    return True;

    

TOT = 0;        setses = [];        SETS = [];
for line in file("../TXTdata/sets.txt"):
    setses.append(line);

for Nu in arange(len(setses)):
    line = setses[Nu];
    sq = list();    N = 0;
    for ch in line:
        if (ch in ['0','1','2','3','4','5','6','7','8','9']):
            N = 10*N+int(ch);
        if (ch == ','):
            sq.append(N);
            N = 0;
    if (N != 0):
        sq.append(N);

    SETS.append(sq);

    if (Check(sq)):
        TOT += sum(sq);
        print sq;

print TOT;


