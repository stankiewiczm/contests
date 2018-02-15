def Iterate(pzero, infected):
    ToDie = [0]*M;
    for p in pzero:
        for q in infected:
            ToDie[(p*q)%M] = 1;

    Ret = [];
    for i in range(M):
        if ToDie[i] == 1:
            Ret.append(i);
    return Ret;
    

[K, M, N] = map(int, raw_input().split());
Pzero = map(int, raw_input().split());
T = 1;

Inf = [ [], Pzero ];

for i in range(min(500, K)):
    Inf.append( Iterate(Pzero, Inf[-1]) );

if K <= 500:
    for k in Inf[K]:
        print k,
    print '';

else:       # Try find a pattern...
    Awesome = False;
    j = 499;
    while (j > 0) and (not Awesome):
        if Inf[j] == Inf[500]:
            Awesome = True;
            Period  = 500-j;
            j -= 1;

    if Awesome:         # There is a pattern!
        steps = (K-500)/period;
        newK = K-steps*period;
        while newK > 500:
            newK -= period;
        for k in Inf[newK]:
            print k,
        print ''

    else:
        for k in Inf[478]:
            print k,
        print '';
        
    
    
    
