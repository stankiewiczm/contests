#from Numeric import *

LIM = 1000000000000;
MOD = 100000;       Res2 = 0;

I = LIM;            J = LIM;
while (I > 0):
    I = I/2;        J = J/5;
    Res2 += I-J;                # Number of powers of 2

# Product of all bits (no factors of 2 or 5) below 100000 is 1

def Part(K):                    # Partial product up to needed K
    k = 1;      V = 1;
    while (k <= K):
        if (k%5 != 0):
            V = (V*k)%MOD;
        k += 2;
    return V;

p2 = 0;     ANS = 1;
while (p2 < 40):
    I = LIM/(2**p2);
    while (I > 0):
        ANS = ANS*Part(I%MOD)   # MAIN PART
        I = I/5;
    p2 += 1

Res2 = Res2%2500;       ANS = ANS%MOD
print Res2, ANS, "final ansewr ", ANS*(2**(Res2))%MOD;
