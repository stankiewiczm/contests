T = int(raw_input());
for q in range(T):
    print "Case #%d:" % (q+1),
    N = int(raw_input());
    ooks = map(int, raw_input().split());
    if (sum(ooks)%N != 0):
        print "IMPOSSIBLE";
    else:
        ideal = sum(ooks)/N;
        moved = 0;
        for ook in ooks:
            moved += abs(ideal - ook);
        print moved/2;
