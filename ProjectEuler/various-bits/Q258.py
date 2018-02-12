from numpy import *

G = [];
for k in range(2000):
    G.append(1);
print "start"
while (k < 1e7):
    k += 1;
    G.append( (G[k-2000]+G[k-1999])%20092010 );
    if (G[k] <= 1):
        print k, G[k]
#    print k, G[k];
