from Numeric import *

def C(n,r):
    CNR = 1;
    for i in arange(r):
        CNR = (CNR*(n-i))/(i+1);
    return CNR;


# Straight rectangles: C(L+1,2)*C(H+1,2)
