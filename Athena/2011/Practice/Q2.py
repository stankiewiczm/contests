from math import *

SOL = 0;
for a in range(101):
    for b in range(101):
        C2 = a**2+b**2;
        C = int(sqrt(C2));
        if C < 101:
            if C**2 == C2:
                SOL += 1;
#                print a,b,C;
                
print SOL
