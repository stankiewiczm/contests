T = int(raw_input());
for q in range(T):
    print "Case #%d:" % (q+1),
    N = int(raw_input());

    Data = [];
    Data.append([N, 1]);        # N fish, starting with #2 (#1 indexed from 0)

    while (Data[-1][0] != 1):
        n = Data[-1][0];
        p = Data[-1][1];

        if (n%2 == 0):
            Data.append( [n/2, p] );
        else:
            if (p == 1):
                Data.append( [n/2+1, 0] );
            else:
                Data.append( [n/2, 1] );

    Fish = 1;
    for i in range(len(Data)-2, -1, -1):
        Fish = 2*Fish - Data[i][1];

    print Fish
