T = int(raw_input());
for q in range(T):
    N = int(raw_input());
    Con = [];
    for i in range(N):
        routes = [];
        idx = 0;
        for c in list(raw_input()):
            if c == 'Y':
                routes.append(idx);
            idx += 1;
        Con.append(routes)

    seq = [0];
    for i in range(1, N):
        if i in Con[seq[-1]]:
            seq = seq + [i];
        elif (seq[0] in Con[i]):
            seq = [i] + seq;
        else:
            j = 0;
            found = False;
            while (j < len(seq)-1) and (not found):
                if (i in Con[seq[j]] and seq[j+1] in Con[i]):
                    seq = seq[:j+1] + [i] + seq[j+1:];
                    found = True;
                j += 1;

    ans = str(seq[0]+1);
    for i in range(1, len(seq)):
        ans += ' ' + str(seq[i]+1);
                
    print "Case #%d: %s" % (q+1, ans);  
