from random import *
#from numpy import *

def Test(height, bests):
   
   for i in range(N-1):
      best = [-1,0];
      besti = 0;
      for j in range(i+1,N):
         dH = height[j]-height[i];
         dX = j-i;
         if dH*best[1] > dX*best[0]:
#            
#         if dH/float(dX) > best:
#            best = dH/float(dX);
            best = [dH, dX];
            besti = j;

      if besti != bests[i]-1:
         return False;
   return True;



def Rand(N):
   R = [0]*N
   for i in range(N):
      R[i] = int(10000*random())
   return R;      
         
            
T = int(raw_input());
for i in range(T):         
   print "Case #%d:" % (i+1),;
   N = int(raw_input());
   xi = map(int, raw_input().split());

   count = 0;
   done = False;
   while (count < 5e5) and not done:
      guess = Rand(N);
      done = Test( guess, xi )
      count += 1
   if done:
      for e in guess:
         print e,
      print
#      print guess
   else:
      print "Impossible"
#   print done
