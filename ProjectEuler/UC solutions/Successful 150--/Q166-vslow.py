from Numeric import *

LM = 10;


def Complete(A1,A2,A3,A4,B1,B2,B3,C1,C3):
    SUM = A1+A2+A3+A4;
    B4 = SUM-(B1+B2+B3);
    D1 = SUM-(A1+B1+C1);
    C2 = SUM-(A4+B3+D1);
    D2 = SUM-(A2+B2+C2);

    C4 = SUM-C1-C2-C3;
    D3 = SUM-A3-B3-C3;
    D4 = SUM-A4-B4-C4;

    if max(B4,D1,C2,D2,D3,C4,D4) > 9 or min(B4,D1,C2,D2,D3,C4,D4) < 0:
        return 0;

    if (A1+A2+A3+A4 == B1+B2+B3+B4 == C1+C2+C3+C4 == D1+D2+D3+D4):
        if (A1+B1+C1+D1 == A2+B2+C2+D2 == A3+B3+C3+D3 == A4+B4+C4+D4):
            if (A1+B2+C3+D4 == A4+B3+C2+D1 == SUM):
                return 1;
    return 0;

    if ((C1+C2+D1+D2) == (A3+A4+B3+B4)):
        SUM = A1+A2+B1+B2;
        C3 = 3*SUM - (2*A1+2*A2+A3+B1+B2+B3+C1+C2);
        if (C3 % 2 == 1):
            return 0;
        else:
            C3 = C3/2;
        C4 = SUM-(C1+C2+C3);
        D3 = SUM-(A3+B3+C3);
        D4 = SUM-(A4+B4+C4);

        if max(C3,C4,D3,D4) > 9 or min(C3,C4,D3,D4) < 0:
            return 0;

        D4 = SUM-A1-B2-C3;
        D3 = SUM-D1-D2-D4;
        C4 = SUM-C1-C2-C3;

        if (A3+B3+C3+D4 == A4+B4+C4+D4 == SUM):
            return 1;
        
#        if (A1+B2+C3+D4 == SUM):
#            if (C1+C2+C3+C4 == D1+D2+D3+D4 == A3+B3+C3+D3 == A4+B4+C4+D4 == SUM):
#                if (A1+B2+C3+D4 == D1+C2+B3+A4 == A1+A2+A3+A4 == A1+B1+C1+D1 == SUM):
#                    print "Poss solution",[[A1,A2,A3,A4],[B1,B2,B3,B4],[C1,C2,C3,C4],[D1,D2,D3,D4]];
#                    return 1;
#            else:
#                print "coocky", A1, A2, A3, A4
#                return 0
#        else:
#            return 0;
    return 0;


NUM = 0;
for a1 in arange(LM/2):
    for a2 in arange(LM):
        for a3 in arange(LM):
            for a4 in arange(LM):
#                S = a1+a2+a3+a4;
                for b1 in arange(LM):
                    for b2 in arange(LM):
                        for b3 in arange(LM):
                            for c1 in arange(LM):
                                for c3 in arange(LM):
                                    NUM += Complete(a1,a2,a3,a4,b1,b2,b3,c1,c3);
        print a1,a2, NUM;

print NUM*2;
print "Done"
