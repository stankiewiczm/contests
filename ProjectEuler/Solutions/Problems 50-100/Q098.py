from numpy import *

DATA = [];          Anag = [];      OUT = [];
SQ = [[],[]];       q = 0;          D = 1;

while (q*q < 1e6):
    q += 1;
    if q*q >= 10**D:
        D += 1;
        SQ.append([]);
    SQ[D].append(q*q);


def CheckAn(s1, s2):
    if len(s1) != len(s2):
        return;
    AR = zeros(100, int);
    for c in s1:
        AR[ord(c)] += 1;
    for c in s2:
        AR[ord(c)] -= 1;
    if min(AR) == max(AR):
        Anag.append([s1, s2]);
    return;

def ReadIn():
    F = open('../TXTdata/words.txt');
    s = F.readline();       tmp = '';
    for i in range(len(s)):
        if s[i] == ',':
            DATA.append(tmp);
            tmp = '';
        if (s[i] >= 'A') and (s[i] <= 'Z'):
            tmp += s[i];
    DATA.append(tmp);


def NumAng(pair):
    L = len(pair[0]);       Ret = 0;
    if (L > 6):
        return

    for s in SQ[L]:
        Map = zeros(100, int);      OK = True;      M2 = zeros(10);
        num = str(s);
        for k in range(len(num)):
            Map[ ord(pair[0][k]) ] *= 10;
            Map[ ord(pair[0][k]) ] += int(num[k]);
        for k in range(len(pair[0])):
            if (M2[ int(num[k]) ] == 0):
                M2[ int(num[k]) ] = ord(pair[0][k]);
            if (M2[ int(num[k]) ] !=  ord(pair[0][k])):
                OK = False;

        if (max(Map) < 10) and OK:
            N2 = 0;
            for k in range(len(num)):
                N2 = 10*N2+Map[ ord(pair[1][k]) ];

            if N2 in SQ[L]:
#                print pair[0], s, N2, pair[1];
                Ret = max(Ret, N2, s);
    return Ret;

ReadIn();
for i in range(len(DATA)):
  for j in range(i):
    CheckAn(DATA[i], DATA[j]);

print "Found",len(Anag),'Anagrams'

for pr in Anag:
    OUT.append(NumAng(pr));
print max(OUT)
