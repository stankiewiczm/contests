from Numeric import *;

Len = 30;  Dig = zeros(Len);   Dig[0] = 1;

def Mult(n):
    for i in arange(15):
        Dig[i] = Dig[i]*n;
    Carry = 0;
    for i in arange(15):
        Dig[i] = Dig[i]+Carry;
        Carry = Dig[i]/10;
        Dig[i] = Dig[i]%10;


for a in arange(7):
    Mult(2);
for k in arange(783045):
    Mult(1024);
Mult(28433)
print Dig;
