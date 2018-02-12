from math import *

#def sqrt(k):
#    return k**0.5;

def zeros(k):
    return [0]*k;

# Circles!
# 3a)

def Shadow(W, L, X, Y, R, I, J):
    Easy = W*L-I*J
    
    Dist = sqrt( (X-I)**2 + (Y-J)**2 );     # Distance center to camera
    lenT = sqrt( Dist**2 - R**2 );
    theta = asin( R/Dist );

    phi1 = acos((I-X+0.)/Dist);
    phi2 = acos((I-Y+0.)/Dist);

    p1 = phi1 - theta;
    p2 = phi2 - theta;

    Pie = 0.5*(pi-2*theta)*R*R;
    Extra = R*lenT-Pie;

#    print theta, phi1, phi2, p1, p2

    Easy = W*L-I*J + Extra;
    
    T1 = 0.5*I*I*tan(p1);
    T2 = 0.5*J*J*tan(p2);

#    if ((I >= X+R) and (J >= Y+R)):
#        Ans = W*L-I*J + 0.5*J*J*tan(p2) + 0.5*I*I*tan(p1);
#        return Ans+Extra;
#
#    if ((I >= X+R) and (J <= Y+R)):
#        Ans = (W-I)*L;
        
    K1 = I*tan(p1);
    K2 = J*tan(p2);
"""
    if ((K1 <= J) and (K2 <= I)):
        ax = 0.;
        ay = J-K1;
        bx = I-K2;
        by = 0.;

    if ((K1 > J) and (K2 <= I)):
        S1 = (K1-J)/tan(p1);
        ax = S1;
        ay = 0.;
        bx = J-K2;
        by = 0.;

    if ((K1 <= J) and (K2 > I)):
        S2 = (K2-I)/tan(p2);
        ax = 0.;
        ay = J-K1;
        bx = 0.;
        by = S2;

    if ((K2+I > W) and (K1 < J)):
"""        
        


Tcases = input();
for T in range(1,Tcases+1):
    line = raw_input();
    token=line.split();

    w = int(token[0]);      l = int(token[1]);
    x = int(token[2]);      y = int(token[3]);
    r = int(token[4]);      i = int(token[5]);      j = int(token[6]);

    if (i > x):
        if (j > y):
            Shadow(w, l, x, y, r, i, j);
        else:
            Shadow(w, l, x, l-y, r, i, l-j);
    else:
        if (j > y):
            Shadow(w, l, w-x, y, r, w-i, j);
        else:
            Shadow(w, l, w-x, l-y, w-i, w-j);
    
#    Solve(T, I, R);

