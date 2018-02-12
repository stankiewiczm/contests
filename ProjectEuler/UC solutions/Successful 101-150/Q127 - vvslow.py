from Numeric import *

MAX = 100001;    Prime = list();    Prime.append(2);    
IsP = ones(MAX);        IsP[1] = 1;     NP = 0;
RAD = zeros(100001);

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
    N0 = N;     M0 = 1;     i = 0;
    while (IsP[N0] == 0):
#        print N0, i
        if (N0%Prime[i] == 0):
            M0 = M0*Prime[i];
        while (N0%Prime[i] == 0):
            N0 = N0/Prime[i];
        i += 1;
    return M0*N0;


def GCD1(A0,B0):
    A = A0;     B = B0;     C = 0;
    while (B > 0):
        C = A - (A/B)*B;
        A = B;
        B = C;
    return (A == 1);
    

NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];


for i in arange(1,100001):
    RAD[i] = Rad(i);

TOT = 0;        SUM = 0;    BA = 0;
for c in arange(2,100000):
    if (RAD[c] < c):
        BA = c/RAD[c];
        for a in arange(1,(c+1)/2):
            if GCD1(c,a):
                if RAD[a]*RAD[c-a] < BA:
                    TOT += 1;
                    SUM += c;
                    print "#",TOT,"is: ",a,c-a,c;


print "Obtained a total of",TOT,"events, with sum",SUM;

# Obtained a total of 414 events, with sum 13994897
# Obtained a total of 417 events, with sum 14092265
# Obtained a total of 418 events, with sum 14125034
