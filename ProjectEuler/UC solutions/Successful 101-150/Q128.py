from Numeric import *

Ends = [1];
for i in arange(1,70000):
    Ends.append( long(i)*6+Ends[i-1]);


MAX = 1000001;    Prime = list();    Prime.append(2);    NP = 0;  
IsP = ones(MAX);        IsP[1] = 0;      

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


def End(i):
    if (i >= 0):
        return Ends[i];
    else:
        return 0;


def NPrimes(List, A):
    Ps = 0;
    for p in List:
        Ps += IsP[p];
    return Ps;



def EDS(n):
    if (n == 1) or (n == 2):
        return True;
    N = n-1;
    if (N%6 == 0):
        N = N/3;
        TS = (sqrt(N+0.25)-0.5);
        if (abs(TS - round(TS)) < 1e-6):
            return True;
    return False;


def CountPs(A,Row):
    L = [];

    if (EDS(A-1)):     # New row;
        L = [6*Row+7, 6*Row+5, 6*(2*Row+3)-1];
    if ( EDS(A)):
        L = [6*Row+5, 6*Row+11, 6*(2*Row+1)-1]

    return NPrimes(L,A);


NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];
Row = -1;        TOT = 0;
print "Starting"
for u in Ends:
    if (CountPs(u,Row) == 3):
        TOT += 1;
    Row += 1;
    if (CountPs(u+1,Row) == 3):
        TOT += 1;
        if (TOT%100 == 0):
            print TOT, u+1 , (Row),CountPs(u+1,Row);
