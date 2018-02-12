from numpy import *

Fin = zeros(600, int);       ANS = 0;

def SSQ(n):
    R = 0;
    while (n > 0):
        R += (n%10)**2;
        n /= 10;
    return R;

def Run(n):
    while (n != 1) and (n != 89):
        n = SSQ(n);
#        print n
    if (n == 89):
        return 1;
    return 0;


for n in range(1,600):
    Fin[n] = Run(n);
for n in range(600,10**7):
    ANS += Fin[SSQ(n)];
print ANS+sum(Fin);
