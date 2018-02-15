def Bounce(direct):
    d = direct;     # 0 left, 1 up, 2 right, 3 down
    x = R;
    y = C;
    time = 1;

    Map = [];
    for i in range(N+2):
        Map.append( [0]*(M+2) );
    Map[x][y] = 1;

    while time < 2*M*N:
        if d == 0:          # moving left
          x -= 1;
          if Data[x][y] == '/':
            d = 3;
          if Data[x][y] == chr(92):
            d = 1;
        else:
          if d == 2:          # moving right
            x += 1;
            if Data[x][y] == '/':
                d = 1;
            if Data[x][y] == chr(92):
                d = 3;
          else:
            if d == 1:          # moving up
              y -= 1;
              if Data[x][y] == '/':
                d = 2;
              if Data[x][y] == chr(92):
                d = 0;
            else:
              if d == 3:          # moving down
                y += 1;
                if Data[x][y] == '/':
                  d = 0;
                if Data[x][y] == chr(92):
                  d = 2;
              else:
                 print 'WTF', d;

        if Data[x][y] == 'C':
            return time;
        else:
            time += 1;
            Map[x][y] += 1;

    return 'Voyager';
            

[N,M] = map(int, raw_input().split());
Data = ['C'*(M+2)];
for i in range(N):
    Data.append( 'C'+raw_input().split()[0]+'C' );
Data.append( 'C'*(M+2) );
[R,C] = map(int, raw_input().split());

Best = 0;
DIR = ['U', 'L', 'D', 'R'];
for i in [0,3,2,1]:
    run = Bounce(i);
    if run > Best:
        Best = run;
        BestD = DIR[i];
#if Best == 10000000:
#    Best = 'Voyager'

print BestD,'\n',Best
