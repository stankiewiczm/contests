from numpy import *

def IsSq(n):
    return ( int(sqrt(n))**2-n == 0);

def Solve(M, LIM):
  N = 0;
  for a in range(1,M+1):
    for bc in range(2,2*a+1):
      if IsSq(a**2+bc**2):
        if (bc <= a+1):
          N += (bc)/2;
        else:
          N += (2*(a+1)-bc)/2;
        if N > LIM:
          return a;
  return 0;

print Solve(2000,10**6);

  
