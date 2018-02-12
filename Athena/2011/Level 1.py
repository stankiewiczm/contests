from numpy import *

def Q1(n):
    A = [];
    for i in range(n+1):
        A.append([]);
        for j in range(n+1):
            A[i].append(0L)
    A[0][0] = 1L;
    for c in range(1,n+1):
        for r in range(n+1):
            A[c][r] = A[c-1][r]
            if r <= c:
                A[c][r] += A[c][r-1];
    return A[n][n]


def C(n,r):
    R = 1L;
    for k in range(r):
        R = (R*(n-k))/(k+1);
    return R

def Q2(n):
    Paths = 0L;
    for steps in range(n,2*n+1):
        diag = 2*n-steps;
        UD = steps-diag;
        Paths += C(steps,diag) * C(UD,UD/2);
    return Paths-1


print "Q1:",Q1(1000)
print "Q2:",Q2(100)
print "Q3:", 2*pi
print "Q4:", 1
print "Q5:", 150**2+149**2
