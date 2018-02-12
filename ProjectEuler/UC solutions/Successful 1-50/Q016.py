from Numeric import *;

Len = 310;  Dig = zeros(Len);   Dig[0] = 1;

def Mult(n):
    for i in arange(Len):
        Dig[i] = Dig[i]*n;
    Carry = 0;
    for i in arange(Len):
        Dig[i] = Dig[i]+Carry;
        Carry = Dig[i]/10;
        Dig[i] = Dig[i]%10;

for k in arange(1000):
    Mult(2);
print Dig, sum(Dig);