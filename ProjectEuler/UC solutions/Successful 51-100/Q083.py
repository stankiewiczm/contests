from Numeric import *
from time import *

t0 = time();

B = list();             L = 80;     QUEUE = list();     Qpos = 0;
for i in arange(L):
    B.append(list());
    for j in arange(L):
        B[i].append(2e6);

A=[map(int ,line.split())for line in file("../TXTdata/matrix2.txt")]

B[0][0] = A[0][0];
QUEUE.append(0);

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

    if (Y != 0):
        if (B[X][Y-1] > B[X][Y]+A[X][Y-1]):
            B[X][Y-1] = B[X][Y]+A[X][Y-1];
            QUEUE.append(100*(X)+Y-1);
   
    if (Y != L-1):
        if (B[X][Y+1] > B[X][Y]+A[X][Y+1]):
            B[X][Y+1] = B[X][Y]+A[X][Y+1];
            QUEUE.append(100*(X)+Y+1);

    Qpos += 1;

print len(QUEUE), Qpos;
print B[L-1][L-1], time()-t0

