from Numeric import *

a = 3.;  b = 2.;    n = 1;  Cnt = 0;

while (n < 1000):
    n = n+1;
    a = a+2*b;
    b = a-b;
    if (b > 1):
        a = a/10.;
        b = b/10.;
    if (a > 1):
        Cnt = Cnt+1;
print Cnt,"/",n;
