from numpy import *

FILE = open("A-large.in","r");

def Solve(reds, blues):                         
    while (len(reds) > len(blues)):
        reds.remove(min(reds));
    while (len(blues) > len(reds)):
        blues.remove(min(blues));
        
    print int(sum(reds)+sum(blues)-len(reds)-len(blues));
    return;


N = int(FILE.readline());
for k in range(N):          # Each of the N cases:
    print "Case #%d:" %(k+1),
    S = int(FILE.readline());
    L = FILE.readline().split();
    Red  = [];
    Blue = [];

    for e in L:
        n = e[0:len(e)-1];
        if e[-1] == 'R':
            Red.append( int(e[:-1]) );
        else:
            Blue.append( int(e[:-1]));
    Solve(Red, Blue);
