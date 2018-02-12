from numpy import *

def Eval(seq, n0):
    N = [ seq[-1] ] ;        D = [ 1 ];
    for i in range(len(seq)-2,-1,-1):
        D.append( N[-1] );
        N.append( seq[i]*N[-1] + D[-2] );

    if (N[-1]**2 == n0*D[-1]**2+1):
        return N[-1];
    return 0
    
def Seq(n0):
    Rn = sqrt(n0);      k = int(Rn);        
    S = [];             K = [k];     # List of trips, and k's
    d = 1;              n = k;

    while (True):
        u = int(d/(Rn-n))               # New out
        v = (n0-n*n)/d                  # New d
        w = -n+u*v;                     # New n;

        k = u;      d = v;      n = w;
        K.append(k);
        num = Eval(K, n0);
        if (num > 0):
            return num;


ANS = 0;        NMax = 0;
for n in range(1,1000+1):
    if int(sqrt(n))**2 != n:
        if NMax < Seq(n):
            NMax = Seq(n);      ANS = n;
            print n, NMax;
print ANS;
