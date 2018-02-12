from numpy import *

#10^18th digit is same as 10^16th digit
M = 10**16;

F1 = 1091774490000001;      F2 = 2775323470000001;      P = 15000003;
D1 = 1091774490000000;      D2 = 2775323470000000;
EXT = 500000000000000;      STEP = 15000000;            N = 0;

while (P+STEP < 10**16):
    N += 1;
    F1 = (F1+D1+N*EXT)%M;
    F2 = (F2+D2+N*EXT)%M;
    P = P+STEP;
    if (N%10**6 == 0):
        print N, P;
#    print F1, F2, P
print "Almost there"
print F1, F2, P

while (P+2 < 10**16):
    F1 = (F1+F2)%M;
    F2 = (F2+F1)%M;
    P += 2;

print (F1+F2)%M;

#3715972900390626
