T = int(raw_input());
for q in range(T):
    [word, K] = raw_input().split();
    K = int(K);

    shift = (-K) % len(word)
    shifted = word[shift:] + word[:shift];

    final = '';
    for c in shifted:
        final += chr( (ord(c) + K - 65)%26 + 65 )
        
    print "Case #%d:" % (q+1),;
    print final
