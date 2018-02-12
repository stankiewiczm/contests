from Numeric import *

# Have following: 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p;
Den = [1,2,5,10,20,50,100,200];

L = 201;
Z = zeros(L);
A = [ones(L)];
for i in arange(7):
    A.append(Z);


def Calc(i,Alast):
    D = Den[i];
#    print Alast;
    Anew = zeros(L);
    for j in arange(L):
        T = 0;  J = j;
        while (J >= D):
            J = J-D;
            T = T+Alast[J];
        Anew[j] = T;
    return Anew;

for I in arange(1,8):
    A[I] = A[I-1]+Calc(I,A[I-1]);
#    print A[I];

print A[7][200];        # Using all 8 coins, making 2 pounds.
