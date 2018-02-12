from numpy import *

for a in range(3,300):
    for b in range(a,500):
        c = int(sqrt(a*a+b*b))
        if (c*c == a*a+b*b) and (a+b+c == 1000):
            print (a,b,c), a*b*c;
