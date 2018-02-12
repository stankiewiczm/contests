from Numeric import *

Prime = zeros(10001);    Prime[0] = 2;   Prime[1] = 3;

def Generate():
    N = 3;
    NPrime = 2;
    while(NPrime < 10001):
        N = N+2;
        Good = 1;
        for i in arange(min(NPrime,100)):
            if (N%Prime[i] == 0):
                Good = 0;
                break;
        if (Good == 1):
            Prime[NPrime] = N;
            NPrime = NPrime + 1;
    return 0;
            

Generate();
print Prime[10000];
