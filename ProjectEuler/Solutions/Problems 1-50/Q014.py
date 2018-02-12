from numpy import *

Time = zeros(1000, int);     Max = 0;        MaxT = 0;

def Collatz(n0):
    step = 0;       n = n0;
    while (n >= n0):
        step += 1;
        if (n%2 == 0):
            n /= 2;
        else:
            n = 3*n+1;
    return step+Time[n];


Time[1] = 1;
for k in range(2,1000):
    Time[k] = Collatz(k);
    if max(Time) == Time[k]:
        Max = k;

print Max, Time[Max];
