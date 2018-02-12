from numpy import *
from random import *

MPB = [0]*40;       Steps = 10**6;

def D(n):
    return int(n*random())+1;

def Move():
    T = 0;      Doub = 0;
    while (Doub != 3):
        D1 = D(4);      D2 = D(4);
        T += D1+D2;
        if (D1 == D2):
            Doub += 1;
        else:
            return T;
    return (50-Pos);


Pos = 0;
for k in range(Steps):
    Pos = (Pos + Move())%40;
    if Pos == 30:
        Pos = 10;
    if (Pos in [2,13,33]):
        R = D(8);
        if R == 1:  Pos = 0;
        if R == 2:  Pos = 10;
    if (Pos in [7, 22, 36]):
        R = D(16);
        if R == 1:  Pos = 0;
        if R == 2:  Pos = 10;
        if R == 3:  Pos = 11;
        if R == 4:  Pos = 24;
        if R == 5:  Pos = 39;
        if R == 6:  Pos = 5;
        if R in [7,8]:
            Pos += (5-Pos)%10;
        if R == 9:  Pos = 12;
        if R == 10: Pos = Pos-3

    Pos = Pos%40;
    MPB[Pos] += 1;

for k in range(3):
  i = MPB.index(max(MPB));
  print i, MPB[i];
  MPB[i] = 0;
