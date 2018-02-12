def IsPal(N):
    if (N > 100000):
        if (N%10) == N/100000:
            if (N/10)%10 == (N/10000)%10:
                if (N/100)%10 == (N/1000)%10:
                    return True;
    return False
    

MAX = 0;
for n1 in range(100,1000):
    for n2 in range(100000/n1,n1):
        if (n1*n2 > MAX) and IsPal(n1*n2):
            MAX = n1*n2;
print MAX;

