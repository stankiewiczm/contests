from numpy import *

def Solve():
    [N,T] = map(int, raw_input().split());
    E = int(raw_input());

    NEED = [0]*(N+1);
    CARS = [];
    for k in range(N+1):
        CARS.append([]);
    
    for e in range(E):
        # Next employee
        [h,p] = map(int, raw_input().split());
        if ((h != T)):
            NEED[h] += 1;
            CARS[h].append(p);

    for k in range(1,N+1):
        if (sum(CARS[k]) < NEED[k]):
            print "IMPOSSIBLE";
#            print CARS[k], NEED[k]
            return;

    for k in range(1,N+1):
        count = 0;
        while (NEED[k] > 0):
            mx = max(CARS[k]);
            NEED[k] -= mx;
            count += 1;
            CARS[k].remove(mx);
        print count,
    print "";
    return


T = int(raw_input());
for t in range(1,T+1):
    print "Case #%d:" %t,
    Solve();
