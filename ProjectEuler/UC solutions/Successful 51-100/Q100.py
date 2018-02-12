from Numeric import *

a = long(1);  b = long(1);    N = 1;  P = 0;

while (N+P < 1e12):
    a = a+2*b;
    b = a-b;

    M = a**2+2*b**2;
    P = int(sqrt(float((M*M-1)/8)));

    N = (M+(2*P+1))/2

#    print n,a,b,M,P,N
    print N,P,N+P

