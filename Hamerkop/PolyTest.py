from Numeric import *
from visual.graph import *

POLYX = [0., 1., 3., 2., 6., 9., 8., 4., 0.];
POLYY = [0., 2., 6., 8.,10., 5., 0., 2., 0.];
NPOLY = 7;

# Takes a point (x0,y0) and checks to see if it's inside polygon defined:
def InPoly(x0,y0,xPol,yPol,nPol):

    VProb = False;

    Poly = gcurve(color = color.red);
    Ball = gcurve(color = color.yellow);
    Poly.plot( pos = (xPol[0],yPol[0]) );
    Ball.plot( pos = (x0-0.02,y0-0.02) );
    Ball.plot( pos = (x0+0.02,y0-0.02) );
    Ball.plot( pos = (x0+0.02,y0+0.02) );
    Ball.plot( pos = (x0-0.02,y0+0.02) );
    Ball.plot( pos = (x0-0.02,y0-0.02) );

    # DRAW POLYGON
    for i in arange(nPol):
#        print (xPol[i], yPol[i])," -> ",(xPol[i+1], yPol[i+1])
        Poly.plot( pos = (xPol[i+1], yPol[i+1]) );\

    # Check if point is on polygon edge:
    for i in arange(nPol):
        x1 = xPol[i];       y1 = yPol[i];
        x2 = xPol[i+1];     y2 = yPol[i+1];

        if (x1 == x2):
            if (x0 == x1):
                VProb = True;
                if ((y0 <= max(y1,y2)) and (y0 >= min(y1,y2))):
                    return 0;
        if (y1 == y2):
            if ((y0 == y1) and (x0 <= max(x1,x2)) and (x0 >= min(x1,x2))):
                return 0;
        if ( (y2-y1)/(x2-x1)*(x0-x1) + y1 == y0 ):
            return 0;

    print "Not on edge"
    if (VProb):
        x0 = x0-1e-6;

    Inter = 0;                      # Number of intersections from a vertical line
    for i in arange(nPol):
        x1 = xPol[i];       y1 = yPol[i];
        x2 = xPol[i+1];     y2 = yPol[i+1];

        if (x0 == x1) and (y0 < y1):
            Inter += 1;
            
        if (x0 < max(x1,x2)) and (x0 > min(x1,x2)):
            yCrit = (y2-y1)/(x2-x1)*(x0-x1)+y1;         # 
            if (y0 > yCrit):
                Inter += 1;

    MIN = 1e6;
    MULT = 1;
    if (Inter%2 == 1):
        print "Inside polygon"
        MULT = -1;

    for i in arange(nPol):
        x1 = xPol[i];       y1 = yPol[i];
        x2 = xPol[i+1];     y2 = yPol[i+1];
        
        S0 = sqrt( (x2-x1)**2 + (y2-y1)**2 );
        S1 = sqrt( (x1-x0)**2 + (y1-y0)**2 );       # Side lengths 
        S2 = sqrt( (x2-x0)**2 + (y2-y0)**2 );
        AREA = sqrt((S0+S1+S2)*(S0-S1+S2)*(S0+S1-S2)*(-S0+S1+S2))/4;
        
        if ( max(S1,S2)**2 > S0**2+min(S1,S2)**2 ):
            Closest = min(S1,S2);
        else:
            Closest = (2*AREA)/S0;

        if (MIN > Closest):
            MIN = Closest;
#            
#        print (x0,y0), (x1,y1), (x2,y2), (S0,S1,S2), AREA, Closest

    return MULT*MIN;



print InPoly(1.,1.73,POLYX, POLYY, NPOLY);

