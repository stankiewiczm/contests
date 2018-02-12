MAX = 300000;    Prime = [1,2];     NP = 0;  

def Gen():
    IsP = [1]*MAX;                IsP[1] = 0;
    for i in range(2,MAX/2):
        IsP[2*i] = 0;
    n = 3;
    while (n < MAX):
        if (IsP[n] == 1):
            Prime.append(n);
            for i in range(2,(MAX-1)/n+1):
                IsP[n*i] = 0;
        n += 2;
    return len(Prime);


Gen();      LIM = 10**10;        n = 1;
while (2*n*Prime[n] < LIM):
    n += 2;
print n
