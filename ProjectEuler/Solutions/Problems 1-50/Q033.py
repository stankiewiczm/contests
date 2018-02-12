from numpy import *

N = 1;      D = 1;
for a in range(1,10):
  for b in range(a+1,10):
    for d in range(1, 10):              # Case 3;
      if (10*a*b == 9*a*d+b*d):
        print 10*a+b,'/',10*b+d;
        N *= a;     D *= d;

print "\n", D/N

