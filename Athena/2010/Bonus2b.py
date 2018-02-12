from numpy import *

def C(n,r):
    R = 1;
    for k in range(r):
        R = (R*(n-k))/(k+1);
    return R;

LIM = 10**3;    P = [];     IsP = ones(LIM+1, int);        IsP[1] = 0;
for n in range(2,LIM):
    if IsP[n] == 1:
        P.append(n);
        for i in range(n, LIM/n+1):
            IsP[n*i] = 0;

print "Generated",len(P),"primes";



def Calc(p, p1):
    Inv = zeros(p, int);

    for k in range(p1):
        for l in range(p):
            if (k*l)%p == 1:
                Inv[k] = l;

    SUM = sum(Inv[1:p/2+1]);
    SUM = SUM%p;

    RET = (2-2*p)*(1-p*SUM);
    RET = RET%(p*p);

    print (RET%p, RET/p),;
    return;
    

P.pop(0);    P.pop(0);     P.pop(0);
for k in P:
    if (k%4 == 1):#IsP[k/2+1] :
        CK = ((C(k, k/2+1)/k)%(k*k));
        print k, k/2+1,"  ",CK%k, CK/k, "   ", ;
        Calc(k, k/2+1);

        if IsP[k/2+1]:
            print "    Prime",;
        print " ";
 
# Mozna pokazac (prosto) ze C(p, (p+1)/2) jest = p*2 mod p^2
# Patrzymy na C(p,(p+1)/2)/p, zeby uproscic.  Jest to =2 mod 2
# Potrzebujemy znalezdz mod p^2.
