from Numeric import *

Prime = zeros(400);    Prime[0] = 2;   Prime[1] = 3; AMAX = 5000;

def Generate():
    N = 3;
    NPrime = 2;
    while(NPrime < 400):
        N = N+2;
        Good = 1;
        for i in arange(NPrime):
            if (N%Prime[i] == 0):
                Good = 0;
                break;
        if (Good == 1):
            Prime[NPrime] = N;
            NPrime = NPrime + 1;
    return 0;
            

def SDivs(N):
    N0 = N;     P = 1;      Facts = ones(400);
    if (N == 0):
        return 0;
    
    for i in arange(400):
        Cnt = 0;
        while (N%Prime[i] == 0):
            N = N/Prime[i];
            Cnt += 1;
            Facts[i] += Prime[i]**Cnt;
    for i in arange(400):
        P = P*Facts[i];
            
    return P-N0;


def Check():
    Tot = 0;
    for i in arange(1,10001):
        if (SDivs(i) == i):
            print i,"is a perfect number, ommitted";
        else:
            if (SDivs(SDivs(i)) == i):
                print i, SDivs(i);
                Tot = Tot+i+SDivs(i);
    print "Total sum of amicable pairs is",Tot/2;
            
Generate();
Check();
