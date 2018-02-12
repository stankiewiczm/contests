from Numeric import *;

def LenRuc(p):
    while (p%2 == 0):
        p = p/2;
    while (p%5 == 0):
        p = p/5;
    if (p == 1):
        return 0;
    
    Rem = 10%p;
    N = 1;
    while (Rem > 1):
        Rem = (Rem*10)%p;
        N = N+1;
    return N;

Max = 0;    MAX = 0;    Tm = 0;
for i in arange(2,1000):
    Tm = LenRuc(i);
    if (Tm > MAX):
        MAX = Tm;
        Max = i;
print Max,MAX;
2
