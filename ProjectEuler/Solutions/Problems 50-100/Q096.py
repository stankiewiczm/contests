from numpy import *

def Print(board):
    print ' '
    for i in range(9):
      s = '';
      for j in range(9):
        if board[i][j] != 0:
          s += str(board[i][j]);
        else:
          s += chr(183);
      print s;
    print ' ';
    return;


def Verified(board):
    for i in range(9):
        Row = [1,0,0,0,0,0,0,0,0,0];        Col = [1,0,0,0,0,0,0,0,0,0];
        for j in range(9):
            Row[ board[i][j] ] += 1;        Col[ board[j][i] ] += 1;
        if (max(Row) != min(Row)) or (max(Col) != min(Col)):
            return 0;

        for Bx in range(3):
          for By in range(3):
            Hit = [1,0,0,0,0,0,0,0,0,0];
            for q in range(9):
              Hit[ board[3*Bx+q%3][3*By+q/3] ] += 1;
            if (max(Hit) != min(Hit)):
              return 0;
    return 1;
                                          

            
def ReadIn():
    Board = [[], [], [], [], [], [], [], [], []];
    n = int(F.readline().split()[1]);
    for k in range(9):
        Line = F.readline();
        for l in range(9):
            Board[k].append( int(Line[l]) );
    return Board;


def SDKcopy(From):
    To = [[], [], [], [], [], [], [], [], []];
    for i in range(9):
        for j in range(9):
            To[i].append(From[i][j]);
    return To;


def CellPoss(board, c):
    Bx = c[0]/3;     By = c[1]/3;
    Allow = [1,2,3,4,5,6,7,8,9];
    for i in range(9):
        if (board[c[0]][i] in Allow):
            Allow.remove( board[c[0]][i] );
        if (board[i][c[1]] in Allow):
            Allow.remove( board[i][c[1]] );
    for i in range(3):
        for j in range(3):
            if board[3*Bx+i][3*By+j] in Allow:
                Allow.remove( board[3*Bx+i][3*By+j] );
    return Allow;


def Solve(start):
    sdk = SDKcopy(start);       
    
    Progress = True;
    while (Progress):
        Progress = False;
        TODO = [];
        for i in range(9):
          for j in range(9):
            if sdk[i][j] == 0:
              TODO.append([i,j]);

        for cell in TODO:
            Allowed = CellPoss(sdk, cell)
            if len(Allowed) == 1:                       # A cell has a unique value
                Progress = True;
                AnyP = True;
                sdk[cell[0]][cell[1]] = Allowed[0];
#        """
            # A row has a unique place to insert a number
        for i in range(9):
            Need = [1,2,3,4,5,6,7,8,9];     Poss = [];
            Ins =  [1,2,3,4,5,6,7,8,9];
            for j in range(9):
                if sdk[i][j] in Need:
                    Need.remove(sdk[i][j]);
                else:
                    Poss.append( CellPoss(sdk, [i,j]));

            for n in Need:
                npos = 0;
                for p in Poss:
                    if n in p:
                        npos += 1;

                if npos == 1:               # Unique place for n in row i
                    for j in range(9):      # If n fits in column j
                       if (n in CellPoss(sdk, [i,j])) and (sdk[i][j] == 0):
                           sdk[i][j] = n;
                           Need.remove(n);
                           Progress = True;
                           AnyP = True;
#        """
        # END LOOP
    # THIS PART HAS FINISHED ALL THE DIRECT INPUTS                        

    if len(TODO) > 0:
        Gc = TODO[0];                   ## Guess a value
        CanDo = CellPoss(sdk, Gc);

        for v in CanDo:
            sdk = SDKcopy(start);
            sdk[Gc[0]][Gc[1]] = v;

            Ret = Solve(sdk);
            if Ret != 0:
#                print '. .',
                return Ret;

    [x,y,z] = sdk[0][0:3];
    if (len(TODO) == 0):
        if Verified(sdk) == 1:
            print  100*x+10*y+z,;
            return 100*x+10*y+z;

#    print '.',
    sdk = SDKcopy(start);

    return 0


F = open('../TXTdata/sudoku.txt');
Ans = zeros(50,int);            
for i in range(50):
    print '\nBoard #',i+1,
    Ans[i] = Solve(ReadIn()); 
    
print '\n\nSolved',sum(Ans != 0),'boards.  Total sum', sum(Ans)
