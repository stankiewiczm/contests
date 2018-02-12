from numpy import *

def C(n,r):
    RET = 1;
    for k in range(r):
        RET = (RET*(n-k))/(k+1);
    return RET;

print C(40,20)
