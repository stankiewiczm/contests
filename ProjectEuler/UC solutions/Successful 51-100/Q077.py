from Numeric import *

MAX = 101;        DWay = zeros(MAX);

Prime = list();     Prime.append(2);     NP = 0;  
IsP = ones(MAX);    IsP[0] = 0;         IsP[1] = 0;      

MX = 1230;

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


###############################################
#############  MAIN CODE STARTS HERE ##########
###############################################

NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];
    
for i in arange(MAX/2+1):
    DWay[2*i] = 1;

for i in arange(1,NP):
    Pr = Prime[i];
#    print i, Pr;
    for j in arange(MAX-1,-1,-1):
        DC = DWay[j];
        N0 = j;
        while (N0 + Pr < MAX):
            N0 += Pr;
            DWay[N0] += DC;

for I in arange(MAX):
    if (DWay[I] >= 5000):
        break;
print MAX, max(DWay),"at",I,DWay[I];
