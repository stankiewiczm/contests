from Numeric import *

Fact = [1,1,2,6,24,120,720,5040,40320,362880];  ANS = 0;

def Mix(P):
    Ss = 0;
    for a in str(P):
        Ss = Ss + Fact[int(a)];
    return Ss;


for i in arange(1000000):
    if (Mix(i) == i):
        ANS = ANS+i;
        print i;
print "Done, answer being",ANS-3;
