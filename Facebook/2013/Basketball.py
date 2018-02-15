from numpy import *

def GetNumbers(n, m, p):        # n people, m minutes, p at a time
    t = 0;
    team = array([1]*p + [0]*(n-p), int);        # Cumulative timings.
#    print team, ;
    for t in range(m):
        Tmin = min(team);
        newteam = zeros(n, int);
        # First add new players:
        NewP = 0;
        for i in range(n):
            if team[i] == Tmin and (NewP < p):
                newteam[i] = 1;
                NewP += 1;
        # Now keep old players
        for i in range(n):
            if newteam[i] == 0 and (NewP < p):
                newteam[i] = 1;
                NewP += 1;

#        print team, newteam, team+newteam ;
        team += newteam
    return newteam;
                

T = int(raw_input());
DATA = [];
for q in range(T):
    [N,M,P] = map(int, raw_input().split());
    for r in range(N):
        line = raw_input().split();
        DATA.append( [line[1], line[2], line[0]] );
    DATA.sort()
    Team1 = [];     Team2 = [];     Curr = 1;
    while DATA != []:
        if Curr == 1:
            Team1.append( DATA.pop(-1) );
            Curr = 2;
        else:
            Team2.append( DATA.pop(-1) );
            Curr = 1;

#    print Team1
#    print Team2,'\n'
    T1 = GetNumbers( len(Team1), M, P )
    T2 = GetNumbers( len(Team2), M, P )
#    print len(Team1), M, GetNumbers( len(Team1), M, P )
#    print len(Team2), M, GetNumbers( len(Team2), M, P )
    ANS = [];
    for i in range(len(T1)):
        if T1[i] == 1:
            ANS.append( Team1[i][2] );
    for j in range(len(T2)):
        if T2[j] == 1:
            ANS.append( Team2[j][2] );
    ANS.sort();

#    print q+1, ANS
    print "Case #%d:" % (q+1),
    for name in ANS:
        print name,
    print 
    

