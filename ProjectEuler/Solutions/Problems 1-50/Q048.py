ANS = 0L;
for k in range(1,1001):
    ANS += k**k;
print ANS%10**10
