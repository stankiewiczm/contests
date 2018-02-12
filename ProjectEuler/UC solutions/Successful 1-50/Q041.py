from Numeric import *

Prime = zeros(500);    Prime[0] = 2;    Prime[1] = 3;     NP = 0;
F = [1,1,2,6,24,120,720,5040,40320];          D = zeros(10);

def Generate():
    N = 3;
    NPrime = 2;
    while(N < 3e3):
        N = N+2;
        Good = 1;
        for i in arange(min(NPrime,100)):
            if (N%Prime[i] == 0):
                Good = 0;
                break;
        if (Good == 1):
            Prime[NPrime] = N;
            NPrime = NPrime + 1;
    return NPrime;


def Translate(d):
    e = zeros(7);
    e[0] = d[0];
    for i in arange(1,7):
        Cnt = 0;
        Fre = zeros(7-i);
        for j in arange(7):
            Mis = 1;
            for k in arange(i):
                if e[k] == j:
                    Mis = 0;
            if (Mis == 1):
                Fre[Cnt] = j;
                Cnt = Cnt+1;
        e[i] = Fre[d[i]];
    return(e);


def MakePan(N):
    for i in arange(7):
        D[i] = N/(F[6-i]);
        N = N - D[i]*F[6-i];


def Pan(d):
    K = 1111111;
    for i in arange(7):
        K = K + d[i] * 10**(6-i);
    return K;


def Pr(p):
    for y in arange(NP):
        if (p%Prime[y] == 0):
            return 0;
    return 1;

    

NP = Generate()
for A in arange(5039,0,-1):
    MakePan(A);
    B = Pan(Translate(D));
    if (Pr(B) == 1):
        print B;
        break;

print "All done"
