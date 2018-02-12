from numpy import *

def DigS(n0):
    R = 0;
    while (n0 > 0):
        R += n0%10;
        n0 /= 10;
    return R;

def Eval(seq):
    N = [ seq[-1] ] ;        D = [ 1 ];
    for i in range(len(seq)-2,-1,-1):
        D.append( N[-1] );
        N.append( seq[i]*N[-1] + D[-2] );
    print DigS(N[-1]);

L = [2];
for k in range(1,34):
    L = L+[1,2*k,1];
Eval(L)    
