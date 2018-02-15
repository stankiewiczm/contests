def Check(word):
    if len(word) == 0:
        return 1;
    
    new = '';
    rm = 0;
    i = 0;
    while i < len(word)-1:
        if word[i] == word[i+1]:
            i += 2;
            rm += 2;
        else:
            new += word[i]
            i += 1;

    if i == len(word)-1:
        new += word[i];
        
    if rm == 0:
#        print 'failed at ',word
        return 0;

#    print 'retrying', new;
    return Check(new);
        

R = 0;                      # Ret (answer);
N = int(raw_input());
for i in range(N):
    Word = raw_input();
    nA = 0;
    nB = 0;
    for i in Word:
        if i == 'A':
            nA += 1;
        else:
            nB += 1;
    if nA%2 == nB%2 == 0:
        R += Check(Word);

print R
