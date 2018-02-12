from numpy import *

LIM = 100000;       radI = 10000;
Rad = [1.]*(LIM+1);

def MakeRad():
    for k in range(1,LIM/2+1):
        Rad[2*k] = 2;

    p = 3;
    while (p < LIM):
        if Rad[p] == 1:
            for i in range(1,LIM/p+1):
                Rad[p*i] *= p
        p += 2;

    for k in range(len(Rad)):
        Rad[k] += float(k)/10**6;


MakeRad();
E = sort(Rad);
print int(round((E[radI]-int(E[radI]))*10**6))
