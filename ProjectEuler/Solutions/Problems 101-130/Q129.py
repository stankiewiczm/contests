def Brute(p):
    if (p%3 != 0):
        N = [10];
        while (N[-1] != 1):
            N.append( (N[-1]*10)%p );
        return len(N);

    N = 1;      M = 1;      S = 1;
    while (S != 0):
        N += 1;
        M = (M*10)%p;
        S = (S+M)%p
    return N
    


n = 10**6+1;
while (True):
    if (n%5 != 0):
        if (Brute(n) > 10**6):
            print n;
            break;
    n += 2;
