from numpy import *

def Seq(n):
    S = '';
    while (n > 1):
        if (n%3 == 0):
            n /= 3;
            S += 'D';
        if (n%3 == 1) and (n > 1):
            n = (4*n+2)/3;
            S += 'U';
        if (n%3 == 2):
            n = (2*n-1)/3;
            S += 'd';
    return S;


def Search(Str, n0, step):
    for k in range(10):
        if Seq(n0+k*step)[0:len(Str)] == Str:
            print n0+k*step, "  ",k;
            return n0+k*step;

for z in range(10):
    

KEY = "DdDddUUdDD";
Search(KEY[0:5]);
