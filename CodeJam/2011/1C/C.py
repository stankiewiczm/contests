T = int(raw_input());
for i in range(T):
    print "Case #%d:" % (i+1),;
    [N, L, H] = map( int, raw_input().split())
    Orch = sorted(map( int, raw_input().split() ))

    Done = False
    for f in range(L, H+1):
        AllGood = True;
        if not Done:
            for p in Orch:
                if (f%p != 0) and (p%f != 0):
                    AllGood = False;
            if AllGood:
                print f;
                Done = True
    if not Done:
        print "NO"
