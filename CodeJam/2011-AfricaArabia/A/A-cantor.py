from numpy import *

FILE = open("A-large.in","r");

def Cantor(n):
    C = 0;
    while (C < 25):
        C += 1
        n *= 3;
        if int(n) == 1:
            return C;
        n -= int(n);
    return 30


def Solve( ints, cants ):
    while len(ints) > 0:
        curr = min(cants);
        boot = [];
        for i in range(len(ints)-1, -1, -1):
            if cants[i] == curr:
                   
                cants.pop(i);
                boot.append(ints.pop(i));
        A = sort(boot);
        for e in A:
           print e;
        

N = int(FILE.readline());
for k in range(N):          # Each of the N cases:
    print "Case #%d:" %(k+1)
    S = int(FILE.readline());
    L = [];
    Li = [];    
    Lc = [];
    for i in range(S):
    	L.append(FILE.readline()[:-1]);
        Li.append(float(L[-1]));
        Lc.append( Cantor(Li[-1]) );
    Solve (Li, Lc);

