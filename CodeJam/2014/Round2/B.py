def AC(s):
    Ret = 0;
    while len(s) > 0:
        Ret += s.index(min(s));
        s.remove(min(s));
    return Ret

def Count(seq, index):
    Amax = max(seq);
    Pos = seq.index(Amax);
    curr = seq.index(max(seq));

    newseq = [];
    for e in seq:
        if e != Amax:
            newseq.append(e);

    parta = newseq[:index];
    partb = newseq[index:];
    partb.reverse();

    return abs(index-Pos) + AC(parta) + AC(partb);


T = int(raw_input());
for q in range(T):
    print "Case #%d:" % (q+1),;

    N = int(raw_input());
    Ai = map(int, raw_input().split());

    Ans = [];
    for i in range(N):
        Ans.append( Count(Ai, i) );

    print Ans;
#    print min(Ans);
