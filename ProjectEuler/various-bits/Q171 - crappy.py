from Numeric import *

L = 11;     L1 = L+1;   D = 0;  S = 0;  SQR = zeros(42)
for i in arange(42):    SQR[i] = i*i;

Firsts = zeros(1000);
Lasts = zeros(1000);


for N0 in arange(L1):
    for N1 in arange(L1-N0):
        for N2 in arange(L1-N0-N1):
            for N3 in arange(L1-(N0+N1+N2)):
                for N4 in arange(L1-(N0+N1+N2+N3)):
                    for N5 in arange(L1-(N0+N1+N2+N3+N4)):
                        for N6 in arange(L1-(N0+N1+N2+N3+N4+N5)):
                            for N7 in arange(L1-(N0+N1+N2+N3+N4+N5+N6)):
                                for N8 in arange(L1-(N0+N1+N2+N3+N4+N5+N6+N7)):
                                    N9 = L - (N0+N1+N2+N3+N4+N5+N6+N7+N8);

                                    S = N1+4*N2+9*N3+16*N4+25*N5+36*N6+49*N7+64*N8+81*N9;
                                    Firsts[S] += 1;
#                                    if S in SQR:
#                                        TOT += 1;
                                    D += 1;
#                                    print N0,N1,N2,N3,N4,N5,N6,N7,N8,N9
#    print N0


def SDS(n0):
    SD = 0;
    while (n0 > 0):
        SD += (n0%10)**2;
        n0 = n0/10;
    return SD;


for i in arange(1000):
    k = 0;
    while (k*k < i):
        k += 1;
    while (k*k - i < 1000):
        Lasts[i] += Firsts[k*k-i];
        k += 1;

print "Starting the real thing"

ANS = 0;
Ls = 0;
while (Ls < 1e9):
    ANS += Ls*Lasts[SDS(Ls)];
    Ls += 1
    if (Ls % 1000000 == 0):
        ANS = (ANS%1000000000);
        print Ls, ANS;



print "Done", L,D, TOT
