def Solve(hand, deck):
    C = len(hand);
    T = 1;
    Score = 0;

    Thand = 0;      Chand = 0;      Shand = 0;
    Tdeck = 0;      Cdeck = 0;      Sdeck = 0;
    for card in hand:
        Chand += card[0];
        Shand += card[1]
        Thand += card[2]
    for card in deck:
        Cdeck += card[0];
        Sdeck += card[1];
        Tdeck += card[2];

    while (T > 0):
        if (len(deck) == 0) or (Chand == 0) or (Sdeck == 0):
            while Thand > 0:                    # No more cards to pick up
                i = 0;
                while hand[i][2] == 0:          # Use up all turn cards
                    i += 1;
                play = hand.pop(i);
                Chand -= play[0];
                Shand -= play[1];       Score += play[1];
                Thand -= play[2];       T += play[2]-1

            scores = []
            for card in hand:                       # Use best score cards
                scores.append(card[1]);
            Sorted = sorted(scores, reverse=True)
            for i in range(T):
                Score += Sorted[i];
            return Score

        else:
            if (T == 1):
                if (Thand = 0):                     # Take best score card
                    scores = []
                    for card in hand:
                        scores.append(card[1]);
                    return Score + max(scores);
                else:
                    
                    


            T = T-1
            # Think

#        print T
#        T -= 1;
    
    return Score



T = int(raw_input());
for i in range(T):
    print "Case #%d:" % (i+1),;
    N = int(raw_input());
    Hand = [];  
    for i in range(N):
        Hand.append( map(int, raw_input().split()) );
    M = int(raw_input());
    Deck = [];  
    for i in range(M):
        Deck.append( map(int, raw_input().split()) );

    print Solve(Hand, Deck);   
#    print N, List;
    
