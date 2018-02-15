import time
import random

def CountFalses(d):
    falses = 0;
    for i in range(len(d)-1, -1, -1):
        if falses < d[i]:
            falses += 1;
    return falses;

def Print(d):
    for e in d:
        print e,
    print;
    return;

def Solve(data, K):
    N = len(data);
    if CountFalses(data) == K:
        Print(data);
        return;

    data.sort();
    Min = CountFalses(data);
    if (Min == K):
        Print(data);
        return;
    data.reverse();
    Max = CountFalses(data);
    if (Max == K):
        Print(data);
        return;
    if (K < Min) or (K > Max):
        print '-1';
        return;

    it = 0;
    while (True):
        it += 1;
        if (it%2 == 0):
            random.shuffle(data);
        else:
            data.reverse();
        
        for i in range(N):
            data = data[1:] + data[:1];
            if CountFalses(data) == K:
                Print(data);
                return;

        timeUsed = (time.time()-T1);
        if (0.99 - timeUsed) < timeUsed/(it):        
            print '-1'
            return;
        

T1 = time.time();
[N, K] = map(int, raw_input().split());
data = [];
for i in range(N):
    data.append(int(raw_input()));

Solve(data, K);
