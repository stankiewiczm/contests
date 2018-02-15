from numpy import *
from time import *

# Question 1 of facebook hacker cup round 1
# Racing along a 2D grid
# S limit is 10 million, prime limit is 3200

def C(n,r):
    R = 1;
    for i in range(r):
        R = (R*(n-i))/(i+1);
    return R

t0 = time();

LIM = 10**7+1;
Best = zeros(LIM, int);
#print "allocated"
T = 1;
while T < LIM:
    i = 0;      val = 0;
    while (i <= T/2) and (val < LIM):
        val = C(T,i);
        if val == 0:
            print T, i, val
        if val < LIM:
            if (Best[val] > T) or (Best[val] == 0):
                Best[val] = T;
        i += 1;
    T += 1;

#print time()-t0;

N = int(raw_input());
for i in range(N):
    S = int(raw_input());

    a = 1;
    ans = 10**9;
    while (a*a <= S):
        if S%a == 0:
            if Best[a]+Best[S/a] < ans:
#                print a, S/a, Best[a], Best[S/a];
                ans = Best[a]+Best[S/a];
        a += 1;
    print 'Case #%i: %i' % (i+1, ans)
        
            

#    W = int(S.pop(0));
#    H = int(S.pop(0));
#    text = sum( len(word) for word in S);
#    font = int( (W*H/text+1)**0.5 )
#    while not Squeeze(S, W/font, H/font):
#        font -= 1;
#    print 'Case #%i: %i' % (i+1, font)
