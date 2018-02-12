from Numeric import *

MT = 1000000;
Lams = zeros(MT+1);     MLen = MT/4+1;      Nn = zeros(85);     SN = 0;


for i in arange(MT/4+2):
    if (i*i > MT):
        J = int(floor(sqrt(float(i*i-MT))-0.1));
    else:
        J = 0;
    for j in arange(i-2,J,-2):
        Sz = i*i-j*j;
        if (Sz <= MT):
            Lams[Sz] = Lams[Sz]+1;
#            print i,j,"tiled with",Sz;

for i in arange(MT+1):
    Nn[Lams[i]] = Nn[Lams[i]]+1;

print MT, sum(Lams);

for i in arange(1,11):
    SN = SN+Nn[i];
print SN;
