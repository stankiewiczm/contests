from numpy import *

def Solve():
    [N,M] = map(int, raw_input().split());
    DATA = [];
    for k in range(M):
        L = raw_input().split();
        L.append(0);
        DATA.append( [ int(L[0])-1, L[1], int(L[2])-1, int(L[3])-1] );

    TRUTH = zeros(N,int);
    LIARS = zeros(N,int);
    for case in range(2**N):
        tmp = case;
        TEST = [];
        Valid = True;
        for k in range(N):
            TEST.append(tmp%2);
            tmp /= 2;
#        print TEST,;
        for m in range(M):
            i = DATA[m][0];
            j = DATA[m][2];
            k = DATA[m][3];

            if (DATA[m][1] == 'T'):
                if (TEST[i] != TEST[j]):
                    Valid = False;
            if (DATA[m][1] == 'L'):
                if (TEST[i] == TEST[j]):
                    Valid = False
            if (DATA[m][1] == 'D'):
                if (TEST[j] != TEST[k]) and (TEST[i] == 0):
                    Valid = False;
                if (TEST[j] == TEST[k]) and (TEST[i] == 1):
                    Valid = False;
            if (DATA[m][1] == 'S'):
                if (TEST[j] != TEST[k]) and (TEST[i] == 1):
                    Valid = False;
                if (TEST[j] == TEST[k]) and (TEST[i] == 0):
                    Valid = False;
#            if (not Valid):
#                break;
#        print Valid;
        if Valid:
            for k in range(N):
                if TEST[k] == 1:
                    TRUTH[k] += 1;
                else:
                    LIARS[k] += 1;
                    
    for k in range(N):
        if ((TRUTH[k] > 0) and (LIARS[k] > 0)):
            print '-',
        if ((TRUTH[k] > 0) and (LIARS[k] == 0)):
            print 'T',
        if ((TRUTH[k] == 0) and (LIARS[k] > 0)):
            print 'L',
            
    print ""
#    print "\n",DATA;



T = int(raw_input());
for t in range(T):
    print "Case #%d:" % (t+1),
    Solve();
