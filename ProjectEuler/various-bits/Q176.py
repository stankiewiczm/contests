from Numeric import *

LIM = 10000;           MAX = 2*LIM*LIM;
Cath = zeros(MAX);
T = 0;

for m in range(2,LIM):
    for n in range(1,m):
        if (m+n)%2 == 1:
            a = m*m-n*n;
            b = 2*m*n
#            c = m*m+n*n;
#            print (m,n),"  ->  ",(a,b,c);
            T += 1;

            Cath[a] += 1;
            Cath[b] += 1;
#            for d in range(1,MAX/a):
#                Cath[a*d] += 1;
#            for d in range(1,MAX/b):
#                Cath[b*d] += 1;

#    print m, T#, max(Cath)
            
