from Numeric import *

def IsSq(N):
    return (int(sqrt(float(N)))**2-N == 0);

TOT = 0;
for i in arange(2,20000):
    I = long(i)

    P = i*i+1;
    S = 3*P+1;
    if IsSq(S):
        if (S <= 1e9):
            print P,P,P+1,S;
            TOT += S;

    P = 2*i*i+1;
    S = 3*P+1;
    if IsSq(S*2):
        if (S <= 1e9):
            print P,P,P+1,S;
            TOT += S;


    P = 2*i*i-1;
    S = 3*P-1;
    if IsSq(S*2):
        if (S <= 1e9):
            print P,P,P-1,S;
            TOT += S;

print TOT;        
