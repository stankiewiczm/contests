from numpy import *

def Check(p):
    print p,
    mx = int(p**0.5)+1;
    if (p%2 == 0):
        print "NOPE"
        return;
    n = 3;
    while n < mx:
        if p%n == 0:
            print "NOPE....."
            return;
        n += 2;
    print "OK",;
    return;
    

Tot = 0L;        Sum = 0L;
for line in file("Bonus2.txt"):
    p = int(line);

    Check(p);
    Check(p/2+1);
    print " ";



#7514470 45086079


