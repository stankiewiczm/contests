from Numeric import *

Prime = zeros(100000);    Prime[0] = 2;   Prime[1] = 3;     NP = 0;
IsP = zeros(1000001);     IsP[2] = 1;     IsP[3] = 1;

def Generate():
    N = 3;
    NPrime = 2;
    while(N < 1e6):
        N = N+2;
        Good = 1;
        for i in arange(min(NPrime,170)):
            if (N%Prime[i] == 0):
                Good = 0;
                break;
        if (Good == 1):
            Prime[NPrime] = N;
            NPrime = NPrime + 1;
            IsP[N] = 1;
    return NPrime;


NP = Generate();     SS = 0;    DIG = 2;    MOD = 10;
print NP, Prime[NP-1];

for i in arange(NP):
    DIG = len(str(Prime[i]));
    MOD = 10**(DIG-1);
    Gd  = 1;    I = Prime[i];
    for j in arange(DIG):
        I = MOD*(I%10)+I/10;
        if (IsP[I] == 0):
            Gd = 0;
            break;
    if (Gd == 1):
        SS = SS+1;
        print SS,Prime[i],MOD,DIG
print SS;
