from Numeric import *

MT = 1000000;
Lams = zeros(MT+1);     MLen = MT/4+1;


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

print MT, sum(Lams);
             
