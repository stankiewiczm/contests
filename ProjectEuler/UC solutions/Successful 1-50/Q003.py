from Numeric import *

Prime = zeros(1000);    Prime[0] = 2;   Prime[1] = 3;

def BitBit(N):
    for i in range(len(Prime)):
        while ((N%Prime[i])==0):
            N = N/Prime[i];
            print Prime[i],"*";
    return N;


def Generate():
    N = 3;
    NPrime = 2;
    while(NPrime < 1000):
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
            

S = 0;
Generate();
BitBit(317584931803);

