from Numeric import *

def f(X):
    return int(2**(30.403243784 - X*X))*1e-9;

x = -1;

for n in arange(1000):
    x = f(x);
print x+f(x);
