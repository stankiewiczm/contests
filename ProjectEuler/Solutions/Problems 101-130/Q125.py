from numpy import *

def IsPalin(n0):
    n1 = n0;        n2 = 0;
    while (n1 > 0):
        n2 = 10*n2 + n1%10;
        n1 /= 10;
    return (n0 == n2)


SSq = [0,1];                    Ans = [];
for k in range(2,7101):
    SSq.append( SSq[-1]+k*k );
    
for a in range(2,len(SSq)):
    for b in range(a-1):
        n = SSq[a]-SSq[b];
        if (n < 10**8):
            if IsPalin(n):
                if n not in Ans:
                    Ans.append(n);

print sum(Ans)
