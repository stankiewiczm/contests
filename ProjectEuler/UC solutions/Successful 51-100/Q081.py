from Numeric import *
from time import *

t0 = time()
B = list();             L = 80;
for i in arange(L):
    B.append(list());
    for j in arange(L):
        B[i].append(0);

A=[map(int ,line.split())for line in file("../TXTdata/matrix2.txt")]

#print A;

B[0][0] = A[0][0];

for i in arange(1,L):
    B[i][0] = B[i-1][0]+A[i][0];
    B[0][i] = B[0][i-1]+A[0][i];
    for j in arange(1,i):
        B[i-j][j] = min(B[i-j][j-1],B[i-j-1][j])+A[i-j][j];

for i in arange(L,2*L-1):
    B[i-L+1][L-1] = B[i-L][L-1]+A[i-L+1][L-1];
    B[L-1][i-L+1] = B[L-1][i-L]+A[L-1][i-L+1];
    for j in arange(i-L+1,L):
        B[i-j][j] = min(B[i-j][j-1],B[i-j-1][j])+A[i-j][j];

print B[L-1][L-1], time()-t0;
