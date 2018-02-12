from numpy import *

def SDig(n):
    R = 0;
    while (n > 0):
        R += n%10;
        n /= 10;
    return R;

    
LIM = 10**20;       Alist = [];
for n in range(2,181):
    m = n*n;
    while (m < LIM):
        if SDig(m) == n:
#            print m, n
            Alist.append(m);
        m *= n;
Slist = sort(Alist);
print Slist[29]
