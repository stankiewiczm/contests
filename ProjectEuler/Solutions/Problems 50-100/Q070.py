from numpy import *

MAX = 10**4;    Prime = [2];     NP = 0;  
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
        

def SameDig(n1, n2):
    Dig = zeros(10,int);
    while (n1 > 0):
        Dig[n1%10] += 1;        n1 /= 10;
    while (n2 > 0):
        Dig[n2%10] -= 1;        n2 /= 10;
    return (min(Dig) == max(Dig))

#############################

NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];

Min = 2.
for i in range(200, 450):
    j  = i+1;
    while (Prime[j]*Prime[i] < 10**7):
        N = Prime[i]*Prime[j];
        PHI = N-Prime[i]-Prime[j]+1;
        if SameDig(N, PHI):
            if (PHI*Min > N):
                Min = (N+0.)/PHI;
                print (Prime[i], Prime[j]), (N, PHI), (N+0.)/PHI;
        j += 1;
