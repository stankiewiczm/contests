from Numeric import *

B = list();             L = 80;     QUEUE = list();     Qpos = 0;
for i in arange(L):
    B.append(list());
    for j in arange(L):
        B[i].append(2e6);

A=[map(int ,line.split())for line in file("../TXTdata/matrix2.txt")]

for i in arange(L):
    B[i][0] = A[i][0];
    QUEUE.append(100*i);

while (Qpos < len(QUEUE)):
    X = QUEUE[Qpos]/100;
    Y = QUEUE[Qpos]%100;
    V = B[X][Y];
#    print X,Y,V;
    
    if (X != 0):
        if (B[X-1][Y] > B[X][Y]+A[X-1][Y]):
            B[X-1][Y] = B[X][Y]+A[X-1][Y];
            QUEUE.append(100*(X-1)+Y);

    if (X != L-1):
        if (B[X+1][Y] > B[X][Y]+A[X+1][Y]):
            B[X+1][Y] = B[X][Y]+A[X+1][Y];
            QUEUE.append(100*(X+1)+Y);

    if (Y != L-1):
        if (B[X][Y+1] > B[X][Y]+A[X][Y+1]):
            B[X][Y+1] = B[X][Y]+A[X][Y+1];
            QUEUE.append(100*(X)+Y+1);
    
    Qpos += 1;

MIN = 1000000;
for j in arange(L):
    if B[j][79] < MIN:
        MIN = B[j][79];
#    print B[j][0],"on left ........ on right:",B[j][79];

print MIN;
