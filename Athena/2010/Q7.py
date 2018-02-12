from numpy import *

Day = 360*60*24;    Tot = 0;
Y = 1925;

while (Y < 2010):
    if (Y%4 == 0):
        Tot += Day*366;
    else:
        Tot += Day*365;
    Y += 1;

Tot -= Day;
Tot -= 6*60*360;
Tot -= 30*360;
Tot += 37*6;

print Tot
