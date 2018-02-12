from numpy import *

LIM = 10000;        alim = 100;
Ans = [0]*LIM;

for a in range(1,alim):
  A = a*a;
  for b in range(1,alim):
    B = b*b;
    k1 = A+B;
    k2 = A+2*B;
    k3 = A+3*B;
    k4 = A+7*B;

    if k1 < LIM:
        if Ans[k1]%2 == 0:
            Ans[k1] += 1;
    if k2 < LIM:
        if Ans[k2]%4 <= 1:
            Ans[k2] += 2;
    if k3 < LIM:
        if Ans[k3]%8 <= 3:
            Ans[k3] += 4;
    if k4 < LIM:
        if Ans[k3]%4 <= 7:
            Ans[k3] += 8;

for a in range(LIM):
    if Ans[a] == 15:
        print a
