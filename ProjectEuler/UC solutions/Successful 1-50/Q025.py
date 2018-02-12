from Numeric import *

phi = (1. + sqrt(5))/2;
P0  = log10(1./sqrt(5));
Pp  = log10(phi);

for i in arange(13):
    print i, (phi**i-(1-phi)**i)/sqrt(5);

NPhi = ceil( (999.-P0)/Pp );

print NPhi, NPhi*Pp+P0, (NPhi-1)*Pp+P0;
