from Numeric import *


def NextN(idx):
    if (idx <= 55):
        return (100003 - 200003*idx+300007*idx**3)%1000000-500000;
    else:
        K1 = idx-24-1;
        K2 = idx-55-1;
        return (TABLE[K1/2000][K1%2000]+TABLE[K2/2000][K2%2000])%1000000-500000;
        
        return 0;


TABLE = [];
for i in arange(2000):
    TABLE.append(zeros(2000));

for i in arange(2000):
    for j in arange(2000):
        TABLE[i][j] = NextN(2000*i+j+1);


print len(TABLE), "square generated "



########### HORIZONTAL SUMS ###############
RMAX = zeros(2000);
for R in arange(2000):
    MAX = zeros(2000);      MAX[0] = max(0,TABLE[R][0]);
    for e in arange(1,2000):
        if (MAX[e-1] > 0):
            MAX[e] = MAX[e-1] + TABLE[R][e];
        else:
            MAX[e] = TABLE[R][e];
    RMAX[R] = max(MAX);
print max(RMAX);

########### VERTICAL SUMS ###############
CMAX = zeros(2000);
for C in arange(2000):
    MAX = zeros(2000);      MAX[0] = max(0,TABLE[0][C]);
    for e in arange(1,2000):
        if (MAX[e-1] > 0):
            MAX[e] = MAX[e-1] + TABLE[e][C];
        else:
            MAX[e] = TABLE[e][C];
    CMAX[C] = max(MAX);
print max(CMAX);

########### DIAGONAL ENTRIES PROVED UNNECESSARY 
