from Numeric import *

MAX = 20001;    Prime = list();    Prime.append(2);    NP = 0;  
IsP = ones(MAX);        IsP[1] = 0;      

def Gen():
    for i in arange(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    NIsP = 1;
    while (n < MAX):
        if (IsP[n] == 1):
            Prime.append(n);
            NIsP += 1;
            for i in arange(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n = n+2;
    return NIsP;
        
    
def Mink(n):
    M = 1;
    S = 1;
    k = 1;
    while (S != 0):
        M = (M*10)%n;
        S = (S+M)%n;
        k += 1;
    return k



NP = Gen();     T25 = list();

for i in arange(10,20000):
    if (i%2 == 1) and (i%5 != 0):
        if (IsP[i] == 0):
            Mi = Mink(i);
            if (i-1)%Mi == 0:
                if (len(T25) < 25):
                    T25.append(i);

print len(T25), sum(T25);
        
