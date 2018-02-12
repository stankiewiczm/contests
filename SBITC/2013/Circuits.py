T = int(raw_input());
for q in range(T):
    N = int(raw_input());
    A = map(int, raw_input().split());
    B = map(int, raw_input().split());

    AL = [];
    for i in range(N):
        AL.append( [A[i], B[i]] );
    AL.sort();

    # Ai values are increasing
    # Bi values are increasing
    # Need to find the longest increasing sub-sequence of b_i
    Best = [1]*N;
    for i in range(N):
        for j in range(i):
            if (AL[i][1] > AL[j][1]) and (Best[j]+1 > Best[i]):
                Best[i] = Best[j]+1;

    print "Case #%d: %d" % (q+1, max(Best))

    
#    Grid = [];
#    Proj = [0]*N;
#    for i in range(N):
#        Grid.append( [0]*N );
#        
#    for i in range(N):              # Boolean map for crossings
#        for j in range(i):
#            if (A[i]-A[j])*(B[i]-B[j]) < 0:
#                Grid[i][j] = 1;
#                Grid[j][i] = 1;
#                Proj[i] += 1;
#                Proj[j] += 1;
#
#    # Just apply greedy -- I'm still not sure if this will work or not...
#    
#    Ans = N;
#    while sum(Proj) != 0:
#        k = Proj.index(max(Proj));      # Find worst offender
#        for i in range(N):
#            if Grid[i][k] == 1:
#                Grid[i][k] = 0;
#                Grid[k][i] = 0;
#                Proj[i] -= 1;
#                Proj[k] -= 1;
#        Ans -= 1;
#    
#    print "Case #%d: %d" % (q+1, Ans)
