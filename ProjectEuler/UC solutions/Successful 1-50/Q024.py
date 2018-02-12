from Numeric import *

N = 1000000-1;    D = zeros(10);

def Translate(d):
    e = zeros(10);
    e[0] = d[0];
    for i in arange(1,10):
        Cnt = 0;
        Fre = zeros(10-i);
        for j in arange(10):
            Mis = 1;
            for k in arange(i):
                if e[k] == j:
                    Mis = 0;
            if (Mis == 1):
                Fre[Cnt] = j;
                Cnt = Cnt+1;
        e[i] = Fre[d[i]];
    return(e);
            

def F(n):
    P = 1;
    for i in arange(1,n+1):
        P = P*i;
    return P;

for i in arange(10):
    D[i] = N/(F(9-i));
    N = N - D[i]*F(9-i);

print D,"\n",Translate(D);

