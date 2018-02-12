from Numeric import *

def GCD(a,b):
    A = max(a,b);     B = min(a,b);
    while (B != 0):
        C = B;
        B = A - B*(A/B);
        A = C;
    return A;

LIM = 100000000; #100000;
TOT = long(0);

# IMAGINARY PARTS
for r in arange(1,10000):
    for i in arange(1,r+1):
        if GCD(r,i) == 1:
            M2 = r*r + i*i;
            Meff = M2;

            if (Meff <= LIM):
                Tmp = 0;
                Mult = 1;       # GCD Multiplication factor
                
                while (LIM >= Meff*Mult):
                    Tmp += 2*Mult*r*(LIM/(Meff*Mult));
                    if (i != r):
                        Tmp += 2*Mult*i*(LIM/(Meff*Mult));
                    Mult += 1;
                    
                TOT += Tmp;
print "Imaginary parts",TOT

# REAL PARTS
for i in arange(1,LIM+1):
    TOT += (LIM/i)*i;

print LIM, TOT;
