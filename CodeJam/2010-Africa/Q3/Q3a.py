from numpy import *

def Solve():
    ANS = 0;
    DATA = map(int, raw_input().split());
    P = DATA[0];        DATA.pop(0);
    C = DATA[0];        DATA.pop(0);
    DATA = sort(DATA, -1);
#    print P, C, P-C, DATA;
    while DATA[P-C] > 0:
        for k in range(C):
            DATA[P-k-1] -= 1;
        ANS += 1;
        DATA = sort(DATA);
    print ANS;



T = int(raw_input());
for t in range(T):
    print "Case #%d:" % (t+1),
    Solve();    
