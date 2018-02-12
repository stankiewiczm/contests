from Numeric import *

def Choose(N,R):
    S = 1;
    for i in arange(R):
        S = S*(N-i);
    for i in arange(R):
        S = S/(i+1);
    return (S);

print Choose(40,20);
