from Numeric import *

MAX = 150000000;    IsP = ones(MAX+1);        IsP[1] = 0;
Mx1 = 100000;     PRIME = [2];              Prime = [2];

def Gen():
    for i in arange(2,MAX/2+1):
        IsP[2*i] = 0;
    n = 3;
    while (n < MAX):
        if (IsP[n] == 1):
            PRIME.append(n);
            if (n < Mx1):
                Prime.append(n);
            for i in arange(2,MAX/n+1):
                IsP[n*i] = 0;
                
        n += 2
    return;

Gen();
print "Generated",len(PRIME),"primes up to ",PRIME[-1];
print "Generated",len(Prime),"primes up to ",Prime[-1];

################################################################

def Pass1(n1):
    M = n1*n1;
    if (M+27 < MAX):
        if (IsP[M+1] == IsP[M+3] == IsP[M+7] == IsP[M+9] == IsP[M+13] == IsP[M+27] == 1):
            return n1;
        return 0

    else:
        for p in Prime:
            if p >= n1:
                return n1;
            M2 = (M+9)%p
            if (M2 == 8) or (M2 == 6) or (M2 == 2) or (M2 == 0):
                return 0;
            if ((M+13)%p == 0) or ((M+27)%p == 0):
                return 0;
        return n1;


def Pass2(n2):
    for p in PRIME:
        if p >= n2:
            return True;
        M = (n2*n2+9)%p;
        if (M == 8) or (M == 6) or (M == 2) or (M == 0):
            return False
        if ((M+4)%p == 0) or ((M+18)%p == 0):
            return False;
    return True;


def FinalCheck(f):                  # Need to ensure that n^2+21 is not prime
    Pr = f*f+21;
    for p in PRIME:
	if (Pr%p == 0) and (Pr != p):
            print f,'+21 is divisible by',p;
            return True;
    return False;

##########################################################
	
TOT = 0;        LIST = [];      n = 0;      L2 = [];    FLIST = [];
while n < 15000000:
    n += 1;
    if (n%3 != 0) and ((n%7 == 1) or (n%7 == 6)):
        if (Pass1(10*n) != 0):
            LIST.append(10*n);

print "First pass completed", len(LIST);

for n in LIST:
    if (Pass2(n)):
        print n,;       L2.append(n);
print "\nSecond pass completed\n"

for F in L2:
    if FinalCheck(F):
        FLIST.append(F);        TOT += F;       print F;
        
