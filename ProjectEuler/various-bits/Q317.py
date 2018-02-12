from numpy import *
import time

T0 = time.time();
g = 9.81;           V = 20.;
Rrange = 50000;     dR = 100./Rrange;
BestY = zeros(Rrange);
BestY[0] = 100+V*V/(2*g);               # Maximal height will be v^2/2g
angle  = 90;
Start = 1;          End = 1;        New = 0;
while (angle > 0):
    angle -= 0.001
    theta = angle*pi/180;       # radians
    vx = V * cos(theta);
    vy = V * sin(theta);
                                            # s = ut - 1/2 a t^2
    Tmax = (vy + sqrt(vy**2 + 200*g))/g     # Solving for time at impact

    dT = dR/vx;
    Ttest = dT;
    i = Start-1;
    New = 0;

    while ((New == 0) or (End != i)) and Ttest < Tmax:
        i += 1;
        Rtest = i*dR;               # Test radius
        Ttest = i*dT;               # time
        if Ttest < Tmax:
            Yval = 100 + vy*Ttest - g/2*Ttest**2;
            if Yval > BestY[i]:                     # New high point
                BestY[i] = Yval;
                if New == 0:
                    Start = i;                      # First high point
                New  += 1;
            else:
                if New > 0:
                    End = i;                        # Not high any more

print time.time()-T0

Vol = 0;
x = 0;
while BestY[x] != 0:
  V = (BestY[x]-BestY[x+1])*pi*dR**2 * (2*x*x+2*x+1)/2.;
  Vol += V;
  x += 1;

print Vol
# 1856532.84602
# 1856532.8455 is the answer...
# pi (v0^3+2g v0 y0)^2/(4g^3)
