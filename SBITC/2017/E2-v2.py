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

                    grid[r][c] = str(len(regions));
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

    fillValues = [];
    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[0])-1):
            if grid[r][c] == '#':
                neighs = [grid[r-1][c], grid[r+1][c], grid[r][c-1], grid[r][c+1]];
                regs = [];
                val = 1;
                for cell in neighs:
                    if cell != '#' and cell not in regs:
                        regs.append(cell);
                        val += regions[int(regs[-1])];
                fillValues.append(val);
#                print (r, c), regs, val
    print max(fillValues);

T = int(raw_input());
for q in range(T):
    [R, C] = map(int, raw_input().split());
    data = [['#'] * (C+2)]
    for i in range(R):
        data.append( ['#'] + list(raw_input()) + ['#']);
    data.append( ['#']*(C+2) );
    
    print "Case #%d:" % (q+1),;
    Solve(data);
       
