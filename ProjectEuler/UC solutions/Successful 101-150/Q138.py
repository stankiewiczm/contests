from Numeric import *

a = long(3);  b = long(1);    N = 1;  P = 0;    TOT = long(-1);

while (a < 1e16):
    if (a%2 == b%2 == 0):
        if (a**2 < 5*b**2):
            C   = b/2;
            B   = 4*((a/2+4)/10);
            print "Base",B,"Iso side",C, "Height",sqrt(float(C*C-B*B/4));
            TOT = TOT+C;

    a = (a+5*b)/2;
    b = a-2*b;

print TOT;
