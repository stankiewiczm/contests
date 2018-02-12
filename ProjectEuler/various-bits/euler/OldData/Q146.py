from Numeric import *

MAX = 1000001;     Prime = list();     Prime.append(2);    NP = 0;  
IsP = ones(MAX);    IsP[1] = 0;      

MOD = 273;          LIST = [1,22,29,55,62,155,181,209];


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
        

def CheckList(p,NP):
    if (p%3 == 0):
        return 0;
    for i in ([1,3,7,9,13,27]):
        N = p*p+i;
        for j in arange(NP):
            if (N%Prime[j] == 0):
#                if (i%7 == 6):
#                    print "#",p, "fucked up as",Prime[j],"| p^2 +",i;
                return 0;
    return 1;



NP = Gen();
print "Starting",NP,Prime[NP-1]

S = 10;      Pl = 2;    print S;
for i in arange(0,int(ceil(MAX/(10*MOD))) ):
#    while ((Prime[Pl] < 7*10*i+1) and (Pl < Prime[NP-1]-1)):
#        Pl = Pl+1;

    for j in arange(8):
        Tst = (MOD*i + LIST[j])*10;
        if (CheckList(Tst,NP) == 1):
            S = S+Tst;
            print Tst;
        
print "Total is ",S;
