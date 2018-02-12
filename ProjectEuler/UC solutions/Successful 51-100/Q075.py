from Numeric import *

ALL = list();       PERS = list();      HYPS = list();
LIM = 2000000;       Lim = int(ceil(sqrt(LIM)));     # Max perimeter
Pers = zeros(5*LIM/2);  Hyps = zeros(LIM);

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


for i in arange(0,Lim/2):
    I = 2*i+1;
    Jmax = min(I,(LIM/I-I))/2;
    for j in arange(0,Jmax):
        J = 2*j+1;
        if (GCD(I,J) == 1):
            A = (I*I-J*J)/2;    B = I*J;  C = (I*I+J*J)/2;
            Tpl = [A,B,C];
            PERS.append(sum(Tpl));

PERS = sort(PERS);  

DATA = zeros(2*LIM+2);
for a in PERS:
    for j in arange(1,int(ceil((LIM+1)/a))):
        DATA[a*j] = DATA[a*j] + 1;


Count = 0;    
for a in arange(1,LIM+1):    # Normally LIM+1;
    if (DATA[a] == 1):
        Count = Count+1;
print Count;
