from numpy import *

MAX = 10**4;    Prime = [2];     NP = 0;  
IsP = ones(MAX);                IsP[1] = 0;
P2 = [];        P3 = [];        P4 = [];        LIM = 5*10**7;

def Gen():
    for i in range(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    while (n < MAX):
        if (IsP[n] == 1):
            Prime.append(n);
            for i in arange(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n += 2;

    for p in Prime:
        if (p*p < LIM):
            P2.append(p*p);
            if (p*p*p < LIM):
                P3.append(p*p*p);
                if (p**4 < LIM):
                    P4.append(p**4);

    return len(Prime);

Gen();      CanDo = zeros(LIM+1, int);      NC = [];
for a in P2:
    for b in P3:
        for c in P4:
            if (a+b+c < LIM):
                CanDo[a+b+c] = 1;
                NC.append(a+b+c);

print sum(CanDo), len(NC);

