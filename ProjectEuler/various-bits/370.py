from time import *

t0 = time();

def RP(a,b):
    while (a*b != 0):
        b -= (b/a)*a;
        if (b == 0):
            return a;
        a -= (a/b)*b;
    return b;
        
# ad**2, adn, an**2;
# So d**2 <= LIM
# and n**2 <= LIM
# Perimeter = a(d^2+dn+n^2)

LIM = 25*10**12;
lim = int(LIM**0.5)+1
Ans = LIM/3;    # Equilaterals
phi = (5**0.5+1)/2;
for d in range(1,int((LIM/3)**0.5)+1 ):
    if d%100 == 0:
        print d, Ans
    for n in range(d+1, min(lim, int(phi*d)+1)):
        if RP(d,n) == 1:
#            print d, n, LIM/(d*d+d*n+n*n);
            Ans += LIM/(d*d+d*n+n*n);

print Ans
print time()-t0
