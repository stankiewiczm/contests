from numpy import *

Count = zeros(1200, int);

for a in range(3,350):
    for b in range(a, (500-a/2)):
        c2 = a*a+b*b;
        c = int(sqrt(c2));
        if c*c == c2:
            Count[a+b+c] += 1;

for k in range(1001):
    if Count[k] == max(Count):
        print k, Count[k];
