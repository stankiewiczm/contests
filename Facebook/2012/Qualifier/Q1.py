def Squeeze( words, w, h ):
    row = 1;
    col = 0;
    for word in words:
        if len(word)+col <= w:
            col += len(word)+1;
        else:
            row += 1;
            col = len(word)+1;
            if col > w+1:
                return False;

    return row <= h;


N = int(raw_input());
for i in range(N):
    S = raw_input().split();
    W = int(S.pop(0));
    H = int(S.pop(0));
    text = sum( len(word) for word in S);
    font = int( (W*H/text+1)**0.5 )
    while not Squeeze(S, W/font, H/font):
        font -= 1;
    print 'Case #%i: %i' % (i+1, font)
