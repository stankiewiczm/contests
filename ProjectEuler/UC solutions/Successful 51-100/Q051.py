from Numeric import *

MAX = 1000001;    Prime = list();    Prime.append(2);    NP = 0;  
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

NP = Gen();
print "Generated",NP,"primes up to",Prime[NP-1];




def CheckDig(P0):
    Chck = zeros(10);   P = P0;

    while (P > 0):
        Chck[P%10] += 1;
        P = P/10;

    if (max(Chck) <= 2):
        return 0;
    for DIG in arange(10):
        if Chck[DIG] == max(Chck):
            break;

    Hull = P0;       Bit = 0;

    for i in arange(6):
        if (P0/(10**i)%10 == DIG):
            Bit += 10**i;
    Hull = P0 - DIG*Bit;            

    Ps = 0;
    for D in arange(1,10):
#        print P0, Hull+D*Bit, Hull, Bit
        Ps += IsP[Hull+D*Bit]

    if (Ps > 7):
        for D in arange(10):
            if (IsP[Hull+D*Bit]):
                print "Set of ",Ps,"#",D,":",Hull+D*Bit

#    print DIG, P0, Hull, Bit;





for i in arange(NP):
    CheckDig(Prime[i]);
