from Numeric import *

Fact = [1,1,2,6,24,120,720,5040,40320,362880];
Mixd = zeros(1000000);      ANS = 0;


def Mix(P):
    Ss = 0;
    for a in str(P):
        Ss = Ss + Fact[int(a)];
    return Ss;

def Perm(p):
    DIG = zeros(10);
    for q in str(p):
        DIG[int(q)] += 1;
    Ret = Fact[len(str(p))];
    if (DIG[0] == 1):
        Ret -= Ret/(len(str(p)));
    for q in arange(1,10):
        Ret = Ret / Fact[DIG[q]];
    return Ret;


def Chain(N):
    M = N;
    Ls = list();
    Ls.append(N);
    for i in arange(59):
        if (N < 1e6):
            N = Mixd[N];
        else:
            N = Mix(N);
        Ls.append(N);

    Good = 1;
    for j in arange(59):
        if (N == Ls[j]):
            Good = 0;
            break;
    if (Good == 1):
        print M,Perm(M);
        return Perm(M);
    return 0;

def RevSort(N):
    Dl = list();
    for d in str(N):
        Dl.append(int(d));
    D = sort(Dl);
    SN = long(0);
    for b in arange(len(D),0,-1):
        SN = SN*10+D[b-1];
    return SN;


for i in arange(1000000):
    Mixd[i] = Mix(i);
print "Collected"

for i in arange(100000):            # Up to 5 digits long
    if (i == RevSort(i)):
        ANS = ANS + Chain(i);

for a in arange(10):                # 6 Digit beasts
    for b in arange(a+1):
        for c in arange(b+1):
            for d in arange(c+1):
                for e in arange(d+1):
                    for f in arange(e+1):
                        I = ((((10*a+b)*10+c)*10+d)*10+e)*10+f;
                        ANS = ANS + Chain(I);

print "Done, answer being",ANS;
