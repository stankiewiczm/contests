from Numeric import *;

WScore = 0;     Tot = list();       LEN = list();

words = [];
for line in file("../TXTdata/words.txt"):
    words.append(line);

def V(char):
    if (char == 'A'):   return 1;
    if (char == 'B'):   return 2;
    if (char == 'C'):   return 4;
    if (char == 'D'):   return 8;
    if (char == 'E'):   return 16;
    if (char == 'F'):   return 32;
    if (char == 'G'):   return 62;
    if (char == 'H'):   return 128;
    if (char == 'I'):   return 256;
    if (char == 'J'):   return 512;
    if (char == 'K'):   return 1024;
    if (char == 'L'):   return 2**11;
    if (char == 'M'):   return 2**12;
    if (char == 'N'):   return 2**13;
    if (char == 'O'):   return 2**14;
    if (char == 'P'):   return 2**15;
    if (char == 'Q'):   return 2**16;
    if (char == 'R'):   return 2**17;
    if (char == 'S'):   return 2**18;
    if (char == 'T'):   return 2**19;
    if (char == 'U'):   return 2**20;
    if (char == 'V'):   return 2**21;
    if (char == 'W'):   return 2**22;
    if (char == 'X'):   return 2**23;
    if (char == 'Y'):   return 2**24;
    if (char == 'Z'):   return 2**25;
    return 0;


def ReadIn(seq):
    Cnt = 0;    WLen = 0;   WScore = 0;
    for a in words[0]:
        if (a == ','):
            Tot.append(WScore);
            LEN.append(WLen);
            Cnt += 1;
            WScore = 0;
            WLen = 0;
        if ((a != '"') and (a != ',')):
            WScore = WScore + V(a);
            WLen += 1;
    Tot.append(WScore);
    LEN.append(WLen);


def Check(L,seq):
    Cnt = 0;    WLen = 0;   WScore = 0; S = '';     s0 = '';    s1 = '';
    for a in words[0]:
        if (a == ','):
            Cnt += 1;
            WScore = 0;
            WLen = 0;
            if (len(S) > 1):
                if (s0 == ''):
                    s0 = S;
                else:
                    s1 = S;
#                print L,S;
            S = '';
        if ((a != '"') and (a != ',')):
            WScore = WScore + V(a);
            WLen += 1;
            if Cnt in seq:
                S += a;
    return s0,s1;

def AllDif(n0):
    D = zeros(10);      N0 = n0;
    while (N0 > 0):
        D[N0%10] += 1;
        N0 = N0/10;
    return (max(D) == 1)


def Pos(char, Str):
    for i in arange(len(Str)):
        if Str[i] == char:
            return i;
    return -1;


def EqSq(n1, n2):
    N2 = n1**2;     M2 = n2**2;     S2 = 0;     S = 0;

    if len(str(N2)) != len(str(M2)):
        return False;

    for a in str(N2):
        S += int(a);
        S2 += int(a)**5;
    for b in str(M2):
        S -= int(b);
        S2 -= int(b)**5;

    if (S == 0) and (S2 == 0):
        return True
    return False;


def Verify(Digs, Str1, Str2):

    for b in NRPs[Digs]:
        Sb = str(b);
        New = 0;
        for c in Str1:
            New = New + int(Sb[Pos(c,Str1)])*10**(Digs-1-Pos(c,Str2));

        if New in NRPs[Digs]:
            print "SUCCESS!",b,New,"from",Str1,Str2;

#    print "failure :("


ReadIn([]);

NRPs = list([[],[],[],[],[],[],[],[],[],[]]);
for a in arange(4,32000):
    if (AllDif(a*a)):
        NRPs[len(str(a*a))].append(a*a);

S1 = '';        S2 = '';

for i in arange(14,4,-1):
    for j in arange(len(LEN)):
        if (LEN[j] == i):
            for k in arange(j):
                if LEN[k] == i:
                    if Tot[k] == Tot[j]:
#                        print i, LEN[j], LEN[k], Tot[j], Tot[k], j, k
                        [S1,S2] = Check(i,[j,k])
                        Verify(i,S1,S2)

#Verify (4,"CARE","RACE");

