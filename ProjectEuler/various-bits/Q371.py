from numpy import *
from random import *

def Try():
    n = 0;
    Hit = [0]*1001;
    while True:
        t = int(random()*1000);
        n += 1;
        if Hit[1000-t] == 1:
            return n;
        Hit[t] = 1;


N = 10**5;
S = 0;
for k in range(N):
    S += Try();
print S/(N+0.)
