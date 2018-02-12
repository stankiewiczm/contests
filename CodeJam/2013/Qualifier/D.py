def DFS(path, todo, key):
#    print path, todo, key, Chest;

    if len(todo) == 0:
        return ['GOOD', []];

    for e in todo:
        Use = Chest[e][0];
        if Use in key:
            NewTodo = [];            K2 = [];
            for el in todo:
                if e != el:
                    NewTodo.append(el);
            for k in key:
                K2.append(k);
                
#            print [e], 'Keys', key, K2
            K2.remove(Use);
            K2 += Chest[e][2:]

            RET = DFS( path+[e], NewTodo, K2 );
            if RET != 'FAIL':
                return ['GOOD', [e]+RET[1]];

#            print e, Use, RET
                
#    print 'Failed at ', path, todo, key,'\n'    
    return 'FAIL';
    


T = int(raw_input());
for q in range(T):
    print "Case #%d:" %(q+1),
    
    [K,N] = map(int, raw_input().split());
    Keys = map(int, raw_input().split());
    Chest = [];
    for r in range(N):
        Chest.append( map(int, raw_input().split()) );

    OUT = DFS( [], range(N), Keys );
    if OUT[0] == 'GOOD':
        for n in OUT[1]:
            print n+1,
        print
    else:
        print 'IMPOSSIBLE'
#    print 'OUT = ', DFS( [], range(N), Keys )
    
        
