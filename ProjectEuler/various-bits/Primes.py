from visual.graph import *

MAX = 1000001;    ARR = ones(MAX+1);  ARR[1] = 1;     MAXP = 350000;

Prime = zeros(MAXP);    Prime[0] = 2;   NP = 0;  
IsP = ones(MAX);        IsP[1] = 0;      

def Gen():
    for i in arange(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    NIsP = 1;
    while (n < MAX):
        if (IsP[n] == 1):
            Prime[NIsP] = n;
            NIsP += 1;
            for i in arange(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n = n+2;
    return NIsP;
        
    

NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];
