from numpy import *

def Dcheck(n1, n2):
    Dig = zeros(10, int);
    while (n1 > 0):
        Dig[n1%10] += 1;        n1 /= 10;
    while (n2 > 0):
        Dig[n2%10] -= 1;        n2 /= 10;
    return (max(Dig) == min(Dig))


N1 = 123456;        Fin = False;
while (not Fin):
    if Dcheck(N1, 2*N1):
        if Dcheck(3*N1, 4*N1) and Dcheck(N1, 3*N1):
            if Dcheck(5*N1, 6*N1) and Dcheck(N1, 5*N1):
                print N1, 2*N1, 3*N1, 4*N1, 5*N1, 6*N1;
                Fin = True;
    N1 += 1;
    
