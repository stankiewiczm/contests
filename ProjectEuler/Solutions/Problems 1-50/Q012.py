from numpy import *

P = [2,3,5,7,11,13,17,19,23,29];

def Fact(n0):
    power = zeros(10, int);
    for k in range(10):
        while (n0%P[k] == 0):
            n0 /= P[k];
            power[k] += 1;
    
    F = 1;
    if (n0 > 1):
        F = 2;

    for k in range(10):
        F *= (power[k]+1)
    return F;


for n in range(1,10000):
    fact1 = Fact(n)*Fact(2*n+1);        # for 2n  (even)
    fact2 = Fact(2*n+1)*Fact(n+1);      # for 2n+1 (odd)
    if (fact1 > 100):
        print 2*n, n*(2*n+1), fact1;
        break;
    if (fact2 > 100):
        print 2*n+1, (n+1)*(2*n+1), fact2;
        break;
