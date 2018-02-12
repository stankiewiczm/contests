from visual.graph import *

MAX = 10000001;    ARR = ones(MAX+1);  ARR[1] = 1;     MAXP = 350000;

Prime = zeros(MAXP);    Prime[0] = 2;   NP = 0;  
IsP = ones(MAX);        IsP[1] = 0;      

def Gen():
    for i in arange(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    NIsP = 1;
    while (n < MAX/2):
        if (IsP[n] == 1):
            Prime[NIsP] = n;
            NIsP += 1;
            for i in arange(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n = n+2;
    return NIsP;
        
    

NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];


for j in arange(NP):
    Pn = Prime[j];
    for k in arange(MAX/Pn,0,-1):
        if (k%Pn != 0):
            Ex = 1;
            Kn = k*(Pn**Ex)
            while (Kn < MAX):
                ARR[Kn] = ARR[Kn]*(Ex+1);
                Ex = Ex+1;
                Kn = Kn*Pn;

print "List is populated"

Tt = 0;
for j in arange(2,MAX):
    if (ARR[j] == ARR[j-1]):
        Tt = Tt + 1;
        if (Tt%10000 == 1):
            print Tt,"found:",j-1,j,"with",ARR[j],"factors"

print Tt;

# Answer: 986262
