T = int(raw_input());
for q in range(T):
    [d, t] =  map(int, raw_input().split());
    
    print "Case #%d: %i" % (q+1, d/t);
