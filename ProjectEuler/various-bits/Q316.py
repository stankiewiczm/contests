from RandomArray import *

def digits(n0):
    R = [];
    for c in str(n0):
        R.append(int(c));
    return R;


def Iter(n):
    Sn = digits(n);    
    D = len(str(n));
    L = [];
    C = 0;
    for k in range(D):
        L.append( int(10*random()) );
#    print L
    while (L != Sn):
        L = L[1:]+ [ int(10*random()) ]; 
#        print L[C:C+D], Sn
        C += 1

#    print L
    return C+1;



def Avg(n):
    S = 0.;      K = 10000;
    for k in range(K):
        S += Iter(n);
    print S/K
