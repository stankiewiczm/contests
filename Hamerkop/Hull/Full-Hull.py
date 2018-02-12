from Numeric import *
from math import *

########################################################################
### Pod-program ktory wyrzoca wszystkie (albo wiekszasc) out-lierow, ###
###             Program uzywa sudoku (boxed) algorytm                ###
########################################################################

def Outliers(Data, Grid, DensF):
    Xmin = Data[0][0];      Ymin = Data[0][1];      N = len(Data);
    Xmax = Data[0][0];      Ymax = Data[0][1];      LIMIT = N/(Grid*Grid*DensF)+1;

    for p in Data:
        if p[0] < Xmin:
            Xmin = p[0];
        if p[0] > Xmax:
            Xmax = p[0];
        if p[1] < Ymin:
            Ymin = p[1];
        if p[1] > Ymax:
            Ymax = p[1];

    Bucket = [];    
    for a in arange(Grid):
        Bucket.append(zeros(Grid));

    Xgrid = (Xmax-Xmin)/Grid+1;       Ygrid = (Ymax-Ymin)/Grid+1;

    for p in Data:
        buckX = (p[0]-Xmin)/Xgrid;
        buckY = (p[1]-Ymin)/Ygrid;
        Bucket[buckX][buckY] += 1;

    for k in arange(N-1, -1, -1):
        p = Data[k];
        buckX = (p[0]-Xmin)/Xgrid;
        buckY = (p[1]-Ymin)/Ygrid;
        if (Bucket[buckX][buckY] <= LIMIT):
            REJ.append(Data[k]);
            Data.pop(k);


###############################################################################
### Program ktory znajdzie convex hull (metoda gift-wrapping) z danych punktow
###############################################################################

def Pivot0(DATA):
    Xpiv = DATA[0][0];      Ypiv = DATA[0][1];
    for p in DATA:
        if (p[1] == Ypiv) and (p[0] > Xpiv):
            Xpiv = p[1];
        if (p[1] < Ypiv):
            Xpiv = p[0];
            Ypiv = p[1];
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


def HullGW(Data, Print):                # Print decyduje czy wypisywac hull
    (X0,Y0) = Pivot0(Data);
    HULL = [[X0,Y0]];
            
    XCurr = X0;     YCurr = Y0;     Angle = 0.;
    XNext = 0;      YNext = 0;

    while (XNext != X0) and (YNext != Y0):
        (XNext, YNext,Angle) = FindNext(Data, XCurr, YCurr, Angle);

        XCurr = XNext;              YCurr = YNext;
        HULL.append([XCurr,YCurr]);

    if (Print):
        for a in arange(len(HULL)):
            print HULL[a][0], HULL[a][1];
        print " ";
    return HULL;


###############################################################
### Program zeby sprawdzic czy wyrzucony punkt jest w hullu ###
###############################################################

def InPoly(point, HULL):
    Inter = 0;                      # Number of intersections from a vertical line
    x0 = point[0];          y0 = point[1];          nPol = len(HULL)-1;

    for hp in HULL:
        if (x0 == hp[0]) and (y0 == hp[1]):
            return True;
        
    for i in arange(nPol):
        x1 = HULL[i][0];       y1 = HULL[i][1];
        x2 = HULL[i+1][0];     y2 = HULL[i+1][1];

        if (x0 == x1) and (y0 > y1):
            Inter += 1;
            
        if (x0 < max(x1,x2)) and (x0 > min(x1,x2)):
            yCrit = float((y2-y1))/(x2-x1)*(x0-x1)+y1;         
            if (y0 > yCrit):
                Inter += 1;

    if (Inter%2 == 1):
        return True;
    return False



def Check(RData, Hull):
    for i in arange(len(REJ)-1, -1, -1):
        p = REJ[i];
        if InPoly(p, Hull):
            DATA.append(p);
            REJ.pop(i);
    return;



##################################################
################## MAIN PROGRAM ##################
##################################################

DATA= [map(int ,line.split())for line in file(".\Current\Palab.data")];
REJ = []; 

#HullGW(DATA, True);
Outliers(DATA, 9, 50)
#HullGW(DATA, True)
Outliers(DATA, 9, 10)
HullGW(DATA, True)
Outliers(DATA, 9, 10)
FinHull = HullGW(DATA, True)              # Ostatni hull zapisujemy

Check(REJ, FinHull);

#for p in DATA:
#    print p[0], p[1], p[2],"\n";
#for p in REJ:
#    print p[0], p[1], p[2],"\n";
