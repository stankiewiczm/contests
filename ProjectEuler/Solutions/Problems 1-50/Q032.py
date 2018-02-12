from numpy import *

PANS = [];

def CheckPan(S):
    Dig = zeros(10, int);       
    if len(S) != 9:
        return False;
    for c in S:
        Dig[ord(c)-48] += 1;
    if max(Dig) == 1:
        if Dig[0] == 0:
            return True;
    return False;


for n1 in range(1,100):
    for n2 in range(1000/n1, 10000/n1):
        if CheckPan( str(n1)+str(n2)+str(n1*n2)):
            if (n1*n2) not in PANS:
                PANS.append(n1*n2);
#            print n1, n2, n1*n2;

print sum(PANS)
