from Numeric import *


def IsSq(N0):
    return(int(sqrt(N0))**2 == N0);


for a in arange(920,930):
    A = a*a;
    for b in arange(2,a):
        B = b*b;
        if (A-B)%2 == 0:
            y = (A-B)/2;
            x = (A+B)/2;

            cLim = int(sqrt(y))+1;
            for c in arange(1,cLim):
                z = y-c*c;              # So x-y, x+y, y-z are ok;
                if (z > 0):
                    if (IsSq(y+z)):
                        if (IsSq(x+z)):
                            print "Almost",a,b,"   ",x,y,z
                            if (IsSq(x-z)):
                                print x,y,z,"  :  ",x+y,x-y,y-z,y+z,x-z,x+z," and sum ",x+y+z;

#                
#                    z = (y-C)/2;
#                if IsSq(x-z):
#                    if IsSq(y-z):
#                        if IsSq(x+z):
#                            if IsSq(z+y):
#                                print x,y,z;

print "All done"            

#for a in arange(1,1000):
#    b = 0;
#    
#    for b in arange(1,a):
#        if IsSq(a+b):
#            if IsSq(a-b):
#                print a,b;
