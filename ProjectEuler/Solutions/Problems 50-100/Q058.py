from numpy import *

MAX = 10**5;    Prime = [2];     NP = 0;  
IsP = ones(MAX);                IsP[1] = 0;

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
    return len(Prime);


def Check(p):
    for k in range(NP):
        if (p%Prime[k] == 0):
            return 0;
        if (p < Prime[k]**2):
            Diag.append(p);
            return 1;
                        
#############################

NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];

N = 3;      S = 1;      Diag = [3,5,7];      All = [1,3,5,7,9];
while (10*len(Diag) >= len(All)):
    L = N+1;            N2 = N*N;
    Check(N2+L);        All.append(N2+L);
    Check(N2+2*L);      All.append(N2+2*L);
    Check(N2+3*L);      All.append(N2+3*L);       All.append(N2+4*L);

    N += 2;
#    if (N%5000 == 1):
#        print N, len(Diag), len(All);
print N;
