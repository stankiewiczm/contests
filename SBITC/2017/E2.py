def Fill(grid, r0, c0):
    regions = [];
    
    size = 0;
    Todo = [500*r0 + c0];
    Done = [False] * 201000;
    while len(Todo) > 0:
        ij = Todo.pop(0);
        if not Done[ij]:
            Done[ij] = True;
            size += 1;
            r = ij/500;
            c = ij%500;

            if grid[r-1][c] == '.':
                Todo.append(ij - 500);
            if grid[r+1][c] == '.':
                Todo.append(ij + 500);
            if grid[r][c-1] == '.':
                Todo.append(ij - 1);
            if grid[r][c+1] == '.':
                Todo.append(ij + 1);

    return size


T = int(raw_input());
for q in range(T):
    [R, C] = map(int, raw_input().split());
    data = [['#'] * (C+2)]
    for i in range(R):
        data.append( ['#'] + list(raw_input()) + ['#']);
    data.append( ['#']*(C+2) );
    
    print "Case #%d:" % (q+1),;

    results = [];
    for r in range(1, R+1):
        for c in range(1, C+1):
            if (data[r][c] == '#'):
                results.append(Fill(data, r, c));
    print max(results);
        
#    for row in data:
#        print row;
