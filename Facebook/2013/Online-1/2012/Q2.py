from numpy import *
from time import *

# Question 2 of facebook hacker cup round 1
# un-merge sorting

def Checksum(arr):
    R = 1;
    for i in arr:
        R = (31*R+i)%1000003;
    return R


def MergeMix(seq, debug):
    if len(seq) == 1:
        return [seq, debug];
    else:
        first = seq[0:len(seq)/2];
        secnd = seq[len(seq)/2:]
        [first, debug] = MergeMix(first, debug);
        [secnd, debug] = MergeMix(secnd, debug);
        seq = [];
        while (len(first)*len(secnd) != 0):
            if debug[0] == '1':
                seq += [first.pop(0)];
            else:
                seq += [secnd.pop(0)];
            debug = debug[1:]
        seq += first;
        seq += secnd;

    return [seq, debug];



T = int(raw_input());
for q in range(T):
    N = int(raw_input());
    dbg = raw_input()
    index = 0;
    
    clean = [];
    for i in range(N):
          clean += [i+1];

    messy = MergeMix(clean, dbg)[0];
    ans = [];
    for i in range(N):
        ans += [messy.index(i+1)+1];

    print 'Case #%i: %i' % (q+1, Checksum(ans))
