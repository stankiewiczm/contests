from numpy import *

def XOR(c1, i):
    return chr(c1 ^ i);

def Decipher(num):
    All = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]];
    This = All[num];
    Out = "";
    Spaces = 0;
    ASCII = 0;
    for n in range(len(DATA)):
        asc = DATA[n] ^ Val[This[n%3]]
        Out += chr( asc );
        ASCII += asc;
        if DATA[n]^Val[This[n%3]] == 32:
            Spaces += 1;
    if Spaces*10 > len(DATA):
        print chr(Val[This[0]]) + chr(Val[This[1]]) + chr(Val[This[2]]);
        print Out
        print ASCII
    return


Fin = open('../TXTdata/cipher1.txt','r');
[S] = Fin.readline().split();
DATA = [];      n = 0;          FREQ = [0]*256
for c in S:
    if (c == ','):
        DATA.append(n);
        n = 0;
    else:
        n = 10*n+int(c);
DATA.append(n);

for n in DATA:
    FREQ[n] += 1;

Top = sort(FREQ)[-3:len(FREQ)];
Val = [ FREQ.index(Top[0])^32, FREQ.index(Top[1])^32 , FREQ.index(Top[2])^32 ];

for q in range(6):
    Decipher(q);
