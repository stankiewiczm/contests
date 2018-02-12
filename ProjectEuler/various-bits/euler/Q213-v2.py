from Numeric import *

LATT = 30;  TIME = 50;      LARGE = 4**50*3**25;

PROB = [];
for t in arange(TIME+1):
    PROB.append([]);
    for row in arange(LATT):
        PROB[t].append([]);
        for col in arange(LATT):
            PROB[t][row].append(0L);

def Print(T):
    for a in arange(LATT):
        for b in arange(LATT):
            print PROB[0][T][a][b],
        print " ";
    return 

print "start"

FIN = [];
for a in arange(LATT*LATT):
    FIN.append(zeros(LATT*LATT, Float));

for Flea in arange(LATT*LATT):
    for t in arange(TIME+1):
        for row in arange(LATT):
            for col in arange(LATT):
                PROB[t][row][col] = 0L;
    PROB[0][Flea/LATT][Flea%LATT] = LARGE;
    
    for t in arange(TIME):
        for row in arange(LATT):
            for col in arange(LATT):
                V = PROB[t][row][col];
                if (row != 0) and (row != LATT-1) and (col != 0) and (col != LATT-1):
                    PROB[t+1][row+1][col] += V/4.;
                    PROB[t+1][row-1][col] += V/4.;
                    PROB[t+1][row][col+1] += V/4.;
                    PROB[t+1][row][col-1] += V/4.;
                if (row == 0) and ((col != 0) and (col != LATT-1)):
                    PROB[t+1][row+1][col] += V/3;
                    PROB[t+1][row][col+1] += V/3;
                    PROB[t+1][row][col-1] += V/3;
                if (row == LATT-1) and ((col != 0) and (col != LATT-1)):
                    PROB[t+1][row-1][col] += V/3;
                    PROB[t+1][row][col+1] += V/3;
                    PROB[t+1][row][col-1] += V/3;
                if (col == 0) and ((row != 0) and (row != LATT-1)):
                    PROB[t+1][row-1][col] += V/3;
                    PROB[t+1][row+1][col] += V/3;
                    PROB[t+1][row][col+1] += V/3;
                if (col == LATT-1) and ((row != 0) and (row != LATT-1)):
                    PROB[t+1][row-1][col] += V/3;
                    PROB[t+1][row+1][col] += V/3;
                    PROB[t+1][row][col-1] += V/3;
                if (row == 0) and (col == 0):
                    PROB[t+1][row][col+1] += V/2;
                    PROB[t+1][row+1][col] += V/2;
                if (row == 0) and (col == LATT-1):
                    PROB[t+1][row][col-1] += V/2;
                    PROB[t+1][row+1][col] += V/2;
                if (row == LATT-1) and (col == 0):
                    PROB[t+1][row][col+1] += V/2;
                    PROB[t+1][row-1][col] += V/2;
                if (row == LATT-1) and (col == LATT-1):
                    PROB[t+1][row][col-1] += V/2;
                    PROB[t+1][row-1][col] += V/2;

    for a in arange(LATT):
        for b in arange(LATT):
            FIN[Flea][LATT*a+b] = PROB[TIME][a][b];

print "done"

P = ones(LATT*LATT, Float);
for a in arange(LATT*LATT):
    P[a] = 1.;
    for b in arange(LATT*LATT):
        P[a] = P[a]*(1-float(FIN[a][b])/LARGE);
print LATT, sum(P), sum(P)/(LATT*LATT);
