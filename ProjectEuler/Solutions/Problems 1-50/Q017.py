from numpy import *

L = zeros(1001, int);

L[1] = 3;       L[2] = 3;       L[3] = 5;       L[4] = 4;       L[5] = 4;
L[6] = 3;       L[7] = 5;       L[8] = 5;       L[9] = 4;       L[10] = 3;
L[11]= 6;       L[12]= 6;       L[13]= 8;       L[14]= 8;       L[15] = 7;
L[16]= 7;       L[17]= 9;       L[18]= 8;       L[19]= 8;       L[20] = 6;
L[30]= 6;       L[40]= 5;       L[50]= 5;       L[60]= 5;       L[70] = 7;
L[80]= 6;       L[90]= 6;       L[1000]=11;

for a in range(2,10):
    for b in range(1,10):
        L[10*a+b] = L[10*a]+L[b];
        
for a in range(1,10):
    L[100*a] = L[a]+7;
    for b in range(1,100):
        L[100*a+b] = L[100*a] + L[b] + 3;

print sum(L)
    
