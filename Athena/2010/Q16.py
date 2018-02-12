from numpy import *

#i=0-5000 [111511179^((22^(5*i))*310^(5*10^i))]

N = 111511179;      P = 1;      N0 = 111511179;     M = 10**8

while (P != 100000):
    P += 1;
    N = (N*N0)%M;

print P
    
# Need to find exponent mod 5000000 = 5 million
# Exponent is 22^(5i) * 310^(5*10^i)
# Exponent is multiple of 5 million except for the first one.

# 22^0*310**5 == 100000 mod 5 million;

print 5000+N;

# 62005001
