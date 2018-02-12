def PrintGrid(data):
    for row in data:
        print ''.join(row);

def Solve(n, data):
    Grid = [];
    Extras = [];

    rowIllegals = [0]*n;
    colIllegals = [0]*n;
    diagIllegal = [0]*(2*n);
    offDIllegal = [0]*(2*n);
    
    for i in range(n):
        Grid.append(['.']*n);
    for row in data:
        symbol = row[0];
        x = int(row[1])-1;
        y = int(row[2])-1;
        Grid[x][y] = symbol;

        if (symbol == 'o' or symbol == 'x'):
            rowIllegals[x] += 1;
            colIllegals[y] += 1;

        if (symbol == 'o' or symbol == '+'):
            diagIllegal[x+y] += 1;
            offDIllegal[n+x-y] += 1;        

    for x in range(n):
        for y in range(n):
            if Grid[x][y] == '.':
                canCross = (rowIllegals[x] == 0 and colIllegals[y] == 0)
                canPlus = (diagIllegal[x+y] == 0 and offDIllegal[n+x-y] == 0)

                if (canPlus and canCross):
                    Grid[x][y] = 'o';
                    Extras.append(['o', x+1, y+1]);
                    rowIllegals[x] = 1;
                    colIllegals[y] = 1;
                    diagIllegal[x+y] = 1;
                    offDIllegal[n+x-y] = 1;
                if (canPlus and not canCross):
                    Grid[x][y] = '+';
                    Extras.append(['+', x+1, y+1]);
                    diagIllegal[x+y] = 1;
                    offDIllegal[n+x-y] = 1;
                if (not canPlus and canCross):
                    Grid[x][y] = 'x';
                    Extras.append(['x', x+1, y+1]);
                    rowIllegals[x] = 1;
                    colIllegals[y] = 1;                    

    for x in range(n):
        for y in range(n):
            if Grid[x][y] == '+':
                canCross = (rowIllegals[x] == 0 and colIllegals[y] == 0)
                if (canCross):
                    Grid[x][y] = 'o';
                    Extras.append(['o', x+1, y+1]);
                    rowIllegals[x] = 1;
                    colIllegals[y] = 1;

            if Grid[x][y] == 'x':
                canPlus = (diagIllegal[x+y] == 0 and offDIllegal[n+x-y] == 0)
                if (canPlus):
                    Grid[x][y] = 'o';
                    Extras.append(['o', x+1, y+1]);
                    diagIllegal[x+y] = 1;
                    offDIllegal[n+x-y] = 1;

    TotalValue = 0;
    for x in range(n):
        for y in range(n):
            if Grid[x][y] == '+' or Grid[x][y] == 'x':
                TotalValue += 1;
            if Grid[x][y] == 'o':
                TotalValue += 2;
    
    print TotalValue, len(Extras);
    for row in Extras:
        print row[0], row[1], row[2]
    return;


T = int(raw_input());
for q in range(T):
    [N, M] = map(int, raw_input().split());
    Data = [];
    for i in range(M):
        Data.append(raw_input().split());

    print "Case #%d:" % (q+1),;
    Solve(N, Data);
