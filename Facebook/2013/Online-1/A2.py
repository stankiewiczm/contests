from numpy import *

# Question 1 of facebook hacker cup round 1
# Compressing statii

def C(n,k):
    R = 1;
    if k > n:
        return 0;
    if k == n:
        return 1
    for i in range(k):
        R = (R*(n-i))/(i+1);
        R = R%MOD
    return R
    



MOD = 1000000007;
T = int(raw_input());
for q in range(1, T+1):
    [N,K] = map(int, raw_input().split());
    a = map(int, raw_input().split());
    a.sort(reverse=True);

    ANS = 0;
#    print N, K, a
    for i in range(N-K+1):
        ANS += a[i] * C(N-i-1, K-1);

    print 'Case #%i: %i' % (q, ANS%MOD)
        
