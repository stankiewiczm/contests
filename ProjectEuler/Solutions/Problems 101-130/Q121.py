from numpy import *

def Bin(N, i):              # Binary index i among N digits
    R = zeros(N, int);
    for k in range(N):
        R[k] = i%2;
        i /= 2;
    return R;

def Prod(arr):
    R = 1;
    for k in arr:
        R *= k;
    return R;


Turns = 15;                  Chance = zeros(Turns);
for k in range(Turns):
    Chance[k] = 1./(k+2);

TOT = 0.;
for i in range(2**Turns):
    Hit = Bin(Turns, i);
    Prob = Chance*Hit + (1-Chance)*(1-Hit);
    if sum(Hit)*2 > Turns:
        TOT += Prod(Prob);

print int(1./TOT)
