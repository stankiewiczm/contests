from Numeric import *

p = 109;   q = 37;   n = p*q;    phi = (p-1)*(q-1);

MinPhiM = zeros(40000);

def GCD(a,b):
    while (b > 0):
        c = b;
        b = a-(a/b)*b;
        a = c;
    return a;


def CountMs(N):
    for m in arange(N):
        if (m%100 == 0):
            print m
        M = long(m*m);      ex = 2;
        while (M != m):
            M = (M*m)%n;
            ex += 1;
        MinPhiM[m] = ex-1;


CountMs(n);

Es = list();
for e in arange(1,phi):
    if GCD(phi,e) == 1:
        Es.append(e);
print len(Es), phi;

Uncs = zeros(len(Es));
for j in arange(len(Es)):
    e = Es[j];
    for u in arange(1,n):
        if (e-1)%MinPhiM[u] == 0:
            Uncs[j] += 1;

print max(Uncs), Uncs[180];



#for e in arange(181,182):
#    E = e-1;
#    for k in arange(n):
#        if (E%MinPhiM[k] == 0):
#            print k," is unconcealed"            

print "Done"
