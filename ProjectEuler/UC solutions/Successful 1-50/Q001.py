from Numeric import *

S = 0;
for i in arange(1000):
    if ((i%3 ==0) | (i%5==0)):
        S = S+i;
print S;
    
