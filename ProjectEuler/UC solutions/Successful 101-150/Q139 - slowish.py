from Numeric import *

ALL = list();       PERS = list();      HYPS = list();
LIM = int(1e8);         Lim = int(ceil(sqrt(LIM)));         # Max perimeter
#Pers = zeros(5*LIM/2);  Hyps = zeros(LIM);

def GCD(a,b):
    while (a*b > 0):
        if (a > b):
            a = a-(a/b)*b;
        else:
            b = b-(b/a)*a;
    return (a+b);


def NoTri(N):
    Cnt = 0;
    for i in PERS:
        if (N%i == 0):
            Cnt = Cnt+1;
        if (N < i):
            break;
    return Cnt;


TOT = 0;
for i in arange(0,Lim/2):
    I = 2*i+1;
    Jmax = min(I,(LIM/I-I))/2;
    for j in arange(0,Jmax):
        J = 2*j+1;
        if (GCD(I,J) == 1):
            A = (I*I-J*J)/2;    B = I*J;  C = (I*I+J*J)/2;  P = A+B+C;

            if (C*C)%(C*C-2*A*B) == 0:
                print A,B,C, "central hole area", C*C-2*A*B, (A-B)**2
                TOT += LIM/P;
                
#            Tpl = [A,B,C];
#            print Tpl, sum(Tpl)
#            PERS.append(sum(Tpl));
#            TOT += 1;

print "Created PERS array, of length",len(PERS)
print "Make a running total",TOT
