from Numeric import *

S = 0;
for a in arange(3,1001):
    if (a%2 == 1):
        S = S + a*a-a;
    else:
        S = S + (a*a-2*a);
print S;
