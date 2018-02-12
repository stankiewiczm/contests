from numpy import *

Sum = 0;        F = [1,1,2,6,24,120,720,5040,40320,362880];

for n in range(5,100000):
    Sn = 0;     i = 1;
    while n > i:
        Sn += F[(n/i)%10];
        i *= 10;
#    print n, Sn;
    if Sn == n:
        print n;
        Sum += n;

print "\n",Sum
