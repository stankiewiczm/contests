def IsNotP(n):
    k = 3;      n2 = int(n**0.5);
    while (k <= n2):
        if n%k == 0:
            return True;
        k += 2;
    return False;


Ans = [];        n = 3;
while (len(Ans) < 25):
    n += 2;
    if IsNotP(n) and n%3 != 0:
        if pow(10,n-1,n) == 1:
            Ans.append(n);
print sum(Ans)
