from Numeric import *

DIG = 100;
TOT = 0;

Ways = [];
for a in arange(DIG+1):
    Ways.append([]);
    for b in arange(3):
        Ways[a].append([]);
        for c in arange(2):
            Ways[a][b].append(0);

Ways[0][0][0] = 1;

for Day in arange(1,DIG+1):
    # Add a come to class
    Ways[Day][0][0] = Ways[Day-1][0][0] + Ways[Day-1][1][0] + Ways[Day-1][2][0];
    Ways[Day][0][1] = Ways[Day-1][0][1] + Ways[Day-1][1][1] + Ways[Day-1][2][1];

    # Add a coming in late
    Ways[Day][0][1] += Ways[Day-1][0][0] + Ways[Day-1][1][0] + Ways[Day-1][2][0];

    # Add missing a day
    Ways[Day][1][0] = Ways[Day-1][0][0];    Ways[Day][1][1] = Ways[Day-1][0][1];
    Ways[Day][2][0] = Ways[Day-1][1][0];    Ways[Day][2][1] = Ways[Day-1][1][1];


for q in arange(1,DIG+1):
    TOT =  Ways[q][0][0] + Ways[q][1][0] + Ways[q][2][0]
    TOT += Ways[q][0][1] + Ways[q][1][1] + Ways[q][2][1]

    print q, TOT
