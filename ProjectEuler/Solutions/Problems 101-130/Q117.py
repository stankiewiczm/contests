N = 50;         DP = [0]*(N+1);         DP[0] = 1;      
for L in range(1,N+1):
    DP[L] = DP[L-1];
    b = 2;
    while (b <= L) and (b <= 4):
        DP[L] += DP[L-b];
        b += 1

print DP[-1]
