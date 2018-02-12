from Numeric import *

#NET = [zeros(40)]*40;

TOT = 0;        netses = [];        NETS = [];
for line in file("../TXTdata/network.txt"):
    netses.append(line);

for line in netses:
    sq = list();    N = 0;
    for ch in line:
        if (ch in ['0','1','2','3','4','5','6','7','8','9']):
            N = 10*N+int(ch);
        if (ch == ','):
            if (N == 0):
                sq.append(0);
            else:
                sq.append(N);
                TOT += N;
            N = 0;
    if (N != 0):
        sq.append(N);
    TOT += N;

    NETS.append(sq);

print NETS



Cnt = 0;
CNC = [];
for A in arange(len(NETS)):
    CNC.append([]);
    for B in arange(len(NETS)):
        CNC[A].append(0);
    CNC[A][A] = 1;

LAST = 1;           DoneL = list();     Good = True;    NEWL = 0;

while (Cnt < len(NETS)-1):
    MIN = 10000;    Mi = 0;         Mj = 0;    
    for i in arange(len(NETS)):
        for j in arange(i):
            if (NETS[i][j] < MIN) and (NETS[i][j] >= LAST):
                if (100*i+j) not in DoneL:
                    MIN = NETS[i][j];
                    Mi = i;
                    Mj = j;

    if (CNC[Mi][Mj] == 0):
        CNC[Mi][Mj] = 1;        CNC[Mj][Mi] = 1;
        print Cnt,":", Mi,Mj,MIN;
        Cnt += 1;

        DoneL.append(100*Mi+Mj)
        NEWL += MIN;

        for a in arange(len(NETS[Mi])):
            for b in arange(len(NETS[Mj])):
                if (CNC[a][Mi] == 1) and (CNC[b][Mj] == 1):
                    CNC[a][b] = 1;     CNC[b][a] = 1;
    else:
        print "Completed a failed pass", MIN, Mi, Mj
        DoneL.append(100*Mi+Mj)

print TOT/2, NEWL, TOT/2-NEWL;

