def Solve( wordlist, sequence, wrong ):
    if len(wordlist) == 1:
        return 0

    Possible = False;
    while not Possible:                 #### This was my error :(
        c = sequence[0];
        sequence = sequence[1:]
        for p in wordlist:
            if c in p[0]:
                Possible = True;
        
    for pair in wordlist:
        newstr = '';
        for i in range(len(pair[0])):
            if pair[0][i] == c:
                newstr += c;
            else:
                newstr += pair[1][i]
        pair[1] = newstr

    hits = [0]*len(wordlist)
    for i in range(len(wordlist)):
        for pair in wordlist:
            if wordlist[i][1] == pair[1]:
                hits[i] += 1

    for i in range( len(wordlist)-1, -1, -1):       # Word becomes unique
        if hits[i] == 1:
            if c in wordlist[i][0]:
                score = wrong
            else:
                score = wrong+1
            Time[ Dict.index(wordlist[i][0]) ] = score;
            wordlist.pop(i);


    while len(wordlist) > 0:
        Newlist = [ wordlist.pop(0) ]
        for i in range( len(wordlist)-1, -1, -1):
            if wordlist[i][1] == Newlist[0][1]:
                Newlist.append( wordlist.pop(i) );

        if c in Newlist[0][1]:
            Solve( Newlist, sequence, wrong )
        else:
            Solve( Newlist, sequence, wrong+1 )
            

    if len(wordlist) > 0:
        print "Well this is embarrasing"
    return 1



T = int(raw_input());
for i in range(T):
    print "Case #%d:" % (i+1),;
    [N, M] = map(int, raw_input().split() );
    Dict = [];      Guess = [];
    for i in range(N):
        Dict.append( raw_input() );
    for i in range(M):
        Guess.append( raw_input() );

    WORD = [0, [], [], [], [], [], [], [], [], [], [] ];
#    Dict = sorted(Dict)
    for w in Dict:
        WORD[len(w)].append(w);

    for sequence in Guess:
        Time = [0]*len(Dict)
        for l in range(1,11):
            Sean = [];
            for w in WORD[l]:
                Sean.append( [w, '_'*len(w)] );
            if len(WORD[l]) > 1:
                Solve( Sean, sequence, 0 )

        print Dict[ Time.index(max(Time)) ],

    print 
