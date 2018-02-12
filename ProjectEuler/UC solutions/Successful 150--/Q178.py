from Numeric import *

# Arrays will be in format "Min, Max, Last"

WAYS = list();  WAYS.append([]);
for t in arange(1,41):
    WAYS.append([]);
    for i in arange(1000):
        WAYS[t].append(0);

print "Beginning...."

for i in arange(1,10):
    WAYS[1][111*i] = 1;     # One digit solution

for T in arange(1,40):      # Iterations
    for V in arange(1000):
        mn = V/100;     mx = (V/10)%10;     lst = V%10;

        # Increase last digit
        if (lst != 9):
            if (lst == mx):
                WAYS[T+1][V+11] += WAYS[T][V];
            else:
                WAYS[T+1][V+1] += WAYS[T][V];

        # Decrease last digit
        if (lst != 0):
            if (lst == mn):
                WAYS[T+1][V-101] += WAYS[T][V];
            else:
                WAYS[T+1][V-1] += WAYS[T][V]

TOT = 0;
for d in arange(1,41):
    for r in arange(10):
        TOT += WAYS[d][90+r];

print "Finished", TOT, sum(WAYS[40]), 2**40
