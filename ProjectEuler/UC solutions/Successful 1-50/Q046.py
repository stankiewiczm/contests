from Numeric import *

Prime = zeros(10001);   Prime[0] = 2;   Prime[1] = 3;   NP = 0;
IsP = zeros(104750);    IsP[2] = 1;     IsP[3] = 1;
IsG = zeros(104750);    LIM = 1e5;


def Generate():
    N = 3;
    NPrime = 2;
    while(NPrime < 10001):
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
    return NPrime;
            

NP = Generate();
print Prime[10000];

for i in arange(NP):
    for j in arange(320):
        K = Prime[i]+2*j*j
        IsG[K] = 1;
        if K > LIM:
            break;

N = 1;
while (N < LIM):
    N = N+2;
    if (IsP[N] == 0) and (IsG[N] == 0):
        print N;
        break;
    
    


