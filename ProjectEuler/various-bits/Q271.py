from numpy import *

def Gen(n):
    p = 2;      R = [];
    while (n > 1):
        if (n%p == 0):
            R.append(p);
            n /= p;
        else:
            p += 1;
    return R;
    

def roots(p):
    tot = [0]*p;
    for i in range(p):
        if (i**3)%p == 1:
            tot[i] = 1;
#    print p, sum(tot), tot;
    return sum(tot);


#S = 13082761331670030;
S = 13082761331670030;
#S = 91
#S = 2*3*5*7*11*13*17*19;
P = Gen(S);     F = [];
for p in P:
   F.append(roots(p)); 

print prod(F)-1
