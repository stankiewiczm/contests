def maxVal(w):
    Hit = [0]*26;
    for c in w:
        if 'A' <= c <= 'Z':
            Hit[ord(c)-65] += 1;
    Hit.sort();
    Score = 0;
    for i in range(26):
        Score += (i+1)*Hit[i];
    return Score
    

T = int(raw_input());
for case in range(1, T+1):
    print 'Case #%i: %i' % (case, maxVal(raw_input().upper()))
