from numpy import *

FILE = open("A-large.in","r");

def Solve(K, c, l, i):
    for q in range (l):
        for r in range(q+1, l):
            if i[q]+i[r] == c:
                print "Case #%d: %d %d" %(K+1, q+1, r+1)
                return;


N = int(FILE.readline());
for k in range(N):          # Each of the N cases:
    C = int(FILE.readline());
    L = int(FILE.readline());
    I = map( int, FILE.readline().split() );

    Solve(k,C,L,I)
