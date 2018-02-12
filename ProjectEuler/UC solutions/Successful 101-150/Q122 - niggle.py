from Numeric import *

MIN = list();
for i in arange(0,205):
    MIN.append([]);
    for j in arange(i):
        MIN[i].append(j+1);


for m in arange(2,200+1):
    # We try to find the minimal exponentiation menthod for m
    for n in arange(1,m):       # Look at all lesser m's (which are best)
        if (len(MIN[n])+1 < len(MIN[m])) and (m-n in MIN[n]):
            MIN[m] = [];
            for k in MIN[n]:    MIN[m].append(k);
            MIN[m].append(m);
#            print "new minumum found for ",m,"through n=",n,MIN[n], MIN[m]

TOT = 0;
for i in arange(1,201):
#    print i, len(MIN[i])-1, MIN[i]
    TOT += len(MIN[i])-1;
print TOT, TOT-2;       # Mis-nomer on 77 and 154, by one.
