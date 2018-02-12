from Numeric import *

def GCD(a,b): #With a > b
    while (b != 0):
        B = b;
        b = a-(a/b)*b;
        a = B;
    return a;



S = 0;
for i in arange(10001):
    Jlow = i/3 + 1;     Jhigh = i/2+1;
    for j in arange(Jlow, Jhigh):
        if (GCD(i,j) == 1) and (j*2 < i):
            S = S+1;

print S;        
