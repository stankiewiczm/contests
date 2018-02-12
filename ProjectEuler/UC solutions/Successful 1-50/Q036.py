from Numeric import *;

def Check(P):
    Pal = P;
    BTwo = zeros(20);       LTwo = 0;
    while (Pal > 0):
        BTwo[LTwo] = Pal%2;
        Pal = Pal/2;
        LTwo = LTwo+1;
    for I in arange(LTwo):
        if (BTwo[I] != BTwo[LTwo-1-I]):
            return 0;
    print P,BTwo;
    return P;

TOT = 0;
for i in arange(1,10):
    TOT += Check(i);                                   # 1 digit palindromes;
    TOT += Check(11*i);                                # 2 digit palindromes;
    for j in arange(10):
        TOT += Check(101*i+10*j);                      # 3 digit palindromes;
        TOT += Check(1001*i+110*j);                    # 4 digit palindromes;
        for k in arange(10):
            TOT += Check(10001*i + 1010*j + 100*k);
            TOT += Check(100001*i + 10010*j + 1100*k);
#Check(595);

print "All done,",TOT
            
