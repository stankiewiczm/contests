from Numeric import *

# (a,b) + t(u,v) -> t = -2*(au+bv)/(u*u+v*v)

def Laser(x,y,u,v):
    t = -2*(4*x*u+y*v)/(4*u*u+v*v);
#    print t;
    X = x+t*u;
    Y = y+t*v;

    N = Y/(4*X);        # Normal to the eliptical plane;

    n1 = Y;     n2 = 4*X;
    Frc = 2*(n1*n2)/(n1**2-n2**2);

    Beta = sin(arctan(Frc));
    Alph = cos(arctan(Frc));

    U = Alph*u - Beta*v;
    V = -Beta*u - Alph*v;

    LX.append(X);
    LY.append(Y);
    LU.append(U);
    LV.append(V);


x0 = 0.00710731694997;      y0 = 9.9999898972;
u0 = 1.4;                   v0 = -19.7; 

LX = [x0];      LY = [y0];      LU = [u0];      LV = [v0];

i = 0;
while (i < 1000):
#    print (LX[i], LY[i]), "with next direction", (LU[i],LV[i]);
    Laser(LX[i], LY[i], LU[i], LV[i]);
    i += 1;
    if (abs(LX[i]) < 0.01) and (LY[i] > 0):
        break;
print (LX[i], LY[i]), "and OUT, after",i-1,"bounces."

