from random import *

T = 20;
print T;
for n in range(1,T+1):
#  print n;
  print 100,9900;
  for k in range(1,101):
    for l in range(1,101):
      if (k != l):
	Del = int(random()*200000)+1;
	Time = int(random()*1000)+2;
        print k, l, int(random()*1000)+1,Del, Del+Time;

