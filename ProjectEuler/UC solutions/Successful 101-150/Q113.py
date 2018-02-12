from Numeric import *

def Choose(n,k):
    V = 1;
    for a in arange(k):
        V = ((n-a)*V)/(a+1);
    return V

NS = [0L, 0L, 0L, 0L]
for i in arange(100,101):
    NS[1] = Choose(9+i,9)-9*i-1;            # Increasing numbers
    NS[2] = Choose(10+i,10)-10*i-1;         # Decreasing numbers
    NS[3] = 9*i;                            # Constant numbers (> 0)
    NS[0] = 10**i-1 - NS[1]-NS[2]-NS[3];    # Bouncies

    print i, NS[1]+NS[2]+NS[3];                # Non-bouncies
