from math import *
from time import *

R = 10**9;          Rs = R/8;       R2 = 2*Rs*Rs;
AREA = (R+1)*(R+1)+R*R;     Good = (R*R) + (R*R)/2;

t0 = time();         k = 1;     T = 2*int(sqrt(R2))+1;

while k*k < R2:
    h = int(sqrt(R2-k*k));
        
    if k*k+h*h >= R2:
        print k,h,k*k+h*h-R2
        h -= 1;
    T += 4*h + 2
    k += 1;

print "There are a total of",T,"lattice points in circle radius",Rs
print "Area of circle is   ",R2*pi;

print Good + T - (2*Rs-1), time()-t0
