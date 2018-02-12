def Phi(n):
    P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47];
    PH = n;
    for p in P:
        if (n%p == 0):
            PH = (PH*(p-1))/p;
    if (PH == n):
        PH = n-1;
    return PH;

def V(n):
    return (Phi(n)+0.)/(n-1);

N = 2*3*5*7*11*13*17*19*23;
LIM = 15499./94744;

m = 1;
while V(m*N) > LIM:
    print m, m*N, V(m*N);
    m += 1
print m, m*N, V(m*N);
