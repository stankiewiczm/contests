from time import *

def C(n,r):
    if (r == 0):
        return 1;
    else:
        return (C(n-1,r-1)*n)/r;


def SqrFree(n):
    if (n%4 == 0) or (n%9 == 0) or (n%25 == 0) or  (n%49 == 0):
        return False;
    return True;
    

t0 = time();        L = [];
for i in range(51):
    for j in range(i/2+1):
        if SqrFree(C(i,j)):
            if (C(i,j) not in L):
                L.append(C(i,j));

print sum(L), len(L), time()-t0;
