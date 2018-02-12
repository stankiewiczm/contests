from Numeric import *

DBL = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25];

TH = list();        TH.append(0);
for i in arange(1,21):
    TH.append(i);
    TH.append(2*i);
    TH.append(3*i);
TH.append(25);      TH.append(50);

Lth = len(TH)
LIMIT = 99;
TOT = 0;

for i in arange(Lth):
    for j in arange(Lth):
        for k in arange(len(DBL)):
            Out = TH[i]+TH[j]+2*DBL[k];
            if (Out <= LIMIT):
                TOT += 1;
                if (i == j):
                    TOT += 1;

print TOT, TOT/2;                               
                                    
