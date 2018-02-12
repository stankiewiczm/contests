def Sum(L):
    R = ''
    for i in L:
        R += i;
    return R;


def Possible(n, s0):
    BS = Binary(n);
    if len(BS) != len(s0):
        return False;
    for i in range(len(s0)):
        c = s0[i];
        if c != '?' and (c != BS[i]):
            return False;
    return True;

        
def Binary(n):
    B = [];
    while (n > 0):
        if n%2 == 0:
            B.append('0');
        else:
            B.append('1');
        n /= 2;
    B.reverse();
    return B;


def Ans(L):
    V = 0;
    for c in L:
        V = 2*V+int(c);
    if int(V**0.5)**2 == V:
        print Sum(Binary(V))
        Done = True;
        return True;

 
def MinMax(parL):
    Min = 0L;       Max = 0L;
    for c in parL:
        if c == '?':
            Min = 2*Min;
            Max = 2*Max + 1;
        else:
            Min = 2*Min+int(c);
            Max = 2*Max+int(c);
    return [int(Min**0.5), int(Max**0.5)]


def Brute(s):
    l = list(s);
    Qm = 0
    for c in l:
        if c == '?':
            Qm += 1;

    for n in range(2**Qm):
        Map = [];
        for i in range(Qm):
            Map.append( (n/2**i)%2 );
        print n

    Val = 0;
    P2 = 1;
    MapV = [];
    for i in range(len(l)-1,-1,-1):
        if l[i] == '?':
            MapV.append(P2);
        else:
            Val += P2;
        P2 *= 2;

    for m in Map:
        V2 = 0;
        for c in range(len(m)):
            V2 += m[c]*Val[c];
            print V2, Val, V2+Val


Done = False;
T = int(raw_input());
for i in range(T):
    print "Case #%d:" % (i+1),
    S = list(raw_input().split()[0]);
        
    BigList = [];
    Start = S[0:16];
    Qm = 0
    for c in Start:
        if c == '?':
            Qm += 1;

    for n in range(2**Qm):
        Map = [];
        for i in range(Qm):
            Map.append( (n/2**i)%2 );
        im = 0;
        NewS = [];
        for i in range(len(S)):
            if (S[i] == '?') and (im < Qm):
                NewS.append(str(Map[im]));
                im += 1;
            else:
                NewS.append(S[i]);

        BigList.append(NewS);
    
    Done = False;
    for l in BigList:
        [M1, M2] = MinMax(l);

        for i in range(M1, M2+1):
            if Possible(i*i, l):
                Done = True
                print Sum(Binary(i*i))
