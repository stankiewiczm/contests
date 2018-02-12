from numpy import *

N = 50;      S = 0;

for x1 in range(1,N+1):
  for x2 in range(N+1):
    L1 = x1*x1+x2*x2;
    for y1 in range(N+1):
      y2m = (y1*x2/x1)+1;
      for y2 in range(y2m, N+1):
        L2 = y1**2+y2**2;
        L3 = (y1-x1)**2+(y2-x2)**2;
        if (L1+L2+L3 == 2*max(L1,L2,L3)):
          S += 1;

print S
