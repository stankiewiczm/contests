from numpy import *

# Question 2 of facebook hacker cup round 1


def Can(s1, s2):
    for w in range(len(s1)):
        if (s1[w] != '?') and (s2[w] != '?') and (s1[w] != s2[w]):
            return False;
    return True
    

def Try(m, K1, K2):
    DONE1 = [0]*m;
    DONE2 = [0]*m;
    Hits1 = [0]*m;
    Hits2 = [0]*m;

    MAP = [];
    for i in range(m):
        MAP.append([0]*m);
        for j in range(m):
            if Can( K1[i], K2[j] ):
                MAP[i][j] = 1;          # K1[i] matches to K2[j]
                Hits1[i] += 1;
                Hits2[j] += 1;

    while sum(DONE1) != m:
        for i in range(m):
            if DONE1[i] == 0:
              if Hits1[i] == 0:
                return 'IMPOSSIBLE'     # Unmatched node cannot be matched
            if DONE2[i] == 0:
              if Hits2[i] == 0:
                return 'IMPOSSIBLE'

        

    return 1


T = int(raw_input());
for q in range(1, T+1):
    m = int(raw_input());
    k1 = raw_input();       K1 = []
    k2 = raw_input();       K2 = []
    l = len(k1)/m;
    for i in range(m):
        K1.append( k1[i*l : (i+1)*l] );
        K2.append( k2[i*l : (i+1)*l] );

    print 'Case #%i: %i' % (q, Try(m, K1, K2))
    print K1, K2,'\n'
        
