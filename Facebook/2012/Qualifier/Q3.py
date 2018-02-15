N = int(raw_input());
for i in range(N):
    S = raw_input();
    Hits = [0]*26;
    for c in S:
        if (c >= 'A') and (c < 'Z'):
            Hits[ord(c)-64] += 1;
    Bit = [ Hits[1], Hits[3]/2, Hits[5], Hits[8], Hits[11], Hits[16], Hits[18], Hits[21] ];

    print 'Case #%i: %i' % (i+1, min(Bit)) #, Bit    
    
