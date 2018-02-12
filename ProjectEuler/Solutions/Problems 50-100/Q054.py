from numpy import *

def Value(lst):
    # Full > Flush > Straight > 3 > 2x2 > 2 > high card
    #  10      8         7     6     4    2     0
    crd = ['0','1','2','3','4','5','6','7','8','9','T','J','Q','K','A'];
    
    Cards = [0]*15;     Pair = [];      Strait = [];
    Score = 0;

    for card in lst:
        for k in range(15):
            if card[0] == crd[k]:
                Cards[k] += 1;

    if (lst[0][1] == lst[1][1] == lst[2][1] == lst[3][1] == lst[4][1]):
        Score = 8;                 # Flush

    for k in range(len(Cards)):
        if (Cards[k] == 1):
            Strait.append(k);

    if max(Cards) == 1:
        if min(Strait)+4 == max(Strait):
            Score = 7;              # Straight

    if max(Cards) == 2:
        for k in range(len(Cards)):
            if Cards[k] == 2:
                Pair.append(k);     # Pairs
                Score += 2 + k/20.;
                Score += max(Strait)/1000.;

    if max(Cards) >= 3:
        Score = 6;                  # Three of a kind
        Cards.remove(3);
        if max(Cards) == 2:
            Score = 10;             # Full house

    if (Score <= 0):
        Score += max(Strait)/20.;

    return Score


Fin = open('../TXTdata/poker.txt','r');     P1 = 0;
for n in range(1000):
    Line = (Fin.readline()).split();
    if Value(Line[0:5]) > Value(Line[5:10]):
        P1 += 1;
print P1;
