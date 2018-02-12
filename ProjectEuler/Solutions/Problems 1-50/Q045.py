from numpy import *

LIM = 10**5;

def CheckP(pn):
    f = 0.5+sqrt(6*pn+0.25);
    return abs(f/3-int(f)/3) < 1e-6;

def PrintP(pn):
    return int(0.5+sqrt(6*pn+0.25))/3;

def GiveH(n):
    return n*(2*n-1);


for n in range(1,LIM):
    H = GiveH(n);
    if CheckP(H):
        print (2*n-1, PrintP(H), n), H
