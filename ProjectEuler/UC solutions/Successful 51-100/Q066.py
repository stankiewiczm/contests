from Numeric import *

# This is a complete bastardization of the problem
# Straight solution was tried (many times), and eventually chucked out
# Answer of 649 was found on Sloan/Mathworld, and this is simply an attempt
# to reproduce their work.  This is not my own ideas.

# Adaptation of code for Q64 (continued fraction expansions)


def Iter(Seq):
    N = long(1);        D = long(Seq[len(Seq)-1]);
    for h in arange(len(Seq)-2, 0, -1):
        
        T = D;
        D = N + Seq[h]*D;
        N = T;
    N = N+Seq[0]*D;
    return (N,D);


def GCD(a,b):
    while (b > 0):
        c = b;
        b = a-(a/b)*b;
        a = c;
    return a;


def FindFirst(Nprob, FList):
    F0 = int(sqrt(Nprob));      X = 0;      Y = 0;
    SQ = [F0];      Pl = 0;     Flen = len(FList);

    while (Pl < 100):
        (X,Y) = Iter(SQ);
        SQ.append(FList[Pl%Flen]);
        Pl += 1;

        if (X*X-Nprob*Y*Y == 1):
            return X;

    print "Shit has happened: Pl -> 20", Nprob#, X,Y
    return 0;


def ITER(N):
    Nf = sqrt(N);
    REC = zeros(500);
    Tak = int(Nf);      FactD = 1;
    Tak = -Tak;                 Tak0 = Tak;
    Num = Nf - Tak;             Num0 = Num;
    Den = (N-(Tak)**2)/FactD;   Den0 = Den;

    if (Tak+Nf == 0):
        return 0;

    for i in arange(500):
        REC[i] = int(Num/Den);
        Tak = - Tak - REC[i]*Den;
        FactD = Den;

        Num = (Nf - Tak);
        Den = (N-(Tak)**2)/FactD;

        if (Tak0 == Tak) and (Den0 == Den):
            return FindFirst(N, REC[0:1+i])


NUM = 0;        MAX = long(0);        MAXx = 0;       Tx = long(0);
for i in arange(2,10001):
    if (int(sqrt(i))**2 != i):
        Tx = ITER(i);
        if (Tx > MAX):
            MAX  = Tx;
            MAXx = i;
            print MAXx, MAX;

print MAXx, MAX;
