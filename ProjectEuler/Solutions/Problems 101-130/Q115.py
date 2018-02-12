def Count(m, N):
    DP = [0]*(N+2);         DP[0] = 1;      
    for L in range(1,N+2):
        DP[L] = DP[L-1];
        b = m+1;
        while (b <= L):
            DP[L] += DP[L-b];
            b += 1

    return DP[N+1]

m = 50;     n = m+1;        LIM = 10**6;
while (Count(m,n) < LIM):
    n += 1;
print n
