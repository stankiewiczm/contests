from numpy import *

Target = 2*10**6;       Bmax = int((4*Target)**0.25);       Best = [0,0,0];

for b in range(Bmax, 0, -1):
    A2 = 4*Target/(b*(b+1));
    A1 = int(sqrt(A2));
    for a in range(A1-1, A1+2):
        Nab = (a*(a+1)*b*(b+1))/4;
        if abs(Nab - Target) < abs(Best[0]-Target):
            Best = [Nab, a, b];

print Best[1]*Best[2], '   ',Best;
