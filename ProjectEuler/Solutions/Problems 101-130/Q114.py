N = 50;         DP = [0]*(N+2);         DP[0] = 1;      
for L in range(1,N+2):
    DP[L] = DP[L-1];
    b = 4;
    while (b <= L):
        DP[L] += DP[L-b];
        b += 1

print DP[N+1]
