from numpy import *

R2 = [ [3,2] ];     N = 3;      D = 2;      ANS = 0;    Ten = 1;

while len(R2) < 1000:
    D = N+D;            N = 2*D-N;      
    R2.append( [N,D] );
    if (N > 10*Ten):
        Ten *= 10;
    if (Ten > D):
        ANS += 1;
print ANS


