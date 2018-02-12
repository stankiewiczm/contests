def Count(N, m):
    DP = [0]*(N+1);         DP[0] = 1;      
    for L in range(1,N+1):
        DP[L] = DP[L-1];
        if (L >= m):
            DP[L] += DP[L-m]
    return DP[N]-1;           # Less the one without coloured squares

print Count(50,2)+Count(50,3)+Count(50,4);

