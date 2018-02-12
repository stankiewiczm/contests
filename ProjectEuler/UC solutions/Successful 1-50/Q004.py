from Numeric import *

N = 0;      MAX = 0;

for a in arange(999,100,-1):
    for b in arange(999,a,-1):
        PRD = a*b;      MID = (PRD/10)%10000;
        if (a*b > MAX) and (PRD/100000 == PRD%10):
            if  (MID/1000 == MID%10) and (MID%11 == 0):
                MAX = a*b;
                print a,'*', b,'=', MAX
