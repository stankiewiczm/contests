from Numeric import *;

N = 0;      T = 1;      S = 1;
for i in arange(1,200000):
    for j in str(i):
        N = N+1;
        if N == T:
            T = T*10;
            S = S*int(j);
print S;
