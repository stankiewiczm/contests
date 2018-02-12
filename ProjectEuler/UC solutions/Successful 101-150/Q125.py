from Numeric import *

LIM = 100000000 ;

SQR = zeros(10000);
for i in arange(len(SQR)):
    SQR[i] = i*i;

def CheckPal(pal):
    Spal = str(pal);
    for i in arange(len(Spal)):
        if (Spal[i] != Spal[len(Spal)-1-i]):
            return 0;
#    print pal,Spal
    return pal;

Curr = 0;       TOT = long(0);    N = 0;      LIST = list();
for St in arange(1,7071):
    Curr = SQR[St] + SQR[St+1];         N = 2;
    while (Curr < LIM):
        ANS = CheckPal(Curr);
        if (ANS > 1):
            TOT += ANS;
            LIST.append(ANS);
        Curr += SQR[St+N];
        N += 1;

TOT2 = TOT;
SLIST = sort(LIST);
for i in arange(1,len(SLIST)):
    if SLIST[i] == SLIST[i-1]:
        TOT2 = TOT2 - SLIST[i];
    
print "All done, sum is",TOT, len(LIST), sum(LIST), TOT2;
        

