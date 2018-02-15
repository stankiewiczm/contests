def CheckSquare(n):
    NonTriv = [];
    ANS = 'YES';
    for r in range(N):
        line = raw_input().split()[0];
        if '#' in line:
            if len(NonTriv) != 0:
                if line != shape:
                    ANS = 'NO';
            else:
                shape = line;
            NonTriv.append(r)

    if len(NonTriv) == 0:
        return 'NO';

    Nlines = NonTriv[-1]-NonTriv[0]+1
    if  Nlines!= len(NonTriv):
        return 'NO';

    Cols = [];
    for i in range(len(shape)):
        if shape[i] == '#':
            Cols.append(i);
    Ncols = Cols[-1]-Cols[0]+1;
    if Ncols != len(Cols):
        return 'NO';
    if Nlines != Ncols:
        return 'NO';
    
    return ANS
    

T = int(raw_input());
for q in range(T):
    N = int(raw_input());
    print "Case #%d: %s" % (q+1, CheckSquare(N));
    

