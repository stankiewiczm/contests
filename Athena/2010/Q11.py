from numpy import *
from RandomArray import *

H = [1,7,10,13,19,23,28,31,32,44,49];
Happy = zeros(60, int);      NHappy = 0;        Target = 2;

for k in range(1,60):
    n = k;
    for l in range(10):
        n = (n%10)**2 + ((n/10)%10)**2 + (n/100)**2;
    if n == 1:
        Happy[k] = 1;

F = [1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600];


TOTAL = 0;      D12 = [1,2,3,4,5,6,7,8,9,10,11,12];

It1 = [0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3];
It2 = [1,1,2,2,3,3,0,0,2,2,3,3,0,0,1,1,3,3,0,0,1,1,2,2];
It3 = [2,3,1,3,1,2,2,3,0,3,0,2,1,3,0,3,0,1,1,2,0,2,0,1];
It4 = [3,2,3,1,2,1,3,2,3,0,2,0,3,1,3,0,1,0,2,1,2,0,1,0];

def Last6Fit(tgt, r1, r2, c1, c2, LIST):
    L4 = [];        L2 = [];        RET = 0;
    for x1 in LIST:
      for x2 in LIST:
        if (x1 != x2):
#           RET += 24;
          if tgt == Happy[c1+x1+x2]:
            RET += 24;
          else:            
            L4 = [];
            for x in LIST:
              if (x != x1) and (x != x2):
                  L4.append(x);

            for cnt in range(24):
                x3 = L4[It1[cnt]];
                x4 = L4[It2[cnt]];
                x5 = L4[It3[cnt]];
                x6 = L4[It4[cnt]];

                if Happy[c1+x1+x2] + Happy[c2+x3+x4]+Happy[x5+x6]+Happy[r1+x1+x3+x5]+Happy[r2+x2+x4+x6] >= tgt:
                    RET += 1;
#            print LIST, x1, x2, L4; 

    return RET;


          
for a in D12:
  for b in D12:
    for c in D12:
      if (a != b != c != a):
         D9 = [1,2,3,4,5,6,7,8,9,10,11,12];
         for k in range(11,-1,-1):
           if (k == a-1) or (k == b-1) or (k == c-1):
               D9.pop(k);

         # D9 should be fixed by here;

         for d in D9:
           for e in D9:
             for f in D9:
               D6 = [];
               for l in D9: D6.append(l);

               if (d != e != f != d):
                  for l in range(8,-1,-1):
                    if (D6[l] == d) or (D6[l] == e) or (D6[l] == f):
                       D6.pop(l);

                  # D6 should be fixed by here

                  NHappy = Happy[a]+Happy[b]+Happy[c+d]+Happy[e+f];
                  if NHappy > 1:
                      TOTAL += 720

                  else:
                      Target = 2-NHappy;
                      TOTAL += Last6Fit(Target, b+f, e, a+d, c, D6);

         print (a,b,c), TOTAL, float(TOTAL)/F[12];

                      
print TOTAL, TOTAL/720,'/',1320*504;

print "fin"

#(12, 11, 10) 329557628 0.688009451325
#329557628 457718 / 665280
