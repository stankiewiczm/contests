from Numeric import *
from math import *
from visual.graph import *
from matplotlib import *

Data=[map(int ,line.split())for line in file("gfs_drf.evp")]

dt = gcurve(color = color.red);
hl = gcurve(color = color.blue);

#############################################
######### First, find a pivot point #########
#############################################

def Pivot0(DATA):
    Xpiv = DATA[0][0];      Ypiv = DATA[0][1];
    for p in DATA:
        if (p[1] == Ypiv) and (p[0] > Xpiv):
            Xpiv = p[1];
        if (p[1] < Ypiv):
            Xpiv = p[0];
            Ypiv = p[1];
        dt.plot(pos=(p[0],p[1]));
    return (Xpiv, Ypiv);


def FindNext(DATA, x0, y0, angle):
    Xn = 0;     Yn = 0;
    MinAngle = angle+2*pi;
    
    for pnt in arange(len(DATA)):
        px = DATA[pnt][0];        py = DATA[pnt][1];

        if ((px,py) != (x0,y0)):
            if (px == x0):
                if (py > y0):
                    AnglePQ = pi/2;
                if (py < y0):
                    AnglePQ = 3*pi/2;
            else:
                AnglePQ = atan( float((py-y0))/(px-x0) );
                if (AnglePQ < 0):
                    AnglePQ += pi;
                if (py < y0):
                    AnglePQ += pi;

        if (AnglePQ == MinAngle):
            if ( (px-x0)**2+(py-y0)**2 > (Xn-x0)**2+(Yn-y0)**2 ):
                Xn = px;
                Yn = py;
    
        if ((AnglePQ < MinAngle) and (AnglePQ > angle)):
            MinAngle = AnglePQ;
            Xn = px;
            Yn = py;

    return (Xn,Yn, MinAngle)


#############################################
############    MAIN PROGRAM   ##############
#############################################


(X0,Y0) = Pivot0(Data);
print X0,Y0;
hl.plot(pos = (X0,Y0));
        
XCurr = X0;     YCurr = Y0;     Angle = 0.;
XNext = 0;      YNext = 0;

while (XNext != X0) and (YNext != Y0):
    (XNext, YNext,Angle) = FindNext(Data, XCurr, YCurr, Angle);

    XCurr = XNext;      YCurr = YNext;
    print XCurr, YCurr;
    hl.plot(pos = (XCurr,YCurr));

