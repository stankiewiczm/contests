from Numeric import *

Prime = zeros(1234);    Prime[0] = 2;   Prime[1] = 3;      NP = 0;

ALL = list();
for i in arange(10000):
    ALL.append([]);


def Sort(N):
    Dl = list();
    for d in str(N):
        Dl.append(int(d));
    D = sort(Dl);
    SN = 0;
    for b in arange(len(D)):
        SN = SN*10+D[b];
    return SN;


def Generate():
    N = 3;
    NPrime = 2;
    while(N< 10001):
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
            

NP = Generate();
for i in arange(168,1230):
    Sprime = Sort(Prime[i]);
    ALL[Sort(Sprime)].append(Prime[i]);

Nm = 0;
for i in arange(10000):
    if len(ALL[i]) > 3:
        for a in arange(len(ALL[i])):
            for b in arange(a):
                A = ALL[i][a];  B = ALL[i][b];
                if (A+B)/2 in ALL[i]:
                    print ALL[i],"\nPossible solution as ",A,(A+B)/2,B,"with difference:",abs((A-B)/2);
                    Nm  = Nm+1;
#        print i, ALL[i];
print Nm;
