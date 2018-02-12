# Google code jam round 2, problem B

from numpy import *

FILE = open("D-small2.in","r");

#def In(A,B,C,D);

def Solve(g1, g2, b):
   gg = sqrt( (g1[0]-g2[0])**2 + (g1[1]-g2[1])**2 );
   r1 = sqrt( (g1[0]-b[0])**2 + (g1[1]-b[1])**2);
   r2 = sqrt( (g2[0]-b[0])**2 + (g2[1]-b[1])**2);

   s = (r1+r2+gg)/2;
   area = sqrt( s*(s-gg)*(s-r1)*(s-r2) );
   h = 2 * area / gg;
#   print (r1, r2), h
   
   if ((r1 <= gg) and (r2 <= gg)):
      
      phi1 = arccos(1-2*h*h/(r1*r1));
      phi2 = arccos(1-2*h*h/(r2*r2));
      RET = (r1*r1*(phi1-sin(phi1)) + r2*r2*(phi2-sin(phi2)))/2;
      if (RET < 1e-4):
         return 0.0
#         print "SHIT"
      return RET;

#   print "other case"

   psi1 = arcsin(h/r1);
   psi2 = arcsin(h/r2);
   if (h > r1):
      psi1 = pi/2;
   if (h > r2):
      psi2 = pi/2;
      
   if (r1 > r2):
      return (r2**2*(pi-psi2) + 0.5*r2**2*sin(2*psi2) + 0.5*r1**2*(2*psi1 -sin(2*psi1)));
   else:
      return (r1**2*(pi-psi1) + 0.5*r1**2*sin(2*psi1) + 0.5*r2**2*(2*psi2 -sin(2*psi2)));


T = int(FILE.readline());
for k in range(T):          # Each of the N cases:
   print "Case #%d:" %(k+1),
   [N,M] = map(int, FILE.readline().split());
   if (N == 1):
      print 0;
   if (N == 2):
      G1 = map (int, FILE.readline().split());
      G2 = map (int, FILE.readline().split());
      for m in range(M):
         Case = map (int, FILE.readline().split());
         print "%2.6f " %(Solve(G1, G2, Case)),;
#             print "Case #%d:" % (t+1),
      print;
