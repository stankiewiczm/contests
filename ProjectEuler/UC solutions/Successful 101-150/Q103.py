from Numeric import *

SS = [20,31,38,39,40,42,45];        CURR = sum(SS);


def Check(Seq,CASE):
    TST = zeros(300);
    OTH = zeros(300);
    for a0 in arange(2):
        for a1 in arange(2):
            for a2 in arange(2):
                for a3 in arange(2):
                    for a4 in arange(2):
                        for a5 in arange(2):
                            for a6 in arange(2):
                                S  = a0*Seq[0] + a1*Seq[1] + a2*Seq[2] + a3*Seq[3];
                                S += a4*Seq[4] + a5*Seq[5] + a6*Seq[6];
                                TST[S] += 1;
                                OTH[S] = a0+a1+a2+a3+a4+a5+a6;
    if (max(TST) >= 2):
        return False;

    if (CASE == 0):
        return True;

    Mx = 0;
    print "trying",Seq;
    for i in arange(len(OTH)):
        if (OTH[i] >= 1) and (OTH[i] < Mx):
            return False;
        if OTH[i] > Mx:
            Mx = OTH[i];
    return True;
    


for G in arange(50,42,-1):
    for F in arange(35,G):
        for E in arange(35,F):
            if (E+F+G < 130):
                for D in arange(35,E):
                    for C in arange(32,D):
                        for B in arange(28,C):
                            Amin = max((G+F+E)-(B+C+D)+1,15);
                            Amax = min(260-(B+C+D+E+F+G),B);
                            for A in arange(Amin,B):
                                if ( Check([A,B,C,D,E,F,G], 1) ):
                                    print A,B,C,D,E,F,G,"sum",A+B+C+D+E+F+G;
    print "done",G;
