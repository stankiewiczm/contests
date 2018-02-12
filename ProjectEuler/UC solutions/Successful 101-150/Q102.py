from Numeric import *


A=[map(int ,line.split())for line in file("../TXTdata/triangles.mod.txt")]
S = 0;

for L in A:
    X1 = L[0];  Y1 = L[1];
    X2 = L[2];  Y2 = L[3];
    X3 = L[4];  Y3 = L[5];

    ModA = abs(X1*Y2-Y1*X2) + abs(X1*Y3-X3*Y1) +abs(X2*Y3-X3*Y2);
    Full = abs((X1-X3)*(Y2-Y3) - (X2-X3)*(Y1-Y3));

    if (ModA == Full):
        S += 1;

print S
