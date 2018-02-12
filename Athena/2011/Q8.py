from numpy import *

Prime = [2];            BigP = [];
def Gen():
    MAX = 10**6+50;     IsP = ones(MAX+1,int);
    k = 3;
    while (k < MAX):
        if IsP[k]:
            Prime.append(k);
            for l in range(2,MAX/k+1):
                IsP[l*k] = 0;
        k += 2;
    print "There are",len(Prime),"primes up to ",MAX;
    return;

def BigGen():
    MAX = 10**8;
    IsP = ones(MAX+1, int);     IsP[0] = 0;     IsP[MAX] = 0;
    for p in Prime:
        mult = (Xmin/p+1)*p-Xmin;
        while (mult < MAX):
            IsP[mult] = 0;
            mult += p;

    k = 1;
    while (k < MAX):
        if (IsP[k] == 1):
            BigP.append(k);
        k += 2;

    print "There are",len(BigP),"primes up to ",BigP[-1];
    print sum(IsP);
    return;

Xmin = 1000000000000
Xmax = 1000100000000
        
Gen();
BigGen();


"""
def mystery(x):
    # Only accept primes
    if (x == 2) or (x == 5):
        return x-1;

    per # length of repeating decimal
    len # digits in per
    hex # len in hex
    if (len%16 == 1):
        return 1;
    den = 10**(len/2);
    first = per/den;
    second= per%den;
    third = first+second;
    return den-third
"""



