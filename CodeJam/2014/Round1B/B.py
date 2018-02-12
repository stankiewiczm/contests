def BruteSolve(a,b,k):
    Ans = 0;
    for i in range(a):
        for j in range(b):
            if i&j < k:
                Ans += 1;
    return Ans;

T = int(raw_input());
for q in range(T):
    print "Case #%d:" % (q+1),;

    [A,B,K] = map(int, raw_input().split());
    print BruteSolve(A,B,K);
        
