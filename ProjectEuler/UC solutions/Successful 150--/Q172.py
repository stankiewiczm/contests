from Numeric import *

def C(n,r):
    R = 1;
    for i in arange(r):
        R = (R*(n-i))/(i+1);
    return R;

TOT = 0;        ARNG = 0;
for a0 in arange(4):
    for a1 in arange(4):
        for a2 in arange(4):
            for a3 in arange(4):
                for a4 in arange(4):
                    for a5 in arange(4):
                        for a6 in arange(4):
                            for a7 in arange(4):
                                for a8 in arange(4):
                                    a9 = 18-a0-a1-a2-a3-a4-a5-a6-a7-a8;
                                    if (3 >= a9 >= 0):
                                        Sq = [a1,a2,a3,a4,a5,a6,a7,a8,a9];
                                        Tm = C(17,a0);
                                        Free = 18-a0;
                                        for k in arange(9):
                                            Tm = Tm*C(Free,Sq[k]);
                                            Free = Free-Sq[k];
                                        if (Free != 0):
                                            print "Shit"
                                        TOT += Tm;
                                        ARNG += 1;
        print [a0,a1]

print TOT, ARNG;
