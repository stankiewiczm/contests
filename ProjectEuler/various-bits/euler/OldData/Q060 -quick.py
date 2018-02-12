from visual.graph import *

MAX = 1000001;    Prime = list();    Prime.append(2);    NP = 0;  
IsP = ones(MAX);        IsP[1] = 0;      

# There are 9592 primes below 100000;

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
        
    
NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];


def IsPrime(prime):
    for i in Prime:
        if (prime % i == 0):
            if (prime == i):
                return True;
            return False;
    return True;

def ConCat(i1,i2):
    P1 = int(str(i1)+str(i2));
    P2 = int(str(i2)+str(i1));
    
#    P1 = int(10**(ceil(log10(i2)))*i1+i2);
#    P2 = int(10**(ceil(log10(i1)))*i2+i1);

    if P1 < 1e6:
        return ( IsP[P1] == IsP[P2] == 1);
    
    if (IsPrime(P1)):
        if (IsPrime(P2)):
            return True;
    return False;                                         
                                     


PMAX = 1060;    Friends = list();    
for i in arange(PMAX):
    Friends.append(zeros(PMAX));

for i in arange(PMAX):
    if (i%100 == 99):
        print i+1    
    for j in arange(i):
        if ConCat(Prime[i],Prime[j]):
            Friends[i][j] = 1;
            Friends[j][i] = 1;

for i in arange(PMAX):          # Two starting primes
    for j in arange(i):         #
        if (Friends[i][j] == 1):
            for p in arange(j):
                if (Friends[i][p] == Friends[j][p] == 1):
                    for q in arange(p):
                        if (Friends[i][q] == Friends[j][q] == Friends[p][q] == 1):
                            for r in arange(q):
                                if (Friends[i][r] == Friends[j][r] == Friends[p][r] == Friends[q][r] == 1):
                                    print i,j,p,q,r,"or in primes", Prime[i], Prime[j], Prime[p],Prime[q],Prime[r];
