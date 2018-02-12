# Google code jam round 2, problem A

from numpy import *

FILE = open("A-small.in","r");

def Hleft(D, size):
   Sym = size;
   while (Sym > 1):
      Valid = True;
      for r in range(Sym):
         for c in range(r):
            if D[size-Sym+r][c] != D[size-Sym+r][2*r-c-1]:
               Valid = False;
               break;
      if (Valid):
         return Sym;
      Sym -= 1;
   return 1;

def Hright(D, size):
   Sym = size;
   while (Sym > 1):
      Valid = True;
      for r in range(Sym):
         for c in range(r):
            row = size-Sym+r;
            ROW = 2*(size-Sym)-1;
            if D[row][ROW-c] != D[row][ROW-(2*r-c-1)]:
               Valid = False;
               break;
      if (Valid):
         return Sym;
      Sym -= 1;
   return 1;


def Vtop(D, size):
   Sym = size;
   while (Sym > 1):
      Valid = True;
      for r in range(Sym):
         for c in range(r):
#            print (r,c), (2*(Sym-1)-r,c);
            if D[r][c] != D[2*Sym-2-r][c]:
               Valid = False;
               break;
      if (Valid):
         return Sym;
      Sym -= 1;
   return 1;


def Vbot(D, size):
   Sym = size;
   while (Sym > 1):
      Valid = True;
      for r in range(Sym):
         for c in range(r):
#            print (r,c), (2*(Sym-1)-r,c);
            if D[2*size-1-r][c] != D[2*size-1-(2*Sym-2-r)][c]:
               Valid = False;
               break;
      if (Valid):
         return Sym;
      Sym -= 1;
   return 1;


T = int(FILE.readline());
for q in range(T):          # Each of the N cases:
   print "Case #%d:" %(q+1),
   k = int(FILE.readline());
   D = [];
   for l in range(2*k-1):
      D.append( map(int, FILE.readline().split()));
   print Hleft(D,k); 
   Hoff = k - max( Hright(D,k));
   Voff = k - max( Vtop(D,k), Vbot(D,k));

   print (k+Hoff+Voff)**2-k**2

#   print Vtop(D, k);

#   print D;
