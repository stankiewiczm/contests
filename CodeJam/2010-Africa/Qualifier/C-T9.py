from numpy import *

Map = ['','2','22','222','3','33','333','4','44','444','5','55','555','6','66','666',
       '7','77','777','7777','8','88','888','9','99','999','9999'];

def Convert(c):
    if (c == ' '):
        return '0';
    return Map[ord(c)-96];


def SolveC(k, text):
    print "Case #%d:" % (k+1),
    Last = '&';       OUT = '';
    for a in range(len(text)-1):
        next = Convert(text[a]);
        if next[0] == Last:
            OUT += ' ';
        OUT += Convert(text[a]);
        Last = next[-1];
    print OUT;
    

FILE = open("C-large.in","r");
N = int(FILE.readline());
for k in range(N):          # Each of the N cases:
    words = FILE.readline();
    SolveC(k,words);


