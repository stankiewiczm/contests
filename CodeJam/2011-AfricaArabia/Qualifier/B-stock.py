from numpy import *

FILE = open("B-large.in","r");

def Solve(M, prices):
    Best = 0;
    Ans = [0,0,0];
    for i in range(11):
        purch = M/prices[i];
        cost = purch*prices[i];
        for j in range(i+1,12):
            if (purch*prices[j] > cost+Best):
                Best = purch*prices[j]-cost;
                Ans = [i,j,prices[i]];
            if (purch*prices[j] == cost+Best) and (prices[i] < Ans[2]):
                Ans = [i,j,prices[i]];
#    print 
    if Best == 0:
        print "IMPOSSIBLE"
    else:
        print Ans[0]+1, Ans[1]+1, Best;
#    print M, prices
#    for q in range (l):
#        for r in range(q+1, l):
#            if i[q]+i[r] == c:
#                print "Case #%d: %d %d" %(K+1, q+1, r+1)
#                return;


N = int(FILE.readline());
for k in range(N):          # Each of the N cases:
    print "Case #%d:" %(k+1),
    M = int(FILE.readline());
    P = map( int, FILE.readline().split() );

    Solve(M,P)
