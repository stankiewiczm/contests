from Numeric import *

ALL = list();       PERS = list();      HYPS = list();
LIM = 1090000;       Lim = int(ceil(sqrt(LIM)));     # Max hypotenuse
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


for i in arange(1,Lim):
    J = min(int(ceil(sqrt(LIM-i*i))),i)
    for j in arange(1,J):
        if (GCD(i,j) == 1):
            A = i*i-j*j;    B = 2*i*j;  C = i*i+j*j;
            if (A%2 == 0):
                A = A/2;    B = B/2;    C = C/2;
            Tpl = [A,B,C];
            if ((Pers[sum(Tpl)] == 0) or (Hyps[C] == 0)):
                Pers[sum(Tpl)] = Pers[sum(Tpl)] + 1;
                Hyps[C] = Hyps[C] + 1;
                PERS.append(sum(Tpl));

PERS = sort(PERS);  

DATA = zeros(2*LIM+2);
for a in PERS:
    for j in arange(1,int(ceil(2.*(LIM+1)/a))):
        DATA[a*j] = DATA[a*j] + 1;


Max = 0;    MAX = 0;
for a in arange(1,2*LIM+1):
    if (DATA[a] > MAX):
        MAX = DATA[a];
        Max = a;
        print Max,MAX;

#print "\n\n",PERS;     # Answer: 2162160

