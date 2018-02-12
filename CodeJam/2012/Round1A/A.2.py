def Eval(A, B, Pi):
   prob = 1.;

   ret = [];
   
   for n in range(A):
      step = 2*n +  (B-A) +1;    # if it works
      fail = B+1;    # if it doesn't
      
#$      for i in range(A-n):            # What are the chances first A-n are good?
      prob *= Pi[A-n-1];

   #   print (n, prob), (step, fail);
     
      ret.append( prob*step + (1-prob)*(step+fail) )
   return min(ret)
   

T = int(raw_input());
for i in range(T):
   print "Case #%d:" % (i+1),;
   [A,B] = map(int, raw_input().split());
   Pi = map(float, raw_input().split());

   Ans = [B+2.];         # Keystrokes for surrender and do again
   Ans.append( Eval(A, B, Pi) );      # Evaluate for back backspaces, len B;

   print min(Ans)
   
   
   

