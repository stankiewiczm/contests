def IsPretty(n):
    strn = str(n);
    return len(set(strn)) == len(strn)

Pretties = [];
for i in range(1, 10**4):
    if IsPretty(i):
        Pretties.append(i);

def TryMatch(n):
    if IsPretty(n):
#        print 1, n;
        return;

    for n1 in Pretties:
        if IsPretty(n-n1):
#            print 2, n1, n-n1;
            return 1;
    return 0;

def PrettyDown(n):
    

T = int(raw_input());
pret = salv = 0;
for q in range(T):
    raw_input();
    n = int(raw_input());
    if IsPretty(n):
#        print q, "is pretty"
        pret += 1;
    else:
        salv += TryMatch(n);
print pret, "/", T, "are pretty"
print salv, "/", T, "are salvageable"
