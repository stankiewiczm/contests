from Numeric import *

LIM = 5000000;      LFG = zeros(LIM+1);
MOD = 1000000;      PM = 524287;

for k in arange(1,56):
    LFG[k] = ( int((100003 - 200003*k + 300007*k*k*k)%MOD) );
for k in arange(56, LIM+1):
    LFG[k] = int(( LFG[k-24] + LFG[k-55] )%MOD);
    if (LFG[k] == PM):
        print k, PM

for k in arange(1,LIM/2):
    if (LFG[2*k] == LFG[2*k-1]):
        print 2*k, LFG[2*k]
