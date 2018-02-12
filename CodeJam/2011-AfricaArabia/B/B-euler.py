from numpy import *

FILE = open("B-large.in","r");
#FILE = open("B-sample", "r");

def Connected(N, R, Road):   
    OK = [];
    for i in range(N):
        OK.append( [0]*N );
        OK[i][i] = 1;
    for e in Road:
        OK[e[0]][e[1]] = 1;
        OK[e[1]][e[0]] = 1;         # Direct connections established

    news = 1;
    while (news > 0):
        news = 0;
        for i in range(N):                  # Connections to i
            if sum(OK[i] > 1):
                for j in range(N):              # From i connected to j
                    if (OK[i][j] == 1) and (i != j):
                        for k in range(N):          # And j connected to k
                            if (OK[j][k] == 1) and (OK[i][k] == 0):
                                OK[i][k] = 1;
                                OK[k][i] = 1;
                                news += 1;

    TODO = range(N);
    Islands = [];

    for i in range(N):
        if (i in TODO):
            if sum(OK) == 1:
                Islands.append([i]);
                TODO.remove(i);
            else:
                small = [i];
                for j in range(i+1,N):
                    if OK[i][j] == 1:
                        small.append(j);
                        TODO.remove(j);
                Islands.append(small)

#    print Islands
    for i in range(len(Islands)-1, -1, -1):
        if len(Islands[i]) == 1:
            Islands.pop(i);

    return Islands


N = int(FILE.readline());
for k in range(N):          # Each of the N cases:
    print "Case #%d:" %(k+1),
    N = int(FILE.readline());
    R = int(FILE.readline());
    Deg = [0]*N;
    Road = [];
    for i in range(R):
        Road.append( map(int, FILE.readline().split() ) );
        Deg[Road[-1][0]] += 1;
        Deg[Road[-1][1]] += 1; 

    for n in range(N-1, -1, -1):
        if Deg[n] == 0:
            N -= 1;
            for r in Road:
                if r[0] > n:
                    r[0] -= 1;
                if r[1] > n:
                    r[1] -= 1;

    Deg = [0]*N;
    for i in range(R):
        Deg[Road[i][0]] += 1;
        Deg[Road[i][1]] += 1; 

    Islands = Connected(N, R, Road);
    Odds = [];
    for isle in Islands:
        Odds.append(0);
        for n in isle:
            if Deg[n]%2 == 1:
                Odds[-1] += 1;
        if Odds[-1] < 2 and len(Islands) > 1:
            Odds[-1] += 2;

#    print Deg        
#    print Odds
    print sum(Odds)/2;

    
#    PlusRoads = 0;
    


