from Numeric import *;

Len = 300;  Dig = zeros(Len);   Dig[0] = 1;

def Mult(n):
    for i in arange(Len):
        Dig[i] = Dig[i]*n;
    Carry = 0;
    for i in arange(Len):
        Dig[i] = Dig[i]+Carry;
        Carry = Dig[i]/10;
        Dig[i] = Dig[i]%10;


def SumDig(a,b):        # Sum of digits of a^b;
    for i in arange(Len):
        Dig[i] = 0;
    Af = 1;     Ex = 0;
    while (Af < 1e6):
        Af = Af*a;
        Ex = Ex+1;
    Dig[0] = a**(b%Ex);
#    print a,b,Dig[0],Af;
    Mult(1);
    for j in arange(b/Ex):
        Mult(Af);
    return sum(Dig);


MX = 0;     Ma = 0;     Mb = 0;     Tm = 0;
for A in arange(100,80,-1):
    if (A%10 != 0):
        for B in arange(60,101):
            Tm  = SumDig(A,B);
            if (Tm > MX):
                MX = Tm;
                Ma = A;
                Mb = B;
                print "New leader:",A,"^",B," has sum",MX;
    print "Completed ",A;

