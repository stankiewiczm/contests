from Numeric import *

for m in arange(2,10000):
    for n  in arange(1,m):
        a = m*m-n*n;
        b = 2*m*n
        c = m*m+n*n;

        if (int(sqrt(c))**2 == c):
            if (a*b)%84 != 0:
                print (m,n),"   ->   ",(a,b,c),

print "All perfect squares are super-pefect too, so ",0    
