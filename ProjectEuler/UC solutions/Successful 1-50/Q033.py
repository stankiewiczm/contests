from Numeric import *

# Case 1: ab/bc = a/c

Pr = 1.;
for a in arange(1,10):
    for b in arange(1,10):
        if (((10*a*b % (9*a+b)) == 0) and (a != b)):
            c = 10*a*b / (9*a+b);
            Pr = Pr*a/c;
            print 10*a+b,"/",10*b+c,"=",a,"/",c,Pr;


print "Product is 1 /",1/Pr;
