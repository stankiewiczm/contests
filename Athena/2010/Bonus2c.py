from numpy import *
from RandomArray import *

def C(n,r,P3):
    C = 1;      k = 1;
    while k < r:
      C = (C*(n+1-k))/(k)%P3;
      k += 1
      if (k%10**6 == 0):
          print k;
    return C;


Tot = 0L;        Sum = 0L;
for line in file("Bonus2.txt"):
    p = int(line);
#    print p, C(p,p/2+1, p**3);
    
    Tot = int (p*random());
#    print p, Tot;
    Sum += Tot*p*p + 2*p;

print Sum

#7514470 45086079


