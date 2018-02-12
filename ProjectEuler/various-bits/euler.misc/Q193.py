from Numeric import *
from time import *

LIM = 2**50;    MAX = 2**20;    Prime = [2];    NP = 0;     t0 = time();

def Gen():
    IsP = ones(MAX);    IsP[1] = 0;      

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

    print "Generated",NIsP,"primes up to ",Prime[-1],"in a time of ",time()-t0;
    return NIsP;


NP = Gen();
L1 = [];    L2 = [];    L3 = [];    L4 = [];
L5 = [];    L6 = [];    L7 = [];    L8 = [];

for el in range(NP-1,-1,-1):
    p = Prime[el];
    if (el%100 == 2):
        print el, p
    for q in L7:
        if (q*p < MAX):
            L8.append(q*p);
    for q in L6:
        if (q*p < MAX):
            L7.append(q*p);
    for q in L5:
        if (q*p < MAX):
            L6.append(q*p);
    for q in L4:
        if (q*p < MAX):
            L5.append(q*p);
    for q in L3:
        if (q*p < MAX):
            L4.append(q*p);
    for q in L2:
        if (q*p < MAX):
            L3.append(q*p);
    for q in L1:
        if (q*p < MAX):
            L2.append(q*p);
    L1.append(p)


TotLen = len(L1)+len(L2)+len(L3)+len(L4)+len(L5)+len(L6)+len(L7)+len(L8);

print TotLen, time()-t0


"""
LIST = [];                       # All combinations of prime-tuplets to check
for p in range(NP-1,-1,-1):      # Primes in reverse order
    NewLIST = [];

    for Elmt in LIST:
        PRD = 1;        NewElmt = [];
        for r in Elmt:
            PRD *= r;
            NewElmt.append(r);

        if PRD*Prime[p] <= MAX:
            NewElmt.append(Prime[p]);
            NewLIST.append(NewElmt);

    LIST.append([Prime[p]]);
    for nl in NewLIST:
        LIST.append(nl);
        



LIM = 100000;     NUM = 0;
P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,87,97];

for k in range(1,LIM+1):
    Valid = True;
    for p in P:
        if (k%(p*p) == 0):
            Valid = False;
    if Valid:
        NUM += 1;
    if k%1000 == 0:
        print k, NUM


TOT = LIM;
for a in range(len(P)):
    p = P[a];
    DCp = 0;
    Np = LIM/(p*p);     # of numbers divisible by p^2;
    for b in range(a):
        DCp += Np/(P[b]**2)  # Numbers with a lower prime factor
    TOT -= Np-DCp

"""


