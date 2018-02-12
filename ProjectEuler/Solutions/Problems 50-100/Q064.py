from numpy import *

def Seq(n0):
    Rn = sqrt(n0);      S = [];         K = [];     # List of trips, and k's
    k = int(Rn);        d = 1;          n = k;

    while (True):
        u = int(d/(Rn-n))               # New out
        v = (n0-n*n)/d                  # New d
        w = -n+u*v;                     # New n;

        k = u;      d = v;      n = w;
        if [k,d,n] not in S:
            S.append([k,d,n]);
            K.append(k);
        else:
            return K


ANS = 0;
for n in range(1,10000+1):
    if int(sqrt(n))**2 != n:
        ANS += (len(Seq(n))%2 == 1);
print ANS;
