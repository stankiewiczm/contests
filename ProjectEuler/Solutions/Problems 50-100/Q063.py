ANS = 0;

for a in range(1,10):
    n = 1;
    while (a**n >= 10**(n-1)):
        ANS += 1;
        n += 1;

print ANS;
