from numpy import *

MAX = 200000;       Prime = [2];        IsP = ones(MAX);        IsP[1] = 0;
for k in range(MAX/2):
    IsP[2*k] = 0;

N = 3;
while (N < MAX):
    if IsP[N]:
        Prime.append(N);
        for k in range(2,MAX/N):
            IsP[N*k] = 0;
    N += 2;
            
print Prime[10000];
