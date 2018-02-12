from numpy import *

def C(n,r):
    R = 1L;
    for k in range(r):
        R = (R*(n-k))/(k+1);
    return R;

EXT = 100+50*99;

print C( EXT+99, 99);
