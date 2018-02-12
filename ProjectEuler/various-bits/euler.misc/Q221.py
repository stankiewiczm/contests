from Numeric import *
from time import *

t0 = time();        t1 = t0;    L = [];     Lp = [];

for s in range(3,2000000):
    T = 0;      SOL = 0;
    for q in range(1,s/2+1):
        T = (T+2*q-1)%s;
        if (T == s-1):                  # Need q*q+1 = 0 (mod s)
            p = (q*(s-q))/s
            A = p*q*(s-q);
#            if (A not in L):
            L.append(A);
#            Lp.append(p);
#            if p == 1:
#                print (p,q,s-q), s
#            else:
#                print "Repeat",A,(p,q,s-q)
    if (s%1000 == 0):
        print s, len(L), time()-t1
        t1 = time();
                        
#        r = s-q;
#        if (r*q)%s == 1:
#            p = (r*q)/s
#            if (p*q*r) not in L:
#                L.append(p*q*r);
#                print len(L),s, (q,r), ((r*r)%s, (q*q)%s);

#                print L[-1], (p,-q,-r);

print len(L), time()-t0;

