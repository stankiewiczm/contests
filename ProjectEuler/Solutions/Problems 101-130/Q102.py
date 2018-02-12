from numpy import *

F = open('../TXTdata/triangles.txt','r');

def ReadTri():
    L = F.readline().split()[0];        S = ''
    for c in L:
        if c == ',':
            S += ' ';
        else:
            S += c;
    return map(int, S.split());


def Area(A,B,C):
    S1 = sqrt( (A[0]-B[0])**2 + (A[1]-B[1])**2 );
    S2 = sqrt( (B[0]-C[0])**2 + (B[1]-C[1])**2 );
    S3 = sqrt( (C[0]-A[0])**2 + (C[1]-A[1])**2 );
    s = (S1+S2+S3)/2;
    return sqrt( s*(s-S1)*(s-S2)*(s-S3) );


def Ocheck(coord):
    a = coord[0:2];
    b = coord[2:4];
    c = coord[4:6];
    O = [0,0];
    return (Area(a,b,O)+Area(b,c,O)+Area(c,a,O) - Area(a,b,c) < 1e-6);


Ans = 0;
for i in range(1000):
    Ans += Ocheck(ReadTri())
print Ans
