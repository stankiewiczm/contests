from numpy import *

T = 0;
for a in range(1, 1001):
  for b in range(1,a):
    for c in range(1,b):
      d2 = (b*b+c*c-a*a);
      if (d2 >= 0):
        d = int(sqrt(d2+0.1));
	if (d2 == d*d):
	  T += 1;
  print a;

print "done", T
