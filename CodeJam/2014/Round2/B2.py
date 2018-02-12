def swap(seq, i):
    new = [];
    for q in range(len(seq)):
        if (q < i) or (q > i+1):
            new.append(seq[q]);
        if (q == i):
            new.append(seq[i+1]);
        if (q == i+1):
            new.append(seq[i]);
    return new;

    
def Valid(seq):
    for i in range(1, len(seq)-1):
        if (seq[i] < seq[i-1]) and (seq[i] < seq[i+1]):
            return i;
    return -1;
    
def Try(sequence):
#    print 'trying', sequence
    bad = Valid(sequence);
    if bad == -1:
        return 0;

    seq1 = swap(sequence, bad);
    seq2 = swap(sequence, bad-1);
    old1 = str(seq1) in StringList;
    old2 = str(seq2) in StringList;

    if (old1 and old2):
        return 1000000;
    if (old1 and not old2):
        StringList.append(str(seq2));
        return 1 + Try(seq2);
    if (old2 and not old1):
        StringList.append(str(seq1));
        return 1 + Try(seq1);
    
    StringList.append(str(seq1));
    StringList.append(str(seq2));

    return 1 + min( Try(seq1), Try(seq2) );

def Count(seq, index):
    Amax = max(seq);
    Pos = seq.index(Amax);
    curr = seq.index(max(seq));

    newseq = [];
    for e in seq:
        if e != Amax:
            newseq.append(e);

    newseq = newseq[:index] + [Amax] + newseq[index:];

    return abs(index-Pos) + Try(newseq);


T = int(raw_input());
for q in range(T):
    StringList = [];
    print "Case #%d:" % (q+1),;

    N = int(raw_input());
    Ai = map(int, raw_input().split());

#    print Try(Ai);
    Ans = [];
    for i in range(N):
        Ans.append( Count(Ai, i) );

#    print Ans;
    print min(Ans);
