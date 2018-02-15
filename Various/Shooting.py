## u'' == L u
## u(x+h)-2u(x)+u(x-h) = L u h^2
from math import *

def Shoot(L):
    u = [0., 1.];
    h = 1e-4;
    for i in range(9999):
        u.append( 2*u[-1]-u[-2]+L*u[-1]*h*h );
    return u[-1]


def f(x):
    return x*sin(x)*exp(-2*x*x);

def f2(y):
    return sin(sqrt(y))*exp(-2*y)/2.;

print sum( f(i/1000.) for i in range(10000))/1000;
print sum( f2(i/1000.) for i in range(10000))/1000;
