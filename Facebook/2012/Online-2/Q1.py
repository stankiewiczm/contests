from numpy import *

# Question 1 of facebook hacker cup round 2
# Removing roads and stuff


def FindCycles(n, Rlist):
    todo = [];
    for i in range(n):
        todo.append(i);

    RET  = [];
    while len(todo) != 0:
        cyc = [ todo.pop(0) ];
        Djk = [ cyc[-1] ];
        hit = [0]*N;
        hit[cyc[0]] = 1;
        while len(Djk) != 0:
#            print cyc, Djk, todo
            curr = Djk.pop(0);
            for e in Rlist[curr]:
                if hit[e] == 0:
                    hit[e] = 1;
                    cyc.append(e);
                    Djk.append(e);
                    todo.remove(e);
        cyc.sort();
        RET.append( cyc );
#        print RET[-1]
    return RET
    
    

    

T = int(raw_input());
for i in range(T):
    [N, M, K] = map(int, raw_input().split());
    Road = [];
    Bool = [];
    List = [];
    harmless = [0]*N;
    for j in range(N):
        Bool.append( [0]*N );
        List.append( [] );
    for j in range(M):
        [p, q] = map(int, raw_input().split());
        Road.append( [p, q] );
        Bool[ p ][ q ] = 1;
        Bool[ q ][ p ] = 1;
        List[p].append(q);
        List[q].append(p);
    for j in range(K, N):
#        print j, harmless[j], Bool[j], K
        harmless[j] = sum( Bool[j][K:] )

#    for row in Bool:
#        print row;
#    print;
#    for row in List:
#        print row
#    print;

#    print harmless
    Cycle = FindCycles(N, List);

    ans = 0;
    for part in Cycle:
        if max(part) < K:
            ans += len(part)-1
        else:
            for e in part:
                if e < K:
                    ans += 2;
                else:
                    ans += harmless[e];
#    print ans, ans/2

#    if M-ans/2 < 0:
#        ans = 2*M

#    print N, M, K
#    print ans%2
    print 'Case #%i: %i' % (i+1, M-ans/2)
        
