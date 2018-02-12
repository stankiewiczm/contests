def SolvePrimary(R, Y, B):
    if 2*max(R, Y, B) > R+Y+B:
        return "IMPOSSIBLE";
    if max(R, Y, B) == 0:
        return '';
    
    ans = '';
    if max(R, Y, B) == R:
        ans = 'R';
    elif max(R, Y, B) == Y:
        ans = 'Y';
    else:
        ans = 'B';

    while (R+Y+B > 1):
        if ans[-1] == 'R':
            if (Y > B):
                nxt = 'Y';
                Y -= 1;
            else:
                nxt = 'B';
                B -= 1
        if ans[-1] == 'Y':
            if (R > B):
                nxt = 'R';
                R -= 1;
            else:
                nxt = 'B';
                B -= 1
        if ans[-1] == 'B':
            if (Y > R):
                nxt = 'Y';
                Y -= 1;
            else:
                nxt = 'R';
                R -= 1

        ans += nxt;
        
    return ans;


T = int(raw_input());
for q in range(T):
    # Orange = Red + Yellow
    # Green = Yellow + Blue
    # Violet = Blue + Red
                
    [N, R, O, Y, G, B, V] = map(int, raw_input().split())

    red = R + O + V
    yellow = Y + O + G 
    blue = B + G + V

    print "Case #%d:" % (q+1),
    print SolvePrimary(R, Y, B);
    
