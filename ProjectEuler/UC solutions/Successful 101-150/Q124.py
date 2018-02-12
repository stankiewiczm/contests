from Numeric import *

MAX = 1001;    Prime = list();    Prime.append(2);    
IsP = ones(MAX);        IsP[1] = 0;     NP = 0;  

def Gen():
    for i in arange(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    NIsP = 1;
    while (n < MAX):
        if (IsP[n] == 1):
            Prime.append(n);
            NIsP += 1;
            for i in arange(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n = n+2;
    return NIsP;
        
    
def Rad(N):
    N0 = N;     M0 = 1;
    for i in arange(NP):
        if (N0%Prime[i] == 0):
            M0 = M0*Prime[i];
        while (N0%Prime[i] == 0):
            N0 = N0/Prime[i];
    return M0*N0;


NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];
LIST = list();      LIST.append(0);

for i in arange(1,100001):
    LIST.append(Rad(i)*1000000+i);
SLIST = sort(LIST);
print SLIST[10000]%100000;
