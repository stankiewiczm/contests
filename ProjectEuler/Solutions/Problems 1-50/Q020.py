N = 1;          SUM = 0;
for k in range(2,101):
    N *= k;

while N > 0:
    SUM += N%10;
    N /= 10;

print SUM;
