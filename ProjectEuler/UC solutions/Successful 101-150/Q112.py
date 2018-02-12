from Numeric import *

def IsB(N0):
    if (N0 < 10):
        return False;

    D = list();    N = N0;          #D[0] is last digit
    while (N > 0):
        D.append(N%10);
        N = N/10;

    Del = D[len(D)-1]-D[0];         # Difference: First-last;
    
    if (Del == 0):
        return (max(D) != min(D));

    if (Del > 0):                   # Last number is lower
        for i in arange(len(D)-1):
            if (D[i+1] < D[i]):
                return True;
        return False;

    if (Del < 0):                   
        for i in arange(len(D)-1):  # Last number is higher
            if (D[i+1] > D[i]):
                return True;
        return False;



TOT = 0;
for i in arange(1,2000001):
    if (IsB(i)):
        TOT += 1;
    if (TOT*2 == i):
        print "50% at ",TOT,"/",i;
    if (TOT*100 == i*99):
        print "99% at ",TOT,"/",i;

print "Finished on ",TOT,"/",i;
