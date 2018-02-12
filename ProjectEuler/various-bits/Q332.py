from numpy import *

#r = 14;
def Count(r):
    R2 = r**2;
    Ret = 0;
    for a in range(-r,r+1):
        for b in range(-r,r+1):
            C2 = R2-b**2-a**2;
            if int(sqrt(C2))**2 == C2:
                c = int(sqrt(C2));
                Ret += 2;
                if (C2 == 0):
                    Ret -= 1;
#                print (a,b,c);
#                print (a,b,-c);
    return Ret;

for i in range(1,51):
    print i, Count(i);
