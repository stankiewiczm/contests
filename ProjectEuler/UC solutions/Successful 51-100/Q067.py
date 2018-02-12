from Numeric import *

B = list();
for i in arange(100):
    B.append(list());
    for j in arange(i+1):
        B[i].append(0);

A=[map(int ,line.split())for line in file("../TXTdata/triangle.txt")]

B[0][0] = A[0][0];

for i in arange(99):
    B[i+1][0] = B[i][0] + A[i+1][0];
    B[i+1][i+1] = B[i][i] + A[i+1][i+1];
    for j in arange(1,i+1):
        B[i+1][j] = max(B[i][j],B[i][j-1]) + A[i+1][j];

print "Max is ",max(B[99]);
        
        
