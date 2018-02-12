from Numeric import *
import time

S = [290797L];      T = [];     LINE = [];      t0 = time.time();

for k in range(20000):
    S.append((S[-1]**2)%50515093);
    T.append(int(S[-1]%500));
for k in range(5000):
    LINE.append( (T[4*k], T[4*k+1], T[4*k+2], T[4*k+3]) );

###########################################################

def Inter(a, b):
    (x1,y1,x2,y2) = LINE[a];
    (X1,Y1,X2,Y2) = LINE[b];

    # Parallel lines
    if (y2-y1)*(X2-X1) == (Y2-Y1)*(x2-x1):
        return 0;

    # Non-overlapping domains or co-domains
    if (max(x1,x2) < min(X1,X2)) or (min(x1,x2) > max(X1,X2)):
        return 0;
    if (max(y1,y2) < min(Y1,Y2)) or (min(y1,y2) > max(Y1,Y2)):
        return 0;


    if (x1 == x2):    # Vertical line
        Yint = float(Y2*(X2-x1) + Y1*(X1-x1))/(X2-X1);
        if (Yint < max(y1, y2)):
            if (Yint > min(y1,y2)):
                return 1;
        return 0;


    
        

    return 0;


ANS = 0;            # There is one set of parallel lines that are same line ?

for a in range(1,5000):
#    if LINE[a][0] == LINE[a][2]:
#        print LINE[a]
    for b in range(a):
        ANS += Inter(a,b);

print ANS, time.time()-t0;

