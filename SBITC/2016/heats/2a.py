def AreSorted(List):
    for i in range(len(List)-1):
        if List[i] < List[i+1]:
            return False;
    return True;


T = int(raw_input());
for q in range(T):
    print "Case #%d:" % (q+1),
    N = int(raw_input());
    bowls = map(int, raw_input().split());

    staff = 0;
    while (not AreSorted(bowls)):
        staff += 1;
        for i in range(N-1):
            if bowls[i] < bowls[i+1]:
                tmp = bowls[i];
                bowls[i] = bowls[i+1];
                bowls[i+1] = tmp;
    print staff;
