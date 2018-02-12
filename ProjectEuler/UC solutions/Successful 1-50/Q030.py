from Numeric import *

F = zeros(10);          S = 0;
for i in arange(10):
    F[i] = i**5;

for a in arange(4):
    for b in arange(10):
        for c in arange(10):
            for d in arange(10):
                for e in arange(10):
                    for f in arange(10):
                        Nm = 100000*a + 10000*b + 1000*c + 100*d + 10*e + f
                        if (F[a] + F[b] + F[c] + F[d] + F[e] + F[f] == Nm):
                            print Nm;
                            if (Nm > 1):
                                S = S+Nm;

print "All done", S
