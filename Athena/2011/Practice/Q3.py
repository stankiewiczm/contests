from numpy import *

MAX = 60000;
Prime = [2];        
IsP = ones(MAX+1);
Super = [];
SuperN = [];

def AllDiff(n):
    digs = zeros(10,int);
    while n > 0:
        digs[n%10] += 1;
        n /= 10;
    return max(digs) < 2;
    
def Generate():
    IsP[1] = 0;     NP = 0;
    for i in range(2,MAX/2+1):
        IsP[2*i] = 0;
    for i in range(3, MAX):
        if IsP[i] == 1:
            Prime.append(i);        NP += 1;
            for j in range(i, MAX/i+1):
                IsP[i*j] = 0;

    print "Generated",NP,"primes up to",MAX;
    return NP;

def Nx(n):
    c = 9876543210/n;
    d = 0;
    while (d < 1e6):
        if AllDiff(n*(c-d)):
            if d > 5000:
                print n, c, d, n*(c-d);
            return n*(c-d);
        d += 1;
    print "Holy Shit ...", n
    return 0


Generate();
for i in range(700):
    Super.append( Prime[Prime[i]-1] );
    SuperN.append( Nx(Super[-1]) );
