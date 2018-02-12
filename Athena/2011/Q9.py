from numpy import *

MOD = 10**1;
# Chameleons:
# 0 = black     1 = yellow      2 = green
# 3 = red       4 = white       5 = brown       6 = Blue

def Day(chm, day):
    Rch = [];               RET = [];       change = 0;
    for c in chm:
        Rch.append(c);

    change = Rch[(day+1)%7];
    Rch[day]       += 1000+chm[(day+1)%7]+chm[(day+2)%7]+2*chm[(day+4)%7] + chm[(day+1)%7];
    Rch[(day+5)%7] += 13+chm[(day+5)%7];
    Rch[(day+3)%7] *= 3;
    Rch[(day+1)%7] = 0;
    for e in Rch:
        RET.append(e%MOD);
#        e = e%MOD;
    return [RET, change];    

#for d in range(7):
#    Ch[t+1][d]   = Ch[t][d] + 1000+Ch[t][d+1]+Ch[t][d+2]+2*Ch[t][d+4] + Ch[t][d+1];
#    Ch[t+1][d+5] = 13+2*Ch[t][d+5];
#    Ch[t+1][d+3] *= 3;
#    Ch[t+1][1]   = 0;

Ch = [0,0,0,0,0,0,0];       change = 0
for w in range(1000):
#    print w, change
    for i in range(7):
        [Ch, change] = Day(Ch, i);
        if (i == 2):
            print w, change
