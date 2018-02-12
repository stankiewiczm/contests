# Blancmange

from numpy import *


def B(x,LIM):
    y = 0;
    for n in range(LIM):
        v = x * 2**n;
        f = v-int(v);
        if f < 0.5:
            y += f/2**n;
        else:
            y += (1-f)/2**n;
    return y

def CircVal(x):
    return 0.5-sqrt(1./16 - (x-0.25)**2)

Steps = 10**6;        dx = 1./Steps;      Area = 0;     depth = 50;
for x in range(Steps):
    xval = x*dx;
    if (xval > 0.078) and (xval < 0.501):
        yval = B(xval,depth);
        if (xval-0.25)**2 + (yval-0.5)**2 <= 1./16:
            Area += yval - CircVal(xval);
        
print (Steps, depth), Area*dx

# (1000000, 50) 0.113160169359
# Rounds off to 0.11316017
