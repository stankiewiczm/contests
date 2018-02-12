T = int(raw_input());
for i in range(T):
    print "Case #%d:" % (i+1),;
    N = int(raw_input());
    List = map(int, raw_input().split());
    XOR = 0;
    for el in List:
        XOR = XOR^el;
    if (XOR == 0):
        print sum(List)-min(List);
    else:
        print "NO"
