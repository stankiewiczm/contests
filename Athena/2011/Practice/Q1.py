from numpy import *

Y = 2010;
Day = 5.;

while (Y < 34567):
    Y += 1;
    Day += 1;
    if (Y % 4 == 0):
        Day += 1;
    if (Y % 100 == 0):
        Day -= 1;
    if (Y%400 == 0):
        Day += 1;

print Y, Day%7

print "februarymarchnovember"
