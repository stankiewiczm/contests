from Numeric import *

MX = 100;

DEN = list();
for i in arange(MX):
    DEN.append(long(i+1));
#Den = [1,2,3,4,5,6,7,8];

L = 101;
Z = zeros(L)-1;
A = [ones(L)];
for i in arange(MX):
    A.append(Z);
    for w in arange(len(A[i])):
        A[i][w] = long(A[i][w]);


def Calc(i,Alast):
    D = DEN[i];
#    print Alast;
    Anew = zeros(L);
    for w in arange(len(Anew)):
        Anew[w] = long(Anew[w]);
    for j in arange(L):
        T = long(0);  J = long(j);
        while (J >= D):
            J = J-D;
            T = T+Alast[J];
        Anew[j] = T;
    return Anew;

for I in arange(1,MX):
    A[I] = A[I-1]+Calc(I,A[I-1]);
#    print A[I];


#for i in arange(100):
#    print i+1,A[i][100];
print MX,A[len(DEN)-1][100]-1;
