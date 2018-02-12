from numpy import *

def Solve():
    ANS = 0L;
    DATA = map(int, raw_input().split());
    P = DATA[0];        DATA.pop(0);
    C = DATA[0];        DATA.pop(0);
    if (P == C):
        print min(DATA);
        return;
    if (C == 1):
        print sum(DATA);
        return;
    if (C == 2):
        if (2*max(DATA) > sum(DATA)):
            print (sum(DATA)-max(DATA));
            return;
        print (sum(DATA)/2);
        return;

    if 2*max(DATA) > sum(DATA):
        DATA.remove(max(DATA));
        DATA.append(sum(DATA));

    DATA = sort(DATA);
    REC = 0;
#    diff = min(DATA[0], DATA[P-1]-DATA[P-2]);
    while (P > C):
        REC += 1;
        
        DATA = sort(DATA);
#        print DATA, C;

        if (DATA[0] < DATA[P-1]-DATA[P-C]):
            Nblock = DATA[0]/C;
            ANS += Nblock * P;
            for k in range(P):
               DATA[k] -= Nblock*C;

            while (DATA[0] > 0):
                DATA=sort(DATA);
                for k in range(1,C):
                    DATA[P-k] -= 1;
                DATA[0] -= 1;
            REC = 0;

        if (DATA[0] == 0):
            ARR = DATA;     DATA = [];
            for j in range(len(ARR)):
                if ARR[j] != 0:
                    DATA.append(ARR[j]);
            P = len(DATA);
            REC = 0;

    #    print "\n ", ANS, DATA;
        if (P < C):
            break;
        
        if (DATA[0] >= DATA[P-1]-DATA[P-C]):
            block = (DATA[P-1]-DATA[P-C])/(P-C+1);
            ANS += block*(P-C+1);
            for k in range(1,C):
                DATA[P-k] -= block*(P-C+1);
            for k in range(P-C+1):
                DATA[k] -= block;
            if block > 0:
                REC = 0;

        if (DATA[0] >= DATA[P-1]-DATA[P-2]):
            diff = DATA[P-1]-DATA[P-2];
            Nblock = diff/(P-1);
            ANS += Nblock*(P-1);
            DATA[P-1] -= Nblock*(P-1);
            for k in range(P-1):
                DATA[k] -= Nblock*(C-1);
            if (Nblock > 0):
                REC = 0;


        if REC > 2:
            print sum(DATA)/C;
            return;

           
    if (P == C):
        ANS += min(DATA);#

    print ANS;
    return
    
    #    print "\n ", ANS, DATA;
        
#    P -= 1;
#    ARR = DATA;         DATA = [];
#    for j in range(1,len(ARR)):
#        DATA.append(ARR[j]);
    
    print "WOOOOOOOOOOO"
#    print P, C, P-C, DATA;
    while DATA[P-C] > 0:
        for k in range(C):
            DATA[P-k-1] -= 1;
        ANS += 1;
        DATA = sort(DATA);
#    print ANS;



T = int(raw_input());
for t in range(T):
    print "Case #%d:" % (t+1),
    Solve();    
