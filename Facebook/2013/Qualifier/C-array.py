def Init(inp, K):
    [a,b,c,r] = inp;
    m = [0]*K;      m[0] = a;
    for i in range(1, K):
        m[i] = (b*m[i-1]+c)%r
    return m

T = int(raw_input());
for case in range(1, T+1):
    [N,K] = map(int, raw_input().split());
    M = Init(  map(int, raw_input().split()), K );

# The list will consist of some initial configuration, and then of subsequences
# length K of the numbers 0 to K-1 in some order.
# After the initial K numbers, no number >= K will ever be added again
# Only the terms K to 2K-1 need be calculated.
# Then M[N] = M[N%K+K].

    First = [];
    Hits = [0]*(K+1)
    for i in M:
        if i < K+1:
            First.append(i);
            Hits[i] += 1;           # Hits stores the multiplicity of K-elements
    Needs = [];
    for j in range(K+1):
        if Hits[j] == 0:
            Needs.append(j);

    for i in range(K+2):            # Remove element m[i], add element m[i+K];
        M.append( Needs.pop(0) );
        Hits[M[-1]] += 1;
        if M[i] < K+1:
            Hits[M[i]] -= 1;        

        if M[i] < K+1:              # Element removed small
            if Hits[M[i]] == 0:     # and not in last K entries
                Needs.append( M[i] );
                Needs.sort()

    print 'Case #%i: %i' %(case, M[(N-1)%(K+1)+(K+1)])

