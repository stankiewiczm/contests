from numpy import *

N9 = 2011;
Sum = 0;

for p in range(1,1010):
  for q in range(p+1, 2012-p):
    Sq = 2*sqrt(p*q);
    if (p+q > Sq) and (p+q < Sq+1):
      Sum += 1-int( N9/log10(p+q-Sq))
