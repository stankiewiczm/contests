from numpy import *

N = 648466233099656895;

#P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97];
LIST = [];
k = 3;

while (N > k*k):
    while (N%k == 0):
        LIST.append(k);
        N = N/k;
    k += 2;
LIST.append(N);

print LIST;

ANS = 6*2*4*2*2*3*3*2*2;


print ANS;
print 2*ANS;
