def Crash(i, Cars):
   overlap = [];
   for j in range(len(Cars)):
      if j != i:
         dV = Cars[i][0]-Cars[j][0];
         dR = Cars[i][1]-Cars[j][1];
         if (dV == 0):
            if (abs(dR) < 5):
               overlap.append( [0, 1e10] );     # Always next to each other;
         else:
            if (dV*dR > 0):                     # Faster car in front:
               if dR < 5:
                  overlap.append( [0, (5.-dR)/dV] );

            else:                               # Faster car behind:
               start = 0.;
               end = 0.;
               if abs(dR) > 5:
                  start = (abs(dR)-5.)/abs(dV);
               end   = (abs(dR)+5.)/abs(dV);
               overlap.append( [start, end] );            
            
#   print "Overlap calculation"

   IntTime = [];
   for pair in overlap:
      if pair[0] not in IntTime:
         IntTime.append( pair[0] );
      if pair[1] not in IntTime:
         IntTime.append( pair[1] );
   IntTime.sort();
#   print "Interesting times", IntTime;
         
   return IntTime;
#   print i, overlap

#   if time < 1e11:
#      return time;
   


def Check(t0, cars):
   D = [];
   if t0 < 0:
      return False;
   
   for veh in cars:
      D.append( veh[0]*(t0+1e-6) + veh[1] );

#   if t0 > 10:
#      print "Woooooooooo", t0,  D
      
   for a in range(len(cars)):
      for b in range(len(cars)):
         for c in range(len(cars)):
            if (a != b) and (a != c) and (b != c):
               if (abs(D[a]-D[b]) < 5) and (abs(D[b]-D[c]) < 5) and (abs(D[a]-D[c]) < 5):
                  return True;

#            for d in range(len(cars)):
#               if (a != b) and (b != c) and (c != a) and (a != d) and (b!= d) and (c != d):
#                  if (abs(D[a]-D[b]) < 5) and (abs(D[b]-D[c]) < 5) and (abs(D[c]-D[d]) < 5):
#                     return True;
   return False;

   

T = int(raw_input());
for i in range(T):
   print "Case #%d:" % (i+1),;
   N = int(raw_input());
   Data = []
   Cars = [];
   for i in range(N):
      line = raw_input().split();
      Cars.append( map(int, line[1:] ) );
   if N <= 2:
      print "Possible";
   else:
      problem = [];
      times = [];
      for i in range(len(Cars)):
#         problem.append( Crash(i, Cars) );
         times += Crash(i, Cars);
      times.sort();
      q = 0;
      #print "\n\n", times
      while (q < len(times)-1):
         if times[q] == times[q+1]:
            times.pop(q);
         else:
            q += 1
#      print times, "\n\n"

      Crashed = False;
      q = 0;
      while (q < len(times)) and not Crashed:
         Crashed = Check(times[q], Cars);
         q += 1;
      if Crashed:
         print times[q-1];
      else:
         print "Possible"
      

#      print min(problem)
#      print Cars

