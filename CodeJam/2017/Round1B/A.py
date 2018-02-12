T = int(raw_input());
for q in range(T):
    [D, N] = map(int, raw_input().split());
    speed = [];
    for i in range(N):
        [Ki, Si] = map(int, raw_input().split());
        speed.append( D*(Si+0.)/(D-Ki) );

    print "Case #%d:" % (q+1),
    print "%.6f" % min(speed)

