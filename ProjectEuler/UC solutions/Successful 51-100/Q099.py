from Numeric import *

A=[map(str ,line.split())for line in file("../TXTdata/base_exp.txt")]

V = zeros(1000,Float);      

for i in arange(1000):
    BS = 0;  EX = 0;    Tmp = 0;
    for a in A[i][0]:
        if (a == ','):
            if (BS == 0):
                BS = Tmp;
                Tmp = 0;
            else:
                EX = Tmp;
        else:
            Tmp = 10*Tmp + int(a);
    EX = Tmp;
    V[i] = EX*log10(BS);

Mx = 0;     Mxi = 0;
for i in arange(1000):
    if V[i] > Mx:
        Mx = V[i];
        Mxi = i;
print Mxi+1;
    
