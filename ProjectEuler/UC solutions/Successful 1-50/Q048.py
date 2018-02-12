from Numeric import *;

a = long(0);    b = long(0);    Tot = long(0);      LIM = long(10000000000);


for a in arange(1,1000):
#    Dig[0] = 1;
    Curr = long(1);
    for b in arange(a):
        Curr = (Curr*a)%LIM;
    Tot = (Tot+Curr)%LIM;

print Tot;
