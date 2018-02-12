from numpy import *

MAX = 10**6;    Prime = [2];     NP = 0;  
IsP = ones(MAX);                IsP[1] = 0;

def Gen():
    for i in range(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    while (n < MAX):
        if (IsP[n] == 1):
            Prime.append(n);
            for i in arange(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n += 2;
    return len(Prime);
        

def MakeMap():
    ALL = [];       
    for a in range(1,6):
        for b in range(1,a):
            for c in range(1,b):
                Hull = 10**a+10**b+10**c;
                Rest = [100000,10000,1000,100,10,1];
                Rest.remove(10**a);
                Rest.remove(10**b);
                Rest.remove(10**c);
                ALL.append([Hull, Rest]);
    return ALL;        


def Solve(parms):
    [d, [P,Q,R]] = parms;
    for n in range(1,1000):
        if (n%2 != 0) and (n%5 != 0):
            a = n/100;
            b = (n/10)%10;
            c = n%10;

            NPrime = 0;
            for k in range(1,10):
                NPrime += IsP[ k*d + P*a+Q*b+R*c ];
            if NPrime >= 8:
                print d+P*a+Q*b+R*c;
    
#############################

NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];

LIST = MakeMap();
for e in LIST:
    Solve(e);
