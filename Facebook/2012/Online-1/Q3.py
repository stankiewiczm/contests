from numpy import *

# Question 3 of facebook hacker cup round 1
# Compressing statii

N = int(raw_input());
MOD = 4207849484;
TODO = [];
while len(TODO) < 2*N:
    TODO += map(int, raw_input().split());
#print TODO
for i in range(1,N+1):
    M = TODO.pop(0);
    mess = str(TODO.pop(0));

    L = len(mess);
    DP = zeros(L+1, long);
    DP[0] = 1;
    for index in range(1,L+1):
        if (index-1 >= 0):
            word = mess[index-1:index];
            if word[0] != '0' and int(word) <= M:
                DP[index] += DP[index-1];
                
        if (index-2 >= 0):
            word = mess[index-2:index];
            if word[0] != '0' and int(word) <= M:
                DP[index] += DP[index-2];
        
        if (index-3 >= 0):
            word = mess[index-3:index];
            if word[0] != '0' and int(word) <= M:
                DP[index] += DP[index-3];

        DP[index] = DP[index]%MOD;
    
    print 'Case #%i: %i' % (i, DP[L])
        
