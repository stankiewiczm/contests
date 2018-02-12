from numpy import *

S = 18*101;               # (a,0,a),   (0,a,0)   - (0,0,0);

# n = 2;

def Check(A,B,C):
    RET = 0;
    if ((A*B) == 0) and (A+B == C):
        return 1;
    if (A*A+B*B==C*C):
        return 1;
    return 0;

    
S = 0;

for a in range(0,101):
    print a, S;
    for b in range(0,101):
        for c in range(0,101):
            S += Check(a,b,c);

print S
