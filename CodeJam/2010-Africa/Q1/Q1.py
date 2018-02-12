from numpy import *


T = int(raw_input());
for t in range(1,T+1):
    G = int(raw_input());
    Glist = map(int,raw_input().split());
    LIST = [];
    for g in Glist:
        if g not in LIST:
            LIST.append(g);
        else:
            for k in range(len(LIST)):
                if LIST[k] == g:
                    LIST.pop(k);
                    break;
    print "Case #%d: %d" % (t, LIST[0]);

