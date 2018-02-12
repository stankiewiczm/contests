from Numeric import *

# Arrays will be in format "Min, Max, Last"

WAYS = list();  WAYS.append([]);
for t in arange(1,41):
    WAYS.append([]);
    for i in arange(1000):
        WAYS[t].append(0);

print "Beginning...."

for i in arange(1,10):
    WAYS[1][111*i] = 1;

for T in arange(2,41):      # Iterations
    for mn in arange(10):
        for mx in arange(10):
            for lst in arange(10):
                if (mx >= lst >= mn):
                    V = 100*mn+10*mx+lst;

                    WAYS[T][V] = 0;
                    
                    if (lst != 0) and (lst != 9):
                        WAYS[T][V] += WAYS[T-1][V-1];
                        WAYS[T][V] += WAYS[T-1][V+1];

                        if (mn == lst):
                            WAYS[T][V] += WAYS[T-1][V+101]
#                            WAYS[T][V] += WAYS[T-1][V-101]

                        if (mx == lst):
#                            WAYS[T][V] += WAYS[T-1][V+11]
                            WAYS[T][V] += WAYS[T-1][V-11]

                    if (lst == 0):
                        WAYS[T][V] = WAYS[T-1][V+1];
                        if (mn == lst):
                            WAYS[T][V] += WAYS[T-1][V+101]
                        if (mx == lst):
                            WAYS[T][V] += WAYS[T-1][V+11]

                    if (lst == 9):
                        WAYS[T][V] = WAYS[T-1][V-1];
                        if (mn == lst):
                            WAYS[T][V] += WAYS[T-1][V-101]
                        if (mx == lst):
                            WAYS[T][V] += WAYS[T-1][V-11]

#    print "Completed ",T, WAYS[T][455]

TOT = 0;
for k in arange(4,41):
    for r in arange(10):
        TOT += WAYS[k][90+r];
    print k, TOT

print "Finished", TOT, sum(WAYS[40]), 2**40
