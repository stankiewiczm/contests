from Numeric import *

MAX = 20001;    Prime = list();    Prime.append(2);    NP = 0;  
IsP = ones(MAX);        IsP[1] = 0;      

def Gen():
    for i in arange(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    NIsP = 1;
    while (n < MAX):
        if (IsP[n] == 1):
            Prime.append(n);
            NIsP += 1;
            for i in arange(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n = n+2;
    return NIsP;


def SortN(N):
    Dl = list();
    for d in str(N):
        Dl.append(int(d));
    D = sort(Dl);
    SN = 0;
    for b in arange(len(D)):
        SN = SN*10+D[b];
    return SN;



NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];


BEST = 0.5
for i in arange(500,250,-1):
#    print i, Prime[i];
    for j in arange(250,460):
        p1 = Prime[i];      p2 = Prime[j];

        if (p1*p2 < 1e7):
            if SortN(p1*p2) == SortN( (p1-1)*(p2-1) ):
                if (float(p1+p2-1)/(p1*p2) < MAX):
                    MAX = float(p1+p2-1)/(p1*p2)
                    print p1*p2, (p1-1)*(p2-1), 1-float(p1+p2-1)/(p1*p2)

print "All done"
