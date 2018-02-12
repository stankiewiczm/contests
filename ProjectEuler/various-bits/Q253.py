from numpy import *
from RandomArray import *

N = 40;     MC = 1000;

def Rand(n):
    L = [];     N = [];
    for a in range(n):
        L.append(a+1);
    for a in range(n):
        b = int((n-a)*random());
        N.append(L[b]);
        L.pop(b);
    return N
    

def Analyze(Seq):
    MAX = 0;    Cat = zeros(N+2);       M = 0;      Ms = [];
#    print Seq;
    for e in Seq:
        Cat[e] = 1;
        if (Cat[e-1] + Cat[e+1] == 0):
            M += 1;
            Ms.append(M);
        if (Cat[e-1] + Cat[e+1] == 2):
            M -= 1;
#        print M, Cat;

    return max(Ms)


TOT = 0.;    Cnt = 0;
while (Cnt < 1e7):
    for t in range(MC):
        An = Analyze(Rand(N));
        TOT += An;
#        Hist[An] += 1;
    Cnt += MC;
    print Cnt, int(1000000*TOT/Cnt)/1000000.;
