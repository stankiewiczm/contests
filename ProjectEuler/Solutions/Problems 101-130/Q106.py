def Set(bin, N):
    R = [];
    for k in range(N):
        if (bin%2 == 1):
            R.append(k);
        bin /= 2;
    return R;

def NeedCheck(s1, s2):
    hit = [0]*N;
    for k in range(len(s1)):
        hit[s1[k]] += 1;        hit[s2[k]] += 1;
    if max(hit) >= 2:
        return 0

    c1 = False;     c2 = False; 
    for k in range(len(s1)):
        if s1[k] < s2[k]:
            c1 = True;
        if s1[k] > s2[k]:
            c2 = True;
    return int(c1 and c2);


ALL = [];       N = 12;      ANS = 0;
for k in range(N+1):
    ALL.append([]);
for k in range(2**N):
    X = Set(k,N);
    ALL[len(X)].append(X);
for L in range(N):
    for a in range(len(ALL[L])):
        for b in range(a):
            ANS += NeedCheck(ALL[L][a], ALL[L][b]);
            
print ANS
