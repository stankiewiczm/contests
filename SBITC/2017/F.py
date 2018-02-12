T = int(raw_input());
for q in range(T):
    print "Case #%d:" % (q+1);

    [sources, zoos] = map(int, raw_input().split());
    strength = [];
    booze = [];
    ppl = [];
    for i in range(sources):
        booze.append(map(int, raw_input().split()));
        strength.append( (100.*booze[-1][0]) / booze[-1][1] );

    maxIndex = strength.index(max(strength));
    minIndex = strength.index(min(strength));

    a1 = booze[maxIndex][0];
    b1 = booze[maxIndex][1];

    a2 = booze[minIndex][0];
    b2 = booze[minIndex][1];

    vol1 = a1 + b1;
    vol2 = a2 + b2;

    for j in range(zoos):
        [c, d] = map(int, raw_input().split());

        if c*b1 > a1*d or c*b2 < a2*d:
            print "NO"
        else:
            print "YES", #(c, d)
            
            ans = [0]*sources;
            if (a2 * d == b2 * c):
                totA = a2;
                totB = b2;
                ans[minIndex] = vol2;
            else:
                totA = a1;
                totB = b1;
                ans[maxIndex] = vol1;

            while (totA * d != totB * c):
                if (totA * d < totB * c):
                    totA += a1;
                    totB += b1;
                    ans[maxIndex] += vol1;
                if (totA * d > totB * c):
                    totA += a2;
                    totB += b2;
                    ans[minIndex] += vol2;
#            print (totA, totB), (a1, b1), (a2, b2), ans;
            
            for a in ans:
                print a,
            print 
