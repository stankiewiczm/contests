from numpy import *

MAX = 10**6;    Prime = [2];     NP = 0;  
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

Phi = zeros(MAX+1, long);
for k in range(2,len(Phi)):
    Phi[k] = k;

NP = Gen();
print "Tables generated"

for p in Prime:
    for k in range((MAX)/p+1):
        Phi[p*k] = (p-1)*Phi[p*k]/p;

print sum(Phi);
