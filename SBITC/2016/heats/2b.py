T = int(raw_input());
for q in range(T):
    print "Case #%d:" % (q+1),
    N = int(raw_input());
    bowls = map(int, raw_input().split());

    staff = 0;
    for i in range(N):
        staff = max(staff, i + bowls[i] - N);

    print staff;
