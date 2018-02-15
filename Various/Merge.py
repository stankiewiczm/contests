from time import *
import random as r
from numpy import *


def Merge(Data):
   n = len(Data);
   if n == 1:
      return Data;
   m = n/2;
   A = Merge(Data[0:m]);     n1 = m;
   B = Merge(Data[m:n]);     n2 = n-m;
   Ret = zeros(n);
   i1 = 0;     i2 = 0;
   while (n1 > i1) and (n2 > i2):
      if A[i1] < B[i2]:
         Ret[i1+i2] = A[i1];
         i1 += 1;
      else:
         Ret[i1+i2] = B[i2];
         i2 += 1;
   # One of the lists is now empty
   while (i1 < n1):
      Ret[i1+i2] = A[i1];
      i1 += 1;
   while (i2 < n2):
      Ret[i1+i2] = B[i2];
      i2 += 1;
   return Ret;
   
   
   
A = zeros(20, int).reshape(5,2,2)      # 3D array
N = 100;
L = [];

for i in range(N):
   L += [r.random()];                  # As opposed to randint(low, high);

print L, Merge(L)
