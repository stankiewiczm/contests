def IsPretty(n):
    strn = str(n);
    return len(set(strn)) == len(strn)

Pretties = [];
for i in range(1, 10**5):
    if IsPretty(i):
        Pretties.append(i);

def TryMatch(n):
    if IsPretty(n):
        print 1, n;
        return;

    for n1 in Pretties:
        if (n-n1) in Pretties:
            print 2, n1, n-n1;
            return;
        
        if 2*n1 > n:
            print "SHIT";
            return;

T = int(raw_input());
pret = 0;
for q in range(T):
    raw_input();
    n = int(raw_input());
    TryMatch(n);
