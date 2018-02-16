def clicks(r, c):
    mn = min(r, c)
    mx = max(r, c)
    print min(r, c) + ((max(r, c) - min(r, c) + 1)/2)

    for i in range(mn):
        print i, i

    if r == c:
        return;

    for x in range(mn + 1, mx - 1, 2):
        if (r < c):
            print 0, x
        else:
            print x, 0

    if (r < c):
        print 0, c-1
    else:
        print r-1, 0


T = int(raw_input())
for q in range(T):
    raw_input()
    [r, c] = map(int, raw_input().split())
    clicks(r, c)
