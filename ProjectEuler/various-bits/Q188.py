from Numeric import *

LIM = 100000000;       PhiLIM = 1250000;

BASE = 1777;
POWER = 15;

Exps = zeros(25);
Exps[0] = BASE;
for i in arange(1,25):
    Exps[i] = (Exps[i-1]**2)%LIM


def Iter(Base, Pow):
    nexp = Pow%PhiLIM;
    Nexp = Pow%PhiLIM;

    RET = 1;
    POW = 0;
    
    while (nexp > 0):
        if (nexp % 2 == 1):
            RET = RET*Exps[POW];
        POW += 1;
        nexp = nexp/2;
    
    return RET%LIM


Curr = BASE;

print BASE, 1, Curr;

for i in arange(1,POWER):
    Curr = Iter(BASE, Curr);
    print BASE, i+1, Curr;
