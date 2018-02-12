def Move( inp ):
    [R,C,D] = inp;
    if D == 'U':
        return [R-1,C,D];
    if D == 'D':
        return [R+1,C,D];
    if D == 'R':
        return [R,C+1,D];
    if D == 'L':
        return [R,C-1,D];
        
def Name( n ):
    DIG = [' ', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth',
           'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth',
           'twentieth', 'twenty-first', 'twenty-second', 'twenty-third', 'twenty-fourth', 'twenty-fifth', 'twenty-sixth', 'twenty-seventh', 'twenty-eighth', 'twenty-ninth',
           'thirtieth', 'thirty-first', 'thirty-second', 'thirty-third', 'thirty-fourth', 'thirty-fifth', 'thirty-sixth', 'thirty-seventh', 'thirty-eighth', 'thirty-ninth',
           'fortieth', 'forty-first', 'forty-second', 'forty-third', 'forty-fourth', 'forty-fifth', 'forty-sixth', 'forty-seventh', 'forty-eighth', 'forty-ninth',
           'fiftieth', 'fifty-first', 'fifty-second', 'fifty-third', 'fifty-fourth', 'fifty-fifth', 'fifty-sixth', 'fifty-seventh', 'fifty-eighth', 'fifty-ninth',
           'sixtieth', 'sixty-first', 'sixty-second', 'sixty-third', 'sixty-fourth', 'sixty-fifth', 'sixty-sixth', 'sixty-seventh', 'sixty-eighth', 'sixty-ninth',
           'seventieth', 'seventy-first', 'seventy-second', 'seventy-third', 'seventy-fourth', 'seventy-fifth', 'seventy-sixth', 'seventy-seventh', 'seventy-eighth', 'seventy-ninth',
           'eightieth', 'eighty-first', 'eighty-second', 'eighty-third', 'eighty-fourth', 'eighty-fifth', 'eighty-sixth', 'eighty-seventh', 'eighty-eighth', 'eighty-ninth',
           'ninetieth', 'ninety-first', 'ninety-second', 'ninety-third', 'ninety-fourth', 'ninety-fifth', 'ninety-sixth', 'ninety-seventh', 'ninety-eighth', 'ninety-ninth', 'hundredth'];
    return DIG[n];
           

def Texty( v1, v2 ):
    # moving from v1 to v2, then turning:
#    print v1, v2
    EoR = False;
    EoR = EoR or ((v1[2] == 'R') and (Map[v2[0]][v2[1]+1] != '.')); # Moving right, end of road?
    EoR = EoR or ((v1[2] == 'L') and (Map[v2[0]][v2[1]-1] != '.')); # Moving left, end of road?
    EoR = EoR or ((v1[2] == 'U') and (Map[v2[0]-1][v2[1]] != ':')); # ...
    EoR = EoR or ((v1[2] == 'D') and (Map[v2[0]+1][v2[1]] != ':')); # ...

    TR = False;
    TR = TR or ( (v1[2]=='R') and (v2[2] == 'D'));
    TR = TR or ( (v1[2]=='D') and (v2[2] == 'L'));
    TR = TR or ( (v1[2]=='L') and (v2[2] == 'U'));
    TR = TR or ( (v1[2]=='U') and (v2[2] == 'R'));
    if TR:
        DIR = 'right';
    else:
        DIR = 'left'

    if EoR:
        print 'Turn '+DIR+' at the end of the road'
    else:
        # Calculate the Nth turn thingy
        if v1[0] == v2[0]:                              # First horizontals
            N = 0;
            d = (v2[1]-v1[1])/abs(v2[1]-v1[1]);
            c = v1[1];
            while (c != v2[1]):
                c += d;
                if Map[v1[0]][c] == '#':
                    N += 1;
        else:
            N=0;
            d = (v2[0]-v1[0])/abs(v2[0]-v1[0]);         # Now verticals
            c = v1[0];
            while (c != v2[0]):
                c += d;
                if Map[c][v1[1]] == '#':
                    N += 1;
            
        print 'Take the '+Name(N)+' '+DIR;

    return

    
T = int(raw_input());           maxW = 100;
for q in range(T):
    print "Case #%d:" % (q+1);
    L = int(raw_input());       R = 0;
    Map = [' '*(maxW+2)];
    for i in range(L):
        Map.append( ' '+raw_input()+' '*(maxW) );
    Map.append(' '*(maxW));
    
    for y in range(len(Map)):
        if '~' in Map[y]:
            x = Map[y].index('~');
            if Map[y][x-1] in ['-','#']:
                d = 'L';
            else:
                d = 'R';
            Start = [y,x, d];
            
        if 'I' in Map[y]:
            x = Map[y].index('I');
            if Map[y-1][x] in ['|','#']:
                d = 'U';
            else:
                d = 'D';
            Start = [y,x,d];

    Path = [Start];
    Fin = False;
    while not Fin:
        [row, col, Dir] = Move(Path[-1]);
#        print [row, col, Dir]
        
        if Map[row][col] == '#':        # Need to figure out new direction
            Maybe = [];
            if (Map[row-1][col] == '|'):
                Maybe.append( 'U' );
            if (Map[row+1][col] == '|'):
                Maybe.append( 'D' );
            if (Map[row][col+1] == '-'):
                Maybe.append( 'R' );
            if (Map[row][col-1] == '-'):
                Maybe.append( 'L' );

            if (Dir == 'U') and ('D' in Maybe):
                Maybe.remove('D');
            if (Dir == 'D') and ('U' in Maybe):
                Maybe.remove('U');
            if (Dir == 'R') and ('L' in Maybe):
                Maybe.remove('L');
            if (Dir == 'L') and ('R' in Maybe):
                Maybe.remove('R');

#            if len(Maybe) != 1:
#                print 'Well this is problematic';
            Dir = Maybe[0];

        else:                       # See if we're done
            if (Dir == 'U') and (Map[row-1][col] not in ['|','#']):
                Fin = True;
            if (Dir == 'D') and (Map[row+1][col] not in ['|','#']):
                Fin = True;

            if (Dir == 'L') and (Map[row][col-1] not in ['-','#']):
                Fin = True;
            if (Dir == 'R') and (Map[row][col+1] not in ['-','#']):
                Fin = True;
            
        Path.append([row,col,Dir]);

############ At this point in time we should have the point-to-point path
############ Now need to convert it to directions

    Path2 = [Path[0]];
    for i in range(1, len(Path)-1):
        if Path[i][2] != Path[i-1][2]:
            Path2.append( Path[i] );
    Path2.append(Path[-1]);
    # Path2 should contain the vertices of the path
        
    if Path2[0][2] == 'R':
       print 'Head east';
    if Path2[0][2] == 'L':
       print 'Head west';
    if Path2[0][2] == 'U':
       print 'Head north';
    if Path2[0][2] == 'D':
       print 'Head south';

    for i in range(1, len(Path2)-1):            # Directions
        Texty( Path2[i-1], Path2[i] );

    # And reaching the destination:
    END = Path2[-1];
#    print END
    MM = (END[2] == 'R') and (Map[END[0]][END[1]+1] in ['.','+']);
    MM = MM or ((END[2] == 'L') and (Map[END[0]][END[1]-1] in ['.','+']));
    MM = MM or ((END[2] == 'U') and (Map[END[0]-1][END[1]] in [':','+']));
    MM = MM or ((END[2] == 'D') and (Map[END[0]+1][END[1]] in [':','+']));

    if MM:
        dX = abs(Path2[-1][0]-Path2[-2][0]) + abs(Path2[-1][1]-Path2[-2][1]) 
        print 'Continue for',50*dX,'metres'
    else:
        print 'Continue to the end of the road';
    print 'Stop\n'
                


#
#    for row in Map:
#        print row[0:50]
#    print Path2
