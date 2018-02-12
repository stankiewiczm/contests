from Numeric import *

MAX = 150000000;  PRIME = [2];     IsP = ones(MAX+1);     IsP[0] = 0;     IsP[1] = 0;
def Gen():
    for k in arange(2,MAX/2+1):
        IsP[2*k] = 0;
    k = 3;
    while (k < MAX):
        if (IsP[k] == 1):
            PRIME.append(k);
            for l in arange(2,MAX/k+1):
                IsP[k*l] = 0;
        k += 2;
    print "Generated",len(PRIME),"primes up to ",PRIME[len(PRIME)-1]


def Check(N):
    M = 100*N*N;
    if (M+27 < MAX):
        if (IsP[M+1] == IsP[M+3] == IsP[M+7] == IsP[M+9] == 1):
            print "Possibile for ",10*N,;
            if (IsP[M+13] == IsP[M+27] == 1):
                print "WOOOOOOOOOO",10*N
                return True;
            print "nah"
        return False;

#    print N, M+1, M+3,'...'
#    Poss = True;
    
    for p in PRIME:
        n2 = M%p;
        if (n2 == p-1) or (n2 == p-3) or (n2 == p-7) or (n2 == p-9):
            return False;
        if ((n2+13)%p == 0) or ((n2+27)%p == 0):
            return False;
#        if (p > 10*N):
#            return True;
    return True;


Gen();  TOT = 0;
for n in arange(1,15000001):      # Divide by 10.        # Up to 150 MIL
    if (n%3 != 0) and ((n%7 == 1) or (n%7 == 6)):
        if (Check(n)):
            print n, 10*n;
            TOT += 10*n;
print "Finished with a total of ",TOT

    
