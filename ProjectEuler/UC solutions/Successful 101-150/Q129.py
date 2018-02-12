from Numeric import *

def Mink(n):
    M = 1;
    S = 1;
    k = 1;
    while (S != 0):
        M = (M*10)%n;
        S = (S+M)%n;
        k += 1;
    return k


for i in arange(1000000,1000050):
    if (i%2 == 1) and (i%5 != 0):
        if (Mink(i) > 1e5):
            print i, Mink(i);

        
