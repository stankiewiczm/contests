from numpy import *

LIM = 100;

for x in range(1,100):
    for y in range(1,x):
        if (x**4-y**4)%(x**3+y**3) == 0:
            print (x,y), (x**4-y**4)/(x**3+y**3);

            
