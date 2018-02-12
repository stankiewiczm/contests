from Numeric import *

DATA = list();      INTS = list();

def MakeData():
    S0 = 290797;    S = S0;
    for i in arange(20000):
        if (i%4 == 0):
            DATA.append(list());
        S = (S*S)%50515093;
        DATA[i/4].append( int(S%500) );


def Compare(L1, L2):
#    print L1, L2,;

    a1 = L1[0];      b1 = L1[1];      c1 = L1[2];       d1 = L1[3];
    a2 = L2[0];      b2 = L2[1];      c2 = L2[2];       d2 = L2[3];

    MX1 = max(a1,c1);       Mn1 = min(a1,c1)#a1+c1-MX1;
    MX2 = max(a2,c2);       Mn2 = min(a2,c2)#a2+c2-MX2;

    D = (d1-b1)*(c2-a2) - (d2-b2)*(c1-a1)
    if D == 0:
        return 0;           # Lines are parallell

    N = (c1-a1)*(c2-a2)*(b2-b1) + a1*(d1-b1)*(c2-a2) - a2*(d2-b2)*(c1-a1);

    X = float(N)/D;

    if (MX1 > X > Mn1):
        if (MX2 > X > Mn2):
 #           if X not in INTS:
#            Y = (X-a1)*(d1-b1)/(c1-a1);
#            INTS.append( 1000*int(100*X)+Y );
            return 1;
    return 0;
    

MakeData();     TOT = 0;
        
for i in arange(5000):
    for j in arange(i):
        BIT  = Compare(DATA[i],DATA[j]);
        TOT += BIT;

print TOT
