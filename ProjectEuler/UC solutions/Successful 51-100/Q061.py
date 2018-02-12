from Numeric import *;

ALL = list();
for i in arange(9):
    ALL.append([]);

for i in arange(1,150):
    I = i*(i+1)/2;
    if (I > 999) and (I < 1e4) and (I% 100 > 10):
        ALL[3].append(I);

for i in arange(1,100):
    I = i*i;
    if (I > 999) and (I < 1e4) and (I% 100 > 10):
        ALL[4].append(I);

for i in arange(1,100):
    I = i*(3*i-1)/2;
    if (I > 999) and (I < 1e4) and (I% 100 > 10):
        ALL[5].append(I);

for i in arange(100):
    I = i*(2*i-1);
    if (I > 999) and (I < 1e4) and (I% 100 > 10):
        ALL[6].append(I);

for i in arange(65):
    I = i*(5*i-3)/2;
    if (I > 999) and (I < 1e4) and (I% 100 > 10):
        ALL[7].append(I);

for i in arange(60):
    I = i*(3*i-2);
    if (I > 999) and (I < 1e4) and (I% 100 > 10):
        ALL[8].append(I);
    
######################################################

def Check(a,b,c,d,e,f):
    for A in ALL[a]:
        for B in ALL[b]:
            if (A%100 == B/100):
                for C in ALL[c]:
                    if (B%100 == C/100):
                        for D in ALL[d]:
                            if (C%100 == D/100):
                                for E in ALL[e]:
                                    if (D%100 == E/100):
                                        for F in ALL[f]:
                                            if (E%100 == F/100):
                                                if (F%100 == A/100):
                                                    print A,B,C,D,E,F;
                                                    print A+B+C+D+E+F;


Check(3,4,7,8,6,5); 
