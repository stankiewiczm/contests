def Distribute(points, P):
    P = [1] + P;
    while points > 0 and min(P) < 1-1e-6:
        minP = min(P);
        nextLowest = 2;
        pmins = [];
        for i in range(len(P)):
            if P[i] == minP:
                pmins.append(i);
            else:
                if P[i] < nextLowest:
                    nextLowest = P[i];

        diff = nextLowest - minP;
        
        if diff*len(pmins) < points:
            points -= diff * len(pmins);
            for i in pmins:
                P[i] = nextLowest;
        else:
            for i in pmins:
                P[i] += points/len(pmins);
            points = 0;
                
#        print "---", P, minP, pmins, nextLowest;
            
    return P[1:]

T = int(raw_input());
for q in range(T):
    [N, K] = map(int, raw_input().split());
    U = float(raw_input());
    Pi = map(float, raw_input().split());
    Pi.sort();
    Pi.reverse();

    print "Case #%d:" % (q+1),
    P = Distribute(U, Pi[:K]) + Pi[K:];
    Ans = 1.
    for p in P:
        Ans *= p;
    print Ans

#    print "%.9f" % Solve(K, pancakes);

