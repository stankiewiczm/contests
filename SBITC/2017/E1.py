def Solve(grid):
    regions = [];
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                size = 0;
                Todo = [1000*i + j];
                while len(Todo) > 0:
                    ij = Todo.pop(0);
                    size += 1;
                    r = ij/1000;
                    c = ij%1000;

                    grid[r][c] = '#';
                    if grid[r-1][c] == '.':
                        if (ij-1000 not in Todo):
                            Todo.append(ij - 1000);
                    if grid[r+1][c] == '.':
                        if (ij+1000 not in Todo):
                            Todo.append(ij + 1000);
                    if grid[r][c-1] == '.':
                        if (ij-1 not in Todo):
                            Todo.append(ij - 1);
                    if grid[r][c+1] == '.':
                        if (ij+1 not in Todo):
                            Todo.append(ij + 1);

                regions.append(size);
    regions.sort();
    for reg in regions:
        print reg,
    print

T = int(raw_input());
for q in range(T):
    [R, C] = map(int, raw_input().split());
    data = [['#'] * (C+2)]
    for i in range(R):
        data.append( ['#'] + list(raw_input()) + ['#']);
    data.append( ['#']*(C+2) );
    
    print "Case #%d:" % (q+1),;
    Solve(data);
        
