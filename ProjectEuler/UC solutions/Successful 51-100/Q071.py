from Numeric import *

MAX = 1000000;      DENs = zeros(MAX);
BEST = 0.;          BestD = 0;      BestN = 0;

for i in arange(1,MAX):
    if (i%7 != 0):
        j = (3*i)/7;
    if float(j)/i > BEST:
        BEST = float(j)/i;
        BestD = i;
        BestN = j;

print BestN,"/",BestD,"=",BEST
        
    
