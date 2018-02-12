from Numeric import *

LEN = 600;      FINS = zeros(LEN);

SQ = [0,1,4,9,16,25,36,49,64,81];

def SQRd(N):
    Ret = 0;
    for a in str(N):
        Ret += int(a)**2;
#        print Ret,a;
    return Ret;


def Iter(n):
    while (n != 1) and (n != 89):
        n = SQRd(n);
    return n;


for i in arange(1,LEN):
    FINS[i] = Iter(i);


S = zeros(100);
for a in arange(10):
    for b in arange(10):
        for c in arange(10):
            for d in arange(10):
                for e in arange(10):
                    for f in arange(10):
                        for g in arange(10):
                            I = (SQ[a]+SQ[b]+SQ[c]+SQ[d]+SQ[e]+SQ[f]+SQ[g]);
                            S[FINS[I]] += 1                        

#
#for i in arange(1,1000000):
#    S[FINS[SQRd(i)]] += 1
print S;
