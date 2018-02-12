from Numeric import *;

def ITER(N):
    Nf = sqrt(N);
    REC = zeros(500);
    Tak = int(Nf);      FactD = 1;
    Tak = -Tak;                 Tak0 = Tak;
    Num = Nf - Tak;             Num0 = Num;
    Den = (N-(Tak)**2)/FactD;   Den0 = Den;

    if (Tak+Nf == 0):
        return 0;

    for i in arange(500):
        REC[i] = int(Num/Den);
        Tak = - Tak - REC[i]*Den;
        FactD = Den;

        Num = (Nf - Tak);
        Den = (N-(Tak)**2)/FactD;

        if (Tak0 == Tak) and (Den0 == Den):
            return i+1;
    print N, REC;
        
    
NUM = 0;
for i in arange(1,10001):
#    print i, ITER(i);
    if (ITER(i) % 2 == 1):
        NUM += 1;
print NUM;
