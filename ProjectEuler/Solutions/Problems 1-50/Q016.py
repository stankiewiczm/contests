N = 2**1000;     SUM = 0;
while N > 0:
    SUM += N%10;
    N /= 10;
print SUM;
