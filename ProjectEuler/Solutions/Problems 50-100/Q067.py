from numpy import *

F = open('../TXTdata/triangle.txt','r');
A = [];     B = [];

for n in range(100):
    A.append( map(int, F.readline().split()));
    B.append( [0]*(n+1) );
B[0][0] = A[0][0];

for i in range(1,100):
    B[i][0] = B[i-1][0]+A[i][0];
    B[i][i] = B[i-1][i-1]+A[i][i];
    for j in range(1,i):
        B[i][j] = max( B[i-1][j-1], B[i-1][j])+A[i][j];

print max(B[99]);
