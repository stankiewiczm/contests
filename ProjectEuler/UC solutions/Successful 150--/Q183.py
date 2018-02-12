from Numeric import *

def GCD(a,b):
    while (b > 0):
        c = b;
        b = a-(a/b)*b;
        a = c;
    return a;


def MaxK(N):
    e = exp(1);
    MAX = log(N);       Best = 1;
    for k in arange (int((N+1)/e)-1,int(N/e)+5):
        TMP = k * log( (N+0.)/k );
        if TMP > MAX:
            MAX = TMP;
            Best = k;
    return Best;


def D(N):
    K = MaxK(N);
    if ((65536*3125*N)%K == 0):
        return -N;
    return N;



TOT = 0;
for i in arange(5,10001):
    TOT += D(i);

print TOT;
