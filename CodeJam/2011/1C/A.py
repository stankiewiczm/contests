def PrintList( Matrix ):
    for row in Matrix:
        s = '';
        for c in row:
            s += c;
        print s
    return

def Solve( Mat , R,C):
    NB = 0;
    for row in Mat:
        for c in row:
            if c == '#':
                NB += 1;

    for i in range(R-1):
        for j in range(C-1):
            if Mat[i][j] == Mat[i+1][j] == Mat[i][j+1] == Mat[i+1][j+1] == '#':
                Mat[i][j] = '/'
                Mat[i+1][j] = chr(92)
                Mat[i][j+1] = chr(92)
                Mat[i+1][j+1] = '/'
                NB -= 4;

    if NB != 0:
        print "Impossible"
    else:
        PrintList(Mat);
    return


T = int(raw_input());
for i in range(T):
    print "Case #%d:" % (i+1);
    [R, C] = map(int, raw_input().split());

    DATA = [ list(raw_input()) for i in range(R) ];

    Solve(DATA, R,C);
