from Numeric import *

def Bin(N0):
    dig = zeros(100);
    N = N0;     pos = 0;
    while N > 0:
        dig[pos] = N%2;
        N = N/2;
        pos += 1;
    An = 0;
    for i in arange(pos, -1, -1):
        An = An*10+dig[i];
    return An;

Way = list();
for i in arange(6):
    Way.append(zeros(32));

Way[0][1] = 1;      Way[0][0] = 1;      Way[0][2] = 1;
for p in arange(1,6):
    PW = 2**p;
    for h in arange(32):
        Way[p][h] = Way[p-1][h];
        if (h >= PW):
            Way[p][h] += Way[p-1][h-PW];
        if (h >= 2*PW):
            Way[p][h] += Way[p-1][h-2*PW];


for i in arange(32):
    print i, Way[5][i], "binary", Bin(i);

print Bin(5**25)

#print Bin(10);
