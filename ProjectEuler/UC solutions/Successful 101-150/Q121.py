from Numeric import *

ARR = list();
for i in arange(16):
    ARR.append(zeros(16,Float));

ARR[0][0] = 1.;


for Turn in arange(1,16):
    for Win in arange(16):
        ARR[Turn][Win] = ARR[Turn-1][Win-1]/(Turn+1) + ARR[Turn-1][Win]*(1.-1./(Turn+1));

    print Turn, sum(ARR[Turn]);
        

PROB = 0.;
for i in arange(8,16):
    PROB += ARR[15][i];
print 1./PROB;
