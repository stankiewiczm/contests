def TrySolve(n, R, O, Y, G, B, V):
    solved = False;
    for c in ['R', 'O', 'Y', 'G', 'B', 'V']:
        r = int(c == 'R');
        o = int(c == 'O');
        y = int(c == 'Y');
        g = int(c == 'G');
        b = int(c == 'B');
        v = int(c == 'V');

        ans = '' + c;
        done = 0;
        nxt = '';
        while (not Solved) and (done < N):
            red = r + o + v;
            yellow = y + o + g;
            blue = b + g + v;

            if (ans[-1] == 'O'):
                nxt = 'B';
                b += 1;
            if (ans[-1] == 'G'):
                nxt = 'R';
                r += 1;
            if (ans[-1] == 'V'):
                nxt = 'Y';
                y += 1;
                
            if (ans[-1] == 'R'):
                if (G - g > 0):
                    nxt = 'G'
                    g += 1
                else:
                    
            if (ans[-1] == 'Y'):
            if (ans[-1] == 'B'):
                
            most = max(red, yellow, blue);
        print N, red, yellow, blue;



T = int(raw_input());
for q in range(T):
    # Orange = Red + Yellow
    # Green = Yellow + Blue
    # Violet = Blue + Red
                
    [N, R, O, Y, G, B, V] = map(int, raw_input().split())

    red = R + O + V
    yellow = Y + O + G 
    blue = B + G + V

    print "Case #%d:" % (q+1),
    if 2*max(red, yellow, blue) > N:
        print "IMPOSSIBLE";
    else:
        TrySolve(N, R, O, Y, G, B, V)
    
