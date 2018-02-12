def Try(N, hmax):
   Ans = [0]*N;
   Ans[N-1] = 10**4;
   Ans[N-2] = 10**4;
   for i in range(N-3, -1, -1):
      Hmin = Ans[i+1]/2.;
      Hmax = Ans[i+1]*2.;
      highest = hmax[i]
      for j in range(i+1, N):
         if j < highest:
            Hmin = max( Hmin, Ans[highest] - (Ans[highest]-Ans[j])*(highest-i)/(highest-j+0.) );
         if j > highest:
            tmp = Ans[highest] - (Ans[highest]-Ans[j])*(highest-i)/(highest-j+0.)
            Hmax = min( Hmax, tmp );
#      print i+1, Hmin, Hmax;

      Ans[i] = int(Hmax);
      if Ans[i] < Hmin:
         Ans[i] = 0;

      print i+1, highest, Ans

   if min(Ans) <= 0 or max(Ans) >= 1e9:
      print "Impossible"
   else:
      for e in Ans:
         print e,
      print 
   



T = int(raw_input());
for i in range(T):
   print "Case #%d:" % (i+1),;
   N = int(raw_input());
   xi = map(int, raw_input().split());

   Guess = Try(N, xi);

