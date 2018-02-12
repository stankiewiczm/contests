from numpy import *

N = int(FILE.readline());
for k in range(N):          # Each of the N cases:
    print "Case #%d:" %(k+1),
    N = int(FILE.readline());
    L = [];
    for i in range(N):
        L += [map(int, FILE.readline().split() )];

    Dmin = 0;  
    for i in range(N):
        for j in range(i):
            Dist = abs(L[j][0] - L[i][0]);
            Time = abs(L[j][1] - L[i][1]);
            if 2*Dmin < Dist-Time:
                Dmin = (Dist-Time)/2.0;
    print Dmin

