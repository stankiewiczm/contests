# Google code jam round 2, problem B

from numpy import *

FILE = open("B-sample.in","r");

def Solve(DATA):

   return;


T = int(FILE.readline());
for k in range(T):          # Each of the N cases:
   print "Case #%d:" %(k+1),
   [D,I,M,N] = map( int, FILE.readline().split() );
   DATA = map(int, FILE.readline().split());
   print Solve(DATA);
