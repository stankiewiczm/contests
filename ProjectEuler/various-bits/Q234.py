from numpy import *

LIM = 1000005;  Big = 999966663333;
Prime = [2];    IsP = ones(LIM+1, int);     IsP[0] = IsP[1] = 0;
def Gen():
    for i in range(2,LIM/2+1):
        IsP[2*i] = 0;
    p = 3;
    while (p < LIM):
        if IsP[p]:
            Prime.append(p)
            for q in range(2,LIM/p+1):
                IsP[p*q] = 0;
        p += 2;
    print "Generated",len(Prime),"primes up to",Prime[-1],".";


def T(n):
    return (n*(n-1))/2;
    
Gen();      Ans = 0;    sp = ' ';   NAns = 0;

for x in range(1,len(Prime)):
    psmall = Prime[x-1];
    plarge = Prime[x];

    if psmall**2 < Big:
    # now count numbers fro psmall**2+1 to plarge**2-1;
        Bot = psmall**2;
        if plarge**2 <= Big:
            Top = plarge**2;
        else:
            Top = Big;
            sp = 'end';
        
        FirstLarge = (Bot/plarge+1)*plarge;
        FirstSmall = Bot+psmall;
        
        Nsmall = (Top-Bot)/psmall;
        Nlarge = (Top-1-FirstLarge)/plarge+1;

        c1 = (FirstSmall*Nsmall) + psmall*T(Nsmall);
        c2 = (FirstLarge*Nlarge) + plarge*T(Nlarge);
        if (psmall*plarge < Big):
            c1 -= psmall*plarge;
            c2 -= psmall*plarge;
            NAns -= 2;
        Ans += c1+c2;
            
        NAns += Nsmall + Nlarge
        
print Ans, NAns
