from numpy import *

def C(n,r):
    R = 1L;
    for k in range(r):
        R = (R*(n-k))/(k+1);
    return R;

def calc(a):
    COUNT = 0L;
    for w in range(0,1001):
        if (1+2*a)**(w)*(1-a)**(1000-w) > 1e9:
            COUNT += C(1000,w);
    return (COUNT+0.)/2**(1000);


Min = 0.1;     Max = 0.2;     Step = 0.001;     best = 0;
k = Min;
while (k < Max):
    if ( calc(k) > best ):
        best = calc(k);
        print k, best;
    k += Step
