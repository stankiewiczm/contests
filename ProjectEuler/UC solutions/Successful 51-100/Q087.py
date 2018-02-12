from Numeric import *

MAX = 10000;    Prime = list();    Prime.append(2);    NP = 0;  
IsP = ones(MAX);        IsP[1] = 0;     BIG = 5e7;

SQRS = list();      CUBS = list();       FRTS = list();

LIST = list();

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

for i in Prime:
    if i**2 < BIG:
        SQRS.append(i**2);
    if i**3 < BIG:
        CUBS.append(i**3);
    if i**4 < BIG:
        FRTS.append(i**4);

print len(SQRS), len(CUBS), len(FRTS);

TOT = 0;
for i in SQRS:
    for j in CUBS:
        for k in FRTS:
            I = i+j+k
            if (I < BIG):
                LIST.append(I);
                TOT += 1;
#                LIST[i+j+k] = 1;

print TOT, len(LIST)

SLIST =  sort(LIST);

for i in arange(len(SLIST)-1):
    if SLIST[i] == SLIST[i+1]:
#        print SLIST[i];
        TOT = TOT-1;

print TOT, len(SLIST)




