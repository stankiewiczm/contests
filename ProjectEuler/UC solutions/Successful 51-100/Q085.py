from Numeric import *

TAR = 2000000;      D = 5000;

for a in arange(1,600):
    for b in arange(1,a):
        c = a*(a+1)*b*(b+1)/4;
        d = abs(TAR-c);
        if (d < D):
            D = d;
            print a,b,"grid gives",c,"while a*b=",a*b;

print "All done"
        
