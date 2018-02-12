from Numeric import *

MX = 100001;
Prime = zeros(MX);    Prime[0] = 2;   Prime[1] = 3;
IsP = zeros(1185180);     IsP[2] = 1;     IsP[3] = 1;

def Generate():
    N = 3;
    NPrime = 2;
    while(NPrime < MX):
        N = N+2;
        Good = 1;
        for i in arange(min(NPrime,100)):
            if (N%Prime[i] == 0):
                Good = 0;
                break;
        if (Good == 1):
            Prime[NPrime] = N;
            NPrime = NPrime + 1;
            IsP[N] = 1;
    return 0;


def Check(Idx):
    P = Prime[Idx];
    G = 1;   N = 10;
    while (P > N):
        if (IsP[P%N] * IsP[P/N] == 0):
            G = 0;
        N = N*10;
    return G;

            

Generate();     SS = 0;
print Prime[MX-1];
for i in arange(4,MX):
    if (Check(i) == 1):
        SS = SS+Prime[i]
        print Prime[i];
print SS;
