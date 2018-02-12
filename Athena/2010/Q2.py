from numpy import *

def C(n,r):
    R = 1L;
    for k in range(r):
        R = (R*(n-k))/(k+1);
    return R;

def max(n1, n2):
    if (n2 > n1):
        return n2;
    return n1;


REC2 = C(5001,2)**2;

N = 5000;       SQR = 0L;
for x1 in range(N):
    SQR += (N-x1)**2;

OBL = REC2-SQR;
STR = "";

print SQR, OBL, REC2;


for k in range(35):
    STR += str(OBL/REC2);
    print OBL/REC2,;
    OBL = (OBL%REC2)*10;

print "\n\n",STR;
