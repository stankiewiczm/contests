from numpy import *

def IsPalin(s):
    s2 = "";
    for c in range(len(s)-1, -1, -1):
        s2 += s[c];
    for c in range(len(s)):
        if s[c] != s2[c]:
            return False
    return True;


def Bin(k):
    RevBin = "";
    while (k > 0):
        RevBin += str(k%2);
        k /= 2;
    return RevBin

Total = 0;
for k in range(1,1000000):
    if IsPalin(str(k)):
        if IsPalin(Bin(k)):
            Total += k;
#            print k, Bin(k);

print "\n",Total;
    
