from Numeric import *;

HAND = list();      Cn = 0;     Str = '';   POne = 0;

PNT = [0,0,3,8,15];

hands = []
for line in file("../TXTdata/poker.txt"):
    hands.append(line);
print len(hands);


def RetS(String):
    if (String == 'C'): return 0;
    if (String == 'D'): return 1;
    if (String == 'H'): return 2;
    if (String == 'S'): return 3;
    
def RetC(String):
    if (String == 'A'): return 14;
    if (String == 'K'): return 13;
    if (String == 'Q'): return 12;
    if (String == 'J'): return 11;
    if (String == 'T'): return 10;
    return int(String);
    

def Compare(Idx):
#    print HAND[Idx]
    ASuit = zeros(4);       ACard = zeros(15);      AScore = 0;
    BSuit = zeros(4);       BCard = zeros(15);      BScore = 0;
    for i in arange(5):
        ASuit[RetS(HAND[Idx][ i ][1])] += 1;
        BSuit[RetS(HAND[Idx][5+i][1])] += 1;

        ACard[RetC(HAND[Idx][ i ][0])] += 1;
        BCard[RetC(HAND[Idx][5+i][0])] += 1;

# Flushes:

    if (max(ASuit) == 5): AScore += 10;
    if (max(BSuit) == 5): BScore += 10;

# MultiCards:
    
    for i in arange(15):
        AScore += PNT[ACard[i]];
        BScore += PNT[BCard[i]];

    ACard[1] = ACard[14];           ACard[1] = ACard[14];

# Straights:

    for i in arange(10):
        if (ACard[i] == ACard[i+1] == ACard[i+2] == ACard[i+3] == ACard[i+4] == 1):
            AScore += 9;
        if (BCard[i] == BCard[i+1] == BCard[i+2] == BCard[i+3] == BCard[i+4] == 1):
            BScore += 9;
    
#    print ASuit,BSuit;  
#    print ACard,BCard;
#    print AScore,BScore;


    if (AScore == BScore == 0):
        for i in arange(14,1,-1):
            if ACard[i] > BCard[i]:
                return 1;
            if ACard[i] < BCard[i]:
                return -1;

    if (AScore == BScore == 3):
        for i in arange(14,1,-1):
            if (ACard[i] == 2) and (BCard[i] < 2):
                return 1;
            if (ACard[i] < 2) and (BCard[i] == 2):
                return -1;

        for i in arange(14,1,-1):
            if ACard[i] > BCard[i]:
                return 1;
            if ACard[i] < BCard[i]:
                return -1;
    
            
        print "Tie",AScore,BScore, "          ",HAND[Idx];
        
    return AScore-BScore;



for H in hands:
    HAND.append(list());
    for s in H:
        if (s == ' ') or (s == '\n'):
            HAND[Cn].append(Str);
            Str = '';
        else:
            if (s != '\n'):
                Str = Str+s;
    Cn = Cn+1;


Awin = 0;       Bwin = 0;   Ties = 0;   Out = 0;
for i in arange(1000):
    Out = Compare(i);
    if (Out > 0): Awin += 1;
    if (Out < 0): Bwin += 1;
    if (Out== 0): Ties += 1;

#    print Compare(i), "          ",HAND[i];

print Awin,Bwin,Ties;
