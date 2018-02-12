from Numeric import *


def Check(A,B,C,D,E):     # Ordered set;
    if (A == B) or (C == D) or (A == D):
        return 0;
    if (A == C) or (B == C) or (B == D):
        return 0;
    if (A == E) or (B == E) or (C == E) or (D == E):
        return 0;

    if (max(A,B,C,D,E) > 6):
        return 0;

    Sin = (A+B+C+D+E);
    if (Sin % 5 != 0):
        return 0;

    S = 11 + Sin/5;

    O1 = S-(E+A);
    O2 = S-(B+A);
    O3 = S-(B+C);
    O4 = S-(D+C);
    O5 = S-(D+E);

    if (O1*O2*O3*O4*O5*A*B*C*D*E == 3628800):
        print O1,O2,O3,O4,O5,"and",A,B,C,D,E, "with sum", S;
        return 1;
    return 0;
    


Tot = 0;

for a in arange(10):
    for b in arange(a):
        for c in arange(a):
            for d in arange(a):
                for e in arange(a):
                    Tot += Check(a,b,c,d,e);
                

print "Done",Tot
