from numpy import *

F = open('../TXTdata/matrix2.txt','r');
N = 80;     A = [];     B = [];      TODO = [];
for n in range(N):
    A.append(map(int, F.readline().split()));
    B.append([10**9]*N);
    B[n][0] = A[n][0]
    TODO.append([n,0]);

while len(TODO) > 0:
    [X,Y] = TODO.pop(0);
    if (X != 0):
        if (B[X-1][Y] > B[X][Y] + A[X-1][Y]):
            B[X-1][Y] = B[X][Y] + A[X-1][Y];
            if  [X-1,Y] not in TODO:
                TODO.append([X-1,Y]);
#    if (Y != 0):
#        if (B[X][Y-1] > B[X][Y] + A[X][Y-1]):
#            B[X][Y-1] = B[X][Y] + A[X][Y-1];
#            if [X,Y-1] not in TODO:
#                TODO.append([X,Y-1]);
    if (X != N-1):
        if (B[X+1][Y] > B[X][Y] + A[X+1][Y]):
            B[X+1][Y] = B[X][Y] + A[X+1][Y];
            if [X+1,Y] not in TODO:
                TODO.append([X+1,Y]);
    if (Y != N-1):
        if (B[X][Y+1] > B[X][Y] + A[X][Y+1]):
            B[X][Y+1] = B[X][Y] + A[X][Y+1];
            if [X,Y+1] not in TODO:
                TODO.append([X,Y+1]);

Ans = 10**9;
for i in range(len(B)):
    Ans = min(Ans, B[i][-1]);
print Ans;
