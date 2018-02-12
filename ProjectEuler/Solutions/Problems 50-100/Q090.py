from numpy import *

def MakeDice():
    for i in range(1024):
        L = [];     n = i;
        for j in range(10):
            if n%2 == 1:
               L.append(j);
            n /= 2;
        if len(L) == 6:
            if 6 in L and 9 not in L:
                L.append(9);
            if 9 in L and 6 not in L:
                L.append(6);
            Die.append(L);


def CheckDice(D1, D2):
    Can = zeros(100,int);
    for q in D1:
        for r in D2:
            Can[10*q+r] = 1;
            Can[10*r+q] = 1;
    return Can[1]*Can[4]*Can[9]*Can[16]*Can[25]*Can[36]*Can[49]*Can[64]*Can[81]


Die = [];       MakeDice();     ANS = 0;
for a in range(len(Die)):
    for b in range(a+1):
        ANS += CheckDice(Die[a], Die[b]);
print ANS
