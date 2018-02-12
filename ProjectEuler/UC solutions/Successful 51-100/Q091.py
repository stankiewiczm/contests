from Numeric import *


L = 50+1;        TOT = 0;
Xmin = 0;       Ymin = 0;

for x1 in arange(L):
    for y1 in arange(L):
        S1 = (x1**2+y1**2);
        if (x1+y1 > 0):
#            if (x1 == 0):
#                Xmin = 1;
#                Ymin = 0;
#            else:
#                Xmin = 0;
#                Ymin = (y1*x2)/(x1) + 1;
            for x2 in arange(Xmin,L):
                for y2 in arange(Ymin,L):
                    if (y1*x2 != y2*x1):
                        S2 = (x2**2+y2**2);
                        S3 = ((x1-x2)**2 + (y1-y2)**2);
                        if (S1+S2+S3 == 2*max(S1,S2,S3)):
                            TOT += 1;
#                            print (x1,y1),(x2,y2);

print "All done", TOT,TOT/2;

                    
