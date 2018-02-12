from Numeric import *

CC = zeros(40);     
SS = zeros(40);

for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    for f in range(4):
                        for g in range(4):
                            for h in range(4):
                                for i in range(4):
                                    CC[a+b+c+d+e+f+g+h+i+9] += 1;

for a in range(6):
    for b in range(6):
        for c in range(6):
            for d in range(6):
                for e in range(6):
                    for f in range(6):
                        SS[a+b+c+d+e+f+6] += 1;

EVT = 0;

for Tot in range(40):
    FreqS = SS[Tot];
    FreqC = 0;
    for i in range(Tot+1,40):
        FreqC += CC[i];
    EVT += FreqC*FreqS;

print EVT, sum(CC)*sum(SS), float(EVT)/(sum(CC)*sum(SS))
