def Evaluate(dice, values):
    score = 0.;
    for line in values:
        mult = 10;
#        print line, dice
        for j in range(M):
            if (line[j] != 0):
                mult = min(mult, dice[j]/line[j]);
        score += mult * line[-1];
    return score;

def DieCounts(dice, M):
    ret = [0]*M;
    for d in dice:
        ret[d-1] += 1;
    return ret;

def Binary(N):
    List = [];
    for i in range(2**N):
        item = [];
        for j in range(N):
            item.append([i%2]);
            i /= 2;
        List.append(item);
    return List;    

Bins = [[], [[0],[1]]]
Bins.append(Binary(2));
Bins.append(Binary(3));
Bins.append(Binary(4));
Bins.append(Binary(5));
Bins.append(Binary(6));

T = int(raw_input());
for q in range(T):
    print "Case #%d:" % (q+1),
    [N,M,P] = map(int, raw_input().split());
    Dice = map(int, raw_input().split());
    DieCount = DieCounts(Dice, M);
    Value = [];
    for i in range(P):
        Value.append(map(int, raw_input().split()));

    BestScore = 0.;
    for roll in Bins[N]:
        ## Now rolling subset of dice
        ## Evaluate it's score

        Nroll = M**sum(roll);
        Mrange = range(1, M+1);

        

        range1 = [Dice[1]];
        
        


        

#    print Dice, Value
    print Evaluate(DieCount, Value);
