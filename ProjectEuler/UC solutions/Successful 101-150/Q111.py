from Numeric import *

MAX = 100001;    Prime = list();    Prime.append(2);    NP = 0;    DIG = 10;

def Gen():
    IsP = ones(MAX);        IsP[1] = 0;      
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


def CheckP(p0):
    if p0 < 1e9:
        return False;
    for i in arange(NP):
        if p0%Prime[i] == 0:
            if (p0 == Prime[i]):
                return True;
            return False;
    return True;

NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];

S = list();             H = list();
for i in arange(10):
    S.append(long(0));
for i in arange(DIG):
    H.append(((10**DIG)-1)/9);
    H[i] = H[i] - 10**i;

#print H

#####################################
############### ZERO CASE ###########
for i in arange(1,10):
    for j in arange(1,10):
        IJ = 10**(DIG-1)*i+j;
        if (CheckP(IJ)):
#            print IJ ,"is prime"
            S[0] += IJ;

####################################
######## ALL OTHER CASES ###########
for D in arange(1,10):
    for i in arange(DIG):
        for j in arange(10):
            IJ = D*H[i]+10**i*j
            if CheckP(IJ):
#                print IJ, "9-digit repeat prime";
                S[D] += IJ;

####################################
############# The case of TWO ######    Must be last digit...

for i in arange(1,DIG):
    for j in arange(10):
        for k in [1,3,7,9]:
            IJ = (2*H[i]-2)+10**i*j + k;
            if CheckP(IJ):
                S[2] += IJ;
            IJ = (8*H[i]-8)+10**i*j + k;
            if CheckP(IJ):
                S[8] += IJ;

print S,"\n\n",sum(S);

