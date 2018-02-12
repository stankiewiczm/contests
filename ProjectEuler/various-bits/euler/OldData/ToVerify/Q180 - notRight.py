from Numeric import *

# f1+f2-f3 == (x+y+z)(x**n+y**n-z**n);

#def f1(x,y,z,n):
#    return ( x**(n+1) + y**(n+1) - z**(n+1) );
#
#def f2(x,y,z,n):
#    return (x*y+y*z+z*x)*( x**(n-1) + y**(n-1) - z**(n-1) );
#
#def f3(x,y,z,n):
#    return (x*y*z)*( x**(n-2) + y**(n-2) - z**(n-2) );
#
#def F(x,y,z,n):
#    return (x+y+z)*(x**n+y**n-z**n);

def GCD(a,b):       # for a > b;
    while (b>0):
        c = b;
        b = a-(a/b)*b;
        a = c;
    return a;


def IsSqB1(n, Lim):
    if n >= Lim:
        return False;

    if (int(sqrt(n))**2-n == 0):
        return True;

    return False;


LARGE = 64*81*25*49*11*13*17*19*23*29*31;
LIM = 35;

Ss = list();
for i in arange(100):
    Ss.append([]);
    for j in arange(100):
        Ss[i].append(0);
    


TOT = 0;        TOT2 = 0;       S = long(0);
for xd in arange(1,LIM+1):
    for xn in arange(1,xd):
        if GCD(xd,xn) == 1:
            for yd in arange(1,LIM+1):
                for yn in arange(1,yd):
                    if GCD(yd,yn) == 1:
                        if (xn*yd + xd*yn < yd*xd):
                            zn = xn*yd+xd*yn;
                            zd = yd*xd;
                            GZ = GCD(zd, zn);
                            zn = zn/GZ;     zd = zd/GZ;
                            if (zd <= LIM):
                                TOT += 1;

                                Sn = xn*yd*zd + xd*yn*zd + xd*yd*zn;
                                Sd = xd*yd*zd;
                                Gs = GCD(Sn,Sd);        
                                Sn = Sn/Gs;     Sd = Sd/Gs;

                                Ss[Sn][Sd] = 1;
                            
                        zn2 = (xn*yd)**2+(xd*yn)**2
                        zn = int(sqrt(zn2));
                        zd = (xd*yd);
                        if (zn < zd) and (zn**2 == zn2):
                            GCz = GCD(zd,zn);

                            zd = zd/GCz;
                            zn = zn/GCz;
                            if (zd <= LIM):
                                TOT2 += 1;

                                Sn = xn*yd*zd + xd*yn*zd + xd*yd*zn;
                                Sd = xd*yd*zd;
                                Gs = GCD(Sn,Sd);
                                Sn = Sn/Gs;     Sd = Sd/Gs;

                                Ss[Sn][Sd] = 1;
                                if (Sd > LIM):
                                    print Sn,Sd;

NUM = 0;
DEN = LARGE;
NSs = 0;

for i in arange(100):
    for j in arange(100):
        if (Ss[i][j] == 1):
            NUM += (LARGE/j)*i;
            NSs += 1;

GLS = GCD(NUM, DEN)

print NSs, GLS, TOT, TOT2;
print NUM/GLS, DEN/GLS, (NUM+DEN)/GLS;

"""
N = 3;
for i in arange(50):
    for j in arange(i+1):
        for k in arange(j+1):
            if (f1(i,j,k,N)+f2(i,j,k,N)-f3(i,j,k,N)-F(i,j,k,N) != 0):
                print i,j,k,N,f1(i,j,k,N)+f2(i,j,k,N)-f3(i,j,k,N),F(i,j,k,N);
"""
