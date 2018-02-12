from Numeric import *

Sevs = zeros(25000);
for i in arange(1,25000):
    Sevs[i] = i/7+i/49+i/343+i/2401+i/(7**5);


def Cd7(n,r):
    N = Sevs[n]-Sevs[n-r]-Sevs[r];
    return (N == 0);

def Guess(n):
    ss = zeros(11);     MX = 0;     MXi = 0;
    for i in arange(11):
        ss[i] = (n/(7**i))%(7);
        if (ss[i] > 0):
            MX = 7**i;      # highest power of 7
            MXi = i;        # indexed

    R = 1;
    for i in arange(11):
        R *= ss[i]+1;
    return R


def SumToN(N):
    ss = zeros(11);     MX = 0;     MXi = 0;
    for i in arange(11):
        ss[i] = (N/(7**i))%(7);
        if (ss[i] > 0):
            MX = 7**i;      # highest power of 7
            MXi = i;        # indexed

    print ss,;
    R = 0;
    for i in arange(11):
        H = 1;
        for h in arange(i+1,11):
            H *= (ss[h]+1);
        for j in arange(ss[i]):
            R += (j+1)*28**i*H;
    return R

print SumToN(10**9);
