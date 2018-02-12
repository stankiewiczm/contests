T = int(raw_input());
for i in range(T):
    print "Case #%d:" % (i+1),;
    Data = map(int, raw_input().split());
    L = Data.pop(0)     # Up to L boosters
    t = Data.pop(0)     # time to build booster
    N = Data.pop(0)     # N stars
    C = Data.pop(0)     # C distances
#    [R, C] = map(int, raw_input().split());

    DATA = [ list(raw_input()) for i in range(R) ];
