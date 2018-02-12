from numpy import *

FILE = open("A-small-1.in","r");

def Solve(N, K):
    LIST = zeros(N);
    for k in range(K):
        POWER = zeros(N);
        POWER[0] = 1;
        for l in range(1,N):
            POWER[l] = POWER[l-1]*LIST[l-1];
        for l in range(N):
            LIST[l] = (LIST[l]+POWER[l])%2;
    if LIST[-1] == 1:
        print "ON";
    else:
        print "OFF";
    Bin = (K/2**(N-1))%2;
#    if (Bin == 0):
#        return "OFF";
#    else:
#        return "ON";
    if (LIST[-1] != Bin):
        print List[-1], Bin


T = int(FILE.readline());
for k in range(T):          # Each of the N cases:
    print "Case #%d:" %(k+1),
    [N,K] = map( int, FILE.readline().split() );
#    print (N,K), " ", Solve(N,K);
#    print Solve(N,K);
#    if (k%100 == 99):
#        print k+1;
    Solve(N,K);
