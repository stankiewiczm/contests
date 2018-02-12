from Numeric import *
from random import *

FREQ = zeros(40);       # Number of times place is visited
GOTO = [0,0,10,11,24,39,5];


def Die(N):
    return int(N*random())+1

def Move(Start,CoCh,Chns):
    Pos = Start;
    Doubs = 0;
    D1 = 0;     D2 = 0;
    while (D1 == D2):
        D1 = Die(4);
        D2 = Die(4);
        if (D1 == D2):
            Doubs += 1;
        Pos += D1+D2;
    if (Doubs >= 3) or (Pos == 30):
        Pos = 10;
        return Pos;

    Pos = (Pos%40);


    # Community chest:    
    if (Pos == 2) or (Pos == 17) or (Pos == 33):
#        print "Community chest for the ",CoCh
        CoCh = Die(16);
        if (CoCh == 1) or (CoCh == 2):
            Pos = GOTO[CoCh]

    if (Pos == 7) or (Pos == 22) or (Pos == 36):
#        print "Chance ",Chns
        Chns = Die(16)
#        print "chance roled a ",Chns
        if (Chns >= 1) and (Chns <= 6):
            Pos = GOTO[Chns];
        if (Chns == 7) or (Chns == 8):
            Pos = Pos + (55-Pos)%10;
        if (Chns == 9):
            if (Pos == 22):
                Pos = 28;
            else:
                Pos = 12;
        if (Chns == 10):
            Pos = Pos-3;

    if (Pos == 30):
        Pos = 10;


    return (Pos%40);



POS = 0;    CO = 0;     CH = 0;     R = 0;

for i in arange(1000000):
    POS = Move(POS,CO,CH);
#    R = Move(POS,CO,CH);
#    POS = R%100;
#    CH  = R/1000000;
#    CO  = (R)/1000-CH*1000;
    
#    print i, POS;
    FREQ[POS] += 1;
    
print FREQ;
