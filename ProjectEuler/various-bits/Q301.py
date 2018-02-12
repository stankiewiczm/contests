import time;

T0 = time.time();
N = 2**30;      Ans = 0;        i = 0;
while (i < N):
    i += 1
    K = i^(i<<1)^(i+(i<<1))
    Ans += (K == 0)
print Ans, time.time()-T0,'s'

# 15 minutes run time
# 2178309 -- The 32nd Fibonacci number...

#It's easy to see that nim sum equals 0
#iff every "1" in binary representation of n is followed by "0".
#So, n must be built of "0" and "01" blocks and there are
#1+∑Fibi, i=0..30 = Fib31 such ns.
