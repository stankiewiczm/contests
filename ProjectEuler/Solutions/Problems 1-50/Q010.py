from numpy import *

MAX = 2000000;       Prime = [2L];        IsP = ones(MAX);        IsP[1] = 0;
for k in range(MAX/2):
    IsP[2*k] = 0;

N = 3;
while (N < MAX):
    if IsP[N]:
        Prime.append(N);
        for k in range(2,(MAX+N-1)/N):
            IsP[N*k] = 0;
    N += 2;

print sum(Prime)
