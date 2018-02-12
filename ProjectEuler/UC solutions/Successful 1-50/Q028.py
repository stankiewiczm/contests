from Numeric import *

N = 1;
S = 1;

while (N < 1000):
    N = N+2;
    S = S + 4*(N*N) -6*(N-1);
print N, S;
    
